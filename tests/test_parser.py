"""Smoke tests for CodebaseParser wrapping Kit."""

from pathlib import Path

import pytest

from src.core.parser import CodebaseParser, Symbol, _normalize_kind, _make_fqn


# The repo root is the project root (where pyproject.toml lives)
REPO_ROOT = Path(__file__).parent.parent
FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def parser() -> CodebaseParser:
    """Create a parser pointed at our project root."""
    return CodebaseParser(REPO_ROOT)


# ── Helper unit tests ──────────────────────────────────────────────


class TestNormalizeKind:
    def test_function_to_fn(self):
        assert _normalize_kind("function") == "fn"

    def test_class_stays_class(self):
        assert _normalize_kind("class") == "class"

    def test_interface_stays(self):
        assert _normalize_kind("interface") == "interface"

    def test_method_stays(self):
        assert _normalize_kind("method") == "method"

    def test_unknown_passes_through(self):
        assert _normalize_kind("some_new_thing") == "some_new_thing"


class TestMakeFqn:
    def test_python_file(self):
        assert (
            _make_fqn("src/auth/login.py", "authenticate")
            == "src/auth/login::authenticate"
        )

    def test_typescript_file(self):
        assert (
            _make_fqn("src/auth/login.ts", "AuthService")
            == "src/auth/login::AuthService"
        )

    def test_nested_path(self):
        assert _make_fqn("a/b/c/d.tsx", "Foo") == "a/b/c/d::Foo"


# ── TypeScript fixture tests ───────────────────────────────────────


class TestParseTypeScript:
    def test_extracts_symbols_from_ts(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.ts")
        assert len(symbols) > 0, "Should extract at least one symbol from sample.ts"

    def test_finds_interface(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.ts")
        names = {s.name for s in symbols}
        assert "UserConfig" in names, f"Expected 'UserConfig' interface, got: {names}"

    def test_finds_class(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.ts")
        names = {s.name for s in symbols}
        assert "AuthService" in names, f"Expected 'AuthService' class, got: {names}"

    def test_finds_function(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.ts")
        names = {s.name for s in symbols}
        assert "createDefaultUser" in names, (
            f"Expected 'createDefaultUser' function, got: {names}"
        )

    def test_symbol_has_correct_file(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.ts")
        for sym in symbols:
            assert "sample.ts" in sym.file, (
                f"Symbol file should reference sample.ts, got: {sym.file}"
            )

    def test_symbol_has_line_numbers(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.ts")
        for sym in symbols:
            # Kit uses 0-indexed lines for some languages
            assert sym.line >= 0, (
                f"Symbol {sym.name} should have a non-negative line number"
            )
            assert sym.end_line >= sym.line, (
                f"Symbol {sym.name} end_line should be >= line"
            )

    def test_symbol_has_fqn(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.ts")
        for sym in symbols:
            assert "::" in sym.fqn, (
                f"Symbol {sym.name} FQN should contain '::', got: {sym.fqn}"
            )

    def test_symbol_has_signature(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.ts")
        # At least some symbols should have non-empty signatures
        signatures = [s.signature for s in symbols if s.signature]
        assert len(signatures) > 0, "At least some symbols should have signatures"


# ── Python fixture tests ──────────────────────────────────────────


class TestParsePython:
    def test_extracts_symbols_from_py(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.py")
        assert len(symbols) > 0, "Should extract at least one symbol from sample.py"

    def test_finds_class_config(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.py")
        names = {s.name for s in symbols}
        assert "Config" in names, f"Expected 'Config' class, got: {names}"

    def test_finds_class_app_server(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.py")
        names = {s.name for s in symbols}
        assert "AppServer" in names, f"Expected 'AppServer' class, got: {names}"

    def test_finds_function_create_app(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.py")
        names = {s.name for s in symbols}
        assert "create_app" in names, f"Expected 'create_app' function, got: {names}"

    def test_class_kind_is_correct(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.py")
        config_symbols = [s for s in symbols if s.name == "Config"]
        assert len(config_symbols) > 0
        assert config_symbols[0].kind == "class"

    def test_function_kind_is_correct(self, parser: CodebaseParser):
        symbols = parser.parse_file("tests/fixtures/sample.py")
        fn_symbols = [s for s in symbols if s.name == "create_app"]
        assert len(fn_symbols) > 0
        assert fn_symbols[0].kind == "fn"


# ── Directory parsing tests ───────────────────────────────────────


class TestParseDirectory:
    def test_parses_fixtures_directory(self, parser: CodebaseParser):
        result = parser.parse_directory(subpath="tests/fixtures")
        assert len(result) > 0, "Should find at least one file with symbols"

    def test_includes_ts_and_py_files(self, parser: CodebaseParser):
        result = parser.parse_directory(subpath="tests/fixtures")
        extensions = {Path(f).suffix for f in result.keys()}
        assert ".ts" in extensions or ".py" in extensions, (
            f"Should include .ts or .py files, got: {extensions}"
        )

    def test_skips_unsupported_extensions(self, parser: CodebaseParser):
        result = parser.parse_directory(subpath="tests/fixtures")
        for file_path in result.keys():
            suffix = Path(file_path).suffix
            assert suffix in {".ts", ".tsx", ".py"}, (
                f"Should only include supported extensions, got: {suffix}"
            )


# ── Edge case tests ───────────────────────────────────────────────


class TestEdgeCases:
    def test_unsupported_extension_returns_empty(self, parser: CodebaseParser):
        symbols = parser.parse_file("pyproject.toml")
        assert symbols == []

    def test_nonexistent_file_returns_empty(self, parser: CodebaseParser):
        # Kit should handle this gracefully
        symbols = parser.parse_file("does_not_exist.py")
        assert symbols == []

    def test_symbol_is_frozen_dataclass(self):
        sym = Symbol(
            name="test",
            kind="fn",
            file="test.py",
            line=1,
            end_line=5,
            signature="def test():",
            fqn="test::test",
        )
        with pytest.raises(AttributeError):
            sym.name = "changed"  # type: ignore
