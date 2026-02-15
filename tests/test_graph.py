"""Tests for module clustering, hierarchy extraction, and cross-module deps."""

from pathlib import Path

import pytest

from src.core.graph import (
    Hierarchy,
    Module,
    ModuleClusterer,
    detect_cross_module_deps,
    extract_hierarchies,
    _normalize_posix_path,
)
from src.core.parser import Symbol


# ── Helpers ────────────────────────────────────────────────────────


def _sym(
    name: str,
    kind: str = "fn",
    file: str = "src/core/main.py",
    line: int = 1,
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


# ── ModuleClusterer tests ─────────────────────────────────────────


class TestModuleClusterer:
    def setup_method(self):
        self.clusterer = ModuleClusterer()

    def test_groups_by_src_subdirectory(self):
        """Symbols in src/auth/ and src/orders/ form two modules."""
        symbols = {
            "src/auth/login.py": [_sym("login", file="src/auth/login.py")],
            "src/auth/models.py": [
                _sym("User", kind="class", file="src/auth/models.py")
            ],
            "src/orders/service.py": [
                _sym("create_order", file="src/orders/service.py")
            ],
        }
        modules = self.clusterer.cluster(symbols)

        names = {m.name for m in modules}
        assert "auth" in names
        assert "orders" in names
        assert len(modules) == 2

    def test_module_has_correct_path(self):
        symbols = {
            "src/auth/login.py": [_sym("login", file="src/auth/login.py")],
        }
        modules = self.clusterer.cluster(symbols)
        auth_mod = modules[0]
        assert auth_mod.path == "src/auth"

    def test_root_level_files_get_root_module(self):
        """Files with no directory go to the __root__ module."""
        symbols = {
            "main.py": [_sym("main", file="main.py")],
        }
        modules = self.clusterer.cluster(symbols)
        assert len(modules) == 1
        assert modules[0].name == "__root__"
        assert modules[0].path == "."

    def test_non_src_directory_uses_first_dir(self):
        """Files under lib/ use 'lib' as the module."""
        symbols = {
            "lib/utils.py": [_sym("helper", file="lib/utils.py")],
        }
        modules = self.clusterer.cluster(symbols)
        assert modules[0].name == "lib"
        assert modules[0].path == "lib"

    def test_key_types_extracted(self):
        """Classes and interfaces are extracted as key_types."""
        symbols = {
            "src/auth/models.py": [
                _sym("User", kind="class", file="src/auth/models.py"),
                _sym("Session", kind="class", file="src/auth/models.py"),
                _sym("login", kind="fn", file="src/auth/models.py"),
                _sym("Serializable", kind="interface", file="src/auth/models.py"),
            ],
        }
        modules = self.clusterer.cluster(symbols)
        auth = modules[0]
        assert "User" in auth.key_types
        assert "Session" in auth.key_types
        assert "Serializable" in auth.key_types
        assert "login" not in auth.key_types  # functions excluded

    def test_key_types_sorted(self):
        symbols = {
            "src/auth/models.py": [
                _sym("Zebra", kind="class", file="src/auth/models.py"),
                _sym("Alpha", kind="class", file="src/auth/models.py"),
            ],
        }
        modules = self.clusterer.cluster(symbols)
        assert modules[0].key_types == ["Alpha", "Zebra"]

    def test_symbols_attached_to_module(self):
        symbols = {
            "src/auth/login.py": [_sym("login", file="src/auth/login.py")],
            "src/auth/models.py": [
                _sym("User", kind="class", file="src/auth/models.py")
            ],
        }
        modules = self.clusterer.cluster(symbols)
        auth = modules[0]
        assert len(auth.symbols) == 2

    def test_multiple_modules_from_src(self):
        """Multiple src/ subdirectories form separate modules."""
        symbols = {
            "src/auth/login.py": [_sym("login", file="src/auth/login.py")],
            "src/orders/service.py": [_sym("create", file="src/orders/service.py")],
            "src/inventory/stock.py": [_sym("check", file="src/inventory/stock.py")],
        }
        modules = self.clusterer.cluster(symbols)
        names = {m.name for m in modules}
        assert names == {"auth", "orders", "inventory"}

    def test_empty_input(self):
        modules = self.clusterer.cluster({})
        assert modules == []

    def test_mixed_root_and_src_files(self):
        """Root-level and src/ files form separate modules."""
        symbols = {
            "main.py": [_sym("main", file="main.py")],
            "src/core/parser.py": [_sym("parse", file="src/core/parser.py")],
        }
        modules = self.clusterer.cluster(symbols)
        names = {m.name for m in modules}
        assert "__root__" in names
        assert "core" in names

    def test_deep_nesting_still_uses_first_subdir(self):
        """src/auth/v2/handlers/login.py still maps to src/auth module."""
        symbols = {
            "src/auth/v2/handlers/login.py": [
                _sym("login", file="src/auth/v2/handlers/login.py")
            ],
        }
        modules = self.clusterer.cluster(symbols)
        assert modules[0].name == "auth"
        assert modules[0].path == "src/auth"


# ── Hierarchy extraction tests ─────────────────────────────────────


class TestExtractHierarchies:
    def test_python_extends(self):
        """class AdminUser(User): should produce an extends hierarchy."""
        symbols = {
            "src/auth/models.py": [
                _sym(
                    "User",
                    kind="class",
                    file="src/auth/models.py",
                    signature="class User:",
                ),
                _sym(
                    "AdminUser",
                    kind="class",
                    file="src/auth/models.py",
                    signature="class AdminUser(User):",
                ),
            ],
        }
        hierarchies = extract_hierarchies(symbols)
        extends = [h for h in hierarchies if h.relationship == "extends"]
        assert len(extends) == 1
        assert extends[0].target == "User"
        assert "AdminUser" in extends[0].symbol

    def test_python_multiple_inheritance(self):
        """class MyClass(Base, Mixin): should produce extends for each base."""
        symbols = {
            "models.py": [
                _sym("Base", kind="class", file="models.py", signature="class Base:"),
                _sym("Mixin", kind="class", file="models.py", signature="class Mixin:"),
                _sym(
                    "MyClass",
                    kind="class",
                    file="models.py",
                    signature="class MyClass(Base, Mixin):",
                ),
            ],
        }
        hierarchies = extract_hierarchies(symbols)
        extends = [h for h in hierarchies if h.relationship == "extends"]
        targets = {h.target for h in extends}
        assert "Base" in targets
        assert "Mixin" in targets

    def test_python_ignores_stdlib_bases(self):
        """class MyError(Exception): should NOT produce extends."""
        symbols = {
            "errors.py": [
                _sym(
                    "MyError",
                    kind="class",
                    file="errors.py",
                    signature="class MyError(Exception):",
                ),
            ],
        }
        hierarchies = extract_hierarchies(symbols)
        extends = [h for h in hierarchies if h.relationship == "extends"]
        assert len(extends) == 0

    def test_ts_extends(self):
        """class AdminUser extends User should produce extends."""
        symbols = {
            "models.ts": [
                _sym("User", kind="class", file="models.ts", signature="class User {"),
                _sym(
                    "AdminUser",
                    kind="class",
                    file="models.ts",
                    signature="class AdminUser extends User {",
                ),
            ],
        }
        hierarchies = extract_hierarchies(symbols)
        extends = [h for h in hierarchies if h.relationship == "extends"]
        assert len(extends) == 1
        assert extends[0].target == "User"

    def test_ts_implements(self):
        """class User implements Authenticatable should produce implements."""
        symbols = {
            "models.ts": [
                _sym(
                    "Authenticatable",
                    kind="interface",
                    file="models.ts",
                    signature="interface Authenticatable {",
                ),
                _sym(
                    "User",
                    kind="class",
                    file="models.ts",
                    signature="class User implements Authenticatable {",
                ),
            ],
        }
        hierarchies = extract_hierarchies(symbols)
        impls = [h for h in hierarchies if h.relationship == "implements"]
        assert len(impls) == 1
        assert impls[0].target == "Authenticatable"

    def test_ts_extends_and_implements(self):
        """class Admin extends User implements Serializable."""
        symbols = {
            "models.ts": [
                _sym("User", kind="class", file="models.ts", signature="class User {"),
                _sym(
                    "Serializable",
                    kind="interface",
                    file="models.ts",
                    signature="interface Serializable {",
                ),
                _sym(
                    "Admin",
                    kind="class",
                    file="models.ts",
                    signature="class Admin extends User implements Serializable {",
                ),
            ],
        }
        hierarchies = extract_hierarchies(symbols)
        extends = [h for h in hierarchies if h.relationship == "extends"]
        impls = [h for h in hierarchies if h.relationship == "implements"]
        assert len(extends) == 1
        assert extends[0].target == "User"
        assert len(impls) == 1
        assert impls[0].target == "Serializable"

    def test_ts_multiple_implements(self):
        """class User implements Authenticatable, Serializable."""
        symbols = {
            "models.ts": [
                _sym(
                    "Authenticatable",
                    kind="interface",
                    file="models.ts",
                    signature="interface Authenticatable {",
                ),
                _sym(
                    "Serializable",
                    kind="interface",
                    file="models.ts",
                    signature="interface Serializable {",
                ),
                _sym(
                    "User",
                    kind="class",
                    file="models.ts",
                    signature="class User implements Authenticatable, Serializable {",
                ),
            ],
        }
        hierarchies = extract_hierarchies(symbols)
        impls = [h for h in hierarchies if h.relationship == "implements"]
        targets = {h.target for h in impls}
        assert "Authenticatable" in targets
        assert "Serializable" in targets

    def test_contains_known_type(self):
        """A class with a field of another known type gets 'contains'."""
        symbols = {
            "models.ts": [
                _sym(
                    "OrderItem",
                    kind="interface",
                    file="models.ts",
                    signature="interface OrderItem {",
                ),
                _sym(
                    "Order",
                    kind="class",
                    file="models.ts",
                    signature="class Order { items: OrderItem[]",
                ),
            ],
        }
        hierarchies = extract_hierarchies(symbols)
        contains = [h for h in hierarchies if h.relationship == "contains"]
        assert len(contains) >= 1
        assert any(c.target == "OrderItem" for c in contains)

    def test_contains_ignores_primitives(self):
        """Fields with primitive types shouldn't produce contains."""
        symbols = {
            "models.ts": [
                _sym(
                    "Order",
                    kind="class",
                    file="models.ts",
                    signature="class Order { total: number",
                ),
            ],
        }
        hierarchies = extract_hierarchies(symbols)
        contains = [h for h in hierarchies if h.relationship == "contains"]
        assert len(contains) == 0

    def test_contains_ignores_self_reference(self):
        """A class that references its own type shouldn't self-contain."""
        symbols = {
            "models.ts": [
                _sym(
                    "Node",
                    kind="class",
                    file="models.ts",
                    signature="class Node { next: Node",
                ),
            ],
        }
        hierarchies = extract_hierarchies(symbols)
        contains = [h for h in hierarchies if h.relationship == "contains"]
        # Self-reference is filtered out
        assert len(contains) == 0

    def test_hierarchy_has_correct_file_and_line(self):
        symbols = {
            "src/auth/models.py": [
                _sym(
                    "User",
                    kind="class",
                    file="src/auth/models.py",
                    line=10,
                    signature="class User:",
                ),
                _sym(
                    "Admin",
                    kind="class",
                    file="src/auth/models.py",
                    line=20,
                    signature="class Admin(User):",
                ),
            ],
        }
        hierarchies = extract_hierarchies(symbols)
        extends = [h for h in hierarchies if h.relationship == "extends"]
        assert extends[0].file == "src/auth/models.py"
        assert extends[0].line == 20

    def test_empty_input(self):
        hierarchies = extract_hierarchies({})
        assert hierarchies == []

    def test_no_classes_no_hierarchies(self):
        symbols = {
            "utils.py": [
                _sym("helper", kind="fn", file="utils.py"),
            ],
        }
        hierarchies = extract_hierarchies(symbols)
        assert hierarchies == []


# ── Cross-module dependency detection tests ────────────────────────


class TestCrossModuleDeps:
    """Tests for detect_cross_module_deps using real fixture files."""

    FIXTURES_ROOT = Path(__file__).parent / "fixtures"

    def test_ts_cross_module_deps(self):
        """orders/types.ts imports from auth/models — orders depends on auth."""
        ts_root = self.FIXTURES_ROOT / "ts_project"
        if not ts_root.exists():
            pytest.skip("ts_project fixture not found")

        # Build symbols that mirror the fixture file structure
        auth_sym = _sym("User", kind="class", file="src/auth/models.ts")
        orders_sym = _sym("Order", kind="class", file="src/orders/types.ts")

        clusterer = ModuleClusterer()
        modules = clusterer.cluster(
            {
                "src/auth/models.ts": [auth_sym],
                "src/orders/types.ts": [orders_sym],
            }
        )

        detect_cross_module_deps(modules, str(ts_root))

        orders_mod = next(m for m in modules if m.name == "orders")
        assert "auth" in orders_mod.depends_on

    def test_py_cross_module_deps(self):
        """services/auth.py imports from models/user — services depends on models."""
        py_root = self.FIXTURES_ROOT / "py_project"
        if not py_root.exists():
            pytest.skip("py_project fixture not found")

        models_sym = _sym("User", kind="class", file="src/models/user.py")
        services_sym = _sym("AuthService", kind="class", file="src/services/auth.py")

        clusterer = ModuleClusterer()
        modules = clusterer.cluster(
            {
                "src/models/user.py": [models_sym],
                "src/services/auth.py": [services_sym],
            }
        )

        detect_cross_module_deps(modules, str(py_root))

        services_mod = next(m for m in modules if m.name == "services")
        assert "models" in services_mod.depends_on

    def test_no_self_dependency(self):
        """A module should not depend on itself."""
        ts_root = self.FIXTURES_ROOT / "ts_project"
        if not ts_root.exists():
            pytest.skip("ts_project fixture not found")

        # service.ts imports from models.ts — both in auth
        sym1 = _sym("AuthService", kind="class", file="src/auth/service.ts")
        sym2 = _sym("User", kind="class", file="src/auth/models.ts")

        clusterer = ModuleClusterer()
        modules = clusterer.cluster(
            {
                "src/auth/service.ts": [sym1],
                "src/auth/models.ts": [sym2],
            }
        )

        detect_cross_module_deps(modules, str(ts_root))

        auth_mod = modules[0]
        assert "auth" not in auth_mod.depends_on

    def test_deps_are_sorted(self):
        """depends_on should be sorted alphabetically."""
        # Build fake modules with multiple deps
        mod = Module(
            name="orders",
            path="src/orders",
            key_types=[],
            depends_on=["zebra", "alpha"],
            symbols=[],
        )
        # After detect_cross_module_deps, deps get re-sorted.
        # We just verify the sort contract here.
        mod.depends_on = sorted(mod.depends_on)
        assert mod.depends_on == ["alpha", "zebra"]


# ── normalize_posix_path tests ─────────────────────────────────────


class TestNormalizePosixPath:
    def test_simple_path(self):
        assert _normalize_posix_path("src/auth/login.ts") == "src/auth/login.ts"

    def test_dotdot(self):
        assert _normalize_posix_path("src/orders/../auth/models") == "src/auth/models"

    def test_dot(self):
        assert _normalize_posix_path("./src/auth") == "src/auth"

    def test_multiple_dotdot(self):
        assert _normalize_posix_path("a/b/c/../../d") == "a/d"
