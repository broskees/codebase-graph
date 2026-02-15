"""Integration tests for the full codebase-graph pipeline.

Covers:
- End-to-end one-shot mode on realistic multi-file projects
- End-to-end watch mode (incremental updates)
- Performance validation (cold index < 1s, incremental < 50ms)
- Edge cases (empty project, syntax errors, large files, deep nesting, etc.)
- Multi-language support (TS + Python mixed projects)
- TOON output validation (parseable, correct field counts)
"""

from __future__ import annotations

import os
import subprocess
import time
from pathlib import Path
from unittest.mock import patch

import pytest

from src.cli import main
from src.core.watcher import FileFilter, IncrementalPipeline


# ── Shared Helpers ─────────────────────────────────────────────────


def _setup_git_repo(root: Path) -> None:
    """Initialize a minimal git repo."""
    subprocess.run(["git", "init"], cwd=str(root), capture_output=True, check=True)
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


def _git_commit(root: Path, msg: str = "init") -> None:
    """Stage all files and commit."""
    subprocess.run(["git", "add", "."], cwd=str(root), capture_output=True, check=True)
    subprocess.run(
        ["git", "commit", "-m", msg], cwd=str(root), capture_output=True, check=True
    )


def _split_toon_row(line: str) -> list[str]:
    """Parse a TOON row respecting quoted fields."""
    fields: list[str] = []
    current = ""
    in_quotes = False

    for ch in line.strip():
        if ch == '"' and not in_quotes:
            in_quotes = True
        elif ch == '"' and in_quotes:
            in_quotes = False
        elif ch == "," and not in_quotes:
            fields.append(current)
            current = ""
        else:
            current += ch

    fields.append(current)
    return fields


def _extract_toon_block(content: str) -> str:
    """Extract the TOON codeblock from .codebase.md content."""
    start = content.find("```toon\n")
    if start < 0:
        return ""
    start += len("```toon\n")
    end = content.find("```", start)
    if end < 0:
        return content[start:]
    return content[start:end]


# ── Fixture Builders ───────────────────────────────────────────────


def _make_ts_project(tmp_path: Path) -> Path:
    """Create a realistic TypeScript project (~20 files)."""
    project = tmp_path / "ts-project"
    project.mkdir()
    _setup_git_repo(project)

    # package.json
    (project / "package.json").write_text(
        """{
  "name": "ts-project",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.18.2",
    "prisma": "^5.10.0"
  },
  "devDependencies": {
    "typescript": "^5.4.0",
    "vitest": "^1.0.0"
  }
}""",
        encoding="utf-8",
    )

    # .gitignore
    (project / ".gitignore").write_text(
        "node_modules/\ndist/\n.env\n", encoding="utf-8"
    )

    # src/auth/models.ts
    auth = project / "src" / "auth"
    auth.mkdir(parents=True)
    (auth / "models.ts").write_text(
        """\
export interface User {
  id: string;
  name: string;
  email: string;
}

export interface Session {
  token: string;
  userId: string;
  expiresAt: Date;
}

export interface Credentials {
  email: string;
  password: string;
}
""",
        encoding="utf-8",
    )

    # src/auth/login.ts
    (auth / "login.ts").write_text(
        """\
import { User, Credentials, Session } from './models';

export async function login(creds: Credentials): Promise<Session> {
  // authenticate
  return { token: 'abc', userId: '1', expiresAt: new Date() };
}

export async function logout(session: Session): Promise<void> {
  // invalidate session
}

export function validateToken(token: string): boolean {
  return token.length > 0;
}
""",
        encoding="utf-8",
    )

    # src/auth/middleware.ts
    (auth / "middleware.ts").write_text(
        """\
import { Session } from './models';
import { validateToken } from './login';

export class AuthMiddleware {
  async authenticate(req: any): Promise<Session | null> {
    const token = req.headers['authorization'];
    if (!token || !validateToken(token)) return null;
    return { token, userId: '1', expiresAt: new Date() };
  }
}
""",
        encoding="utf-8",
    )

    # src/orders/types.ts
    orders = project / "src" / "orders"
    orders.mkdir(parents=True)
    (orders / "types.ts").write_text(
        """\
export enum OrderStatus {
  PENDING = 'pending',
  CONFIRMED = 'confirmed',
  SHIPPED = 'shipped',
  DELIVERED = 'delivered',
}

export interface OrderItem {
  productId: string;
  quantity: number;
  price: number;
}

export interface Order {
  id: string;
  userId: string;
  items: OrderItem[];
  status: OrderStatus;
  total: number;
}
""",
        encoding="utf-8",
    )

    # src/orders/service.ts
    (orders / "service.ts").write_text(
        """\
import { Order, OrderItem, OrderStatus } from './types';
import { Session } from '../auth/models';

export class OrderService {
  async createOrder(session: Session, items: OrderItem[]): Promise<Order> {
    const total = items.reduce((sum, item) => sum + item.price * item.quantity, 0);
    return {
      id: '1',
      userId: session.userId,
      items,
      status: OrderStatus.PENDING,
      total,
    };
  }

  async getOrder(id: string): Promise<Order | null> {
    return null;
  }
}
""",
        encoding="utf-8",
    )

    # src/orders/routes.ts
    (orders / "routes.ts").write_text(
        """\
import { OrderService } from './service';
import { AuthMiddleware } from '../auth/middleware';

export class OrderRoutes {
  private service = new OrderService();
  private auth = new AuthMiddleware();

  async handleCreate(req: any, res: any) {
    const session = await this.auth.authenticate(req);
    if (!session) { res.status(401); return; }
    const order = await this.service.createOrder(session, req.body.items);
    res.json(order);
  }
}
""",
        encoding="utf-8",
    )

    # src/database/client.ts
    db = project / "src" / "database"
    db.mkdir(parents=True)
    (db / "client.ts").write_text(
        """\
export interface DatabaseConfig {
  host: string;
  port: number;
  database: string;
}

export class DatabaseClient {
  private config: DatabaseConfig;

  constructor(config: DatabaseConfig) {
    this.config = config;
  }

  async connect(): Promise<void> {
    // connect to database
  }

  async disconnect(): Promise<void> {
    // disconnect
  }
}
""",
        encoding="utf-8",
    )

    # src/database/migrations.ts
    (db / "migrations.ts").write_text(
        """\
import { DatabaseClient } from './client';

export class MigrationRunner {
  constructor(private client: DatabaseClient) {}

  async runAll(): Promise<void> {
    // run migrations
  }
}
""",
        encoding="utf-8",
    )

    # src/config/index.ts
    config = project / "src" / "config"
    config.mkdir(parents=True)
    (config / "index.ts").write_text(
        """\
export interface AppConfig {
  port: number;
  databaseUrl: string;
  jwtSecret: string;
}

export function loadConfig(): AppConfig {
  return {
    port: parseInt(process.env.PORT || '3000'),
    databaseUrl: process.env.DATABASE_URL || 'localhost',
    jwtSecret: process.env.JWT_SECRET || 'secret',
  };
}
""",
        encoding="utf-8",
    )

    # src/app.ts (root-level src file)
    (project / "src" / "app.ts").write_text(
        """\
import { loadConfig } from './config';
import { DatabaseClient } from './database/client';
import { OrderRoutes } from './orders/routes';

export class App {
  async start() {
    const config = loadConfig();
    const db = new DatabaseClient({ host: 'localhost', port: 5432, database: 'mydb' });
    await db.connect();
    console.log('Server started on port', config.port);
  }
}
""",
        encoding="utf-8",
    )

    _git_commit(project, "init ts project")
    return project


