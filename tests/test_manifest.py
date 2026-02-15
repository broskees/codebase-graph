"""Tests for manifest file parsing (package.json and pyproject.toml)."""

import json
import textwrap
from pathlib import Path

import pytest

from src.core.manifest import Dependency, ManifestParser, _parse_pep508, _is_dev_group


FIXTURES_ROOT = Path(__file__).parent / "fixtures"


# ── PEP 508 parsing unit tests ────────────────────────────────────


class TestParsePep508:
    def test_name_and_version(self):
        name, version = _parse_pep508("cased-kit>=3.5.0")
        assert name == "cased-kit"
        assert version == ">=3.5.0"

    def test_name_only(self):
        name, version = _parse_pep508("requests")
        assert name == "requests"
        assert version == "*"

    def test_with_extras(self):
        name, version = _parse_pep508("numpy[extra]>=1.0")
        assert name == "numpy"
        assert version == ">=1.0"

    def test_complex_version(self):
        name, version = _parse_pep508("django>=4.0,<5.0")
        assert name == "django"
        assert version == ">=4.0,<5.0"

    def test_with_env_marker(self):
        name, version = _parse_pep508('pywin32>=300; sys_platform == "win32"')
        assert name == "pywin32"
        assert version == ">=300"

    def test_empty_string(self):
        name, version = _parse_pep508("")
        assert name == ""
        assert version == "*"

    def test_whitespace(self):
        name, version = _parse_pep508("  pytest >= 8.0  ")
        assert name == "pytest"
        assert version == ">= 8.0"


class TestIsDevGroup:
    def test_dev(self):
        assert _is_dev_group("dev") is True

    def test_test(self):
        assert _is_dev_group("test") is True

    def test_docs(self):
        assert _is_dev_group("docs") is True

    def test_runtime_group(self):
        assert _is_dev_group("server") is False

    def test_case_insensitive(self):
        assert _is_dev_group("DEV") is True
        assert _is_dev_group("Test") is True


# ── package.json parsing ───────────────────────────────────────────


class TestParsePackageJson:
    def test_parses_ts_project_fixture(self):
        """Parse the ts_project fixture's package.json."""
        parser = ManifestParser()
        deps = parser.parse(FIXTURES_ROOT / "ts_project")

        names = {d.name for d in deps}
        assert "express" in names
        assert "typescript" in names

    def test_runtime_vs_dev(self):
        parser = ManifestParser()
        deps = parser.parse(FIXTURES_ROOT / "ts_project")

        runtime = {d.name for d in deps if d.category == "runtime"}
        dev = {d.name for d in deps if d.category == "dev"}

        assert "express" in runtime
        assert "pg" in runtime
        assert "typescript" in dev
        assert "jest" in dev

    def test_versions_preserved(self):
        parser = ManifestParser()
        deps = parser.parse(FIXTURES_ROOT / "ts_project")

        express = next(d for d in deps if d.name == "express")
        assert express.version == "^4.18.2"

    def test_from_temp_dir(self, tmp_path: Path):
        """Parse a dynamically created package.json."""
        pkg = {
            "name": "test",
            "dependencies": {"react": "^18.2.0"},
            "devDependencies": {"vitest": "^1.0.0"},
        }
        (tmp_path / "package.json").write_text(json.dumps(pkg))

        parser = ManifestParser()
        deps = parser.parse(tmp_path)
        assert len(deps) == 2

        react = next(d for d in deps if d.name == "react")
        assert react.category == "runtime"
        assert react.version == "^18.2.0"

        vitest = next(d for d in deps if d.name == "vitest")
        assert vitest.category == "dev"

    def test_empty_deps(self, tmp_path: Path):
        (tmp_path / "package.json").write_text('{"name": "empty"}')
        parser = ManifestParser()
        deps = parser.parse(tmp_path)
        assert deps == []

    def test_malformed_json(self, tmp_path: Path):
        (tmp_path / "package.json").write_text("not json at all")
        parser = ManifestParser()
        deps = parser.parse(tmp_path)
        assert deps == []


