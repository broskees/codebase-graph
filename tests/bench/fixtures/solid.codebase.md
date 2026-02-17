## Live Codebase Map

The following is a **real-time structural map** of this codebase. It was
regenerated moments ago and reflects the current state of all files on disk.

All file paths and line numbers are accurate right now. When you edit a file,
this map updates before your next turn.

Use this map to navigate directly to the right files and line numbers without
searching. Trust these locations — they are current.

```toon
codebase:
  name: solid
  languages[2]: javascript,typescript
  last_indexed: 2026-02-16T21:45:12Z

modules[1]{name,path,key_types,depends_on}:
  packages,packages,"A|Accessor|AccessorArray|Animal|ArrayFilterFn|Assert|B|BaseOptions|ChildrenReturn|Component|ComponentProps|ComponentType|Computation|ComputationState|Context|ContextProviderComponent|CustomPartial|CustomThing|D|DataNode|DataNodes|DataState|DeepMutable|DeepReadonly|DeferredOptions|DevComponent|Directives|DistributeOverride|Dog|DynamicProps|EffectFunction|EffectOptions|EqualityCheckerFunction|Equals|Errored|EvalConditions|ExampleProps|ExternalSource|ExternalSourceFactory|FlowComponent|FlowProps|HydrationContext|InitializedResource|InitializedResourceOptions|InitializedResourceReturn|IsExact|JSXElement|KeyOf|KobaltMultiSelectProps|KobaltSelectProps|KobaltSingleSelectProps|KobalteBaseSelectProps|LegacyResults|M1|M2|M3|M4Type|M5|M6|M7|M8|M9|MatchProps|Memo|MemoOptions|MergeProps|MutableKeyOf|NavigatorScheduling|NoInfer|NotWrappable|Observable|ObservableObserver|OnEffectFunction|OnOptions|OnStoreNodeUpdate|Override|OverrideSpread|Owner|ParentComponent|ParentProps|Part|Pending|PickMutable|Producer|PropsWithChildren|Ready|ReconcileOptions|Recursive|Ref|Refreshing|RequiredParameter|ResolvedChildren|ResolvedJSXElement|Resource|ResourceActions|ResourceFetcher|ResourceFetcherInfo|ResourceOptions|ResourceReturn|ResourceSource|Rest|RestContinue|RestSetterOrContinue|ReturnTypes|RootFunction|S1|S2|S3|SetStoreFunction|Setter|SharedConfig|Signal|SignalOptions|SignalState|SimplePropTypes|Simplify|SourceMapValue|SplitProps|StaticConfig|Store|StoreNode|StorePathRange|StoreSetter|SuspenseContext|SuspenseContextType|SuspenseListContextType|SuspenseListRegisteredState|SuspenseListState|SymbolConstructor|TODO|Task|Test|TestM1|TestM2|TestM3|TestM5|TestM6|TestM7|TestM8|TestM9|TestRepo|TestS1|TestS2|TestS3|Tests|TodoState|Transition|TransitionState|Unresolved|Unwrappable|User|ValidComponent|VoidComponent|VoidProps|W|_MergeProps|fruits",

symbols[500]{fqn,kind,file,line,signature}:
  packages/solid-ssr/static/index.d::StaticConfig,type,packages/solid-ssr/static/index.d.ts,1,type StaticConfig = { entry: string; output: string; url: string };
  packages/solid-element/src/index::ComponentType,type,packages/solid-element/src/index.ts,10,type ComponentType<T> = mComponentType<T>;
  packages/solid/test/signals.type-tests::Animal,class,packages/solid/test/signals.type-tests.ts,14,class Animal {
  packages/solid/test/signals.type-tests::Dog,class,packages/solid/test/signals.type-tests.ts,17,class Dog extends Animal {
  packages/solid/test/signals.type-tests::KobalteBaseSelectProps,interface,packages/solid/test/signals.type-tests.ts,883,"interface KobalteBaseSelectProps<Option, OptGroup = never> {"
  packages/solid/test/signals.type-tests::KobaltSingleSelectProps,interface,packages/solid/test/signals.type-tests.ts,887,interface KobaltSingleSelectProps<T> {
  packages/solid/test/signals.type-tests::KobaltMultiSelectProps,interface,packages/solid/test/signals.type-tests.ts,893,interface KobaltMultiSelectProps<T> {
  packages/solid/test/signals.type-tests::KobaltSelectProps,type,packages/solid/test/signals.type-tests.ts,899,"type KobaltSelectProps<Option, OptGroup = never> = ("
  packages/solid/test/signals.type-tests::fruits,type,packages/solid/test/signals.type-tests.ts,905,"type fruits = \"apple\" | \"banana\" | \"orange\";"
  packages/solid/test/external-source.spec::ExternalSource,class,packages/solid/test/external-source.spec.ts,6,class ExternalSource<T = any> {
  packages/solid/test/resource.type-tests::Assert,type,packages/solid/test/resource.type-tests.ts,4,type Assert<T extends true> = T;
  packages/solid/test/resource.type-tests::Equals,type,packages/solid/test/resource.type-tests.ts,6,"type Equals<X, Y> ="
  packages/solid/test/resource.type-tests::Tests,type,packages/solid/test/resource.type-tests.ts,17,"type Tests = Assert<Equals<typeof resourceReturn, ResourceReturn<number, unknown>>> &"
  packages/solid/test/resource.type-tests::Tests,type,packages/solid/test/resource.type-tests.ts,25,"type Tests = Assert<Equals<typeof k, true | undefined>> &"
  packages/solid/test/resource.type-tests::Tests,type,packages/solid/test/resource.type-tests.ts,38,type Tests = Assert<
  packages/solid/test/resource.type-tests::Tests,type,packages/solid/test/resource.type-tests.ts,49,"type Tests = Assert<Equals<typeof k, true | undefined>> &"
  packages/solid/test/resource.type-tests::ResourceActions,type,packages/solid/test/resource.type-tests.ts,55,type ResourceActions = (typeof resourceReturn)[1];
  packages/solid/test/resource.type-tests::Tests,type,packages/solid/test/resource.type-tests.ts,56,"type Tests = Assert<Equals<ResourceActions[\"mutate\"], Setter<number>>>;"
  packages/solid/test/resource.type-tests::Tests,type,packages/solid/test/resource.type-tests.ts,66,"type Tests = Assert<Equals<typeof resourceReturn, ResourceReturn<number, unknown>>> &"
  packages/solid/test/resource.type-tests::Tests,type,packages/solid/test/resource.type-tests.ts,74,"type Tests = Assert<Equals<typeof k, number | undefined>> &"
  packages/solid/test/resource.type-tests::ResourceActions,type,packages/solid/test/resource.type-tests.ts,80,type ResourceActions = (typeof resourceReturn)[1];
  packages/solid/test/resource.type-tests::Tests,type,packages/solid/test/resource.type-tests.ts,81,"type Tests = Assert<Equals<ResourceActions[\"mutate\"], Setter<number | undefined>>>;"
  packages/solid/test/resource.type-tests::Tests,type,packages/solid/test/resource.type-tests.ts,90,type Tests = Assert<
  packages/solid/test/resource.type-tests::Tests,type,packages/solid/test/resource.type-tests.ts,101,"type Tests = Assert<Equals<typeof k, number | undefined>> &"
  packages/solid/test/resource.type-tests::Tests,type,packages/solid/test/resource.type-tests.ts,115,"type Tests = Assert<Equals<typeof resourceValue, string | undefined>> &"
  packages/solid/test/resource.type-tests::Test,type,packages/solid/test/resource.type-tests.ts,139,"type Test = Assert<Equals<typeof errorValue, never>> &"
  packages/solid/test/resource.type-tests::Test,type,packages/solid/test/resource.type-tests.ts,157,"type Test = Assert<Equals<typeof errorValue, never>> &"
  packages/solid/test/component.type-tests::Assert,type,packages/solid/test/component.type-tests.ts,3,type Assert<T extends true> = never;
  packages/solid/test/component.type-tests::IsExact,type,packages/solid/test/component.type-tests.ts,5,"type IsExact<T, U, I = never> ="
  packages/solid/test/component.type-tests::M1,type,packages/solid/test/component.type-tests.ts,47,type M1 = typeof m1;
  packages/solid/test/component.type-tests::TestM1,type,packages/solid/test/component.type-tests.ts,48,type TestM1 = Assert<
  packages/solid/test/component.type-tests::M2,type,packages/solid/test/component.type-tests.ts,78,type M2 = typeof m2;
  packages/solid/test/component.type-tests::TestM2,type,packages/solid/test/component.type-tests.ts,79,"type TestM2 = Assert<IsExact<M2, { a?: number }>>;"
  packages/solid/test/component.type-tests::M3,type,packages/solid/test/component.type-tests.ts,83,type M3 = typeof m3;
  packages/solid/test/component.type-tests::TestM3,type,packages/solid/test/component.type-tests.ts,84,"type TestM3 = Assert<IsExact<M3, { a: number }>>;"
  packages/solid/test/component.type-tests::M4Type,type,packages/solid/test/component.type-tests.ts,87,type M4Type = {
  packages/solid/test/component.type-tests::M5,type,packages/solid/test/component.type-tests.ts,157,type M5 = typeof m5;
  packages/solid/test/component.type-tests::TestM5,type,packages/solid/test/component.type-tests.ts,158,"type TestM5 = Assert<IsExact<M5, { a: number; b: number; c: number }>>;"
  packages/solid/test/component.type-tests::M6,type,packages/solid/test/component.type-tests.ts,161,type M6 = typeof m6;
  packages/solid/test/component.type-tests::TestM6,type,packages/solid/test/component.type-tests.ts,162,"type TestM6 = Assert<IsExact<M6, { b: number; c: number }>>;"
  packages/solid/test/component.type-tests::M7,type,packages/solid/test/component.type-tests.ts,165,type M7 = typeof m7;
  packages/solid/test/component.type-tests::TestM7,type,packages/solid/test/component.type-tests.ts,166,"type TestM7 = Assert<IsExact<M7, { a: number; b: number }>>;"
  packages/solid/test/component.type-tests::M8,type,packages/solid/test/component.type-tests.ts,169,type M8 = typeof m8;
  packages/solid/test/component.type-tests::TestM8,type,packages/solid/test/component.type-tests.ts,170,"type TestM8 = Assert<IsExact<M8, { b: number }>>;"
  packages/solid/test/component.type-tests::M9,type,packages/solid/test/component.type-tests.ts,173,type M9 = typeof m9;
  packages/solid/test/component.type-tests::TestM9,type,packages/solid/test/component.type-tests.ts,174,"type TestM9 = Assert<IsExact<M9, { a: number; b: number; c: number }>>;"
  packages/solid/test/component.type-tests::S1,type,packages/solid/test/component.type-tests.ts,179,type S1 = typeof s1;
  packages/solid/test/component.type-tests::TestS1,type,packages/solid/test/component.type-tests.ts,180,"type TestS1 = Assert<IsExact<S1, [{ a: number }, { b: number }]>>;"
  packages/solid/test/component.type-tests::S2,type,packages/solid/test/component.type-tests.ts,183,type S2 = typeof s2;
  packages/solid/test/component.type-tests::TestS2,type,packages/solid/test/component.type-tests.ts,184,"type TestS2 = Assert<IsExact<S2, { b: number }>>;"
  packages/solid/test/component.type-tests::S3,type,packages/solid/test/component.type-tests.ts,187,type S3 = typeof s3;
  packages/solid/test/component.type-tests::TestS3,type,packages/solid/test/component.type-tests.ts,188,"type TestS3 = Assert<IsExact<S3, { a: number }>>;"
  packages/solid/test/resource.spec::User,interface,packages/solid/test/resource.spec.ts,80,interface User {
  packages/solid/test/resource.spec::User,type,packages/solid/test/resource.spec.ts,238,type User = {
  packages/solid/test/component.bench::Test,type,packages/solid/test/component.bench.ts,39,type Test = {
  packages/solid/test/component.bench::SplitProps,type,packages/solid/test/component.bench.ts,80,"type SplitProps = (...args: any[]) => Record<string, any>[];"
  packages/solid/test/component.spec::SimplePropTypes,type,packages/solid/test/component.spec.ts,14,type SimplePropTypes = {
  packages/solid/web/test/dynamic.spec::ExampleProps,interface,packages/solid/web/test/dynamic.spec.tsx,13,interface ExampleProps {
  packages/solid/web/test/dynamic.spec::ExampleProps,interface,packages/solid/web/test/dynamic.spec.tsx,61,interface ExampleProps {
  packages/solid/web/test/element.spec::Directives,interface,packages/solid/web/test/element.spec.tsx,10,interface Directives {
  packages/solid/web/server/index::DynamicProps,type,packages/solid/web/server/index.ts,37,"type DynamicProps<T extends ValidComponent, P = ComponentProps<T>> = {"
  packages/solid/web/src/server-mock::LegacyResults,type,packages/solid/web/src/server-mock.ts,59,type LegacyResults = {
  packages/solid/web/src/index::DynamicProps,type,packages/solid/web/src/index.ts,113,"type DynamicProps<T extends ValidComponent, P = ComponentProps<T>> = {"
  packages/solid/store/test/mutableWithClass.spec::D,class,packages/solid/store/test/mutableWithClass.spec.tsx,7,class D {
  packages/solid/store/test/mutableWithClass.spec::A,class,packages/solid/store/test/mutableWithClass.spec.tsx,13,class A {
  packages/solid/store/test/mutableWithClass.spec::A,class,packages/solid/store/test/mutableWithClass.spec.tsx,58,class A {
  packages/solid/store/test/mutableWithClass.spec::B,class,packages/solid/store/test/mutableWithClass.spec.tsx,64,class B extends A {}
  packages/solid/store/test/store.spec::CustomThing,class,packages/solid/store/test/store.spec.ts,697,class CustomThing {
  packages/solid/store/test/store.spec::CustomThing,class,packages/solid/store/test/store.spec.ts,726,class CustomThing {
  packages/solid/store/test/store.spec::Recursive,type,packages/solid/store/test/store.spec.ts,956,type Recursive = { a: Recursive };
  packages/solid/store/test/store.spec::User,type,packages/solid/store/test/store.spec.ts,966,type User = {
  packages/solid/store/test/store.spec::A,type,packages/solid/store/test/store.spec.ts,1014,"type A = { a: T; b: Record<string, string>; c: Record<T, string> };"
  packages/solid/store/test/modifiers.spec::DataState,interface,packages/solid/store/test/modifiers.spec.ts,171,interface DataState {
  packages/solid/store/test/modifiers.spec::TodoState,interface,packages/solid/store/test/modifiers.spec.ts,243,interface TodoState {
  packages/solid/store/test/modifiers.spec::TodoState,type,packages/solid/store/test/modifiers.spec.ts,264,type TodoState = Array<{
  packages/solid/store/src/modifiers::ReconcileOptions,type,packages/solid/store/src/modifiers.ts,5,type ReconcileOptions = {
  packages/solid/store/src/server::ReconcileOptions,type,packages/solid/store/src/server.ts,124,type ReconcileOptions = {
  packages/solid/store/src/store::DataNode,type,packages/solid/store/src/store.ts,16,type DataNode = {
  packages/solid/store/src/store::DataNodes,type,packages/solid/store/src/store.ts,20,"type DataNodes = Record<PropertyKey, DataNode | undefined>;"
  packages/solid/store/src/store::OnStoreNodeUpdate,type,packages/solid/store/src/store.ts,22,type OnStoreNodeUpdate = (
  packages/solid/store/src/store::StoreNode,interface,packages/solid/store/src/store.ts,29,interface StoreNode {
  packages/solid/store/src/store::Unwrappable,interface,packages/solid/store/src/store.ts,35,interface Unwrappable {}
  packages/solid/store/src/store::NotWrappable,type,packages/solid/store/src/store.ts,37,type NotWrappable =
  packages/solid/store/src/store::Store,type,packages/solid/store/src/store.ts,47,type Store<T> = T;
  packages/solid/store/src/store::DeepReadonly,type,packages/solid/store/src/store.ts,316,type DeepReadonly<T> = 0 extends 1 & T
  packages/solid/store/src/store::DeepMutable,type,packages/solid/store/src/store.ts,324,type DeepMutable<T> = 0 extends 1 & T
  packages/solid/store/src/store::CustomPartial,type,packages/solid/store/src/store.ts,332,type CustomPartial<T> = T extends readonly unknown[]
  packages/solid/store/src/store::PickMutable,type,packages/solid/store/src/store.ts,338,type PickMutable<T> = {
  packages/solid/store/src/store::StorePathRange,type,packages/solid/store/src/store.ts,348,type StorePathRange = { from?: number; to?: number; by?: number };
  packages/solid/store/src/store::ArrayFilterFn,type,packages/solid/store/src/store.ts,350,"type ArrayFilterFn<T> = (item: T, index: number) => boolean;"
  packages/solid/store/src/store::StoreSetter,type,packages/solid/store/src/store.ts,352,"type StoreSetter<T, U extends PropertyKey[] = []> ="
  packages/solid/store/src/store::Part,type,packages/solid/store/src/store.ts,357,"type Part<T, K extends KeyOf<T> = KeyOf<T>> ="
  packages/solid/store/src/store::W,type,packages/solid/store/src/store.ts,363,"type W<T> = Exclude<T, NotWrappable>;"
  packages/solid/store/src/store::KeyOf,type,packages/solid/store/src/store.ts,366,type KeyOf<T> = number extends keyof T // have to check this otherwise ts won't allow KeyOf<T> to index T
  packages/solid/store/src/store::MutableKeyOf,type,packages/solid/store/src/store.ts,377,type MutableKeyOf<T> = KeyOf<T> & keyof PickMutable<T>;
  packages/solid/store/src/store::Rest,type,packages/solid/store/src/store.ts,380,"type Rest<T, U extends PropertyKey[], K extends KeyOf<T> = KeyOf<T>> = [T] extends [never]"
  packages/solid/store/src/store::RestContinue,type,packages/solid/store/src/store.ts,388,"type RestContinue<T, U extends PropertyKey[]> = 0 extends 1 & T"
  packages/solid/store/src/store::RestSetterOrContinue,type,packages/solid/store/src/store.ts,392,"type RestSetterOrContinue<T, U extends PropertyKey[]> = [StoreSetter<T, U>] | RestContinue<T, U>;"
  packages/solid/store/src/store::SetStoreFunction,interface,packages/solid/store/src/store.ts,394,interface SetStoreFunction<T> {
  packages/solid/src/reactive/scheduler::Task,interface,packages/solid/src/reactive/scheduler.ts,2,interface Task {
  packages/solid/src/reactive/scheduler::NavigatorScheduling,type,packages/solid/src/reactive/scheduler.ts,10,type NavigatorScheduling = Navigator & {
  packages/solid/src/reactive/observable::SymbolConstructor,interface,packages/solid/src/reactive/observable.ts,17,interface SymbolConstructor {
  packages/solid/src/reactive/observable::Observable,interface,packages/solid/src/reactive/observable.ts,22,interface Observable<T> {
  packages/solid/src/reactive/observable::ObservableObserver,type,packages/solid/src/reactive/observable.ts,29,type ObservableObserver<T> =
  packages/solid/src/reactive/observable::Producer,type,packages/solid/src/reactive/observable.ts,87,type Producer<T> =
  packages/solid/src/reactive/signal::ComputationState,type,packages/solid/src/reactive/signal.ts,77,"type ComputationState = 0 | 1 | 2;"
  packages/solid/src/reactive/signal::SourceMapValue,interface,packages/solid/src/reactive/signal.ts,79,interface SourceMapValue {
  packages/solid/src/reactive/signal::SignalState,interface,packages/solid/src/reactive/signal.ts,85,interface SignalState<T> extends SourceMapValue {
  packages/solid/src/reactive/signal::Owner,interface,packages/solid/src/reactive/signal.ts,95,interface Owner {
  packages/solid/src/reactive/signal::Computation,interface,packages/solid/src/reactive/signal.ts,104,"interface Computation<Init, Next extends Init = Init> extends Owner {"
  packages/solid/src/reactive/signal::TransitionState,interface,packages/solid/src/reactive/signal.ts,117,interface TransitionState {
  packages/solid/src/reactive/signal::ExternalSourceFactory,type,packages/solid/src/reactive/signal.ts,129,"type ExternalSourceFactory = <Prev, Next extends Prev = Prev>("
  packages/solid/src/reactive/signal::ExternalSource,interface,packages/solid/src/reactive/signal.ts,134,interface ExternalSource {
  packages/solid/src/reactive/signal::RootFunction,type,packages/solid/src/reactive/signal.ts,139,type RootFunction<T> = (dispose: () => void) => T;
  packages/solid/src/reactive/signal::Accessor,type,packages/solid/src/reactive/signal.ts,187,type Accessor<T> = () => T;
  packages/solid/src/reactive/signal::Setter,type,packages/solid/src/reactive/signal.ts,189,type Setter<in out T> = {
  packages/solid/src/reactive/signal::Signal,type,packages/solid/src/reactive/signal.ts,198,"type Signal<T> = [get: Accessor<T>, set: Setter<T>];"
  packages/solid/src/reactive/signal::SignalOptions,interface,packages/solid/src/reactive/signal.ts,200,interface SignalOptions<T> extends MemoOptions<T> {
  packages/solid/src/reactive/signal::BaseOptions,interface,packages/solid/src/reactive/signal.ts,263,interface BaseOptions {
  packages/solid/src/reactive/signal::NoInfer,type,packages/solid/src/reactive/signal.ts,270,type NoInfer<T extends any> = [T][T extends any ? 0 : never];
  packages/solid/src/reactive/signal::EffectOptions,interface,packages/solid/src/reactive/signal.ts,272,interface EffectOptions extends BaseOptions {}
  packages/solid/src/reactive/signal::EffectFunction,type,packages/solid/src/reactive/signal.ts,275,"type EffectFunction<Prev, Next extends Prev = Prev> = (v: Prev) => Next;"
  packages/solid/src/reactive/signal::Memo,interface,packages/solid/src/reactive/signal.ts,407,"interface Memo<Prev, Next = Prev> extends SignalState<Next>, Computation<Next> {"
  packages/solid/src/reactive/signal::MemoOptions,interface,packages/solid/src/reactive/signal.ts,412,interface MemoOptions<T> extends EffectOptions {
  packages/solid/src/reactive/signal::Unresolved,interface,packages/solid/src/reactive/signal.ts,467,interface Unresolved {
  packages/solid/src/reactive/signal::Pending,interface,packages/solid/src/reactive/signal.ts,475,interface Pending {
  packages/solid/src/reactive/signal::Ready,interface,packages/solid/src/reactive/signal.ts,483,interface Ready<T> {
  packages/solid/src/reactive/signal::Refreshing,interface,packages/solid/src/reactive/signal.ts,491,interface Refreshing<T> {
  packages/solid/src/reactive/signal::Errored,interface,packages/solid/src/reactive/signal.ts,499,interface Errored {
  packages/solid/src/reactive/signal::Resource,type,packages/solid/src/reactive/signal.ts,507,"type Resource<T> = Unresolved | Pending | Ready<T> | Refreshing<T> | Errored;"
  packages/solid/src/reactive/signal::InitializedResource,type,packages/solid/src/reactive/signal.ts,509,"type InitializedResource<T> = Ready<T> | Refreshing<T> | Errored;"
  packages/solid/src/reactive/signal::ResourceActions,type,packages/solid/src/reactive/signal.ts,511,"type ResourceActions<T, R = unknown> = {"
  packages/solid/src/reactive/signal::ResourceSource,type,packages/solid/src/reactive/signal.ts,516,"type ResourceSource<S> = S | false | null | undefined | (() => S | false | null | undefined);"
  packages/solid/src/reactive/signal::ResourceFetcher,type,packages/solid/src/reactive/signal.ts,518,"type ResourceFetcher<S, T, R = unknown> = ("
  packages/solid/src/reactive/signal::ResourceFetcherInfo,type,packages/solid/src/reactive/signal.ts,523,"type ResourceFetcherInfo<T, R = unknown> = {"
  packages/solid/src/reactive/signal::ResourceOptions,type,packages/solid/src/reactive/signal.ts,528,"type ResourceOptions<T, S = unknown> = {"
  packages/solid/src/reactive/signal::InitializedResourceOptions,type,packages/solid/src/reactive/signal.ts,537,"type InitializedResourceOptions<T, S = unknown> = ResourceOptions<T, S> & {"
  packages/solid/src/reactive/signal::ResourceReturn,type,packages/solid/src/reactive/signal.ts,541,"type ResourceReturn<T, R = unknown> = [Resource<T>, ResourceActions<T | undefined, R>];"
  packages/solid/src/reactive/signal::InitializedResourceReturn,type,packages/solid/src/reactive/signal.ts,543,"type InitializedResourceReturn<T, R = unknown> = ["
  packages/solid/src/reactive/signal::DeferredOptions,interface,packages/solid/src/reactive/signal.ts,763,interface DeferredOptions<T> {
  packages/solid/src/reactive/signal::EqualityCheckerFunction,type,packages/solid/src/reactive/signal.ts,808,"type EqualityCheckerFunction<T, U> = (a: U, b: T) => boolean;"
  packages/solid/src/reactive/signal::ReturnTypes,type,packages/solid/src/reactive/signal.ts,909,type ReturnTypes<T> = T extends readonly Accessor<unknown>[]
  packages/solid/src/reactive/signal::AccessorArray,type,packages/solid/src/reactive/signal.ts,916,"type AccessorArray<T> = [...Extract<{ [K in keyof T]: Accessor<T[K]> }, readonly unknown[]>];"
  packages/solid/src/reactive/signal::OnEffectFunction,type,packages/solid/src/reactive/signal.ts,919,"type OnEffectFunction<S, Prev, Next extends Prev = Prev> = ("
  packages/solid/src/reactive/signal::OnOptions,interface,packages/solid/src/reactive/signal.ts,925,interface OnOptions {
  packages/solid/src/reactive/signal::Transition,type,packages/solid/src/reactive/signal.ts,1107,"type Transition = [Accessor<boolean>, (fn: () => void) => Promise<void>];"
  packages/solid/src/reactive/signal::DevComponent,interface,packages/solid/src/reactive/signal.ts,1129,interface DevComponent<T> extends Memo<unknown> {
  packages/solid/src/reactive/signal::ContextProviderComponent,type,packages/solid/src/reactive/signal.ts,1165,type ContextProviderComponent<T> = FlowComponent<{ value: T }>;
  packages/solid/src/reactive/signal::Context,interface,packages/solid/src/reactive/signal.ts,1168,interface Context<T> {
  packages/solid/src/reactive/signal::ResolvedJSXElement,type,packages/solid/src/reactive/signal.ts,1221,"type ResolvedJSXElement = Exclude<JSX.Element, JSX.ArrayElement>;"
  packages/solid/src/reactive/signal::ResolvedChildren,type,packages/solid/src/reactive/signal.ts,1222,"type ResolvedChildren = ResolvedJSXElement | ResolvedJSXElement[];"
  packages/solid/src/reactive/signal::ChildrenReturn,type,packages/solid/src/reactive/signal.ts,1223,type ChildrenReturn = Accessor<ResolvedChildren> & { toArray: () => ResolvedJSXElement[] };
  packages/solid/src/reactive/signal::SuspenseContextType,type,packages/solid/src/reactive/signal.ts,1246,type SuspenseContextType = {
  packages/solid/src/reactive/signal::SuspenseContext,type,packages/solid/src/reactive/signal.ts,1254,"type SuspenseContext = Context<SuspenseContextType | undefined> & {"
  packages/solid/src/reactive/signal::TODO,type,packages/solid/src/reactive/signal.ts,1772,type TODO = any;
  packages/solid/src/render/component::Component,type,packages/solid/src/render/component.ts,25,"type Component<P extends Record<string, any> = {}> = (props: P) => JSX.Element;"
  packages/solid/src/render/component::VoidProps,type,packages/solid/src/render/component.ts,32,"type VoidProps<P extends Record<string, any> = {}> = P & { children?: never };"
  packages/solid/src/render/component::VoidComponent,type,packages/solid/src/render/component.ts,38,"type VoidComponent<P extends Record<string, any> = {}> = Component<VoidProps<P>>;"
  packages/solid/src/render/component::ParentProps,type,packages/solid/src/render/component.ts,45,"type ParentProps<P extends Record<string, any> = {}> = P & { children?: JSX.Element };"
  packages/solid/src/render/component::ParentComponent,type,packages/solid/src/render/component.ts,51,"type ParentComponent<P extends Record<string, any> = {}> = Component<ParentProps<P>>;"
  packages/solid/src/render/component::FlowProps,type,packages/solid/src/render/component.ts,59,"type FlowProps<P extends Record<string, any> = {}, C = JSX.Element> = P & { children: C };"
  packages/solid/src/render/component::FlowComponent,type,packages/solid/src/render/component.ts,66,"type FlowComponent<P extends Record<string, any> = {}, C = JSX.Element> = Component<"
  packages/solid/src/render/component::PropsWithChildren,type,packages/solid/src/render/component.ts,71,"type PropsWithChildren<P extends Record<string, any> = {}> = ParentProps<P>;"
  packages/solid/src/render/component::ValidComponent,type,packages/solid/src/render/component.ts,73,"type ValidComponent = keyof JSX.IntrinsicElements | Component<any> | (string & {});"
  packages/solid/src/render/component::ComponentProps,type,packages/solid/src/render/component.ts,82,type ComponentProps<T extends ValidComponent> =
  packages/solid/src/render/component::Ref,type,packages/solid/src/render/component.ts,94,"type Ref<T> = T | ((val: T) => void);"
  packages/solid/src/render/component::DistributeOverride,type,packages/solid/src/render/component.ts,150,"type DistributeOverride<T, F> = T extends undefined ? F : T;"
  packages/solid/src/render/component::Override,type,packages/solid/src/render/component.ts,151,"type Override<T, U> = T extends any"
  packages/solid/src/render/component::OverrideSpread,type,packages/solid/src/render/component.ts,160,"type OverrideSpread<T, U> = T extends any"
  packages/solid/src/render/component::Simplify,type,packages/solid/src/render/component.ts,171,type Simplify<T> = T extends any ? { [K in keyof T]: T[K] } : T;
  packages/solid/src/render/component::_MergeProps,type,packages/solid/src/render/component.ts,172,"type _MergeProps<T extends unknown[], Curr = {}> = T extends ["
  packages/solid/src/render/component::MergeProps,type,packages/solid/src/render/component.ts,185,type MergeProps<T extends unknown[]> = Simplify<_MergeProps<T>>;
  packages/solid/src/render/component::SplitProps,type,packages/solid/src/render/component.ts,278,"type SplitProps<T, K extends (readonly (keyof T)[])[]> = ["
  packages/solid/src/render/hydration::HydrationContext,type,packages/solid/src/render/hydration.ts,3,type HydrationContext = { id: string; count: number };
  packages/solid/src/render/hydration::SharedConfig,type,packages/solid/src/render/hydration.ts,5,type SharedConfig = {
  packages/solid/src/render/flow::RequiredParameter,type,packages/solid/src/render/flow.ts,81,type RequiredParameter<T> = T extends () => unknown ? never : T;
  packages/solid/src/render/flow::EvalConditions,type,packages/solid/src/render/flow.ts,151,"type EvalConditions = readonly [number, Accessor<unknown>, MatchProps<unknown>];"
  packages/solid/src/render/flow::MatchProps,type,packages/solid/src/render/flow.ts,223,type MatchProps<T> = {
  packages/solid/src/render/Suspense::SuspenseListContextType,type,packages/solid/src/render/Suspense.ts,17,type SuspenseListContextType = {
  packages/solid/src/render/Suspense::SuspenseListRegisteredState,type,packages/solid/src/render/Suspense.ts,21,type SuspenseListRegisteredState = { showContent: boolean; showFallback: boolean };
  packages/solid/src/render/Suspense::SuspenseListState,interface,packages/solid/src/render/Suspense.ts,22,interface SuspenseListState extends Array<SuspenseListRegisteredState> {
  packages/solid/src/server/reactive::Accessor,type,packages/solid/src/server/reactive.ts,9,type Accessor<T> = () => T;
  packages/solid/src/server/reactive::Setter,type,packages/solid/src/server/reactive.ts,10,type Setter<T> = undefined extends T
  packages/solid/src/server/reactive::Signal,type,packages/solid/src/server/reactive.ts,13,"type Signal<T> = [get: Accessor<T>, set: Setter<T>];"
  packages/solid/src/server/reactive::Owner,interface,packages/solid/src/server/reactive.ts,36,interface Owner {
  packages/solid/src/server/reactive::Context,interface,packages/solid/src/server/reactive.ts,193,interface Context<T> {
  packages/solid/src/server/reactive::ChildrenReturn,type,packages/solid/src/server/reactive.ts,214,type ChildrenReturn = Accessor<any> & { toArray: () => any[] };
  packages/solid/src/server/reactive::Task,interface,packages/solid/src/server/reactive.ts,259,interface Task {
  packages/solid/src/server/reactive::ObservableObserver,type,packages/solid/src/server/reactive.ts,296,type ObservableObserver<T> =
  packages/solid/src/server/rendering::Component,type,packages/solid/src/server/rendering.ts,17,type Component<P = {}> = (props: P) => JSX.Element;
  packages/solid/src/server/rendering::VoidProps,type,packages/solid/src/server/rendering.ts,18,type VoidProps<P = {}> = P & { children?: never };
  packages/solid/src/server/rendering::VoidComponent,type,packages/solid/src/server/rendering.ts,19,type VoidComponent<P = {}> = Component<VoidProps<P>>;
  packages/solid/src/server/rendering::ParentProps,type,packages/solid/src/server/rendering.ts,20,type ParentProps<P = {}> = P & { children?: JSX.Element };
  packages/solid/src/server/rendering::ParentComponent,type,packages/solid/src/server/rendering.ts,21,type ParentComponent<P = {}> = Component<ParentProps<P>>;
  packages/solid/src/server/rendering::FlowProps,type,packages/solid/src/server/rendering.ts,22,"type FlowProps<P = {}, C = JSX.Element> = P & { children: C };"
  packages/solid/src/server/rendering::FlowComponent,type,packages/solid/src/server/rendering.ts,23,"type FlowComponent<P = {}, C = JSX.Element> = Component<FlowProps<P, C>>;"
  packages/solid/src/server/rendering::Ref,type,packages/solid/src/server/rendering.ts,24,"type Ref<T> = T | ((val: T) => void);"
  packages/solid/src/server/rendering::ValidComponent,type,packages/solid/src/server/rendering.ts,25,"type ValidComponent = keyof JSX.IntrinsicElements | Component<any> | (string & {});"
  packages/solid/src/server/rendering::ComponentProps,type,packages/solid/src/server/rendering.ts,26,type ComponentProps<T extends ValidComponent> =
  packages/solid/src/server/rendering::SharedConfig,type,packages/solid/src/server/rendering.ts,106,type SharedConfig = {
  packages/solid/src/server/rendering::RequiredParameter,type,packages/solid/src/server/rendering.ts,287,type RequiredParameter<T> = T extends () => unknown ? never : T;
  packages/solid/src/server/rendering::MatchProps,type,packages/solid/src/server/rendering.ts,323,type MatchProps<T> = {
  packages/solid/src/server/rendering::Resource,interface,packages/solid/src/server/rendering.ts,367,interface Resource<T> {
  packages/solid/src/server/rendering::SuspenseContextType,type,packages/solid/src/server/rendering.ts,375,type SuspenseContextType = {
  packages/solid/src/server/rendering::ResourceActions,type,packages/solid/src/server/rendering.ts,380,type ResourceActions<T> = { mutate: Setter<T>; refetch: (info?: unknown) => void };
  packages/solid/src/server/rendering::ResourceReturn,type,packages/solid/src/server/rendering.ts,382,"type ResourceReturn<T> = [Resource<T>, ResourceActions<T>];"
  packages/solid/src/server/rendering::ResourceSource,type,packages/solid/src/server/rendering.ts,384,"type ResourceSource<S> = S | false | null | undefined | (() => S | false | null | undefined);"
  packages/solid/src/server/rendering::ResourceFetcher,type,packages/solid/src/server/rendering.ts,386,"type ResourceFetcher<S, T> = (k: S, info: ResourceFetcherInfo<T>) => T | Promise<T>;"
  packages/solid/src/server/rendering::ResourceFetcherInfo,type,packages/solid/src/server/rendering.ts,388,"type ResourceFetcherInfo<T> = { value: T | undefined; refetching?: unknown };"
  packages/solid/src/server/rendering::ResourceOptions,type,packages/solid/src/server/rendering.ts,390,type ResourceOptions<T> = undefined extends T
  packages/solid/src/server/rendering::HydrationContext,type,packages/solid/src/server/rendering.ts,623,type HydrationContext = {
  packages/solid/src/index::JSXElement,type,packages/solid/src/index.ts,72,type JSXElement = JSX.Element;
  packages/test-integration/tests/downloaded.spec::TestRepo,type,packages/test-integration/tests/downloaded.spec.ts,17,type TestRepo = ReturnType<typeof makeTestRepo>;
  packages/solid-ssr/static/index::run,fn,packages/solid-ssr/static/index.js,10,"async function run({ entry, output, url }) {"
  packages/solid-ssr/static/index::renderStatic,fn,packages/solid-ssr/static/index.js,22,async function renderStatic(config) {
  packages/solid-ssr/static/writeToDisk::write,fn,packages/solid-ssr/static/writeToDisk.js,4,async function write() {
  packages/solid-ssr/examples/shared/src/components/Home::Home,fn,packages/solid-ssr/examples/shared/src/components/Home.js,2,Home = () => {
  packages/solid-ssr/examples/shared/src/components/Profile/Profile::Profile,fn,packages/solid-ssr/examples/shared/src/components/Profile/Profile.js,1,Profile = props => (
  packages/solid-ssr/examples/shared/src/components/Settings::Settings,fn,packages/solid-ssr/examples/shared/src/components/Settings.js,3,Settings = () => {
  packages/solid-ssr/examples/shared/src/router::RouteHOC,fn,packages/solid-ssr/examples/shared/src/router.js,6,function RouteHOC(Comp) {
  packages/solid-ssr/examples/shared/src/router::matches,fn,packages/solid-ssr/examples/shared/src/router.js,11,"matches = match => match === (location() || \"index\")"
  packages/solid-ssr/examples/shared/src/router::Link,fn,packages/solid-ssr/examples/shared/src/router.js,25,Link = props => {
  packages/solid-ssr/examples/shared/src/router::navigate,fn,packages/solid-ssr/examples/shared/src/router.js,27,navigate = e => {
  packages/solid-element/src/index::createProps,fn,packages/solid-element/src/index.ts,14,function createProps<T extends object>(raw: T) {
  packages/solid-element/src/index::lookupContext,fn,packages/solid-element/src/index.ts,29,function lookupContext(el: ICustomElement & { _$owner?: any }) {
  packages/solid-element/src/index::withSolid,fn,packages/solid-element/src/index.ts,43,function withSolid<T extends object>(ComponentType: ComponentType<T>): ComponentType<T> {
  packages/solid-element/src/index::customElement,fn,packages/solid-element/src/index.ts,72,function customElement<T extends object>(
  packages/solid/test/signals.type-tests::one,fn,packages/solid/test/signals.type-tests.ts,652,one = (): number => 123
  packages/solid/test/signals.type-tests::two,fn,packages/solid/test/signals.type-tests.ts,653,two = () => Boolean(Math.random())
  packages/solid/test/signals.type-tests::memoCreator,fn,packages/solid/test/signals.type-tests.ts,713,memoCreator = (defer: boolean) =>
  packages/solid/test/signals.type-tests::createGenericSignal,fn,packages/solid/test/signals.type-tests.ts,871,"function createGenericSignal<T>(): Signal<T | undefined> {"
  packages/solid/test/signals.type-tests::customSet,fn,packages/solid/test/signals.type-tests.ts,873,"customSet: Setter<T | undefined> = (v?) => setGeneric(v!)"
  packages/solid/test/signals.type-tests::createInitializedSignal,fn,packages/solid/test/signals.type-tests.ts,877,function createInitializedSignal<T>(init: T): Signal<T> {
  packages/solid/test/signals.type-tests::customSet,fn,packages/solid/test/signals.type-tests.ts,879,customSet: Setter<T> = (v?) => setGeneric(v!)
  packages/solid/test/signals.type-tests::kobalteSelect,fn,packages/solid/test/signals.type-tests.ts,909,function kobalteSelect<T>(props: KobaltSelectProps<T>) {}
  packages/solid/test/external-source.spec::constructor,method,packages/solid/test/external-source.spec.ts,9,constructor(private value: T) {}
  packages/solid/test/external-source.spec::update,method,packages/solid/test/external-source.spec.ts,11,update(x: T) {
  packages/solid/test/external-source.spec::get,method,packages/solid/test/external-source.spec.ts,16,get() {
  packages/solid/test/external-source.spec::removeListener,method,packages/solid/test/external-source.spec.ts,24,removeListener(listener: () => void) {
  packages/solid/test/external-source.spec::untrackSource,fn,packages/solid/test/external-source.spec.ts,31,function untrackSource<T>(fn: () => T) {
  packages/solid/test/component.type-tests::M4,fn,packages/solid/test/component.type-tests.ts,91,"function M4<T extends keyof M4Type = \"a\">("
  packages/solid/test/rendering.spec::fn,fn,packages/solid/test/rendering.spec.ts,26,"fn = () => \"dynamic content\""
  packages/solid/test/signals.memo.spec::init,fn,packages/solid/test/signals.memo.spec.ts,206,function init() {
  packages/solid/test/resource.spec::fetcher,fn,packages/solid/test/resource.spec.ts,23,function fetcher(id: string) {
  packages/solid/test/resource.spec::fetcher,fn,packages/solid/test/resource.spec.ts,92,"function fetcher(_: unknown, { value }: ResourceFetcherInfo<Store<User>>) {"
  packages/solid/test/resource.spec::fetcher,fn,packages/solid/test/resource.spec.ts,153,function fetcher(id: string) {
  packages/solid/test/resource.spec::fetcher,fn,packages/solid/test/resource.spec.ts,186,function fetcher(id: string) {
  packages/solid/test/resource.spec::fetcher,fn,packages/solid/test/resource.spec.ts,251,function fetcher() {
  packages/solid/test/resource.spec::createDeepSignal,fn,packages/solid/test/resource.spec.ts,256,"function createDeepSignal<T>(value: T, options?: ReconcileOptions): Signal<T> {"
  packages/solid/test/component.bench::createObject,fn,packages/solid/test/component.bench.ts,22,createObject = (
  packages/solid/test/component.bench::keys,fn,packages/solid/test/component.bench.ts,37,"keys = (o: Record<string, any>) => Object.keys(o)"
  packages/solid/test/component.bench::createTest,fn,packages/solid/test/component.bench.ts,44,"function createTest<T extends (...args: any[]) => any, G extends (...args: any[]) => any>(options: {"
  packages/solid/test/component.spec::Comp,fn,packages/solid/test/component.spec.ts,21,Comp = (props: { greeting: string; name: string }) => `${props.greeting} ${props.name}`
  packages/solid/test/component.spec::Comp2,fn,packages/solid/test/component.spec.ts,23,Comp2 = (props: { greeting: string; name: string; optional?: string }) => {
  packages/solid/test/signals.spec::fn,fn,packages/solid/test/signals.spec.ts,371,fn = (arg?: number) => {
  packages/solid/test/signals.spec::fn,fn,packages/solid/test/signals.spec.ts,391,fn = (arg: number) => {
  packages/solid/universal/src/index::createRenderer,fn,packages/solid/universal/src/index.ts,7,function createRenderer<NodeType>(options: RendererOptions<NodeType>): Renderer<NodeType> {
  packages/solid/web/test/dynamic.spec::Component,fn,packages/solid/web/test/dynamic.spec.tsx,18,Component = () => (
  packages/solid/web/test/dynamic.spec::CompA,fn,packages/solid/web/test/dynamic.spec.tsx,23,CompA: Component<ExampleProps> = props => <div>Hi {props.id}</div>
  packages/solid/web/test/dynamic.spec::CompB,fn,packages/solid/web/test/dynamic.spec.tsx,24,CompB: Component<ExampleProps> = props => <span>Yo {props.id}</span>
  packages/solid/web/test/dynamic.spec::Component,fn,packages/solid/web/test/dynamic.spec.tsx,68,Component = () => (
  packages/solid/web/test/dynamic.spec::CompA,fn,packages/solid/web/test/dynamic.spec.tsx,73,CompA: Component<ExampleProps> = props => <div>Hi {props.id}</div>
  packages/solid/web/test/dynamic.spec::CompB,fn,packages/solid/web/test/dynamic.spec.tsx,74,CompB: Component<ExampleProps> = props => <span>Yo {props.id}</span>
  packages/solid/web/test/for.spec::Component,fn,packages/solid/web/test/for.spec.tsx,16,Component = () => (
  packages/solid/web/test/for.spec::apply,fn,packages/solid/web/test/for.spec.tsx,22,function apply(array: string[]) {
  packages/solid/web/test/for.spec::Component,fn,packages/solid/web/test/for.spec.tsx,101,Component = () => <For each={list()}>{item => item}</For>
  packages/solid/web/test/for.spec::apply,fn,packages/solid/web/test/for.spec.tsx,104,function apply(array: string[]) {
  packages/solid/web/test/for.spec::Component,fn,packages/solid/web/test/for.spec.tsx,182,Component = () => (
  packages/solid/web/test/for.spec::apply,fn,packages/solid/web/test/for.spec.tsx,195,function apply(array: string[]) {
  packages/solid/web/test/for.spec::Component,fn,packages/solid/web/test/for.spec.tsx,273,Component = () => (
  packages/solid/web/test/for.spec::apply,fn,packages/solid/web/test/for.spec.tsx,279,function apply(array: string[]) {
  packages/solid/web/test/for.spec::Component,fn,packages/solid/web/test/for.spec.tsx,357,Component = () => (
  packages/solid/web/test/for.spec::Component,fn,packages/solid/web/test/for.spec.tsx,387,Component = () => (
  packages/solid/web/test/for.spec::Component,fn,packages/solid/web/test/for.spec.tsx,415,Component = () => (
  packages/solid/web/test/portal.spec::Component,fn,packages/solid/web/test/portal.spec.tsx,13,Component = () => <Portal mount={testMount}>Hi</Portal>
  packages/solid/web/test/portal.spec::Component,fn,packages/solid/web/test/portal.spec.tsx,32,Component = () => (
  packages/solid/web/test/portal.spec::Component,fn,packages/solid/web/test/portal.spec.tsx,53,Component = () => (
  packages/solid/web/test/portal.spec::Component,fn,packages/solid/web/test/portal.spec.tsx,92,Component = () => (
  packages/solid/web/test/portal.spec::Component,fn,packages/solid/web/test/portal.spec.tsx,123,Component = () => <Portal ref={portalElem}>{count()}</Portal>
  packages/solid/web/test/suspense.spec::ChildComponent,fn,packages/solid/web/test/suspense.spec.tsx,46,ChildComponent = (props: { greeting: string }) => {
  packages/solid/web/test/suspense.spec::Component,fn,packages/solid/web/test/suspense.spec.tsx,58,Component = () => (
  packages/solid/web/test/suspense.spec::promiseFactory,fn,packages/solid/web/test/suspense.spec.tsx,154,promiseFactory = (time: number) => {
  packages/solid/web/test/suspense.spec::A,fn,packages/solid/web/test/suspense.spec.tsx,162,A = () => {
  packages/solid/web/test/suspense.spec::B,fn,packages/solid/web/test/suspense.spec.tsx,166,B = () => {
  packages/solid/web/test/suspense.spec::C,fn,packages/solid/web/test/suspense.spec.tsx,170,C = () => {
  packages/solid/web/test/suspense.spec::Comp,fn,packages/solid/web/test/suspense.spec.tsx,177,Comp = () => (
  packages/solid/web/test/suspense.spec::Comp,fn,packages/solid/web/test/suspense.spec.tsx,207,Comp = () => (
  packages/solid/web/test/suspense.spec::Comp,fn,packages/solid/web/test/suspense.spec.tsx,239,Comp = () => (
  packages/solid/web/test/suspense.spec::Comp,fn,packages/solid/web/test/suspense.spec.tsx,271,Comp = () => (
  packages/solid/web/test/suspense.spec::Comp,fn,packages/solid/web/test/suspense.spec.tsx,303,Comp = () => (
  packages/solid/web/test/suspense.spec::Comp,fn,packages/solid/web/test/suspense.spec.tsx,335,Comp = () => (
  packages/solid/web/test/suspense.spec::Comp,fn,packages/solid/web/test/suspense.spec.tsx,367,Comp = () => (
  packages/solid/web/test/suspense.spec::Comp,fn,packages/solid/web/test/suspense.spec.tsx,403,Comp = () => (
  packages/solid/web/test/context.spec::Component,fn,packages/solid/web/test/context.spec.tsx,12,Component = () => {
  packages/solid/web/test/context.spec::CondComponent,fn,packages/solid/web/test/context.spec.tsx,16,CondComponent = () => {
  packages/solid/web/test/context.spec::child,fn,packages/solid/web/test/context.spec.tsx,85,child = () => <Component />
  packages/solid/web/test/context.spec::child,fn,packages/solid/web/test/context.spec.tsx,100,child = () => <CondComponent />
  packages/solid/web/test/index.spec::Component,fn,packages/solid/web/test/index.spec.tsx,16,Component = () => (
  packages/solid/web/test/index.spec::apply,fn,packages/solid/web/test/index.spec.tsx,22,function apply(array: string[]) {
  packages/solid/web/test/index.spec::Component,fn,packages/solid/web/test/index.spec.tsx,101,Component = () => <Index each={list()}>{item => <>{item()}</>}</Index>
  packages/solid/web/test/index.spec::apply,fn,packages/solid/web/test/index.spec.tsx,104,function apply(array: string[]) {
  packages/solid/web/test/index.spec::Component,fn,packages/solid/web/test/index.spec.tsx,182,Component = () => (
  packages/solid/web/test/index.spec::apply,fn,packages/solid/web/test/index.spec.tsx,195,function apply(array: string[]) {
  packages/solid/web/test/index.spec::Component,fn,packages/solid/web/test/index.spec.tsx,273,Component = () => (
  packages/solid/web/test/index.spec::apply,fn,packages/solid/web/test/index.spec.tsx,286,function apply(array: string[]) {
  packages/solid/web/test/index.spec::Component,fn,packages/solid/web/test/index.spec.tsx,364,Component = () => (
  packages/solid/web/test/index.spec::Component,fn,packages/solid/web/test/index.spec.tsx,394,Component = () => (
  packages/solid/web/test/index.spec::Component,fn,packages/solid/web/test/index.spec.tsx,422,Component = () => (
  packages/solid/web/test/errorboundary.spec::Component,fn,packages/solid/web/test/errorboundary.spec.tsx,12,Component = () => {
  packages/solid/web/test/errorboundary.spec::Component2,fn,packages/solid/web/test/errorboundary.spec.tsx,17,Component2 = () => {
  packages/solid/web/test/errorboundary.spec::Component3,fn,packages/solid/web/test/errorboundary.spec.tsx,25,Component3 = () => {
  packages/solid/web/test/element.spec::JSX,namespace,packages/solid/web/test/element.spec.tsx,9,namespace JSX {
  packages/solid/web/test/element.spec::getRef,fn,packages/solid/web/test/element.spec.tsx,71,getRef = (el: HTMLDivElement) => (ref = el)
  packages/solid/web/test/element.spec::Comp,fn,packages/solid/web/test/element.spec.tsx,93,Comp = (props: { children?: JSX.Element }) => {
  packages/solid/web/test/switch.spec::Component,fn,packages/solid/web/test/switch.spec.tsx,13,Component = () => (
  packages/solid/web/test/switch.spec::Component,fn,packages/solid/web/test/switch.spec.tsx,43,Component = () => (
  packages/solid/web/test/switch.spec::Component,fn,packages/solid/web/test/switch.spec.tsx,90,Component = () => (
  packages/solid/web/test/switch.spec::Component,fn,packages/solid/web/test/switch.spec.tsx,134,Component = () => (
  packages/solid/web/test/switch.spec::Component,fn,packages/solid/web/test/switch.spec.tsx,178,Component = () => (
  packages/solid/web/test/switch.spec::makeCondition,fn,packages/solid/web/test/switch.spec.tsx,213,function makeCondition() {
  packages/solid/web/test/switch.spec::Component,fn,packages/solid/web/test/switch.spec.tsx,229,Component = () => (
  packages/solid/web/test/switch.spec::Component,fn,packages/solid/web/test/switch.spec.tsx,325,Component = () => (
  packages/solid/web/test/switch.spec::Component,fn,packages/solid/web/test/switch.spec.tsx,369,Component = () => (
  packages/solid/web/test/switch.spec::Component,fn,packages/solid/web/test/switch.spec.tsx,404,Component = () => (
  packages/solid/web/test/show.spec::Component,fn,packages/solid/web/test/show.spec.tsx,12,Component = () => (
  packages/solid/web/test/show.spec::Component,fn,packages/solid/web/test/show.spec.tsx,42,Component = () => (
  packages/solid/web/test/show.spec::when,fn,packages/solid/web/test/show.spec.tsx,77,function when() {
  packages/solid/web/test/show.spec::Component,fn,packages/solid/web/test/show.spec.tsx,81,Component = () => (
  packages/solid/web/test/show.spec::when,fn,packages/solid/web/test/show.spec.tsx,128,function when() {
  packages/solid/web/test/show.spec::Component,fn,packages/solid/web/test/show.spec.tsx,132,Component = () => (
  packages/solid/web/test/show.spec::when,fn,packages/solid/web/test/show.spec.tsx,179,function when() {
  packages/solid/web/test/show.spec::Component,fn,packages/solid/web/test/show.spec.tsx,183,Component = () => (
  packages/solid/web/test/show.spec::Component,fn,packages/solid/web/test/show.spec.tsx,233,Component = () => (
  packages/solid/web/test/show.spec::Component,fn,packages/solid/web/test/show.spec.tsx,274,Component = () => (
  packages/solid/web/test/show.spec::Component,fn,packages/solid/web/test/show.spec.tsx,311,Component = () => (
  packages/solid/web/test/show.spec::Component,fn,packages/solid/web/test/show.spec.tsx,348,Component = () => (
  packages/solid/web/server/index::createDynamic,fn,packages/solid/web/server/index.ts,22,function createDynamic<T extends ValidComponent>(
  packages/solid/web/server/index::Dynamic,fn,packages/solid/web/server/index.ts,43,function Dynamic<T extends ValidComponent>(props: DynamicProps<T>): JSX.Element {
  packages/solid/web/server/index::Portal,fn,packages/solid/web/server/index.ts,48,function Portal(props: { mount?: Node; useShadow?: boolean; children: JSX.Element }) {
  packages/solid/web/storage/src/index::provideRequestEvent,fn,packages/solid/web/storage/src/index.ts,6,"function provideRequestEvent<T extends RequestEvent, U>(init: T, cb: () => U): U {"
  packages/solid/web/src/core::memo,fn,packages/solid/web/src/core.ts,13,memo = fn => createMemo(() => fn())
  packages/solid/web/src/server-mock::throwInBrowser,fn,packages/solid/web/src/server-mock.ts,2,function throwInBrowser(func: Function) {
  packages/solid/web/src/server-mock::renderToString,fn,packages/solid/web/src/server-mock.ts,8,function renderToString<T>(
  packages/solid/web/src/server-mock::renderToStringAsync,fn,packages/solid/web/src/server-mock.ts,17,function renderToStringAsync<T>(
  packages/solid/web/src/server-mock::renderToStream,fn,packages/solid/web/src/server-mock.ts,27,function renderToStream<T>(
  packages/solid/web/src/server-mock::ssr,fn,packages/solid/web/src/server-mock.ts,41,"function ssr(template: string[] | string, ...nodes: any[]): { t: string } {}"
  packages/solid/web/src/server-mock::ssrElement,fn,packages/solid/web/src/server-mock.ts,42,function ssrElement(
  packages/solid/web/src/server-mock::ssrClassList,fn,packages/solid/web/src/server-mock.ts,48,function ssrClassList(value: { [k: string]: boolean }): string {}
  packages/solid/web/src/server-mock::ssrStyle,fn,packages/solid/web/src/server-mock.ts,49,function ssrStyle(value: { [k: string]: string }): string {}
  packages/solid/web/src/server-mock::ssrAttribute,fn,packages/solid/web/src/server-mock.ts,50,"function ssrAttribute(key: string, value: boolean): string {}"
  packages/solid/web/src/server-mock::ssrHydrationKey,fn,packages/solid/web/src/server-mock.ts,51,function ssrHydrationKey(): string {}
  packages/solid/web/src/server-mock::resolveSSRNode,fn,packages/solid/web/src/server-mock.ts,52,function resolveSSRNode(node: any): string {}
  packages/solid/web/src/server-mock::escape,fn,packages/solid/web/src/server-mock.ts,53,function escape(html: string): string {}
  packages/solid/web/src/server-mock::ssrSpread,fn,packages/solid/web/src/server-mock.ts,58,"function ssrSpread(props: any, isSVG: boolean, skipChildren: boolean): void {}"
  packages/solid/web/src/index::createElement,fn,packages/solid/web/src/index.ts,40,"function createElement(tagName: string, isSVG = false, is = undefined): HTMLElement | SVGElement {"
  packages/solid/web/src/index::hydrate,fn,packages/solid/web/src/index.ts,46,hydrate: typeof hydrateCore = (...args) => {
  packages/solid/web/src/index::Portal,fn,packages/solid/web/src/index.ts,58,"function Portal<T extends boolean = false, S extends boolean = false>(props: {"
  packages/solid/web/src/index::mount,fn,packages/solid/web/src/index.ts,72,"mount = () => props.mount || document.body"
  packages/solid/web/src/index::cleanup,fn,packages/solid/web/src/index.ts,85,cleanup = () => setClean(true)
  packages/solid/web/src/index::createDynamic,fn,packages/solid/web/src/index.ts,131,function createDynamic<T extends ValidComponent>(
  packages/solid/web/src/index::Dynamic,fn,packages/solid/web/src/index.ts,168,function Dynamic<T extends ValidComponent>(props: DynamicProps<T>): JSX.Element {
  packages/solid/h/jsx-runtime/src/index::Fragment,fn,packages/solid/h/jsx-runtime/src/index.ts,5,function Fragment(props: { children: JSX.Element }) {
  packages/solid/h/jsx-runtime/src/index::jsx,fn,packages/solid/h/jsx-runtime/src/index.ts,9,"function jsx(type: any, props: any) {"
  packages/solid/rollup.config::replaceDev,fn,packages/solid/rollup.config.js,33,replaceDev = isDev =>
  packages/solid/store/test/mutableWithClass.spec::e,method,packages/solid/store/test/mutableWithClass.spec.tsx,9,get e() {
  packages/solid/store/test/mutableWithClass.spec::b,method,packages/solid/store/test/mutableWithClass.spec.tsx,15,get b() {
  packages/solid/store/test/mutableWithClass.spec::increment,fn,packages/solid/store/test/mutableWithClass.spec.tsx,23,increment = () => {
  packages/solid/store/test/mutableWithClass.spec::getVal,method,packages/solid/store/test/mutableWithClass.spec.tsx,60,get getVal() {
  packages/solid/store/test/store.spec::constructor,method,packages/solid/store/test/store.spec.ts,700,constructor(value: number) {
  packages/solid/store/test/store.spec::constructor,method,packages/solid/store/test/store.spec.ts,729,constructor(value: number) {
  packages/solid/store/test/store.spec::h,fn,packages/solid/store/test/store.spec.ts,979,h: NotWrappable = () => 1
  packages/solid/store/src/mutable::proxyDescriptor,fn,packages/solid/store/src/mutable.ts,17,"function proxyDescriptor(target: StoreNode, property: PropertyKey) {"
  packages/solid/store/src/mutable::wrap,fn,packages/solid/store/src/mutable.ts,92,function wrap<T extends StoreNode>(value: T): T {
  packages/solid/store/src/mutable::set,fn,packages/solid/store/src/mutable.ts,128,"set = (v: T[keyof T]) => batch(() => og.call(p, v))"
  packages/solid/store/src/mutable::createMutable,fn,packages/solid/store/src/mutable.ts,139,"function createMutable<T extends StoreNode>(state: T, options?: { name?: string }): T {"
  packages/solid/store/src/mutable::modifyMutable,fn,packages/solid/store/src/mutable.ts,151,"function modifyMutable<T>(state: T, modifier: (state: T) => T) {"
  packages/solid/store/src/modifiers::applyState,fn,packages/solid/store/src/modifiers.ts,10,function applyState(
  packages/solid/store/src/modifiers::reconcile,fn,packages/solid/store/src/modifiers.ts,129,"function reconcile<T extends U, U>("
  packages/solid/store/src/modifiers::produce,fn,packages/solid/store/src/modifiers.ts,166,function produce<T>(fn: (state: T) => void): (state: T) => T {
  packages/solid/store/src/server::isWrappable,fn,packages/solid/store/src/server.ts,19,function isWrappable(obj: any) {
  packages/solid/store/src/server::unwrap,fn,packages/solid/store/src/server.ts,27,function unwrap<T>(item: T): T {
  packages/solid/store/src/server::setProperty,fn,packages/solid/store/src/server.ts,31,"function setProperty(state: any, property: PropertyKey, value: any, force?: boolean) {"
  packages/solid/store/src/server::mergeStoreNode,fn,packages/solid/store/src/server.ts,38,"function mergeStoreNode(state: any, value: any, force?: boolean) {"
  packages/solid/store/src/server::updateArray,fn,packages/solid/store/src/server.ts,46,function updateArray(
  packages/solid/store/src/server::updatePath,fn,packages/solid/store/src/server.ts,63,"function updatePath(current: any, path: any[], traversed: PropertyKey[] = []) {"
  packages/solid/store/src/server::createStore,fn,packages/solid/store/src/server.ts,108,"function createStore<T>(state: T | Store<T>): [Store<T>, SetStoreFunction<T>] {"
  packages/solid/store/src/server::setStore,fn,packages/solid/store/src/server.ts,110,function setStore(...args: any[]): void {
  packages/solid/store/src/server::createMutable,fn,packages/solid/store/src/server.ts,116,"function createMutable<T>(state: T | Store<T>): T {"
  packages/solid/store/src/server::modifyMutable,fn,packages/solid/store/src/server.ts,120,"function modifyMutable<T>(state: T, modifier: (state: T) => T) {"
  packages/solid/store/src/server::reconcile,fn,packages/solid/store/src/server.ts,130,"function reconcile<T extends U, U extends object>("
  packages/solid/store/src/server::produce,fn,packages/solid/store/src/server.ts,150,function produce<T>(fn: (state: T) => void): (state: T) => T {
  packages/solid/store/src/store::SolidStore,namespace,packages/solid/store/src/store.ts,34,namespace SolidStore {
  packages/solid/store/src/store::wrap,fn,packages/solid/store/src/store.ts,49,function wrap<T extends StoreNode>(value: T): T {
  packages/solid/store/src/store::isWrappable,fn,packages/solid/store/src/store.ts,71,function isWrappable(obj: any) {
  packages/solid/store/src/store::unwrap,fn,packages/solid/store/src/store.ts,95,"function unwrap<T>(item: any, set = new Set()): T {"
  packages/solid/store/src/store::getNodes,fn,packages/solid/store/src/store.ts,122,"function getNodes(target: StoreNode, symbol: typeof $NODE | typeof $HAS): DataNodes {"
  packages/solid/store/src/store::getNode,fn,packages/solid/store/src/store.ts,129,"function getNode(nodes: DataNodes, property: PropertyKey, value?: any) {"
  packages/solid/store/src/store::proxyDescriptor,fn,packages/solid/store/src/store.ts,139,"function proxyDescriptor(target: StoreNode, property: PropertyKey) {"
  packages/solid/store/src/store::trackSelf,fn,packages/solid/store/src/store.ts,149,function trackSelf(target: StoreNode) {
  packages/solid/store/src/store::ownKeys,fn,packages/solid/store/src/store.ts,153,function ownKeys(target: StoreNode) {
  packages/solid/store/src/store::setProperty,fn,packages/solid/store/src/store.ts,212,function setProperty(
  packages/solid/store/src/store::mergeStoreNode,fn,packages/solid/store/src/store.ts,243,"function mergeStoreNode(state: StoreNode, value: Partial<StoreNode>) {"
  packages/solid/store/src/store::updateArray,fn,packages/solid/store/src/store.ts,251,function updateArray(
  packages/solid/store/src/store::updatePath,fn,packages/solid/store/src/store.ts,269,"function updatePath(current: StoreNode, path: any[], traversed: PropertyKey[] = []) {"
  packages/solid/store/src/store::createStore,fn,packages/solid/store/src/store.ts,501,function createStore<T extends object = {}>(
  packages/solid/store/src/store::setStore,fn,packages/solid/store/src/store.ts,514,function setStore(...args: any[]): void {
  packages/solid/src/reactive/array::dispose,fn,packages/solid/src/reactive/array.ts,13,function dispose(d: (() => void)[]) {
  packages/solid/src/reactive/array::mapArray,fn,packages/solid/src/reactive/array.ts,49,"function mapArray<T, U>("
  packages/solid/src/reactive/array::mapper,fn,packages/solid/src/reactive/array.ts,167,function mapper(disposer: () => void) {
  packages/solid/src/reactive/array::indexArray,fn,packages/solid/src/reactive/array.ts,186,"function indexArray<T, U>("
  packages/solid/src/reactive/array::mapper,fn,packages/solid/src/reactive/array.ts,245,function mapper(disposer: () => void) {
  packages/solid/src/reactive/scheduler::setupScheduler,fn,packages/solid/src/reactive/scheduler.ts,29,function setupScheduler() {
  packages/solid/src/reactive/scheduler::enqueue,fn,packages/solid/src/reactive/scheduler.ts,87,"function enqueue(taskQueue: Task[], task: Task) {"
  packages/solid/src/reactive/scheduler::findIndex,fn,packages/solid/src/reactive/scheduler.ts,88,function findIndex() {
  packages/solid/src/reactive/scheduler::requestCallback,fn,packages/solid/src/reactive/scheduler.ts,104,"function requestCallback(fn: () => void, options?: { timeout: number }): Task {"
  packages/solid/src/reactive/scheduler::cancelCallback,fn,packages/solid/src/reactive/scheduler.ts,128,function cancelCallback(task: Task) {
  packages/solid/src/reactive/scheduler::flushWork,fn,packages/solid/src/reactive/scheduler.ts,132,function flushWork(initialTime: number) {
  packages/solid/src/reactive/scheduler::workLoop,fn,packages/solid/src/reactive/scheduler.ts,144,function workLoop(initialTime: number) {
  packages/solid/src/reactive/observable::observable,fn,packages/solid/src/reactive/observable.ts,46,function observable<T>(input: Accessor<T>): Observable<T> {
  packages/solid/src/reactive/observable::from,fn,packages/solid/src/reactive/observable.ts,93,function from<T>(
  packages/solid/src/reactive/signal::equalFn,fn,packages/solid/src/reactive/signal.ts,34,"equalFn = <T>(a: T, b: T) => a === b"
  packages/solid/src/reactive/signal::createRoot,fn,packages/solid/src/reactive/signal.ts,150,"function createRoot<T>(fn: RootFunction<T>, detachedOwner?: typeof Owner): T {"
  packages/solid/src/reactive/signal::createSignal,fn,packages/solid/src/reactive/signal.ts,229,function createSignal<T>(
  packages/solid/src/reactive/signal::setter,fn,packages/solid/src/reactive/signal.ts,252,"setter: Setter<T | undefined> = (value?: unknown) => {"
  packages/solid/src/reactive/signal::createComputed,fn,packages/solid/src/reactive/signal.ts,298,"function createComputed<Next, Init>("
  packages/solid/src/reactive/signal::createRenderEffect,fn,packages/solid/src/reactive/signal.ts,329,"function createRenderEffect<Next, Init>("
  packages/solid/src/reactive/signal::createEffect,fn,packages/solid/src/reactive/signal.ts,360,"function createEffect<Next, Init>("
  packages/solid/src/reactive/signal::createReaction,fn,packages/solid/src/reactive/signal.ts,386,"function createReaction(onInvalidate: () => void, options?: EffectOptions) {"
  packages/solid/src/reactive/signal::createMemo,fn,packages/solid/src/reactive/signal.ts,442,"function createMemo<Next extends Prev, Init, Prev>("
  packages/solid/src/reactive/signal::isPromise,fn,packages/solid/src/reactive/signal.ts,548,function isPromise(v: any): v is Promise<any> {
  packages/solid/src/reactive/signal::createResource,fn,packages/solid/src/reactive/signal.ts,598,"function createResource<T, S, R>("
  packages/solid/src/reactive/signal::loadEnd,fn,packages/solid/src/reactive/signal.ts,641,"function loadEnd(p: Promise<T> | null, v: T | undefined, error?: any, key?: S) {"
  packages/solid/src/reactive/signal::completeLoad,fn,packages/solid/src/reactive/signal.ts,659,"function completeLoad(v: T | undefined, err: any) {"
  packages/solid/src/reactive/signal::read,fn,packages/solid/src/reactive/signal.ts,669,function read() {
  packages/solid/src/reactive/signal::load,fn,packages/solid/src/reactive/signal.ts,688,"function load(refetching: R | boolean = true) {"
  packages/solid/src/reactive/signal::createDeferred,fn,packages/solid/src/reactive/signal.ts,782,"function createDeferred<T>(source: Accessor<T>, options?: DeferredOptions<T>) {"
  packages/solid/src/reactive/signal::createSelector,fn,packages/solid/src/reactive/signal.ts,834,"function createSelector<T, U = T>("
  packages/solid/src/reactive/signal::batch,fn,packages/solid/src/reactive/signal.ts,884,function batch<T>(fn: Accessor<T>): T {
  packages/solid/src/reactive/signal::untrack,fn,packages/solid/src/reactive/signal.ts,895,function untrack<T>(fn: Accessor<T>): T {
  packages/solid/src/reactive/signal::on,fn,packages/solid/src/reactive/signal.ts,965,"function on<S, Next extends Prev, Prev = Next>("
  packages/solid/src/reactive/signal::onMount,fn,packages/solid/src/reactive/signal.ts,995,function onMount(fn: () => void) {
  packages/solid/src/reactive/signal::onCleanup,fn,packages/solid/src/reactive/signal.ts,1007,function onCleanup<T extends () => any>(fn: T): T {
  packages/solid/src/reactive/signal::catchError,fn,packages/solid/src/reactive/signal.ts,1024,"function catchError<T>(fn: () => T, handler: (err: Error) => void) {"
  packages/solid/src/reactive/signal::getListener,fn,packages/solid/src/reactive/signal.ts,1038,function getListener() {
  packages/solid/src/reactive/signal::getOwner,fn,packages/solid/src/reactive/signal.ts,1042,function getOwner() {
  packages/solid/src/reactive/signal::runWithOwner,fn,packages/solid/src/reactive/signal.ts,1046,"function runWithOwner<T>(o: typeof Owner, fn: () => T): T | undefined {"
  packages/solid/src/reactive/signal::enableScheduling,fn,packages/solid/src/reactive/signal.ts,1062,function enableScheduling(scheduler = requestCallback) {
  packages/solid/src/reactive/signal::startTransition,fn,packages/solid/src/reactive/signal.ts,1073,function startTransition(fn: () => unknown): Promise<void> {
  packages/solid/src/reactive/signal::useTransition,fn,packages/solid/src/reactive/signal.ts,1120,function useTransition(): Transition {
  packages/solid/src/reactive/signal::resumeEffects,fn,packages/solid/src/reactive/signal.ts,1124,function resumeEffects(e: Computation<any>[]) {
  packages/solid/src/reactive/signal::devComponent,fn,packages/solid/src/reactive/signal.ts,1136,"function devComponent<P, V>(Comp: (props: P) => V, props: P): V {"
  packages/solid/src/reactive/signal::registerGraph,fn,packages/solid/src/reactive/signal.ts,1156,function registerGraph(value: SourceMapValue): void {
  packages/solid/src/reactive/signal::createContext,fn,packages/solid/src/reactive/signal.ts,1198,function createContext<T>(
  packages/solid/src/reactive/signal::useContext,fn,packages/solid/src/reactive/signal.ts,1214,function useContext<T>(context: Context<T>): T {
  packages/solid/src/reactive/signal::children,fn,packages/solid/src/reactive/signal.ts,1233,function children(fn: Accessor<JSX.Element>): ChildrenReturn {
  packages/solid/src/reactive/signal::getSuspenseContext,fn,packages/solid/src/reactive/signal.ts,1262,function getSuspenseContext() {
  packages/solid/src/reactive/signal::enableExternalSource,fn,packages/solid/src/reactive/signal.ts,1267,function enableExternalSource(
  packages/solid/src/reactive/signal::readSignal,fn,packages/solid/src/reactive/signal.ts,1293,"function readSignal(this: SignalState<any> | Memo<any>) {"
  packages/solid/src/reactive/signal::writeSignal,fn,packages/solid/src/reactive/signal.ts,1329,"function writeSignal(node: SignalState<any> | Memo<any>, value: any, isComp?: boolean) {"
  packages/solid/src/reactive/signal::updateComputation,fn,packages/solid/src/reactive/signal.ts,1366,function updateComputation(node: Computation<any>) {
  packages/solid/src/reactive/signal::runComputation,fn,packages/solid/src/reactive/signal.ts,1390,"function runComputation(node: Computation<any>, value: any, time: number) {"
  packages/solid/src/reactive/signal::createComputation,fn,packages/solid/src/reactive/signal.ts,1427,"function createComputation<Next, Init = unknown>("
  packages/solid/src/reactive/signal::triggerInTransition,fn,packages/solid/src/reactive/signal.ts,1474,triggerInTransition: () => void = () =>
  packages/solid/src/reactive/signal::runTop,fn,packages/solid/src/reactive/signal.ts,1488,function runTop(node: Computation<any>) {
  packages/solid/src/reactive/signal::runUpdates,fn,packages/solid/src/reactive/signal.ts,1521,"function runUpdates<T>(fn: () => T, init: boolean) {"
  packages/solid/src/reactive/signal::completeUpdates,fn,packages/solid/src/reactive/signal.ts,1539,function completeUpdates(wait: boolean) {
  packages/solid/src/reactive/signal::runQueue,fn,packages/solid/src/reactive/signal.ts,1589,function runQueue(queue: Computation<any>[]) {
  packages/solid/src/reactive/signal::scheduleQueue,fn,packages/solid/src/reactive/signal.ts,1593,function scheduleQueue(queue: Computation<any>[]) {
  packages/solid/src/reactive/signal::runUserEffects,fn,packages/solid/src/reactive/signal.ts,1611,function runUserEffects(queue: Computation<any>[]) {
  packages/solid/src/reactive/signal::lookUpstream,fn,packages/solid/src/reactive/signal.ts,1635,"function lookUpstream(node: Computation<any>, ignore?: Computation<any>) {"
  packages/solid/src/reactive/signal::markDownstream,fn,packages/solid/src/reactive/signal.ts,1651,function markDownstream(node: Memo<any>) {
  packages/solid/src/reactive/signal::cleanNode,fn,packages/solid/src/reactive/signal.ts,1665,function cleanNode(node: Owner) {
  packages/solid/src/reactive/signal::reset,fn,packages/solid/src/reactive/signal.ts,1705,"function reset(node: Computation<any>, top?: boolean) {"
  packages/solid/src/reactive/signal::castError,fn,packages/solid/src/reactive/signal.ts,1715,function castError(err: unknown): Error {
  packages/solid/src/reactive/signal::runErrors,fn,packages/solid/src/reactive/signal.ts,1720,"function runErrors(err: unknown, fns: ((err: any) => void)[], owner: Owner | null) {"
  packages/solid/src/reactive/signal::handleError,fn,packages/solid/src/reactive/signal.ts,1728,"function handleError(err: unknown, owner = Owner) {"
  packages/solid/src/reactive/signal::resolveChildren,fn,packages/solid/src/reactive/signal.ts,1743,"function resolveChildren(children: JSX.Element | Accessor<any>): ResolvedChildren {"
  packages/solid/src/reactive/signal::createProvider,fn,packages/solid/src/reactive/signal.ts,1756,"function createProvider(id: symbol, options?: EffectOptions) {"
  packages/solid/src/reactive/signal::onError,fn,packages/solid/src/reactive/signal.ts,1783,function onError(fn: (err: Error) => void): void {
  packages/solid/src/reactive/signal::mutateContext,fn,packages/solid/src/reactive/signal.ts,1795,"function mutateContext(o: Owner, key: symbol, value: any) {"
  packages/solid/src/render/component::enableHydration,fn,packages/solid/src/render/component.ts,17,function enableHydration() {
  packages/solid/src/render/component::createComponent,fn,packages/solid/src/render/component.ts,96,"function createComponent<T extends Record<string, any>>("
  packages/solid/src/render/component::trueFn,fn,packages/solid/src/render/component.ts,115,function trueFn() {
  packages/solid/src/render/component::resolveSource,fn,packages/solid/src/render/component.ts,187,function resolveSource(s: any) {
  packages/solid/src/render/component::resolveSources,fn,packages/solid/src/render/component.ts,191,function resolveSources(this: (() => any)[]) {
  packages/solid/src/render/component::mergeProps,fn,packages/solid/src/render/component.ts,198,function mergeProps<T extends unknown[]>(...sources: T): MergeProps<T> {
  packages/solid/src/render/component::splitProps,fn,packages/solid/src/render/component.ts,287,function splitProps<
  packages/solid/src/render/component::lazy,fn,packages/solid/src/render/component.ts,356,function lazy<T extends Component<any>>(
  packages/solid/src/render/component::createUniqueId,fn,packages/solid/src/render/component.ts,398,function createUniqueId(): string {
  packages/solid/src/render/hydration::getContextId,fn,packages/solid/src/render/hydration.ts,32,function getContextId(count: number) {
  packages/solid/src/render/hydration::setHydrateContext,fn,packages/solid/src/render/hydration.ts,38,function setHydrateContext(context?: HydrationContext): void {
  packages/solid/src/render/hydration::nextHydrateContext,fn,packages/solid/src/render/hydration.ts,42,"function nextHydrateContext(): HydrationContext | undefined {"
  packages/solid/src/render/flow::narrowedError,fn,packages/solid/src/render/flow.ts,16,narrowedError = (name: string) =>
  packages/solid/src/render/flow::For,fn,packages/solid/src/render/flow.ts,34,"function For<T extends readonly any[], U extends JSX.Element>(props: {"
  packages/solid/src/render/flow::Index,fn,packages/solid/src/render/flow.ts,64,"function Index<T extends readonly any[], U extends JSX.Element>(props: {"
  packages/solid/src/render/flow::Show,fn,packages/solid/src/render/flow.ts,101,function Show<T>(props: {
  packages/solid/src/render/flow::Switch,fn,packages/solid/src/render/flow.ts,167,function Switch(props: { fallback?: JSX.Element; children: JSX.Element }): JSX.Element {
  packages/solid/src/render/flow::func,fn,packages/solid/src/render/flow.ts,172,"func: Accessor<EvalConditions | undefined> = () => undefined"
  packages/solid/src/render/flow::Match,fn,packages/solid/src/render/flow.ts,250,function Match<T>(props: MatchProps<T>) {
  packages/solid/src/render/flow::resetErrorBoundaries,fn,packages/solid/src/render/flow.ts,255,function resetErrorBoundaries() {
  # ... 81 more symbols omitted

hierarchies[9]{symbol,relationship,target,file,line}:
  packages/solid/test/signals.type-tests::Dog,extends,Animal,packages/solid/test/signals.type-tests.ts,17
  packages/solid/store/test/mutableWithClass.spec::B,extends,A,packages/solid/store/test/mutableWithClass.spec.tsx,64
  packages/solid/src/reactive/signal::Signal,contains,Accessor,packages/solid/src/reactive/signal.ts,198
  packages/solid/src/reactive/signal::Signal,contains,Setter,packages/solid/src/reactive/signal.ts,198
  packages/solid/src/reactive/signal::AccessorArray,contains,Accessor,packages/solid/src/reactive/signal.ts,916
  packages/solid/src/server/reactive::Signal,contains,Accessor,packages/solid/src/server/reactive.ts,13
  packages/solid/src/server/reactive::Signal,contains,Setter,packages/solid/src/server/reactive.ts,13
  packages/solid/src/server/rendering::ResourceActions,contains,Setter,packages/solid/src/server/rendering.ts,380
  packages/solid/src/server/rendering::ResourceFetcher,contains,ResourceFetcherInfo,packages/solid/src/server/rendering.ts,386

dependencies[34]{name,version,category}:
  @babel/cli,^7.18.9,dev
  @babel/core,^7.20.12,dev
  @babel/preset-env,^7.18.9,dev
  @babel/preset-typescript,^7.18.6,dev
  @changesets/cli,^2.25.2,dev
  @rollup/plugin-babel,^6.0.3,dev
  @rollup/plugin-commonjs,^24.0.0,dev
  @rollup/plugin-json,^6.0.0,dev
  @rollup/plugin-node-resolve,^15.0.1,dev
  @rollup/plugin-replace,^5.0.2,dev
  @types/node,^22.7.5,dev
  @vitest/coverage-v8,^2.1.2,dev
  babel-plugin-jsx-dom-expressions,^0.40.3,dev
  coveralls,^3.1.1,dev
  csstype,^3.1.0,dev
  dom-expressions,0.40.4,dev
  hyper-dom-expressions,0.40.4,dev
  jsdom,^25.0.1,dev
  lit-dom-expressions,0.40.4,dev
  ncp,^2.0.0,dev
  npm-run-all,^4.1.5,dev
  prettier,^3.6.2,dev
  rimraf,^3.0.2,dev
  rollup,^4.24.0,dev
  rollup-plugin-cleanup,^3.2.1,dev
  rollup-plugin-copy,^3.4.0,dev
  seroval,~1.5.0,dev
  simple-git-hooks,^2.8.1,dev
  symlink-dir,^5.0.1,dev
  tsconfig-replace-paths,^0.0.11,dev
  turbo,^1.3.1,dev
  typescript,~5.7.2,dev
  vite-plugin-solid,^2.6.1,dev
  vitest,^2.1.2,dev
```
