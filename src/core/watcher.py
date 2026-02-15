"""File watcher, filtering, content-hash diffing, and incremental pipeline.

Components:
- FileFilter: Combines .gitignore + hardcoded ignores + .codebasegraphignore
- ContentHasher: SHA-256 based content-hash diffing to skip unchanged files
- IncrementalPipeline: Re-parse changed files, rebuild graph, re-serialize
- CodebaseWatcher: watchfiles-based file change detection
"""

from __future__ import annotations

import hashlib
import logging
import os
import tempfile
import threading
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path

import pathspec
import watchfiles

from src.core.graph import (
    Hierarchy,
    Module,
    ModuleClusterer,
    detect_cross_module_deps,
    extract_hierarchies,
)
from src.core.manifest import Dependency, ManifestParser
from src.core.parser import SUPPORTED_EXTENSIONS, CodebaseParser, Symbol
from src.core.writer import CodebaseMeta, CodebaseWriter

logger = logging.getLogger(__name__)


# ── Hardcoded ignore directories ───────────────────────────────────

HARDCODED_IGNORES: frozenset[str] = frozenset(
    {
        "node_modules",
        "dist",
        "target",
        ".venv",
        "__pycache__",
        "build",
        "out",
        ".next",
        "coverage",
        ".git",
    }
)


# ── FileFilter ─────────────────────────────────────────────────────


class FileFilter:
    """Combines .gitignore + hardcoded ignores + .codebasegraphignore.

    Used by both the watcher and initial full-directory parse to decide
    which files to include or exclude.

    Usage:
        filt = FileFilter(project_root="/path/to/repo")
        if filt.should_include("src/main.py"):
            # process file
    """

    def __init__(self, project_root: str | Path) -> None:
        self._root = Path(project_root).resolve()
        self._gitignore_spec = self._load_spec(".gitignore")
        self._custom_spec = self._load_spec(".codebasegraphignore")

    def _load_spec(self, filename: str) -> pathspec.PathSpec | None:
        """Load a gitignore-style spec file from the project root."""
        ignore_file = self._root / filename
        if not ignore_file.is_file():
            return None
        try:
            text = ignore_file.read_text(encoding="utf-8", errors="replace")
            lines = text.splitlines()
            return pathspec.PathSpec.from_lines("gitignore", lines)
        except OSError:
            return None

    def should_include(self, rel_path: str) -> bool:
        """Check if a file (relative to project root) should be included.

        Returns False if the file matches any ignore pattern:
        1. Hardcoded directory ignores (node_modules, .git, etc.)
        2. .gitignore patterns
        3. .codebasegraphignore patterns

        Args:
            rel_path: Relative path from the project root (forward slashes).

        Returns:
            True if the file should be processed.
        """
        # Normalize to forward slashes (handles Windows backslashes too)
        rel_path = rel_path.replace("\\", "/")

        # Check hardcoded directory ignores — any path component matches
        parts = rel_path.split("/")
        for part in parts:
            if part in HARDCODED_IGNORES:
                return False

        # Check .gitignore patterns
        if self._gitignore_spec and self._gitignore_spec.match_file(rel_path):
            return False

        # Check .codebasegraphignore patterns
        if self._custom_spec and self._custom_spec.match_file(rel_path):
            return False

        return True

    def should_include_abs(self, abs_path: str | Path) -> bool:
        """Check if an absolute path should be included.

        Converts to relative path first, then delegates to should_include.
        """
        try:
            rel = Path(abs_path).resolve().relative_to(self._root)
            return self.should_include(str(rel))
        except ValueError:
            # Path is outside project root — exclude
            return False


# ── Content Hash Diffing ───────────────────────────────────────────


def _hash_file(path: Path) -> str:
    """Compute SHA-256 hash of file content."""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while True:
                chunk = f.read(65536)
                if not chunk:
                    break
                h.update(chunk)
    except OSError:
        return ""
    return h.hexdigest()


class ContentHasher:
    """Tracks file content hashes to skip re-parsing unchanged files.

    Maintains a dict mapping relative file paths to their SHA-256 hash.
    When a file change event arrives, computes the new hash and compares
    to the stored one — returns True only if the content actually changed.

    Usage:
        hasher = ContentHasher(project_root="/path/to/repo")
        hasher.compute_initial(["src/main.py", "src/utils.py"])
        changed = hasher.check_and_update("src/main.py")  # True if content changed
    """

    def __init__(self, project_root: str | Path) -> None:
        self._root = Path(project_root).resolve()
        self._hashes: dict[str, str] = {}

    @property
    def hashes(self) -> dict[str, str]:
        """Read-only access to the current hash map."""
        return dict(self._hashes)

    def compute_initial(self, rel_paths: list[str]) -> None:
        """Compute and store hashes for a list of files."""
        for rel_path in rel_paths:
            full_path = self._root / rel_path
            self._hashes[rel_path] = _hash_file(full_path)

    def check_and_update(self, rel_path: str) -> bool:
        """Check if a file's content has changed since last hash.

        Computes the current hash and compares with the stored one.
        If changed (or new file), updates the stored hash and returns True.
        If unchanged, returns False.

        Args:
            rel_path: Relative path from project root.

        Returns:
            True if content changed, False if unchanged.
        """
        full_path = self._root / rel_path
        new_hash = _hash_file(full_path)

        if not new_hash:
            # File was deleted or unreadable — treat as changed
            old = self._hashes.pop(rel_path, None)
            return old is not None

        old_hash = self._hashes.get(rel_path)
        self._hashes[rel_path] = new_hash
        return new_hash != old_hash

    def remove(self, rel_path: str) -> bool:
        """Remove a file from the hash tracker.

        Returns True if the file was previously tracked.
        """
        return self._hashes.pop(rel_path, None) is not None