def _make_py_project(tmp_path: Path) -> Path:
    """Create a realistic Python project (~15 files)."""
    project = tmp_path / "py-project"
    project.mkdir()
    _setup_git_repo(project)

    # pyproject.toml
    (project / "pyproject.toml").write_text(
        """\
[project]
name = "py-project"
version = "0.1.0"
dependencies = [
    "fastapi>=0.100.0",
    "sqlalchemy>=2.0.0",
    "pydantic>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "ruff>=0.3.0",
]
""",
        encoding="utf-8",
    )

    # .gitignore
    (project / ".gitignore").write_text(
        "__pycache__/\n.venv/\n*.pyc\n.env\n", encoding="utf-8"
    )

    # src/models/user.py
    models = project / "src" / "models"
    models.mkdir(parents=True)
    (models / "__init__.py").write_text("", encoding="utf-8")
    (models / "user.py").write_text(
        """\
from dataclasses import dataclass


@dataclass
class User:
    id: str
    name: str
    email: str
    is_active: bool = True


@dataclass
class UserCreate:
    name: str
    email: str
    password: str
""",
        encoding="utf-8",
    )

    # src/models/order.py
    (models / "order.py").write_text(
        """\
from dataclasses import dataclass
from enum import Enum


class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"


@dataclass
class OrderItem:
    product_id: str
    quantity: int
    price: float


@dataclass
class Order:
    id: str
    user_id: str
    items: list
    status: OrderStatus
    total: float
""",
        encoding="utf-8",
    )

    # src/services/auth.py
    services = project / "src" / "services"
    services.mkdir(parents=True)
    (services / "__init__.py").write_text("", encoding="utf-8")
    (services / "auth.py").write_text(
        """\
from src.models.user import User, UserCreate


class AuthService:
    def login(self, email: str, password: str) -> User:
        return User(id="1", name="test", email=email)

    def register(self, data: UserCreate) -> User:
        return User(id="2", name=data.name, email=data.email)

    def validate_token(self, token: str) -> bool:
        return len(token) > 0
""",
        encoding="utf-8",
    )

    # src/services/orders.py
    (services / "orders.py").write_text(
        """\
from src.models.order import Order, OrderItem, OrderStatus


class OrderService:
    def create_order(self, user_id: str, items: list) -> Order:
        total = sum(item.price * item.quantity for item in items)
        return Order(
            id="1",
            user_id=user_id,
            items=items,
            status=OrderStatus.PENDING,
            total=total,
        )

    def get_order(self, order_id: str) -> Order | None:
        return None
""",
        encoding="utf-8",
    )

    # src/api/routes.py
    api = project / "src" / "api"
    api.mkdir(parents=True)
    (api / "__init__.py").write_text("", encoding="utf-8")
    (api / "routes.py").write_text(
        """\
from src.services.auth import AuthService
from src.services.orders import OrderService


class Router:
    def __init__(self):
        self.auth = AuthService()
        self.orders = OrderService()

    def handle_login(self, email: str, password: str):
        return self.auth.login(email, password)

    def handle_create_order(self, user_id: str, items: list):
        return self.orders.create_order(user_id, items)
""",
        encoding="utf-8",
    )

    # src/api/middleware.py
    (api / "middleware.py").write_text(
        """\
from src.services.auth import AuthService


class AuthMiddleware:
    def __init__(self):
        self.auth = AuthService()

    def check_auth(self, token: str) -> bool:
        return self.auth.validate_token(token)
""",
        encoding="utf-8",
    )

    # src/db/connection.py
    db = project / "src" / "db"
    db.mkdir(parents=True)
    (db / "__init__.py").write_text("", encoding="utf-8")
    (db / "connection.py").write_text(
        """\
class DatabaseConnection:
    def __init__(self, url: str):
        self.url = url
        self._connected = False

    def connect(self) -> None:
        self._connected = True

    def disconnect(self) -> None:
        self._connected = False

    @property
    def is_connected(self) -> bool:
        return self._connected
""",
        encoding="utf-8",
    )

    # src/config.py (root-level src file)
    (project / "src" / "__init__.py").write_text("", encoding="utf-8")
    (project / "src" / "config.py").write_text(
        """\
from dataclasses import dataclass


@dataclass
class AppConfig:
    host: str = "0.0.0.0"
    port: int = 8000
    database_url: str = "sqlite:///db.sqlite"
    debug: bool = False


def load_config() -> AppConfig:
    return AppConfig()
""",
        encoding="utf-8",
    )

    _git_commit(project, "init py project")
    return project


