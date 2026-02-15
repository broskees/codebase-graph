"""Tests for file watcher, filtering, content-hash diffing, and incremental pipeline."""

from __future__ import annotations

import os
import time
from pathlib import Path

import pytest

from src.core.parser import Symbol
from src.core.watcher import (
    HARDCODED_IGNORES,
    CodebaseWatcher,
    ContentHasher,
    FileFilter,
    IncrementalPipeline,
    PipelineState,
    _hash_file,
)


# ── Helpers ────────────────────────────────────────────────────────


def _sym(
    name: str,
    kind: str = "fn",
    file: str = "src/core/main.py",
    line: int = 10,
    signature: str = "",
) -> Symbol:
    """Shorthand to create a Symbol for testing."""
    return Symbol(
        name=name,
        kind=kind,
        file=file,
        line=line,
        end_line=line + 5,
        signature=signature or f"def {name}():",
        fqn=f"{file.rsplit('.', 1)[0]}::{name}",
    )


def _make_gitignore(tmp_path: Path, lines: list[str]) -> None:
    """Write a .gitignore file in the given directory."""
    (tmp_path / ".gitignore").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _make_codebasegraphignore(tmp_path: Path, lines: list[str]) -> None:
    """Write a .codebasegraphignore file in the given directory."""
    (tmp_path / ".codebasegraphignore").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


# ═══════════════════════════════════════════════════════════════════
# FileFilter Tests
# ═══════════════════════════════════════════════════════════════════