# ── pyproject.toml parsing ─────────────────────────────────────────


class TestParsePyprojectToml:
    def test_parses_py_project_fixture(self):
        """Parse the py_project fixture's pyproject.toml."""
        parser = ManifestParser()
        deps = parser.parse(FIXTURES_ROOT / "py_project")

        names = {d.name for d in deps}
        assert "fastapi" in names
        assert "pytest" in names

    def test_runtime_vs_dev(self):
        parser = ManifestParser()
        deps = parser.parse(FIXTURES_ROOT / "py_project")

        runtime = {d.name for d in deps if d.category == "runtime"}
        dev = {d.name for d in deps if d.category == "dev"}

        assert "fastapi" in runtime
        assert "sqlalchemy" in runtime
        assert "pydantic" in runtime
        assert "pytest" in dev
        assert "ruff" in dev

    def test_docs_group_is_not_dev(self):
        """The 'docs' group should be categorized as dev."""
        parser = ManifestParser()
        deps = parser.parse(FIXTURES_ROOT / "py_project")

        mkdocs = next(d for d in deps if d.name == "mkdocs")
        assert mkdocs.category == "dev"

    def test_versions_preserved(self):
        parser = ManifestParser()
        deps = parser.parse(FIXTURES_ROOT / "py_project")

        fastapi = next(d for d in deps if d.name == "fastapi")
        assert fastapi.version == ">=0.100.0"

    def test_our_own_pyproject(self):
        """Parse codebase-graph's own pyproject.toml."""
        parser = ManifestParser()
        project_root = Path(__file__).parent.parent
        deps = parser.parse(project_root)

        names = {d.name for d in deps}
        assert "cased-kit" in names

        kit_dep = next(d for d in deps if d.name == "cased-kit")
        assert kit_dep.category == "runtime"

    def test_from_temp_dir(self, tmp_path: Path):
        """Parse a dynamically created pyproject.toml."""
        toml_content = textwrap.dedent("""\
            [project]
            name = "test"
            dependencies = [
                "httpx>=0.24.0",
            ]

            [project.optional-dependencies]
            dev = [
                "black>=23.0",
            ]
        """)
        (tmp_path / "pyproject.toml").write_text(toml_content)

        parser = ManifestParser()
        deps = parser.parse(tmp_path)
        assert len(deps) == 2

        httpx = next(d for d in deps if d.name == "httpx")
        assert httpx.category == "runtime"

        black = next(d for d in deps if d.name == "black")
        assert black.category == "dev"

    def test_empty_project(self, tmp_path: Path):
        (tmp_path / "pyproject.toml").write_text('[project]\nname = "empty"\n')
        parser = ManifestParser()
        deps = parser.parse(tmp_path)
        assert deps == []


# ── Both manifests together ────────────────────────────────────────


class TestBothManifests:
    def test_no_manifests(self, tmp_path: Path):
        """A directory with no manifests returns empty list."""
        parser = ManifestParser()
        deps = parser.parse(tmp_path)
        assert deps == []

    def test_both_manifests_combined(self, tmp_path: Path):
        """When both package.json and pyproject.toml exist, deps are merged."""
        pkg = {"dependencies": {"express": "^4.0"}}
        (tmp_path / "package.json").write_text(json.dumps(pkg))

        toml = '[project]\nname = "test"\ndependencies = ["flask>=2.0"]\n'
        (tmp_path / "pyproject.toml").write_text(toml)

        parser = ManifestParser()
        deps = parser.parse(tmp_path)
        names = {d.name for d in deps}
        assert "express" in names
        assert "flask" in names


# ── Dependency dataclass tests ─────────────────────────────────────


class TestDependencyDataclass:
    def test_frozen(self):
        dep = Dependency(name="foo", version="1.0", category="runtime")
        with pytest.raises(AttributeError):
            dep.name = "bar"  # type: ignore

    def test_equality(self):
        a = Dependency(name="foo", version="1.0", category="runtime")
        b = Dependency(name="foo", version="1.0", category="runtime")
        assert a == b