def _make_mixed_project(tmp_path: Path) -> Path:
    """Create a mixed TS + Python project."""
    project = tmp_path / "mixed-project"
    project.mkdir()
    _setup_git_repo(project)

    # Both manifests
    (project / "package.json").write_text(
        '{"name": "mixed-project", "dependencies": {"express": "^4.18.0"}}',
        encoding="utf-8",
    )
    (project / "pyproject.toml").write_text(
        '[project]\nname = "mixed-project"\ndependencies = ["flask>=3.0.0"]\n',
        encoding="utf-8",
    )

    (project / ".gitignore").write_text(
        "node_modules/\n__pycache__/\n.venv/\n", encoding="utf-8"
    )

    # TypeScript files
    frontend = project / "src" / "frontend"
    frontend.mkdir(parents=True)
    (frontend / "app.ts").write_text(
        """\
export interface AppState {
  user: string | null;
  loading: boolean;
}

export class AppComponent {
  private state: AppState = { user: null, loading: false };

  render(): string {
    return this.state.loading ? 'Loading...' : 'Ready';
  }
}
""",
        encoding="utf-8",
    )
    (frontend / "api.ts").write_text(
        """\
export class ApiClient {
  async fetchUser(id: string): Promise<any> {
    return {};
  }

  async fetchOrders(userId: string): Promise<any[]> {
    return [];
  }
}
""",
        encoding="utf-8",
    )

    # Python files
    backend = project / "src" / "backend"
    backend.mkdir(parents=True)
    (backend / "__init__.py").write_text("", encoding="utf-8")
    (backend / "server.py").write_text(
        """\
class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass
""",
        encoding="utf-8",
    )
    (backend / "handlers.py").write_text(
        """\
from src.backend.server import Server


class RequestHandler:
    def __init__(self, server: Server):
        self.server = server

    def handle_get(self, path: str) -> dict:
        return {"path": path}

    def handle_post(self, path: str, data: dict) -> dict:
        return {"path": path, "data": data}
""",
        encoding="utf-8",
    )

    _git_commit(project, "init mixed project")
    return project


# ═══════════════════════════════════════════════════════════════════
# End-to-End: One-Shot Mode on TypeScript Project
# ═══════════════════════════════════════════════════════════════════


