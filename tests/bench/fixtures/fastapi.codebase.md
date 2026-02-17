## Live Codebase Map

The following is a **real-time structural map** of this codebase. It was
regenerated moments ago and reflects the current state of all files on disk.

All file paths and line numbers are accurate right now. When you edit a file,
this map updates before your next turn.

Use this map to navigate directly to the right files and line numbers without
searching. Trust these locations — they are current.

```toon
codebase:
  name: fastapi
  languages[2]: javascript,python
  last_indexed: 2026-02-16T21:45:10Z

modules[6]{name,path,key_types,depends_on}:
  __root__,.,,
  docs,docs,Termynal,
  docs_src,docs_src,"Author|BaseItem|BaseUser|CarItem|CommonHeaders|CommonQueryParams|ConnectionManager|Cookies|CustomORJSONResponse|FilterParams|FixedContentQueryChecker|FormData|GzipRequest|GzipRoute|HTTPBearer403|Hero|HeroBase|HeroCreate|HeroPublic|HeroUpdate|Image|InternalError|Invoice|InvoiceEvent|InvoiceEventReceived|Item|ItemV2|Message|ModelName|MySuperContextManager|Offer|OwnerError|Person|PlaneItem|Query|ResponseMessage|Settings|Subscription|Tags|TimedRoute|Token|TokenData|UnicornException|User|UserBase|UserIn|UserInDB|UserOut|ValidationErrorLoggingRoute",fastapi
  fastapi,fastapi,"APIKey|APIKeyBase|APIKeyCookie|APIKeyHeader|APIKeyIn|APIKeyQuery|APIRoute|APIRouter|APIWebSocketRoute|AsyncExitStackMiddleware|BackgroundTasks|BaseModelWithConfig|Body|Components|Contact|Cookie|DefaultPlaceholder|Dependant|DependencyScopeError|Depends|Discriminator|EmailStr|Encoding|EndpointContext|Example|ExternalDocumentation|FastAPI|FastAPIDeprecationWarning|FastAPIError|File|Form|HTTPAuthorizationCredentials|HTTPBase|HTTPBasic|HTTPBasicCredentials|HTTPBearer|HTTPDigest|HTTPException|Header|Info|License|Link|MediaType|ModelField|OAuth2|OAuth2AuthorizationCodeBearer|OAuth2PasswordBearer|OAuth2PasswordRequestForm|OAuth2PasswordRequestFormStrict|OAuthFlow|OAuthFlowAuthorizationCode|OAuthFlowClientCredentials|OAuthFlowImplicit|OAuthFlowPassword|OAuthFlows|ORJSONResponse|OpenAPI|OpenIdConnect|Operation|Param|ParamDetails|ParamTypes|Parameter|ParameterBase|ParameterInType|Path|PathItem|PydanticV1NotSupportedError|Query|Reference|RequestBody|RequestValidationError|Response|ResponseValidationError|Schema|Security|SecurityBase|SecuritySchemeType|SecurityScopes|Server|ServerVariable|SolvedDependency|Tag|UJSONResponse|UploadFile|ValidationException|WebSocketException|WebSocketRequestValidationError|XML|_AsyncLiftContextManager|_DefaultLifespan",
  scripts,scripts,"AddCommentData|AddCommentResponse|AddDiscussionComment|AllDiscussionsData|AllDiscussionsDiscussionLabels|AllDiscussionsDiscussionNode|AllDiscussionsDiscussions|AllDiscussionsLabelNode|AllDiscussionsLabelsEdge|AllDiscussionsRepository|AllDiscussionsResponse|Author|CodeIncludeInfo|Comment|Comments|CommentsData|CommentsDiscussion|CommentsEdge|CommentsNode|CommentsRepository|CommentsResponse|ContributorsResults|DiscussionExpertsResults|Discussions|DiscussionsComments|DiscussionsCommentsNode|DiscussionsEdge|DiscussionsNode|DiscussionsRepository|DiscussionsResponse|DiscussionsResponseData|EnFile|HTMLLinkAttribute|HeaderPermalinkInfo|HtmlLinkInfo|LabelNode|LabelSettings|Labels|LinkData|MarkdownLinkInfo|MultilineCodeBlockInfo|PRsRepository|PRsResponse|PRsResponseData|PartialGitHubEvent|PartialGitHubEventIssue|PullRequestEdge|PullRequestNode|PullRequests|Replies|Repo|ReviewNode|Reviews|Settings|SponsorEntity|SponsorsResponse|SponsorsResponseData|SponsorsUser|SponsorshipAsMaintainer|SponsorshipAsMaintainerEdge|SponsorshipAsMaintainerNode|Tier|UpdateCommentData|UpdateCommentResponse|UpdateDiscussionComment|VisibleTextExtractor",
  tests,tests,"A|APIRouteA|APIRouteB|APIRouteC|Address|AsyncCallableDependency|AsyncCallableGenDependency|AsyncDependencyError|B|BaseUser|BodyModelOptionalAlias|BodyModelOptionalAliasAndValidationAlias|BodyModelOptionalListAlias|BodyModelOptionalListAliasAndValidationAlias|BodyModelOptionalListStr|BodyModelOptionalListValidationAlias|BodyModelOptionalStr|BodyModelOptionalValidationAlias|BodyModelRequiredAlias|BodyModelRequiredAliasAndValidationAlias|BodyModelRequiredListAlias|BodyModelRequiredListAliasAndValidationAlias|BodyModelRequiredListStr|BodyModelRequiredListValidationAlias|BodyModelRequiredStr|BodyModelRequiredValidationAlias|CallableDependency|CallableGenDependency|Cat|ClassDep|ClassInstanceAsyncDep|ClassInstanceAsyncGenDep|ClassInstanceAsyncWrappedAsyncDep|ClassInstanceAsyncWrappedDep|ClassInstanceAsyncWrappedGenAsyncDep|ClassInstanceAsyncWrappedGenDep|ClassInstanceDep|ClassInstanceGenDep|ClassInstanceWrappedAsyncDep|ClassInstanceWrappedAsyncGenDep|ClassInstanceWrappedDep|ClassInstanceWrappedGenDep|CompanyForm|ContentSizeLimitMiddleware|CookieModelOptionalAlias|CookieModelOptionalAliasAndValidationAlias|CookieModelOptionalStr|CookieModelOptionalValidationAlias|CookieModelRequiredAlias|CookieModelRequiredAliasAndValidationAlias|CookieModelRequiredStr|CookieModelRequiredValidationAlias|Coordinate|CustomError|CustomModel|DBUser|Dep|DictablePerson|DictablePet|Dog|DummyClient|DummyUser|EmbeddedModel|Error|ErrorModelV1|Event|ExceptionCapture|ExtendedItem|Facility|FakeNumpyArray|FirstItem|Foo|FooBaseModel|FormModel|FormModelExtraAllow|FormModelOptionalAlias|FormModelOptionalAliasAndValidationAlias|FormModelOptionalListAlias|FormModelOptionalListAliasAndValidationAlias|FormModelOptionalListStr|FormModelOptionalListValidationAlias|FormModelOptionalStr|FormModelOptionalValidationAlias|FormModelRequiredAlias|FormModelRequiredAliasAndValidationAlias|FormModelRequiredListAlias|FormModelRequiredListAliasAndValidationAlias|FormModelRequiredListStr|FormModelRequiredListValidationAlias|FormModelRequiredStr|FormModelRequiredValidationAlias|ForwardRefModel|HeaderModelOptionalAlias|HeaderModelOptionalAliasAndValidationAlias|HeaderModelOptionalListAlias|HeaderModelOptionalListAliasAndValidationAlias|HeaderModelOptionalListStr|HeaderModelOptionalListValidationAlias|HeaderModelOptionalStr|HeaderModelOptionalValidationAlias|HeaderModelRequiredAlias|HeaderModelRequiredAliasAndValidationAlias|HeaderModelRequiredListAlias|HeaderModelRequiredListAliasAndValidationAlias|HeaderModelRequiredListStr|HeaderModelRequiredListValidationAlias|HeaderModelRequiredStr|HeaderModelRequiredValidationAlias|Invoice|InvoiceEvent|InvoiceEventReceived|Item|ItemGroup|ItemIn|ItemOut|Items|JsonApiError|JsonApiResponse|LargeIn|LargeOut|Message|MessageEvent|MessageEventType|MessageOutput|MethodsDependency|Missing|Model|Model1|Model2|Model3|ModelA|ModelB|ModelC|ModelDefaults|ModelNoAlias|ModelSubclass|ModelV1|ModelV1A|ModelWithAlias|ModelWithConfig|ModelWithCustomEncoder|ModelWithCustomEncoderSubclass|ModelWithDatetimeField|ModelWithDefault|ModelWithPath|ModelWithRef|MyDict|MyEnum|MyModel|MyUuid|NamedSession|NonPydanticModel|ORJSONResponse|OtherDependencyError|OtherItem|OtherRole|OverrideResponse|ParamModelV1|Person|PersonBase|PersonCreate|PersonRead|Pet|PetDB|PetOut|PlatformRole|Product|QueryModelOptionalAlias|QueryModelOptionalAliasAndValidationAlias|QueryModelOptionalListAlias|QueryModelOptionalListAliasAndValidationAlias|QueryModelOptionalListStr|QueryModelOptionalListValidationAlias|QueryModelOptionalStr|QueryModelOptionalValidationAlias|QueryModelRequiredAlias|QueryModelRequiredAliasAndValidationAlias|QueryModelRequiredListAlias|QueryModelRequiredListAliasAndValidationAlias|QueryModelRequiredListStr|QueryModelRequiredListValidationAlias|QueryModelRequiredStr|QueryModelRequiredValidationAlias|Rectangle|RecursiveItem|RecursiveItemViaSubmodel|RecursiveSubitemInSubmodel|ResponseLevel0|ResponseLevel1|ResponseLevel2|ResponseLevel3|ResponseLevel4|ResponseLevel5|ResponseModel|ResponseModelV1|ReturnModelV1|RoleEnum|Session|Shop|SomeCustomClass|State|SubItem|SubModel|Subscription|SyncDependencyError|Unserializable|User|UserBase|UserCreate|UserDB|UserForm|WithComputedField|safe_datetime","docs|fastapi"

symbols[500]{fqn,kind,file,line,signature}:
  docs/en/docs/js/termynal::Termynal,class,docs/en/docs/js/termynal.js,14,class Termynal {
  docs_src/settings/app01_py39/config::Settings,class,docs_src/settings/app01_py39/config.py,4,class Settings(BaseSettings):
  docs_src/settings/tutorial001_py310::Settings,class,docs_src/settings/tutorial001_py310.py,5,class Settings(BaseSettings):
  docs_src/settings/app02_py310/config::Settings,class,docs_src/settings/app02_py310/config.py,4,class Settings(BaseSettings):
  docs_src/settings/app03_py39/config::Settings,class,docs_src/settings/app03_py39/config.py,4,class Settings(BaseSettings):
  docs_src/settings/app02_an_py39/config::Settings,class,docs_src/settings/app02_an_py39/config.py,4,class Settings(BaseSettings):
  docs_src/settings/app03_an_py39/config::Settings,class,docs_src/settings/app03_an_py39/config.py,4,class Settings(BaseSettings):
  docs_src/settings/app02_py39/config::Settings,class,docs_src/settings/app02_py39/config.py,4,class Settings(BaseSettings):
  docs_src/settings/app01_py310/config::Settings,class,docs_src/settings/app01_py310/config.py,4,class Settings(BaseSettings):
  docs_src/settings/app02_an_py310/config::Settings,class,docs_src/settings/app02_an_py310/config.py,4,class Settings(BaseSettings):
  docs_src/settings/app03_an_py310/config::Settings,class,docs_src/settings/app03_an_py310/config.py,4,class Settings(BaseSettings):
  docs_src/settings/tutorial001_py39::Settings,class,docs_src/settings/tutorial001_py39.py,5,class Settings(BaseSettings):
  docs_src/settings/app03_py310/config::Settings,class,docs_src/settings/app03_py310/config.py,4,class Settings(BaseSettings):
  docs_src/conditional_openapi/tutorial001_py310::Settings,class,docs_src/conditional_openapi/tutorial001_py310.py,5,class Settings(BaseSettings):
  docs_src/conditional_openapi/tutorial001_py39::Settings,class,docs_src/conditional_openapi/tutorial001_py39.py,5,class Settings(BaseSettings):
  docs_src/authentication_error_status_code/tutorial001_an_py39::HTTPBearer403,class,docs_src/authentication_error_status_code/tutorial001_an_py39.py,9,class HTTPBearer403(HTTPBearer):
  docs_src/authentication_error_status_code/tutorial001_an_py310::HTTPBearer403,class,docs_src/authentication_error_status_code/tutorial001_an_py310.py,9,class HTTPBearer403(HTTPBearer):
  docs_src/body_multiple_params/tutorial004_an_py310::Item,class,docs_src/body_multiple_params/tutorial004_an_py310.py,9,class Item(BaseModel):
  docs_src/body_multiple_params/tutorial004_an_py310::User,class,docs_src/body_multiple_params/tutorial004_an_py310.py,16,class User(BaseModel):
  docs_src/body_multiple_params/tutorial001_py310::Item,class,docs_src/body_multiple_params/tutorial001_py310.py,7,class Item(BaseModel):
  docs_src/body_multiple_params/tutorial001_an_py310::Item,class,docs_src/body_multiple_params/tutorial001_an_py310.py,9,class Item(BaseModel):
  docs_src/body_multiple_params/tutorial005_py310::Item,class,docs_src/body_multiple_params/tutorial005_py310.py,7,class Item(BaseModel):
  docs_src/body_multiple_params/tutorial004_py310::Item,class,docs_src/body_multiple_params/tutorial004_py310.py,7,class Item(BaseModel):
  docs_src/body_multiple_params/tutorial004_py310::User,class,docs_src/body_multiple_params/tutorial004_py310.py,14,class User(BaseModel):
  docs_src/body_multiple_params/tutorial003_an_py310::Item,class,docs_src/body_multiple_params/tutorial003_an_py310.py,9,class Item(BaseModel):
  docs_src/body_multiple_params/tutorial003_an_py310::User,class,docs_src/body_multiple_params/tutorial003_an_py310.py,16,class User(BaseModel):
  docs_src/body_multiple_params/tutorial002_py310::Item,class,docs_src/body_multiple_params/tutorial002_py310.py,7,class Item(BaseModel):
  docs_src/body_multiple_params/tutorial002_py310::User,class,docs_src/body_multiple_params/tutorial002_py310.py,14,class User(BaseModel):
  docs_src/body_multiple_params/tutorial003_py310::Item,class,docs_src/body_multiple_params/tutorial003_py310.py,7,class Item(BaseModel):
  docs_src/body_multiple_params/tutorial003_py310::User,class,docs_src/body_multiple_params/tutorial003_py310.py,14,class User(BaseModel):
  docs_src/body_multiple_params/tutorial005_an_py310::Item,class,docs_src/body_multiple_params/tutorial005_an_py310.py,9,class Item(BaseModel):
  docs_src/body_nested_models/tutorial006_py310::Image,class,docs_src/body_nested_models/tutorial006_py310.py,7,class Image(BaseModel):
  docs_src/body_nested_models/tutorial006_py310::Item,class,docs_src/body_nested_models/tutorial006_py310.py,12,class Item(BaseModel):
  docs_src/body_nested_models/tutorial007_py310::Image,class,docs_src/body_nested_models/tutorial007_py310.py,7,class Image(BaseModel):
  docs_src/body_nested_models/tutorial007_py310::Item,class,docs_src/body_nested_models/tutorial007_py310.py,12,class Item(BaseModel):
  docs_src/body_nested_models/tutorial007_py310::Offer,class,docs_src/body_nested_models/tutorial007_py310.py,21,class Offer(BaseModel):
  docs_src/body_nested_models/tutorial001_py310::Item,class,docs_src/body_nested_models/tutorial001_py310.py,7,class Item(BaseModel):
  docs_src/body_nested_models/tutorial005_py310::Image,class,docs_src/body_nested_models/tutorial005_py310.py,7,class Image(BaseModel):
  docs_src/body_nested_models/tutorial005_py310::Item,class,docs_src/body_nested_models/tutorial005_py310.py,12,class Item(BaseModel):
  docs_src/body_nested_models/tutorial004_py310::Image,class,docs_src/body_nested_models/tutorial004_py310.py,7,class Image(BaseModel):
  docs_src/body_nested_models/tutorial004_py310::Item,class,docs_src/body_nested_models/tutorial004_py310.py,12,class Item(BaseModel):
  docs_src/body_nested_models/tutorial002_py310::Item,class,docs_src/body_nested_models/tutorial002_py310.py,7,class Item(BaseModel):
  docs_src/body_nested_models/tutorial003_py310::Item,class,docs_src/body_nested_models/tutorial003_py310.py,7,class Item(BaseModel):
  docs_src/body_nested_models/tutorial008_py39::Image,class,docs_src/body_nested_models/tutorial008_py39.py,7,class Image(BaseModel):
  docs_src/body_nested_models/tutorial008_py310::Image,class,docs_src/body_nested_models/tutorial008_py310.py,7,class Image(BaseModel):
  docs_src/openapi_callbacks/tutorial001_py310::Invoice,class,docs_src/openapi_callbacks/tutorial001_py310.py,7,class Invoice(BaseModel):
  docs_src/openapi_callbacks/tutorial001_py310::InvoiceEvent,class,docs_src/openapi_callbacks/tutorial001_py310.py,14,class InvoiceEvent(BaseModel):
  docs_src/openapi_callbacks/tutorial001_py310::InvoiceEventReceived,class,docs_src/openapi_callbacks/tutorial001_py310.py,19,class InvoiceEventReceived(BaseModel):
  docs_src/response_model/tutorial006_py310::Item,class,docs_src/response_model/tutorial006_py310.py,7,class Item(BaseModel):
  docs_src/response_model/tutorial001_py310::Item,class,docs_src/response_model/tutorial001_py310.py,9,class Item(BaseModel):
  docs_src/response_model/tutorial001_01_py310::Item,class,docs_src/response_model/tutorial001_01_py310.py,7,class Item(BaseModel):
  docs_src/response_model/tutorial005_py310::Item,class,docs_src/response_model/tutorial005_py310.py,7,class Item(BaseModel):
  docs_src/response_model/tutorial004_py310::Item,class,docs_src/response_model/tutorial004_py310.py,7,class Item(BaseModel):
  docs_src/response_model/tutorial003_01_py310::BaseUser,class,docs_src/response_model/tutorial003_01_py310.py,7,class BaseUser(BaseModel):
  docs_src/response_model/tutorial003_01_py310::UserIn,class,docs_src/response_model/tutorial003_01_py310.py,13,class UserIn(BaseUser):
  docs_src/response_model/tutorial002_py310::UserIn,class,docs_src/response_model/tutorial002_py310.py,7,class UserIn(BaseModel):
  docs_src/response_model/tutorial003_py310::UserIn,class,docs_src/response_model/tutorial003_py310.py,9,class UserIn(BaseModel):
  docs_src/response_model/tutorial003_py310::UserOut,class,docs_src/response_model/tutorial003_py310.py,16,class UserOut(BaseModel):
  docs_src/python_types/tutorial011_py310::User,class,docs_src/python_types/tutorial011_py310.py,6,class User(BaseModel):
  docs_src/python_types/tutorial010_py310::Person,class,docs_src/python_types/tutorial010_py310.py,1,class Person:
  docs_src/python_types/tutorial010_py39::Person,class,docs_src/python_types/tutorial010_py39.py,1,class Person:
  docs_src/cookie_param_models/tutorial002_an_py310::Cookies,class,docs_src/cookie_param_models/tutorial002_an_py310.py,9,class Cookies(BaseModel):
  docs_src/cookie_param_models/tutorial001_py310::Cookies,class,docs_src/cookie_param_models/tutorial001_py310.py,7,class Cookies(BaseModel):
  docs_src/cookie_param_models/tutorial001_an_py310::Cookies,class,docs_src/cookie_param_models/tutorial001_an_py310.py,9,class Cookies(BaseModel):
  docs_src/cookie_param_models/tutorial002_py310::Cookies,class,docs_src/cookie_param_models/tutorial002_py310.py,7,class Cookies(BaseModel):
  docs_src/security/tutorial002_an_py310::User,class,docs_src/security/tutorial002_an_py310.py,12,class User(BaseModel):
  docs_src/security/tutorial004_an_py310::Token,class,docs_src/security/tutorial004_an_py310.py,29,class Token(BaseModel):
  docs_src/security/tutorial004_an_py310::TokenData,class,docs_src/security/tutorial004_an_py310.py,34,class TokenData(BaseModel):
  docs_src/security/tutorial004_an_py310::User,class,docs_src/security/tutorial004_an_py310.py,38,class User(BaseModel):
  docs_src/security/tutorial004_an_py310::UserInDB,class,docs_src/security/tutorial004_an_py310.py,45,class UserInDB(User):
  docs_src/security/tutorial005_py310::Token,class,docs_src/security/tutorial005_py310.py,39,class Token(BaseModel):
  docs_src/security/tutorial005_py310::TokenData,class,docs_src/security/tutorial005_py310.py,44,class TokenData(BaseModel):
  docs_src/security/tutorial005_py310::User,class,docs_src/security/tutorial005_py310.py,49,class User(BaseModel):
  docs_src/security/tutorial005_py310::UserInDB,class,docs_src/security/tutorial005_py310.py,56,class UserInDB(User):
  docs_src/security/tutorial004_py310::Token,class,docs_src/security/tutorial004_py310.py,28,class Token(BaseModel):
  docs_src/security/tutorial004_py310::TokenData,class,docs_src/security/tutorial004_py310.py,33,class TokenData(BaseModel):
  docs_src/security/tutorial004_py310::User,class,docs_src/security/tutorial004_py310.py,37,class User(BaseModel):
  docs_src/security/tutorial004_py310::UserInDB,class,docs_src/security/tutorial004_py310.py,44,class UserInDB(User):
  docs_src/security/tutorial003_an_py310::User,class,docs_src/security/tutorial003_an_py310.py,34,class User(BaseModel):
  docs_src/security/tutorial003_an_py310::UserInDB,class,docs_src/security/tutorial003_an_py310.py,41,class UserInDB(User):
  docs_src/security/tutorial002_py310::User,class,docs_src/security/tutorial002_py310.py,10,class User(BaseModel):
  docs_src/security/tutorial003_py310::User,class,docs_src/security/tutorial003_py310.py,32,class User(BaseModel):
  docs_src/security/tutorial003_py310::UserInDB,class,docs_src/security/tutorial003_py310.py,39,class UserInDB(User):
  docs_src/security/tutorial005_an_py310::Token,class,docs_src/security/tutorial005_an_py310.py,40,class Token(BaseModel):
  docs_src/security/tutorial005_an_py310::TokenData,class,docs_src/security/tutorial005_an_py310.py,45,class TokenData(BaseModel):
  docs_src/security/tutorial005_an_py310::User,class,docs_src/security/tutorial005_an_py310.py,50,class User(BaseModel):
  docs_src/security/tutorial005_an_py310::UserInDB,class,docs_src/security/tutorial005_an_py310.py,57,class UserInDB(User):
  docs_src/sql_databases/tutorial002_an_py310::HeroBase,class,docs_src/sql_databases/tutorial002_an_py310.py,7,class HeroBase(SQLModel):
  docs_src/sql_databases/tutorial002_an_py310::Hero,class,docs_src/sql_databases/tutorial002_an_py310.py,12,"class Hero(HeroBase, table=True):"
  docs_src/sql_databases/tutorial002_an_py310::HeroPublic,class,docs_src/sql_databases/tutorial002_an_py310.py,17,class HeroPublic(HeroBase):
  docs_src/sql_databases/tutorial002_an_py310::HeroCreate,class,docs_src/sql_databases/tutorial002_an_py310.py,21,class HeroCreate(HeroBase):
  docs_src/sql_databases/tutorial002_an_py310::HeroUpdate,class,docs_src/sql_databases/tutorial002_an_py310.py,25,class HeroUpdate(HeroBase):
  docs_src/sql_databases/tutorial001_py310::Hero,class,docs_src/sql_databases/tutorial001_py310.py,5,"class Hero(SQLModel, table=True):"
  docs_src/sql_databases/tutorial001_an_py310::Hero,class,docs_src/sql_databases/tutorial001_an_py310.py,7,"class Hero(SQLModel, table=True):"
  docs_src/sql_databases/tutorial002_py310::HeroBase,class,docs_src/sql_databases/tutorial002_py310.py,5,class HeroBase(SQLModel):
  docs_src/sql_databases/tutorial002_py310::Hero,class,docs_src/sql_databases/tutorial002_py310.py,10,"class Hero(HeroBase, table=True):"
  docs_src/sql_databases/tutorial002_py310::HeroPublic,class,docs_src/sql_databases/tutorial002_py310.py,15,class HeroPublic(HeroBase):
  docs_src/sql_databases/tutorial002_py310::HeroCreate,class,docs_src/sql_databases/tutorial002_py310.py,19,class HeroCreate(HeroBase):
  docs_src/sql_databases/tutorial002_py310::HeroUpdate,class,docs_src/sql_databases/tutorial002_py310.py,23,class HeroUpdate(HeroBase):
  docs_src/query_param_models/tutorial002_an_py310::FilterParams,class,docs_src/query_param_models/tutorial002_an_py310.py,9,class FilterParams(BaseModel):
  docs_src/query_param_models/tutorial001_py310::FilterParams,class,docs_src/query_param_models/tutorial001_py310.py,9,class FilterParams(BaseModel):
  docs_src/query_param_models/tutorial001_an_py310::FilterParams,class,docs_src/query_param_models/tutorial001_an_py310.py,9,class FilterParams(BaseModel):
  docs_src/query_param_models/tutorial002_py310::FilterParams,class,docs_src/query_param_models/tutorial002_py310.py,9,class FilterParams(BaseModel):
  docs_src/encoder/tutorial001_py310::Item,class,docs_src/encoder/tutorial001_py310.py,10,class Item(BaseModel):
  docs_src/body_updates/tutorial001_py310::Item,class,docs_src/body_updates/tutorial001_py310.py,8,class Item(BaseModel):
  docs_src/body_updates/tutorial002_py310::Item,class,docs_src/body_updates/tutorial002_py310.py,8,class Item(BaseModel):
  docs_src/body/tutorial001_py310::Item,class,docs_src/body/tutorial001_py310.py,5,class Item(BaseModel):
  docs_src/body/tutorial004_py310::Item,class,docs_src/body/tutorial004_py310.py,5,class Item(BaseModel):
  docs_src/body/tutorial002_py310::Item,class,docs_src/body/tutorial002_py310.py,5,class Item(BaseModel):
  docs_src/body/tutorial003_py310::Item,class,docs_src/body/tutorial003_py310.py,5,class Item(BaseModel):
  docs_src/path_operation_advanced_configuration/tutorial007_py310::Item,class,docs_src/path_operation_advanced_configuration/tutorial007_py310.py,8,class Item(BaseModel):
  docs_src/path_operation_advanced_configuration/tutorial007_py39::Item,class,docs_src/path_operation_advanced_configuration/tutorial007_py39.py,8,class Item(BaseModel):
  docs_src/path_operation_advanced_configuration/tutorial004_py310::Item,class,docs_src/path_operation_advanced_configuration/tutorial004_py310.py,7,class Item(BaseModel):
  docs_src/generate_clients/tutorial001_py310::Item,class,docs_src/generate_clients/tutorial001_py310.py,7,class Item(BaseModel):
  docs_src/generate_clients/tutorial001_py310::ResponseMessage,class,docs_src/generate_clients/tutorial001_py310.py,12,class ResponseMessage(BaseModel):
  docs_src/generate_clients/tutorial002_py39::Item,class,docs_src/generate_clients/tutorial002_py39.py,7,class Item(BaseModel):
  docs_src/generate_clients/tutorial002_py39::ResponseMessage,class,docs_src/generate_clients/tutorial002_py39.py,12,class ResponseMessage(BaseModel):
  docs_src/generate_clients/tutorial002_py39::User,class,docs_src/generate_clients/tutorial002_py39.py,16,class User(BaseModel):
  docs_src/generate_clients/tutorial003_py39::Item,class,docs_src/generate_clients/tutorial003_py39.py,13,class Item(BaseModel):
  docs_src/generate_clients/tutorial003_py39::ResponseMessage,class,docs_src/generate_clients/tutorial003_py39.py,18,class ResponseMessage(BaseModel):
  docs_src/generate_clients/tutorial003_py39::User,class,docs_src/generate_clients/tutorial003_py39.py,22,class User(BaseModel):
  docs_src/generate_clients/tutorial002_py310::Item,class,docs_src/generate_clients/tutorial002_py310.py,7,class Item(BaseModel):
  docs_src/generate_clients/tutorial002_py310::ResponseMessage,class,docs_src/generate_clients/tutorial002_py310.py,12,class ResponseMessage(BaseModel):
  docs_src/generate_clients/tutorial002_py310::User,class,docs_src/generate_clients/tutorial002_py310.py,16,class User(BaseModel):
  docs_src/generate_clients/tutorial003_py310::Item,class,docs_src/generate_clients/tutorial003_py310.py,13,class Item(BaseModel):
  docs_src/generate_clients/tutorial003_py310::ResponseMessage,class,docs_src/generate_clients/tutorial003_py310.py,18,class ResponseMessage(BaseModel):
  docs_src/generate_clients/tutorial003_py310::User,class,docs_src/generate_clients/tutorial003_py310.py,22,class User(BaseModel):
  docs_src/generate_clients/tutorial001_py39::Item,class,docs_src/generate_clients/tutorial001_py39.py,7,class Item(BaseModel):
  docs_src/generate_clients/tutorial001_py39::ResponseMessage,class,docs_src/generate_clients/tutorial001_py39.py,12,class ResponseMessage(BaseModel):
  docs_src/path_params/tutorial005_py39::ModelName,class,docs_src/path_params/tutorial005_py39.py,6,"class ModelName(str, Enum):"
  docs_src/path_params/tutorial005_py310::ModelName,class,docs_src/path_params/tutorial005_py310.py,6,"class ModelName(str, Enum):"
  docs_src/dependencies/tutorial008c_an_py39::InternalError,class,docs_src/dependencies/tutorial008c_an_py39.py,8,class InternalError(Exception):
  docs_src/dependencies/tutorial002_an_py310::CommonQueryParams,class,docs_src/dependencies/tutorial002_an_py310.py,11,class CommonQueryParams:
  docs_src/dependencies/tutorial008d_py310::InternalError,class,docs_src/dependencies/tutorial008d_py310.py,6,class InternalError(Exception):
  docs_src/dependencies/tutorial011_py310::FixedContentQueryChecker,class,docs_src/dependencies/tutorial011_py310.py,6,class FixedContentQueryChecker:
  docs_src/dependencies/tutorial010_py310::MySuperContextManager,class,docs_src/dependencies/tutorial010_py310.py,1,class MySuperContextManager:
  docs_src/dependencies/tutorial008b_py310::OwnerError,class,docs_src/dependencies/tutorial008b_py310.py,12,class OwnerError(Exception):
  docs_src/dependencies/tutorial008c_py310::InternalError,class,docs_src/dependencies/tutorial008c_py310.py,6,class InternalError(Exception):
  docs_src/dependencies/tutorial008c_an_py310::InternalError,class,docs_src/dependencies/tutorial008c_an_py310.py,8,class InternalError(Exception):
  docs_src/dependencies/tutorial004_an_py310::CommonQueryParams,class,docs_src/dependencies/tutorial004_an_py310.py,11,class CommonQueryParams:
  docs_src/dependencies/tutorial008c_py39::InternalError,class,docs_src/dependencies/tutorial008c_py39.py,6,class InternalError(Exception):
  docs_src/dependencies/tutorial011_an_py310::FixedContentQueryChecker,class,docs_src/dependencies/tutorial011_an_py310.py,8,class FixedContentQueryChecker:
  docs_src/dependencies/tutorial008b_py39::OwnerError,class,docs_src/dependencies/tutorial008b_py39.py,12,class OwnerError(Exception):
  docs_src/dependencies/tutorial014_an_py310::User,class,docs_src/dependencies/tutorial014_an_py310.py,11,"class User(SQLModel, table=True):"
  docs_src/dependencies/tutorial008d_an_py39::InternalError,class,docs_src/dependencies/tutorial008d_an_py39.py,8,class InternalError(Exception):
  docs_src/dependencies/tutorial013_an_py310::User,class,docs_src/dependencies/tutorial013_an_py310.py,11,"class User(SQLModel, table=True):"
  docs_src/dependencies/tutorial011_an_py39::FixedContentQueryChecker,class,docs_src/dependencies/tutorial011_an_py39.py,8,class FixedContentQueryChecker:
  docs_src/dependencies/tutorial008b_an_py39::OwnerError,class,docs_src/dependencies/tutorial008b_an_py39.py,14,class OwnerError(Exception):
  docs_src/dependencies/tutorial004_py310::CommonQueryParams,class,docs_src/dependencies/tutorial004_py310.py,9,class CommonQueryParams:
  docs_src/dependencies/tutorial008d_an_py310::InternalError,class,docs_src/dependencies/tutorial008d_an_py310.py,8,class InternalError(Exception):
  docs_src/dependencies/tutorial003_an_py310::CommonQueryParams,class,docs_src/dependencies/tutorial003_an_py310.py,11,class CommonQueryParams:
  docs_src/dependencies/tutorial002_py310::CommonQueryParams,class,docs_src/dependencies/tutorial002_py310.py,9,class CommonQueryParams:
  docs_src/dependencies/tutorial003_py310::CommonQueryParams,class,docs_src/dependencies/tutorial003_py310.py,9,class CommonQueryParams:
  docs_src/dependencies/tutorial008d_py39::InternalError,class,docs_src/dependencies/tutorial008d_py39.py,6,class InternalError(Exception):
  docs_src/dependencies/tutorial011_py39::FixedContentQueryChecker,class,docs_src/dependencies/tutorial011_py39.py,6,class FixedContentQueryChecker:
  docs_src/dependencies/tutorial010_py39::MySuperContextManager,class,docs_src/dependencies/tutorial010_py39.py,1,class MySuperContextManager:
  docs_src/dependencies/tutorial008b_an_py310::OwnerError,class,docs_src/dependencies/tutorial008b_an_py310.py,14,class OwnerError(Exception):
  docs_src/websockets/tutorial003_py39::ConnectionManager,class,docs_src/websockets/tutorial003_py39.py,44,class ConnectionManager:
  docs_src/websockets/tutorial003_py310::ConnectionManager,class,docs_src/websockets/tutorial003_py310.py,44,class ConnectionManager:
  docs_src/graphql_/tutorial001_py310::User,class,docs_src/graphql_/tutorial001_py310.py,7,class User:
  docs_src/graphql_/tutorial001_py310::Query,class,docs_src/graphql_/tutorial001_py310.py,13,class Query:
  docs_src/graphql_/tutorial001_py39::User,class,docs_src/graphql_/tutorial001_py39.py,7,class User:
  docs_src/graphql_/tutorial001_py39::Query,class,docs_src/graphql_/tutorial001_py39.py,13,class Query:
  docs_src/additional_responses/tutorial001_py310::Item,class,docs_src/additional_responses/tutorial001_py310.py,6,class Item(BaseModel):
  docs_src/additional_responses/tutorial001_py310::Message,class,docs_src/additional_responses/tutorial001_py310.py,11,class Message(BaseModel):
  docs_src/additional_responses/tutorial004_py310::Item,class,docs_src/additional_responses/tutorial004_py310.py,6,class Item(BaseModel):
  docs_src/additional_responses/tutorial003_py39::Item,class,docs_src/additional_responses/tutorial003_py39.py,6,class Item(BaseModel):
  docs_src/additional_responses/tutorial003_py39::Message,class,docs_src/additional_responses/tutorial003_py39.py,11,class Message(BaseModel):
  docs_src/additional_responses/tutorial002_py310::Item,class,docs_src/additional_responses/tutorial002_py310.py,6,class Item(BaseModel):
  docs_src/additional_responses/tutorial003_py310::Item,class,docs_src/additional_responses/tutorial003_py310.py,6,class Item(BaseModel):
  docs_src/additional_responses/tutorial003_py310::Message,class,docs_src/additional_responses/tutorial003_py310.py,11,class Message(BaseModel):
  docs_src/additional_responses/tutorial001_py39::Item,class,docs_src/additional_responses/tutorial001_py39.py,6,class Item(BaseModel):
  docs_src/additional_responses/tutorial001_py39::Message,class,docs_src/additional_responses/tutorial001_py39.py,11,class Message(BaseModel):
  docs_src/handling_errors/tutorial005_py39::Item,class,docs_src/handling_errors/tutorial005_py39.py,18,class Item(BaseModel):
  docs_src/handling_errors/tutorial005_py310::Item,class,docs_src/handling_errors/tutorial005_py310.py,18,class Item(BaseModel):
  docs_src/handling_errors/tutorial003_py39::UnicornException,class,docs_src/handling_errors/tutorial003_py39.py,5,class UnicornException(Exception):
  docs_src/handling_errors/tutorial003_py310::UnicornException,class,docs_src/handling_errors/tutorial003_py310.py,5,class UnicornException(Exception):
  docs_src/pydantic_v1_in_v2/tutorial002_an_py310::Item,class,docs_src/pydantic_v1_in_v2/tutorial002_an_py310.py,5,class Item(BaseModel):
  docs_src/pydantic_v1_in_v2/tutorial004_an_py310::Item,class,docs_src/pydantic_v1_in_v2/tutorial004_an_py310.py,8,class Item(BaseModel):
  docs_src/pydantic_v1_in_v2/tutorial001_an_py310::Item,class,docs_src/pydantic_v1_in_v2/tutorial001_an_py310.py,4,class Item(BaseModel):
  docs_src/pydantic_v1_in_v2/tutorial003_an_py310::Item,class,docs_src/pydantic_v1_in_v2/tutorial003_an_py310.py,6,class Item(BaseModel):
  docs_src/pydantic_v1_in_v2/tutorial003_an_py310::ItemV2,class,docs_src/pydantic_v1_in_v2/tutorial003_an_py310.py,12,class ItemV2(BaseModelV2):
  docs_src/dataclasses_/tutorial001_py310::Item,class,docs_src/dataclasses_/tutorial001_py310.py,7,class Item:
  docs_src/dataclasses_/tutorial002_py310::Item,class,docs_src/dataclasses_/tutorial002_py310.py,7,class Item:
  docs_src/dataclasses_/tutorial003_py310::Item,class,docs_src/dataclasses_/tutorial003_py310.py,8,class Item:
  docs_src/dataclasses_/tutorial003_py310::Author,class,docs_src/dataclasses_/tutorial003_py310.py,14,class Author:
  docs_src/header_param_models/tutorial002_an_py310::CommonHeaders,class,docs_src/header_param_models/tutorial002_an_py310.py,9,class CommonHeaders(BaseModel):
  docs_src/header_param_models/tutorial001_py310::CommonHeaders,class,docs_src/header_param_models/tutorial001_py310.py,7,class CommonHeaders(BaseModel):
  docs_src/header_param_models/tutorial001_an_py310::CommonHeaders,class,docs_src/header_param_models/tutorial001_an_py310.py,9,class CommonHeaders(BaseModel):
  docs_src/header_param_models/tutorial003_an_py310::CommonHeaders,class,docs_src/header_param_models/tutorial003_an_py310.py,9,class CommonHeaders(BaseModel):
  docs_src/header_param_models/tutorial002_py310::CommonHeaders,class,docs_src/header_param_models/tutorial002_py310.py,7,class CommonHeaders(BaseModel):
  docs_src/header_param_models/tutorial003_py310::CommonHeaders,class,docs_src/header_param_models/tutorial003_py310.py,7,class CommonHeaders(BaseModel):
  docs_src/path_operation_configuration/tutorial002b_py310::Tags,class,docs_src/path_operation_configuration/tutorial002b_py310.py,8,class Tags(Enum):
  docs_src/path_operation_configuration/tutorial001_py310::Item,class,docs_src/path_operation_configuration/tutorial001_py310.py,7,class Item(BaseModel):
  docs_src/path_operation_configuration/tutorial002b_py39::Tags,class,docs_src/path_operation_configuration/tutorial002b_py39.py,8,class Tags(Enum):
  docs_src/path_operation_configuration/tutorial005_py310::Item,class,docs_src/path_operation_configuration/tutorial005_py310.py,7,class Item(BaseModel):
  docs_src/path_operation_configuration/tutorial004_py310::Item,class,docs_src/path_operation_configuration/tutorial004_py310.py,7,class Item(BaseModel):
  docs_src/path_operation_configuration/tutorial002_py310::Item,class,docs_src/path_operation_configuration/tutorial002_py310.py,7,class Item(BaseModel):
  docs_src/path_operation_configuration/tutorial003_py310::Item,class,docs_src/path_operation_configuration/tutorial003_py310.py,7,class Item(BaseModel):
  docs_src/schema_extra_example/tutorial004_an_py310::Item,class,docs_src/schema_extra_example/tutorial004_an_py310.py,9,class Item(BaseModel):
  docs_src/schema_extra_example/tutorial001_py310::Item,class,docs_src/schema_extra_example/tutorial001_py310.py,7,class Item(BaseModel):
  docs_src/schema_extra_example/tutorial005_py310::Item,class,docs_src/schema_extra_example/tutorial005_py310.py,7,class Item(BaseModel):
  docs_src/schema_extra_example/tutorial004_py310::Item,class,docs_src/schema_extra_example/tutorial004_py310.py,7,class Item(BaseModel):
  docs_src/schema_extra_example/tutorial003_an_py310::Item,class,docs_src/schema_extra_example/tutorial003_an_py310.py,9,class Item(BaseModel):
  docs_src/schema_extra_example/tutorial002_py310::Item,class,docs_src/schema_extra_example/tutorial002_py310.py,7,class Item(BaseModel):
  docs_src/schema_extra_example/tutorial003_py310::Item,class,docs_src/schema_extra_example/tutorial003_py310.py,7,class Item(BaseModel):
  docs_src/schema_extra_example/tutorial005_an_py310::Item,class,docs_src/schema_extra_example/tutorial005_an_py310.py,9,class Item(BaseModel):
  docs_src/openapi_webhooks/tutorial001_py310::Subscription,class,docs_src/openapi_webhooks/tutorial001_py310.py,9,class Subscription(BaseModel):
  docs_src/openapi_webhooks/tutorial001_py39::Subscription,class,docs_src/openapi_webhooks/tutorial001_py39.py,9,class Subscription(BaseModel):
  docs_src/custom_request_and_route/tutorial002_an_py310::ValidationErrorLoggingRoute,class,docs_src/custom_request_and_route/tutorial002_an_py310.py,9,class ValidationErrorLoggingRoute(APIRoute):
  docs_src/custom_request_and_route/tutorial001_py310::GzipRequest,class,docs_src/custom_request_and_route/tutorial001_py310.py,8,class GzipRequest(Request):
  docs_src/custom_request_and_route/tutorial001_py310::GzipRoute,class,docs_src/custom_request_and_route/tutorial001_py310.py,18,class GzipRoute(APIRoute):
  docs_src/custom_request_and_route/tutorial001_an_py310::GzipRequest,class,docs_src/custom_request_and_route/tutorial001_an_py310.py,9,class GzipRequest(Request):
  docs_src/custom_request_and_route/tutorial001_an_py310::GzipRoute,class,docs_src/custom_request_and_route/tutorial001_an_py310.py,19,class GzipRoute(APIRoute):
  docs_src/custom_request_and_route/tutorial002_py310::ValidationErrorLoggingRoute,class,docs_src/custom_request_and_route/tutorial002_py310.py,8,class ValidationErrorLoggingRoute(APIRoute):
  docs_src/custom_request_and_route/tutorial003_py310::TimedRoute,class,docs_src/custom_request_and_route/tutorial003_py310.py,8,class TimedRoute(APIRoute):
  docs_src/extra_models/tutorial004_py39::Item,class,docs_src/extra_models/tutorial004_py39.py,7,class Item(BaseModel):
  docs_src/extra_models/tutorial001_py310::UserIn,class,docs_src/extra_models/tutorial001_py310.py,7,class UserIn(BaseModel):
  docs_src/extra_models/tutorial001_py310::UserOut,class,docs_src/extra_models/tutorial001_py310.py,14,class UserOut(BaseModel):
  docs_src/extra_models/tutorial001_py310::UserInDB,class,docs_src/extra_models/tutorial001_py310.py,20,class UserInDB(BaseModel):
  docs_src/extra_models/tutorial004_py310::Item,class,docs_src/extra_models/tutorial004_py310.py,7,class Item(BaseModel):
  docs_src/extra_models/tutorial002_py310::UserBase,class,docs_src/extra_models/tutorial002_py310.py,7,class UserBase(BaseModel):
  docs_src/extra_models/tutorial002_py310::UserIn,class,docs_src/extra_models/tutorial002_py310.py,13,class UserIn(UserBase):
  docs_src/extra_models/tutorial002_py310::UserOut,class,docs_src/extra_models/tutorial002_py310.py,17,class UserOut(UserBase):
  docs_src/extra_models/tutorial002_py310::UserInDB,class,docs_src/extra_models/tutorial002_py310.py,21,class UserInDB(UserBase):
  docs_src/extra_models/tutorial003_py310::BaseItem,class,docs_src/extra_models/tutorial003_py310.py,9,class BaseItem(BaseModel):
  docs_src/extra_models/tutorial003_py310::CarItem,class,docs_src/extra_models/tutorial003_py310.py,14,class CarItem(BaseItem):
  docs_src/extra_models/tutorial003_py310::PlaneItem,class,docs_src/extra_models/tutorial003_py310.py,18,class PlaneItem(BaseItem):
  docs_src/separate_openapi_schemas/tutorial001_py310::Item,class,docs_src/separate_openapi_schemas/tutorial001_py310.py,5,class Item(BaseModel):
  docs_src/separate_openapi_schemas/tutorial002_py310::Item,class,docs_src/separate_openapi_schemas/tutorial002_py310.py,5,class Item(BaseModel):
  docs_src/app_testing/app_b_py310/main::Item,class,docs_src/app_testing/app_b_py310/main.py,14,class Item(BaseModel):
  docs_src/app_testing/app_b_an_py310/main::Item,class,docs_src/app_testing/app_b_an_py310/main.py,16,class Item(BaseModel):
  docs_src/request_form_models/tutorial002_an_py310::FormData,class,docs_src/request_form_models/tutorial002_an_py310.py,9,class FormData(BaseModel):
  docs_src/request_form_models/tutorial001_an_py39::FormData,class,docs_src/request_form_models/tutorial001_an_py39.py,9,class FormData(BaseModel):
  docs_src/request_form_models/tutorial001_py310::FormData,class,docs_src/request_form_models/tutorial001_py310.py,7,class FormData(BaseModel):
  docs_src/request_form_models/tutorial001_an_py310::FormData,class,docs_src/request_form_models/tutorial001_an_py310.py,9,class FormData(BaseModel):
  docs_src/request_form_models/tutorial002_py39::FormData,class,docs_src/request_form_models/tutorial002_py39.py,7,class FormData(BaseModel):
  docs_src/request_form_models/tutorial002_py310::FormData,class,docs_src/request_form_models/tutorial002_py310.py,7,class FormData(BaseModel):
  docs_src/request_form_models/tutorial002_an_py39::FormData,class,docs_src/request_form_models/tutorial002_an_py39.py,9,class FormData(BaseModel):
  docs_src/request_form_models/tutorial001_py39::FormData,class,docs_src/request_form_models/tutorial001_py39.py,7,class FormData(BaseModel):
  docs_src/body_fields/tutorial001_py310::Item,class,docs_src/body_fields/tutorial001_py310.py,7,class Item(BaseModel):
  docs_src/body_fields/tutorial001_an_py310::Item,class,docs_src/body_fields/tutorial001_an_py310.py,9,class Item(BaseModel):
  docs_src/custom_response/tutorial009c_py310::CustomORJSONResponse,class,docs_src/custom_response/tutorial009c_py310.py,9,class CustomORJSONResponse(Response):
  docs_src/custom_response/tutorial009c_py39::CustomORJSONResponse,class,docs_src/custom_response/tutorial009c_py39.py,9,class CustomORJSONResponse(Response):
  docs_src/response_directly/tutorial001_py310::Item,class,docs_src/response_directly/tutorial001_py310.py,9,class Item(BaseModel):
  fastapi/middleware/asyncexitstack::AsyncExitStackMiddleware,class,fastapi/middleware/asyncexitstack.py,8,class AsyncExitStackMiddleware:
  fastapi/params::ParamTypes,class,fastapi/params.py,20,class ParamTypes(Enum):
  fastapi/params::Param,class,fastapi/params.py,27,class Param(FieldInfo):  # type: ignore[misc]
  fastapi/params::Path,class,fastapi/params.py,138,class Path(Param):  # type: ignore[misc]
  fastapi/params::Query,class,fastapi/params.py,222,class Query(Param):  # type: ignore[misc]
  fastapi/params::Header,class,fastapi/params.py,304,class Header(Param):  # type: ignore[misc]
  fastapi/params::Cookie,class,fastapi/params.py,388,class Cookie(Param):  # type: ignore[misc]
  fastapi/params::Body,class,fastapi/params.py,470,class Body(FieldInfo):  # type: ignore[misc]
  fastapi/params::Form,class,fastapi/params.py,582,class Form(Body):  # type: ignore[misc]
  fastapi/params::File,class,fastapi/params.py,664,class File(Form):  # type: ignore[misc]
  fastapi/params::Depends,class,fastapi/params.py,747,class Depends:
  fastapi/params::Security,class,fastapi/params.py,754,class Security(Depends):
  fastapi/responses::UJSONResponse,class,fastapi/responses.py,23,class UJSONResponse(JSONResponse):
  fastapi/responses::ORJSONResponse,class,fastapi/responses.py,36,class ORJSONResponse(JSONResponse):
  fastapi/security/open_id_connect_url::OpenIdConnect,class,fastapi/security/open_id_connect_url.py,11,class OpenIdConnect(SecurityBase):
  fastapi/security/oauth2::OAuth2PasswordRequestForm,class,fastapi/security/oauth2.py,14,class OAuth2PasswordRequestForm:
  fastapi/security/oauth2::OAuth2PasswordRequestFormStrict,class,fastapi/security/oauth2.py,162,class OAuth2PasswordRequestFormStrict(OAuth2PasswordRequestForm):
  fastapi/security/oauth2::OAuth2,class,fastapi/security/oauth2.py,330,class OAuth2(SecurityBase):
  fastapi/security/oauth2::OAuth2PasswordBearer,class,fastapi/security/oauth2.py,433,class OAuth2PasswordBearer(OAuth2):
  fastapi/security/oauth2::OAuth2AuthorizationCodeBearer,class,fastapi/security/oauth2.py,547,class OAuth2AuthorizationCodeBearer(OAuth2):
  fastapi/security/oauth2::SecurityScopes,class,fastapi/security/oauth2.py,653,class SecurityScopes:
  fastapi/security/api_key::APIKeyBase,class,fastapi/security/api_key.py,11,class APIKeyBase(SecurityBase):
  fastapi/security/api_key::APIKeyQuery,class,fastapi/security/api_key.py,53,class APIKeyQuery(APIKeyBase):
  fastapi/security/api_key::APIKeyHeader,class,fastapi/security/api_key.py,145,class APIKeyHeader(APIKeyBase):
  fastapi/security/api_key::APIKeyCookie,class,fastapi/security/api_key.py,233,class APIKeyCookie(APIKeyBase):
  fastapi/security/http::HTTPBasicCredentials,class,fastapi/security/http.py,16,class HTTPBasicCredentials(BaseModel):
  fastapi/security/http::HTTPAuthorizationCredentials,class,fastapi/security/http.py,29,class HTTPAuthorizationCredentials(BaseModel):
  fastapi/security/http::HTTPBase,class,fastapi/security/http.py,69,class HTTPBase(SecurityBase):
  fastapi/security/http::HTTPBasic,class,fastapi/security/http.py,105,class HTTPBasic(HTTPBase):
  fastapi/security/http::HTTPBearer,class,fastapi/security/http.py,222,class HTTPBearer(HTTPBase):
  fastapi/security/http::HTTPDigest,class,fastapi/security/http.py,319,class HTTPDigest(HTTPBase):
  fastapi/security/base::SecurityBase,class,fastapi/security/base.py,4,class SecurityBase:
  fastapi/applications::FastAPI,class,fastapi/applications.py,45,class FastAPI(Starlette):
  fastapi/background::BackgroundTasks,class,fastapi/background.py,11,class BackgroundTasks(StarletteBackgroundTasks):
  fastapi/dependencies/models::Dependant,class,fastapi/dependencies/models.py,32,class Dependant:
  fastapi/dependencies/utils::ParamDetails,class,fastapi/dependencies/utils.py,354,class ParamDetails:
  fastapi/dependencies/utils::SolvedDependency,class,fastapi/dependencies/utils.py,557,class SolvedDependency:
  fastapi/openapi/models::EmailStr,class,fastapi/openapi/models.py,23,class EmailStr(str):  # type: ignore
  fastapi/openapi/models::BaseModelWithConfig,class,fastapi/openapi/models.py,57,class BaseModelWithConfig(BaseModel):
  fastapi/openapi/models::Contact,class,fastapi/openapi/models.py,61,class Contact(BaseModelWithConfig):
  fastapi/openapi/models::License,class,fastapi/openapi/models.py,67,class License(BaseModelWithConfig):
  fastapi/openapi/models::Info,class,fastapi/openapi/models.py,73,class Info(BaseModelWithConfig):
  fastapi/openapi/models::ServerVariable,class,fastapi/openapi/models.py,83,class ServerVariable(BaseModelWithConfig):
  fastapi/openapi/models::Server,class,fastapi/openapi/models.py,89,class Server(BaseModelWithConfig):
  fastapi/openapi/models::Reference,class,fastapi/openapi/models.py,95,class Reference(BaseModel):
  fastapi/openapi/models::Discriminator,class,fastapi/openapi/models.py,99,class Discriminator(BaseModel):
  fastapi/openapi/models::XML,class,fastapi/openapi/models.py,104,class XML(BaseModelWithConfig):
  fastapi/openapi/models::ExternalDocumentation,class,fastapi/openapi/models.py,112,class ExternalDocumentation(BaseModelWithConfig):
  fastapi/openapi/models::Schema,class,fastapi/openapi/models.py,123,class Schema(BaseModelWithConfig):
  fastapi/openapi/models::Example,class,fastapi/openapi/models.py,212,"class Example(TypedDict, total=False):"
  fastapi/openapi/models::ParameterInType,class,fastapi/openapi/models.py,221,class ParameterInType(Enum):
  fastapi/openapi/models::Encoding,class,fastapi/openapi/models.py,228,class Encoding(BaseModelWithConfig):
  fastapi/openapi/models::MediaType,class,fastapi/openapi/models.py,236,class MediaType(BaseModelWithConfig):
  fastapi/openapi/models::ParameterBase,class,fastapi/openapi/models.py,243,class ParameterBase(BaseModelWithConfig):
  fastapi/openapi/models::Parameter,class,fastapi/openapi/models.py,258,class Parameter(ParameterBase):
  fastapi/openapi/models::Header,class,fastapi/openapi/models.py,263,class Header(ParameterBase):
  fastapi/openapi/models::RequestBody,class,fastapi/openapi/models.py,267,class RequestBody(BaseModelWithConfig):
  fastapi/openapi/models::Link,class,fastapi/openapi/models.py,273,class Link(BaseModelWithConfig):
  fastapi/openapi/models::Response,class,fastapi/openapi/models.py,282,class Response(BaseModelWithConfig):
  fastapi/openapi/models::Operation,class,fastapi/openapi/models.py,289,class Operation(BaseModelWithConfig):
  fastapi/openapi/models::PathItem,class,fastapi/openapi/models.py,305,class PathItem(BaseModelWithConfig):
  fastapi/openapi/models::SecuritySchemeType,class,fastapi/openapi/models.py,321,class SecuritySchemeType(Enum):
  fastapi/openapi/models::SecurityBase,class,fastapi/openapi/models.py,328,class SecurityBase(BaseModelWithConfig):
  fastapi/openapi/models::APIKeyIn,class,fastapi/openapi/models.py,333,class APIKeyIn(Enum):
  fastapi/openapi/models::APIKey,class,fastapi/openapi/models.py,339,class APIKey(SecurityBase):
  fastapi/openapi/models::HTTPBase,class,fastapi/openapi/models.py,345,class HTTPBase(SecurityBase):
  fastapi/openapi/models::HTTPBearer,class,fastapi/openapi/models.py,350,class HTTPBearer(HTTPBase):
  fastapi/openapi/models::OAuthFlow,class,fastapi/openapi/models.py,355,class OAuthFlow(BaseModelWithConfig):
  fastapi/openapi/models::OAuthFlowImplicit,class,fastapi/openapi/models.py,360,class OAuthFlowImplicit(OAuthFlow):
  fastapi/openapi/models::OAuthFlowPassword,class,fastapi/openapi/models.py,364,class OAuthFlowPassword(OAuthFlow):
  fastapi/openapi/models::OAuthFlowClientCredentials,class,fastapi/openapi/models.py,368,class OAuthFlowClientCredentials(OAuthFlow):
  fastapi/openapi/models::OAuthFlowAuthorizationCode,class,fastapi/openapi/models.py,372,class OAuthFlowAuthorizationCode(OAuthFlow):
  fastapi/openapi/models::OAuthFlows,class,fastapi/openapi/models.py,377,class OAuthFlows(BaseModelWithConfig):
  fastapi/openapi/models::OAuth2,class,fastapi/openapi/models.py,384,class OAuth2(SecurityBase):
  fastapi/openapi/models::OpenIdConnect,class,fastapi/openapi/models.py,389,class OpenIdConnect(SecurityBase):
  fastapi/openapi/models::Components,class,fastapi/openapi/models.py,399,class Components(BaseModelWithConfig):
  fastapi/openapi/models::Tag,class,fastapi/openapi/models.py,413,class Tag(BaseModelWithConfig):
  fastapi/openapi/models::OpenAPI,class,fastapi/openapi/models.py,419,class OpenAPI(BaseModelWithConfig):
  fastapi/routing::_AsyncLiftContextManager,class,fastapi/routing.py,154,class _AsyncLiftContextManager(AbstractAsyncContextManager[_T]):
  fastapi/routing::_DefaultLifespan,class,fastapi/routing.py,211,class _DefaultLifespan:
  fastapi/routing::APIWebSocketRoute,class,fastapi/routing.py,512,class APIWebSocketRoute(routing.WebSocketRoute):
  fastapi/routing::APIRoute,class,fastapi/routing.py,554,class APIRoute(routing.Route):
  fastapi/routing::APIRouter,class,fastapi/routing.py,708,class APIRouter(routing.Router):
  fastapi/exceptions::EndpointContext,class,fastapi/exceptions.py,10,"class EndpointContext(TypedDict, total=False):"
  fastapi/exceptions::HTTPException,class,fastapi/exceptions.py,17,class HTTPException(StarletteHTTPException):
  fastapi/exceptions::WebSocketException,class,fastapi/exceptions.py,86,class WebSocketException(StarletteWebSocketException):
  fastapi/exceptions::FastAPIError,class,fastapi/exceptions.py,161,class FastAPIError(RuntimeError):
  fastapi/exceptions::DependencyScopeError,class,fastapi/exceptions.py,167,class DependencyScopeError(FastAPIError):
  fastapi/exceptions::ValidationException,class,fastapi/exceptions.py,174,class ValidationException(Exception):
  fastapi/exceptions::RequestValidationError,class,fastapi/exceptions.py,212,class RequestValidationError(ValidationException):
  fastapi/exceptions::WebSocketRequestValidationError,class,fastapi/exceptions.py,224,class WebSocketRequestValidationError(ValidationException):
  fastapi/exceptions::ResponseValidationError,class,fastapi/exceptions.py,234,class ResponseValidationError(ValidationException):
  fastapi/exceptions::PydanticV1NotSupportedError,class,fastapi/exceptions.py,246,class PydanticV1NotSupportedError(FastAPIError):
  fastapi/exceptions::FastAPIDeprecationWarning,class,fastapi/exceptions.py,252,class FastAPIDeprecationWarning(UserWarning):
  fastapi/_compat/v2::ModelField,class,fastapi/_compat/v2.py,84,class ModelField:
  fastapi/datastructures::UploadFile,class,fastapi/datastructures.py,21,class UploadFile(StarletteUploadFile):
  fastapi/datastructures::DefaultPlaceholder,class,fastapi/datastructures.py,153,class DefaultPlaceholder:
  scripts/contributors::Author,class,scripts/contributors.py,59,class Author(BaseModel):
  scripts/contributors::LabelNode,class,scripts/contributors.py,65,class LabelNode(BaseModel):
  scripts/contributors::Labels,class,scripts/contributors.py,69,class Labels(BaseModel):
  scripts/contributors::ReviewNode,class,scripts/contributors.py,73,class ReviewNode(BaseModel):
  scripts/contributors::Reviews,class,scripts/contributors.py,78,class Reviews(BaseModel):
  scripts/contributors::PullRequestNode,class,scripts/contributors.py,82,class PullRequestNode(BaseModel):
  scripts/contributors::PullRequestEdge,class,scripts/contributors.py,94,class PullRequestEdge(BaseModel):
  scripts/contributors::PullRequests,class,scripts/contributors.py,99,class PullRequests(BaseModel):
  scripts/contributors::PRsRepository,class,scripts/contributors.py,103,class PRsRepository(BaseModel):
  scripts/contributors::PRsResponseData,class,scripts/contributors.py,107,class PRsResponseData(BaseModel):
  scripts/contributors::PRsResponse,class,scripts/contributors.py,111,class PRsResponse(BaseModel):
  scripts/contributors::Settings,class,scripts/contributors.py,115,class Settings(BaseSettings):
  scripts/contributors::ContributorsResults,class,scripts/contributors.py,168,class ContributorsResults(BaseModel):
  scripts/label_approved::LabelSettings,class,scripts/label_approved.py,10,class LabelSettings(BaseModel):
  scripts/label_approved::Settings,class,scripts/label_approved.py,18,class Settings(BaseSettings):
  scripts/notify_translations::Comment,class,scripts/notify_translations.py,87,class Comment(BaseModel):
  scripts/notify_translations::UpdateDiscussionComment,class,scripts/notify_translations.py,93,class UpdateDiscussionComment(BaseModel):
  scripts/notify_translations::UpdateCommentData,class,scripts/notify_translations.py,97,class UpdateCommentData(BaseModel):
  scripts/notify_translations::UpdateCommentResponse,class,scripts/notify_translations.py,101,class UpdateCommentResponse(BaseModel):
  scripts/notify_translations::AddDiscussionComment,class,scripts/notify_translations.py,105,class AddDiscussionComment(BaseModel):
  scripts/notify_translations::AddCommentData,class,scripts/notify_translations.py,109,class AddCommentData(BaseModel):
  scripts/notify_translations::AddCommentResponse,class,scripts/notify_translations.py,113,class AddCommentResponse(BaseModel):
  scripts/notify_translations::CommentsEdge,class,scripts/notify_translations.py,117,class CommentsEdge(BaseModel):
  scripts/notify_translations::Comments,class,scripts/notify_translations.py,122,class Comments(BaseModel):
  scripts/notify_translations::CommentsDiscussion,class,scripts/notify_translations.py,126,class CommentsDiscussion(BaseModel):
  scripts/notify_translations::CommentsRepository,class,scripts/notify_translations.py,130,class CommentsRepository(BaseModel):
  scripts/notify_translations::CommentsData,class,scripts/notify_translations.py,134,class CommentsData(BaseModel):
  scripts/notify_translations::CommentsResponse,class,scripts/notify_translations.py,138,class CommentsResponse(BaseModel):
  scripts/notify_translations::AllDiscussionsLabelNode,class,scripts/notify_translations.py,142,class AllDiscussionsLabelNode(BaseModel):
  scripts/notify_translations::AllDiscussionsLabelsEdge,class,scripts/notify_translations.py,147,class AllDiscussionsLabelsEdge(BaseModel):
  scripts/notify_translations::AllDiscussionsDiscussionLabels,class,scripts/notify_translations.py,151,class AllDiscussionsDiscussionLabels(BaseModel):
  scripts/notify_translations::AllDiscussionsDiscussionNode,class,scripts/notify_translations.py,155,class AllDiscussionsDiscussionNode(BaseModel):
  scripts/notify_translations::AllDiscussionsDiscussions,class,scripts/notify_translations.py,162,class AllDiscussionsDiscussions(BaseModel):
  scripts/notify_translations::AllDiscussionsRepository,class,scripts/notify_translations.py,166,class AllDiscussionsRepository(BaseModel):
  scripts/notify_translations::AllDiscussionsData,class,scripts/notify_translations.py,170,class AllDiscussionsData(BaseModel):
  scripts/notify_translations::AllDiscussionsResponse,class,scripts/notify_translations.py,174,class AllDiscussionsResponse(BaseModel):
  scripts/notify_translations::Settings,class,scripts/notify_translations.py,178,class Settings(BaseSettings):
  scripts/notify_translations::PartialGitHubEventIssue,class,scripts/notify_translations.py,190,class PartialGitHubEventIssue(BaseModel):
  scripts/notify_translations::PartialGitHubEvent,class,scripts/notify_translations.py,194,class PartialGitHubEvent(BaseModel):
  scripts/sponsors::SponsorEntity,class,scripts/sponsors.py,48,class SponsorEntity(BaseModel):
  scripts/sponsors::Tier,class,scripts/sponsors.py,54,class Tier(BaseModel):
  scripts/sponsors::SponsorshipAsMaintainerNode,class,scripts/sponsors.py,59,class SponsorshipAsMaintainerNode(BaseModel):
  scripts/sponsors::SponsorshipAsMaintainerEdge,class,scripts/sponsors.py,64,class SponsorshipAsMaintainerEdge(BaseModel):
  scripts/sponsors::SponsorshipAsMaintainer,class,scripts/sponsors.py,69,class SponsorshipAsMaintainer(BaseModel):
  scripts/sponsors::SponsorsUser,class,scripts/sponsors.py,73,class SponsorsUser(BaseModel):
  scripts/sponsors::SponsorsResponseData,class,scripts/sponsors.py,77,class SponsorsResponseData(BaseModel):
  scripts/sponsors::SponsorsResponse,class,scripts/sponsors.py,81,class SponsorsResponse(BaseModel):
  scripts/sponsors::Settings,class,scripts/sponsors.py,85,class Settings(BaseSettings):
  scripts/doc_parsing_utils::CodeIncludeInfo,class,scripts/doc_parsing_utils.py,37,class CodeIncludeInfo(TypedDict):
  scripts/doc_parsing_utils::HeaderPermalinkInfo,class,scripts/doc_parsing_utils.py,42,class HeaderPermalinkInfo(TypedDict):
  scripts/doc_parsing_utils::MarkdownLinkInfo,class,scripts/doc_parsing_utils.py,49,class MarkdownLinkInfo(TypedDict):
  scripts/doc_parsing_utils::HTMLLinkAttribute,class,scripts/doc_parsing_utils.py,58,class HTMLLinkAttribute(TypedDict):
  scripts/doc_parsing_utils::HtmlLinkInfo,class,scripts/doc_parsing_utils.py,64,class HtmlLinkInfo(TypedDict):
  scripts/doc_parsing_utils::MultilineCodeBlockInfo,class,scripts/doc_parsing_utils.py,71,class MultilineCodeBlockInfo(TypedDict):
  scripts/docs::VisibleTextExtractor,class,scripts/docs.py,69,class VisibleTextExtractor(HTMLParser):
  scripts/mkdocs_hooks::EnFile,class,scripts/mkdocs_hooks.py,48,class EnFile(File):
  scripts/people::Author,class,scripts/people.py,65,class Author(BaseModel):
  scripts/people::CommentsNode,class,scripts/people.py,71,class CommentsNode(BaseModel):
  scripts/people::Replies,class,scripts/people.py,76,class Replies(BaseModel):
  scripts/people::DiscussionsCommentsNode,class,scripts/people.py,81,class DiscussionsCommentsNode(CommentsNode):
  scripts/people::DiscussionsComments,class,scripts/people.py,85,class DiscussionsComments(BaseModel):
  scripts/people::DiscussionsNode,class,scripts/people.py,90,class DiscussionsNode(BaseModel):
  scripts/people::DiscussionsEdge,class,scripts/people.py,98,class DiscussionsEdge(BaseModel):
  scripts/people::Discussions,class,scripts/people.py,103,class Discussions(BaseModel):
  scripts/people::DiscussionsRepository,class,scripts/people.py,107,class DiscussionsRepository(BaseModel):
  scripts/people::DiscussionsResponseData,class,scripts/people.py,111,class DiscussionsResponseData(BaseModel):
  scripts/people::DiscussionsResponse,class,scripts/people.py,115,class DiscussionsResponse(BaseModel):
  scripts/people::Settings,class,scripts/people.py,119,class Settings(BaseSettings):
  scripts/people::DiscussionExpertsResults,class,scripts/people.py,171,class DiscussionExpertsResults(BaseModel):
  scripts/deploy_docs_status::Settings,class,scripts/deploy_docs_status.py,10,class Settings(BaseSettings):
  scripts/deploy_docs_status::LinkData,class,scripts/deploy_docs_status.py,19,class LinkData(BaseModel):
  scripts/topic_repos::Settings,class,scripts/topic_repos.py,12,class Settings(BaseSettings):
  scripts/topic_repos::Repo,class,scripts/topic_repos.py,17,class Repo(BaseModel):
  tests/test_request_params/test_cookie/test_required_str::CookieModelRequiredStr,class,tests/test_request_params/test_cookie/test_required_str.py,21,class CookieModelRequiredStr(BaseModel):
  tests/test_request_params/test_cookie/test_required_str::CookieModelRequiredAlias,class,tests/test_request_params/test_cookie/test_required_str.py,88,class CookieModelRequiredAlias(BaseModel):
  tests/test_request_params/test_cookie/test_required_str::CookieModelRequiredValidationAlias,class,tests/test_request_params/test_cookie/test_required_str.py,187,class CookieModelRequiredValidationAlias(BaseModel):
  tests/test_request_params/test_cookie/test_required_str::CookieModelRequiredAliasAndValidationAlias,class,tests/test_request_params/test_cookie/test_required_str.py,293,class CookieModelRequiredAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_cookie/test_optional_str::CookieModelOptionalStr,class,tests/test_request_params/test_cookie/test_optional_str.py,20,class CookieModelOptionalStr(BaseModel):
  tests/test_request_params/test_cookie/test_optional_str::CookieModelOptionalAlias,class,tests/test_request_params/test_cookie/test_optional_str.py,83,class CookieModelOptionalAlias(BaseModel):
  tests/test_request_params/test_cookie/test_optional_str::CookieModelOptionalValidationAlias,class,tests/test_request_params/test_cookie/test_optional_str.py,161,class CookieModelOptionalValidationAlias(BaseModel):
  tests/test_request_params/test_cookie/test_optional_str::CookieModelOptionalAliasAndValidationAlias,class,tests/test_request_params/test_cookie/test_optional_str.py,246,class CookieModelOptionalAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_form/test_list::FormModelRequiredListStr,class,tests/test_request_params/test_form/test_list.py,22,class FormModelRequiredListStr(BaseModel):
  tests/test_request_params/test_form/test_list::FormModelRequiredListAlias,class,tests/test_request_params/test_form/test_list.py,93,class FormModelRequiredListAlias(BaseModel):
  tests/test_request_params/test_form/test_list::FormModelRequiredListValidationAlias,class,tests/test_request_params/test_form/test_list.py,196,class FormModelRequiredListValidationAlias(BaseModel):
  tests/test_request_params/test_form/test_list::FormModelRequiredListAliasAndValidationAlias,class,tests/test_request_params/test_form/test_list.py,308,class FormModelRequiredListAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_form/test_required_str::FormModelRequiredStr,class,tests/test_request_params/test_form/test_required_str.py,22,class FormModelRequiredStr(BaseModel):
  tests/test_request_params/test_form/test_required_str::FormModelRequiredAlias,class,tests/test_request_params/test_form/test_required_str.py,89,class FormModelRequiredAlias(BaseModel):
  tests/test_request_params/test_form/test_required_str::FormModelRequiredValidationAlias,class,tests/test_request_params/test_form/test_required_str.py,181,class FormModelRequiredValidationAlias(BaseModel):
  tests/test_request_params/test_form/test_required_str::FormModelRequiredAliasAndValidationAlias,class,tests/test_request_params/test_form/test_required_str.py,291,class FormModelRequiredAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_form/test_optional_str::FormModelOptionalStr,class,tests/test_request_params/test_form/test_optional_str.py,21,class FormModelOptionalStr(BaseModel):
  tests/test_request_params/test_form/test_optional_str::FormModelOptionalAlias,class,tests/test_request_params/test_form/test_optional_str.py,83,class FormModelOptionalAlias(BaseModel):
  tests/test_request_params/test_form/test_optional_str::FormModelOptionalValidationAlias,class,tests/test_request_params/test_form/test_optional_str.py,159,class FormModelOptionalValidationAlias(BaseModel):
  tests/test_request_params/test_form/test_optional_str::FormModelOptionalAliasAndValidationAlias,class,tests/test_request_params/test_form/test_optional_str.py,247,class FormModelOptionalAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_form/test_optional_list::FormModelOptionalListStr,class,tests/test_request_params/test_form/test_optional_list.py,23,class FormModelOptionalListStr(BaseModel):
  tests/test_request_params/test_form/test_optional_list::FormModelOptionalListAlias,class,tests/test_request_params/test_form/test_optional_list.py,88,class FormModelOptionalListAlias(BaseModel):
  tests/test_request_params/test_form/test_optional_list::FormModelOptionalListValidationAlias,class,tests/test_request_params/test_form/test_optional_list.py,171,class FormModelOptionalListValidationAlias(BaseModel):
  tests/test_request_params/test_form/test_optional_list::FormModelOptionalListAliasAndValidationAlias,class,tests/test_request_params/test_form/test_optional_list.py,260,class FormModelOptionalListAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_header/test_list::HeaderModelRequiredListStr,class,tests/test_request_params/test_header/test_list.py,21,class HeaderModelRequiredListStr(BaseModel):
  tests/test_request_params/test_header/test_list::HeaderModelRequiredListAlias,class,tests/test_request_params/test_header/test_list.py,91,class HeaderModelRequiredListAlias(BaseModel):
  tests/test_request_params/test_header/test_list::HeaderModelRequiredListValidationAlias,class,tests/test_request_params/test_header/test_list.py,191,class HeaderModelRequiredListValidationAlias(BaseModel):
  tests/test_request_params/test_header/test_list::HeaderModelRequiredListAliasAndValidationAlias,class,tests/test_request_params/test_header/test_list.py,298,class HeaderModelRequiredListAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_header/test_required_str::HeaderModelRequiredStr,class,tests/test_request_params/test_header/test_required_str.py,21,class HeaderModelRequiredStr(BaseModel):
  tests/test_request_params/test_header/test_required_str::HeaderModelRequiredAlias,class,tests/test_request_params/test_header/test_required_str.py,87,class HeaderModelRequiredAlias(BaseModel):
  tests/test_request_params/test_header/test_required_str::HeaderModelRequiredValidationAlias,class,tests/test_request_params/test_header/test_required_str.py,181,class HeaderModelRequiredValidationAlias(BaseModel):
  tests/test_request_params/test_header/test_required_str::HeaderModelRequiredAliasAndValidationAlias,class,tests/test_request_params/test_header/test_required_str.py,285,class HeaderModelRequiredAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_header/test_optional_str::HeaderModelOptionalStr,class,tests/test_request_params/test_header/test_optional_str.py,20,class HeaderModelOptionalStr(BaseModel):
  tests/test_request_params/test_header/test_optional_str::HeaderModelOptionalAlias,class,tests/test_request_params/test_header/test_optional_str.py,82,class HeaderModelOptionalAlias(BaseModel):
  tests/test_request_params/test_header/test_optional_str::HeaderModelOptionalValidationAlias,class,tests/test_request_params/test_header/test_optional_str.py,158,class HeaderModelOptionalValidationAlias(BaseModel):
  tests/test_request_params/test_header/test_optional_str::HeaderModelOptionalAliasAndValidationAlias,class,tests/test_request_params/test_header/test_optional_str.py,241,class HeaderModelOptionalAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_header/test_optional_list::HeaderModelOptionalListStr,class,tests/test_request_params/test_header/test_optional_list.py,22,class HeaderModelOptionalListStr(BaseModel):
  tests/test_request_params/test_header/test_optional_list::HeaderModelOptionalListAlias,class,tests/test_request_params/test_header/test_optional_list.py,89,class HeaderModelOptionalListAlias(BaseModel):
  tests/test_request_params/test_header/test_optional_list::HeaderModelOptionalListValidationAlias,class,tests/test_request_params/test_header/test_optional_list.py,170,class HeaderModelOptionalListValidationAlias(BaseModel):
  tests/test_request_params/test_header/test_optional_list::HeaderModelOptionalListAliasAndValidationAlias,class,tests/test_request_params/test_header/test_optional_list.py,255,class HeaderModelOptionalListAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_body/test_list::BodyModelRequiredListStr,class,tests/test_request_params/test_body/test_list.py,22,class BodyModelRequiredListStr(BaseModel):
  tests/test_request_params/test_body/test_list::BodyModelRequiredListAlias,class,tests/test_request_params/test_body/test_list.py,96,class BodyModelRequiredListAlias(BaseModel):
  tests/test_request_params/test_body/test_list::BodyModelRequiredListValidationAlias,class,tests/test_request_params/test_body/test_list.py,195,class BodyModelRequiredListValidationAlias(BaseModel):
  tests/test_request_params/test_body/test_list::BodyModelRequiredListAliasAndValidationAlias,class,tests/test_request_params/test_body/test_list.py,309,class BodyModelRequiredListAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_body/test_required_str::BodyModelRequiredStr,class,tests/test_request_params/test_body/test_required_str.py,22,class BodyModelRequiredStr(BaseModel):
  tests/test_request_params/test_body/test_required_str::BodyModelRequiredAlias,class,tests/test_request_params/test_body/test_required_str.py,92,class BodyModelRequiredAlias(BaseModel):
  tests/test_request_params/test_body/test_required_str::BodyModelRequiredValidationAlias,class,tests/test_request_params/test_body/test_required_str.py,185,class BodyModelRequiredValidationAlias(BaseModel):
  tests/test_request_params/test_body/test_required_str::BodyModelRequiredAliasAndValidationAlias,class,tests/test_request_params/test_body/test_required_str.py,297,class BodyModelRequiredAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_body/test_optional_str::BodyModelOptionalStr,class,tests/test_request_params/test_body/test_optional_str.py,21,class BodyModelOptionalStr(BaseModel):
  tests/test_request_params/test_body/test_optional_str::BodyModelOptionalAlias,class,tests/test_request_params/test_body/test_optional_str.py,106,class BodyModelOptionalAlias(BaseModel):
  tests/test_request_params/test_body/test_optional_str::BodyModelOptionalValidationAlias,class,tests/test_request_params/test_body/test_optional_str.py,207,class BodyModelOptionalValidationAlias(BaseModel):
  tests/test_request_params/test_body/test_optional_str::BodyModelOptionalAliasAndValidationAlias,class,tests/test_request_params/test_body/test_optional_str.py,318,class BodyModelOptionalAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_body/test_optional_list::BodyModelOptionalListStr,class,tests/test_request_params/test_body/test_optional_list.py,23,class BodyModelOptionalListStr(BaseModel):
  tests/test_request_params/test_body/test_optional_list::BodyModelOptionalListAlias,class,tests/test_request_params/test_body/test_optional_list.py,111,class BodyModelOptionalListAlias(BaseModel):
  tests/test_request_params/test_body/test_optional_list::BodyModelOptionalListValidationAlias,class,tests/test_request_params/test_body/test_optional_list.py,217,class BodyModelOptionalListValidationAlias(BaseModel):
  tests/test_request_params/test_body/test_optional_list::BodyModelOptionalListAliasAndValidationAlias,class,tests/test_request_params/test_body/test_optional_list.py,333,class BodyModelOptionalListAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_query/test_list::QueryModelRequiredListStr,class,tests/test_request_params/test_query/test_list.py,21,class QueryModelRequiredListStr(BaseModel):
  tests/test_request_params/test_query/test_list::QueryModelRequiredListAlias,class,tests/test_request_params/test_query/test_list.py,91,class QueryModelRequiredListAlias(BaseModel):
  tests/test_request_params/test_query/test_list::QueryModelRequiredListValidationAlias,class,tests/test_request_params/test_query/test_list.py,191,class QueryModelRequiredListValidationAlias(BaseModel):
  tests/test_request_params/test_query/test_list::QueryModelRequiredListAliasAndValidationAlias,class,tests/test_request_params/test_query/test_list.py,296,class QueryModelRequiredListAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_query/test_required_str::QueryModelRequiredStr,class,tests/test_request_params/test_query/test_required_str.py,21,class QueryModelRequiredStr(BaseModel):
  tests/test_request_params/test_query/test_required_str::QueryModelRequiredAlias,class,tests/test_request_params/test_query/test_required_str.py,87,class QueryModelRequiredAlias(BaseModel):
  tests/test_request_params/test_query/test_required_str::QueryModelRequiredValidationAlias,class,tests/test_request_params/test_query/test_required_str.py,184,class QueryModelRequiredValidationAlias(BaseModel):
  tests/test_request_params/test_query/test_required_str::QueryModelRequiredAliasAndValidationAlias,class,tests/test_request_params/test_query/test_required_str.py,288,class QueryModelRequiredAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_query/test_optional_str::QueryModelOptionalStr,class,tests/test_request_params/test_query/test_optional_str.py,20,class QueryModelOptionalStr(BaseModel):
  tests/test_request_params/test_query/test_optional_str::QueryModelOptionalAlias,class,tests/test_request_params/test_query/test_optional_str.py,82,class QueryModelOptionalAlias(BaseModel):
  tests/test_request_params/test_query/test_optional_str::QueryModelOptionalValidationAlias,class,tests/test_request_params/test_query/test_optional_str.py,158,class QueryModelOptionalValidationAlias(BaseModel):
  tests/test_request_params/test_query/test_optional_str::QueryModelOptionalAliasAndValidationAlias,class,tests/test_request_params/test_query/test_optional_str.py,241,class QueryModelOptionalAliasAndValidationAlias(BaseModel):
  tests/test_request_params/test_query/test_optional_list::QueryModelOptionalListStr,class,tests/test_request_params/test_query/test_optional_list.py,22,class QueryModelOptionalListStr(BaseModel):
  tests/test_request_params/test_query/test_optional_list::QueryModelOptionalListAlias,class,tests/test_request_params/test_query/test_optional_list.py,89,class QueryModelOptionalListAlias(BaseModel):
  tests/test_request_params/test_query/test_optional_list::QueryModelOptionalListValidationAlias,class,tests/test_request_params/test_query/test_optional_list.py,170,class QueryModelOptionalListValidationAlias(BaseModel):
  tests/test_request_params/test_query/test_optional_list::QueryModelOptionalListAliasAndValidationAlias,class,tests/test_request_params/test_query/test_optional_list.py,253,class QueryModelOptionalListAliasAndValidationAlias(BaseModel):
  tests/test_multi_body_errors::Item,class,tests/test_multi_body_errors.py,12,class Item(BaseModel):
  tests/test_union_body_discriminator_annotated::Cat,class,tests/test_union_body_discriminator_annotated.py,17,class Cat(BaseModel):
  tests/test_union_body_discriminator_annotated::Dog,class,tests/test_union_body_discriminator_annotated.py,21,class Dog(BaseModel):
  tests/test_computed_fields::Rectangle,class,tests/test_computed_fields.py,14,class Rectangle(BaseModel):
  tests/test_security_oauth2::User,class,tests/test_security_oauth2.py,20,class User(BaseModel):
  tests/test_response_model_invalid::NonPydanticModel,class,tests/test_response_model_invalid.py,6,class NonPydanticModel:
  tests/test_dependency_yield_scope::Session,class,tests/test_dependency_yield_scope.py,11,class Session:
  tests/test_dependency_yield_scope::NamedSession,class,tests/test_dependency_yield_scope.py,32,class NamedSession:
  tests/test_union_forms::UserForm,class,tests/test_union_forms.py,11,class UserForm(BaseModel):
  tests/test_union_forms::CompanyForm,class,tests/test_union_forms.py,16,class CompanyForm(BaseModel):
  tests/test_schema_extra_examples::Item,class,tests/test_schema_extra_examples.py,14,class Item(BaseModel):
  tests/test_default_response_class_router::OverrideResponse,class,tests/test_default_response_class_router.py,6,class OverrideResponse(JSONResponse):
  tests/test_invalid_sequence_param::Item,class,tests/test_invalid_sequence_param.py,15,class Item(BaseModel):
  # ... 4675 more symbols omitted

hierarchies[602]{symbol,relationship,target,file,line}:
  tests/test_request_params/test_cookie/test_required_str::CookieModelRequiredStr,extends,BaseModel,tests/test_request_params/test_cookie/test_required_str.py,21
  tests/test_request_params/test_cookie/test_required_str::CookieModelRequiredAlias,extends,BaseModel,tests/test_request_params/test_cookie/test_required_str.py,88
  tests/test_request_params/test_cookie/test_required_str::CookieModelRequiredValidationAlias,extends,BaseModel,tests/test_request_params/test_cookie/test_required_str.py,187
  tests/test_request_params/test_cookie/test_required_str::CookieModelRequiredAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_cookie/test_required_str.py,293
  tests/test_request_params/test_cookie/test_optional_str::CookieModelOptionalStr,extends,BaseModel,tests/test_request_params/test_cookie/test_optional_str.py,20
  tests/test_request_params/test_cookie/test_optional_str::CookieModelOptionalAlias,extends,BaseModel,tests/test_request_params/test_cookie/test_optional_str.py,83
  tests/test_request_params/test_cookie/test_optional_str::CookieModelOptionalValidationAlias,extends,BaseModel,tests/test_request_params/test_cookie/test_optional_str.py,161
  tests/test_request_params/test_cookie/test_optional_str::CookieModelOptionalAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_cookie/test_optional_str.py,246
  tests/test_request_params/test_form/test_list::FormModelRequiredListStr,extends,BaseModel,tests/test_request_params/test_form/test_list.py,22
  tests/test_request_params/test_form/test_list::FormModelRequiredListAlias,extends,BaseModel,tests/test_request_params/test_form/test_list.py,93
  tests/test_request_params/test_form/test_list::FormModelRequiredListValidationAlias,extends,BaseModel,tests/test_request_params/test_form/test_list.py,196
  tests/test_request_params/test_form/test_list::FormModelRequiredListAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_form/test_list.py,308
  tests/test_request_params/test_form/test_required_str::FormModelRequiredStr,extends,BaseModel,tests/test_request_params/test_form/test_required_str.py,22
  tests/test_request_params/test_form/test_required_str::FormModelRequiredAlias,extends,BaseModel,tests/test_request_params/test_form/test_required_str.py,89
  tests/test_request_params/test_form/test_required_str::FormModelRequiredValidationAlias,extends,BaseModel,tests/test_request_params/test_form/test_required_str.py,181
  tests/test_request_params/test_form/test_required_str::FormModelRequiredAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_form/test_required_str.py,291
  tests/test_request_params/test_form/test_optional_str::FormModelOptionalStr,extends,BaseModel,tests/test_request_params/test_form/test_optional_str.py,21
  tests/test_request_params/test_form/test_optional_str::FormModelOptionalAlias,extends,BaseModel,tests/test_request_params/test_form/test_optional_str.py,83
  tests/test_request_params/test_form/test_optional_str::FormModelOptionalValidationAlias,extends,BaseModel,tests/test_request_params/test_form/test_optional_str.py,159
  tests/test_request_params/test_form/test_optional_str::FormModelOptionalAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_form/test_optional_str.py,247
  tests/test_request_params/test_form/test_optional_list::FormModelOptionalListStr,extends,BaseModel,tests/test_request_params/test_form/test_optional_list.py,23
  tests/test_request_params/test_form/test_optional_list::FormModelOptionalListAlias,extends,BaseModel,tests/test_request_params/test_form/test_optional_list.py,88
  tests/test_request_params/test_form/test_optional_list::FormModelOptionalListValidationAlias,extends,BaseModel,tests/test_request_params/test_form/test_optional_list.py,171
  tests/test_request_params/test_form/test_optional_list::FormModelOptionalListAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_form/test_optional_list.py,260
  tests/test_request_params/test_header/test_list::HeaderModelRequiredListStr,extends,BaseModel,tests/test_request_params/test_header/test_list.py,21
  tests/test_request_params/test_header/test_list::HeaderModelRequiredListAlias,extends,BaseModel,tests/test_request_params/test_header/test_list.py,91
  tests/test_request_params/test_header/test_list::HeaderModelRequiredListValidationAlias,extends,BaseModel,tests/test_request_params/test_header/test_list.py,191
  tests/test_request_params/test_header/test_list::HeaderModelRequiredListAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_header/test_list.py,298
  tests/test_request_params/test_header/test_required_str::HeaderModelRequiredStr,extends,BaseModel,tests/test_request_params/test_header/test_required_str.py,21
  tests/test_request_params/test_header/test_required_str::HeaderModelRequiredAlias,extends,BaseModel,tests/test_request_params/test_header/test_required_str.py,87
  tests/test_request_params/test_header/test_required_str::HeaderModelRequiredValidationAlias,extends,BaseModel,tests/test_request_params/test_header/test_required_str.py,181
  tests/test_request_params/test_header/test_required_str::HeaderModelRequiredAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_header/test_required_str.py,285
  tests/test_request_params/test_header/test_optional_str::HeaderModelOptionalStr,extends,BaseModel,tests/test_request_params/test_header/test_optional_str.py,20
  tests/test_request_params/test_header/test_optional_str::HeaderModelOptionalAlias,extends,BaseModel,tests/test_request_params/test_header/test_optional_str.py,82
  tests/test_request_params/test_header/test_optional_str::HeaderModelOptionalValidationAlias,extends,BaseModel,tests/test_request_params/test_header/test_optional_str.py,158
  tests/test_request_params/test_header/test_optional_str::HeaderModelOptionalAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_header/test_optional_str.py,241
  tests/test_request_params/test_header/test_optional_list::HeaderModelOptionalListStr,extends,BaseModel,tests/test_request_params/test_header/test_optional_list.py,22
  tests/test_request_params/test_header/test_optional_list::HeaderModelOptionalListAlias,extends,BaseModel,tests/test_request_params/test_header/test_optional_list.py,89
  tests/test_request_params/test_header/test_optional_list::HeaderModelOptionalListValidationAlias,extends,BaseModel,tests/test_request_params/test_header/test_optional_list.py,170
  tests/test_request_params/test_header/test_optional_list::HeaderModelOptionalListAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_header/test_optional_list.py,255
  tests/test_request_params/test_body/test_list::BodyModelRequiredListStr,extends,BaseModel,tests/test_request_params/test_body/test_list.py,22
  tests/test_request_params/test_body/test_list::BodyModelRequiredListAlias,extends,BaseModel,tests/test_request_params/test_body/test_list.py,96
  tests/test_request_params/test_body/test_list::BodyModelRequiredListValidationAlias,extends,BaseModel,tests/test_request_params/test_body/test_list.py,195
  tests/test_request_params/test_body/test_list::BodyModelRequiredListAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_body/test_list.py,309
  tests/test_request_params/test_body/test_required_str::BodyModelRequiredStr,extends,BaseModel,tests/test_request_params/test_body/test_required_str.py,22
  tests/test_request_params/test_body/test_required_str::BodyModelRequiredAlias,extends,BaseModel,tests/test_request_params/test_body/test_required_str.py,92
  tests/test_request_params/test_body/test_required_str::BodyModelRequiredValidationAlias,extends,BaseModel,tests/test_request_params/test_body/test_required_str.py,185
  tests/test_request_params/test_body/test_required_str::BodyModelRequiredAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_body/test_required_str.py,297
  tests/test_request_params/test_body/test_optional_str::BodyModelOptionalStr,extends,BaseModel,tests/test_request_params/test_body/test_optional_str.py,21
  tests/test_request_params/test_body/test_optional_str::BodyModelOptionalAlias,extends,BaseModel,tests/test_request_params/test_body/test_optional_str.py,106
  tests/test_request_params/test_body/test_optional_str::BodyModelOptionalValidationAlias,extends,BaseModel,tests/test_request_params/test_body/test_optional_str.py,207
  tests/test_request_params/test_body/test_optional_str::BodyModelOptionalAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_body/test_optional_str.py,318
  tests/test_request_params/test_body/test_optional_list::BodyModelOptionalListStr,extends,BaseModel,tests/test_request_params/test_body/test_optional_list.py,23
  tests/test_request_params/test_body/test_optional_list::BodyModelOptionalListAlias,extends,BaseModel,tests/test_request_params/test_body/test_optional_list.py,111
  tests/test_request_params/test_body/test_optional_list::BodyModelOptionalListValidationAlias,extends,BaseModel,tests/test_request_params/test_body/test_optional_list.py,217
  tests/test_request_params/test_body/test_optional_list::BodyModelOptionalListAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_body/test_optional_list.py,333
  tests/test_request_params/test_query/test_list::QueryModelRequiredListStr,extends,BaseModel,tests/test_request_params/test_query/test_list.py,21
  tests/test_request_params/test_query/test_list::QueryModelRequiredListAlias,extends,BaseModel,tests/test_request_params/test_query/test_list.py,91
  tests/test_request_params/test_query/test_list::QueryModelRequiredListValidationAlias,extends,BaseModel,tests/test_request_params/test_query/test_list.py,191
  tests/test_request_params/test_query/test_list::QueryModelRequiredListAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_query/test_list.py,296
  tests/test_request_params/test_query/test_required_str::QueryModelRequiredStr,extends,BaseModel,tests/test_request_params/test_query/test_required_str.py,21
  tests/test_request_params/test_query/test_required_str::QueryModelRequiredAlias,extends,BaseModel,tests/test_request_params/test_query/test_required_str.py,87
  tests/test_request_params/test_query/test_required_str::QueryModelRequiredValidationAlias,extends,BaseModel,tests/test_request_params/test_query/test_required_str.py,184
  tests/test_request_params/test_query/test_required_str::QueryModelRequiredAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_query/test_required_str.py,288
  tests/test_request_params/test_query/test_optional_str::QueryModelOptionalStr,extends,BaseModel,tests/test_request_params/test_query/test_optional_str.py,20
  tests/test_request_params/test_query/test_optional_str::QueryModelOptionalAlias,extends,BaseModel,tests/test_request_params/test_query/test_optional_str.py,82
  tests/test_request_params/test_query/test_optional_str::QueryModelOptionalValidationAlias,extends,BaseModel,tests/test_request_params/test_query/test_optional_str.py,158
  tests/test_request_params/test_query/test_optional_str::QueryModelOptionalAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_query/test_optional_str.py,241
  tests/test_request_params/test_query/test_optional_list::QueryModelOptionalListStr,extends,BaseModel,tests/test_request_params/test_query/test_optional_list.py,22
  tests/test_request_params/test_query/test_optional_list::QueryModelOptionalListAlias,extends,BaseModel,tests/test_request_params/test_query/test_optional_list.py,89
  tests/test_request_params/test_query/test_optional_list::QueryModelOptionalListValidationAlias,extends,BaseModel,tests/test_request_params/test_query/test_optional_list.py,170
  tests/test_request_params/test_query/test_optional_list::QueryModelOptionalListAliasAndValidationAlias,extends,BaseModel,tests/test_request_params/test_query/test_optional_list.py,253
  tests/test_multi_body_errors::Item,extends,BaseModel,tests/test_multi_body_errors.py,12
  tests/test_union_body_discriminator_annotated::Cat,extends,BaseModel,tests/test_union_body_discriminator_annotated.py,17
  tests/test_union_body_discriminator_annotated::Dog,extends,BaseModel,tests/test_union_body_discriminator_annotated.py,21
  tests/test_computed_fields::Rectangle,extends,BaseModel,tests/test_computed_fields.py,14
  tests/test_security_oauth2::User,extends,BaseModel,tests/test_security_oauth2.py,20
  tests/test_union_forms::UserForm,extends,BaseModel,tests/test_union_forms.py,11
  tests/test_union_forms::CompanyForm,extends,BaseModel,tests/test_union_forms.py,16
  tests/test_schema_extra_examples::Item,extends,BaseModel,tests/test_schema_extra_examples.py,14
  tests/test_default_response_class_router::OverrideResponse,extends,JSONResponse,tests/test_default_response_class_router.py,6
  tests/test_invalid_sequence_param::Item,extends,BaseModel,tests/test_invalid_sequence_param.py,15
  tests/test_invalid_sequence_param::Item,extends,BaseModel,tests/test_invalid_sequence_param.py,30
  tests/test_invalid_sequence_param::Item,extends,BaseModel,tests/test_invalid_sequence_param.py,45
  tests/test_invalid_sequence_param::Item,extends,BaseModel,tests/test_invalid_sequence_param.py,60
  tests/forward_reference_type::ForwardRefModel,extends,BaseModel,tests/forward_reference_type.py,8
  tests/test_response_model_sub_types::Model,extends,BaseModel,tests/test_response_model_sub_types.py,7
  tests/test_schema_ref_pydantic_v2::ModelWithRef,extends,BaseModel,tests/test_schema_ref_pydantic_v2.py,14
  tests/test_security_openid_connect_description::User,extends,BaseModel,tests/test_security_openid_connect_description.py,14
  tests/test_inherited_custom_class::SomeCustomClass,extends,BaseModel,tests/test_inherited_custom_class.py,41
  tests/test_union_inherited_body::Item,extends,BaseModel,tests/test_union_inherited_body.py,11
  tests/test_union_inherited_body::ExtendedItem,extends,Item,tests/test_union_inherited_body.py,15
  tests/test_arbitrary_types::MyModel,extends,BaseModel,tests/test_arbitrary_types.py,29
  tests/test_arbitrary_types::MyModel,extends,BaseModel,tests/test_arbitrary_types.py,68
  tests/test_response_model_as_return_annotation::BaseUser,extends,BaseModel,tests/test_response_model_as_return_annotation.py,12
  tests/test_response_model_as_return_annotation::User,extends,BaseUser,tests/test_response_model_as_return_annotation.py,16
  tests/test_response_model_as_return_annotation::DBUser,extends,User,tests/test_response_model_as_return_annotation.py,20
  tests/test_response_model_as_return_annotation::Item,extends,BaseModel,tests/test_response_model_as_return_annotation.py,24
  tests/test_invalid_path_param::Item,extends,BaseModel,tests/test_invalid_path_param.py,10
  tests/test_invalid_path_param::Item,extends,BaseModel,tests/test_invalid_path_param.py,22
  tests/test_invalid_path_param::Item,extends,BaseModel,tests/test_invalid_path_param.py,34
  tests/test_schema_compat_pydantic_v2::PlatformRole,extends,str,tests/test_schema_compat_pydantic_v2.py,16
  tests/test_schema_compat_pydantic_v2::OtherRole,extends,str,tests/test_schema_compat_pydantic_v2.py,20
  tests/test_schema_compat_pydantic_v2::User,extends,BaseModel,tests/test_schema_compat_pydantic_v2.py,22
  tests/test_get_request_body::Product,extends,BaseModel,tests/test_get_request_body.py,9
  tests/test_datetime_custom_encoder::ModelWithDatetimeField,extends,BaseModel,tests/test_datetime_custom_encoder.py,11
  tests/test_security_api_key_cookie_optional::User,extends,BaseModel,tests/test_security_api_key_cookie_optional.py,14
  tests/test_read_with_orm_mode::PersonBase,extends,BaseModel,tests/test_read_with_orm_mode.py,9
  tests/test_read_with_orm_mode::Person,extends,PersonBase,tests/test_read_with_orm_mode.py,13
  tests/test_read_with_orm_mode::PersonCreate,extends,PersonBase,tests/test_read_with_orm_mode.py,20
  tests/test_read_with_orm_mode::PersonRead,extends,PersonBase,tests/test_read_with_orm_mode.py,23
  tests/test_validate_response::Item,extends,BaseModel,tests/test_validate_response.py,12
  tests/test_security_api_key_header::User,extends,BaseModel,tests/test_security_api_key_header.py,12
  tests/test_additional_responses_union_duplicate_anyof::ModelA,extends,BaseModel,tests/test_additional_responses_union_duplicate_anyof.py,15
  tests/test_additional_responses_union_duplicate_anyof::ModelB,extends,BaseModel,tests/test_additional_responses_union_duplicate_anyof.py,19
  tests/test_additional_responses_custom_model_in_callback::CustomModel,extends,BaseModel,tests/test_additional_responses_custom_model_in_callback.py,8
  tests/test_generate_unique_id_function::Item,extends,BaseModel,tests/test_generate_unique_id_function.py,22
  tests/test_generate_unique_id_function::Message,extends,BaseModel,tests/test_generate_unique_id_function.py,27
  tests/test_pydantic_v1_error::ParamModelV1,extends,BaseModel,tests/test_pydantic_v1_error.py,21
  tests/test_pydantic_v1_error::ReturnModelV1,extends,BaseModel,tests/test_pydantic_v1_error.py,34
  tests/test_pydantic_v1_error::ResponseModelV1,extends,BaseModel,tests/test_pydantic_v1_error.py,47
  tests/test_pydantic_v1_error::ErrorModelV1,extends,BaseModel,tests/test_pydantic_v1_error.py,60
  tests/test_pydantic_v1_error::ModelV1A,extends,BaseModel,tests/test_pydantic_v1_error.py,75
  tests/test_pydantic_v1_error::ModelV1A,extends,BaseModel,tests/test_pydantic_v1_error.py,88
  tests/test_forms_single_model::FormModel,extends,BaseModel,tests/test_forms_single_model.py,10
  tests/test_forms_single_model::FormModelExtraAllow,extends,BaseModel,tests/test_forms_single_model.py,18
  tests/test_security_openid_connect_optional::User,extends,BaseModel,tests/test_security_openid_connect_optional.py,14
  tests/test_response_model_data_filter_no_inheritance::UserCreate,extends,BaseModel,tests/test_response_model_data_filter_no_inheritance.py,8
  tests/test_response_model_data_filter_no_inheritance::UserDB,extends,BaseModel,tests/test_response_model_data_filter_no_inheritance.py,13
  tests/test_response_model_data_filter_no_inheritance::User,extends,BaseModel,tests/test_response_model_data_filter_no_inheritance.py,18
  tests/test_response_model_data_filter_no_inheritance::PetDB,extends,BaseModel,tests/test_response_model_data_filter_no_inheritance.py,22
  tests/test_response_model_data_filter_no_inheritance::PetOut,extends,BaseModel,tests/test_response_model_data_filter_no_inheritance.py,27
  tests/test_response_by_alias::Model,extends,BaseModel,tests/test_response_by_alias.py,9
  tests/test_response_by_alias::ModelNoAlias,extends,BaseModel,tests/test_response_by_alias.py,13
  tests/test_validation_error_context::Item,extends,BaseModel,tests/test_validation_error_context.py,11
  tests/test_duplicate_models_openapi::Model,extends,BaseModel,tests/test_duplicate_models_openapi.py,9
  tests/test_duplicate_models_openapi::Model2,extends,BaseModel,tests/test_duplicate_models_openapi.py,13
  tests/test_duplicate_models_openapi::Model3,extends,BaseModel,tests/test_duplicate_models_openapi.py,17
  tests/test_security_api_key_query::User,extends,BaseModel,tests/test_security_api_key_query.py,12
  tests/test_security_api_key_query_description::User,extends,BaseModel,tests/test_security_api_key_query_description.py,12
  tests/test_response_code_no_body::JsonApiResponse,extends,JSONResponse,tests/test_response_code_no_body.py,10
  tests/test_response_code_no_body::Error,extends,BaseModel,tests/test_response_code_no_body.py,14
  tests/test_response_code_no_body::JsonApiError,extends,BaseModel,tests/test_response_code_no_body.py,19
  tests/test_additional_properties_bool::FooBaseModel,extends,BaseModel,tests/test_additional_properties_bool.py,9
  tests/test_additional_properties_bool::Foo,extends,FooBaseModel,tests/test_additional_properties_bool.py,13
  tests/test_security_oauth2_optional_description::User,extends,BaseModel,tests/test_security_oauth2_optional_description.py,24
  tests/test_webhooks_security::Subscription,extends,BaseModel,tests/test_webhooks_security.py,15
  tests/test_jsonable_encoder::DictablePerson,extends,Person,tests/test_jsonable_encoder.py,35
  tests/test_jsonable_encoder::DictablePet,extends,Pet,tests/test_jsonable_encoder.py,40
  tests/test_jsonable_encoder::ModelWithConfig,extends,BaseModel,tests/test_jsonable_encoder.py,59
  tests/test_jsonable_encoder::ModelWithAlias,extends,BaseModel,tests/test_jsonable_encoder.py,65
  tests/test_jsonable_encoder::ModelWithDefault,extends,BaseModel,tests/test_jsonable_encoder.py,69
  tests/test_jsonable_encoder::ModelWithCustomEncoder,extends,BaseModel,tests/test_jsonable_encoder.py,143
  tests/test_jsonable_encoder::ModelWithCustomEncoderSubclass,extends,ModelWithCustomEncoder,tests/test_jsonable_encoder.py,150
  tests/test_jsonable_encoder::ModelV1,extends,v1.BaseModel,tests/test_jsonable_encoder.py,164
  tests/test_jsonable_encoder::safe_datetime,extends,datetime,tests/test_jsonable_encoder.py,206
  tests/test_jsonable_encoder::ModelWithPath,extends,BaseModel,tests/test_jsonable_encoder.py,244
  tests/test_jsonable_encoder::ModelWithPath,extends,BaseModel,tests/test_jsonable_encoder.py,255
  tests/test_jsonable_encoder::ModelWithPath,extends,BaseModel,tests/test_jsonable_encoder.py,265
  tests/test_jsonable_encoder::Model,extends,BaseModel,tests/test_jsonable_encoder.py,303
  tests/test_additional_responses_custom_validationerror::JsonApiResponse,extends,JSONResponse,tests/test_additional_responses_custom_validationerror.py,10
  tests/test_additional_responses_custom_validationerror::Error,extends,BaseModel,tests/test_additional_responses_custom_validationerror.py,14
  tests/test_additional_responses_custom_validationerror::JsonApiError,extends,BaseModel,tests/test_additional_responses_custom_validationerror.py,19
  tests/test_tuples::ItemGroup,extends,BaseModel,tests/test_tuples.py,9
  tests/test_tuples::Coordinate,extends,BaseModel,tests/test_tuples.py,13
  tests/test_custom_route_class::APIRouteA,extends,APIRoute,tests/test_custom_route_class.py,11
  tests/test_custom_route_class::APIRouteB,extends,APIRoute,tests/test_custom_route_class.py,15
  tests/test_custom_route_class::APIRouteC,extends,APIRoute,tests/test_custom_route_class.py,19
  tests/test_union_body::Item,extends,BaseModel,tests/test_union_body.py,11
  tests/test_union_body::OtherItem,extends,BaseModel,tests/test_union_body.py,15
  tests/benchmarks/test_general_performance::ItemIn,extends,BaseModel,tests/benchmarks/test_general_performance.py,49
  tests/benchmarks/test_general_performance::ItemOut,extends,BaseModel,tests/benchmarks/test_general_performance.py,54
  tests/benchmarks/test_general_performance::LargeIn,extends,BaseModel,tests/benchmarks/test_general_performance.py,60
  tests/benchmarks/test_general_performance::LargeOut,extends,BaseModel,tests/benchmarks/test_general_performance.py,65
  tests/test_dependency_duplicates::Item,extends,BaseModel,tests/test_dependency_duplicates.py,11
  tests/test_security_api_key_header_description::User,extends,BaseModel,tests/test_security_api_key_header_description.py,12
  tests/test_security_oauth2_optional::User,extends,BaseModel,tests/test_security_oauth2_optional.py,23
  tests/test_default_response_class::ORJSONResponse,extends,JSONResponse,tests/test_default_response_class.py,9
  tests/test_default_response_class::OverrideResponse,extends,JSONResponse,tests/test_default_response_class.py,16
  tests/test_router_events::State,extends,BaseModel,tests/test_router_events.py,11
  tests/test_compat::EmbeddedModel,extends,BaseModel,tests/test_compat.py,50
  tests/test_compat::Model,extends,BaseModel,tests/test_compat.py,54
  tests/test_additional_responses_response_class::JsonApiResponse,extends,JSONResponse,tests/test_additional_responses_response_class.py,10
  tests/test_additional_responses_response_class::Error,extends,BaseModel,tests/test_additional_responses_response_class.py,14
  tests/test_additional_responses_response_class::JsonApiError,extends,BaseModel,tests/test_additional_responses_response_class.py,19
  tests/test_additional_responses_router::ResponseModel,extends,BaseModel,tests/test_additional_responses_router.py,7
  tests/test_validate_response_recursive/app::RecursiveItem,extends,BaseModel,tests/test_validate_response_recursive/app.py,7
  tests/test_validate_response_recursive/app::RecursiveSubitemInSubmodel,extends,BaseModel,tests/test_validate_response_recursive/app.py,12
  tests/test_validate_response_recursive/app::RecursiveItemViaSubmodel,extends,BaseModel,tests/test_validate_response_recursive/app.py,17
  tests/test_custom_schema_fields::Item,extends,BaseModel,tests/test_custom_schema_fields.py,10
  tests/test_request_param_model_by_alias::Model,extends,BaseModel,tests/test_request_param_model_by_alias.py,9
  tests/test_serialize_response::Item,extends,BaseModel,tests/test_serialize_response.py,10
  tests/test_no_schema_split::MessageEventType,extends,str,tests/test_no_schema_split.py,13
  tests/test_no_schema_split::MessageEvent,extends,BaseModel,tests/test_no_schema_split.py,18
  tests/test_no_schema_split::MessageOutput,extends,BaseModel,tests/test_no_schema_split.py,23
  tests/test_no_schema_split::Message,extends,BaseModel,tests/test_no_schema_split.py,28
  tests/test_union_body_discriminator::FirstItem,extends,BaseModel,tests/test_union_body_discriminator.py,15
  tests/test_union_body_discriminator::OtherItem,extends,BaseModel,tests/test_union_body_discriminator.py,19
  tests/test_openapi_separate_input_output_schemas::SubItem,extends,BaseModel,tests/test_openapi_separate_input_output_schemas.py,9
  tests/test_openapi_separate_input_output_schemas::Item,extends,BaseModel,tests/test_openapi_separate_input_output_schemas.py,16
  tests/test_openapi_separate_input_output_schemas::WithComputedField,extends,BaseModel,tests/test_openapi_separate_input_output_schemas.py,23
  tests/test_filter_pydantic_sub_model_pv2::ModelB,extends,BaseModel,tests/test_filter_pydantic_sub_model_pv2.py,17
  tests/test_filter_pydantic_sub_model_pv2::ModelC,extends,ModelB,tests/test_filter_pydantic_sub_model_pv2.py,20
  tests/test_filter_pydantic_sub_model_pv2::ModelA,extends,BaseModel,tests/test_filter_pydantic_sub_model_pv2.py,23
  tests/test_query_cookie_header_model_extra_params::Model,extends,BaseModel,tests/test_query_cookie_header_model_extra_params.py,8
  tests/test_sub_callbacks::Invoice,extends,BaseModel,tests/test_sub_callbacks.py,11
  tests/test_sub_callbacks::InvoiceEvent,extends,BaseModel,tests/test_sub_callbacks.py,18
  tests/test_sub_callbacks::InvoiceEventReceived,extends,BaseModel,tests/test_sub_callbacks.py,23
  tests/test_sub_callbacks::Event,extends,BaseModel,tests/test_sub_callbacks.py,37
  tests/test_response_model_data_filter::UserBase,extends,BaseModel,tests/test_response_model_data_filter.py,8
  tests/test_response_model_data_filter::UserCreate,extends,UserBase,tests/test_response_model_data_filter.py,12
  tests/test_response_model_data_filter::UserDB,extends,UserBase,tests/test_response_model_data_filter.py,16
  tests/test_response_model_data_filter::PetDB,extends,BaseModel,tests/test_response_model_data_filter.py,20
  tests/test_response_model_data_filter::PetOut,extends,BaseModel,tests/test_response_model_data_filter.py,25
  tests/test_security_api_key_query_optional::User,extends,BaseModel,tests/test_security_api_key_query_optional.py,14
  tests/test_include_router_defaults_overrides::ResponseLevel0,extends,JSONResponse,tests/test_include_router_defaults_overrides.py,10
  tests/test_include_router_defaults_overrides::ResponseLevel1,extends,JSONResponse,tests/test_include_router_defaults_overrides.py,14
  tests/test_include_router_defaults_overrides::ResponseLevel2,extends,JSONResponse,tests/test_include_router_defaults_overrides.py,18
  tests/test_include_router_defaults_overrides::ResponseLevel3,extends,JSONResponse,tests/test_include_router_defaults_overrides.py,22
  tests/test_include_router_defaults_overrides::ResponseLevel4,extends,JSONResponse,tests/test_include_router_defaults_overrides.py,26
  tests/test_include_router_defaults_overrides::ResponseLevel5,extends,JSONResponse,tests/test_include_router_defaults_overrides.py,30
  tests/test_skip_defaults::SubModel,extends,BaseModel,tests/test_skip_defaults.py,10
  tests/test_skip_defaults::Model,extends,BaseModel,tests/test_skip_defaults.py,14
  tests/test_skip_defaults::ModelSubclass,extends,Model,tests/test_skip_defaults.py,19
  tests/test_skip_defaults::ModelDefaults,extends,BaseModel,tests/test_skip_defaults.py,25
  tests/test_extra_routes::Item,extends,BaseModel,tests/test_extra_routes.py,12
  tests/test_security_api_key_cookie::User,extends,BaseModel,tests/test_security_api_key_cookie.py,12
  tests/test_serialize_response_model::Item,extends,BaseModel,tests/test_serialize_response_model.py,10
  tests/test_additional_properties::Items,extends,BaseModel,tests/test_additional_properties.py,9
  tests/test_security_openid_connect::User,extends,BaseModel,tests/test_security_openid_connect.py,12
  tests/test_response_model_include_exclude::Model1,extends,BaseModel,tests/test_response_model_include_exclude.py,6
  tests/test_response_model_include_exclude::Model2,extends,BaseModel,tests/test_response_model_include_exclude.py,11
  tests/test_response_model_include_exclude::Model3,extends,BaseModel,tests/test_response_model_include_exclude.py,16
  tests/test_get_model_definitions_formfeed_escape::Address,extends,BaseModel,tests/test_get_model_definitions_formfeed_escape.py,11
  tests/test_get_model_definitions_formfeed_escape::Facility,extends,BaseModel,tests/test_get_model_definitions_formfeed_escape.py,22
  tests/test_response_model_default_factory::ResponseModel,extends,BaseModel,tests/test_response_model_default_factory.py,8
  tests/test_response_class_no_mediatype::JsonApiResponse,extends,JSONResponse,tests/test_response_class_no_mediatype.py,10
  tests/test_response_class_no_mediatype::Error,extends,BaseModel,tests/test_response_class_no_mediatype.py,14
  tests/test_response_class_no_mediatype::JsonApiError,extends,BaseModel,tests/test_response_class_no_mediatype.py,19
  tests/test_openapi_model_description_trim_on_formfeed::MyModel,extends,BaseModel,tests/test_openapi_model_description_trim_on_formfeed.py,8
  tests/test_security_api_key_cookie_description::User,extends,BaseModel,tests/test_security_api_key_cookie_description.py,12
  tests/test_openapi_examples::Item,extends,BaseModel,tests/test_openapi_examples.py,11
  tests/test_request_body_parameters_media_type::Product,extends,BaseModel,tests/test_request_body_parameters_media_type.py,13
  tests/test_request_body_parameters_media_type::Shop,extends,BaseModel,tests/test_request_body_parameters_media_type.py,18
  tests/test_security_api_key_header_optional::User,extends,BaseModel,tests/test_security_api_key_header_optional.py,14
  fastapi/params::Param,extends,FieldInfo,fastapi/params.py,27
  fastapi/params::Path,extends,Param,fastapi/params.py,138
  fastapi/params::Query,extends,Param,fastapi/params.py,222
  fastapi/params::Header,extends,Param,fastapi/params.py,304
  fastapi/params::Cookie,extends,Param,fastapi/params.py,388
  fastapi/params::Body,extends,FieldInfo,fastapi/params.py,470
  fastapi/params::Form,extends,Body,fastapi/params.py,582
  fastapi/params::File,extends,Form,fastapi/params.py,664
  fastapi/params::Security,extends,Depends,fastapi/params.py,754
  fastapi/responses::UJSONResponse,extends,JSONResponse,fastapi/responses.py,23
  fastapi/responses::ORJSONResponse,extends,JSONResponse,fastapi/responses.py,36
  fastapi/security/open_id_connect_url::OpenIdConnect,extends,SecurityBase,fastapi/security/open_id_connect_url.py,11
  fastapi/security/oauth2::OAuth2PasswordRequestFormStrict,extends,OAuth2PasswordRequestForm,fastapi/security/oauth2.py,162
  fastapi/security/oauth2::OAuth2,extends,SecurityBase,fastapi/security/oauth2.py,330
  fastapi/security/oauth2::OAuth2PasswordBearer,extends,OAuth2,fastapi/security/oauth2.py,433
  fastapi/security/oauth2::OAuth2AuthorizationCodeBearer,extends,OAuth2,fastapi/security/oauth2.py,547
  fastapi/security/api_key::APIKeyBase,extends,SecurityBase,fastapi/security/api_key.py,11
  fastapi/security/api_key::APIKeyQuery,extends,APIKeyBase,fastapi/security/api_key.py,53
  fastapi/security/api_key::APIKeyHeader,extends,APIKeyBase,fastapi/security/api_key.py,145
  fastapi/security/api_key::APIKeyCookie,extends,APIKeyBase,fastapi/security/api_key.py,233
  fastapi/security/http::HTTPBasicCredentials,extends,BaseModel,fastapi/security/http.py,16
  fastapi/security/http::HTTPAuthorizationCredentials,extends,BaseModel,fastapi/security/http.py,29
  fastapi/security/http::HTTPBase,extends,SecurityBase,fastapi/security/http.py,69
  fastapi/security/http::HTTPBasic,extends,HTTPBase,fastapi/security/http.py,105
  fastapi/security/http::HTTPBearer,extends,HTTPBase,fastapi/security/http.py,222
  fastapi/security/http::HTTPDigest,extends,HTTPBase,fastapi/security/http.py,319
  fastapi/applications::FastAPI,extends,Starlette,fastapi/applications.py,45
  fastapi/background::BackgroundTasks,extends,StarletteBackgroundTasks,fastapi/background.py,11
  fastapi/openapi/models::EmailStr,extends,str,fastapi/openapi/models.py,23
  fastapi/openapi/models::BaseModelWithConfig,extends,BaseModel,fastapi/openapi/models.py,57
  fastapi/openapi/models::Contact,extends,BaseModelWithConfig,fastapi/openapi/models.py,61
  fastapi/openapi/models::License,extends,BaseModelWithConfig,fastapi/openapi/models.py,67
  fastapi/openapi/models::Info,extends,BaseModelWithConfig,fastapi/openapi/models.py,73
  fastapi/openapi/models::ServerVariable,extends,BaseModelWithConfig,fastapi/openapi/models.py,83
  fastapi/openapi/models::Server,extends,BaseModelWithConfig,fastapi/openapi/models.py,89
  fastapi/openapi/models::Reference,extends,BaseModel,fastapi/openapi/models.py,95
  fastapi/openapi/models::Discriminator,extends,BaseModel,fastapi/openapi/models.py,99
  fastapi/openapi/models::XML,extends,BaseModelWithConfig,fastapi/openapi/models.py,104
  fastapi/openapi/models::ExternalDocumentation,extends,BaseModelWithConfig,fastapi/openapi/models.py,112
  fastapi/openapi/models::Schema,extends,BaseModelWithConfig,fastapi/openapi/models.py,123
  fastapi/openapi/models::Example,extends,total=False,fastapi/openapi/models.py,212
  fastapi/openapi/models::Encoding,extends,BaseModelWithConfig,fastapi/openapi/models.py,228
  fastapi/openapi/models::MediaType,extends,BaseModelWithConfig,fastapi/openapi/models.py,236
  fastapi/openapi/models::ParameterBase,extends,BaseModelWithConfig,fastapi/openapi/models.py,243
  fastapi/openapi/models::Parameter,extends,ParameterBase,fastapi/openapi/models.py,258
  fastapi/openapi/models::Header,extends,ParameterBase,fastapi/openapi/models.py,263
  fastapi/openapi/models::RequestBody,extends,BaseModelWithConfig,fastapi/openapi/models.py,267
  fastapi/openapi/models::Link,extends,BaseModelWithConfig,fastapi/openapi/models.py,273
  fastapi/openapi/models::Response,extends,BaseModelWithConfig,fastapi/openapi/models.py,282
  fastapi/openapi/models::Operation,extends,BaseModelWithConfig,fastapi/openapi/models.py,289
  fastapi/openapi/models::PathItem,extends,BaseModelWithConfig,fastapi/openapi/models.py,305
  fastapi/openapi/models::SecurityBase,extends,BaseModelWithConfig,fastapi/openapi/models.py,328
  fastapi/openapi/models::APIKey,extends,SecurityBase,fastapi/openapi/models.py,339
  fastapi/openapi/models::HTTPBase,extends,SecurityBase,fastapi/openapi/models.py,345
  fastapi/openapi/models::HTTPBearer,extends,HTTPBase,fastapi/openapi/models.py,350
  fastapi/openapi/models::OAuthFlow,extends,BaseModelWithConfig,fastapi/openapi/models.py,355
  fastapi/openapi/models::OAuthFlowImplicit,extends,OAuthFlow,fastapi/openapi/models.py,360
  fastapi/openapi/models::OAuthFlowPassword,extends,OAuthFlow,fastapi/openapi/models.py,364
  fastapi/openapi/models::OAuthFlowClientCredentials,extends,OAuthFlow,fastapi/openapi/models.py,368
  fastapi/openapi/models::OAuthFlowAuthorizationCode,extends,OAuthFlow,fastapi/openapi/models.py,372
  fastapi/openapi/models::OAuthFlows,extends,BaseModelWithConfig,fastapi/openapi/models.py,377
  fastapi/openapi/models::OAuth2,extends,SecurityBase,fastapi/openapi/models.py,384
  fastapi/openapi/models::OpenIdConnect,extends,SecurityBase,fastapi/openapi/models.py,389
  fastapi/openapi/models::Components,extends,BaseModelWithConfig,fastapi/openapi/models.py,399
  fastapi/openapi/models::Tag,extends,BaseModelWithConfig,fastapi/openapi/models.py,413
  fastapi/openapi/models::OpenAPI,extends,BaseModelWithConfig,fastapi/openapi/models.py,419
  fastapi/routing::_AsyncLiftContextManager,extends,AbstractAsyncContextManager,fastapi/routing.py,154
  fastapi/routing::APIWebSocketRoute,extends,routing.WebSocketRoute,fastapi/routing.py,512
  fastapi/routing::APIRoute,extends,routing.Route,fastapi/routing.py,554
  fastapi/routing::APIRouter,extends,routing.Router,fastapi/routing.py,708
  fastapi/exceptions::EndpointContext,extends,total=False,fastapi/exceptions.py,10
  fastapi/exceptions::HTTPException,extends,StarletteHTTPException,fastapi/exceptions.py,17
  fastapi/exceptions::WebSocketException,extends,StarletteWebSocketException,fastapi/exceptions.py,86
  fastapi/exceptions::DependencyScopeError,extends,FastAPIError,fastapi/exceptions.py,167
  fastapi/exceptions::RequestValidationError,extends,ValidationException,fastapi/exceptions.py,212
  fastapi/exceptions::WebSocketRequestValidationError,extends,ValidationException,fastapi/exceptions.py,224
  fastapi/exceptions::ResponseValidationError,extends,ValidationException,fastapi/exceptions.py,234
  fastapi/exceptions::PydanticV1NotSupportedError,extends,FastAPIError,fastapi/exceptions.py,246
  fastapi/exceptions::FastAPIDeprecationWarning,extends,UserWarning,fastapi/exceptions.py,252
  fastapi/datastructures::UploadFile,extends,StarletteUploadFile,fastapi/datastructures.py,21
  scripts/contributors::Author,extends,BaseModel,scripts/contributors.py,59
  scripts/contributors::LabelNode,extends,BaseModel,scripts/contributors.py,65
  scripts/contributors::Labels,extends,BaseModel,scripts/contributors.py,69
  scripts/contributors::ReviewNode,extends,BaseModel,scripts/contributors.py,73
  scripts/contributors::Reviews,extends,BaseModel,scripts/contributors.py,78
  scripts/contributors::PullRequestNode,extends,BaseModel,scripts/contributors.py,82
  scripts/contributors::PullRequestEdge,extends,BaseModel,scripts/contributors.py,94
  scripts/contributors::PullRequests,extends,BaseModel,scripts/contributors.py,99
  scripts/contributors::PRsRepository,extends,BaseModel,scripts/contributors.py,103
  scripts/contributors::PRsResponseData,extends,BaseModel,scripts/contributors.py,107
  scripts/contributors::PRsResponse,extends,BaseModel,scripts/contributors.py,111
  scripts/contributors::Settings,extends,BaseSettings,scripts/contributors.py,115
  scripts/contributors::ContributorsResults,extends,BaseModel,scripts/contributors.py,168
  scripts/label_approved::LabelSettings,extends,BaseModel,scripts/label_approved.py,10
  scripts/label_approved::Settings,extends,BaseSettings,scripts/label_approved.py,18
  scripts/notify_translations::Comment,extends,BaseModel,scripts/notify_translations.py,87
  scripts/notify_translations::UpdateDiscussionComment,extends,BaseModel,scripts/notify_translations.py,93
  scripts/notify_translations::UpdateCommentData,extends,BaseModel,scripts/notify_translations.py,97
  scripts/notify_translations::UpdateCommentResponse,extends,BaseModel,scripts/notify_translations.py,101
  scripts/notify_translations::AddDiscussionComment,extends,BaseModel,scripts/notify_translations.py,105
  scripts/notify_translations::AddCommentData,extends,BaseModel,scripts/notify_translations.py,109
  scripts/notify_translations::AddCommentResponse,extends,BaseModel,scripts/notify_translations.py,113
  scripts/notify_translations::CommentsEdge,extends,BaseModel,scripts/notify_translations.py,117
  scripts/notify_translations::Comments,extends,BaseModel,scripts/notify_translations.py,122
  scripts/notify_translations::CommentsDiscussion,extends,BaseModel,scripts/notify_translations.py,126
  scripts/notify_translations::CommentsRepository,extends,BaseModel,scripts/notify_translations.py,130
  scripts/notify_translations::CommentsData,extends,BaseModel,scripts/notify_translations.py,134
  scripts/notify_translations::CommentsResponse,extends,BaseModel,scripts/notify_translations.py,138
  scripts/notify_translations::AllDiscussionsLabelNode,extends,BaseModel,scripts/notify_translations.py,142
  scripts/notify_translations::AllDiscussionsLabelsEdge,extends,BaseModel,scripts/notify_translations.py,147
  scripts/notify_translations::AllDiscussionsDiscussionLabels,extends,BaseModel,scripts/notify_translations.py,151
  scripts/notify_translations::AllDiscussionsDiscussionNode,extends,BaseModel,scripts/notify_translations.py,155
  scripts/notify_translations::AllDiscussionsDiscussions,extends,BaseModel,scripts/notify_translations.py,162
  scripts/notify_translations::AllDiscussionsRepository,extends,BaseModel,scripts/notify_translations.py,166
  scripts/notify_translations::AllDiscussionsData,extends,BaseModel,scripts/notify_translations.py,170
  scripts/notify_translations::AllDiscussionsResponse,extends,BaseModel,scripts/notify_translations.py,174
  scripts/notify_translations::Settings,extends,BaseSettings,scripts/notify_translations.py,178
  scripts/notify_translations::PartialGitHubEventIssue,extends,BaseModel,scripts/notify_translations.py,190
  scripts/notify_translations::PartialGitHubEvent,extends,BaseModel,scripts/notify_translations.py,194
  scripts/sponsors::SponsorEntity,extends,BaseModel,scripts/sponsors.py,48
  scripts/sponsors::Tier,extends,BaseModel,scripts/sponsors.py,54
  scripts/sponsors::SponsorshipAsMaintainerNode,extends,BaseModel,scripts/sponsors.py,59
  scripts/sponsors::SponsorshipAsMaintainerEdge,extends,BaseModel,scripts/sponsors.py,64
  scripts/sponsors::SponsorshipAsMaintainer,extends,BaseModel,scripts/sponsors.py,69
  scripts/sponsors::SponsorsUser,extends,BaseModel,scripts/sponsors.py,73
  scripts/sponsors::SponsorsResponseData,extends,BaseModel,scripts/sponsors.py,77
  scripts/sponsors::SponsorsResponse,extends,BaseModel,scripts/sponsors.py,81
  scripts/sponsors::Settings,extends,BaseSettings,scripts/sponsors.py,85
  scripts/docs::VisibleTextExtractor,extends,HTMLParser,scripts/docs.py,69
  scripts/mkdocs_hooks::EnFile,extends,File,scripts/mkdocs_hooks.py,48
  scripts/people::Author,extends,BaseModel,scripts/people.py,65
  scripts/people::CommentsNode,extends,BaseModel,scripts/people.py,71
  scripts/people::Replies,extends,BaseModel,scripts/people.py,76
  scripts/people::DiscussionsCommentsNode,extends,CommentsNode,scripts/people.py,81
  scripts/people::DiscussionsComments,extends,BaseModel,scripts/people.py,85
  scripts/people::DiscussionsNode,extends,BaseModel,scripts/people.py,90
  scripts/people::DiscussionsEdge,extends,BaseModel,scripts/people.py,98
  scripts/people::Discussions,extends,BaseModel,scripts/people.py,103
  scripts/people::DiscussionsRepository,extends,BaseModel,scripts/people.py,107
  scripts/people::DiscussionsResponseData,extends,BaseModel,scripts/people.py,111
  scripts/people::DiscussionsResponse,extends,BaseModel,scripts/people.py,115
  scripts/people::Settings,extends,BaseSettings,scripts/people.py,119
  scripts/people::DiscussionExpertsResults,extends,BaseModel,scripts/people.py,171
  scripts/deploy_docs_status::Settings,extends,BaseSettings,scripts/deploy_docs_status.py,10
  scripts/deploy_docs_status::LinkData,extends,BaseModel,scripts/deploy_docs_status.py,19
  scripts/topic_repos::Settings,extends,BaseSettings,scripts/topic_repos.py,12
  scripts/topic_repos::Repo,extends,BaseModel,scripts/topic_repos.py,17
  docs_src/settings/app01_py39/config::Settings,extends,BaseSettings,docs_src/settings/app01_py39/config.py,4
  docs_src/settings/tutorial001_py310::Settings,extends,BaseSettings,docs_src/settings/tutorial001_py310.py,5
  docs_src/settings/app02_py310/config::Settings,extends,BaseSettings,docs_src/settings/app02_py310/config.py,4
  docs_src/settings/app03_py39/config::Settings,extends,BaseSettings,docs_src/settings/app03_py39/config.py,4
  docs_src/settings/app02_an_py39/config::Settings,extends,BaseSettings,docs_src/settings/app02_an_py39/config.py,4
  docs_src/settings/app03_an_py39/config::Settings,extends,BaseSettings,docs_src/settings/app03_an_py39/config.py,4
  docs_src/settings/app02_py39/config::Settings,extends,BaseSettings,docs_src/settings/app02_py39/config.py,4
  docs_src/settings/app01_py310/config::Settings,extends,BaseSettings,docs_src/settings/app01_py310/config.py,4
  docs_src/settings/app02_an_py310/config::Settings,extends,BaseSettings,docs_src/settings/app02_an_py310/config.py,4
  docs_src/settings/app03_an_py310/config::Settings,extends,BaseSettings,docs_src/settings/app03_an_py310/config.py,4
  docs_src/settings/tutorial001_py39::Settings,extends,BaseSettings,docs_src/settings/tutorial001_py39.py,5
  docs_src/settings/app03_py310/config::Settings,extends,BaseSettings,docs_src/settings/app03_py310/config.py,4
  docs_src/conditional_openapi/tutorial001_py310::Settings,extends,BaseSettings,docs_src/conditional_openapi/tutorial001_py310.py,5
  docs_src/conditional_openapi/tutorial001_py39::Settings,extends,BaseSettings,docs_src/conditional_openapi/tutorial001_py39.py,5
  docs_src/authentication_error_status_code/tutorial001_an_py39::HTTPBearer403,extends,HTTPBearer,docs_src/authentication_error_status_code/tutorial001_an_py39.py,9
  docs_src/authentication_error_status_code/tutorial001_an_py310::HTTPBearer403,extends,HTTPBearer,docs_src/authentication_error_status_code/tutorial001_an_py310.py,9
  docs_src/body_multiple_params/tutorial004_an_py310::Item,extends,BaseModel,docs_src/body_multiple_params/tutorial004_an_py310.py,9
  docs_src/body_multiple_params/tutorial004_an_py310::User,extends,BaseModel,docs_src/body_multiple_params/tutorial004_an_py310.py,16
  docs_src/body_multiple_params/tutorial001_py310::Item,extends,BaseModel,docs_src/body_multiple_params/tutorial001_py310.py,7
  docs_src/body_multiple_params/tutorial001_an_py310::Item,extends,BaseModel,docs_src/body_multiple_params/tutorial001_an_py310.py,9
  docs_src/body_multiple_params/tutorial005_py310::Item,extends,BaseModel,docs_src/body_multiple_params/tutorial005_py310.py,7
  docs_src/body_multiple_params/tutorial004_py310::Item,extends,BaseModel,docs_src/body_multiple_params/tutorial004_py310.py,7
  docs_src/body_multiple_params/tutorial004_py310::User,extends,BaseModel,docs_src/body_multiple_params/tutorial004_py310.py,14
  docs_src/body_multiple_params/tutorial003_an_py310::Item,extends,BaseModel,docs_src/body_multiple_params/tutorial003_an_py310.py,9
  docs_src/body_multiple_params/tutorial003_an_py310::User,extends,BaseModel,docs_src/body_multiple_params/tutorial003_an_py310.py,16
  docs_src/body_multiple_params/tutorial002_py310::Item,extends,BaseModel,docs_src/body_multiple_params/tutorial002_py310.py,7
  docs_src/body_multiple_params/tutorial002_py310::User,extends,BaseModel,docs_src/body_multiple_params/tutorial002_py310.py,14
  docs_src/body_multiple_params/tutorial003_py310::Item,extends,BaseModel,docs_src/body_multiple_params/tutorial003_py310.py,7
  docs_src/body_multiple_params/tutorial003_py310::User,extends,BaseModel,docs_src/body_multiple_params/tutorial003_py310.py,14
  docs_src/body_multiple_params/tutorial005_an_py310::Item,extends,BaseModel,docs_src/body_multiple_params/tutorial005_an_py310.py,9
  docs_src/body_nested_models/tutorial006_py310::Image,extends,BaseModel,docs_src/body_nested_models/tutorial006_py310.py,7
  docs_src/body_nested_models/tutorial006_py310::Item,extends,BaseModel,docs_src/body_nested_models/tutorial006_py310.py,12
  docs_src/body_nested_models/tutorial007_py310::Image,extends,BaseModel,docs_src/body_nested_models/tutorial007_py310.py,7
  docs_src/body_nested_models/tutorial007_py310::Item,extends,BaseModel,docs_src/body_nested_models/tutorial007_py310.py,12
  docs_src/body_nested_models/tutorial007_py310::Offer,extends,BaseModel,docs_src/body_nested_models/tutorial007_py310.py,21
  docs_src/body_nested_models/tutorial001_py310::Item,extends,BaseModel,docs_src/body_nested_models/tutorial001_py310.py,7
  docs_src/body_nested_models/tutorial005_py310::Image,extends,BaseModel,docs_src/body_nested_models/tutorial005_py310.py,7
  docs_src/body_nested_models/tutorial005_py310::Item,extends,BaseModel,docs_src/body_nested_models/tutorial005_py310.py,12
  docs_src/body_nested_models/tutorial004_py310::Image,extends,BaseModel,docs_src/body_nested_models/tutorial004_py310.py,7
  docs_src/body_nested_models/tutorial004_py310::Item,extends,BaseModel,docs_src/body_nested_models/tutorial004_py310.py,12
  docs_src/body_nested_models/tutorial002_py310::Item,extends,BaseModel,docs_src/body_nested_models/tutorial002_py310.py,7
  docs_src/body_nested_models/tutorial003_py310::Item,extends,BaseModel,docs_src/body_nested_models/tutorial003_py310.py,7
  docs_src/body_nested_models/tutorial008_py39::Image,extends,BaseModel,docs_src/body_nested_models/tutorial008_py39.py,7
  docs_src/body_nested_models/tutorial008_py310::Image,extends,BaseModel,docs_src/body_nested_models/tutorial008_py310.py,7
  docs_src/openapi_callbacks/tutorial001_py310::Invoice,extends,BaseModel,docs_src/openapi_callbacks/tutorial001_py310.py,7
  docs_src/openapi_callbacks/tutorial001_py310::InvoiceEvent,extends,BaseModel,docs_src/openapi_callbacks/tutorial001_py310.py,14
  docs_src/openapi_callbacks/tutorial001_py310::InvoiceEventReceived,extends,BaseModel,docs_src/openapi_callbacks/tutorial001_py310.py,19
  docs_src/response_model/tutorial006_py310::Item,extends,BaseModel,docs_src/response_model/tutorial006_py310.py,7
  docs_src/response_model/tutorial001_py310::Item,extends,BaseModel,docs_src/response_model/tutorial001_py310.py,9
  docs_src/response_model/tutorial001_01_py310::Item,extends,BaseModel,docs_src/response_model/tutorial001_01_py310.py,7
  docs_src/response_model/tutorial005_py310::Item,extends,BaseModel,docs_src/response_model/tutorial005_py310.py,7
  docs_src/response_model/tutorial004_py310::Item,extends,BaseModel,docs_src/response_model/tutorial004_py310.py,7
  docs_src/response_model/tutorial003_01_py310::BaseUser,extends,BaseModel,docs_src/response_model/tutorial003_01_py310.py,7
  docs_src/response_model/tutorial003_01_py310::UserIn,extends,BaseUser,docs_src/response_model/tutorial003_01_py310.py,13
  docs_src/response_model/tutorial002_py310::UserIn,extends,BaseModel,docs_src/response_model/tutorial002_py310.py,7
  docs_src/response_model/tutorial003_py310::UserIn,extends,BaseModel,docs_src/response_model/tutorial003_py310.py,9
  docs_src/response_model/tutorial003_py310::UserOut,extends,BaseModel,docs_src/response_model/tutorial003_py310.py,16
  docs_src/python_types/tutorial011_py310::User,extends,BaseModel,docs_src/python_types/tutorial011_py310.py,6
  docs_src/cookie_param_models/tutorial002_an_py310::Cookies,extends,BaseModel,docs_src/cookie_param_models/tutorial002_an_py310.py,9
  docs_src/cookie_param_models/tutorial001_py310::Cookies,extends,BaseModel,docs_src/cookie_param_models/tutorial001_py310.py,7
  docs_src/cookie_param_models/tutorial001_an_py310::Cookies,extends,BaseModel,docs_src/cookie_param_models/tutorial001_an_py310.py,9
  docs_src/cookie_param_models/tutorial002_py310::Cookies,extends,BaseModel,docs_src/cookie_param_models/tutorial002_py310.py,7
  docs_src/security/tutorial002_an_py310::User,extends,BaseModel,docs_src/security/tutorial002_an_py310.py,12
  docs_src/security/tutorial004_an_py310::Token,extends,BaseModel,docs_src/security/tutorial004_an_py310.py,29
  docs_src/security/tutorial004_an_py310::TokenData,extends,BaseModel,docs_src/security/tutorial004_an_py310.py,34
  docs_src/security/tutorial004_an_py310::User,extends,BaseModel,docs_src/security/tutorial004_an_py310.py,38
  docs_src/security/tutorial004_an_py310::UserInDB,extends,User,docs_src/security/tutorial004_an_py310.py,45
  docs_src/security/tutorial005_py310::Token,extends,BaseModel,docs_src/security/tutorial005_py310.py,39
  docs_src/security/tutorial005_py310::TokenData,extends,BaseModel,docs_src/security/tutorial005_py310.py,44
  docs_src/security/tutorial005_py310::User,extends,BaseModel,docs_src/security/tutorial005_py310.py,49
  docs_src/security/tutorial005_py310::UserInDB,extends,User,docs_src/security/tutorial005_py310.py,56
  docs_src/security/tutorial004_py310::Token,extends,BaseModel,docs_src/security/tutorial004_py310.py,28
  docs_src/security/tutorial004_py310::TokenData,extends,BaseModel,docs_src/security/tutorial004_py310.py,33
  docs_src/security/tutorial004_py310::User,extends,BaseModel,docs_src/security/tutorial004_py310.py,37
  docs_src/security/tutorial004_py310::UserInDB,extends,User,docs_src/security/tutorial004_py310.py,44
  docs_src/security/tutorial003_an_py310::User,extends,BaseModel,docs_src/security/tutorial003_an_py310.py,34
  docs_src/security/tutorial003_an_py310::UserInDB,extends,User,docs_src/security/tutorial003_an_py310.py,41
  docs_src/security/tutorial002_py310::User,extends,BaseModel,docs_src/security/tutorial002_py310.py,10
  docs_src/security/tutorial003_py310::User,extends,BaseModel,docs_src/security/tutorial003_py310.py,32
  docs_src/security/tutorial003_py310::UserInDB,extends,User,docs_src/security/tutorial003_py310.py,39
  docs_src/security/tutorial005_an_py310::Token,extends,BaseModel,docs_src/security/tutorial005_an_py310.py,40
  docs_src/security/tutorial005_an_py310::TokenData,extends,BaseModel,docs_src/security/tutorial005_an_py310.py,45
  docs_src/security/tutorial005_an_py310::User,extends,BaseModel,docs_src/security/tutorial005_an_py310.py,50
  docs_src/security/tutorial005_an_py310::UserInDB,extends,User,docs_src/security/tutorial005_an_py310.py,57
  docs_src/sql_databases/tutorial002_an_py310::HeroBase,extends,SQLModel,docs_src/sql_databases/tutorial002_an_py310.py,7
  docs_src/sql_databases/tutorial002_an_py310::Hero,extends,HeroBase,docs_src/sql_databases/tutorial002_an_py310.py,12
  docs_src/sql_databases/tutorial002_an_py310::Hero,extends,table=True,docs_src/sql_databases/tutorial002_an_py310.py,12
  docs_src/sql_databases/tutorial002_an_py310::HeroPublic,extends,HeroBase,docs_src/sql_databases/tutorial002_an_py310.py,17
  docs_src/sql_databases/tutorial002_an_py310::HeroCreate,extends,HeroBase,docs_src/sql_databases/tutorial002_an_py310.py,21
  docs_src/sql_databases/tutorial002_an_py310::HeroUpdate,extends,HeroBase,docs_src/sql_databases/tutorial002_an_py310.py,25
  docs_src/sql_databases/tutorial001_py310::Hero,extends,SQLModel,docs_src/sql_databases/tutorial001_py310.py,5
  docs_src/sql_databases/tutorial001_py310::Hero,extends,table=True,docs_src/sql_databases/tutorial001_py310.py,5
  docs_src/sql_databases/tutorial001_an_py310::Hero,extends,SQLModel,docs_src/sql_databases/tutorial001_an_py310.py,7
  docs_src/sql_databases/tutorial001_an_py310::Hero,extends,table=True,docs_src/sql_databases/tutorial001_an_py310.py,7
  docs_src/sql_databases/tutorial002_py310::HeroBase,extends,SQLModel,docs_src/sql_databases/tutorial002_py310.py,5
  docs_src/sql_databases/tutorial002_py310::Hero,extends,HeroBase,docs_src/sql_databases/tutorial002_py310.py,10
  docs_src/sql_databases/tutorial002_py310::Hero,extends,table=True,docs_src/sql_databases/tutorial002_py310.py,10
  docs_src/sql_databases/tutorial002_py310::HeroPublic,extends,HeroBase,docs_src/sql_databases/tutorial002_py310.py,15
  docs_src/sql_databases/tutorial002_py310::HeroCreate,extends,HeroBase,docs_src/sql_databases/tutorial002_py310.py,19
  docs_src/sql_databases/tutorial002_py310::HeroUpdate,extends,HeroBase,docs_src/sql_databases/tutorial002_py310.py,23
  docs_src/query_param_models/tutorial002_an_py310::FilterParams,extends,BaseModel,docs_src/query_param_models/tutorial002_an_py310.py,9
  docs_src/query_param_models/tutorial001_py310::FilterParams,extends,BaseModel,docs_src/query_param_models/tutorial001_py310.py,9
  docs_src/query_param_models/tutorial001_an_py310::FilterParams,extends,BaseModel,docs_src/query_param_models/tutorial001_an_py310.py,9
  docs_src/query_param_models/tutorial002_py310::FilterParams,extends,BaseModel,docs_src/query_param_models/tutorial002_py310.py,9
  docs_src/encoder/tutorial001_py310::Item,extends,BaseModel,docs_src/encoder/tutorial001_py310.py,10
  docs_src/body_updates/tutorial001_py310::Item,extends,BaseModel,docs_src/body_updates/tutorial001_py310.py,8
  docs_src/body_updates/tutorial002_py310::Item,extends,BaseModel,docs_src/body_updates/tutorial002_py310.py,8
  docs_src/body/tutorial001_py310::Item,extends,BaseModel,docs_src/body/tutorial001_py310.py,5
  docs_src/body/tutorial004_py310::Item,extends,BaseModel,docs_src/body/tutorial004_py310.py,5
  docs_src/body/tutorial002_py310::Item,extends,BaseModel,docs_src/body/tutorial002_py310.py,5
  docs_src/body/tutorial003_py310::Item,extends,BaseModel,docs_src/body/tutorial003_py310.py,5
  docs_src/path_operation_advanced_configuration/tutorial007_py310::Item,extends,BaseModel,docs_src/path_operation_advanced_configuration/tutorial007_py310.py,8
  docs_src/path_operation_advanced_configuration/tutorial007_py39::Item,extends,BaseModel,docs_src/path_operation_advanced_configuration/tutorial007_py39.py,8
  docs_src/path_operation_advanced_configuration/tutorial004_py310::Item,extends,BaseModel,docs_src/path_operation_advanced_configuration/tutorial004_py310.py,7
  docs_src/generate_clients/tutorial001_py310::Item,extends,BaseModel,docs_src/generate_clients/tutorial001_py310.py,7
  docs_src/generate_clients/tutorial001_py310::ResponseMessage,extends,BaseModel,docs_src/generate_clients/tutorial001_py310.py,12
  docs_src/generate_clients/tutorial002_py39::Item,extends,BaseModel,docs_src/generate_clients/tutorial002_py39.py,7
  docs_src/generate_clients/tutorial002_py39::ResponseMessage,extends,BaseModel,docs_src/generate_clients/tutorial002_py39.py,12
  docs_src/generate_clients/tutorial002_py39::User,extends,BaseModel,docs_src/generate_clients/tutorial002_py39.py,16
  docs_src/generate_clients/tutorial003_py39::Item,extends,BaseModel,docs_src/generate_clients/tutorial003_py39.py,13
  docs_src/generate_clients/tutorial003_py39::ResponseMessage,extends,BaseModel,docs_src/generate_clients/tutorial003_py39.py,18
  docs_src/generate_clients/tutorial003_py39::User,extends,BaseModel,docs_src/generate_clients/tutorial003_py39.py,22
  docs_src/generate_clients/tutorial002_py310::Item,extends,BaseModel,docs_src/generate_clients/tutorial002_py310.py,7
  docs_src/generate_clients/tutorial002_py310::ResponseMessage,extends,BaseModel,docs_src/generate_clients/tutorial002_py310.py,12
  docs_src/generate_clients/tutorial002_py310::User,extends,BaseModel,docs_src/generate_clients/tutorial002_py310.py,16
  docs_src/generate_clients/tutorial003_py310::Item,extends,BaseModel,docs_src/generate_clients/tutorial003_py310.py,13
  docs_src/generate_clients/tutorial003_py310::ResponseMessage,extends,BaseModel,docs_src/generate_clients/tutorial003_py310.py,18
  docs_src/generate_clients/tutorial003_py310::User,extends,BaseModel,docs_src/generate_clients/tutorial003_py310.py,22
  docs_src/generate_clients/tutorial001_py39::Item,extends,BaseModel,docs_src/generate_clients/tutorial001_py39.py,7
  docs_src/generate_clients/tutorial001_py39::ResponseMessage,extends,BaseModel,docs_src/generate_clients/tutorial001_py39.py,12
  docs_src/path_params/tutorial005_py39::ModelName,extends,str,docs_src/path_params/tutorial005_py39.py,6
  docs_src/path_params/tutorial005_py310::ModelName,extends,str,docs_src/path_params/tutorial005_py310.py,6
  docs_src/dependencies/tutorial014_an_py310::User,extends,SQLModel,docs_src/dependencies/tutorial014_an_py310.py,11
  docs_src/dependencies/tutorial014_an_py310::User,extends,table=True,docs_src/dependencies/tutorial014_an_py310.py,11
  docs_src/dependencies/tutorial013_an_py310::User,extends,SQLModel,docs_src/dependencies/tutorial013_an_py310.py,11
  docs_src/dependencies/tutorial013_an_py310::User,extends,table=True,docs_src/dependencies/tutorial013_an_py310.py,11
  docs_src/additional_responses/tutorial001_py310::Item,extends,BaseModel,docs_src/additional_responses/tutorial001_py310.py,6
  docs_src/additional_responses/tutorial001_py310::Message,extends,BaseModel,docs_src/additional_responses/tutorial001_py310.py,11
  docs_src/additional_responses/tutorial004_py310::Item,extends,BaseModel,docs_src/additional_responses/tutorial004_py310.py,6
  docs_src/additional_responses/tutorial003_py39::Item,extends,BaseModel,docs_src/additional_responses/tutorial003_py39.py,6
  docs_src/additional_responses/tutorial003_py39::Message,extends,BaseModel,docs_src/additional_responses/tutorial003_py39.py,11
  docs_src/additional_responses/tutorial002_py310::Item,extends,BaseModel,docs_src/additional_responses/tutorial002_py310.py,6
  docs_src/additional_responses/tutorial003_py310::Item,extends,BaseModel,docs_src/additional_responses/tutorial003_py310.py,6
  docs_src/additional_responses/tutorial003_py310::Message,extends,BaseModel,docs_src/additional_responses/tutorial003_py310.py,11
  docs_src/additional_responses/tutorial001_py39::Item,extends,BaseModel,docs_src/additional_responses/tutorial001_py39.py,6
  docs_src/additional_responses/tutorial001_py39::Message,extends,BaseModel,docs_src/additional_responses/tutorial001_py39.py,11
  docs_src/handling_errors/tutorial005_py39::Item,extends,BaseModel,docs_src/handling_errors/tutorial005_py39.py,18
  docs_src/handling_errors/tutorial005_py310::Item,extends,BaseModel,docs_src/handling_errors/tutorial005_py310.py,18
  docs_src/pydantic_v1_in_v2/tutorial002_an_py310::Item,extends,BaseModel,docs_src/pydantic_v1_in_v2/tutorial002_an_py310.py,5
  docs_src/pydantic_v1_in_v2/tutorial004_an_py310::Item,extends,BaseModel,docs_src/pydantic_v1_in_v2/tutorial004_an_py310.py,8
  docs_src/pydantic_v1_in_v2/tutorial001_an_py310::Item,extends,BaseModel,docs_src/pydantic_v1_in_v2/tutorial001_an_py310.py,4
  docs_src/pydantic_v1_in_v2/tutorial003_an_py310::Item,extends,BaseModel,docs_src/pydantic_v1_in_v2/tutorial003_an_py310.py,6
  docs_src/pydantic_v1_in_v2/tutorial003_an_py310::ItemV2,extends,BaseModelV2,docs_src/pydantic_v1_in_v2/tutorial003_an_py310.py,12
  docs_src/header_param_models/tutorial002_an_py310::CommonHeaders,extends,BaseModel,docs_src/header_param_models/tutorial002_an_py310.py,9
  docs_src/header_param_models/tutorial001_py310::CommonHeaders,extends,BaseModel,docs_src/header_param_models/tutorial001_py310.py,7
  docs_src/header_param_models/tutorial001_an_py310::CommonHeaders,extends,BaseModel,docs_src/header_param_models/tutorial001_an_py310.py,9
  docs_src/header_param_models/tutorial003_an_py310::CommonHeaders,extends,BaseModel,docs_src/header_param_models/tutorial003_an_py310.py,9
  docs_src/header_param_models/tutorial002_py310::CommonHeaders,extends,BaseModel,docs_src/header_param_models/tutorial002_py310.py,7
  docs_src/header_param_models/tutorial003_py310::CommonHeaders,extends,BaseModel,docs_src/header_param_models/tutorial003_py310.py,7
  docs_src/path_operation_configuration/tutorial001_py310::Item,extends,BaseModel,docs_src/path_operation_configuration/tutorial001_py310.py,7
  docs_src/path_operation_configuration/tutorial005_py310::Item,extends,BaseModel,docs_src/path_operation_configuration/tutorial005_py310.py,7
  docs_src/path_operation_configuration/tutorial004_py310::Item,extends,BaseModel,docs_src/path_operation_configuration/tutorial004_py310.py,7
  docs_src/path_operation_configuration/tutorial002_py310::Item,extends,BaseModel,docs_src/path_operation_configuration/tutorial002_py310.py,7
  docs_src/path_operation_configuration/tutorial003_py310::Item,extends,BaseModel,docs_src/path_operation_configuration/tutorial003_py310.py,7
  docs_src/schema_extra_example/tutorial004_an_py310::Item,extends,BaseModel,docs_src/schema_extra_example/tutorial004_an_py310.py,9
  docs_src/schema_extra_example/tutorial001_py310::Item,extends,BaseModel,docs_src/schema_extra_example/tutorial001_py310.py,7
  docs_src/schema_extra_example/tutorial005_py310::Item,extends,BaseModel,docs_src/schema_extra_example/tutorial005_py310.py,7
  docs_src/schema_extra_example/tutorial004_py310::Item,extends,BaseModel,docs_src/schema_extra_example/tutorial004_py310.py,7
  docs_src/schema_extra_example/tutorial003_an_py310::Item,extends,BaseModel,docs_src/schema_extra_example/tutorial003_an_py310.py,9
  docs_src/schema_extra_example/tutorial002_py310::Item,extends,BaseModel,docs_src/schema_extra_example/tutorial002_py310.py,7
  docs_src/schema_extra_example/tutorial003_py310::Item,extends,BaseModel,docs_src/schema_extra_example/tutorial003_py310.py,7
  docs_src/schema_extra_example/tutorial005_an_py310::Item,extends,BaseModel,docs_src/schema_extra_example/tutorial005_an_py310.py,9
  docs_src/openapi_webhooks/tutorial001_py310::Subscription,extends,BaseModel,docs_src/openapi_webhooks/tutorial001_py310.py,9
  docs_src/openapi_webhooks/tutorial001_py39::Subscription,extends,BaseModel,docs_src/openapi_webhooks/tutorial001_py39.py,9
  docs_src/custom_request_and_route/tutorial002_an_py310::ValidationErrorLoggingRoute,extends,APIRoute,docs_src/custom_request_and_route/tutorial002_an_py310.py,9
  docs_src/custom_request_and_route/tutorial001_py310::GzipRequest,extends,Request,docs_src/custom_request_and_route/tutorial001_py310.py,8
  docs_src/custom_request_and_route/tutorial001_py310::GzipRoute,extends,APIRoute,docs_src/custom_request_and_route/tutorial001_py310.py,18
  docs_src/custom_request_and_route/tutorial001_an_py310::GzipRequest,extends,Request,docs_src/custom_request_and_route/tutorial001_an_py310.py,9
  docs_src/custom_request_and_route/tutorial001_an_py310::GzipRoute,extends,APIRoute,docs_src/custom_request_and_route/tutorial001_an_py310.py,19
  docs_src/custom_request_and_route/tutorial002_py310::ValidationErrorLoggingRoute,extends,APIRoute,docs_src/custom_request_and_route/tutorial002_py310.py,8
  docs_src/custom_request_and_route/tutorial003_py310::TimedRoute,extends,APIRoute,docs_src/custom_request_and_route/tutorial003_py310.py,8
  docs_src/extra_models/tutorial004_py39::Item,extends,BaseModel,docs_src/extra_models/tutorial004_py39.py,7
  docs_src/extra_models/tutorial001_py310::UserIn,extends,BaseModel,docs_src/extra_models/tutorial001_py310.py,7
  docs_src/extra_models/tutorial001_py310::UserOut,extends,BaseModel,docs_src/extra_models/tutorial001_py310.py,14
  docs_src/extra_models/tutorial001_py310::UserInDB,extends,BaseModel,docs_src/extra_models/tutorial001_py310.py,20
  docs_src/extra_models/tutorial004_py310::Item,extends,BaseModel,docs_src/extra_models/tutorial004_py310.py,7
  docs_src/extra_models/tutorial002_py310::UserBase,extends,BaseModel,docs_src/extra_models/tutorial002_py310.py,7
  docs_src/extra_models/tutorial002_py310::UserIn,extends,UserBase,docs_src/extra_models/tutorial002_py310.py,13
  docs_src/extra_models/tutorial002_py310::UserOut,extends,UserBase,docs_src/extra_models/tutorial002_py310.py,17
  docs_src/extra_models/tutorial002_py310::UserInDB,extends,UserBase,docs_src/extra_models/tutorial002_py310.py,21
  docs_src/extra_models/tutorial003_py310::BaseItem,extends,BaseModel,docs_src/extra_models/tutorial003_py310.py,9
  docs_src/extra_models/tutorial003_py310::CarItem,extends,BaseItem,docs_src/extra_models/tutorial003_py310.py,14
  docs_src/extra_models/tutorial003_py310::PlaneItem,extends,BaseItem,docs_src/extra_models/tutorial003_py310.py,18
  docs_src/separate_openapi_schemas/tutorial001_py310::Item,extends,BaseModel,docs_src/separate_openapi_schemas/tutorial001_py310.py,5
  docs_src/separate_openapi_schemas/tutorial002_py310::Item,extends,BaseModel,docs_src/separate_openapi_schemas/tutorial002_py310.py,5
  docs_src/app_testing/app_b_py310/main::Item,extends,BaseModel,docs_src/app_testing/app_b_py310/main.py,14
  docs_src/app_testing/app_b_an_py310/main::Item,extends,BaseModel,docs_src/app_testing/app_b_an_py310/main.py,16
  docs_src/request_form_models/tutorial002_an_py310::FormData,extends,BaseModel,docs_src/request_form_models/tutorial002_an_py310.py,9
  docs_src/request_form_models/tutorial001_an_py39::FormData,extends,BaseModel,docs_src/request_form_models/tutorial001_an_py39.py,9
  docs_src/request_form_models/tutorial001_py310::FormData,extends,BaseModel,docs_src/request_form_models/tutorial001_py310.py,7
  docs_src/request_form_models/tutorial001_an_py310::FormData,extends,BaseModel,docs_src/request_form_models/tutorial001_an_py310.py,9
  docs_src/request_form_models/tutorial002_py39::FormData,extends,BaseModel,docs_src/request_form_models/tutorial002_py39.py,7
  docs_src/request_form_models/tutorial002_py310::FormData,extends,BaseModel,docs_src/request_form_models/tutorial002_py310.py,7
  docs_src/request_form_models/tutorial002_an_py39::FormData,extends,BaseModel,docs_src/request_form_models/tutorial002_an_py39.py,9
  docs_src/request_form_models/tutorial001_py39::FormData,extends,BaseModel,docs_src/request_form_models/tutorial001_py39.py,7
  docs_src/body_fields/tutorial001_py310::Item,extends,BaseModel,docs_src/body_fields/tutorial001_py310.py,7
  docs_src/body_fields/tutorial001_an_py310::Item,extends,BaseModel,docs_src/body_fields/tutorial001_an_py310.py,9
  docs_src/custom_response/tutorial009c_py310::CustomORJSONResponse,extends,Response,docs_src/custom_response/tutorial009c_py310.py,9
  docs_src/custom_response/tutorial009c_py39::CustomORJSONResponse,extends,Response,docs_src/custom_response/tutorial009c_py39.py,9
  docs_src/response_directly/tutorial001_py310::Item,extends,BaseModel,docs_src/response_directly/tutorial001_py310.py,9

dependencies[33]{name,version,category}:
  starlette,">=0.40.0,<1.0.0",runtime
  pydantic,>=2.7.0,runtime
  typing-extensions,>=4.8.0,runtime
  typing-inspection,>=0.4.2,runtime
  annotated-doc,>=0.0.2,runtime
  fastapi-cli,>=0.0.8,runtime
  httpx,">=0.23.0,<1.0.0",runtime
  jinja2,>=3.1.5,runtime
  python-multipart,>=0.0.18,runtime
  email-validator,>=2.0.0,runtime
  uvicorn,>=0.12.0,runtime
  pydantic-settings,>=2.0.0,runtime
  pydantic-extra-types,>=2.0.0,runtime
  fastapi-cli,>=0.0.8,runtime
  httpx,">=0.23.0,<1.0.0",runtime
  jinja2,>=3.1.5,runtime
  python-multipart,>=0.0.18,runtime
  email-validator,>=2.0.0,runtime
  uvicorn,>=0.12.0,runtime
  pydantic-settings,>=2.0.0,runtime
  pydantic-extra-types,>=2.0.0,runtime
  fastapi-cli,>=0.0.8,runtime
  httpx,">=0.23.0,<1.0.0",runtime
  jinja2,>=3.1.5,runtime
  python-multipart,>=0.0.18,runtime
  itsdangerous,>=1.1.0,runtime
  pyyaml,>=5.3.1,runtime
  ujson,>=5.8.0,runtime
  orjson,>=3.9.3,runtime
  email-validator,>=2.0.0,runtime
  uvicorn,>=0.12.0,runtime
  pydantic-settings,>=2.0.0,runtime
  pydantic-extra-types,>=2.0.0,runtime
```
