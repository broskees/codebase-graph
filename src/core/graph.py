"""Module clustering and graph building.

Groups symbols into directory-based modules, extracts type hierarchies
(extends/implements/contains), and detects cross-module dependencies
by scanning import statements.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import PurePosixPath

from src.core.parser import Symbol


# ── Dataclasses ────────────────────────────────────────────────────


@dataclass(slots=True)
class Module:
    """A logical module derived from directory structure.

    Attributes:
        name: Short module name (directory name).
        path: Relative directory path from repo root.
        key_types: Important types in this module (classes, interfaces, structs).
        depends_on: Names of other modules this one imports from.
        symbols: All symbols belonging to this module.
    """

    name: str
    path: str
    key_types: list[str] = field(default_factory=list)
    depends_on: list[str] = field(default_factory=list)
    symbols: list[Symbol] = field(default_factory=list)


@dataclass(frozen=True, slots=True)
class Hierarchy:
    """A type relationship extracted from symbol signatures.

    Attributes:
        symbol: FQN of the source symbol.
        relationship: One of "extends", "implements", "contains".
        target: Name of the target type.
        file: File where the relationship is declared.
        line: Line number of the declaration.
    """

    symbol: str
    relationship: str
    target: str
    file: str
    line: int


# ── Hierarchy extraction patterns ─────────────────────────────────

# Python: class Foo(Bar, Baz):
_PY_EXTENDS_RE = re.compile(r"^class\s+\w+\s*\(([^)]+)\)\s*:")

# TypeScript: class Foo extends Bar
_TS_EXTENDS_RE = re.compile(r"\bextends\s+([\w.]+)")

# TypeScript: class Foo implements Bar, Baz
_TS_IMPLEMENTS_RE = re.compile(r"\bimplements\s+([\w.,\s]+)")

# Type annotations that reference other types — field: SomeType or field: SomeType[]
# Matches patterns like `: OrderItem`, `: OrderItem[]`, `: List[OrderItem]`
_CONTAINS_RE = re.compile(
    r":\s*(?:list\[|List\[|Array<|Set<|Optional\[)?([\w]+)\]?>?\s*(?:\[\])?"
)

# Python builtins / primitives we should skip when detecting "contains" relationships
_PRIMITIVE_TYPES = frozenset(
    {
        "str",
        "int",
        "float",
        "bool",
        "None",
        "bytes",
        "dict",
        "list",
        "tuple",
        "set",
        "frozenset",
        "type",
        "object",
        "any",
        "Any",
        # TypeScript primitives
        "string",
        "number",
        "boolean",
        "void",
        "undefined",
        "null",
        "never",
        "unknown",
        "Map",
        "Set",
        "Array",
        "Promise",
        "Date",
        "Error",
        "RegExp",
        "Symbol",
        "Record",
        "Partial",
        "Required",
        "Readonly",
        "Pick",
        "Omit",
        "Exclude",
        "Extract",
        "Optional",
        "List",
    }
)

# Python base classes that are not real "extends" relationships
_IGNORED_BASES = frozenset(
    {
        "object",
        "ABC",
        "Protocol",
        "NamedTuple",
        "TypedDict",
        "Enum",
        "IntEnum",
        "StrEnum",
        "Flag",
        "IntFlag",
        "Exception",
        "BaseException",
        "ValueError",
        "TypeError",
        "RuntimeError",
        "IOError",
        "OSError",
        "KeyError",
        "IndexError",
        "AttributeError",
    }
)

# Import patterns for cross-module dependency detection
# Python: from src.auth.login import X  or  import src.auth.login
_PY_IMPORT_RE = re.compile(
    r"^\s*(?:from\s+([\w.]+)\s+import|import\s+([\w.]+))", re.MULTILINE
)
# TypeScript/JS: import ... from "./auth/login"  or  import ... from "../auth/login"
_TS_IMPORT_RE = re.compile(
    r"""^\s*import\s+.*?\s+from\s+['"](\.\.?/[^'"]+)['"]""", re.MULTILINE
)


# ── Module Clusterer ───────────────────────────────────────────────

# Kinds that count as "key types" for module summaries
_KEY_TYPE_KINDS = frozenset({"class", "interface", "struct", "enum", "type"})


class ModuleClusterer:
    """Groups symbols into directory-based modules.

    Each top-level directory under the project root (or under src/) forms
    one module. Symbols in the root directory itself get a special "__root__"
    module.
    """

    def cluster(self, symbols_by_file: dict[str, list[Symbol]]) -> list[Module]:
        """Cluster file-grouped symbols into modules.

        Args:
            symbols_by_file: Dict mapping relative file paths to their symbols
                             (the output of CodebaseParser.parse_directory).

        Returns:
            List of Module objects, one per top-level directory.
        """
        # Bucket files into modules by their top-level directory
        module_buckets: dict[str, list[Symbol]] = {}
        module_files: dict[str, set[str]] = {}

        for file_path, file_symbols in symbols_by_file.items():
            module_path = self._module_path_for(file_path)
            module_buckets.setdefault(module_path, []).extend(file_symbols)
            module_files.setdefault(module_path, set()).add(file_path)

        # Build Module objects
        modules: list[Module] = []
        for mod_path in sorted(module_buckets):
            name = PurePosixPath(mod_path).name if mod_path != "." else "__root__"
            syms = module_buckets[mod_path]

            key_types = sorted({s.name for s in syms if s.kind in _KEY_TYPE_KINDS})

            modules.append(
                Module(
                    name=name,
                    path=mod_path,
                    key_types=key_types,
                    depends_on=[],  # filled in by detect_cross_module_deps
                    symbols=syms,
                )
            )

        return modules

    @staticmethod
    def _module_path_for(file_path: str) -> str:
        """Determine which module a file belongs to.

        Strategy:
        - If path starts with src/, use the first directory under src/
          e.g. "src/auth/login.py" -> "src/auth"
        - Otherwise use the first directory component
          e.g. "lib/utils.py" -> "lib"
        - Root-level files (no directory) -> "."
        """
        parts = PurePosixPath(file_path).parts

        if len(parts) <= 1:
            # Root-level file like "main.py"
            return "."

        if parts[0] == "src" and len(parts) > 2:
            # Under src/ — module is src/<first_subdir>
            return f"{parts[0]}/{parts[1]}"

        # Otherwise module is the first directory
        return parts[0]


# ── Hierarchy Extraction ───────────────────────────────────────────


def extract_hierarchies(
    symbols_by_file: dict[str, list[Symbol]],
) -> list[Hierarchy]:
    """Extract type hierarchies from symbol signatures.

    Detects three relationship types:
    - extends: class inherits from another class
    - implements: class implements an interface (TypeScript)
    - contains: type has fields referencing other known types

    Args:
        symbols_by_file: Dict mapping file paths to symbols.

    Returns:
        List of Hierarchy records.
    """
    # Build a set of all known type names for "contains" matching
    all_type_names: set[str] = set()
    all_symbols: list[Symbol] = []
    for syms in symbols_by_file.values():
        for s in syms:
            all_symbols.append(s)
            if s.kind in _KEY_TYPE_KINDS:
                all_type_names.add(s.name)

    hierarchies: list[Hierarchy] = []

    for sym in all_symbols:
        if sym.kind == "class":
            hierarchies.extend(_extract_extends_implements(sym))

        if sym.kind in _KEY_TYPE_KINDS:
            hierarchies.extend(_extract_contains(sym, all_type_names))

    return hierarchies


def _extract_extends_implements(sym: Symbol) -> list[Hierarchy]:
    """Extract extends/implements from a class symbol's signature."""
    results: list[Hierarchy] = []
    sig = sym.signature

    # Python extends: class Foo(Bar, Baz):
    py_match = _PY_EXTENDS_RE.match(sig)
    if py_match:
        bases_str = py_match.group(1)
        bases = [b.strip() for b in bases_str.split(",")]
        for base in bases:
            # Strip generic params: Base[T] -> Base
            base = re.sub(r"\[.*\]", "", base).strip()
            if base and base not in _IGNORED_BASES:
                results.append(
                    Hierarchy(
                        symbol=sym.fqn,
                        relationship="extends",
                        target=base,
                        file=sym.file,
                        line=sym.line,
                    )
                )
        return results

    # TypeScript extends
    ts_extends = _TS_EXTENDS_RE.search(sig)
    if ts_extends:
        target = ts_extends.group(1).strip()
        results.append(
            Hierarchy(
                symbol=sym.fqn,
                relationship="extends",
                target=target,
                file=sym.file,
                line=sym.line,
            )
        )

    # TypeScript implements (can coexist with extends)
    ts_impl = _TS_IMPLEMENTS_RE.search(sig)
    if ts_impl:
        ifaces_str = ts_impl.group(1)
        # Handle text up to `{` to avoid matching body content
        ifaces_str = ifaces_str.split("{")[0]
        ifaces = [i.strip() for i in ifaces_str.split(",")]
        for iface in ifaces:
            if iface:
                results.append(
                    Hierarchy(
                        symbol=sym.fqn,
                        relationship="implements",
                        target=iface,
                        file=sym.file,
                        line=sym.line,
                    )
                )

    return results


