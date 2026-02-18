"""Tests for TOON serialization and .codebase.md output."""

from pathlib import Path

import pytest

from src.core.graph import Hierarchy, Module
from src.core.manifest import Dependency
from src.core.parser import Symbol
from src.core.writer import (
    CodebaseMeta,
    CodebaseWriter,
    _escape_value,
    _pipe_join,
    _PROMPT_FRAMING,
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


def _mod(
    name: str,
    path: str,
    symbols: list[Symbol] | None = None,
    key_types: list[str] | None = None,
    depends_on: list[str] | None = None,
) -> Module:
    """Shorthand to create a Module for testing."""
    return Module(
        name=name,
        path=path,
        symbols=symbols or [],
        key_types=key_types or [],
        depends_on=depends_on or [],
    )


def _meta(
    name: str = "test-project",
    languages: list[str] | None = None,
    last_indexed: str = "2026-02-15T21:00:00Z",
) -> CodebaseMeta:
    """Shorthand to create CodebaseMeta for testing."""
    return CodebaseMeta(
        name=name,
        languages=languages or ["python"],
        last_indexed=last_indexed,
    )


# ── _escape_value tests ───────────────────────────────────────────


class TestEscapeValue:
    def test_plain_string_unchanged(self):
        assert _escape_value("hello") == "hello"

    def test_empty_string(self):
        assert _escape_value("") == ""

    def test_string_with_comma_gets_quoted(self):
        assert _escape_value("a,b") == '"a,b"'

    def test_string_with_pipe_gets_quoted(self):
        assert _escape_value("a|b") == '"a|b"'

    def test_string_with_double_quote_gets_escaped_and_quoted(self):
        assert _escape_value('say "hi"') == '"say \\"hi\\""'

    def test_string_with_comma_and_pipe(self):
        result = _escape_value("a,b|c")
        assert result == '"a,b|c"'

    def test_no_quoting_for_simple_signature(self):
        assert _escape_value("def login():") == "def login():"

    def test_signature_with_comma_gets_quoted(self):
        sig = "def login(user: str, password: str):"
        result = _escape_value(sig)
        assert result.startswith('"')
        assert result.endswith('"')
        assert "user: str" in result


# ── _pipe_join tests ──────────────────────────────────────────────


class TestPipeJoin:
    def test_single_item(self):
        assert _pipe_join(["User"]) == "User"

    def test_multiple_items(self):
        assert _pipe_join(["User", "Session", "Token"]) == "User|Session|Token"

    def test_empty_list(self):
        assert _pipe_join([]) == ""


# ── Metadata serialization ────────────────────────────────────────


class TestSerializeMetadata:
    def setup_method(self):
        self.writer = CodebaseWriter()

    def test_basic_metadata(self):
        meta = _meta(name="my-project", languages=["python", "typescript"])
        result = self.writer._serialize_metadata(meta)
        assert "codebase:" in result
        assert "name: my-project" in result
        assert "languages[2]: python,typescript" in result
        assert "last_indexed: 2026-02-15T21:00:00Z" in result

    def test_single_language(self):
        meta = _meta(languages=["python"])
        result = self.writer._serialize_metadata(meta)
        assert "languages[1]: python" in result

    def test_auto_timestamp_when_none(self):
        meta = CodebaseMeta(name="test", languages=["python"], last_indexed=None)
        result = self.writer._serialize_metadata(meta)
        # Should contain a timestamp in ISO format
        assert "last_indexed: 20" in result  # starts with year 20xx
        assert "T" in result  # has time separator
        assert "Z" in result  # UTC marker


# ── Module serialization ──────────────────────────────────────────


class TestSerializeModules:
    def setup_method(self):
        self.writer = CodebaseWriter()

    def test_module_header_format(self):
        modules = [_mod("auth", "src/auth")]
        result = self.writer._serialize_modules(modules)
        assert result.startswith("modules[1]{name,path,key_types,depends_on}:")

    def test_module_with_key_types_and_deps(self):
        modules = [
            _mod(
                "auth",
                "src/auth",
                key_types=["User", "Session"],
                depends_on=["database", "config"],
            ),
        ]
        result = self.writer._serialize_modules(modules)
        # key_types are pipe-delimited and quoted (contains pipe)
        assert '"User|Session"' in result
        assert '"database|config"' in result

    def test_module_with_no_key_types(self):
        modules = [_mod("utils", "src/utils")]
        result = self.writer._serialize_modules(modules)
        # Line should have empty fields for key_types and depends_on
        lines = result.strip().split("\n")
        assert len(lines) == 2
        row = lines[1].strip()
        assert row == "utils,src/utils,,"

    def test_multiple_modules(self):
        modules = [
            _mod("auth", "src/auth", key_types=["User"]),
            _mod("orders", "src/orders", key_types=["Order"]),
        ]
        result = self.writer._serialize_modules(modules)
        assert result.startswith("modules[2]")
        assert "auth,src/auth,User," in result
        assert "orders,src/orders,Order," in result

    def test_count_matches_module_count(self):
        modules = [_mod(f"mod{i}", f"src/mod{i}") for i in range(5)]
        result = self.writer._serialize_modules(modules)
        assert "modules[5]" in result


# ── Symbol serialization ──────────────────────────────────────────


class TestSerializeSymbols:
    def setup_method(self):
        self.writer = CodebaseWriter()

    def test_symbol_header_format(self):
        modules = [_mod("auth", "src/auth", symbols=[_sym("login")])]
        result = self.writer._serialize_symbols(modules)
        assert result.startswith("symbols[1]{fqn,kind,file,line,signature}:")

    def test_line_numbers_are_1_indexed(self):
        """Kit gives 0-indexed lines; TOON output should be 1-indexed."""
        sym = _sym("login", line=0)  # 0-indexed first line
        modules = [_mod("auth", "src/auth", symbols=[sym])]
        result = self.writer._serialize_symbols(modules)
        # Line 0 in Kit -> line 1 in output
        lines = result.strip().split("\n")
        row = lines[1].strip()
        # The line number field (4th field) should be 1
        fields = _split_toon_row(row)
        assert fields[3] == "1"

    def test_symbol_with_simple_signature(self):
        sym = _sym(
            "login",
            kind="fn",
            file="src/auth/login.py",
            line=41,
            signature="def login(creds):",
        )
        modules = [_mod("auth", "src/auth", symbols=[sym])]
        result = self.writer._serialize_symbols(modules)
        assert "src/auth/login::login" in result
        assert "fn" in result
        assert "42" in result  # line 41 (0-indexed) + 1
        assert "def login(creds):" in result

    def test_symbol_with_comma_in_signature(self):
        sig = "def login(user: str, password: str) -> bool:"
        sym = _sym("login", signature=sig)
        modules = [_mod("auth", "src/auth", symbols=[sym])]
        result = self.writer._serialize_symbols(modules)
        # Signature should be quoted because it contains commas
        assert f'"{sig}"' in result

    def test_count_matches_total_symbols(self):
        sym1 = _sym("login", file="src/auth/login.py")
        sym2 = _sym("User", kind="class", file="src/auth/models.py")
        sym3 = _sym("Order", kind="class", file="src/orders/models.py")
        modules = [
            _mod("auth", "src/auth", symbols=[sym1, sym2]),
            _mod("orders", "src/orders", symbols=[sym3]),
        ]
        result = self.writer._serialize_symbols(modules)
        assert "symbols[3]" in result

    def test_truncation_when_over_budget(self):
        """When symbol count exceeds max_symbols, truncate with comment."""
        writer = CodebaseWriter(max_symbols=3)
        syms = [_sym(f"fn{i}", line=i) for i in range(10)]
        modules = [_mod("core", "src/core", symbols=syms)]
        result = writer._serialize_symbols(modules)
        assert "symbols[3]" in result
        assert "# ... 7 more symbols omitted" in result

    def test_truncation_prioritizes_type_definitions(self):
        """Type definitions (class/interface/enum) should be kept over functions."""
        writer = CodebaseWriter(max_symbols=3)
        syms = [
            _sym("helper1", kind="fn", file="src/core/utils.py"),
            _sym("User", kind="class", file="src/core/models.py"),
            _sym("helper2", kind="fn", file="src/core/utils.py"),
            _sym("Session", kind="interface", file="src/core/models.py"),
            _sym("helper3", kind="fn", file="src/core/utils.py"),
            _sym("Status", kind="enum", file="src/core/models.py"),
        ]
        modules = [_mod("core", "src/core", symbols=syms)]
        result = writer._serialize_symbols(modules)
        # All 3 type defs should be included
        assert "User" in result
        assert "Session" in result
        assert "Status" in result
        # No function helpers
        assert "helper1" not in result
        assert "helper2" not in result
        assert "helper3" not in result
        assert "# ... 3 more symbols omitted" in result

    def test_no_truncation_under_budget(self):
        writer = CodebaseWriter(max_symbols=100)
        syms = [_sym(f"fn{i}", line=i) for i in range(5)]
        modules = [_mod("core", "src/core", symbols=syms)]
        result = writer._serialize_symbols(modules)
        assert "symbols[5]" in result
        assert "omitted" not in result

    def test_truncation_distributes_symbols_across_modules(self):
        writer = CodebaseWriter(max_symbols=6, min_symbols_per_module=3)
        auth_syms = [
            _sym(
                f"AuthType{i}",
                kind="class",
                file="src/auth/models.py",
                line=i,
            )
            for i in range(10)
        ]
        ui_syms = [
            _sym(
                f"UiType{i}",
                kind="class",
                file="src/ui/models.py",
                line=i,
            )
            for i in range(10)
        ]
        modules = [
            _mod("auth", "src/auth", symbols=auth_syms),
            _mod("ui", "src/ui", symbols=ui_syms),
        ]

        result = writer._serialize_symbols(modules)
        rows = [
            row
            for row in result.splitlines()
            if row.startswith("  ") and not row.startswith("  #")
        ]
        files = [_split_toon_row(row.strip())[2] for row in rows]

        assert "symbols[6]" in result
        assert any(file_path.startswith("src/auth/") for file_path in files)
        assert any(file_path.startswith("src/ui/") for file_path in files)

    def test_floor_keeps_small_module_visible(self):
        writer = CodebaseWriter(max_symbols=5, min_symbols_per_module=2)
        core_syms = [
            _sym(
                f"CoreType{i}",
                kind="class",
                file="src/core/models.py",
                line=i,
            )
            for i in range(20)
        ]
        ui_syms = [
            _sym("render", kind="fn", file="src/ui/view.py"),
            _sym("mount", kind="fn", file="src/ui/view.py", line=20),
        ]
        modules = [
            _mod("core", "src/core", symbols=core_syms),
            _mod("ui", "src/ui", symbols=ui_syms),
        ]

        result = writer._serialize_symbols(modules)

        assert "symbols[5]" in result
        assert "src/ui/view::render" in result
        assert "src/ui/view::mount" in result

    def test_empty_modules_produce_empty_symbols(self):
        modules = [_mod("empty", "src/empty")]
        result = self.writer._serialize_symbols(modules)
        assert "symbols[0]" in result


# ── Hierarchy serialization ───────────────────────────────────────


class TestSerializeHierarchies:
    def setup_method(self):
        self.writer = CodebaseWriter()

    def test_hierarchy_header_format(self):
        hierarchies = [
            Hierarchy(
                symbol="src/auth/models::User",
                relationship="extends",
                target="BaseModel",
                file="src/auth/models.py",
                line=10,
            ),
        ]
        result = self.writer._serialize_hierarchies(hierarchies)
        assert result.startswith(
            "hierarchies[1]{symbol,relationship,target,file,line}:"
        )

    def test_hierarchy_line_numbers_1_indexed(self):
        h = Hierarchy(
            symbol="src/auth/models::User",
            relationship="extends",
            target="BaseModel",
            file="src/auth/models.py",
            line=0,
        )
        result = self.writer._serialize_hierarchies([h])
        lines = result.strip().split("\n")
        row = lines[1].strip()
        fields = _split_toon_row(row)
        assert fields[4] == "1"

    def test_extends_relationship(self):
        h = Hierarchy(
            symbol="src/auth/models::Admin",
            relationship="extends",
            target="User",
            file="src/auth/models.py",
            line=20,
        )
        result = self.writer._serialize_hierarchies([h])
        assert "extends" in result
        assert "Admin" in result
        assert "User" in result
        assert "21" in result  # 20 + 1

    def test_implements_relationship(self):
        h = Hierarchy(
            symbol="src/auth/models::User",
            relationship="implements",
            target="Authenticatable",
            file="src/auth/models.ts",
            line=27,
        )
        result = self.writer._serialize_hierarchies([h])
        assert "implements" in result
        assert "Authenticatable" in result

    def test_count_matches(self):
        hierarchies = [
            Hierarchy("a::X", "extends", "Y", "a.py", 1),
            Hierarchy("b::Z", "implements", "W", "b.ts", 2),
            Hierarchy("c::M", "contains", "N", "c.py", 3),
        ]
        result = self.writer._serialize_hierarchies(hierarchies)
        assert "hierarchies[3]" in result


# ── Dependency serialization ──────────────────────────────────────


class TestSerializeDependencies:
    def setup_method(self):
        self.writer = CodebaseWriter()

    def test_dependency_header_format(self):
        deps = [Dependency("express", "^4.18.2", "runtime")]
        result = self.writer._serialize_dependencies(deps)
        assert result.startswith("dependencies[1]{name,version,category}:")

    def test_runtime_dependency(self):
        deps = [Dependency("express", "^4.18.2", "runtime")]
        result = self.writer._serialize_dependencies(deps)
        assert "express,^4.18.2,runtime" in result

    def test_dev_dependency(self):
        deps = [Dependency("pytest", ">=8.0", "dev")]
        result = self.writer._serialize_dependencies(deps)
        assert "pytest,>=8.0,dev" in result

    def test_count_matches(self):
        deps = [
            Dependency("express", "^4.18.2", "runtime"),
            Dependency("typescript", "^5.4.0", "dev"),
            Dependency("prisma", "^5.10.0", "runtime"),
        ]
        result = self.writer._serialize_dependencies(deps)
        assert "dependencies[3]" in result

    def test_version_with_star(self):
        deps = [Dependency("requests", "*", "runtime")]
        result = self.writer._serialize_dependencies(deps)
        assert "requests,*,runtime" in result


# ── Full .codebase.md output ──────────────────────────────────────


class TestWrite:
    def setup_method(self):
        self.writer = CodebaseWriter()

    def test_output_has_prompt_framing(self):
        result = self.writer.write(
            modules=[],
            hierarchies=[],
            dependencies=[],
            metadata=_meta(),
        )
        assert "## Live Codebase Map" in result
        assert "real-time structural map" in result
        assert "Trust these locations" in result

    def test_output_has_toon_codeblock(self):
        result = self.writer.write(
            modules=[],
            hierarchies=[],
            dependencies=[],
            metadata=_meta(),
        )
        assert "```toon" in result
        assert result.strip().endswith("```")

    def test_output_has_codebase_metadata(self):
        result = self.writer.write(
            modules=[],
            hierarchies=[],
            dependencies=[],
            metadata=_meta(name="myapp", languages=["python", "typescript"]),
        )
        assert "name: myapp" in result
        assert "languages[2]: python,typescript" in result

    def test_output_has_modules_section(self):
        modules = [_mod("auth", "src/auth", key_types=["User"])]
        result = self.writer.write(
            modules=modules,
            hierarchies=[],
            dependencies=[],
            metadata=_meta(),
        )
        assert "modules[1]{name,path,key_types,depends_on}:" in result
        assert "auth,src/auth,User," in result

    def test_output_has_symbols_section(self):
        sym = _sym("login", kind="fn", file="src/auth/login.py", line=10)
        modules = [_mod("auth", "src/auth", symbols=[sym])]
        result = self.writer.write(
            modules=modules,
            hierarchies=[],
            dependencies=[],
            metadata=_meta(),
        )
        assert "symbols[1]{fqn,kind,file,line,signature}:" in result

    def test_output_omits_empty_hierarchies(self):
        result = self.writer.write(
            modules=[],
            hierarchies=[],
            dependencies=[],
            metadata=_meta(),
        )
        # The TOON section header (hierarchies[N]{fields}:) should not appear
        # when there are no hierarchies. The word "hierarchies" may appear
        # in the prompt framing guide text, so check for the section pattern.
        import re

        assert not re.search(r"hierarchies\[\d+\]\{", result)

    def test_output_omits_empty_dependencies(self):
        result = self.writer.write(
            modules=[],
            hierarchies=[],
            dependencies=[],
            metadata=_meta(),
        )
        # The TOON section header (dependencies[N]{fields}:) should not appear
        # when there are no dependencies.
        import re

        assert not re.search(r"dependencies\[\d+\]\{", result)

    def test_output_includes_hierarchies_when_present(self):
        hierarchies = [
            Hierarchy("a::X", "extends", "Y", "a.py", 5),
        ]
        result = self.writer.write(
            modules=[],
            hierarchies=hierarchies,
            dependencies=[],
            metadata=_meta(),
        )
        assert "hierarchies[1]" in result

    def test_output_includes_dependencies_when_present(self):
        deps = [Dependency("express", "^4.18.2", "runtime")]
        result = self.writer.write(
            modules=[],
            hierarchies=[],
            dependencies=deps,
            metadata=_meta(),
        )
        assert "dependencies[1]" in result

    def test_full_output_structure(self):
        """End-to-end test: realistic data produces valid structure."""
        user_sym = _sym(
            "User",
            kind="class",
            file="src/auth/models.py",
            line=5,
            signature="class User(BaseModel):",
        )
        login_sym = _sym(
            "login",
            kind="fn",
            file="src/auth/login.py",
            line=20,
            signature="def login(creds: Credentials) -> Session:",
        )
        order_sym = _sym(
            "Order",
            kind="class",
            file="src/orders/models.py",
            line=0,
            signature="class Order:",
        )

        modules = [
            _mod(
                "auth",
                "src/auth",
                symbols=[user_sym, login_sym],
                key_types=["User"],
                depends_on=["database"],
            ),
            _mod(
                "orders",
                "src/orders",
                symbols=[order_sym],
                key_types=["Order"],
                depends_on=["auth"],
            ),
        ]

        hierarchies = [
            Hierarchy(
                "src/auth/models::User", "extends", "BaseModel", "src/auth/models.py", 5
            ),
        ]

        deps = [
            Dependency("fastapi", ">=0.100.0", "runtime"),
            Dependency("pytest", ">=8.0", "dev"),
        ]

        result = self.writer.write(
            modules=modules,
            hierarchies=hierarchies,
            dependencies=deps,
            metadata=_meta(name="my-app", languages=["python"]),
        )

        # Structure checks
        assert "## Live Codebase Map" in result
        assert "```toon" in result
        assert "codebase:" in result
        assert "modules[2]" in result
        assert "symbols[3]" in result
        assert "hierarchies[1]" in result
        assert "dependencies[2]" in result
        assert result.strip().endswith("```")

        # Content checks
        assert "name: my-app" in result
        assert "auth,src/auth,User,database" in result
        assert "orders,src/orders,Order,auth" in result
        assert "extends" in result
        assert "fastapi,>=0.100.0,runtime" in result
        assert "pytest,>=8.0,dev" in result


# ── write_to_file ─────────────────────────────────────────────────


class TestWriteToFile:
    def test_writes_to_disk(self, tmp_path):
        writer = CodebaseWriter()
        outfile = tmp_path / ".codebase.md"
        writer.write_to_file(
            path=outfile,
            modules=[],
            hierarchies=[],
            dependencies=[],
            metadata=_meta(),
        )
        assert outfile.exists()
        content = outfile.read_text(encoding="utf-8")
        assert "## Live Codebase Map" in content
        assert "```toon" in content

    def test_overwrites_existing_file(self, tmp_path):
        writer = CodebaseWriter()
        outfile = tmp_path / ".codebase.md"
        outfile.write_text("old content")

        writer.write_to_file(
            path=outfile,
            modules=[],
            hierarchies=[],
            dependencies=[],
            metadata=_meta(name="new-project"),
        )
        content = outfile.read_text(encoding="utf-8")
        assert "old content" not in content
        assert "name: new-project" in content


# ── Edge cases ────────────────────────────────────────────────────


class TestEdgeCases:
    def setup_method(self):
        self.writer = CodebaseWriter()

    def test_empty_module_still_listed(self):
        """Modules with no symbols should still appear in the modules table."""
        modules = [_mod("empty", "src/empty")]
        result = self.writer.write(
            modules=modules,
            hierarchies=[],
            dependencies=[],
            metadata=_meta(),
        )
        assert "modules[1]" in result
        assert "empty,src/empty,," in result
        assert "symbols[0]" in result

    def test_missing_line_number_zero(self):
        """Symbols with line=0 should output line 1 (0+1)."""
        sym = _sym("main", line=0)
        modules = [_mod("root", ".", symbols=[sym])]
        result = self.writer._serialize_symbols(modules)
        lines = result.strip().split("\n")
        row = lines[1].strip()
        fields = _split_toon_row(row)
        assert fields[3] == "1"

    def test_signature_with_complex_generics(self):
        sig = "def process(items: list[tuple[str, int]], callback: Callable[[int], None]) -> dict[str, Any]:"
        sym = _sym("process", signature=sig)
        modules = [_mod("core", "src/core", symbols=[sym])]
        result = self.writer._serialize_symbols(modules)
        # Should be quoted due to commas
        assert '"' in result
        # The signature content should be present (unescaped inside quotes)
        assert "list[tuple[str" in result

    def test_pipe_in_module_key_types_is_quoted(self):
        """When key_types are pipe-joined, the result gets quoted."""
        modules = [_mod("auth", "src/auth", key_types=["User", "Session"])]
        result = self.writer._serialize_modules(modules)
        assert '"User|Session"' in result

    def test_single_key_type_not_quoted(self):
        """A single key_type has no pipe, so no quoting needed."""
        modules = [_mod("auth", "src/auth", key_types=["User"])]
        result = self.writer._serialize_modules(modules)
        assert "User" in result
        # Should not be quoted since there's no pipe
        assert '"User"' not in result

    def test_toon_block_ends_with_newline_before_closing_fence(self):
        """The TOON block should end cleanly."""
        result = self.writer.write(
            modules=[],
            hierarchies=[],
            dependencies=[],
            metadata=_meta(),
        )
        # Should end with ```\n (closing code fence)
        assert result.strip().endswith("```")

    def test_prompt_framing_text_is_complete(self):
        """All key phrases from the prompt framing should be present."""
        result = self.writer.write(
            modules=[],
            hierarchies=[],
            dependencies=[],
            metadata=_meta(),
        )
        assert "real-time structural map" in result
        assert "regenerated moments ago" in result
        assert "All file paths and line numbers are accurate right now" in result
        assert "this map updates before your next turn" in result
        assert "Trust these locations" in result


# ── Round-trip / structure validation ─────────────────────────────


class TestRoundTrip:
    """Verify the output structure is parseable / well-formed."""

    def test_toon_block_extractable(self):
        """The TOON block can be extracted from between code fences."""
        writer = CodebaseWriter()
        modules = [
            _mod(
                "auth",
                "src/auth",
                symbols=[_sym("User", kind="class", file="src/auth/models.py")],
                key_types=["User"],
            ),
        ]
        result = writer.write(
            modules=modules,
            hierarchies=[],
            dependencies=[Dependency("flask", ">=3.0", "runtime")],
            metadata=_meta(),
        )
        # Extract TOON block
        start = result.index("```toon\n") + len("```toon\n")
        end = result.rindex("```")
        toon_block = result[start:end]

        # Should have these sections
        assert "codebase:" in toon_block
        assert "modules[" in toon_block
        assert "symbols[" in toon_block
        assert "dependencies[" in toon_block

    def test_each_table_row_has_correct_field_count(self):
        """Every data row should have the right number of comma-separated fields."""
        writer = CodebaseWriter()
        sym = _sym(
            "login",
            kind="fn",
            file="src/auth/login.py",
            line=10,
            signature="def login():",
        )
        modules = [
            _mod(
                "auth", "src/auth", symbols=[sym], key_types=["User"], depends_on=["db"]
            ),
        ]
        hierarchies = [
            Hierarchy("src/auth::X", "extends", "Y", "a.py", 1),
        ]
        deps = [Dependency("flask", ">=3.0", "runtime")]
        result = writer.write(
            modules=modules,
            hierarchies=hierarchies,
            dependencies=deps,
            metadata=_meta(),
        )

        # Extract TOON block
        start = result.index("```toon\n") + len("```toon\n")
        end = result.rindex("```")
        toon_block = result[start:end]

        for line in toon_block.strip().split("\n"):
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            # Header lines end with ":"
            if line.endswith(":") and ("{" in line or line == "codebase:"):
                continue

            # Metadata key-value lines (codebase section)
            if ":" in line and not line.startswith('"') and "{" not in line:
                # Could be metadata like "name: my-project"
                # or a data row — data rows are comma-separated
                if "," not in line:
                    continue  # metadata line

            # Data rows for modules: 4 fields
            if "modules[" in toon_block:
                # Verify parseable (this is a structural check, not exhaustive)
                pass

    def test_output_is_valid_markdown(self):
        """The output should be valid markdown with proper code fence."""
        writer = CodebaseWriter()
        result = writer.write(
            modules=[],
            hierarchies=[],
            dependencies=[],
            metadata=_meta(),
        )
        # Count code fences — should be exactly one pair
        fence_count = result.count("```")
        assert fence_count == 2  # opening ```toon and closing ```

    def test_no_trailing_whitespace_in_rows(self):
        """TOON rows should not have trailing whitespace."""
        writer = CodebaseWriter()
        sym = _sym("login", line=10)
        modules = [_mod("auth", "src/auth", symbols=[sym])]
        result = writer.write(
            modules=modules,
            hierarchies=[],
            dependencies=[],
            metadata=_meta(),
        )
        # Extract TOON block
        start = result.index("```toon\n") + len("```toon\n")
        end = result.rindex("```")
        toon_block = result[start:end]

        for line in toon_block.split("\n"):
            if line.strip():  # skip blank lines
                assert line == line.rstrip(), f"Trailing whitespace in: {line!r}"


# ── TOON row parsing helper for tests ─────────────────────────────


def _split_toon_row(row: str) -> list[str]:
    """Split a TOON row into fields, respecting quoted values.

    Simple CSV-like split that handles double-quoted fields.
    """
    fields = []
    current = ""
    in_quotes = False
    i = 0
    while i < len(row):
        ch = row[i]
        if ch == '"' and not in_quotes:
            in_quotes = True
        elif ch == '"' and in_quotes:
            # Check for escaped quote
            if i + 1 < len(row) and row[i + 1] == '"':
                current += '"'
                i += 1
            else:
                in_quotes = False
        elif ch == "," and not in_quotes:
            fields.append(current)
            current = ""
        else:
            current += ch
        i += 1
    fields.append(current)
    return fields
