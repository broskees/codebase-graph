"""Tests for the CLI entry point (src/cli.py).

Covers:
- Argument parsing (all flags and combos)
- One-shot mode end-to-end
- Custom --output path
- Error handling (invalid path, missing arg, non-directory)
- Watch mode setup (without actually blocking)
- --version and --help flags
- --format json rejection
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

from src.cli import build_parser, main, resolve_project_dir, __version__


# ── Fixtures ───────────────────────────────────────────────────────


def _setup_git_repo(root: Path) -> None:
    """Initialize a minimal git repo with a Python file for Kit."""
    subprocess.run(
        ["git", "init"],
        cwd=str(root),
        capture_output=True,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.email", "test@test.com"],
        cwd=str(root),
        capture_output=True,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Test"],
        cwd=str(root),
        capture_output=True,
        check=True,
    )


def _make_project(tmp_path: Path) -> Path:
    """Create a minimal Python project fixture for testing."""
    project = tmp_path / "test-project"
    project.mkdir()
    _setup_git_repo(project)

    src = project / "src"
    src.mkdir()
    (src / "main.py").write_text(
        'class App:\n    """Main application."""\n    pass\n\n'
        'def run():\n    """Run the app."""\n    pass\n',
        encoding="utf-8",
    )

    # Git add + commit so Kit can see the files
    subprocess.run(
        ["git", "add", "."],
        cwd=str(project),
        capture_output=True,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "init"],
        cwd=str(project),
        capture_output=True,
        check=True,
    )

    return project


# ── Argument Parsing ───────────────────────────────────────────────


class TestBuildParser:
    """Tests for argparse configuration."""

    def test_positional_path(self):
        parser = build_parser()
        args = parser.parse_args(["./my-project"])
        assert args.path == "./my-project"
        assert args.watch is False

    def test_dir_flag(self):
        parser = build_parser()
        args = parser.parse_args(["--dir", "/some/path"])
        assert args.dir_path == "/some/path"
        assert args.path is None

    def test_watch_flag(self):
        parser = build_parser()
        args = parser.parse_args(["--watch", "--dir", "./proj"])
        assert args.watch is True
        assert args.dir_path == "./proj"

    def test_output_flag_long(self):
        parser = build_parser()
        args = parser.parse_args(["./proj", "--output", "/tmp/out.md"])
        assert args.output == "/tmp/out.md"

    def test_output_flag_short(self):
        parser = build_parser()
        args = parser.parse_args(["./proj", "-o", "/tmp/out.md"])
        assert args.output == "/tmp/out.md"

    def test_format_default(self):
        parser = build_parser()
        args = parser.parse_args(["./proj"])
        assert args.format == "toon"

    def test_format_json(self):
        parser = build_parser()
        args = parser.parse_args(["--format", "json", "./proj"])
        assert args.format == "json"

    def test_verbose_flag(self):
        parser = build_parser()
        args = parser.parse_args(["-v", "./proj"])
        assert args.verbose is True

    def test_verbose_long(self):
        parser = build_parser()
        args = parser.parse_args(["--verbose", "./proj"])
        assert args.verbose is True

    def test_no_args_defaults(self):
        parser = build_parser()
        args = parser.parse_args([])
        assert args.path is None
        assert args.dir_path is None
        assert args.watch is False
        assert args.output is None
        assert args.format == "toon"
        assert args.verbose is False

    def test_positional_takes_priority_over_dir(self):
        """When both positional and --dir are given, positional wins."""
        parser = build_parser()
        args = parser.parse_args(["./pos-path", "--dir", "./dir-path"])
        assert args.path == "./pos-path"
        assert args.dir_path == "./dir-path"
        # resolve_project_dir uses args.path first (positional priority)


# ── resolve_project_dir ────────────────────────────────────────────


class TestResolveProjectDir:
    """Tests for project directory resolution and validation."""

    def test_resolves_positional(self, tmp_path):
        parser = build_parser()
        args = parser.parse_args([str(tmp_path)])
        result = resolve_project_dir(args)
        assert result == tmp_path.resolve()

    def test_resolves_dir_flag(self, tmp_path):
        parser = build_parser()
        args = parser.parse_args(["--dir", str(tmp_path)])
        result = resolve_project_dir(args)
        assert result == tmp_path.resolve()

    def test_positional_over_dir(self, tmp_path):
        """Positional path takes priority over --dir."""
        other = tmp_path / "other"
        other.mkdir()
        parser = build_parser()
        args = parser.parse_args([str(tmp_path), "--dir", str(other)])
        result = resolve_project_dir(args)
        assert result == tmp_path.resolve()

    def test_no_path_exits(self):
        parser = build_parser()
        args = parser.parse_args([])
        with pytest.raises(SystemExit) as exc_info:
            resolve_project_dir(args)
        assert exc_info.value.code == 1

    def test_nonexistent_path_exits(self):
        parser = build_parser()
        args = parser.parse_args(["/nonexistent/path/xyz123"])
        with pytest.raises(SystemExit) as exc_info:
            resolve_project_dir(args)
        assert exc_info.value.code == 1

    def test_file_not_directory_exits(self, tmp_path):
        f = tmp_path / "afile.txt"
        f.write_text("hello")
        parser = build_parser()
        args = parser.parse_args([str(f)])
        with pytest.raises(SystemExit) as exc_info:
            resolve_project_dir(args)
        assert exc_info.value.code == 1


# ── One-shot mode (end-to-end) ─────────────────────────────────────


class TestOneshotMode:
    """Tests for one-shot indexing via the CLI."""

    def test_oneshot_creates_codebase_md(self, tmp_path):
        """Running main() on a project creates .codebase.md."""
        project = _make_project(tmp_path)
        main([str(project)])

        codebase_md = project / ".codebase.md"
        assert codebase_md.exists(), ".codebase.md should be created"

        content = codebase_md.read_text(encoding="utf-8")
        assert "## Live Codebase Map" in content
        assert "```toon" in content

    def test_oneshot_contains_symbols(self, tmp_path):
        """The generated .codebase.md should contain the symbols."""
        project = _make_project(tmp_path)
        main([str(project)])

        content = (project / ".codebase.md").read_text(encoding="utf-8")
        # Our fixture has a class App and function run
        assert "App" in content
        assert "run" in content

    def test_oneshot_prints_summary(self, tmp_path, capsys):
        """One-shot mode should print an index summary."""
        project = _make_project(tmp_path)
        main([str(project)])

        captured = capsys.readouterr()
        assert "Indexed" in captured.out
        assert "files" in captured.out
        assert "symbols" in captured.out
        assert "modules" in captured.out
        assert "tokens" in captured.out

    def test_oneshot_custom_output(self, tmp_path):
        """--output flag should change the output location."""
        project = _make_project(tmp_path)
        custom_out = tmp_path / "custom-output.md"

        main([str(project), "-o", str(custom_out)])

        assert custom_out.exists(), "Custom output file should be created"
        content = custom_out.read_text(encoding="utf-8")
        assert "```toon" in content

        # Default location should NOT exist
        default = project / ".codebase.md"
        assert not default.exists(), "Default .codebase.md should not be created"

    def test_oneshot_empty_project(self, tmp_path):
        """A project with no parseable files should still produce output."""
        project = tmp_path / "empty-proj"
        project.mkdir()
        _setup_git_repo(project)

        # Create a non-code file so git init works
        (project / "README.md").write_text("# Empty")
        subprocess.run(
            ["git", "add", "."],
            cwd=str(project),
            capture_output=True,
            check=True,
        )
        subprocess.run(
            ["git", "commit", "-m", "init"],
            cwd=str(project),
            capture_output=True,
            check=True,
        )

        main([str(project)])

        codebase_md = project / ".codebase.md"
        assert codebase_md.exists()
        content = codebase_md.read_text(encoding="utf-8")
        assert "```toon" in content


# ── Error handling ─────────────────────────────────────────────────


class TestErrorHandling:
    """Tests for CLI error handling."""

    def test_no_args_exits(self):
        with pytest.raises(SystemExit) as exc_info:
            main([])
        assert exc_info.value.code == 1

    def test_nonexistent_path_exits(self):
        with pytest.raises(SystemExit) as exc_info:
            main(["/nonexistent/path/abc123"])
        assert exc_info.value.code == 1

    def test_file_as_path_exits(self, tmp_path):
        f = tmp_path / "file.txt"
        f.write_text("not a dir")
        with pytest.raises(SystemExit) as exc_info:
            main([str(f)])
        assert exc_info.value.code == 1

    def test_json_format_exits(self, tmp_path):
        """--format json should exit with error since it's not yet supported."""
        with pytest.raises(SystemExit) as exc_info:
            main(["--format", "json", str(tmp_path)])
        assert exc_info.value.code == 1


