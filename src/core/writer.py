"""TOON serialization and .codebase.md output.

Generates the final .codebase.md file containing:
- Markdown prompt framing (tells the model this is live data)
- TOON-encoded codeblock with modules, symbols, hierarchies,
  and dependencies

TOON format rules:
- Table header declares field names: table_name[count]{field1,field2,...}:
- Each row is comma-separated values on its own line, indented 2 spaces
- Pipe | for multi-value fields (e.g. key_types: User|Session)
- Strings are unquoted unless they contain commas or pipes
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from src.core.graph import Hierarchy, Module
from src.core.manifest import Dependency


# ── Prompt framing ─────────────────────────────────────────────────

_PROMPT_FRAMING = """\
## Live Codebase Map

The following is a **real-time structural map** of this codebase. It was
regenerated moments ago and reflects the current state of all files on disk.

All file paths and line numbers are accurate right now. When you edit a file,
this map updates before your next turn.

Use this map to navigate directly to the right files and line numbers without
searching. Trust these locations — they are current."""


# ── TOON helpers ───────────────────────────────────────────────────


def _escape_value(value: str) -> str:
    """Escape a TOON field value if it contains commas or pipes.

    Wraps the value in double quotes if it contains characters that
    would be ambiguous in the comma-separated row format.
    """
    if not value:
        return ""
    # Quote if the value contains commas, pipes, or double quotes
    if "," in value or "|" in value or '"' in value:
        # Escape any internal double quotes
        escaped = value.replace('"', '\\"')
        return f'"{escaped}"'
    return value


def _pipe_join(items: list[str]) -> str:
    """Join a list of strings with pipe separators for TOON multi-value fields."""
    return "|".join(items)


# ── Metadata ───────────────────────────────────────────────────────


@dataclass
class CodebaseMeta:
    """Metadata for the codebase section of TOON output.

    Attributes:
        name: Project name.
        languages: List of detected languages (e.g. ["python", "typescript"]).
        last_indexed: ISO timestamp of when the index was generated.
    """

    name: str
    languages: list[str]
    last_indexed: str | None = None  # ISO 8601 string; auto-filled if None


# ── CodebaseWriter ─────────────────────────────────────────────────


class CodebaseWriter:
    """Serializes graph data into .codebase.md with TOON format.

    Usage:
        writer = CodebaseWriter()
        content = writer.write(
            modules=modules,
            hierarchies=hierarchies,
            dependencies=deps,
            metadata=CodebaseMeta(name="my-project", languages=["python"]),
        )
        writer.write_to_file(Path(".codebase.md"), ...)
    """

    def __init__(self, max_symbols: int = 500) -> None:
        """Initialize the writer.

        Args:
            max_symbols: Maximum number of symbols to include.
                         If exceeded, type definitions are prioritized
                         and a truncation comment is added.
        """
        self.max_symbols = max_symbols

    def write(
        self,
        modules: list[Module],
        hierarchies: list[Hierarchy],
        dependencies: list[Dependency],
        metadata: CodebaseMeta,
    ) -> str:
        """Serialize the graph to .codebase.md content.

        Returns the full file content as a string: markdown prompt
        framing wrapping a TOON codeblock.
        """
        toon = self._serialize_toon(modules, hierarchies, dependencies, metadata)
        return f"{_PROMPT_FRAMING}\n\n```toon\n{toon}```\n"

    def write_to_file(
        self,
        path: str | Path,
        modules: list[Module],
        hierarchies: list[Hierarchy],
        dependencies: list[Dependency],
        metadata: CodebaseMeta,
    ) -> None:
        """Write .codebase.md to disk.

        Args:
            path: Output file path.
            modules: Module list from graph building.
            hierarchies: Hierarchy list from graph building.
            dependencies: Dependency list from manifest parsing.
            metadata: Codebase metadata.
        """
        content = self.write(modules, hierarchies, dependencies, metadata)
        Path(path).write_text(content, encoding="utf-8")

    # ── TOON serialization ─────────────────────────────────────────

    def _serialize_toon(
        self,
        modules: list[Module],
        hierarchies: list[Hierarchy],
        dependencies: list[Dependency],
        metadata: CodebaseMeta,
    ) -> str:
        """Build the full TOON content string."""
        parts: list[str] = []

        parts.append(self._serialize_metadata(metadata))
        parts.append("")  # blank line between sections

        parts.append(self._serialize_modules(modules))
        parts.append("")

        parts.append(self._serialize_symbols(modules))
        parts.append("")

        if hierarchies:
            parts.append(self._serialize_hierarchies(hierarchies))
            parts.append("")

        if dependencies:
            parts.append(self._serialize_dependencies(dependencies))
            parts.append("")

        return "\n".join(parts)

    @staticmethod
    def _serialize_metadata(meta: CodebaseMeta) -> str:
        """Serialize the codebase: metadata block."""
        timestamp = meta.last_indexed or datetime.now(timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        lang_count = len(meta.languages)
        lang_list = ",".join(meta.languages)

        lines = [
            "codebase:",
            f"  name: {meta.name}",
            f"  languages[{lang_count}]: {lang_list}",
            f"  last_indexed: {timestamp}",
        ]
        return "\n".join(lines)

    @staticmethod
    def _serialize_modules(modules: list[Module]) -> str:
        """Serialize the modules table."""
        count = len(modules)
        lines = [f"modules[{count}]{{name,path,key_types,depends_on}}:"]

        for mod in modules:
            key_types = _pipe_join(mod.key_types) if mod.key_types else ""
            depends_on = _pipe_join(mod.depends_on) if mod.depends_on else ""

            name = _escape_value(mod.name)
            path = _escape_value(mod.path)
            key_types_val = _escape_value(key_types)
            depends_on_val = _escape_value(depends_on)

            lines.append(f"  {name},{path},{key_types_val},{depends_on_val}")

        return "\n".join(lines)

    def _serialize_symbols(self, modules: list[Module]) -> str:
        """Serialize the symbols table, respecting max_symbols budget."""
        # Collect all symbols from all modules
        all_symbols = []
        for mod in modules:
            all_symbols.extend(mod.symbols)

        # Priority kinds — type definitions come first
        type_kinds = frozenset({"class", "interface", "struct", "enum", "type"})
        truncated = 0

        if len(all_symbols) > self.max_symbols:
            # Split into type defs and others
            type_syms = [s for s in all_symbols if s.kind in type_kinds]
            other_syms = [s for s in all_symbols if s.kind not in type_kinds]

            if len(type_syms) >= self.max_symbols:
                # Even type defs alone exceed budget — truncate those too
                symbols_to_write = type_syms[: self.max_symbols]
                truncated = len(all_symbols) - self.max_symbols
            else:
                # Include all type defs + fill remaining budget with others
                remaining = self.max_symbols - len(type_syms)
                symbols_to_write = type_syms + other_syms[:remaining]
                truncated = len(all_symbols) - len(symbols_to_write)
        else:
            symbols_to_write = all_symbols

        count = len(symbols_to_write)
        lines = [f"symbols[{count}]{{fqn,kind,file,line,signature}}:"]

        for sym in symbols_to_write:
            # Line numbers: Kit uses 0-indexed, add 1 for human-readable
            line_num = sym.line + 1

            fqn = _escape_value(sym.fqn)
            kind = sym.kind
            file = _escape_value(sym.file)
            sig = _escape_value(sym.signature)

            lines.append(f"  {fqn},{kind},{file},{line_num},{sig}")

        if truncated > 0:
            lines.append(f"  # ... {truncated} more symbols omitted")

        return "\n".join(lines)

    @staticmethod
    def _serialize_hierarchies(hierarchies: list[Hierarchy]) -> str:
        """Serialize the hierarchies table."""
        count = len(hierarchies)
        lines = [f"hierarchies[{count}]{{symbol,relationship,target,file,line}}:"]

        for h in hierarchies:
            # Line numbers: Kit uses 0-indexed, add 1 for human-readable
            line_num = h.line + 1

            symbol = _escape_value(h.symbol)
            target = _escape_value(h.target)
            file = _escape_value(h.file)

            lines.append(f"  {symbol},{h.relationship},{target},{file},{line_num}")

        return "\n".join(lines)

    @staticmethod
    def _serialize_dependencies(dependencies: list[Dependency]) -> str:
        """Serialize the dependencies table."""
        count = len(dependencies)
        lines = [f"dependencies[{count}]{{name,version,category}}:"]

        for dep in dependencies:
            name = _escape_value(dep.name)
            version = _escape_value(dep.version)
            lines.append(f"  {name},{version},{dep.category}")

        return "\n".join(lines)