class TestFileFilterHardcoded:
    """Tests for hardcoded ignore patterns."""

    def test_node_modules_excluded(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert not filt.should_include("node_modules/express/index.js")

    def test_dist_excluded(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert not filt.should_include("dist/bundle.js")

    def test_pycache_excluded(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert not filt.should_include("src/__pycache__/main.cpython-311.pyc")

    def test_dot_git_excluded(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert not filt.should_include(".git/objects/abc123")

    def test_venv_excluded(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert not filt.should_include(".venv/lib/python3.11/site-packages/foo.py")

    def test_build_excluded(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert not filt.should_include("build/output.js")

    def test_target_excluded(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert not filt.should_include("target/debug/binary")

    def test_next_excluded(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert not filt.should_include(".next/static/chunks/main.js")

    def test_coverage_excluded(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert not filt.should_include("coverage/lcov.info")

    def test_out_excluded(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert not filt.should_include("out/index.html")

    def test_hardcoded_in_nested_path(self, tmp_path: Path) -> None:
        """node_modules anywhere in the path should be excluded."""
        filt = FileFilter(tmp_path)
        assert not filt.should_include("packages/frontend/node_modules/react/index.js")

    def test_normal_file_included(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert filt.should_include("src/main.py")

    def test_deeply_nested_file_included(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert filt.should_include("src/core/auth/handlers/login.py")

    def test_all_hardcoded_dirs_present(self) -> None:
        """Verify the hardcoded set contains all expected directories."""
        expected = {
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
        assert HARDCODED_IGNORES == expected


class TestFileFilterGitignore:
    """Tests for .gitignore pattern matching."""

    def test_gitignore_glob_pattern(self, tmp_path: Path) -> None:
        _make_gitignore(tmp_path, ["*.log"])
        filt = FileFilter(tmp_path)
        assert not filt.should_include("debug.log")
        assert not filt.should_include("src/error.log")
        assert filt.should_include("src/main.py")

    def test_gitignore_directory_pattern(self, tmp_path: Path) -> None:
        _make_gitignore(tmp_path, ["vendor/"])
        filt = FileFilter(tmp_path)
        assert not filt.should_include("vendor/lib/foo.py")
        assert filt.should_include("src/vendor_utils.py")

    def test_gitignore_negation_pattern(self, tmp_path: Path) -> None:
        _make_gitignore(tmp_path, ["*.log", "!important.log"])
        filt = FileFilter(tmp_path)
        assert not filt.should_include("debug.log")
        assert filt.should_include("important.log")

    def test_gitignore_wildcard_dir(self, tmp_path: Path) -> None:
        _make_gitignore(tmp_path, ["**/temp/"])
        filt = FileFilter(tmp_path)
        assert not filt.should_include("temp/cache.txt")
        assert not filt.should_include("src/temp/cache.txt")

    def test_gitignore_comment_ignored(self, tmp_path: Path) -> None:
        _make_gitignore(tmp_path, ["# this is a comment", "*.log"])
        filt = FileFilter(tmp_path)
        assert not filt.should_include("app.log")
        assert filt.should_include("# this is a comment")  # literal filename

    def test_no_gitignore_no_error(self, tmp_path: Path) -> None:
        """Should work fine when there's no .gitignore."""
        filt = FileFilter(tmp_path)
        assert filt.should_include("src/main.py")


class TestFileFilterCodebasegraphignore:
    """Tests for .codebasegraphignore support."""

    def test_custom_ignore_pattern(self, tmp_path: Path) -> None:
        _make_codebasegraphignore(tmp_path, ["generated/", "*.generated.ts"])
        filt = FileFilter(tmp_path)
        assert not filt.should_include("generated/api.ts")
        assert not filt.should_include("src/types.generated.ts")
        assert filt.should_include("src/types.ts")

    def test_custom_plus_gitignore_combined(self, tmp_path: Path) -> None:
        _make_gitignore(tmp_path, ["*.log"])
        _make_codebasegraphignore(tmp_path, ["docs/"])
        filt = FileFilter(tmp_path)
        assert not filt.should_include("debug.log")  # from .gitignore
        assert not filt.should_include("docs/readme.md")  # from .codebasegraphignore
        assert filt.should_include("src/main.py")  # included

    def test_no_custom_ignore_no_error(self, tmp_path: Path) -> None:
        """Should work fine when there's no .codebasegraphignore."""
        filt = FileFilter(tmp_path)
        assert filt.should_include("src/main.py")


class TestFileFilterAbsolutePath:
    """Tests for should_include_abs() method."""

    def test_abs_path_conversion(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        # Create a real file to test with
        (tmp_path / "src").mkdir()
        (tmp_path / "src" / "main.py").write_text("# hello")
        assert filt.should_include_abs(str(tmp_path / "src" / "main.py"))

    def test_abs_path_excluded(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert not filt.should_include_abs(
            str(tmp_path / "node_modules" / "express" / "index.js")
        )

    def test_abs_path_outside_root_excluded(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert not filt.should_include_abs("/some/other/project/main.py")


class TestFileFilterEdgeCases:
    """Edge cases for FileFilter."""

    def test_empty_path(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        # Empty path has no parts to check against hardcoded
        assert filt.should_include("")

    def test_root_level_file(self, tmp_path: Path) -> None:
        filt = FileFilter(tmp_path)
        assert filt.should_include("README.md")

    def test_backslash_normalization(self, tmp_path: Path) -> None:
        """Windows-style paths should be normalized."""
        filt = FileFilter(tmp_path)
        assert not filt.should_include("node_modules\\express\\index.js")

    def test_gitignore_with_specific_file(self, tmp_path: Path) -> None:
        _make_gitignore(tmp_path, ["secrets.env"])
        filt = FileFilter(tmp_path)
        assert not filt.should_include("secrets.env")
        assert filt.should_include("config.env")


# ═══════════════════════════════════════════════════════════════════
# ContentHasher Tests
# ═══════════════════════════════════════════════════════════════════


class TestContentHasher:
    """Tests for content-hash diffing."""

    def test_compute_initial(self, tmp_path: Path) -> None:
        (tmp_path / "a.py").write_text("hello")
        (tmp_path / "b.py").write_text("world")
        hasher = ContentHasher(tmp_path)
        hasher.compute_initial(["a.py", "b.py"])
        assert len(hasher.hashes) == 2
        assert "a.py" in hasher.hashes
        assert "b.py" in hasher.hashes

    def test_check_unchanged_returns_false(self, tmp_path: Path) -> None:
        """Touching a file without changing content should return False."""
        (tmp_path / "main.py").write_text("original content")
        hasher = ContentHasher(tmp_path)
        hasher.compute_initial(["main.py"])

        # "Touch" the file without changing content
        changed = hasher.check_and_update("main.py")
        assert not changed

    def test_check_changed_returns_true(self, tmp_path: Path) -> None:
        """Modifying file content should return True."""
        f = tmp_path / "main.py"
        f.write_text("original")
        hasher = ContentHasher(tmp_path)
        hasher.compute_initial(["main.py"])

        # Change the content
        f.write_text("modified")
        changed = hasher.check_and_update("main.py")
        assert changed

    def test_new_file_returns_true(self, tmp_path: Path) -> None:
        """A file not previously tracked should return True."""
        (tmp_path / "new.py").write_text("new content")
        hasher = ContentHasher(tmp_path)
        changed = hasher.check_and_update("new.py")
        assert changed

    def test_deleted_file_returns_true(self, tmp_path: Path) -> None:
        """Removing a tracked file should return True."""
        f = tmp_path / "main.py"
        f.write_text("content")
        hasher = ContentHasher(tmp_path)
        hasher.compute_initial(["main.py"])

        # Delete the file
        f.unlink()
        changed = hasher.check_and_update("main.py")
        assert changed
        # Hash should be removed
        assert "main.py" not in hasher.hashes

    def test_remove_tracked_file(self, tmp_path: Path) -> None:
        (tmp_path / "main.py").write_text("content")
        hasher = ContentHasher(tmp_path)
        hasher.compute_initial(["main.py"])
        assert hasher.remove("main.py")
        assert "main.py" not in hasher.hashes

    def test_remove_untracked_file(self, tmp_path: Path) -> None:
        hasher = ContentHasher(tmp_path)
        assert not hasher.remove("nonexistent.py")

    def test_hash_stability(self, tmp_path: Path) -> None:
        """Same content should always produce the same hash."""
        (tmp_path / "a.py").write_text("hello world")
        (tmp_path / "b.py").write_text("hello world")
        hasher = ContentHasher(tmp_path)
        hasher.compute_initial(["a.py", "b.py"])
        assert hasher.hashes["a.py"] == hasher.hashes["b.py"]

    def test_different_content_different_hash(self, tmp_path: Path) -> None:
        (tmp_path / "a.py").write_text("hello")
        (tmp_path / "b.py").write_text("world")
        hasher = ContentHasher(tmp_path)
        hasher.compute_initial(["a.py", "b.py"])
        assert hasher.hashes["a.py"] != hasher.hashes["b.py"]


class TestHashFile:
    """Tests for the _hash_file utility function."""

    def test_hash_returns_hex_string(self, tmp_path: Path) -> None:
        f = tmp_path / "test.py"
        f.write_text("hello")
        h = _hash_file(f)
        assert len(h) == 64  # SHA-256 hex
        assert all(c in "0123456789abcdef" for c in h)

    def test_hash_nonexistent_returns_empty(self, tmp_path: Path) -> None:
        h = _hash_file(tmp_path / "nonexistent.py")
        assert h == ""

    def test_hash_deterministic(self, tmp_path: Path) -> None:
        f = tmp_path / "test.py"
        f.write_text("deterministic")
        assert _hash_file(f) == _hash_file(f)


# ═══════════════════════════════════════════════════════════════════
# IncrementalPipeline Tests
# ═══════════════════════════════════════════════════════════════════


def _setup_git_repo(tmp_path: Path) -> Path:
    """Initialize a minimal git repo with some Python files.

    Kit requires a git-initialized directory to work.
    """
    # Init git repo
    os.system(f"git init {tmp_path} > /dev/null 2>&1")
    os.system(
        f'cd {tmp_path} && git config user.email "test@test.com" && git config user.name "Test"'
    )

    # Create directory structure
    src_dir = tmp_path / "src" / "core"
    src_dir.mkdir(parents=True)

    # Create Python files with some symbols
    (src_dir / "models.py").write_text(
        'class User:\n    """A user."""\n    name: str\n\nclass Session:\n    """A session."""\n    token: str\n',
        encoding="utf-8",
    )
    (src_dir / "utils.py").write_text(
        'def helper():\n    """A helper."""\n    return True\n',
        encoding="utf-8",
    )

    # Add and commit so Kit can see the files
    os.system(f"cd {tmp_path} && git add -A && git commit -m 'init' > /dev/null 2>&1")

    return tmp_path


class TestIncrementalPipeline:
    """Tests for the incremental update pipeline."""

    def test_full_index_produces_output(self, tmp_path: Path) -> None:
        repo = _setup_git_repo(tmp_path)
        output = repo / ".codebase.md"
        pipeline = IncrementalPipeline(repo, output)
        content = pipeline.full_index()

        assert "Live Codebase Map" in content
        assert "```toon" in content
        assert output.exists()

    def test_full_index_finds_symbols(self, tmp_path: Path) -> None:
        repo = _setup_git_repo(tmp_path)
        pipeline = IncrementalPipeline(repo, repo / ".codebase.md")
        pipeline.full_index()

        # Should have found symbols from our fixture files
        assert len(pipeline.state.symbols_by_file) > 0

    def test_incremental_update_reparses_changed_file(self, tmp_path: Path) -> None:
        repo = _setup_git_repo(tmp_path)
        pipeline = IncrementalPipeline(repo, repo / ".codebase.md")
        pipeline.full_index()

        initial_symbols = dict(pipeline.state.symbols_by_file)

        # Modify a file and add to git
        models_file = repo / "src" / "core" / "models.py"
        models_file.write_text(
            'class User:\n    """A user."""\n    name: str\n\nclass Session:\n    """A session."""\n    token: str\n\nclass Admin:\n    """An admin."""\n    role: str\n',
            encoding="utf-8",
        )
        os.system(
            f"cd {repo} && git add -A && git commit -m 'add admin' > /dev/null 2>&1"
        )

        # Incremental update
        content = pipeline.update_files(["src/core/models.py"])

        # The admin class should now be in the output
        assert "Admin" in content

    def test_remove_files_removes_symbols(self, tmp_path: Path) -> None:
        repo = _setup_git_repo(tmp_path)
        pipeline = IncrementalPipeline(repo, repo / ".codebase.md")
        pipeline.full_index()

        assert "src/core/utils.py" in pipeline.state.symbols_by_file

        # Remove file from state
        content = pipeline.remove_files(["src/core/utils.py"])
        assert "src/core/utils.py" not in pipeline.state.symbols_by_file

    def test_atomic_write(self, tmp_path: Path) -> None:
        """Output file should be written atomically (no temp files left)."""
        repo = _setup_git_repo(tmp_path)
        output = repo / ".codebase.md"
        pipeline = IncrementalPipeline(repo, output)
        pipeline.full_index()

        assert output.exists()
        # No temp files should remain
        temp_files = list(repo.glob(".codebase_*.md.tmp"))
        assert len(temp_files) == 0

    def test_languages_detected(self, tmp_path: Path) -> None:
        repo = _setup_git_repo(tmp_path)
        pipeline = IncrementalPipeline(repo, repo / ".codebase.md")
        pipeline.full_index()

        assert pipeline.state.metadata is not None
        assert "python" in pipeline.state.metadata.languages

    def test_file_filter_respected(self, tmp_path: Path) -> None:
        """Ignored files should not appear in the index."""
        repo = _setup_git_repo(tmp_path)
        _make_gitignore(repo, ["src/core/utils.py"])
        pipeline = IncrementalPipeline(repo, repo / ".codebase.md")
        pipeline.full_index()

        # utils.py should be excluded by gitignore
        assert "src/core/utils.py" not in pipeline.state.symbols_by_file

    def test_update_ignored_file_removes_from_state(self, tmp_path: Path) -> None:
        """If a file becomes ignored, it should be removed from state."""
        repo = _setup_git_repo(tmp_path)
        pipeline = IncrementalPipeline(repo, repo / ".codebase.md")
        pipeline.full_index()

        # Now add a gitignore that excludes utils.py
        _make_gitignore(repo, ["src/core/utils.py"])
        # Recreate filter (in real usage, the watcher would use the same filter)
        pipeline._filter = FileFilter(repo)

        pipeline.update_files(["src/core/utils.py"])
        assert "src/core/utils.py" not in pipeline.state.symbols_by_file

    def test_project_name_default(self, tmp_path: Path) -> None:
        repo = _setup_git_repo(tmp_path)
        pipeline = IncrementalPipeline(repo, repo / ".codebase.md")
        pipeline.full_index()
        assert pipeline.state.metadata is not None
        # Default name is the directory name
        assert pipeline.state.metadata.name == repo.name

    def test_project_name_custom(self, tmp_path: Path) -> None:
        repo = _setup_git_repo(tmp_path)
        pipeline = IncrementalPipeline(
            repo, repo / ".codebase.md", project_name="my-project"
        )
        pipeline.full_index()
        assert pipeline.state.metadata is not None
        assert pipeline.state.metadata.name == "my-project"


class TestIncrementalPipelineStateManagement:
    """Tests that the pipeline maintains correct state across updates."""

    def test_state_preserved_across_updates(self, tmp_path: Path) -> None:
        repo = _setup_git_repo(tmp_path)
        pipeline = IncrementalPipeline(repo, repo / ".codebase.md")
        pipeline.full_index()

        initial_files = set(pipeline.state.symbols_by_file.keys())

        # Update one file — other files should remain in state
        pipeline.update_files(["src/core/models.py"])

        current_files = set(pipeline.state.symbols_by_file.keys())
        # models.py should still be there (re-parsed), other files preserved
        assert "src/core/models.py" in current_files
        # Other files from initial should still be present
        for f in initial_files:
            if f != "src/core/models.py":
                assert f in current_files

    def test_modules_rebuilt_on_update(self, tmp_path: Path) -> None:
        repo = _setup_git_repo(tmp_path)
        pipeline = IncrementalPipeline(repo, repo / ".codebase.md")
        pipeline.full_index()

        initial_modules = len(pipeline.state.modules)

        # Update shouldn't change module count for same files
        pipeline.update_files(["src/core/models.py"])
        assert len(pipeline.state.modules) == initial_modules


# ═══════════════════════════════════════════════════════════════════
# CodebaseWatcher Tests
# ═══════════════════════════════════════════════════════════════════


class TestCodebaseWatcher:
    """Tests for the watchfiles-based file watcher."""

    def test_watcher_creation(self, tmp_path: Path) -> None:
        watcher = CodebaseWatcher(tmp_path)
        assert watcher.hasher is not None

    def test_watcher_stop(self, tmp_path: Path) -> None:
        watcher = CodebaseWatcher(tmp_path)
        watcher.stop()
        # Should not raise

    def test_watcher_requires_callback(self, tmp_path: Path) -> None:
        watcher = CodebaseWatcher(tmp_path)
        with pytest.raises(ValueError, match="on_change callback is required"):
            watcher.watch()

    def test_watcher_background_thread(self, tmp_path: Path) -> None:
        """Watcher should be able to start in a background thread and stop."""
        changes: list[list[str]] = []

        def on_change(files: list[str]) -> None:
            changes.append(files)

        watcher = CodebaseWatcher(tmp_path, on_change=on_change)
        watcher.start_background()

        # Give the watcher a moment to start
        time.sleep(0.2)

        # Stop it
        watcher.stop()
        time.sleep(0.2)
        # Should not raise or hang

    def test_watcher_detects_file_change(self, tmp_path: Path) -> None:
        """Watcher should detect actual file changes and call the callback."""
        changes: list[list[str]] = []

        def on_change(files: list[str]) -> None:
            changes.append(files)

        # Create initial file
        py_file = tmp_path / "main.py"
        py_file.write_text("# initial")

        watcher = CodebaseWatcher(tmp_path, on_change=on_change)
        watcher.start_background()

        try:
            # Give watcher time to start
            time.sleep(0.3)

            # Modify the file
            py_file.write_text("# modified")

            # Wait for change detection (watchfiles polls)
            time.sleep(1.0)

            # We should have seen at least one change
            assert len(changes) > 0
            # The change should include our file
            all_changed = [f for batch in changes for f in batch]
            assert any("main.py" in f for f in all_changed)
        finally:
            watcher.stop()
            time.sleep(0.2)

    def test_watcher_filters_ignored_files(self, tmp_path: Path) -> None:
        """Files in ignored directories should not trigger callbacks."""
        changes: list[list[str]] = []

        def on_change(files: list[str]) -> None:
            changes.append(files)

        _make_gitignore(tmp_path, ["ignored/"])

        watcher = CodebaseWatcher(tmp_path, on_change=on_change)
        watcher.start_background()

        try:
            time.sleep(0.3)

            # Create file in ignored directory
            ignored_dir = tmp_path / "ignored"
            ignored_dir.mkdir()
            (ignored_dir / "test.py").write_text("# should be ignored")

            time.sleep(1.0)

            # Changes should be empty (or not contain any ignored/ files)
            all_changed = [f for batch in changes for f in batch]
            assert not any("ignored/" in f for f in all_changed)
        finally:
            watcher.stop()
            time.sleep(0.2)

    def test_watcher_skips_non_supported_extensions(self, tmp_path: Path) -> None:
        """Non-supported extensions (.md, .json, etc.) should be filtered."""
        changes: list[list[str]] = []

        def on_change(files: list[str]) -> None:
            changes.append(files)

        watcher = CodebaseWatcher(tmp_path, on_change=on_change)
        watcher.start_background()

        try:
            time.sleep(0.3)

            # Create a markdown file (not a supported extension)
            (tmp_path / "README.md").write_text("# Hello")

            time.sleep(1.0)

            # Should not see .md files in changes
            all_changed = [f for batch in changes for f in batch]
            assert not any(f.endswith(".md") for f in all_changed)
        finally:
            watcher.stop()
            time.sleep(0.2)

    def test_watcher_content_hash_dedup(self, tmp_path: Path) -> None:
        """Files touched without content change should not trigger callbacks."""
        changes: list[list[str]] = []

        def on_change(files: list[str]) -> None:
            changes.append(files)

        # Create initial file and hash it
        py_file = tmp_path / "main.py"
        py_file.write_text("# original content")

        watcher = CodebaseWatcher(tmp_path, on_change=on_change)
        # Pre-seed the hash
        watcher.hasher.compute_initial(["main.py"])

        watcher.start_background()

        try:
            time.sleep(0.3)

            # "Touch" the file with same content
            py_file.write_text("# original content")

            time.sleep(1.0)

            # Should not see changes (content hash same)
            all_changed = [f for batch in changes for f in batch]
            assert not any("main.py" in f for f in all_changed)
        finally:
            watcher.stop()
            time.sleep(0.2)


# ═══════════════════════════════════════════════════════════════════
# Integration Tests
# ═══════════════════════════════════════════════════════════════════


class TestEndToEndIncremental:
    """End-to-end tests combining watcher + pipeline."""

    def test_full_roundtrip(self, tmp_path: Path) -> None:
        """Full index -> modify file -> incremental update -> verify output."""
        repo = _setup_git_repo(tmp_path)
        output = repo / ".codebase.md"
        pipeline = IncrementalPipeline(repo, output)

        # Full index
        content1 = pipeline.full_index()
        assert "User" in content1
        assert "Session" in content1
        assert output.exists()

        # Add a new class
        models_file = repo / "src" / "core" / "models.py"
        models_file.write_text(
            'class User:\n    """A user."""\n    name: str\n\nclass Session:\n    """A session."""\n    token: str\n\nclass Payment:\n    """A payment."""\n    amount: float\n',
            encoding="utf-8",
        )
        os.system(
            f"cd {repo} && git add -A && git commit -m 'add payment' > /dev/null 2>&1"
        )

        # Incremental update
        content2 = pipeline.update_files(["src/core/models.py"])
        assert "Payment" in content2
        assert "User" in content2  # existing symbols preserved
        assert output.exists()

        # Verify the file was updated
        on_disk = output.read_text(encoding="utf-8")
        assert "Payment" in on_disk

    def test_incremental_performance(self, tmp_path: Path) -> None:
        """Incremental update should be fast (< 50ms for single file)."""
        repo = _setup_git_repo(tmp_path)
        pipeline = IncrementalPipeline(repo, repo / ".codebase.md")
        pipeline.full_index()

        # Time the incremental update
        start = time.perf_counter()
        pipeline.update_files(["src/core/models.py"])
        elapsed_ms = (time.perf_counter() - start) * 1000

        # Should be well under 50ms (this is a tiny project)
        assert elapsed_ms < 50, f"Incremental update took {elapsed_ms:.1f}ms"
