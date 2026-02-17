## Live Codebase Map

The following is a **real-time structural map** of this codebase. It was
regenerated moments ago and reflects the current state of all files on disk.

All file paths and line numbers are accurate right now. When you edit a file,
this map updates before your next turn.

Use this map to navigate directly to the right files and line numbers without
searching. Trust these locations — they are current.

```toon
codebase:
  name: express
  languages[1]: javascript
  last_indexed: 2026-02-16T21:45:11Z

modules[3]{name,path,key_types,depends_on}:
  examples,examples,,
  lib,lib,,
  test,test,,

symbols[127]{fqn,kind,file,line,signature}:
  examples/auth/index::authenticate,fn,examples/auth/index.js,60,"function authenticate(name, pass, fn) {"
  examples/auth/index::restrict,fn,examples/auth/index.js,75,"function restrict(req, res, next) {"
  examples/view-locals/user::User,fn,examples/view-locals/user.js,7,"function User(name, age, species) {"
  examples/view-locals/index::ferrets,fn,examples/view-locals/index.js,17,function ferrets(user) {
  examples/view-locals/index::count,fn,examples/view-locals/index.js,48,"function count(req, res, next) {"
  examples/view-locals/index::users,fn,examples/view-locals/index.js,56,"function users(req, res, next) {"
  examples/view-locals/index::count2,fn,examples/view-locals/index.js,86,"function count2(req, res, next) {"
  examples/view-locals/index::users2,fn,examples/view-locals/index.js,94,"function users2(req, res, next) {"
  examples/view-constructor/github-view::GithubView,fn,examples/view-constructor/github-view.js,23,"function GithubView(name, options){"
  examples/search/index::initializeRedis,fn,examples/search/index.js,29,async function initializeRedis() {
  examples/web-service/index::error,fn,examples/web-service/index.js,15,"function error(status, msg) {"
  examples/online/index::list,fn,examples/online/index.js,40,function list(ids) {
  examples/error/index::error,fn,examples/error/index.js,20,"function error(err, req, res, next) {"
  examples/route-middleware/index::loadUser,fn,examples/route-middleware/index.js,25,"function loadUser(req, res, next) {"
  examples/route-middleware/index::andRestrictToSelf,fn,examples/route-middleware/index.js,36,"function andRestrictToSelf(req, res, next) {"
  examples/route-middleware/index::andRestrictTo,fn,examples/route-middleware/index.js,50,function andRestrictTo(role) {
  examples/content-negotiation/index::format,fn,examples/content-negotiation/index.js,33,function format(path) {
  lib/response::sendfile,fn,lib/response.js,921,"function sendfile(res, file, options, callback) {"
  lib/response::onaborted,fn,lib/response.js,926,function onaborted() {
  lib/response::ondirectory,fn,lib/response.js,936,function ondirectory() {
  lib/response::onerror,fn,lib/response.js,946,function onerror(err) {
  lib/response::onend,fn,lib/response.js,953,function onend() {
  lib/response::onfile,fn,lib/response.js,960,function onfile() {
  lib/response::onfinish,fn,lib/response.js,965,function onfinish(err) {
  lib/response::onstream,fn,lib/response.js,983,function onstream() {
  lib/response::stringify,fn,lib/response.js,1023,"function stringify (value, replacer, spaces, escape) {"
  lib/request::defineGetter,fn,lib/request.js,521,"function defineGetter(obj, name, getter) {"
  lib/express::createApplication,fn,lib/express.js,36,function createApplication() {
  lib/express::app,fn,lib/express.js,37,"app = function(req, res, next) {"
  lib/utils::acceptParams,fn,lib/utils.js,89,function acceptParams (str) {
  lib/utils::createETagGenerator,fn,lib/utils.js,249,function createETagGenerator (options) {
  lib/utils::parseExtendedQueryString,fn,lib/utils.js,267,function parseExtendedQueryString(str) {
  lib/view::View,fn,lib/view.js,52,"function View(name, options) {"
  lib/view::tryStat,fn,lib/view.js,197,function tryStat(path) {
  lib/application::logerror,fn,lib/application.js,615,function logerror(err) {
  lib/application::tryRender,fn,lib/application.js,625,"function tryRender(view, options, callback) {"
  test/res.render::createApp,fn,test/res.render.js,361,function createApp() {
  test/express.json::accept,fn,test/express.json.js,356,function accept (req) {
  test/express.json::accept,fn,test/express.json.js,370,function accept (req) {
  test/express.json::accept,fn,test/express.json.js,382,function accept (req) {
  test/express.json::createApp,fn,test/express.json.js,722,function createApp (options) {
  test/express.json::parseError,fn,test/express.json.js,742,function parseError (str) {
  test/express.json::shouldContainInBody,fn,test/express.json.js,750,function shouldContainInBody (str) {
  test/res.sendFile::handleHeaders,fn,test/res.sendFile.js,90,function handleHeaders (res) {
  test/res.sendFile::createApp,fn,test/res.sendFile.js,905,"function createApp(path, options, fn) {"
  test/express.urlencoded::accept,fn,test/express.urlencoded.js,487,function accept (req) {
  test/express.urlencoded::accept,fn,test/express.urlencoded.js,501,function accept (req) {
  test/express.urlencoded::accept,fn,test/express.urlencoded.js,513,function accept (req) {
  test/express.urlencoded::createManyParams,fn,test/express.urlencoded.js,788,function createManyParams (count) {
  test/express.urlencoded::createApp,fn,test/express.urlencoded.js,805,function createApp (options) {
  test/express.urlencoded::expectKeyCount,fn,test/express.urlencoded.js,824,function expectKeyCount (count) {
  test/app.render::View,fn,test/app.render.js,64,"function View(name, options){"
  test/app.render::View,fn,test/app.render.js,210,"function View(name, options){"
  test/app.render::View,fn,test/app.render.js,234,"function View(name, options){"
  test/app.render::View,fn,test/app.render.js,264,"function View(name, options){"
  test/app.render::View,fn,test/app.render.js,357,"function View(name, options){"
  test/app.render::createApp,fn,test/app.render.js,386,function createApp() {
  test/express.raw::accept,fn,test/express.raw.js,243,function accept (req) {
  test/express.raw::accept,fn,test/express.raw.js,256,function accept (req) {
  test/express.raw::accept,fn,test/express.raw.js,268,function accept (req) {
  test/express.raw::createApp,fn,test/express.raw.js,492,function createApp (options) {
  test/express.text::accept,fn,test/express.text.js,258,function accept (req) {
  test/express.text::accept,fn,test/express.text.js,272,function accept (req) {
  test/express.text::accept,fn,test/express.text.js,284,function accept (req) {
  test/express.text::createApp,fn,test/express.text.js,549,function createApp (options) {
  test/res.format::test,fn,test/res.format.js,182,function test(app) {
  test/config::fn,fn,test/config.js,49,fn = function(){}
  test/config::fn,fn,test/config.js,58,fn = function(){}
  test/config::fn,fn,test/config.js,107,function fn() { return false }
  test/config::fn1,fn,test/config.js,123,function fn1() { return false }
  test/config::fn2,fn,test/config.js,124,function fn2() { return true }
  test/app.engine::render,fn,test/app.engine.js,8,"function render(path, options, fn) {"
  test/Router::handler,fn,test/Router.js,94,"handler = function (req, res) { res.end(new Error('wrong handler')) }"
  test/Router::no,fn,test/Router.js,463,function no() {
  test/Router::fn1,fn,test/Router.js,481,"function fn1(req, res, next) {"
  test/Router::fn2,fn,test/Router.js,486,"function fn2(req, res, next) {"
  test/acceptance/cookie-sessions::getCookies,fn,test/acceptance/cookie-sessions.js,34,function getCookies(res) {
  test/acceptance/auth::getCookie,fn,test/acceptance/auth.js,4,function getCookie(res) {
  test/req.query::createApp,fn,test/req.query.js,94,function createApp(setting) {
  test/support/tmpl::onReadFile,fn,test/support/tmpl.js,6,"function onReadFile(err, str) {"
  test/support/tmpl::generateVariableLookup,fn,test/support/tmpl.js,25,function generateVariableLookup(data) {
  test/support/utils::shouldHaveBody,fn,test/support/utils.js,28,function shouldHaveBody (buf) {
  test/support/utils::shouldHaveHeader,fn,test/support/utils.js,45,function shouldHaveHeader (header) {
  test/support/utils::shouldNotHaveBody,fn,test/support/utils.js,57,function shouldNotHaveBody () {
  test/support/utils::shouldNotHaveHeader,fn,test/support/utils.js,69,function shouldNotHaveHeader(header) {
  test/support/utils::getMajorVersion,fn,test/support/utils.js,75,function getMajorVersion(versionString) {
  test/support/utils::shouldSkipQuery,fn,test/support/utils.js,79,function shouldSkipQuery(versionString) {
  test/res.location::createRedirectServerForDomain,fn,test/res.location.js,127,function createRedirectServerForDomain (domain) {
  test/res.location::testRequestedRedirect,fn,test/res.location.js,141,"function testRequestedRedirect (app, inputUrl, expected, expectedHost, done) {"
  test/express.static::createApp,fn,test/express.static.js,804,"function createApp (dir, options, fn) {"
  test/app.router::handler1,fn,test/app.router.js,16,"function handler1(req, res, next) {"
  test/app.router::handler2,fn,test/app.router.js,21,"function handler2(req, res) {"
  test/app.router::fn,fn,test/app.router.js,852,"function fn(req, res, next) {"
  test/app.router::fn,fn,test/app.router.js,877,"function fn(req, res, next) {"
  test/app.router::fn1,fn,test/app.router.js,941,"function fn1(req, res, next) {"
  test/app.router::fn2,fn,test/app.router.js,945,"function fn2(req, res, next) {"
  test/app.router::fn3,fn,test/app.router.js,949,"function fn3(err, req, res, next) {"
  test/app.router::supportsRegexp,fn,test/app.router.js,1210,function supportsRegexp(source) {
  test/app.use::fn1,fn,test/app.use.js,92,"function fn1(req, res, next) {"
  test/app.use::fn2,fn,test/app.use.js,97,"function fn2(req, res, next) {"
  test/app.use::fn1,fn,test/app.use.js,129,"function fn1(req, res, next) {"
  test/app.use::fn2,fn,test/app.use.js,134,"function fn2(req, res, next) {"
  test/app.use::fn1,fn,test/app.use.js,176,"function fn1(req, res, next) {"
  test/app.use::fn2,fn,test/app.use.js,181,"function fn2(req, res, next) {"
  test/app.use::fn3,fn,test/app.use.js,186,"function fn3(req, res, next) {"
  test/app.use::fn1,fn,test/app.use.js,204,"function fn1(req, res, next) {"
  test/app.use::fn2,fn,test/app.use.js,209,"function fn2(req, res, next) {"
  test/app.use::fn3,fn,test/app.use.js,214,"function fn3(req, res, next) {"
  test/app.use::fn1,fn,test/app.use.js,232,"function fn1(req, res, next) {"
  test/app.use::fn2,fn,test/app.use.js,237,"function fn2(req, res, next) {"
  test/app.use::fn3,fn,test/app.use.js,242,"function fn3(req, res, next) {"
  test/app.use::fn1,fn,test/app.use.js,299,"function fn1(req, res, next) {"
  test/app.use::fn2,fn,test/app.use.js,304,"function fn2(req, res, next) {"
  test/app.use::fn1,fn,test/app.use.js,367,"function fn1(req, res, next) {"
  test/app.use::fn2,fn,test/app.use.js,372,"function fn2(req, res, next) {"
  test/app.use::fn3,fn,test/app.use.js,377,"function fn3(req, res, next) {"
  test/app.use::fn1,fn,test/app.use.js,395,"function fn1(req, res, next) {"
  test/app.use::fn2,fn,test/app.use.js,400,"function fn2(req, res, next) {"
  test/app.use::fn3,fn,test/app.use.js,405,"function fn3(req, res, next) {"
  test/app.use::fn1,fn,test/app.use.js,423,"function fn1(req, res, next) {"
  test/app.use::fn2,fn,test/app.use.js,428,"function fn2(req, res, next) {"
  test/app.use::fn3,fn,test/app.use.js,433,"function fn3(req, res, next) {"
  test/app.use::fn1,fn,test/app.use.js,473,"function fn1(req, res, next) {"
  test/app.use::fn2,fn,test/app.use.js,478,"function fn2(req, res, next) {"
  test/app.use::fn3,fn,test/app.use.js,483,"function fn3(req, res, next) {"
  test/res.append::shouldHaveHeaderValues,fn,test/res.append.js,107,"function shouldHaveHeaderValues (key, values) {"
  test/req.ip::getExpectedClientAddress,fn,test/req.ip.js,109,function getExpectedClientAddress(server) {

dependencies[44]{name,version,category}:
  accepts,^2.0.0,runtime
  body-parser,^2.2.1,runtime
  content-disposition,^1.0.0,runtime
  content-type,^1.0.5,runtime
  cookie,^0.7.1,runtime
  cookie-signature,^1.2.1,runtime
  debug,^4.4.0,runtime
  depd,^2.0.0,runtime
  encodeurl,^2.0.0,runtime
  escape-html,^1.0.3,runtime
  etag,^1.8.1,runtime
  finalhandler,^2.1.0,runtime
  fresh,^2.0.0,runtime
  http-errors,^2.0.0,runtime
  merge-descriptors,^2.0.0,runtime
  mime-types,^3.0.0,runtime
  on-finished,^2.4.1,runtime
  once,^1.4.0,runtime
  parseurl,^1.3.3,runtime
  proxy-addr,^2.0.7,runtime
  qs,^6.14.1,runtime
  range-parser,^1.2.1,runtime
  router,^2.2.0,runtime
  send,^1.1.0,runtime
  serve-static,^2.2.0,runtime
  statuses,^2.0.1,runtime
  type-is,^2.0.1,runtime
  vary,^1.1.2,runtime
  after,0.8.2,dev
  connect-redis,^8.0.1,dev
  cookie-parser,1.4.7,dev
  cookie-session,2.1.1,dev
  ejs,^3.1.10,dev
  eslint,8.47.0,dev
  express-session,^1.18.1,dev
  hbs,4.2.0,dev
  marked,^15.0.3,dev
  method-override,3.0.0,dev
  mocha,^10.7.3,dev
  morgan,1.10.1,dev
  nyc,^17.1.0,dev
  pbkdf2-password,1.2.1,dev
  supertest,^6.3.0,dev
  vhost,~3.0.2,dev
```
