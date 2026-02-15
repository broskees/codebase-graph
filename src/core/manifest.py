"""Manifest file parsing for dependency extraction.

Reads package manifests (package.json, pyproject.toml) and extracts
dependency information (name, version, runtime vs dev).
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # type: ignore[no-redef]


@dataclass(frozen=True, slots=True)
class Dependency:
    """A project dependency extracted from a manifest file.

    Attributes:
        name: Package name (e.g. "express", "pytest").
        version: Version spec (e.g. "^4.18.2", ">=8.0").
        category: Either "runtime" or "dev".
    """

    name: str
    version: str
    category: str  # "runtime" | "dev"


class ManifestParser:
    """Parses package manifests to extract dependency lists.

    Supports:
    - package.json (Node.js) — dependencies + devDependencies
    - pyproject.toml (Python) — project.dependencies + optional/dev deps
    """

    def parse(self, project_root: str | Path) -> list[Dependency]:
        """Parse all recognized manifest files in the project root.

        Args:
            project_root: Path to the project root directory.

        Returns:
            Combined list of dependencies from all found manifests.
        """
        root = Path(project_root)
        deps: list[Dependency] = []

        pkg_json = root / "package.json"
        if pkg_json.exists():
            deps.extend(self._parse_package_json(pkg_json))

        pyproject = root / "pyproject.toml"
        if pyproject.exists():
            deps.extend(self._parse_pyproject_toml(pyproject))

        return deps

    @staticmethod
    def _parse_package_json(path: Path) -> list[Dependency]:
        """Parse a package.json file for dependencies.

        Extracts from:
        - dependencies (-> runtime)
        - devDependencies (-> dev)
        """
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return []

        deps: list[Dependency] = []

        for name, version in data.get("dependencies", {}).items():
            deps.append(Dependency(name=name, version=version, category="runtime"))

        for name, version in data.get("devDependencies", {}).items():
            deps.append(Dependency(name=name, version=version, category="dev"))

        return deps

    @staticmethod
    def _parse_pyproject_toml(path: Path) -> list[Dependency]:
        """Parse a pyproject.toml file for dependencies.

        Extracts from:
        - [project.dependencies] (-> runtime)
        - [project.optional-dependencies.dev] (-> dev)
        - [tool.*.dev-dependencies] (-> dev) e.g. [tool.pdm.dev-dependencies]
        """
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
        except (Exception,):
            return []

        deps: list[Dependency] = []

        # [project.dependencies] — list of PEP 508 strings like "cased-kit>=3.5.0"
        project = data.get("project", {})
        for dep_str in project.get("dependencies", []):
            name, version = _parse_pep508(dep_str)
            deps.append(Dependency(name=name, version=version, category="runtime"))

        # [project.optional-dependencies] — check for "dev" group
        opt_deps = project.get("optional-dependencies", {})
        for group_name, group_deps in opt_deps.items():
            category = "dev" if _is_dev_group(group_name) else "runtime"
            for dep_str in group_deps:
                name, version = _parse_pep508(dep_str)
                deps.append(Dependency(name=name, version=version, category=category))

        # [tool.*.dev-dependencies] — PDM, Poetry dev groups
        tool = data.get("tool", {})
        for tool_name, tool_config in tool.items():
            if isinstance(tool_config, dict):
                dev_deps = tool_config.get("dev-dependencies", {})
                if isinstance(dev_deps, list):
                    # PDM style: list of strings
                    for dep_str in dev_deps:
                        name, version = _parse_pep508(dep_str)
                        deps.append(
                            Dependency(name=name, version=version, category="dev")
                        )
                elif isinstance(dev_deps, dict):
                    # Poetry style: {name = "version"}
                    for name, version_spec in dev_deps.items():
                        version = (
                            version_spec
                            if isinstance(version_spec, str)
                            else str(version_spec)
                        )
                        deps.append(
                            Dependency(name=name, version=version, category="dev")
                        )

        return deps


def _parse_pep508(dep_str: str) -> tuple[str, str]:
    """Parse a PEP 508 dependency string into (name, version).

    Examples:
        "cased-kit>=3.5.0"  -> ("cased-kit", ">=3.5.0")
        "pytest>=8.0"       -> ("pytest", ">=8.0")
        "requests"          -> ("requests", "*")
        "numpy[extra]>=1.0" -> ("numpy", ">=1.0")
    """
    dep_str = dep_str.strip()
    if not dep_str:
        return ("", "*")

    # Strip extras: numpy[extra] -> numpy
    # Split on version operators: >=, <=, ==, !=, ~=, >, <
    import re

    # Match name (possibly with extras) then version spec
    match = re.match(r"^([a-zA-Z0-9_.-]+)(?:\[.*?\])?\s*(.*)", dep_str)
    if not match:
        return (dep_str, "*")

    name = match.group(1).strip()
    version = match.group(2).strip()

    # Strip trailing environment markers: ; python_version >= "3.8"
    if ";" in version:
        version = version.split(";")[0].strip()

    return (name, version if version else "*")


def _is_dev_group(group_name: str) -> bool:
    """Check if an optional-dependencies group name is a dev group."""
    dev_names = {"dev", "test", "testing", "tests", "lint", "docs", "typing", "ci"}
    return group_name.lower() in dev_names