# ── Version flag ───────────────────────────────────────────────────


class TestVersionFlag:
    """Tests for --version flag."""

    def test_version_prints_and_exits(self):
        with pytest.raises(SystemExit) as exc_info:
            main(["--version"])
        assert exc_info.value.code == 0

    def test_version_string(self):
        assert __version__ == "0.1.0"


# ── Help flag ──────────────────────────────────────────────────────


class TestHelpFlag:
    """Tests for --help flag."""

    def test_help_exits_zero(self):
        with pytest.raises(SystemExit) as exc_info:
            main(["--help"])
        assert exc_info.value.code == 0


# ── Watch mode (non-blocking tests) ────────────────────────────────


class TestWatchModeSetup:
    """Tests for watch mode initialization.

    We don't test the full blocking loop — just that the setup works
    and the initial index runs. The blocking watch is tested by
    immediately interrupting with KeyboardInterrupt.

    Patches CodebaseWatcher at the source module (src.core.watcher) since
    run_watch imports it locally.
    """

    def test_watch_does_initial_index(self, tmp_path):
        """Watch mode should do a full initial index before watching."""
        project = _make_project(tmp_path)
        from src.cli import run_watch

        # Patch CodebaseWatcher at the source so the local import in
        # run_watch picks up our mock
        with patch("src.core.watcher.CodebaseWatcher") as MockWatcher:
            mock_watcher = MockWatcher.return_value
            mock_watcher.watch.side_effect = KeyboardInterrupt()
            mock_watcher.hasher.compute_initial = lambda x: None
            mock_watcher.stop = lambda: None

            run_watch(project)

        assert (project / ".codebase.md").exists()

    def test_watch_prints_watching_message(self, tmp_path, capsys):
        """Watch mode should print 'Watching ... for changes' message."""
        project = _make_project(tmp_path)
        from src.cli import run_watch

        with patch("src.core.watcher.CodebaseWatcher") as MockWatcher:
            mock_watcher = MockWatcher.return_value
            mock_watcher.watch.side_effect = KeyboardInterrupt()
            mock_watcher.hasher.compute_initial = lambda x: None
            mock_watcher.stop = lambda: None

            run_watch(project)

        captured = capsys.readouterr()
        assert "Watching" in captured.out
        assert "Ctrl+C to stop" in captured.out

    def test_watch_prints_stopped_on_interrupt(self, tmp_path, capsys):
        """Watch mode should print 'Stopped watching.' on Ctrl+C."""
        project = _make_project(tmp_path)
        from src.cli import run_watch

        with patch("src.core.watcher.CodebaseWatcher") as MockWatcher:
            mock_watcher = MockWatcher.return_value
            mock_watcher.watch.side_effect = KeyboardInterrupt()
            mock_watcher.hasher.compute_initial = lambda x: None
            mock_watcher.stop = lambda: None

            run_watch(project)

        captured = capsys.readouterr()
        assert "Stopped watching." in captured.out


# ── Verbose logging ────────────────────────────────────────────────


class TestVerboseLogging:
    """Tests for --verbose flag."""

    def test_verbose_enables_debug_logging(self, tmp_path):
        """The --verbose flag should set logging to DEBUG."""
        import logging

        project = _make_project(tmp_path)
        main(["-v", str(project)])

        # After main() runs with -v, root logger should be at DEBUG
        root_logger = logging.getLogger()
        assert root_logger.level == logging.DEBUG