def _extract_contains(sym: Symbol, known_types: set[str]) -> list[Hierarchy]:
    """Extract 'contains' relationships from a type's signature/code.

    If a class/interface/struct has fields whose types reference other known
    types in the codebase, we record a 'contains' relationship.
    """
    results: list[Hierarchy] = []

    # We look at the full signature for type annotations
    sig = sym.signature
    matches = _CONTAINS_RE.findall(sig)

    seen: set[str] = set()
    for type_name in matches:
        type_name = type_name.strip()
        if (
            type_name
            and type_name in known_types
            and type_name not in _PRIMITIVE_TYPES
            and type_name != sym.name  # don't self-reference
            and type_name not in seen
        ):
            seen.add(type_name)
            results.append(
                Hierarchy(
                    symbol=sym.fqn,
                    relationship="contains",
                    target=type_name,
                    file=sym.file,
                    line=sym.line,
                )
            )

    return results


# ── Cross-Module Dependency Detection ──────────────────────────────


def detect_cross_module_deps(
    modules: list[Module],
    project_root: str,
) -> None:
    """Detect cross-module dependencies by scanning import statements.

    For each module, reads the source files and looks for imports that
    reference paths belonging to other modules. Mutates module.depends_on
    in place.

    Args:
        modules: List of Module objects from clustering.
        project_root: Absolute path to the project root.
    """
    # Build a map of module_path -> module_name for lookup
    mod_path_to_name: dict[str, str] = {}
    for mod in modules:
        mod_path_to_name[mod.path] = mod.name

    # For each module, scan its files for imports
    for mod in modules:
        deps: set[str] = set()
        files_in_module = {s.file for s in mod.symbols}

        for file_path in files_in_module:
            file_deps = _scan_file_imports(
                file_path, project_root, mod_path_to_name, mod.name
            )
            deps.update(file_deps)

        mod.depends_on = sorted(deps)