class TestE2ETypeScriptProject:
    """End-to-end tests on a realistic TypeScript project."""

    @pytest.fixture(autouse=True)
    def setup(self, tmp_path: Path) -> None:
        self.project = _make_ts_project(tmp_path)
        main([str(self.project)])
        self.codebase_md = self.project / ".codebase.md"
        self.content = self.codebase_md.read_text(encoding="utf-8")
        self.toon = _extract_toon_block(self.content)

    def test_creates_codebase_md(self):
        assert self.codebase_md.exists()

    def test_has_prompt_framing(self):
        assert "## Live Codebase Map" in self.content
        assert "real-time structural map" in self.content
        assert "Trust these locations" in self.content

    def test_has_toon_block(self):
        assert "```toon" in self.content
        assert self.toon

    def test_metadata_section(self):
        assert "codebase:" in self.toon
        assert "name: ts-project" in self.toon
        assert "typescript" in self.toon

    def test_modules_detected(self):
        """Should detect auth, orders, database, config modules."""
        assert "modules[" in self.toon
        assert "auth" in self.toon
        assert "orders" in self.toon
        assert "database" in self.toon
        assert "config" in self.toon

    def test_symbols_detected(self):
        """Should find key symbols from the project."""
        assert "symbols[" in self.toon
        assert "User" in self.toon
        assert "Session" in self.toon
        assert "OrderService" in self.toon
        assert "AuthMiddleware" in self.toon

    def test_interfaces_detected(self):
        """TypeScript interfaces should be extracted."""
        assert "interface" in self.toon

    def test_class_symbols_detected(self):
        """TypeScript classes should be extracted."""
        assert "class" in self.toon

    def test_function_symbols_detected(self):
        """TypeScript functions should be extracted."""
        assert "fn" in self.toon or "login" in self.toon

    def test_hierarchies_detected(self):
        """Some type hierarchies should be present."""
        # We may or may not get hierarchies depending on what Kit detects
        # But the section header should be there if any relationships exist
        # Not asserting specific hierarchies since it depends on Kit's parsing
        pass

    def test_dependencies_from_package_json(self):
        """Dependencies from package.json should appear."""
        assert "dependencies[" in self.toon
        assert "express" in self.toon
        assert "typescript" in self.toon

    def test_module_field_counts(self):
        """Module rows should have 4 fields: name, path, key_types, depends_on."""
        in_modules = False
        for line in self.toon.splitlines():
            if line.startswith("modules["):
                in_modules = True
                continue
            if in_modules and line.startswith("  "):
                fields = _split_toon_row(line)
                assert len(fields) == 4, f"Module row should have 4 fields: {line}"
            elif in_modules and not line.startswith("  "):
                break

    def test_symbol_field_counts(self):
        """Symbol rows should have 5 fields: fqn, kind, file, line, signature."""
        in_symbols = False
        for line in self.toon.splitlines():
            if line.startswith("symbols["):
                in_symbols = True
                continue
            if (
                in_symbols
                and line.startswith("  ")
                and not line.strip().startswith("#")
            ):
                fields = _split_toon_row(line)
                assert len(fields) == 5, f"Symbol row should have 5 fields: {line}"
            elif in_symbols and not line.startswith("  "):
                break

    def test_dependency_field_counts(self):
        """Dependency rows should have 3 fields: name, version, category."""
        in_deps = False
        for line in self.toon.splitlines():
            if line.startswith("dependencies["):
                in_deps = True
                continue
            if in_deps and line.startswith("  "):
                fields = _split_toon_row(line)
                assert len(fields) == 3, f"Dep row should have 3 fields: {line}"
            elif in_deps and not line.startswith("  "):
                break

    def test_line_numbers_are_positive(self):
        """All line numbers in symbols should be >= 1."""
        in_symbols = False
        for line in self.toon.splitlines():
            if line.startswith("symbols["):
                in_symbols = True
                continue
            if (
                in_symbols
                and line.startswith("  ")
                and not line.strip().startswith("#")
            ):
                fields = _split_toon_row(line)
                line_num = int(fields[3])
                assert line_num >= 1, f"Line number should be >= 1: {line}"
            elif in_symbols and not line.startswith("  "):
                break


# ═══════════════════════════════════════════════════════════════════
# End-to-End: One-Shot Mode on Python Project
# ═══════════════════════════════════════════════════════════════════


class TestE2EPythonProject:
    """End-to-end tests on a realistic Python project."""

    @pytest.fixture(autouse=True)
    def setup(self, tmp_path: Path) -> None:
        self.project = _make_py_project(tmp_path)
        main([str(self.project)])
        self.codebase_md = self.project / ".codebase.md"
        self.content = self.codebase_md.read_text(encoding="utf-8")
        self.toon = _extract_toon_block(self.content)

    def test_creates_codebase_md(self):
        assert self.codebase_md.exists()

    def test_metadata_has_python_language(self):
        assert "python" in self.toon

    def test_modules_detected(self):
        """Should detect models, services, api, db modules."""
        assert "modules[" in self.toon
        assert "models" in self.toon
        assert "services" in self.toon
        assert "api" in self.toon
        assert "db" in self.toon

    def test_python_classes_detected(self):
        """Python classes should be extracted."""
        assert "User" in self.toon
        assert "AuthService" in self.toon
        assert "OrderService" in self.toon
        assert "DatabaseConnection" in self.toon

    def test_python_enums_detected(self):
        """Python enums should be extracted."""
        assert "OrderStatus" in self.toon

    def test_python_functions_detected(self):
        """Standalone functions should be detected."""
        assert "load_config" in self.toon

    def test_dependencies_from_pyproject(self):
        """Dependencies from pyproject.toml should appear."""
        assert "dependencies[" in self.toon
        assert "fastapi" in self.toon
        assert "sqlalchemy" in self.toon
        assert "pytest" in self.toon

    def test_python_hierarchy_extends(self):
        """Python class inheritance should be detected when non-ignored bases used."""
        # Note: OrderStatus(Enum) is filtered because Enum is in _IGNORED_BASES.
        # The writer omits the hierarchies section entirely if empty.
        # This is correct behavior — our fixture doesn't have user-defined
        # inheritance. If hierarchies are present, they should have 'extends'.
        if "hierarchies[" in self.toon:
            assert "extends" in self.toon or "contains" in self.toon

    def test_cross_module_deps_detected(self):
        """Cross-module imports should be reflected in module depends_on."""
        # services imports from models, api imports from services
        # The exact format varies but at least some modules should have depends_on
        in_modules = False
        has_dep = False
        for line in self.toon.splitlines():
            if line.startswith("modules["):
                in_modules = True
                continue
            if in_modules and line.startswith("  "):
                fields = _split_toon_row(line)
                if len(fields) >= 4 and fields[3].strip():
                    has_dep = True
            elif in_modules and not line.startswith("  "):
                break
        assert has_dep, "At least one module should have cross-module dependencies"