# ── Incremental Pipeline ──────────────────────────────────────────


@dataclass
class PipelineState:
    """Full in-memory state for the incremental pipeline.

    Holds all parsed symbols, clustered modules, hierarchies, and
    dependencies so that incremental updates can rebuild only what changed.
    """

    symbols_by_file: dict[str, list[Symbol]] = field(default_factory=dict)
    modules: list[Module] = field(default_factory=list)
    hierarchies: list[Hierarchy] = field(default_factory=list)
    dependencies: list[Dependency] = field(default_factory=list)
    metadata: CodebaseMeta | None = None


class IncrementalPipeline:
    """Handles incremental re-parsing and .codebase.md regeneration.

    Maintains full state in memory. On file changes:
    1. Re-parse only changed files
    2. Rebuild modules (full re-cluster — fast since it's just dict grouping)
    3. Re-extract hierarchies
    4. Re-serialize the full .codebase.md
    5. Write atomically (temp file + rename)

    Usage:
        pipeline = IncrementalPipeline(
            project_root="/path/to/repo",
            output_path="/path/to/repo/.codebase.md",
        )
        pipeline.full_index()  # initial parse
        pipeline.update_files(["src/main.py"])  # incremental update
    """

    def __init__(
        self,
        project_root: str | Path,
        output_path: str | Path | None = None,
        project_name: str | None = None,
        file_filter: FileFilter | None = None,
    ) -> None:
        self._root = Path(project_root).resolve()
        self._output = Path(output_path) if output_path else self._root / ".codebase.md"
        self._project_name = project_name or self._root.name
        self._parser = CodebaseParser(self._root)
        self._clusterer = ModuleClusterer()
        self._manifest_parser = ManifestParser()
        self._writer = CodebaseWriter()
        self._filter = file_filter or FileFilter(self._root)
        self.state = PipelineState()

    def full_index(self) -> str:
        """Run a full parse of the entire project.

        Returns the generated .codebase.md content.
        """
        # Parse all files
        raw_symbols = self._parser.parse_directory()

        # Filter through our file filter
        symbols_by_file: dict[str, list[Symbol]] = {}
        for file_path, syms in raw_symbols.items():
            if self._filter.should_include(file_path):
                symbols_by_file[file_path] = syms

        self.state.symbols_by_file = symbols_by_file

        # Rebuild graph from symbols
        return self._rebuild_and_write()

    def update_files(self, changed_files: list[str]) -> str:
        """Incrementally update after file changes.

        Re-parses only the specified files, updates state,
        and regenerates .codebase.md.

        Args:
            changed_files: List of relative file paths that changed.

        Returns:
            The generated .codebase.md content.
        """
        for rel_path in changed_files:
            if not self._filter.should_include(rel_path):
                # File is ignored — remove from state if present
                self.state.symbols_by_file.pop(rel_path, None)
                continue

            # Re-parse just this file
            new_symbols = self._parser.parse_file(rel_path)
            if new_symbols:
                self.state.symbols_by_file[rel_path] = new_symbols
            else:
                # File was deleted or has no symbols
                self.state.symbols_by_file.pop(rel_path, None)

        return self._rebuild_and_write()

    def remove_files(self, deleted_files: list[str]) -> str:
        """Handle file deletions.

        Removes symbols for deleted files and regenerates.

        Args:
            deleted_files: List of relative file paths that were deleted.

        Returns:
            The generated .codebase.md content.
        """
        for rel_path in deleted_files:
            self.state.symbols_by_file.pop(rel_path, None)

        return self._rebuild_and_write()

    def _rebuild_and_write(self) -> str:
        """Rebuild the full graph from current state and write output.

        This is called after any state change (full index or incremental).
        Re-clustering and re-serialization are fast operations, so we always
        rebuild the full graph rather than trying to patch it.
        """
        # Detect languages from file extensions
        languages = self._detect_languages()

        # Cluster into modules
        self.state.modules = self._clusterer.cluster(self.state.symbols_by_file)

        # Extract hierarchies
        self.state.hierarchies = extract_hierarchies(self.state.symbols_by_file)

        # Detect cross-module dependencies
        detect_cross_module_deps(self.state.modules, str(self._root))

        # Parse manifest for external dependencies
        self.state.dependencies = self._manifest_parser.parse(self._root)

        # Build metadata
        self.state.metadata = CodebaseMeta(
            name=self._project_name,
            languages=languages,
        )

        # Serialize
        content = self._writer.write(
            modules=self.state.modules,
            hierarchies=self.state.hierarchies,
            dependencies=self.state.dependencies,
            metadata=self.state.metadata,
        )

        # Write atomically
        self._write_atomic(content)

        return content

    def _detect_languages(self) -> list[str]:
        """Detect programming languages from file extensions in the index."""
        extensions: set[str] = set()
        for file_path in self.state.symbols_by_file:
            ext = Path(file_path).suffix
            extensions.add(ext)

        lang_map = {
            ".py": "python",
            ".ts": "typescript",
            ".tsx": "typescript",
            ".js": "javascript",
            ".jsx": "javascript",
        }

        languages = sorted(
            {lang_map.get(ext, ext) for ext in extensions if ext in lang_map}
        )
        return languages

    def _write_atomic(self, content: str) -> None:
        """Write content to the output file atomically.

        Writes to a temp file in the same directory, then renames.
        This prevents partial reads if the watcher or another process
        reads .codebase.md while we're writing it.
        """
        output_dir = self._output.parent
        output_dir.mkdir(parents=True, exist_ok=True)

        try:
            fd, tmp_path = tempfile.mkstemp(
                dir=str(output_dir),
                prefix=".codebase_",
                suffix=".md.tmp",
            )
            try:
                with os.fdopen(fd, "w", encoding="utf-8") as f:
                    f.write(content)
                # Atomic rename on POSIX (same filesystem)
                os.replace(tmp_path, str(self._output))
            except Exception:
                # Clean up temp file on failure
                try:
                    os.unlink(tmp_path)
                except OSError:
                    pass
                raise
        except OSError as e:
            logger.error("Failed to write %s: %s", self._output, e)
            raise


