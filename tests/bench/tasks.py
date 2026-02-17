"""Benchmark tasks with ground truth for DSPy prompt optimization.

50 tasks across 5 categories (10 each), distributed across 4 repos.
Deterministic train/dev split: 35 train (7/category) + 15 dev (3/category).

Every task references symbols, files, and line numbers that actually exist
in the generated .codebase.md fixtures under tests/bench/fixtures/.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path


# ── Data model ─────────────────────────────────────────────────────


@dataclass
class GroundTruth:
    target_files: list[str] = field(default_factory=list)
    target_symbols: list[str] = field(default_factory=list)
    required_types: list[str] = field(default_factory=list)
    required_imports: list[str] = field(default_factory=list)
    patterns: list[str] = field(default_factory=list)
    anti_patterns: list[str] = field(default_factory=list)


@dataclass
class BenchTask:
    id: str
    repo: str
    category: str  # trust | type | import | contract | pattern
    instruction: str
    ground_truth: GroundTruth


# ── Trust tasks (10) ───────────────────────────────────────────────
# Agent should navigate directly to file:line without searching.


_TRUST_ANTI_PATTERNS = [
    "let me search",
    "grep",
    "let me verify",
    "I'll look for",
    "let me find",
    "searching for",
]

TRUST_TASKS = [
    # express (3)
    BenchTask(
        id="trust-01",
        repo="express",
        category="trust",
        instruction="Where is the View constructor defined in Express?",
        ground_truth=GroundTruth(
            target_files=["lib/view.js"],
            target_symbols=["lib/view::View"],
            anti_patterns=_TRUST_ANTI_PATTERNS,
        ),
    ),
    BenchTask(
        id="trust-02",
        repo="express",
        category="trust",
        instruction="Show me the authenticate function in the Express auth example.",
        ground_truth=GroundTruth(
            target_files=["examples/auth/index.js"],
            target_symbols=["examples/auth/index::authenticate"],
            anti_patterns=_TRUST_ANTI_PATTERNS,
        ),
    ),
    BenchTask(
        id="trust-03",
        repo="express",
        category="trust",
        instruction="Where is the createApplication factory function defined?",
        ground_truth=GroundTruth(
            target_files=["lib/express.js"],
            target_symbols=["lib/express::createApplication"],
            anti_patterns=_TRUST_ANTI_PATTERNS,
        ),
    ),
    # flask (3)
    BenchTask(
        id="trust-04",
        repo="flask",
        category="trust",
        instruction="Where is the Flask application class defined?",
        ground_truth=GroundTruth(
            target_files=["src/flask/app.py"],
            target_symbols=["src/flask/app::Flask"],
            anti_patterns=_TRUST_ANTI_PATTERNS,
        ),
    ),
    BenchTask(
        id="trust-05",
        repo="flask",
        category="trust",
        instruction="Show me the SessionInterface class in Flask.",
        ground_truth=GroundTruth(
            target_files=["src/flask/sessions.py"],
            target_symbols=["src/flask/sessions::SessionInterface"],
            anti_patterns=_TRUST_ANTI_PATTERNS,
        ),
    ),
    BenchTask(
        id="trust-06",
        repo="flask",
        category="trust",
        instruction="Where is the JSONTag base class defined?",
        ground_truth=GroundTruth(
            target_files=["src/flask/json/tag.py"],
            target_symbols=["src/flask/json/tag::JSONTag"],
            anti_patterns=_TRUST_ANTI_PATTERNS,
        ),
    ),
    # fastapi (2)
    BenchTask(
        id="trust-07",
        repo="fastapi",
        category="trust",
        instruction="Where is the FastAPI application class defined?",
        ground_truth=GroundTruth(
            target_files=["fastapi/applications.py"],
            target_symbols=["fastapi/applications::FastAPI"],
            anti_patterns=_TRUST_ANTI_PATTERNS,
        ),
    ),
    BenchTask(
        id="trust-08",
        repo="fastapi",
        category="trust",
        instruction="Show me the APIRouter class definition.",
        ground_truth=GroundTruth(
            target_files=["fastapi/routing.py"],
            target_symbols=["fastapi/routing::APIRouter"],
            anti_patterns=_TRUST_ANTI_PATTERNS,
        ),
    ),
    # solid (2)
    BenchTask(
        id="trust-09",
        repo="solid",
        category="trust",
        instruction="Where is createSignal defined in Solid's source?",
        ground_truth=GroundTruth(
            target_files=["packages/solid/src/reactive/signal.ts"],
            target_symbols=["packages/solid/src/reactive/signal::createSignal"],
            anti_patterns=_TRUST_ANTI_PATTERNS,
        ),
    ),
    BenchTask(
        id="trust-10",
        repo="solid",
        category="trust",
        instruction="Show me where the Component type alias is defined.",
        ground_truth=GroundTruth(
            target_files=["packages/solid/src/render/component.ts"],
            target_symbols=["packages/solid/src/render/component::Component"],
            anti_patterns=_TRUST_ANTI_PATTERNS,
        ),
    ),
]


# ── Type consistency tasks (10) ────────────────────────────────────
# Agent should use correct types from the symbol table.

TYPE_TASKS = [
    # express (2)
    BenchTask(
        id="type-01",
        repo="express",
        category="type",
        instruction=(
            "Write a custom view constructor similar to GithubView that "
            "accepts a name and options parameter."
        ),
        ground_truth=GroundTruth(
            target_files=["examples/view-constructor/github-view.js"],
            target_symbols=["examples/view-constructor/github-view::GithubView"],
            required_types=["GithubView"],
            patterns=["function", "name", "options"],
        ),
    ),
    BenchTask(
        id="type-02",
        repo="express",
        category="type",
        instruction=(
            "Write a middleware function that follows the same signature as "
            "the restrict function in the auth example."
        ),
        ground_truth=GroundTruth(
            target_files=["examples/auth/index.js"],
            target_symbols=["examples/auth/index::restrict"],
            required_types=[],
            patterns=["req", "res", "next"],
        ),
    ),
    # flask (3)
    BenchTask(
        id="type-03",
        repo="flask",
        category="type",
        instruction=(
            "Add a method to a Flask Config subclass that validates a key. "
            "Use the correct Config base class."
        ),
        ground_truth=GroundTruth(
            target_files=["src/flask/config.py"],
            target_symbols=["src/flask/config::Config"],
            required_types=["Config", "dict"],
        ),
    ),
    BenchTask(
        id="type-04",
        repo="flask",
        category="type",
        instruction=(
            "Write a function that takes a Flask Request object and extracts "
            "form data. Use the correct Request wrapper type."
        ),
        ground_truth=GroundTruth(
            target_files=["src/flask/wrappers.py"],
            target_symbols=["src/flask/wrappers::Request"],
            required_types=["Request"],
        ),
    ),
    BenchTask(
        id="type-05",
        repo="flask",
        category="type",
        instruction=(
            "Create a function that accepts a Blueprint and registers an "
            "error handler on it."
        ),
        ground_truth=GroundTruth(
            target_files=["src/flask/blueprints.py"],
            target_symbols=["src/flask/blueprints::Blueprint"],
            required_types=["Blueprint"],
        ),
    ),
    # fastapi (3)
    BenchTask(
        id="type-06",
        repo="fastapi",
        category="type",
        instruction=(
            "Write a dependency function that returns a Dependant object. "
            "Use the correct type from the dependencies module."
        ),
        ground_truth=GroundTruth(
            target_files=["fastapi/dependencies/models.py"],
            target_symbols=["fastapi/dependencies/models::Dependant"],
            required_types=["Dependant"],
        ),
    ),
    BenchTask(
        id="type-07",
        repo="fastapi",
        category="type",
        instruction=(
            "Write a route handler that raises an HTTPException with a 404 status code."
        ),
        ground_truth=GroundTruth(
            target_files=["fastapi/exceptions.py"],
            target_symbols=["fastapi/exceptions::HTTPException"],
            required_types=["HTTPException"],
            patterns=["404", "status_code"],
        ),
    ),
    BenchTask(
        id="type-08",
        repo="fastapi",
        category="type",
        instruction=(
            "Write a function that takes a Query parameter with validation. "
            "Use the correct Query type from fastapi params."
        ),
        ground_truth=GroundTruth(
            target_files=["fastapi/params.py"],
            target_symbols=["fastapi/params::Query"],
            required_types=["Query"],
        ),
    ),
    # solid (2)
    BenchTask(
        id="type-09",
        repo="solid",
        category="type",
        instruction=(
            "Write a Solid component that uses createSignal. Make sure the "
            "Signal type is used correctly as a tuple of [get, set]."
        ),
        ground_truth=GroundTruth(
            target_files=["packages/solid/src/reactive/signal.ts"],
            target_symbols=[
                "packages/solid/src/reactive/signal::createSignal",
                "packages/solid/src/reactive/signal::Signal",
            ],
            required_types=["Signal", "Accessor", "Setter"],
        ),
    ),
    BenchTask(
        id="type-10",
        repo="solid",
        category="type",
        instruction=(
            "Write a typed Solid component using the Component type alias. "
            "The component should accept props with a name field."
        ),
        ground_truth=GroundTruth(
            target_files=["packages/solid/src/render/component.ts"],
            target_symbols=["packages/solid/src/render/component::Component"],
            required_types=["Component", "JSX.Element"],
        ),
    ),
]


# ── Import correctness tasks (10) ─────────────────────────────────
# Agent should import from the right modules.

IMPORT_TASKS = [
    # express (2)
    BenchTask(
        id="import-01",
        repo="express",
        category="import",
        instruction=(
            "Create a new file that uses the stringify utility from "
            "Express's response module."
        ),
        ground_truth=GroundTruth(
            target_files=["lib/response.js"],
            target_symbols=["lib/response::stringify"],
            required_imports=["lib/response"],
        ),
    ),
    BenchTask(
        id="import-02",
        repo="express",
        category="import",
        instruction=(
            "Create a file that uses the acceptParams utility from Express. "
            "Import it from the correct module."
        ),
        ground_truth=GroundTruth(
            target_files=["lib/utils.js"],
            target_symbols=["lib/utils::acceptParams"],
            required_imports=["lib/utils"],
        ),
    ),
    # flask (3)
    BenchTask(
        id="import-03",
        repo="flask",
        category="import",
        instruction=(
            "Create a new module that imports the Flask application class "
            "and the Blueprint class from their correct locations."
        ),
        ground_truth=GroundTruth(
            target_files=["src/flask/app.py", "src/flask/blueprints.py"],
            target_symbols=[
                "src/flask/app::Flask",
                "src/flask/blueprints::Blueprint",
            ],
            required_imports=["flask", "flask.blueprints"],
        ),
    ),
    BenchTask(
        id="import-04",
        repo="flask",
        category="import",
        instruction=(
            "Write a file that imports JSONProvider to create a custom "
            "JSON serializer. Import from the correct submodule."
        ),
        ground_truth=GroundTruth(
            target_files=["src/flask/json/provider.py"],
            target_symbols=["src/flask/json/provider::JSONProvider"],
            required_imports=["flask.json.provider"],
        ),
    ),
    BenchTask(
        id="import-05",
        repo="flask",
        category="import",
        instruction=(
            "Create a file that imports SessionInterface to implement "
            "custom session storage."
        ),
        ground_truth=GroundTruth(
            target_files=["src/flask/sessions.py"],
            target_symbols=["src/flask/sessions::SessionInterface"],
            required_imports=["flask.sessions"],
        ),
    ),
    # fastapi (3)
    BenchTask(
        id="import-06",
        repo="fastapi",
        category="import",
        instruction=(
            "Create a new router module that imports APIRouter from the "
            "correct location in the FastAPI package."
        ),
        ground_truth=GroundTruth(
            target_files=["fastapi/routing.py"],
            target_symbols=["fastapi/routing::APIRouter"],
            required_imports=["fastapi.routing", "fastapi"],
        ),
    ),
    BenchTask(
        id="import-07",
        repo="fastapi",
        category="import",
        instruction=(
            "Write a security module that imports OAuth2PasswordBearer "
            "from FastAPI. Use the correct import path."
        ),
        ground_truth=GroundTruth(
            target_files=["fastapi/security/oauth2.py"],
            target_symbols=["fastapi/security/oauth2::OAuth2PasswordBearer"],
            required_imports=["fastapi.security.oauth2", "fastapi.security"],
        ),
    ),
    BenchTask(
        id="import-08",
        repo="fastapi",
        category="import",
        instruction=(
            "Create an endpoint file that imports both Query and Path "
            "parameter types from FastAPI's params module."
        ),
        ground_truth=GroundTruth(
            target_files=["fastapi/params.py"],
            target_symbols=[
                "fastapi/params::Query",
                "fastapi/params::Path",
            ],
            required_imports=["fastapi.params", "fastapi"],
        ),
    ),
    # solid (2)
    BenchTask(
        id="import-09",
        repo="solid",
        category="import",
        instruction=(
            "Create a new Solid component file that imports createSignal "
            "and createEffect from the correct module."
        ),
        ground_truth=GroundTruth(
            target_files=["packages/solid/src/reactive/signal.ts"],
            target_symbols=[
                "packages/solid/src/reactive/signal::createSignal",
                "packages/solid/src/reactive/signal::createEffect",
            ],
            required_imports=["solid-js"],
        ),
    ),
    BenchTask(
        id="import-10",
        repo="solid",
        category="import",
        instruction=(
            "Write a module that imports createStore from Solid's store "
            "package. Use the correct import path."
        ),
        ground_truth=GroundTruth(
            target_files=["packages/solid/store/src/store.ts"],
            target_symbols=["packages/solid/store/src/store::createStore"],
            required_imports=["solid-js/store"],
        ),
    ),
]


# ── API contract adherence tasks (10) ─────────────────────────────
# Agent should implement required methods when extending/implementing.

CONTRACT_TASKS = [
    # express (2)
    BenchTask(
        id="contract-01",
        repo="express",
        category="contract",
        instruction=(
            "Create a custom View constructor that matches the View "
            "interface in lib/view.js. It should accept name and options."
        ),
        ground_truth=GroundTruth(
            target_files=["lib/view.js"],
            target_symbols=["lib/view::View"],
            patterns=["name", "options", "function"],
        ),
    ),
    BenchTask(
        id="contract-02",
        repo="express",
        category="contract",
        instruction=(
            "Write an error handler middleware matching Express conventions. "
            "It must follow the 4-argument (err, req, res, next) signature."
        ),
        ground_truth=GroundTruth(
            target_files=["lib/application.js"],
            target_symbols=["lib/application::logerror"],
            patterns=["err", "req", "res", "next"],
        ),
    ),
    # flask (3)
    BenchTask(
        id="contract-03",
        repo="flask",
        category="contract",
        instruction=(
            "Create a custom session interface by extending SessionInterface. "
            "Implement the required open_session and save_session methods."
        ),
        ground_truth=GroundTruth(
            target_files=["src/flask/sessions.py"],
            target_symbols=[
                "src/flask/sessions::SessionInterface",
                "src/flask/sessions::SecureCookieSessionInterface",
            ],
            required_types=["SessionInterface"],
            patterns=["open_session", "save_session"],
        ),
    ),
    BenchTask(
        id="contract-04",
        repo="flask",
        category="contract",
        instruction=(
            "Create a custom view class by extending MethodView. "
            "Implement the get and post HTTP method handlers."
        ),
        ground_truth=GroundTruth(
            target_files=["src/flask/views.py"],
            target_symbols=[
                "src/flask/views::View",
                "src/flask/views::MethodView",
            ],
            required_types=["MethodView", "View"],
            patterns=["get", "post", "def "],
        ),
    ),
    BenchTask(
        id="contract-05",
        repo="flask",
        category="contract",
        instruction=(
            "Create a custom JSON tag by extending JSONTag. Implement the "
            "check, to_json, and tag methods following the pattern "
            "of existing tags like TagDict."
        ),
        ground_truth=GroundTruth(
            target_files=["src/flask/json/tag.py"],
            target_symbols=[
                "src/flask/json/tag::JSONTag",
                "src/flask/json/tag::TagDict",
            ],
            required_types=["JSONTag"],
            patterns=["check", "to_json", "tag"],
        ),
    ),
    # fastapi (3)
    BenchTask(
        id="contract-06",
        repo="fastapi",
        category="contract",
        instruction=(
            "Create a custom API route class by extending APIRoute. "
            "Override the get_route_handler method."
        ),
        ground_truth=GroundTruth(
            target_files=["fastapi/routing.py"],
            target_symbols=["fastapi/routing::APIRoute"],
            required_types=["APIRoute"],
            patterns=["get_route_handler"],
        ),
    ),
    BenchTask(
        id="contract-07",
        repo="fastapi",
        category="contract",
        instruction=(
            "Create a custom security scheme by extending SecurityBase. "
            "Follow the pattern used by OAuth2PasswordBearer."
        ),
        ground_truth=GroundTruth(
            target_files=[
                "fastapi/security/oauth2.py",
            ],
            target_symbols=[
                "fastapi/security/oauth2::OAuth2PasswordBearer",
                "fastapi/security/oauth2::OAuth2",
            ],
            required_types=["OAuth2", "SecurityBase"],
            patterns=["__call__", "async"],
        ),
    ),
    BenchTask(
        id="contract-08",
        repo="fastapi",
        category="contract",
        instruction=(
            "Create a custom JSON response class by extending ORJSONResponse. "
            "Override the render method."
        ),
        ground_truth=GroundTruth(
            target_files=["fastapi/responses.py"],
            target_symbols=["fastapi/responses::ORJSONResponse"],
            required_types=["ORJSONResponse", "JSONResponse"],
            patterns=["render"],
        ),
    ),
    # solid (2)
    BenchTask(
        id="contract-09",
        repo="solid",
        category="contract",
        instruction=(
            "Create a custom resource using createResource that fetches "
            "data from an API. Follow the ResourceFetcher contract with "
            "the correct (source, info) signature."
        ),
        ground_truth=GroundTruth(
            target_files=["packages/solid/src/reactive/signal.ts"],
            target_symbols=[
                "packages/solid/src/reactive/signal::createResource",
            ],
            required_types=["ResourceFetcher", "Resource"],
            patterns=["source", "info", "fetcher"],
        ),
    ),
    BenchTask(
        id="contract-10",
        repo="solid",
        category="contract",
        instruction=(
            "Write a FlowComponent that wraps children with conditional "
            "rendering. Follow the FlowComponent type contract."
        ),
        ground_truth=GroundTruth(
            target_files=["packages/solid/src/render/component.ts"],
            target_symbols=[
                "packages/solid/src/render/component::FlowComponent",
            ],
            required_types=["FlowComponent", "JSX.Element"],
            patterns=["children", "props"],
        ),
    ),
]


# ── Pattern adherence tasks (10) ──────────────────────────────────
# Agent should follow existing code conventions.

PATTERN_TASKS = [
    # express (3)
    BenchTask(
        id="pattern-01",
        repo="express",
        category="pattern",
        instruction=(
            "Add a new example application following the pattern of the "
            "existing auth example. Include an authenticate function "
            "and a restrict middleware."
        ),
        ground_truth=GroundTruth(
            target_files=["examples/auth/index.js"],
            target_symbols=[
                "examples/auth/index::authenticate",
                "examples/auth/index::restrict",
            ],
            patterns=[
                "function authenticate",
                "function restrict",
                "req, res, next",
                "module.exports",
            ],
        ),
    ),
    BenchTask(
        id="pattern-02",
        repo="express",
        category="pattern",
        instruction=(
            "Add a new utility function to lib/utils.js following the "
            "coding style of the existing acceptParams function."
        ),
        ground_truth=GroundTruth(
            target_files=["lib/utils.js"],
            target_symbols=["lib/utils::acceptParams"],
            patterns=["function", "exports."],
        ),
    ),
    BenchTask(
        id="pattern-03",
        repo="express",
        category="pattern",
        instruction=(
            "Write a new response helper following the pattern of the "
            "stringify function in lib/response.js."
        ),
        ground_truth=GroundTruth(
            target_files=["lib/response.js"],
            target_symbols=["lib/response::stringify"],
            patterns=["function"],
        ),
    ),
    # flask (2)
    BenchTask(
        id="pattern-04",
        repo="flask",
        category="pattern",
        instruction=(
            "Add a new JSON tag following the pattern of TagDict, TagTuple, "
            "and TagBytes. Extend JSONTag and implement check, to_json, "
            "and tag methods."
        ),
        ground_truth=GroundTruth(
            target_files=["src/flask/json/tag.py"],
            target_symbols=[
                "src/flask/json/tag::JSONTag",
                "src/flask/json/tag::TagDict",
                "src/flask/json/tag::TagTuple",
                "src/flask/json/tag::TagBytes",
            ],
            patterns=["class Tag", "JSONTag", "def check", "def to_json", "def tag"],
        ),
    ),
    BenchTask(
        id="pattern-05",
        repo="flask",
        category="pattern",
        instruction=(
            "Write a new JSON provider following the DefaultJSONProvider "
            "pattern. Extend JSONProvider and implement the loads and "
            "dumps methods."
        ),
        ground_truth=GroundTruth(
            target_files=["src/flask/json/provider.py"],
            target_symbols=[
                "src/flask/json/provider::JSONProvider",
                "src/flask/json/provider::DefaultJSONProvider",
            ],
            patterns=["class", "JSONProvider", "def loads", "def dumps"],
        ),
    ),
    # fastapi (3)
    BenchTask(
        id="pattern-06",
        repo="fastapi",
        category="pattern",
        instruction=(
            "Create a new parameter type following the pattern of Query, "
            "Header, and Cookie. Extend the Param base class."
        ),
        ground_truth=GroundTruth(
            target_files=["fastapi/params.py"],
            target_symbols=[
                "fastapi/params::Param",
                "fastapi/params::Query",
                "fastapi/params::Header",
                "fastapi/params::Cookie",
            ],
            patterns=["class", "Param", "FieldInfo"],
        ),
    ),
    BenchTask(
        id="pattern-07",
        repo="fastapi",
        category="pattern",
        instruction=(
            "Create a new API key security class following the pattern "
            "of APIKeyQuery and APIKeyHeader. Extend APIKeyBase."
        ),
        ground_truth=GroundTruth(
            target_files=["fastapi/security/api_key.py"],
            target_symbols=[
                "fastapi/security/api_key::APIKeyBase",
                "fastapi/security/api_key::APIKeyQuery",
                "fastapi/security/api_key::APIKeyHeader",
            ],
            patterns=["class", "APIKeyBase", "__call__", "async"],
        ),
    ),
    BenchTask(
        id="pattern-08",
        repo="fastapi",
        category="pattern",
        instruction=(
            "Create a custom route class following the pattern of "
            "GzipRoute and TimedRoute from the docs examples. "
            "Extend APIRoute."
        ),
        ground_truth=GroundTruth(
            target_files=[
                "docs_src/custom_request_and_route/tutorial001_py310.py",
                "docs_src/custom_request_and_route/tutorial003_py310.py",
            ],
            target_symbols=[
                "docs_src/custom_request_and_route/tutorial001_py310::GzipRoute",
                "docs_src/custom_request_and_route/tutorial003_py310::TimedRoute",
            ],
            patterns=["class", "APIRoute", "get_route_handler"],
        ),
    ),
    # solid (2)
    BenchTask(
        id="pattern-09",
        repo="solid",
        category="pattern",
        instruction=(
            "Write a custom reactive primitive following the pattern of "
            "createSignal. It should return a tuple of [getter, setter] "
            "and accept an initial value and options."
        ),
        ground_truth=GroundTruth(
            target_files=["packages/solid/src/reactive/signal.ts"],
            target_symbols=[
                "packages/solid/src/reactive/signal::createSignal",
                "packages/solid/src/reactive/signal::SignalOptions",
            ],
            patterns=["function create", "Accessor", "Setter", "options"],
        ),
    ),
    BenchTask(
        id="pattern-10",
        repo="solid",
        category="pattern",
        instruction=(
            "Create a store helper following the createStore pattern from "
            "solid/store. Return a tuple of [store, setStore]."
        ),
        ground_truth=GroundTruth(
            target_files=["packages/solid/store/src/store.ts"],
            target_symbols=["packages/solid/store/src/store::createStore"],
            patterns=["function", "Store", "SetStoreFunction"],
        ),
    ),
]


# ── All tasks ──────────────────────────────────────────────────────

_ALL_TASKS = TRUST_TASKS + TYPE_TASKS + IMPORT_TASKS + CONTRACT_TASKS + PATTERN_TASKS

# Deterministic train/dev split: first 7 train, last 3 dev per category.
_CATEGORIES = ["trust", "type", "import", "contract", "pattern"]


def get_all_tasks() -> list[BenchTask]:
    """Return all 50 tasks."""
    return list(_ALL_TASKS)


def get_train_tasks() -> list[BenchTask]:
    """Return 35 training tasks (7 per category)."""
    train: list[BenchTask] = []
    for cat in _CATEGORIES:
        cat_tasks = [t for t in _ALL_TASKS if t.category == cat]
        train.extend(cat_tasks[:7])
    return train


def get_dev_tasks() -> list[BenchTask]:
    """Return 15 dev tasks (3 per category)."""
    dev: list[BenchTask] = []
    for cat in _CATEGORIES:
        cat_tasks = [t for t in _ALL_TASKS if t.category == cat]
        dev.extend(cat_tasks[7:])
    return dev


# ── DSPy conversion ───────────────────────────────────────────────

_FIXTURES_DIR = Path(__file__).parent / "fixtures"


def _ground_truth_to_dict(gt: GroundTruth) -> dict:
    """Serialize GroundTruth to a dict for DSPy example fields."""
    return {
        "target_files": gt.target_files,
        "target_symbols": gt.target_symbols,
        "required_types": gt.required_types,
        "required_imports": gt.required_imports,
        "patterns": gt.patterns,
        "anti_patterns": gt.anti_patterns,
    }


def to_dspy_examples(
    tasks: list[BenchTask],
    fixtures_dir: Path | None = None,
) -> list:
    """Convert BenchTasks to dspy.Example objects.

    Each example has:
    - codebase_map: the full .codebase.md content for the task's repo
    - task: the instruction text
    - ground_truth: serialized GroundTruth as JSON string
    """
    import dspy

    if fixtures_dir is None:
        fixtures_dir = _FIXTURES_DIR

    # Cache fixture contents so we only read each file once.
    fixture_cache: dict[str, str] = {}
    examples: list[dspy.Example] = []

    for task in tasks:
        # Load fixture for this repo.
        if task.repo not in fixture_cache:
            fixture_path = fixtures_dir / f"{task.repo}.codebase.md"
            fixture_cache[task.repo] = fixture_path.read_text()

        example = dspy.Example(
            codebase_map=fixture_cache[task.repo],
            task=task.instruction,
            ground_truth=json.dumps(_ground_truth_to_dict(task.ground_truth)),
        ).with_inputs("codebase_map", "task")

        examples.append(example)

    return examples