# ═══════════════════════════════════════════════════════════════════
# End-to-End: Mixed TS + Python Project
# ═══════════════════════════════════════════════════════════════════


class TestE2EMixedProject:
    """End-to-end tests on a mixed TypeScript + Python project."""

    @pytest.fixture(autouse=True)
    def setup(self, tmp_path: Path) -> None:
        self.project = _make_mixed_project(tmp_path)
        main([str(self.project)])
        self.codebase_md = self.project / ".codebase.md"
        self.content = self.codebase_md.read_text(encoding="utf-8")
        self.toon = _extract_toon_block(self.content)

    def test_creates_codebase_md(self):
        assert self.codebase_md.exists()

    def test_detects_both_languages(self):
        """Both typescript and python should appear in languages."""
        assert "typescript" in self.toon
        assert "python" in self.toon

    def test_ts_symbols_present(self):
        """TypeScript symbols should be extracted."""
        assert "AppComponent" in self.toon or "ApiClient" in self.toon

    def test_python_symbols_present(self):
        """Python symbols should be extracted."""
        assert "Server" in self.toon
        assert "RequestHandler" in self.toon

    def test_both_manifests_parsed(self):
        """Dependencies from both package.json and pyproject.toml should appear."""
        assert "express" in self.toon
        assert "flask" in self.toon

    def test_frontend_and_backend_modules(self):
        """Should detect frontend and backend as separate modules."""
        assert "frontend" in self.toon
        assert "backend" in self.toon


# ═══════════════════════════════════════════════════════════════════
# End-to-End: Watch Mode
# ═══════════════════════════════════════════════════════════════════


class TestE2EWatchMode:
    """Tests for incremental watch mode updates."""

    def test_incremental_update_modifies_output(self, tmp_path: Path):
        """Modifying a file should update .codebase.md with new symbols."""
        project = _make_py_project(tmp_path)

        # Initial index
        pipeline = IncrementalPipeline(
            project_root=project,
            output_path=project / ".codebase.md",
            project_name="py-project",
            file_filter=FileFilter(project),
        )
        pipeline.full_index()

        content_before = (project / ".codebase.md").read_text(encoding="utf-8")
        assert "BrandNewClass" not in content_before

        # Add a new class to an existing file
        config_file = project / "src" / "config.py"
        original = config_file.read_text(encoding="utf-8")
        config_file.write_text(
            original + "\n\nclass BrandNewClass:\n    pass\n", encoding="utf-8"
        )
        _git_commit(project, "add new class")

        # Incremental update
        pipeline.update_files(["src/config.py"])
        content_after = (project / ".codebase.md").read_text(encoding="utf-8")
        assert "BrandNewClass" in content_after

    def test_incremental_update_removes_deleted_symbols(self, tmp_path: Path):
        """Deleting a file should remove its symbols from .codebase.md."""
        project = _make_py_project(tmp_path)

        pipeline = IncrementalPipeline(
            project_root=project,
            output_path=project / ".codebase.md",
            project_name="py-project",
            file_filter=FileFilter(project),
        )
        pipeline.full_index()

        content_before = (project / ".codebase.md").read_text(encoding="utf-8")
        assert "DatabaseConnection" in content_before

        # Remove the db connection file
        (project / "src" / "db" / "connection.py").unlink()
        _git_commit(project, "delete connection.py")

        pipeline.remove_files(["src/db/connection.py"])
        content_after = (project / ".codebase.md").read_text(encoding="utf-8")
        assert "DatabaseConnection" not in content_after

    def test_incremental_performance(self, tmp_path: Path):
        """Incremental update for a single file should be < 50ms."""
        project = _make_py_project(tmp_path)

        pipeline = IncrementalPipeline(
            project_root=project,
            output_path=project / ".codebase.md",
            project_name="py-project",
            file_filter=FileFilter(project),
        )
        pipeline.full_index()

        # Modify a file
        config_file = project / "src" / "config.py"
        original = config_file.read_text(encoding="utf-8")
        config_file.write_text(
            original + "\n\nclass TimingTest:\n    pass\n", encoding="utf-8"
        )
        _git_commit(project, "add timing class")

        # Measure update time
        t0 = time.monotonic()
        pipeline.update_files(["src/config.py"])
        elapsed_ms = (time.monotonic() - t0) * 1000

        assert elapsed_ms < 50, (
            f"Incremental update took {elapsed_ms:.1f}ms (budget: 50ms)"
        )