# ── CodebaseWatcher ────────────────────────────────────────────────


class CodebaseWatcher:
    """Watches a directory for file changes and triggers incremental updates.

    Uses watchfiles (Rust-backed, cross-platform) for efficient change
    detection. Integrates with FileFilter for ignore patterns and
    ContentHasher for content-based deduplication.

    Usage:
        watcher = CodebaseWatcher(
            project_root="/path/to/repo",
            on_change=my_callback,  # called with list of changed rel paths
        )
        watcher.start()  # blocks, or use start_background()
        # ...
        watcher.stop()
    """

    def __init__(
        self,
        project_root: str | Path,
        on_change: Callable[[list[str]], None] | None = None,
        file_filter: FileFilter | None = None,
    ) -> None:
        self._root = Path(project_root).resolve()
        self._on_change = on_change
        self._filter = file_filter or FileFilter(self._root)
        self._hasher = ContentHasher(self._root)
        self._stop_event = threading.Event()
        self._thread: threading.Thread | None = None

    @property
    def hasher(self) -> ContentHasher:
        """Access the content hasher (for initial hash setup)."""
        return self._hasher

    def watch(self, on_change: Callable[[list[str]], None] | None = None) -> None:
        """Start watching for file changes. Blocks until stop() is called.

        Args:
            on_change: Optional callback override. If provided, replaces
                       the callback set in __init__.
        """
        callback = on_change or self._on_change
        if callback is None:
            raise ValueError("on_change callback is required")

        for changes in watchfiles.watch(
            str(self._root),
            stop_event=self._stop_event,
            watch_filter=self._make_filter(),
        ):
            if self._stop_event.is_set():
                break

            # Process changes: filter + content-hash dedup
            changed_files: list[str] = []
            for change_type, abs_path in changes:
                try:
                    rel_path = str(Path(abs_path).resolve().relative_to(self._root))
                except ValueError:
                    continue

                # Normalize to forward slashes
                rel_path = rel_path.replace(os.sep, "/")

                # Apply file filter
                if not self._filter.should_include(rel_path):
                    continue

                # Only track supported extensions
                if Path(rel_path).suffix not in SUPPORTED_EXTENSIONS:
                    continue

                # Content-hash dedup
                if change_type == watchfiles.Change.deleted:
                    self._hasher.remove(rel_path)
                    changed_files.append(rel_path)
                else:
                    if self._hasher.check_and_update(rel_path):
                        changed_files.append(rel_path)

            if changed_files:
                callback(changed_files)

    def stop(self) -> None:
        """Stop watching for file changes."""
        self._stop_event.set()

    def start_background(
        self,
        on_change: Callable[[list[str]], None] | None = None,
    ) -> None:
        """Start watching in a background thread."""
        callback = on_change or self._on_change
        self._thread = threading.Thread(
            target=self.watch,
            args=(callback,),
            daemon=True,
        )
        self._thread.start()

    def _make_filter(self) -> watchfiles.DefaultFilter | None:
        """Create a watchfiles filter for efficient OS-level filtering.

        Returns a DefaultFilter that skips common ignored directories at
        the OS level (before events even reach Python).
        """
        # watchfiles.DefaultFilter already ignores common dirs like .git, __pycache__
        # We add our custom ignored directories
        return watchfiles.DefaultFilter(
            ignore_dirs=tuple(HARDCODED_IGNORES),
        )
