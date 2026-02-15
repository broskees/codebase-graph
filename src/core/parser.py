"""Kit wrapper for symbol extraction.

Wraps Kit's Repository API to extract symbols from source files,
normalizing the output into our Symbol dataclass format.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from kit import Repository


# File extensions we support for symbol extraction
SUPPORTED_EXTENSIONS: set[str] = {".ts", ".tsx", ".js", ".jsx", ".py"}


@dataclass(frozen=True, slots=True)
class Symbol:
    """A code symbol extracted from a source file.

    Attributes:
        name: The symbol's identifier (e.g. "MyClass", "process_data").
        kind: Normalized kind — one of: fn, class, interface, method, variable.
        file: Relative file path from the repo root.
        line: Start line number (1-indexed).
        end_line: End line number (1-indexed).
        signature: The first line of the symbol's code (declaration/signature).
        fqn: Fully qualified name — module::name (e.g. "src/auth::login").
    """

    name: str
    kind: str
    file: str
    line: int
    end_line: int
    signature: str
    fqn: str


def _normalize_kind(raw_type: str) -> str:
    """Normalize Kit's symbol type strings to our kind vocabulary.

    Kit returns types like "function", "class", "method", "interface", etc.
    We normalize to a compact set for TOON output.
    """
    mapping = {
        "function": "fn",
        "class": "class",
        "method": "method",
        "interface": "interface",
        "type_alias": "type",
        "enum": "enum",
        "variable": "variable",
        "constant": "variable",
        "module": "module",
        "struct": "struct",
        "trait": "trait",
    }
    return mapping.get(raw_type, raw_type)


def _extract_signature(code: str) -> str:
    """Extract a compact signature from the symbol's code block.

    Takes the first line of the code, strips trailing colons/braces,
    and truncates to a reasonable length.
    """
    if not code:
        return ""
    first_line = code.split("\n")[0].strip()
    # Cap at 120 chars for readability
    if len(first_line) > 120:
        first_line = first_line[:117] + "..."
    return first_line


def _make_fqn(file_path: str, symbol_name: str) -> str:
    """Build a fully qualified name from file path and symbol name.

    Converts "src/auth/login.ts" + "authenticate" -> "src/auth/login::authenticate"
    """
    # Strip extension from file path for the module part
    module_path = str(Path(file_path).with_suffix(""))
    return f"{module_path}::{symbol_name}"


def _has_supported_extension(file_path: str) -> bool:
    """Check if a file path has a supported extension."""
    return Path(file_path).suffix in SUPPORTED_EXTENSIONS


class CodebaseParser:
    """Wraps Kit's Repository to extract and normalize symbols.

    Usage:
        parser = CodebaseParser("/path/to/repo")
        symbols = parser.parse_file("src/main.py")
        all_symbols = parser.parse_directory()
    """

    def __init__(self, repo_path: str | Path) -> None:
        self.repo_path = Path(repo_path).resolve()
        self._repo = Repository(str(self.repo_path))

    def parse_file(self, file_path: str) -> list[Symbol]:
        """Extract symbols from a single file.

        Args:
            file_path: Path relative to the repo root (e.g. "src/main.py").

        Returns:
            List of Symbol dataclasses extracted from the file.
        """
        if not _has_supported_extension(file_path):
            return []

        raw_symbols = self._repo.extract_symbols(file_path=file_path)
        if not raw_symbols:
            return []

        symbols: list[Symbol] = []
        for raw in raw_symbols:
            name = raw.get("name", "")
            if not name:
                continue

            raw_type = raw.get("type", "unknown")
            kind = _normalize_kind(raw_type)
            file_rel = raw.get("file", file_path)
            start_line = raw.get("start_line", 0)
            end_line = raw.get("end_line", start_line)
            code = raw.get("code", "")
            signature = _extract_signature(code)
            fqn = _make_fqn(file_rel, name)

            symbols.append(
                Symbol(
                    name=name,
                    kind=kind,
                    file=file_rel,
                    line=start_line,
                    end_line=end_line,
                    signature=signature,
                    fqn=fqn,
                )
            )

        return symbols

    def parse_directory(self, subpath: str | None = None) -> dict[str, list[Symbol]]:
        """Extract symbols from all supported files in a directory.

        Args:
            subpath: Optional subdirectory to scope to (relative to repo root).

        Returns:
            Dict mapping relative file paths to their extracted symbols.
        """
        file_tree = self._repo.get_file_tree(subpath=subpath if subpath else None)

        result: dict[str, list[Symbol]] = {}
        for entry in file_tree:
            if entry.get("is_dir", False):
                continue

            file_path = entry.get("path", "")
            if not _has_supported_extension(file_path):
                continue

            symbols = self.parse_file(file_path)
            if symbols:
                result[file_path] = symbols

        return result