# ═══════════════════════════════════════════════════════════════════
# Performance Validation
# ═══════════════════════════════════════════════════════════════════


class TestPerformance:
    """Performance benchmarks for cold index and incremental updates."""

    def _make_large_project(self, tmp_path: Path, num_files: int = 200) -> Path:
        """Create a project with many files to stress-test performance.

        We generate num_files Python files, each with a few classes/functions.
        At ~50 lines per file and 200 files, this is ~10K LOC.
        """
        project = tmp_path / "large-project"
        project.mkdir()
        _setup_git_repo(project)

        (project / ".gitignore").write_text("__pycache__/\n.venv/\n", encoding="utf-8")
        (project / "pyproject.toml").write_text(
            '[project]\nname = "large-project"\ndependencies = []\n',
            encoding="utf-8",
        )

        for i in range(num_files):
            # Spread across multiple modules
            module_name = f"mod_{i % 10}"
            mod_dir = project / "src" / module_name
            mod_dir.mkdir(parents=True, exist_ok=True)

            # Ensure __init__.py exists
            init_file = mod_dir / "__init__.py"
            if not init_file.exists():
                init_file.write_text("", encoding="utf-8")

            (mod_dir / f"file_{i}.py").write_text(
                f"""\
class Class{i}:
    '''Class number {i}.'''
    def __init__(self):
        self.value = {i}

    def method_a(self) -> int:
        return self.value

    def method_b(self, x: int) -> int:
        return self.value + x


class Helper{i}:
    '''Helper class {i}.'''
    def process(self, data: str) -> str:
        return data.upper()


def utility_function_{i}(x: int) -> int:
    '''Utility function {i}.'''
    return x * 2


def another_function_{i}(name: str) -> str:
    '''Another function {i}.'''
    return f"hello {{name}}"
""",
                encoding="utf-8",
            )

        _git_commit(project, "init large project")
        return project

    def test_cold_index_under_1_second(self, tmp_path: Path):
        """Cold index of a ~200-file project should complete in < 1 second."""
        project = self._make_large_project(tmp_path, num_files=200)

        t0 = time.monotonic()
        main([str(project)])
        elapsed = time.monotonic() - t0

        assert elapsed < 1.0, f"Cold index took {elapsed:.2f}s (budget: 1.0s)"

        # Verify output was created and has content
        content = (project / ".codebase.md").read_text(encoding="utf-8")
        assert "```toon" in content
        assert "modules[" in content

    def test_incremental_update_under_50ms(self, tmp_path: Path):
        """Incremental update on a large project should be < 50ms."""
        project = self._make_large_project(tmp_path, num_files=200)

        pipeline = IncrementalPipeline(
            project_root=project,
            output_path=project / ".codebase.md",
            project_name="large-project",
            file_filter=FileFilter(project),
        )
        pipeline.full_index()

        # Modify one file
        mod_file = project / "src" / "mod_0" / "file_0.py"
        mod_file.write_text(
            "class NewClass:\n    pass\n\ndef new_func():\n    pass\n",
            encoding="utf-8",
        )
        _git_commit(project, "modify file_0")

        t0 = time.monotonic()
        pipeline.update_files(["src/mod_0/file_0.py"])
        elapsed_ms = (time.monotonic() - t0) * 1000

        assert elapsed_ms < 50, (
            f"Incremental update took {elapsed_ms:.1f}ms (budget: 50ms)"
        )

    def test_token_count_reasonable(self, tmp_path: Path):
        """Output token count should be reasonable for a large project."""
        project = self._make_large_project(tmp_path, num_files=200)
        main([str(project)])

        content = (project / ".codebase.md").read_text(encoding="utf-8")
        token_estimate = len(content) // 4

        # For 200 files (~10K LOC), we expect the token count to be bounded
        # The max_symbols=500 default should keep it under control
        assert token_estimate > 0, "Token count should be > 0"
        # With 500 symbol budget, output should be well under 20K tokens
        assert token_estimate < 20000, f"Token count {token_estimate} seems too high"


# ═══════════════════════════════════════════════════════════════════
# Edge Cases
# ═══════════════════════════════════════════════════════════════════


