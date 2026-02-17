## Live Codebase Map

The following is a **real-time structural map** of this codebase. It was
regenerated moments ago and reflects the current state of all files on disk.

All file paths and line numbers are accurate right now. When you edit a file,
this map updates before your next turn.

Use this map to navigate directly to the right files and line numbers without
searching. Trust these locations — they are current.

```toon
codebase:
  name: flask
  languages[1]: python
  last_indexed: 2026-02-16T21:45:13Z

modules[4]{name,path,key_types,depends_on}:
  docs,docs,,
  examples,examples,"AuthActions|FlaskTask|Recorder",
  flask,src/flask,"App|AppContext|AppContextProxy|AppGroup|Blueprint|BlueprintSetupState|CertParamType|Config|ConfigAttribute|DebugFilesKeyError|DefaultJSONProvider|DispatchingJinjaLoader|EnvironBuilder|Environment|Flask|FlaskCliRunner|FlaskClient|FlaskGroup|FlaskProxy|FormDataRoutingRedirect|JSONProvider|JSONTag|MethodView|NoAppException|NullSession|PassDict|PassList|ProxyMixin|Request|RequestProxy|Response|Scaffold|ScriptInfo|SecureCookieSession|SecureCookieSessionInterface|SeparatedPathType|SessionInterface|SessionMixin|SessionMixinProxy|TagBytes|TagDateTime|TagDict|TagMarkup|TagTuple|TagUUID|TaggedJSONSerializer|UnexpectedUnicodeError|View|_AppCtxGlobals|_AppCtxGlobalsProxy|newcls",
  tests,tests,"AppError|AsyncMethodView|AsyncView|Base|BaseView|BetterIndex|BlueprintError|ChildExceptionRegistered|ChildExceptionUnregistered|ChildView|Config|ContextConverter|CountInit|Custom|CustomEnvironment|CustomException|CustomFlask|CustomProvider|CustomRequestGlobals|DeleteView|E1|E2|E3|FailingSessionInterface|FakePath|FixedOffset|Flask|Foo|ForbiddenSubclass|ForbiddenSubclassRegistered|ForbiddenSubclassUnregistered|GetDeleteView|GetView|Index|ListConverter|MockCtx|Module|My900Error|MyAborter|MyBlueprint|MyDecoratorException|MyException|MyFlask|MyFunctionException|MySessionInterface|MyView|NS|Namespace|ObjectWithHTML|Other|OtherView|ParentException|PathAwareSessionInterface|PrefixPathMiddleware|PyBytesIO|RenderTemplateView|SessionError|StaticFileApp|StatusJSON|SubRunner|SuppressedFlask|Tag1|Tag2|TagDict|TagFoo|Test|TestGenericHandlers|TestGreenletContextCopying|TestHelpers|TestNoImports|TestRoutes|TestSendfile|TestStreaming|TestUrlFor|View|Wrapper|X|_TestHandler",

symbols[500]{fqn,kind,file,line,signature}:
  examples/tutorial/tests/conftest::AuthActions,class,examples/tutorial/tests/conftest.py,47,class AuthActions:
  examples/tutorial/tests/test_db::Recorder,class,examples/tutorial/tests/test_db.py,20,class Recorder:
  examples/celery/src/task_app/__init__::FlaskTask,class,examples/celery/src/task_app/__init__.py,30,class FlaskTask(Task):
  src/flask/sansio/blueprints::BlueprintSetupState,class,src/flask/sansio/blueprints.py,34,class BlueprintSetupState:
  src/flask/sansio/blueprints::Blueprint,class,src/flask/sansio/blueprints.py,119,class Blueprint(Scaffold):
  src/flask/sansio/app::App,class,src/flask/sansio/app.py,59,class App(Scaffold):
  src/flask/sansio/scaffold::Scaffold,class,src/flask/sansio/scaffold.py,52,class Scaffold:
  src/flask/sessions::SessionMixin,class,src/flask/sessions.py,24,"class SessionMixin(MutableMapping[str, t.Any]):"
  src/flask/sessions::SecureCookieSession,class,src/flask/sessions.py,52,"class SecureCookieSession(CallbackDict[str, t.Any], SessionMixin):"
  src/flask/sessions::NullSession,class,src/flask/sessions.py,97,class NullSession(SecureCookieSession):
  src/flask/sessions::SessionInterface,class,src/flask/sessions.py,114,class SessionInterface:
  src/flask/sessions::SecureCookieSessionInterface,class,src/flask/sessions.py,298,class SecureCookieSessionInterface(SessionInterface):
  src/flask/config::ConfigAttribute,class,src/flask/config.py,20,class ConfigAttribute(t.Generic[T]):
  src/flask/config::Config,class,src/flask/config.py,50,class Config(dict):  # type: ignore[type-arg]
  src/flask/templating::Environment,class,src/flask/templating.py,35,class Environment(BaseEnvironment):
  src/flask/templating::DispatchingJinjaLoader,class,src/flask/templating.py,48,class DispatchingJinjaLoader(BaseLoader):
  src/flask/globals::ProxyMixin,class,src/flask/globals.py,17,class ProxyMixin(t.Protocol[T]):
  src/flask/globals::FlaskProxy,class,src/flask/globals.py,22,"class FlaskProxy(ProxyMixin[Flask], Flask): ..."
  src/flask/globals::AppContextProxy,class,src/flask/globals.py,24,"class AppContextProxy(ProxyMixin[AppContext], AppContext): ..."
  src/flask/globals::_AppCtxGlobalsProxy,class,src/flask/globals.py,26,"class _AppCtxGlobalsProxy(ProxyMixin[_AppCtxGlobals], _AppCtxGlobals): ..."
  src/flask/globals::RequestProxy,class,src/flask/globals.py,28,"class RequestProxy(ProxyMixin[Request], Request): ..."
  src/flask/globals::SessionMixinProxy,class,src/flask/globals.py,30,"class SessionMixinProxy(ProxyMixin[SessionMixin], SessionMixin): ..."
  src/flask/blueprints::Blueprint,class,src/flask/blueprints.py,18,class Blueprint(SansioBlueprint):
  src/flask/json/provider::JSONProvider,class,src/flask/json/provider.py,19,class JSONProvider:
  src/flask/json/provider::DefaultJSONProvider,class,src/flask/json/provider.py,124,class DefaultJSONProvider(JSONProvider):
  src/flask/json/tag::JSONTag,class,src/flask/json/tag.py,60,class JSONTag:
  src/flask/json/tag::TagDict,class,src/flask/json/tag.py,93,class TagDict(JSONTag):
  src/flask/json/tag::PassDict,class,src/flask/json/tag.py,119,class PassDict(JSONTag):
  src/flask/json/tag::TagTuple,class,src/flask/json/tag.py,133,class TagTuple(JSONTag):
  src/flask/json/tag::PassList,class,src/flask/json/tag.py,147,class PassList(JSONTag):
  src/flask/json/tag::TagBytes,class,src/flask/json/tag.py,159,class TagBytes(JSONTag):
  src/flask/json/tag::TagMarkup,class,src/flask/json/tag.py,173,class TagMarkup(JSONTag):
  src/flask/json/tag::TagUUID,class,src/flask/json/tag.py,191,class TagUUID(JSONTag):
  src/flask/json/tag::TagDateTime,class,src/flask/json/tag.py,205,class TagDateTime(JSONTag):
  src/flask/json/tag::TaggedJSONSerializer,class,src/flask/json/tag.py,219,class TaggedJSONSerializer:
  src/flask/cli::NoAppException,class,src/flask/cli.py,37,class NoAppException(click.UsageError):
  src/flask/cli::ScriptInfo,class,src/flask/cli.py,293,class ScriptInfo:
  src/flask/cli::AppGroup,class,src/flask/cli.py,405,class AppGroup(click.Group):
  src/flask/cli::FlaskGroup,class,src/flask/cli.py,531,class FlaskGroup(AppGroup):
  src/flask/cli::CertParamType,class,src/flask/cli.py,780,class CertParamType(click.ParamType):
  src/flask/cli::SeparatedPathType,class,src/flask/cli.py,867,class SeparatedPathType(click.Path):
  src/flask/wrappers::Request,class,src/flask/wrappers.py,18,class Request(RequestBase):
  src/flask/wrappers::Response,class,src/flask/wrappers.py,222,class Response(ResponseBase):
  src/flask/app::Flask,class,src/flask/app.py,108,class Flask(App):
  src/flask/debughelpers::UnexpectedUnicodeError,class,src/flask/debughelpers.py,17,"class UnexpectedUnicodeError(AssertionError, UnicodeError):"
  src/flask/debughelpers::DebugFilesKeyError,class,src/flask/debughelpers.py,23,"class DebugFilesKeyError(KeyError, AssertionError):"
  src/flask/debughelpers::FormDataRoutingRedirect,class,src/flask/debughelpers.py,50,class FormDataRoutingRedirect(AssertionError):
  src/flask/debughelpers::newcls,class,src/flask/debughelpers.py,90,"class newcls(oldcls):  # type: ignore[valid-type, misc]"
  src/flask/ctx::_AppCtxGlobals,class,src/flask/ctx.py,29,class _AppCtxGlobals:
  src/flask/ctx::AppContext,class,src/flask/ctx.py,259,class AppContext:
  src/flask/testing::EnvironBuilder,class,src/flask/testing.py,27,class EnvironBuilder(werkzeug.test.EnvironBuilder):
  src/flask/testing::FlaskClient,class,src/flask/testing.py,109,class FlaskClient(Client):
  src/flask/testing::FlaskCliRunner,class,src/flask/testing.py,265,class FlaskCliRunner(CliRunner):
  src/flask/views::View,class,src/flask/views.py,16,class View:
  src/flask/views::MethodView,class,src/flask/views.py,138,class MethodView(View):
  tests/test_basic::PrefixPathMiddleware,class,tests/test_basic.py,269,class PrefixPathMiddleware:
  tests/test_basic::MyException,class,tests/test_basic.py,951,class MyException(Exception):
  tests/test_basic::ForbiddenSubclass,class,tests/test_basic.py,967,class ForbiddenSubclass(Forbidden):
  tests/test_basic::E1,class,tests/test_basic.py,999,class E1(Exception):
  tests/test_basic::E2,class,tests/test_basic.py,1002,class E2(Exception):
  tests/test_basic::E3,class,tests/test_basic.py,1005,"class E3(E1, E2):"
  tests/test_basic::View,class,tests/test_basic.py,1841,class View:
  tests/test_converters::ListConverter,class,tests/test_converters.py,9,class ListConverter(BaseConverter):
  tests/test_converters::ContextConverter,class,tests/test_converters.py,30,class ContextConverter(BaseConverter):
  tests/test_async::AppError,class,tests/test_async.py,14,class AppError(Exception):
  tests/test_async::BlueprintError,class,tests/test_async.py,18,class BlueprintError(Exception):
  tests/test_async::AsyncView,class,tests/test_async.py,22,class AsyncView(View):
  tests/test_async::AsyncMethodView,class,tests/test_async.py,30,class AsyncMethodView(MethodView):
  tests/test_session_interface::MySessionInterface,class,tests/test_session_interface.py,12,class MySessionInterface(SessionInterface):
  tests/test_views::Index,class,tests/test_views.py,19,class Index(flask.views.View):
  tests/test_views::Index,class,tests/test_views.py,30,class Index(flask.views.MethodView):
  tests/test_views::Index,class,tests/test_views.py,43,class Index(flask.views.MethodView):
  tests/test_views::Other,class,tests/test_views.py,50,class Other(Index):
  tests/test_views::Index,class,tests/test_views.py,64,class Index(flask.views.MethodView):
  tests/test_views::BetterIndex,class,tests/test_views.py,71,class BetterIndex(Index):
  tests/test_views::Index,class,tests/test_views.py,90,class Index(flask.views.View):
  tests/test_views::Index,class,tests/test_views.py,107,class Index(flask.views.View):
  tests/test_views::Index,class,tests/test_views.py,126,class Index(flask.views.View):
  tests/test_views::Index,class,tests/test_views.py,142,class Index(flask.views.View):
  tests/test_views::Index,class,tests/test_views.py,154,class Index(flask.views.MethodView):
  tests/test_views::Index,class,tests/test_views.py,168,class Index(flask.views.MethodView):
  tests/test_views::Index,class,tests/test_views.py,186,class Index(flask.views.View):
  tests/test_views::BaseView,class,tests/test_views.py,202,class BaseView(flask.views.MethodView):
  tests/test_views::ChildView,class,tests/test_views.py,205,class ChildView(BaseView):
  tests/test_views::GetView,class,tests/test_views.py,220,class GetView(flask.views.MethodView):
  tests/test_views::DeleteView,class,tests/test_views.py,224,class DeleteView(flask.views.MethodView):
  tests/test_views::GetDeleteView,class,tests/test_views.py,228,"class GetDeleteView(GetView, DeleteView):"
  tests/test_views::GetView,class,tests/test_views.py,239,class GetView(flask.views.MethodView):
  tests/test_views::OtherView,class,tests/test_views.py,243,class OtherView(flask.views.MethodView):
  tests/test_views::View,class,tests/test_views.py,247,"class View(GetView, OtherView):"
  tests/test_views::CountInit,class,tests/test_views.py,260,class CountInit(flask.views.View):
  tests/test_json_tag::TagDict,class,tests/test_json_tag.py,33,class TagDict(JSONTag):
  tests/test_json_tag::Foo,class,tests/test_json_tag.py,44,"class Foo:  # noqa: B903, for Python2 compatibility"
  tests/test_json_tag::TagFoo,class,tests/test_json_tag.py,48,class TagFoo(JSONTag):
  tests/test_json_tag::Tag1,class,tests/test_json_tag.py,74,class Tag1(JSONTag):
  tests/test_json_tag::Tag2,class,tests/test_json_tag.py,77,class Tag2(JSONTag):
  tests/test_subclassing::SuppressedFlask,class,tests/test_subclassing.py,7,class SuppressedFlask(flask.Flask):
  tests/test_reqctx::TestGreenletContextCopying,class,tests/test_reqctx.py,149,class TestGreenletContextCopying:
  tests/test_reqctx::SessionError,class,tests/test_reqctx.py,206,class SessionError(Exception):
  tests/test_reqctx::FailingSessionInterface,class,tests/test_reqctx.py,209,class FailingSessionInterface(SessionInterface):
  tests/test_reqctx::CustomFlask,class,tests/test_reqctx.py,213,class CustomFlask(flask.Flask):
  tests/test_reqctx::PathAwareSessionInterface,class,tests/test_reqctx.py,232,class PathAwareSessionInterface(SecureCookieSessionInterface):
  tests/test_reqctx::CustomFlask,class,tests/test_reqctx.py,239,class CustomFlask(flask.Flask):
  tests/type_check/typing_route::StatusJSON,class,tests/type_check/typing_route.py,41,class StatusJSON(t.TypedDict):
  tests/type_check/typing_route::RenderTemplateView,class,tests/type_check/typing_route.py,101,class RenderTemplateView(View):
  tests/test_blueprints::MyDecoratorException,class,tests/test_blueprints.py,47,class MyDecoratorException(Exception):
  tests/test_blueprints::MyFunctionException,class,tests/test_blueprints.py,50,class MyFunctionException(Exception):
  tests/test_blueprints::MyBlueprint,class,tests/test_blueprints.py,224,class MyBlueprint(flask.Blueprint):
  tests/test_config::Base,class,tests/test_config.py,133,class Base:
  tests/test_config::Test,class,tests/test_config.py,136,class Test(Base):
  tests/test_config::Config,class,tests/test_config.py,199,class Config(flask.Config):
  tests/test_config::Flask,class,tests/test_config.py,202,class Flask(flask.Flask):
  tests/test_user_error_handler::CustomException,class,tests/test_user_error_handler.py,11,class CustomException(Exception):
  tests/test_user_error_handler::ParentException,class,tests/test_user_error_handler.py,62,class ParentException(Exception):
  tests/test_user_error_handler::ChildExceptionUnregistered,class,tests/test_user_error_handler.py,65,class ChildExceptionUnregistered(ParentException):
  tests/test_user_error_handler::ChildExceptionRegistered,class,tests/test_user_error_handler.py,68,class ChildExceptionRegistered(ParentException):
  tests/test_user_error_handler::ForbiddenSubclassRegistered,class,tests/test_user_error_handler.py,101,class ForbiddenSubclassRegistered(Forbidden):
  tests/test_user_error_handler::ForbiddenSubclassUnregistered,class,tests/test_user_error_handler.py,104,class ForbiddenSubclassUnregistered(Forbidden):
  tests/test_user_error_handler::TestGenericHandlers,class,tests/test_user_error_handler.py,217,class TestGenericHandlers:
  tests/test_user_error_handler::Custom,class,tests/test_user_error_handler.py,220,class Custom(Exception):
  tests/test_helpers::FakePath,class,tests/test_helpers.py,11,class FakePath:
  tests/test_helpers::PyBytesIO,class,tests/test_helpers.py,25,class PyBytesIO:
  tests/test_helpers::TestSendfile,class,tests/test_helpers.py,33,class TestSendfile:
  tests/test_helpers::StaticFileApp,class,tests/test_helpers.py,75,class StaticFileApp(flask.Flask):
  tests/test_helpers::TestUrlFor,class,tests/test_helpers.py,102,class TestUrlFor:
  tests/test_helpers::MyView,class,tests/test_helpers.py,146,class MyView(MethodView):
  tests/test_helpers::MyAborter,class,tests/test_helpers.py,197,class MyAborter(werkzeug.exceptions.Aborter):
  tests/test_helpers::MyFlask,class,tests/test_helpers.py,200,class MyFlask(flask.Flask):
  tests/test_helpers::My900Error,class,tests/test_helpers.py,208,class My900Error(werkzeug.exceptions.HTTPException):
  tests/test_helpers::TestNoImports,class,tests/test_helpers.py,217,class TestNoImports:
  tests/test_helpers::TestStreaming,class,tests/test_helpers.py,236,class TestStreaming:
  tests/test_helpers::Wrapper,class,tests/test_helpers.py,267,class Wrapper:
  tests/test_helpers::TestHelpers,class,tests/test_helpers.py,333,class TestHelpers:
  tests/test_json::FixedOffset,class,tests/test_json.py,145,class FixedOffset(datetime.tzinfo):
  tests/test_json::X,class,tests/test_json.py,224,"class X:  # noqa: B903, for Python2 compatibility"
  tests/test_json::CustomProvider,class,tests/test_json.py,234,class CustomProvider(DefaultJSONProvider):
  tests/test_json::ObjectWithHTML,class,tests/test_json.py,341,class ObjectWithHTML:
  tests/test_cli::Module,class,tests/test_cli.py,49,class Module:
  tests/test_cli::Module,class,tests/test_cli.py,54,class Module:
  tests/test_cli::Module,class,tests/test_cli.py,59,class Module:
  tests/test_cli::Module,class,tests/test_cli.py,64,class Module:
  tests/test_cli::Module,class,tests/test_cli.py,73,class Module:
  tests/test_cli::Module,class,tests/test_cli.py,82,class Module:
  tests/test_cli::Module,class,tests/test_cli.py,91,class Module:
  tests/test_cli::Module,class,tests/test_cli.py,100,class Module:
  tests/test_cli::Module,class,tests/test_cli.py,109,class Module:
  tests/test_cli::Module,class,tests/test_cli.py,114,class Module:
  tests/test_cli::Module,class,tests/test_cli.py,120,class Module:
  tests/test_cli::Module,class,tests/test_cli.py,127,class Module:
  tests/test_cli::MockCtx,class,tests/test_cli.py,232,class MockCtx:
  tests/test_cli::TestRoutes,class,tests/test_cli.py,446,class TestRoutes:
  tests/test_templating::MyFlask,class,tests/test_templating.py,406,class MyFlask(flask.Flask):
  tests/test_templating::_TestHandler,class,tests/test_templating.py,493,class _TestHandler(logging.Handler):
  tests/test_templating::CustomEnvironment,class,tests/test_templating.py,525,class CustomEnvironment(flask.templating.Environment):
  tests/test_templating::CustomFlask,class,tests/test_templating.py,528,class CustomFlask(flask.Flask):
  tests/test_appctx::CustomRequestGlobals,class,tests/test_appctx.py,160,class CustomRequestGlobals:
  tests/test_regression::Foo,class,tests/test_regression.py,5,class Foo(Exception):
  tests/test_testing::Namespace,class,tests/test_testing.py,276,class Namespace:
  tests/test_testing::SubRunner,class,tests/test_testing.py,331,class SubRunner(FlaskCliRunner):
  tests/test_testing::NS,class,tests/test_testing.py,354,class NS:
  docs/conf::github_link,fn,docs/conf.py,72,"def github_link(name, rawtext, text, lineno, inliner, options=None, content=None):"
  docs/conf::setup,fn,docs/conf.py,100,def setup(app):
  examples/tutorial/tests/conftest::app,fn,examples/tutorial/tests/conftest.py,16,def app():
  examples/tutorial/tests/conftest::client,fn,examples/tutorial/tests/conftest.py,36,def client(app):
  examples/tutorial/tests/conftest::runner,fn,examples/tutorial/tests/conftest.py,42,def runner(app):
  examples/tutorial/tests/conftest::__init__,method,examples/tutorial/tests/conftest.py,48,"def __init__(self, client):"
  examples/tutorial/tests/conftest::login,method,examples/tutorial/tests/conftest.py,51,"def login(self, username=\"test\", password=\"test\"):"
  examples/tutorial/tests/conftest::logout,method,examples/tutorial/tests/conftest.py,56,def logout(self):
  examples/tutorial/tests/conftest::auth,fn,examples/tutorial/tests/conftest.py,61,def auth(client):
  examples/tutorial/tests/test_auth::test_register,fn,examples/tutorial/tests/test_auth.py,8,"def test_register(client, app):"
  examples/tutorial/tests/test_auth::test_register_validate_input,fn,examples/tutorial/tests/test_auth.py,32,"def test_register_validate_input(client, username, password, message):"
  examples/tutorial/tests/test_auth::test_login,fn,examples/tutorial/tests/test_auth.py,39,"def test_login(client, auth):"
  examples/tutorial/tests/test_auth::test_login_validate_input,fn,examples/tutorial/tests/test_auth.py,59,"def test_login_validate_input(auth, username, password, message):"
  examples/tutorial/tests/test_auth::test_logout,fn,examples/tutorial/tests/test_auth.py,64,"def test_logout(client, auth):"
  examples/tutorial/tests/test_db::test_get_close_db,fn,examples/tutorial/tests/test_db.py,8,def test_get_close_db(app):
  examples/tutorial/tests/test_db::test_init_db_command,fn,examples/tutorial/tests/test_db.py,19,"def test_init_db_command(runner, monkeypatch):"
  examples/tutorial/tests/test_factory::test_config,fn,examples/tutorial/tests/test_factory.py,4,def test_config():
  examples/tutorial/tests/test_factory::test_hello,fn,examples/tutorial/tests/test_factory.py,10,def test_hello(client):
  examples/tutorial/tests/test_blog::test_index,fn,examples/tutorial/tests/test_blog.py,6,"def test_index(client, auth):"
  examples/tutorial/tests/test_blog::test_login_required,fn,examples/tutorial/tests/test_blog.py,20,"def test_login_required(client, path):"
  examples/tutorial/tests/test_blog::test_author_required,fn,examples/tutorial/tests/test_blog.py,25,"def test_author_required(app, client, auth):"
  examples/tutorial/tests/test_blog::test_exists_required,fn,examples/tutorial/tests/test_blog.py,41,"def test_exists_required(client, auth, path):"
  examples/tutorial/tests/test_blog::test_create,fn,examples/tutorial/tests/test_blog.py,46,"def test_create(client, auth, app):"
  examples/tutorial/tests/test_blog::test_update,fn,examples/tutorial/tests/test_blog.py,57,"def test_update(client, auth, app):"
  examples/tutorial/tests/test_blog::test_create_update_validate,fn,examples/tutorial/tests/test_blog.py,69,"def test_create_update_validate(client, auth, path):"
  examples/tutorial/tests/test_blog::test_delete,fn,examples/tutorial/tests/test_blog.py,75,"def test_delete(client, auth, app):"
  examples/tutorial/flaskr/auth::login_required,fn,examples/tutorial/flaskr/auth.py,19,def login_required(view):
  examples/tutorial/flaskr/auth::load_logged_in_user,fn,examples/tutorial/flaskr/auth.py,33,def load_logged_in_user():
  examples/tutorial/flaskr/auth::register,fn,examples/tutorial/flaskr/auth.py,47,def register():
  examples/tutorial/flaskr/auth::login,fn,examples/tutorial/flaskr/auth.py,85,def login():
  examples/tutorial/flaskr/auth::logout,fn,examples/tutorial/flaskr/auth.py,113,def logout():
  examples/tutorial/flaskr/db::get_db,fn,examples/tutorial/flaskr/db.py,9,def get_db():
  examples/tutorial/flaskr/db::close_db,fn,examples/tutorial/flaskr/db.py,23,def close_db(e=None):
  examples/tutorial/flaskr/db::init_db,fn,examples/tutorial/flaskr/db.py,33,def init_db():
  examples/tutorial/flaskr/db::init_db_command,fn,examples/tutorial/flaskr/db.py,42,def init_db_command():
  examples/tutorial/flaskr/db::init_app,fn,examples/tutorial/flaskr/db.py,51,def init_app(app):
  examples/tutorial/flaskr/__init__::create_app,fn,examples/tutorial/flaskr/__init__.py,6,def create_app(test_config=None):
  examples/tutorial/flaskr/blog::index,fn,examples/tutorial/flaskr/blog.py,17,def index():
  examples/tutorial/flaskr/blog::get_post,fn,examples/tutorial/flaskr/blog.py,28,"def get_post(id, check_author=True):"
  examples/tutorial/flaskr/blog::create,fn,examples/tutorial/flaskr/blog.py,62,def create():
  examples/tutorial/flaskr/blog::update,fn,examples/tutorial/flaskr/blog.py,88,def update(id):
  examples/tutorial/flaskr/blog::delete,fn,examples/tutorial/flaskr/blog.py,115,def delete(id):
  examples/celery/src/task_app/tasks::add,fn,examples/celery/src/task_app/tasks.py,8,"def add(a: int, b: int) -> int:"
  examples/celery/src/task_app/tasks::block,fn,examples/celery/src/task_app/tasks.py,13,def block() -> None:
  examples/celery/src/task_app/tasks::process,fn,examples/celery/src/task_app/tasks.py,18,"def process(self: Task, total: int) -> object:"
  examples/celery/src/task_app/__init__::create_app,fn,examples/celery/src/task_app/__init__.py,7,def create_app() -> Flask:
  examples/celery/src/task_app/__init__::celery_init_app,fn,examples/celery/src/task_app/__init__.py,29,def celery_init_app(app: Flask) -> Celery:
  examples/celery/src/task_app/__init__::__call__,method,examples/celery/src/task_app/__init__.py,31,"def __call__(self, *args: object, **kwargs: object) -> object:"
  examples/celery/src/task_app/views::result,fn,examples/celery/src/task_app/views.py,11,"def result(id: str) -> dict[str, object]:"
  examples/celery/src/task_app/views::add,fn,examples/celery/src/task_app/views.py,22,"def add() -> dict[str, object]:"
  examples/celery/src/task_app/views::block,fn,examples/celery/src/task_app/views.py,30,"def block() -> dict[str, object]:"
  examples/celery/src/task_app/views::process,fn,examples/celery/src/task_app/views.py,36,"def process() -> dict[str, object]:"
  examples/javascript/js_example/views::index,fn,examples/javascript/js_example/views.py,10,def index(js):
  examples/javascript/js_example/views::add,fn,examples/javascript/js_example/views.py,15,def add():
  examples/javascript/tests/test_js_example::test_index,fn,examples/javascript/tests/test_js_example.py,14,"def test_index(app, client, path, template_name):"
  examples/javascript/tests/test_js_example::test_add,fn,examples/javascript/tests/test_js_example.py,25,"def test_add(client, a, b, result):"
  examples/javascript/tests/conftest::fixture_app,fn,examples/javascript/tests/conftest.py,7,def fixture_app():
  examples/javascript/tests/conftest::client,fn,examples/javascript/tests/conftest.py,14,def client(app):
  src/flask/logging::wsgi_errors_stream,fn,src/flask/logging.py,16,def wsgi_errors_stream() -> t.TextIO:
  src/flask/logging::has_level_handler,fn,src/flask/logging.py,31,def has_level_handler(logger: logging.Logger) -> bool:
  src/flask/logging::create_logger,fn,src/flask/logging.py,58,def create_logger(app: App) -> logging.Logger:
  src/flask/sansio/blueprints::__init__,method,src/flask/sansio/blueprints.py,41,def __init__(
  src/flask/sansio/blueprints::add_url_rule,method,src/flask/sansio/blueprints.py,87,def add_url_rule(
  src/flask/sansio/blueprints::__init__,method,src/flask/sansio/blueprints.py,174,def __init__(
  src/flask/sansio/blueprints::_check_setup_finished,method,src/flask/sansio/blueprints.py,213,"def _check_setup_finished(self, f_name: str) -> None:"
  src/flask/sansio/blueprints::record,method,src/flask/sansio/blueprints.py,224,"def record(self, func: DeferredSetupFunction) -> None:"
  src/flask/sansio/blueprints::record_once,method,src/flask/sansio/blueprints.py,233,"def record_once(self, func: DeferredSetupFunction) -> None:"
  src/flask/sansio/blueprints::make_setup_state,method,src/flask/sansio/blueprints.py,246,def make_setup_state(
  src/flask/sansio/blueprints::register_blueprint,method,src/flask/sansio/blueprints.py,256,"def register_blueprint(self, blueprint: Blueprint, **options: t.Any) -> None:"
  src/flask/sansio/blueprints::register,method,src/flask/sansio/blueprints.py,273,"def register(self, app: App, options: dict[str, t.Any]) -> None:"
  src/flask/sansio/blueprints::_merge_blueprint_funcs,method,src/flask/sansio/blueprints.py,379,"def _merge_blueprint_funcs(self, app: App, name: str) -> None:"
  src/flask/sansio/blueprints::add_url_rule,method,src/flask/sansio/blueprints.py,413,def add_url_rule(
  src/flask/sansio/blueprints::app_template_filter,method,src/flask/sansio/blueprints.py,444,"def app_template_filter(self, name: T_template_filter) -> T_template_filter: ..."
  src/flask/sansio/blueprints::app_template_filter,method,src/flask/sansio/blueprints.py,446,def app_template_filter(
  src/flask/sansio/blueprints::app_template_filter,method,src/flask/sansio/blueprints.py,450,def app_template_filter(
  src/flask/sansio/blueprints::add_app_template_filter,method,src/flask/sansio/blueprints.py,476,def add_app_template_filter(
  src/flask/sansio/blueprints::app_template_test,method,src/flask/sansio/blueprints.py,498,"def app_template_test(self, name: T_template_test) -> T_template_test: ..."
  src/flask/sansio/blueprints::app_template_test,method,src/flask/sansio/blueprints.py,500,def app_template_test(
  src/flask/sansio/blueprints::app_template_test,method,src/flask/sansio/blueprints.py,504,def app_template_test(
  src/flask/sansio/blueprints::add_app_template_test,method,src/flask/sansio/blueprints.py,532,def add_app_template_test(
  src/flask/sansio/blueprints::app_template_global,method,src/flask/sansio/blueprints.py,556,"def app_template_global(self, name: T_template_global) -> T_template_global: ..."
  src/flask/sansio/blueprints::app_template_global,method,src/flask/sansio/blueprints.py,558,def app_template_global(
  src/flask/sansio/blueprints::app_template_global,method,src/flask/sansio/blueprints.py,562,def app_template_global(
  src/flask/sansio/blueprints::add_app_template_global,method,src/flask/sansio/blueprints.py,590,def add_app_template_global(
  src/flask/sansio/blueprints::before_app_request,method,src/flask/sansio/blueprints.py,614,"def before_app_request(self, f: T_before_request) -> T_before_request:"
  src/flask/sansio/blueprints::after_app_request,method,src/flask/sansio/blueprints.py,624,"def after_app_request(self, f: T_after_request) -> T_after_request:"
  src/flask/sansio/blueprints::teardown_app_request,method,src/flask/sansio/blueprints.py,634,"def teardown_app_request(self, f: T_teardown) -> T_teardown:"
  src/flask/sansio/blueprints::app_context_processor,method,src/flask/sansio/blueprints.py,644,def app_context_processor(
  src/flask/sansio/blueprints::app_errorhandler,method,src/flask/sansio/blueprints.py,656,def app_errorhandler(
  src/flask/sansio/blueprints::app_url_value_preprocessor,method,src/flask/sansio/blueprints.py,673,def app_url_value_preprocessor(
  src/flask/sansio/blueprints::app_url_defaults,method,src/flask/sansio/blueprints.py,685,"def app_url_defaults(self, f: T_url_defaults) -> T_url_defaults:"
  src/flask/sansio/app::_make_timedelta,fn,src/flask/sansio/app.py,52,"def _make_timedelta(value: timedelta | int | None) -> timedelta | None:"
  src/flask/sansio/app::__init__,method,src/flask/sansio/app.py,279,def __init__(
  src/flask/sansio/app::_check_setup_finished,method,src/flask/sansio/app.py,410,"def _check_setup_finished(self, f_name: str) -> None:"
  src/flask/sansio/app::name,method,src/flask/sansio/app.py,423,def name(self) -> str:
  src/flask/sansio/app::logger,method,src/flask/sansio/app.py,440,def logger(self) -> logging.Logger:
  src/flask/sansio/app::jinja_env,method,src/flask/sansio/app.py,467,def jinja_env(self) -> Environment:
  src/flask/sansio/app::create_jinja_environment,method,src/flask/sansio/app.py,476,def create_jinja_environment(self) -> Environment:
  src/flask/sansio/app::make_config,method,src/flask/sansio/app.py,479,"def make_config(self, instance_relative: bool = False) -> Config:"
  src/flask/sansio/app::make_aborter,method,src/flask/sansio/app.py,495,def make_aborter(self) -> Aborter:
  src/flask/sansio/app::auto_find_instance_path,method,src/flask/sansio/app.py,507,def auto_find_instance_path(self) -> str:
  src/flask/sansio/app::create_global_jinja_loader,method,src/flask/sansio/app.py,520,def create_global_jinja_loader(self) -> DispatchingJinjaLoader:
  src/flask/sansio/app::select_jinja_autoescape,method,src/flask/sansio/app.py,533,"def select_jinja_autoescape(self, filename: str | None) -> bool:"
  src/flask/sansio/app::debug,method,src/flask/sansio/app.py,547,def debug(self) -> bool:
  src/flask/sansio/app::debug,method,src/flask/sansio/app.py,560,"def debug(self, value: bool) -> None:"
  src/flask/sansio/app::register_blueprint,method,src/flask/sansio/app.py,567,"def register_blueprint(self, blueprint: Blueprint, **options: t.Any) -> None:"
  src/flask/sansio/app::iter_blueprints,method,src/flask/sansio/app.py,594,def iter_blueprints(self) -> t.ValuesView[Blueprint]:
  src/flask/sansio/app::add_url_rule,method,src/flask/sansio/app.py,602,def add_url_rule(
  src/flask/sansio/app::template_filter,method,src/flask/sansio/app.py,661,"def template_filter(self, name: T_template_filter) -> T_template_filter: ..."
  src/flask/sansio/app::template_filter,method,src/flask/sansio/app.py,663,def template_filter(
  src/flask/sansio/app::template_filter,method,src/flask/sansio/app.py,667,def template_filter(
  src/flask/sansio/app::add_template_filter,method,src/flask/sansio/app.py,696,def add_template_filter(
  src/flask/sansio/app::template_test,method,src/flask/sansio/app.py,711,"def template_test(self, name: T_template_test) -> T_template_test: ..."
  src/flask/sansio/app::template_test,method,src/flask/sansio/app.py,713,def template_test(
  src/flask/sansio/app::template_test,method,src/flask/sansio/app.py,717,def template_test(
  src/flask/sansio/app::add_template_test,method,src/flask/sansio/app.py,753,def add_template_test(
  src/flask/sansio/app::template_global,method,src/flask/sansio/app.py,770,"def template_global(self, name: T_template_global) -> T_template_global: ..."
  src/flask/sansio/app::template_global,method,src/flask/sansio/app.py,772,def template_global(
  src/flask/sansio/app::template_global,method,src/flask/sansio/app.py,776,def template_global(
  src/flask/sansio/app::add_template_global,method,src/flask/sansio/app.py,807,def add_template_global(
  src/flask/sansio/app::teardown_appcontext,method,src/flask/sansio/app.py,824,"def teardown_appcontext(self, f: T_teardown) -> T_teardown:"
  src/flask/sansio/app::shell_context_processor,method,src/flask/sansio/app.py,855,def shell_context_processor(
  src/flask/sansio/app::_find_error_handler,method,src/flask/sansio/app.py,865,def _find_error_handler(
  src/flask/sansio/app::trap_http_exception,method,src/flask/sansio/app.py,890,"def trap_http_exception(self, e: Exception) -> bool:"
  src/flask/sansio/app::redirect,method,src/flask/sansio/app.py,936,"def redirect(self, location: str, code: int = 303) -> BaseResponse:"
  src/flask/sansio/app::inject_url_defaults,method,src/flask/sansio/app.py,957,"def inject_url_defaults(self, endpoint: str, values: dict[str, t.Any]) -> None:"
  src/flask/sansio/app::handle_url_build_error,method,src/flask/sansio/app.py,978,def handle_url_build_error(
  src/flask/sansio/scaffold::setupmethod,fn,src/flask/sansio/scaffold.py,42,def setupmethod(f: F) -> F:
  src/flask/sansio/scaffold::__init__,method,src/flask/sansio/scaffold.py,75,def __init__(
  src/flask/sansio/scaffold::__repr__,method,src/flask/sansio/scaffold.py,217,def __repr__(self) -> str:
  src/flask/sansio/scaffold::_check_setup_finished,method,src/flask/sansio/scaffold.py,220,"def _check_setup_finished(self, f_name: str) -> None:"
  src/flask/sansio/scaffold::static_folder,method,src/flask/sansio/scaffold.py,224,"def static_folder(self) -> str | None:"
  src/flask/sansio/scaffold::static_folder,method,src/flask/sansio/scaffold.py,234,"def static_folder(self, value: str | os.PathLike[str] | None) -> None:"
  src/flask/sansio/scaffold::has_static_folder,method,src/flask/sansio/scaffold.py,241,def has_static_folder(self) -> bool:
  src/flask/sansio/scaffold::static_url_path,method,src/flask/sansio/scaffold.py,249,"def static_url_path(self) -> str | None:"
  src/flask/sansio/scaffold::static_url_path,method,src/flask/sansio/scaffold.py,265,"def static_url_path(self, value: str | None) -> None:"
  src/flask/sansio/scaffold::jinja_loader,method,src/flask/sansio/scaffold.py,272,"def jinja_loader(self) -> BaseLoader | None:"
  src/flask/sansio/scaffold::_method_route,method,src/flask/sansio/scaffold.py,284,def _method_route(
  src/flask/sansio/scaffold::get,method,src/flask/sansio/scaffold.py,296,"def get(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:"
  src/flask/sansio/scaffold::post,method,src/flask/sansio/scaffold.py,304,"def post(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:"
  src/flask/sansio/scaffold::put,method,src/flask/sansio/scaffold.py,312,"def put(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:"
  src/flask/sansio/scaffold::delete,method,src/flask/sansio/scaffold.py,320,"def delete(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:"
  src/flask/sansio/scaffold::patch,method,src/flask/sansio/scaffold.py,328,"def patch(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:"
  src/flask/sansio/scaffold::route,method,src/flask/sansio/scaffold.py,336,"def route(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:"
  src/flask/sansio/scaffold::add_url_rule,method,src/flask/sansio/scaffold.py,368,def add_url_rule(
  src/flask/sansio/scaffold::endpoint,method,src/flask/sansio/scaffold.py,436,"def endpoint(self, endpoint: str) -> t.Callable[[F], F]:"
  src/flask/sansio/scaffold::before_request,method,src/flask/sansio/scaffold.py,460,"def before_request(self, f: T_before_request) -> T_before_request:"
  src/flask/sansio/scaffold::after_request,method,src/flask/sansio/scaffold.py,487,"def after_request(self, f: T_after_request) -> T_after_request:"
  src/flask/sansio/scaffold::teardown_request,method,src/flask/sansio/scaffold.py,508,"def teardown_request(self, f: T_teardown) -> T_teardown:"
  src/flask/sansio/scaffold::context_processor,method,src/flask/sansio/scaffold.py,542,def context_processor(
  src/flask/sansio/scaffold::url_value_preprocessor,method,src/flask/sansio/scaffold.py,559,def url_value_preprocessor(
  src/flask/sansio/scaffold::url_defaults,method,src/flask/sansio/scaffold.py,584,"def url_defaults(self, f: T_url_defaults) -> T_url_defaults:"
  src/flask/sansio/scaffold::errorhandler,method,src/flask/sansio/scaffold.py,598,def errorhandler(
  src/flask/sansio/scaffold::register_error_handler,method,src/flask/sansio/scaffold.py,642,def register_error_handler(
  src/flask/sansio/scaffold::_get_exc_class_and_code,method,src/flask/sansio/scaffold.py,657,def _get_exc_class_and_code(
  src/flask/sansio/scaffold::_endpoint_from_view_func,fn,src/flask/sansio/scaffold.py,701,def _endpoint_from_view_func(view_func: ft.RouteCallable) -> str:
  src/flask/sansio/scaffold::_find_package_path,fn,src/flask/sansio/scaffold.py,709,def _find_package_path(import_name: str) -> str:
  src/flask/sansio/scaffold::find_package,fn,src/flask/sansio/scaffold.py,754,"def find_package(import_name: str) -> tuple[str | None, str]:"
  src/flask/sessions::permanent,method,src/flask/sessions.py,28,def permanent(self) -> bool:
  src/flask/sessions::permanent,method,src/flask/sessions.py,33,"def permanent(self, value: bool) -> None:"
  src/flask/sessions::__init__,method,src/flask/sessions.py,74,def __init__(
  src/flask/sessions::__getitem__,method,src/flask/sessions.py,84,"def __getitem__(self, key: str) -> t.Any:"
  src/flask/sessions::get,method,src/flask/sessions.py,88,"def get(self, key: str, default: t.Any = None) -> t.Any:"
  src/flask/sessions::setdefault,method,src/flask/sessions.py,92,"def setdefault(self, key: str, default: t.Any = None) -> t.Any:"
  src/flask/sessions::_fail,method,src/flask/sessions.py,103,"def _fail(self, *args: t.Any, **kwargs: t.Any) -> t.NoReturn:"
  src/flask/sessions::make_null_session,method,src/flask/sessions.py,164,"def make_null_session(self, app: Flask) -> NullSession:"
  src/flask/sessions::is_null_session,method,src/flask/sessions.py,176,"def is_null_session(self, obj: object) -> bool:"
  src/flask/sessions::get_cookie_name,method,src/flask/sessions.py,185,"def get_cookie_name(self, app: Flask) -> str:"
  src/flask/sessions::get_cookie_domain,method,src/flask/sessions.py,189,"def get_cookie_domain(self, app: Flask) -> str | None:"
  src/flask/sessions::get_cookie_path,method,src/flask/sessions.py,201,"def get_cookie_path(self, app: Flask) -> str:"
  src/flask/sessions::get_cookie_httponly,method,src/flask/sessions.py,209,"def get_cookie_httponly(self, app: Flask) -> bool:"
  src/flask/sessions::get_cookie_secure,method,src/flask/sessions.py,216,"def get_cookie_secure(self, app: Flask) -> bool:"
  src/flask/sessions::get_cookie_samesite,method,src/flask/sessions.py,222,"def get_cookie_samesite(self, app: Flask) -> str | None:"
  src/flask/sessions::get_cookie_partitioned,method,src/flask/sessions.py,229,"def get_cookie_partitioned(self, app: Flask) -> bool:"
  src/flask/sessions::get_expiration_time,method,src/flask/sessions.py,237,"def get_expiration_time(self, app: Flask, session: SessionMixin) -> datetime | None:"
  src/flask/sessions::should_set_cookie,method,src/flask/sessions.py,247,"def should_set_cookie(self, app: Flask, session: SessionMixin) -> bool:"
  src/flask/sessions::open_session,method,src/flask/sessions.py,263,"def open_session(self, app: Flask, request: Request) -> SessionMixin | None:"
  src/flask/sessions::save_session,method,src/flask/sessions.py,277,def save_session(
  src/flask/sessions::_lazy_sha1,fn,src/flask/sessions.py,290,"def _lazy_sha1(string: bytes = b\"\") -> t.Any:"
  src/flask/sessions::get_signing_serializer,method,src/flask/sessions.py,317,"def get_signing_serializer(self, app: Flask) -> URLSafeTimedSerializer | None:"
  src/flask/sessions::open_session,method,src/flask/sessions.py,337,"def open_session(self, app: Flask, request: Request) -> SecureCookieSession | None:"
  src/flask/sessions::save_session,method,src/flask/sessions.py,351,def save_session(
  src/flask/config::__init__,method,src/flask/config.py,23,def __init__(
  src/flask/config::__get__,method,src/flask/config.py,30,"def __get__(self, obj: None, owner: None) -> te.Self: ..."
  src/flask/config::__get__,method,src/flask/config.py,33,"def __get__(self, obj: App, owner: type[App]) -> T: ..."
  src/flask/config::__get__,method,src/flask/config.py,35,"def __get__(self, obj: App | None, owner: type[App] | None = None) -> T | te.Self:"
  src/flask/config::__set__,method,src/flask/config.py,46,"def __set__(self, obj: App, value: t.Any) -> None:"
  src/flask/config::__init__,method,src/flask/config.py,94,def __init__(
  src/flask/config::from_envvar,method,src/flask/config.py,102,"def from_envvar(self, variable_name: str, silent: bool = False) -> bool:"
  src/flask/config::from_prefixed_env,method,src/flask/config.py,126,def from_prefixed_env(
  src/flask/config::from_pyfile,method,src/flask/config.py,187,def from_pyfile(
  src/flask/config::from_object,method,src/flask/config.py,218,"def from_object(self, obj: object | str) -> None:"
  src/flask/config::from_file,method,src/flask/config.py,256,def from_file(
  src/flask/config::from_mapping,method,src/flask/config.py,304,def from_mapping(
  src/flask/config::get_namespace,method,src/flask/config.py,323,def get_namespace(
  src/flask/config::__repr__,method,src/flask/config.py,366,def __repr__(self) -> str:
  src/flask/templating::_default_template_ctx_processor,fn,src/flask/templating.py,21,"def _default_template_ctx_processor() -> dict[str, t.Any]:"
  src/flask/templating::__init__,method,src/flask/templating.py,41,"def __init__(self, app: App, **options: t.Any) -> None:"
  src/flask/templating::__init__,method,src/flask/templating.py,53,"def __init__(self, app: App) -> None:"
  src/flask/templating::get_source,method,src/flask/templating.py,56,def get_source(
  src/flask/templating::_get_source_explained,method,src/flask/templating.py,63,def _get_source_explained(
  src/flask/templating::_get_source_fast,method,src/flask/templating.py,87,def _get_source_fast(
  src/flask/templating::_iter_loaders,method,src/flask/templating.py,97,"def _iter_loaders(self, template: str) -> t.Iterator[tuple[Scaffold, BaseLoader]]:"
  src/flask/templating::list_templates,method,src/flask/templating.py,107,def list_templates(self) -> list[str]:
  src/flask/templating::_render,fn,src/flask/templating.py,122,"def _render(ctx: AppContext, template: Template, context: dict[str, t.Any]) -> str:"
  src/flask/templating::render_template,fn,src/flask/templating.py,135,def render_template(
  src/flask/templating::render_template_string,fn,src/flask/templating.py,150,"def render_template_string(source: str, **context: t.Any) -> str:"
  src/flask/templating::_stream,fn,src/flask/templating.py,162,def _stream(
  src/flask/templating::stream_template,fn,src/flask/templating.py,180,def stream_template(
  src/flask/templating::stream_template_string,fn,src/flask/templating.py,199,"def stream_template_string(source: str, **context: t.Any) -> t.Iterator[str]:"
  src/flask/globals::_get_current_object,method,src/flask/globals.py,18,def _get_current_object(self) -> T: ...
  src/flask/globals::__getattr__,fn,src/flask/globals.py,65,def __getattr__(name: str) -> t.Any:
  src/flask/blueprints::__init__,method,src/flask/blueprints.py,19,def __init__(
  src/flask/blueprints::get_send_file_max_age,method,src/flask/blueprints.py,55,"def get_send_file_max_age(self, filename: str | None) -> int | None:"
  src/flask/blueprints::send_static_file,method,src/flask/blueprints.py,82,"def send_static_file(self, filename: str) -> Response:"
  src/flask/blueprints::open_resource,method,src/flask/blueprints.py,104,def open_resource(
  src/flask/json/provider::__init__,method,src/flask/json/provider.py,38,"def __init__(self, app: App) -> None:"
  src/flask/json/provider::dumps,method,src/flask/json/provider.py,41,"def dumps(self, obj: t.Any, **kwargs: t.Any) -> str:"
  src/flask/json/provider::dump,method,src/flask/json/provider.py,49,"def dump(self, obj: t.Any, fp: t.IO[str], **kwargs: t.Any) -> None:"
  src/flask/json/provider::loads,method,src/flask/json/provider.py,59,"def loads(self, s: str | bytes, **kwargs: t.Any) -> t.Any:"
  src/flask/json/provider::load,method,src/flask/json/provider.py,67,"def load(self, fp: t.IO[t.AnyStr], **kwargs: t.Any) -> t.Any:"
  src/flask/json/provider::_prepare_response_obj,method,src/flask/json/provider.py,75,def _prepare_response_obj(
  src/flask/json/provider::response,method,src/flask/json/provider.py,89,"def response(self, *args: t.Any, **kwargs: t.Any) -> Response:"
  src/flask/json/provider::_default,fn,src/flask/json/provider.py,108,def _default(o: t.Any) -> t.Any:
  src/flask/json/provider::dumps,method,src/flask/json/provider.py,166,"def dumps(self, obj: t.Any, **kwargs: t.Any) -> str:"
  src/flask/json/provider::loads,method,src/flask/json/provider.py,181,"def loads(self, s: str | bytes, **kwargs: t.Any) -> t.Any:"
  src/flask/json/provider::response,method,src/flask/json/provider.py,189,"def response(self, *args: t.Any, **kwargs: t.Any) -> Response:"
  src/flask/json/__init__::dumps,fn,src/flask/json/__init__.py,13,"def dumps(obj: t.Any, **kwargs: t.Any) -> str:"
  src/flask/json/__init__::dump,fn,src/flask/json/__init__.py,47,"def dump(obj: t.Any, fp: t.IO[str], **kwargs: t.Any) -> None:"
  src/flask/json/__init__::loads,fn,src/flask/json/__init__.py,77,"def loads(s: str | bytes, **kwargs: t.Any) -> t.Any:"
  src/flask/json/__init__::load,fn,src/flask/json/__init__.py,108,"def load(fp: t.IO[t.AnyStr], **kwargs: t.Any) -> t.Any:"
  src/flask/json/__init__::jsonify,fn,src/flask/json/__init__.py,138,"def jsonify(*args: t.Any, **kwargs: t.Any) -> Response:"
  src/flask/json/tag::__init__,method,src/flask/json/tag.py,69,"def __init__(self, serializer: TaggedJSONSerializer) -> None:"
  src/flask/json/tag::check,method,src/flask/json/tag.py,73,"def check(self, value: t.Any) -> bool:"
  src/flask/json/tag::to_json,method,src/flask/json/tag.py,77,"def to_json(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::to_python,method,src/flask/json/tag.py,82,"def to_python(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::tag,method,src/flask/json/tag.py,87,"def tag(self, value: t.Any) -> dict[str, t.Any]:"
  src/flask/json/tag::check,method,src/flask/json/tag.py,103,"def check(self, value: t.Any) -> bool:"
  src/flask/json/tag::to_json,method,src/flask/json/tag.py,110,"def to_json(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::to_python,method,src/flask/json/tag.py,114,"def to_python(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::check,method,src/flask/json/tag.py,122,"def check(self, value: t.Any) -> bool:"
  src/flask/json/tag::to_json,method,src/flask/json/tag.py,125,"def to_json(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::check,method,src/flask/json/tag.py,137,"def check(self, value: t.Any) -> bool:"
  src/flask/json/tag::to_json,method,src/flask/json/tag.py,140,"def to_json(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::to_python,method,src/flask/json/tag.py,143,"def to_python(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::check,method,src/flask/json/tag.py,150,"def check(self, value: t.Any) -> bool:"
  src/flask/json/tag::to_json,method,src/flask/json/tag.py,153,"def to_json(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::check,method,src/flask/json/tag.py,163,"def check(self, value: t.Any) -> bool:"
  src/flask/json/tag::to_json,method,src/flask/json/tag.py,166,"def to_json(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::to_python,method,src/flask/json/tag.py,169,"def to_python(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::check,method,src/flask/json/tag.py,181,"def check(self, value: t.Any) -> bool:"
  src/flask/json/tag::to_json,method,src/flask/json/tag.py,184,"def to_json(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::to_python,method,src/flask/json/tag.py,187,"def to_python(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::check,method,src/flask/json/tag.py,195,"def check(self, value: t.Any) -> bool:"
  src/flask/json/tag::to_json,method,src/flask/json/tag.py,198,"def to_json(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::to_python,method,src/flask/json/tag.py,201,"def to_python(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::check,method,src/flask/json/tag.py,209,"def check(self, value: t.Any) -> bool:"
  src/flask/json/tag::to_json,method,src/flask/json/tag.py,212,"def to_json(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::to_python,method,src/flask/json/tag.py,215,"def to_python(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::__init__,method,src/flask/json/tag.py,249,def __init__(self) -> None:
  src/flask/json/tag::register,method,src/flask/json/tag.py,256,def register(
  src/flask/json/tag::tag,method,src/flask/json/tag.py,289,"def tag(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::untag,method,src/flask/json/tag.py,297,"def untag(self, value: dict[str, t.Any]) -> t.Any:"
  src/flask/json/tag::_untag_scan,method,src/flask/json/tag.py,309,"def _untag_scan(self, value: t.Any) -> t.Any:"
  src/flask/json/tag::dumps,method,src/flask/json/tag.py,321,"def dumps(self, value: t.Any) -> str:"
  src/flask/json/tag::loads,method,src/flask/json/tag.py,325,"def loads(self, value: str) -> t.Any:"
  src/flask/cli::find_best_app,fn,src/flask/cli.py,41,def find_best_app(module: ModuleType) -> Flask:
  src/flask/cli::_called_with_wrong_args,fn,src/flask/cli.py,94,"def _called_with_wrong_args(f: t.Callable[..., Flask]) -> bool:"
  src/flask/cli::find_app_by_string,fn,src/flask/cli.py,120,"def find_app_by_string(module: ModuleType, app_name: str) -> Flask:"
  src/flask/cli::prepare_import,fn,src/flask/cli.py,200,def prepare_import(path: str) -> str:
  src/flask/cli::locate_app,fn,src/flask/cli.py,230,def locate_app(
  src/flask/cli::locate_app,fn,src/flask/cli.py,236,def locate_app(
  src/flask/cli::locate_app,fn,src/flask/cli.py,241,def locate_app(
  src/flask/cli::get_version,fn,src/flask/cli.py,267,"def get_version(ctx: click.Context, param: click.Parameter, value: t.Any) -> None:"
  src/flask/cli::__init__,method,src/flask/cli.py,305,def __init__(
  src/flask/cli::load_app,method,src/flask/cli.py,333,def load_app(self) -> Flask:
  src/flask/cli::with_appcontext,fn,src/flask/cli.py,380,def with_appcontext(f: F) -> F:
  src/flask/cli::command,method,src/flask/cli.py,413,def command(  # type: ignore[override]
  src/flask/cli::group,method,src/flask/cli.py,429,def group(  # type: ignore[override]
  src/flask/cli::_set_app,fn,src/flask/cli.py,440,"def _set_app(ctx: click.Context, param: click.Option, value: str | None) -> str | None:"
  src/flask/cli::_set_debug,fn,src/flask/cli.py,468,"def _set_debug(ctx: click.Context, param: click.Option, value: bool) -> bool | None:"
  src/flask/cli::_env_file_callback,fn,src/flask/cli.py,493,def _env_file_callback(
  src/flask/cli::__init__,method,src/flask/cli.py,563,def __init__(
  src/flask/cli::_load_plugin_commands,method,src/flask/cli.py,600,def _load_plugin_commands(self) -> None:
  src/flask/cli::get_command,method,src/flask/cli.py,609,"def get_command(self, ctx: click.Context, name: str) -> click.Command | None:"
  src/flask/cli::list_commands,method,src/flask/cli.py,636,"def list_commands(self, ctx: click.Context) -> list[str]:"
  src/flask/cli::make_context,method,src/flask/cli.py,657,def make_context(
  src/flask/cli::parse_args,method,src/flask/cli.py,678,"def parse_args(self, ctx: click.Context, args: list[str]) -> list[str]:"
  src/flask/cli::_path_is_ancestor,fn,src/flask/cli.py,691,"def _path_is_ancestor(path: str, other: str) -> bool:"
  src/flask/cli::load_dotenv,fn,src/flask/cli.py,698,def load_dotenv(
  src/flask/cli::show_server_banner,fn,src/flask/cli.py,766,"def show_server_banner(debug: bool, app_import_path: str | None) -> None:"
  src/flask/cli::__init__,method,src/flask/cli.py,788,def __init__(self) -> None:
  src/flask/cli::convert,method,src/flask/cli.py,791,def convert(
  src/flask/cli::_validate_key,fn,src/flask/cli.py,828,"def _validate_key(ctx: click.Context, param: click.Parameter, value: t.Any) -> t.Any:"
  src/flask/cli::convert,method,src/flask/cli.py,873,def convert(
  src/flask/cli::run_command,fn,src/flask/cli.py,935,def run_command(
  src/flask/cli::shell_command,fn,src/flask/cli.py,1001,def shell_command() -> None:
  src/flask/cli::routes_command,fn,src/flask/cli.py,1061,"def routes_command(sort: str, all_methods: bool) -> None:"
  src/flask/cli::main,fn,src/flask/cli.py,1122,def main() -> None:
  src/flask/wrappers::max_content_length,method,src/flask/wrappers.py,60,"def max_content_length(self) -> int | None:"
  src/flask/wrappers::max_content_length,method,src/flask/wrappers.py,89,"def max_content_length(self, value: int | None) -> None:"
  src/flask/wrappers::max_form_memory_size,method,src/flask/wrappers.py,93,"def max_form_memory_size(self) -> int | None:"
  src/flask/wrappers::max_form_memory_size,method,src/flask/wrappers.py,116,"def max_form_memory_size(self, value: int | None) -> None:"
  src/flask/wrappers::max_form_parts,method,src/flask/wrappers.py,120,"def max_form_parts(self) -> int | None:"
  src/flask/wrappers::max_form_parts,method,src/flask/wrappers.py,143,"def max_form_parts(self, value: int | None) -> None:"
  src/flask/wrappers::endpoint,method,src/flask/wrappers.py,147,"def endpoint(self) -> str | None:"
  src/flask/wrappers::blueprint,method,src/flask/wrappers.py,162,"def blueprint(self) -> str | None:"
  src/flask/wrappers::blueprints,method,src/flask/wrappers.py,181,def blueprints(self) -> list[str]:
  src/flask/wrappers::_load_form_data,method,src/flask/wrappers.py,197,def _load_form_data(self) -> None:
  src/flask/wrappers::on_json_loading_failed,method,src/flask/wrappers.py,212,"def on_json_loading_failed(self, e: ValueError | None) -> t.Any:"
  src/flask/wrappers::max_cookie_size,method,src/flask/wrappers.py,247,def max_cookie_size(self) -> int:  # type: ignore
  src/flask/app::_make_timedelta,fn,src/flask/app.py,72,"def _make_timedelta(value: timedelta | int | None) -> timedelta | None:"
  src/flask/app::remove_ctx,fn,src/flask/app.py,84,def remove_ctx(f: F) -> F:
  src/flask/app::add_ctx,fn,src/flask/app.py,96,def add_ctx(f: F) -> F:
  src/flask/app::__init_subclass__,method,src/flask/app.py,253,"def __init_subclass__(cls, **kwargs: t.Any) -> None:"
  src/flask/app::__init__,method,src/flask/app.py,309,def __init__(
  src/flask/app::get_send_file_max_age,method,src/flask/app.py,364,"def get_send_file_max_age(self, filename: str | None) -> int | None:"
  src/flask/app::send_static_file,method,src/flask/app.py,391,"def send_static_file(self, filename: str) -> Response:"
  src/flask/app::open_resource,method,src/flask/app.py,413,def open_resource(
  src/flask/app::open_instance_resource,method,src/flask/app.py,446,def open_instance_resource(
  src/flask/app::create_jinja_environment,method,src/flask/app.py,468,def create_jinja_environment(self) -> Environment:
  src/flask/app::create_url_adapter,method,src/flask/app.py,508,"def create_url_adapter(self, request: Request | None) -> MapAdapter | None:"
  src/flask/app::raise_routing_exception,method,src/flask/app.py,561,"def raise_routing_exception(self, request: Request) -> t.NoReturn:"
  src/flask/app::update_template_context,method,src/flask/app.py,589,def update_template_context(
  src/flask/app::make_shell_context,method,src/flask/app.py,619,"def make_shell_context(self) -> dict[str, t.Any]:"
  src/flask/app::run,method,src/flask/app.py,631,def run(
  src/flask/app::test_client,method,src/flask/app.py,754,"def test_client(self, use_cookies: bool = True, **kwargs: t.Any) -> FlaskClient:"
  src/flask/app::test_cli_runner,method,src/flask/app.py,812,"def test_cli_runner(self, **kwargs: t.Any) -> FlaskCliRunner:"
  src/flask/app::handle_http_exception,method,src/flask/app.py,829,def handle_http_exception(
  src/flask/app::handle_user_exception,method,src/flask/app.py,864,def handle_user_exception(
  src/flask/app::handle_exception,method,src/flask/app.py,896,"def handle_exception(self, ctx: AppContext, e: Exception) -> Response:"
  src/flask/app::log_exception,method,src/flask/app.py,949,def log_exception(
  src/flask/app::dispatch_request,method,src/flask/app.py,965,"def dispatch_request(self, ctx: AppContext) -> ft.ResponseReturnValue:"
  src/flask/app::full_dispatch_request,method,src/flask/app.py,991,"def full_dispatch_request(self, ctx: AppContext) -> Response:"
  src/flask/app::finalize_request,method,src/flask/app.py,1020,def finalize_request(
  src/flask/app::make_default_options_response,method,src/flask/app.py,1052,"def make_default_options_response(self, ctx: AppContext) -> Response:"
  src/flask/app::ensure_sync,method,src/flask/app.py,1064,"def ensure_sync(self, func: t.Callable[..., t.Any]) -> t.Callable[..., t.Any]:"
  src/flask/app::async_to_sync,method,src/flask/app.py,1078,def async_to_sync(
  src/flask/app::url_for,method,src/flask/app.py,1101,def url_for(
  src/flask/app::make_response,method,src/flask/app.py,1223,"def make_response(self, rv: ft.ResponseReturnValue) -> Response:"
  # ... 585 more symbols omitted

hierarchies[115]{symbol,relationship,target,file,line}:
  tests/test_basic::ForbiddenSubclass,extends,Forbidden,tests/test_basic.py,967
  tests/test_basic::E3,extends,E1,tests/test_basic.py,1005
  tests/test_basic::E3,extends,E2,tests/test_basic.py,1005
  tests/test_converters::ListConverter,extends,BaseConverter,tests/test_converters.py,9
  tests/test_converters::ContextConverter,extends,BaseConverter,tests/test_converters.py,30
  tests/test_async::AsyncView,extends,View,tests/test_async.py,22
  tests/test_async::AsyncMethodView,extends,MethodView,tests/test_async.py,30
  tests/test_session_interface::MySessionInterface,extends,SessionInterface,tests/test_session_interface.py,12
  tests/test_views::Index,extends,flask.views.View,tests/test_views.py,19
  tests/test_views::Index,extends,flask.views.MethodView,tests/test_views.py,30
  tests/test_views::Index,extends,flask.views.MethodView,tests/test_views.py,43
  tests/test_views::Other,extends,Index,tests/test_views.py,50
  tests/test_views::Index,extends,flask.views.MethodView,tests/test_views.py,64
  tests/test_views::BetterIndex,extends,Index,tests/test_views.py,71
  tests/test_views::Index,extends,flask.views.View,tests/test_views.py,90
  tests/test_views::Index,extends,flask.views.View,tests/test_views.py,107
  tests/test_views::Index,extends,flask.views.View,tests/test_views.py,126
  tests/test_views::Index,extends,flask.views.View,tests/test_views.py,142
  tests/test_views::Index,extends,flask.views.MethodView,tests/test_views.py,154
  tests/test_views::Index,extends,flask.views.MethodView,tests/test_views.py,168
  tests/test_views::Index,extends,flask.views.View,tests/test_views.py,186
  tests/test_views::BaseView,extends,flask.views.MethodView,tests/test_views.py,202
  tests/test_views::ChildView,extends,BaseView,tests/test_views.py,205
  tests/test_views::GetView,extends,flask.views.MethodView,tests/test_views.py,220
  tests/test_views::DeleteView,extends,flask.views.MethodView,tests/test_views.py,224
  tests/test_views::GetDeleteView,extends,GetView,tests/test_views.py,228
  tests/test_views::GetDeleteView,extends,DeleteView,tests/test_views.py,228
  tests/test_views::GetView,extends,flask.views.MethodView,tests/test_views.py,239
  tests/test_views::OtherView,extends,flask.views.MethodView,tests/test_views.py,243
  tests/test_views::View,extends,GetView,tests/test_views.py,247
  tests/test_views::View,extends,OtherView,tests/test_views.py,247
  tests/test_views::CountInit,extends,flask.views.View,tests/test_views.py,260
  tests/test_json_tag::TagDict,extends,JSONTag,tests/test_json_tag.py,33
  tests/test_json_tag::TagFoo,extends,JSONTag,tests/test_json_tag.py,48
  tests/test_json_tag::Tag1,extends,JSONTag,tests/test_json_tag.py,74
  tests/test_json_tag::Tag2,extends,JSONTag,tests/test_json_tag.py,77
  tests/test_subclassing::SuppressedFlask,extends,flask.Flask,tests/test_subclassing.py,7
  tests/test_reqctx::FailingSessionInterface,extends,SessionInterface,tests/test_reqctx.py,209
  tests/test_reqctx::CustomFlask,extends,flask.Flask,tests/test_reqctx.py,213
  tests/test_reqctx::PathAwareSessionInterface,extends,SecureCookieSessionInterface,tests/test_reqctx.py,232
  tests/test_reqctx::CustomFlask,extends,flask.Flask,tests/test_reqctx.py,239
  tests/type_check/typing_route::StatusJSON,extends,t.TypedDict,tests/type_check/typing_route.py,41
  tests/type_check/typing_route::RenderTemplateView,extends,View,tests/type_check/typing_route.py,101
  tests/test_blueprints::MyBlueprint,extends,flask.Blueprint,tests/test_blueprints.py,224
  tests/test_config::Test,extends,Base,tests/test_config.py,136
  tests/test_config::Config,extends,flask.Config,tests/test_config.py,199
  tests/test_config::Flask,extends,flask.Flask,tests/test_config.py,202
  tests/test_user_error_handler::ChildExceptionUnregistered,extends,ParentException,tests/test_user_error_handler.py,65
  tests/test_user_error_handler::ChildExceptionRegistered,extends,ParentException,tests/test_user_error_handler.py,68
  tests/test_user_error_handler::ForbiddenSubclassRegistered,extends,Forbidden,tests/test_user_error_handler.py,101
  tests/test_user_error_handler::ForbiddenSubclassUnregistered,extends,Forbidden,tests/test_user_error_handler.py,104
  tests/test_helpers::StaticFileApp,extends,flask.Flask,tests/test_helpers.py,75
  tests/test_helpers::MyView,extends,MethodView,tests/test_helpers.py,146
  tests/test_helpers::MyAborter,extends,werkzeug.exceptions.Aborter,tests/test_helpers.py,197
  tests/test_helpers::MyFlask,extends,flask.Flask,tests/test_helpers.py,200
  tests/test_helpers::My900Error,extends,werkzeug.exceptions.HTTPException,tests/test_helpers.py,208
  tests/test_json::FixedOffset,extends,datetime.tzinfo,tests/test_json.py,145
  tests/test_json::CustomProvider,extends,DefaultJSONProvider,tests/test_json.py,234
  tests/test_templating::MyFlask,extends,flask.Flask,tests/test_templating.py,406
  tests/test_templating::_TestHandler,extends,logging.Handler,tests/test_templating.py,493
  tests/test_templating::CustomEnvironment,extends,flask.templating.Environment,tests/test_templating.py,525
  tests/test_templating::CustomFlask,extends,flask.Flask,tests/test_templating.py,528
  tests/test_testing::SubRunner,extends,FlaskCliRunner,tests/test_testing.py,331
  examples/celery/src/task_app/__init__::FlaskTask,extends,Task,examples/celery/src/task_app/__init__.py,30
  src/flask/sansio/blueprints::Blueprint,extends,Scaffold,src/flask/sansio/blueprints.py,119
  src/flask/sansio/app::App,extends,Scaffold,src/flask/sansio/app.py,59
  src/flask/sessions::SessionMixin,extends,MutableMapping[str,src/flask/sessions.py,24
  src/flask/sessions::SessionMixin,extends,t.Any],src/flask/sessions.py,24
  src/flask/sessions::SecureCookieSession,extends,CallbackDict[str,src/flask/sessions.py,52
  src/flask/sessions::SecureCookieSession,extends,t.Any],src/flask/sessions.py,52
  src/flask/sessions::SecureCookieSession,extends,SessionMixin,src/flask/sessions.py,52
  src/flask/sessions::NullSession,extends,SecureCookieSession,src/flask/sessions.py,97
  src/flask/sessions::SecureCookieSessionInterface,extends,SessionInterface,src/flask/sessions.py,298
  src/flask/config::ConfigAttribute,extends,t.Generic,src/flask/config.py,20
  src/flask/config::Config,extends,dict,src/flask/config.py,50
  src/flask/templating::Environment,extends,BaseEnvironment,src/flask/templating.py,35
  src/flask/templating::DispatchingJinjaLoader,extends,BaseLoader,src/flask/templating.py,48
  src/flask/globals::ProxyMixin,extends,t.Protocol,src/flask/globals.py,17
  src/flask/globals::FlaskProxy,extends,ProxyMixin,src/flask/globals.py,22
  src/flask/globals::FlaskProxy,extends,Flask,src/flask/globals.py,22
  src/flask/globals::AppContextProxy,extends,ProxyMixin,src/flask/globals.py,24
  src/flask/globals::AppContextProxy,extends,AppContext,src/flask/globals.py,24
  src/flask/globals::_AppCtxGlobalsProxy,extends,ProxyMixin,src/flask/globals.py,26
  src/flask/globals::_AppCtxGlobalsProxy,extends,_AppCtxGlobals,src/flask/globals.py,26
  src/flask/globals::RequestProxy,extends,ProxyMixin,src/flask/globals.py,28
  src/flask/globals::RequestProxy,extends,Request,src/flask/globals.py,28
  src/flask/globals::SessionMixinProxy,extends,ProxyMixin,src/flask/globals.py,30
  src/flask/globals::SessionMixinProxy,extends,SessionMixin,src/flask/globals.py,30
  src/flask/blueprints::Blueprint,extends,SansioBlueprint,src/flask/blueprints.py,18
  src/flask/json/provider::DefaultJSONProvider,extends,JSONProvider,src/flask/json/provider.py,124
  src/flask/json/tag::TagDict,extends,JSONTag,src/flask/json/tag.py,93
  src/flask/json/tag::PassDict,extends,JSONTag,src/flask/json/tag.py,119
  src/flask/json/tag::TagTuple,extends,JSONTag,src/flask/json/tag.py,133
  src/flask/json/tag::PassList,extends,JSONTag,src/flask/json/tag.py,147
  src/flask/json/tag::TagBytes,extends,JSONTag,src/flask/json/tag.py,159
  src/flask/json/tag::TagMarkup,extends,JSONTag,src/flask/json/tag.py,173
  src/flask/json/tag::TagUUID,extends,JSONTag,src/flask/json/tag.py,191
  src/flask/json/tag::TagDateTime,extends,JSONTag,src/flask/json/tag.py,205
  src/flask/cli::NoAppException,extends,click.UsageError,src/flask/cli.py,37
  src/flask/cli::AppGroup,extends,click.Group,src/flask/cli.py,405
  src/flask/cli::FlaskGroup,extends,AppGroup,src/flask/cli.py,531
  src/flask/cli::CertParamType,extends,click.ParamType,src/flask/cli.py,780
  src/flask/cli::SeparatedPathType,extends,click.Path,src/flask/cli.py,867
  src/flask/wrappers::Request,extends,RequestBase,src/flask/wrappers.py,18
  src/flask/wrappers::Response,extends,ResponseBase,src/flask/wrappers.py,222
  src/flask/app::Flask,extends,App,src/flask/app.py,108
  src/flask/debughelpers::UnexpectedUnicodeError,extends,AssertionError,src/flask/debughelpers.py,17
  src/flask/debughelpers::UnexpectedUnicodeError,extends,UnicodeError,src/flask/debughelpers.py,17
  src/flask/debughelpers::DebugFilesKeyError,extends,AssertionError,src/flask/debughelpers.py,23
  src/flask/debughelpers::FormDataRoutingRedirect,extends,AssertionError,src/flask/debughelpers.py,50
  src/flask/debughelpers::newcls,extends,oldcls,src/flask/debughelpers.py,90
  src/flask/testing::EnvironBuilder,extends,werkzeug.test.EnvironBuilder,src/flask/testing.py,27
  src/flask/testing::FlaskClient,extends,Client,src/flask/testing.py,109
  src/flask/testing::FlaskCliRunner,extends,CliRunner,src/flask/testing.py,265
  src/flask/views::MethodView,extends,View,src/flask/views.py,138

dependencies[8]{name,version,category}:
  blinker,>=1.9.0,runtime
  click,>=8.1.3,runtime
  itsdangerous,>=2.2.0,runtime
  jinja2,>=3.1.2,runtime
  markupsafe,>=2.1.1,runtime
  werkzeug,>=3.1.0,runtime
  asgiref,>=3.2,runtime
  python-dotenv,*,runtime
```
