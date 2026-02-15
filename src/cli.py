"""CLI entry point for codebase-graph.

Usage:
    codebase-graph ./path              # Generate .codebase.md for a project
    codebase-graph --watch --dir ./path  # Watch mode — keep .codebase.md updated
"""

from __future__ import annotations

import argparse
import logging
import sys
import time
from pathlib import Path

__version__ = "0.1.0"

logger = logging.getLogger(__name__)


# ── Arg parsing ────────────────────────────────────────────────────


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="codebase-graph",
        description="Generate a live, token-efficient structural map of a codebase.",
        epilog="Examples:\n"
        "  codebase-graph ./my-project\n"
        "  codebase-graph --watch --dir ./my-project\n"
        "  codebase-graph ./my-project -o /tmp/map.md\n",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=None,
        help="Project directory to index (positional arg).",
    )
    parser.add_argument(
        "--dir",
        dest="dir_path",
        default=None,
        help="Project directory to index (alternative to positional arg).",
    )
    parser.add_argument(
        "--watch",
        action="store_true",
        default=False,
        help="Watch mode: keep .codebase.md updated on file changes.",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Custom output path (default: <project>/.codebase.md).",
    )
    parser.add_argument(
        "--format",
        choices=["toon", "json"],
        default="toon",
        help="Output format (default: toon). JSON is a stub for v0.2.",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        default=False,
        help="Enable verbose logging.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    return parser


def resolve_project_dir(args: argparse.Namespace) -> Path:
    """Resolve the project directory from CLI args.

    Accepts either positional `path` or `--dir`, with positional taking
    priority. Returns a resolved absolute Path.

    Raises:
        SystemExit: If no path provided or path doesn't exist.
    """
    raw = args.path or args.dir_path
    if raw is None:
        print("Error: No project directory specified.", file=sys.stderr)
        print("Usage: codebase-graph <path>", file=sys.stderr)
        sys.exit(1)

    project_dir = Path(raw).resolve()
    if not project_dir.exists():
        print(f"Error: Path does not exist: {project_dir}", file=sys.stderr)
        sys.exit(1)

    if not project_dir.is_dir():
        print(f"Error: Path is not a directory: {project_dir}", file=sys.stderr)
        sys.exit(1)

    return project_dir


# ── One-shot mode ──────────────────────────────────────────────────


def run_oneshot(project_dir: Path, output_path: Path | None = None) -> None:
    """Run a one-shot index: parse, build graph, write .codebase.md, exit.

    Args:
        project_dir: Absolute path to the project directory.
        output_path: Custom output path, or None for <project>/.codebase.md.
    """
    from src.core.watcher import FileFilter, IncrementalPipeline

    out = output_path or (project_dir / ".codebase.md")
    file_filter = FileFilter(project_dir)

    pipeline = IncrementalPipeline(
        project_root=project_dir,
        output_path=out,
        project_name=project_dir.name,
        file_filter=file_filter,
    )

    t0 = time.monotonic()
    content = pipeline.full_index()
    elapsed_ms = (time.monotonic() - t0) * 1000

    # Gather summary stats
    state = pipeline.state
    num_files = len(state.symbols_by_file)
    num_symbols = sum(len(syms) for syms in state.symbols_by_file.values())
    num_modules = len(state.modules)

    # Rough token estimate: ~4 chars per token for English text
    token_estimate = len(content) // 4

    print(
        f"Indexed {num_files} files, {num_symbols} symbols, "
        f"{num_modules} modules -> {out.name} "
        f"(~{token_estimate} tokens, {elapsed_ms:.0f}ms)"
    )


# ── Watch mode ─────────────────────────────────────────────────────


def run_watch(project_dir: Path, output_path: Path | None = None) -> None:
    """Run watch mode: initial index then watch for changes.

    Handles Ctrl+C gracefully. Prints change notifications.

    Args:
        project_dir: Absolute path to the project directory.
        output_path: Custom output path, or None for <project>/.codebase.md.
    """
    from src.core.watcher import CodebaseWatcher, FileFilter, IncrementalPipeline

    out = output_path or (project_dir / ".codebase.md")
    file_filter = FileFilter(project_dir)

    pipeline = IncrementalPipeline(
        project_root=project_dir,
        output_path=out,
        project_name=project_dir.name,
        file_filter=file_filter,
    )

    # Initial full index
    t0 = time.monotonic()
    pipeline.full_index()
    elapsed_ms = (time.monotonic() - t0) * 1000

    state = pipeline.state
    num_files = len(state.symbols_by_file)
    num_symbols = sum(len(syms) for syms in state.symbols_by_file.values())
    num_modules = len(state.modules)
    # Read the file we just wrote for token estimate
    content = out.read_text(encoding="utf-8") if out.exists() else ""
    token_estimate = len(content) // 4

    print(
        f"Indexed {num_files} files, {num_symbols} symbols, "
        f"{num_modules} modules -> {out.name} "
        f"(~{token_estimate} tokens, {elapsed_ms:.0f}ms)"
    )
    print(f"Watching {project_dir} for changes... (Ctrl+C to stop)")

    # Set up initial content hashes for the watcher
    watcher = CodebaseWatcher(
        project_root=project_dir,
        file_filter=file_filter,
    )
    watcher.hasher.compute_initial(list(state.symbols_by_file.keys()))

    def on_change(changed_files: list[str]) -> None:
        """Handle file changes from the watcher."""
        t_start = time.monotonic()
        pipeline.update_files(changed_files)
        dt_ms = (time.monotonic() - t_start) * 1000

        for f in changed_files:
            print(f"[update] {f} changed -> {out.name} regenerated ({dt_ms:.0f}ms)")

    try:
        watcher.watch(on_change=on_change)
    except KeyboardInterrupt:
        pass
    finally:
        watcher.stop()
        print("\nStopped watching.")


# ── Main ───────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> None:
    """Entry point for the codebase-graph CLI.

    Args:
        argv: Command-line arguments. Defaults to sys.argv[1:].
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    # Configure logging (force=True overrides any existing config from tests/imports)
    level = logging.DEBUG if args.verbose else logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(levelname)s: %(message)s",
        force=True,
    )

    if args.format == "json":
        print(
            "Error: JSON output format is not yet supported (coming in v0.2).",
            file=sys.stderr,
        )
        sys.exit(1)

    project_dir = resolve_project_dir(args)
    output_path = Path(args.output).resolve() if args.output else None

    if args.watch:
        run_watch(project_dir, output_path)
    else:
        run_oneshot(project_dir, output_path)


if __name__ == "__main__":
    main()