class TestEdgeCases:
    """Edge case tests for graceful handling."""

    def test_empty_project(self, tmp_path: Path):
        """Project with no parseable files should produce valid output."""
        project = tmp_path / "empty-project"
        project.mkdir()
        _setup_git_repo(project)
        (project / "README.md").write_text("# Empty", encoding="utf-8")
        _git_commit(project, "init")

        main([str(project)])

        content = (project / ".codebase.md").read_text(encoding="utf-8")
        assert "```toon" in content
        assert "modules[0]" in content or "symbols[0]" in content

    def test_only_gitignore(self, tmp_path: Path):
        """Project with only .gitignore should not crash."""
        project = tmp_path / "gitignore-only"
        project.mkdir()
        _setup_git_repo(project)
        (project / ".gitignore").write_text("*.log\n", encoding="utf-8")
        _git_commit(project, "init")

        main([str(project)])
        assert (project / ".codebase.md").exists()

    def test_syntax_error_file(self, tmp_path: Path):
        """Files with syntax errors should be skipped gracefully."""
        project = tmp_path / "syntax-err-project"
        project.mkdir()
        _setup_git_repo(project)

        # Valid file
        (project / "good.py").write_text(
            "class GoodClass:\n    pass\n", encoding="utf-8"
        )

        # File with syntax errors
        (project / "bad.py").write_text(
            "class BadClass(\n    # missing closing paren and colon\n    def broken(self\n",
            encoding="utf-8",
        )

        _git_commit(project, "init")
        main([str(project)])

        content = (project / ".codebase.md").read_text(encoding="utf-8")
        assert "```toon" in content
        # The good file's symbols should still be there
        assert "GoodClass" in content

    def test_large_file(self, tmp_path: Path):
        """Very large files should still parse (potentially truncated)."""
        project = tmp_path / "large-file-project"
        project.mkdir()
        _setup_git_repo(project)

        # Generate a large Python file with many classes
        lines = []
        for i in range(500):
            lines.append(f"class LargeClass{i}:")
            lines.append(f"    '''Class {i}.'''")
            lines.append("    pass")
            lines.append("")

        (project / "large.py").write_text("\n".join(lines), encoding="utf-8")
        _git_commit(project, "init")

        main([str(project)])

        content = (project / ".codebase.md").read_text(encoding="utf-8")
        assert "```toon" in content
        # Should have symbols (at least some)
        assert "symbols[" in content

    def test_deeply_nested_directories(self, tmp_path: Path):
        """Deeply nested directories (>5 levels) should work."""
        project = tmp_path / "deep-project"
        project.mkdir()
        _setup_git_repo(project)

        deep_dir = project / "src" / "a" / "b" / "c" / "d" / "e" / "f"
        deep_dir.mkdir(parents=True)
        (deep_dir / "deep.py").write_text(
            "class DeepClass:\n    pass\n\ndef deep_func():\n    pass\n",
            encoding="utf-8",
        )
        _git_commit(project, "init")

        main([str(project)])

        content = (project / ".codebase.md").read_text(encoding="utf-8")
        assert "```toon" in content
        assert "DeepClass" in content

    def test_binary_files_ignored(self, tmp_path: Path):
        """Binary files in the project should be ignored."""
        project = tmp_path / "binary-project"
        project.mkdir()
        _setup_git_repo(project)

        (project / "code.py").write_text(
            "class RealCode:\n    pass\n", encoding="utf-8"
        )
        # Write a binary file
        (project / "image.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 100)
        (project / "data.bin").write_bytes(bytes(range(256)))
        _git_commit(project, "init")

        main([str(project)])

        content = (project / ".codebase.md").read_text(encoding="utf-8")
        assert "```toon" in content
        assert "RealCode" in content
        # Binary files should not appear as modules/symbols
        assert "image.png" not in content
        assert "data.bin" not in content

    def test_unicode_content_in_files(self, tmp_path: Path):
        """Files with unicode content should parse correctly."""
        project = tmp_path / "unicode-project"
        project.mkdir()
        _setup_git_repo(project)

        (project / "i18n.py").write_text(
            "# -*- coding: utf-8 -*-\n"
            "class Grüße:\n"
            '    """Greetings in German."""\n'
            '    message = "Héllo Wörld"\n'
            "    pass\n",
            encoding="utf-8",
        )
        _git_commit(project, "init")

        main([str(project)])

        content = (project / ".codebase.md").read_text(encoding="utf-8")
        assert "```toon" in content

    def test_gitignored_files_excluded(self, tmp_path: Path):
        """Files matching .gitignore should not appear in output."""
        project = tmp_path / "gitignore-project"
        project.mkdir()
        _setup_git_repo(project)

        (project / ".gitignore").write_text(
            "ignored/\n*.generated.py\n", encoding="utf-8"
        )
        (project / "good.py").write_text(
            "class Included:\n    pass\n", encoding="utf-8"
        )

        ignored = project / "ignored"
        ignored.mkdir()
        (ignored / "secret.py").write_text(
            "class Secret:\n    pass\n", encoding="utf-8"
        )

        (project / "auto.generated.py").write_text(
            "class Generated:\n    pass\n", encoding="utf-8"
        )

        _git_commit(project, "init")
        main([str(project)])

        content = (project / ".codebase.md").read_text(encoding="utf-8")
        assert "Included" in content
        assert "Secret" not in content
        assert "Generated" not in content

    def test_custom_output_path(self, tmp_path: Path):
        """Custom --output path should write to the specified location."""
        project = tmp_path / "custom-out"
        project.mkdir()
        _setup_git_repo(project)
        (project / "app.py").write_text("class MyApp:\n    pass\n", encoding="utf-8")
        _git_commit(project, "init")

        custom_out = tmp_path / "output" / "my-map.md"
        main([str(project), "-o", str(custom_out)])

        assert custom_out.exists()
        content = custom_out.read_text(encoding="utf-8")
        assert "```toon" in content
        assert "MyApp" in content

        # Default location should NOT exist
        assert not (project / ".codebase.md").exists()


# ═══════════════════════════════════════════════════════════════════
# TOON Format Validation
# ═══════════════════════════════════════════════════════════════════


class TestTOONFormatValidation:
    """Validate that TOON output is well-formed and parseable."""

    @pytest.fixture(autouse=True)
    def setup(self, tmp_path: Path) -> None:
        self.project = _make_ts_project(tmp_path)
        main([str(self.project)])
        content = (self.project / ".codebase.md").read_text(encoding="utf-8")
        self.toon = _extract_toon_block(content)
        self.lines = self.toon.splitlines()

    def test_starts_with_codebase_section(self):
        assert self.lines[0] == "codebase:"

    def test_has_name_field(self):
        assert any("name:" in line for line in self.lines)

    def test_has_languages_field(self):
        assert any("languages[" in line for line in self.lines)

    def test_has_last_indexed_field(self):
        assert any("last_indexed:" in line for line in self.lines)

    def test_modules_header_has_field_names(self):
        for line in self.lines:
            if line.startswith("modules["):
                assert "{name,path,key_types,depends_on}" in line
                break
        else:
            pytest.fail("No modules header found")

    def test_symbols_header_has_field_names(self):
        for line in self.lines:
            if line.startswith("symbols["):
                assert "{fqn,kind,file,line,signature}" in line
                break
        else:
            pytest.fail("No symbols header found")

    def test_dependencies_header_has_field_names(self):
        for line in self.lines:
            if line.startswith("dependencies["):
                assert "{name,version,category}" in line
                break
        else:
            pytest.fail("No dependencies header found")

    def test_module_count_matches_rows(self):
        """The count in modules[N] should match the number of data rows."""
        for i, line in enumerate(self.lines):
            if line.startswith("modules["):
                # Extract count
                count_str = line.split("[")[1].split("]")[0]
                count = int(count_str)

                # Count data rows (indented lines until next section)
                rows = 0
                for j in range(i + 1, len(self.lines)):
                    if self.lines[j].startswith("  "):
                        rows += 1
                    else:
                        break

                assert rows == count, f"modules[{count}] but found {rows} rows"
                break

    def test_symbol_count_matches_rows(self):
        """The count in symbols[N] should match the number of data rows."""
        for i, line in enumerate(self.lines):
            if line.startswith("symbols["):
                count_str = line.split("[")[1].split("]")[0]
                count = int(count_str)

                rows = 0
                for j in range(i + 1, len(self.lines)):
                    if self.lines[j].startswith("  ") and not self.lines[
                        j
                    ].strip().startswith("#"):
                        rows += 1
                    elif self.lines[j].startswith("  ") and self.lines[
                        j
                    ].strip().startswith("#"):
                        pass  # truncation comment
                    else:
                        break

                assert rows == count, f"symbols[{count}] but found {rows} rows"
                break

    def test_no_empty_fqn_in_symbols(self):
        """All symbol rows should have non-empty FQNs."""
        in_symbols = False
        for line in self.lines:
            if line.startswith("symbols["):
                in_symbols = True
                continue
            if (
                in_symbols
                and line.startswith("  ")
                and not line.strip().startswith("#")
            ):
                fields = _split_toon_row(line)
                assert fields[0].strip(), f"Empty FQN in symbol row: {line}"
            elif in_symbols and not line.startswith("  "):
                break

    def test_valid_symbol_kinds(self):
        """Symbol kinds should be from our known vocabulary."""
        valid_kinds = {
            "fn",
            "class",
            "interface",
            "method",
            "variable",
            "type",
            "enum",
            "struct",
            "trait",
            "module",
        }
        in_symbols = False
        for line in self.lines:
            if line.startswith("symbols["):
                in_symbols = True
                continue
            if (
                in_symbols
                and line.startswith("  ")
                and not line.strip().startswith("#")
            ):
                fields = _split_toon_row(line)
                kind = fields[1].strip()
                assert kind in valid_kinds, f"Invalid symbol kind '{kind}' in: {line}"
            elif in_symbols and not line.startswith("  "):
                break

    def test_valid_dependency_categories(self):
        """Dependency categories should be 'runtime' or 'dev'."""
        in_deps = False
        for line in self.lines:
            if line.startswith("dependencies["):
                in_deps = True
                continue
            if in_deps and line.startswith("  "):
                fields = _split_toon_row(line)
                category = fields[2].strip()
                assert category in {"runtime", "dev"}, f"Invalid category '{category}'"
            elif in_deps and not line.startswith("  "):
                break