def _scan_file_imports(
    file_path: str,
    project_root: str,
    mod_path_to_name: dict[str, str],
    own_module_name: str,
) -> set[str]:
    """Scan a single file for imports that reference other modules.

    Returns set of module names this file depends on.
    """
    from pathlib import Path

    full_path = Path(project_root) / file_path
    if not full_path.exists():
        return set()

    try:
        content = full_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return set()

    deps: set[str] = set()
    suffix = Path(file_path).suffix

    if suffix == ".py":
        deps.update(_scan_python_imports(content, mod_path_to_name, own_module_name))
    elif suffix in (".ts", ".tsx", ".js", ".jsx"):
        deps.update(
            _scan_ts_imports(content, file_path, mod_path_to_name, own_module_name)
        )

    return deps


def _scan_python_imports(
    content: str,
    mod_path_to_name: dict[str, str],
    own_module_name: str,
) -> set[str]:
    """Extract module dependencies from Python import statements.

    Matches `from src.auth.login import X` style imports and checks
    if the import path falls under a known module.
    """
    deps: set[str] = set()

    for match in _PY_IMPORT_RE.finditer(content):
        import_path = match.group(1) or match.group(2)
        if not import_path:
            continue

        # Convert dotted path to slash path: src.auth.login -> src/auth/login
        slash_path = import_path.replace(".", "/")

        # Check if this import matches any known module path
        for mod_path, mod_name in mod_path_to_name.items():
            if mod_path == ".":
                continue
            if slash_path.startswith(mod_path) and mod_name != own_module_name:
                deps.add(mod_name)
                break

    return deps


def _scan_ts_imports(
    content: str,
    file_path: str,
    mod_path_to_name: dict[str, str],
    own_module_name: str,
) -> set[str]:
    """Extract module dependencies from TypeScript/JS import statements.

    Matches `import ... from './auth/login'` style imports and resolves
    the relative path to an absolute module path.
    """
    deps: set[str] = set()
    file_dir = str(PurePosixPath(file_path).parent)

    for match in _TS_IMPORT_RE.finditer(content):
        import_spec = match.group(1)
        if not import_spec:
            continue

        # Resolve relative import to absolute path from repo root
        resolved = str(PurePosixPath(file_dir) / import_spec)
        # Normalize .. and . in path
        resolved = str(PurePosixPath(resolved))
        # PurePosixPath doesn't resolve .., do it manually
        resolved = _normalize_posix_path(resolved)

        # Check against known module paths
        for mod_path, mod_name in mod_path_to_name.items():
            if mod_path == ".":
                continue
            if resolved.startswith(mod_path) and mod_name != own_module_name:
                deps.add(mod_name)
                break

    return deps


def _normalize_posix_path(path: str) -> str:
    """Normalize a POSIX path by resolving .. and . components."""
    parts = path.split("/")
    result: list[str] = []
    for part in parts:
        if part == "..":
            if result:
                result.pop()
        elif part != ".":
            result.append(part)
    return "/".join(result)
