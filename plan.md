# Codebase Graph

A standalone tool that gives AI coding agents a **live, token-efficient structural map** of the codebase — injected into the system prompt on every LLM call, updated in real-time as files change.

**Zero API keys. Zero network calls. Fully offline. MIT licensed.**

---

## The Problem

Coding agents waste significant tokens and latency exploring codebases they don't understand. They grep, open files, scan directories — all to build a mental model that could have been handed to them upfront.

## The Solution

A ~2-5K token compressed map of the entire codebase — modules, symbols, type hierarchies, call graphs, dependencies — with file paths and line numbers. Always current. Injected invisibly into the system prompt before every LLM call.

The agent starts every turn knowing:
- What modules exist and what they do
- Every important type and its shape
- How types relate (inheritance, composition, references)
- The call graph between key functions
- Exact file paths and line numbers (updated on every file save)

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                   codebase-graph                     │
│                                                      │
│  ┌──────────┐   ┌──────────┐   ┌────────────────┐   │
│  │ Watcher  │ → │ Kit      │ → │ Graph Builder  │   │
│  │(watchfiles)│  │(symbols) │   │(cluster, rels) │   │
│  └──────────┘   └──────────┘   └───────┬────────┘   │
│                                         │            │
│                                ┌────────▼────────┐   │
│                                │  .codebase.md   │   │
│                                │  (md + toon)    │   │
│                                └────────┬────────┘   │
└─────────────────────────────────────────┼────────────┘
                                          │
                              ┌───────────▼───────────┐
                              │   OpenCode Plugin     │
                              │                       │
                              │ experimental.chat     │
                              │ .system.transform     │
                              │                       │
                              │ Reads .codebase.md    │
                              │ fresh on EVERY LLM    │
                              │ call. Pushes onto     │
                              │ output.system[]       │
                              │                       │
                              │ Works for ALL         │
                              │ providers (API key    │
                              │ + OAuth alike)        │
                              └───────────────────────┘
```

---

## How It Works (OpenCode)

### The Hook: `experimental.chat.system.transform`

OpenCode's plugin SDK exposes a hook that fires **before every single LLM call**, for **all providers** (Anthropic, OpenAI, Copilot OAuth, OpenRouter, local models — everything). It operates at the prompt assembly layer, after auth is resolved, before the provider-specific HTTP request is constructed [1].

```typescript
"experimental.chat.system.transform"?: (
  input: { sessionID?: string; model: Model },
  output: { system: string[] },
) => Promise
```

The plugin reads `.codebase.md` from disk and pushes it onto `output.system`. Since the hook fires on every LLM call and we read from disk each time, the agent always has the latest map — even mid-session as it creates and edits files.

No proxy. No URL swapping. No OAuth workaround. The hook is provider-agnostic by design.

### The Plugin (~20 lines)

```typescript
import type { Hooks, PluginInput } from "@opencode-ai/plugin"
import { readFileSync } from "fs"
import { join } from "path"
import { spawn } from "child_process"

export default async function codebaseGraph(input: PluginInput): Promise<Hooks> {
  const briefingPath = join(input.directory, ".codebase.md")

  // Spawn watcher daemon
  spawn("codebase-graph", [
    "--watch", "--dir", input.directory,
  ], { stdio: "ignore", detached: false })

  return {
    "experimental.chat.system.transform": async (_incoming, output) => {
      try {
        const briefing = readFileSync(briefingPath, "utf-8")
        output.system.push(briefing)
      } catch {
        // File doesn't exist yet (first index in progress), skip
      }
    },
  }
}
```

That's the entire plugin. Everything else lives in the `codebase-graph` binary.

---

## Output Format: `.codebase.md`

The output is a markdown file with prompt framing that tells the model this data is **live and current**, wrapping a TOON (Token-Oriented Object Notation) codeblock for maximum token efficiency.

```markdown
## Live Codebase Map

The following is a **real-time structural map** of this codebase. It was
regenerated moments ago and reflects the current state of all files on disk.

All file paths and line numbers are accurate right now. When you edit a file,
this map updates before your next turn.

Use this map to navigate directly to the right files and line numbers without
searching. Trust these locations — they are current.

​```toon
codebase:
  name: my-project
  languages[2]: typescript,python
  last_indexed: 2026-02-15T21:15:00Z

modules[N]{name,path,key_types,depends_on}:
  auth,src/auth,"User|Session|Credentials","database|config"
  orders,src/orders,"Order|OrderItem|OrderStatus","auth|inventory|payments"
  ...

symbols[N]{fqn,kind,file,line,signature}:
  auth::login,fn,src/auth/login.ts,42,"(creds: Credentials) => Promise<Session>"
  auth::User,interface,src/auth/models.ts,8,"{id: string, name: string, email: string}"
  ...

hierarchies[N]{symbol,relationship,target,file,line}:
  auth::User,implements,Authenticatable,src/auth/models.ts,28
  orders::Order,contains,"OrderItem[]",src/orders/types.ts,10
  ...

call_graph[N]{caller,callee,file,line}:
  orders::createOrder,auth::requireLogin,src/orders/service.ts,16
  orders::createOrder,inventory::reserveItems,src/orders/service.ts,22
  ...

dependencies[N]{name,version,category}:
  express,4.18.2,runtime
  prisma,5.10.0,runtime
  typescript,5.4.0,dev
  ...
​```
```

### Why TOON Inside Markdown

- **TOON** saves 40-60% tokens vs JSON for tabular data (symbols, hierarchies, etc.) by declaring field names once per table
- **Markdown wrapper** provides the prompt framing that tells the model this is live data, not stale documentation
- **~2-5K tokens total** for a substantial codebase — cheap enough to include on every turn

---

## Core Binary: `codebase-graph`

### Parser: Kit (cased/kit)

We use [Kit](https://github.com/cased/kit) as the parsing layer. It handles tree-sitter grammar management and per-language symbol extraction for 12+ languages out of the box via a plugin system. MIT licensed, 1.3K+ stars, actively maintained.

Kit provides:
- Symbol extraction (functions, classes, structs, traits, enums, interfaces) with names, kinds, signatures, line numbers
- Incremental extraction (cache-aware, fast on re-runs)
- Symbol usage tracking (`find_symbol_usages`)
- File tree listing

We build on top of Kit:
- **Module clustering** — group symbols by directory, sub-cluster large modules
- **Hierarchy extraction** — infer implements/extends/contains/references from symbol data
- **Call graph** — match call expressions against known function names (import-aware)
- **Manifest parsing** — extract dependencies from package.json, Cargo.toml, pyproject.toml, etc.
- **TOON serialization** — output the schema above

### Watcher

Uses `watchfiles` (Rust-backed, cross-platform) to detect file changes.

- Respects `.gitignore` as primary filter
- Falls back to hardcoded ignore list (`node_modules`, `dist`, `target`, `__pycache__`, etc.)
- Content-hash diffing to skip files touched but not changed
- On change: re-parse changed file(s) only via Kit's incremental API, rebuild affected graph sections, rewrite `.codebase.md`

### Incremental Update Pipeline

```
File saved to disk
  → Watcher detects change (watchfiles, ~1ms)
  → Content hash compared — skip if unchanged
  → Kit re-parses changed file(s) (incremental, <10ms per file)
  → Diff symbols against previous parse
  → Identify affected modules
  → Rebuild affected rows in symbols/hierarchies/call_graph tables
  → Re-serialize .codebase.md
  → Write to disk
  → Next LLM call reads fresh file via plugin hook
```

**Performance budget:**
- File change detection: < 1ms
- Kit incremental re-parse (single file): < 10ms
- Graph diff + TOON regeneration: < 40ms
- **Total incremental update: < 50ms**
- Full cold index (50K LOC): < 1 second

### CLI

```bash
# Generate .codebase.md for a project
codebase-graph ./my-project

# Watch mode — keep .codebase.md updated on file changes
codebase-graph --watch --dir ./my-project

# JSON output instead of TOON
codebase-graph ./my-project --format json

# Scope to workspace in a monorepo
codebase-graph ./my-project --scope packages/api

# Custom output path
codebase-graph ./my-project --output ./my-briefing.md
```

---

## TOON Schema

### `codebase` (metadata)

```toon
codebase:
  name: {project_name}
  languages[N]: {lang1},{lang2}
  last_indexed: {ISO timestamp}
```

### `modules` (directory-based groupings)

```toon
modules[N]{name,path,key_types,depends_on}:
```

Fields: module name, filesystem path, pipe-delimited key type names, pipe-delimited dependency module names.

### `symbols` (functions, classes, structs, traits, enums, interfaces)

```toon
symbols[N]{fqn,kind,file,line,signature}:
```

Fields: fully qualified name, kind (fn/struct/class/trait/enum/interface), file path, line number, signature as written in source.

### `hierarchies` (type relationships)

```toon
hierarchies[N]{symbol,relationship,target,file,line}:
```

Relationships: `implements`, `extends`, `contains`, `references`.

### `call_graph` (function call relationships)

```toon
call_graph[N]{caller,callee,file,line}:
```

### `dependencies` (from manifest files)

```toon
dependencies[N]{name,version,category}:
```

Category: `runtime` or `dev`. Parsed from package.json, Cargo.toml, pyproject.toml, go.mod, Gemfile, etc.

---

## File Ignore Strategy

Priority order:
1. **`.gitignore`** — primary filter, always respected
2. **Hardcoded defaults** — `node_modules`, `dist`, `target`, `.venv`, `__pycache__`, `build`, `out`, `.next`, `coverage`, etc.
3. **`.codebasegraphignore`** — optional user overrides (same syntax as `.gitignore`)
4. **`--scope` flag** — for monorepo workspace scoping

Manifest files (package.json, Cargo.toml, etc.) are **read for dependency info** but their referenced dependency directories are never parsed.

---

## Monorepo Support

- Detect workspace configuration (`pnpm-workspace.yaml`, `package.json` workspaces, Cargo workspace)
- `--scope` flag limits parsing to a specific workspace package
- Auto-include sibling packages that are imported by the scoped package
- Each workspace can have its own `.codebase.md`

---

## Project Structure

```
codebase-graph/
├── src/
│   ├── core/
│   │   ├── watcher.py          # File watcher, .gitignore parsing
│   │   ├── parser.py           # Kit wrapper for symbol extraction
│   │   ├── graph.py            # Module clustering, hierarchy/call graph inference
│   │   ├── writer.py           # Markdown + TOON serialization
│   │   └── manifest.py         # package.json, Cargo.toml, pyproject.toml parsing
│   └── cli.py                  # CLI entry point
├── plugins/
│   └── opencode/               # OpenCode plugin (< 30 lines TS)
│       └── index.ts
├── tests/
├── pyproject.toml              # Kit as a dependency
├── LICENSE                     # MIT
└── README.md
```

---

## Milestones

### v0.1 — MVP
- [ ] Kit-based symbol extraction (TypeScript + Python)
- [ ] Directory-based module clustering
- [ ] `.codebase.md` output with TOON schema + prompt framing
- [ ] `.gitignore` respect + hardcoded ignore list
- [ ] Manifest parsing (package.json, pyproject.toml)
- [ ] CLI: `codebase-graph ./path`
- [ ] CLI: `--watch` mode
- [ ] Line numbers and file paths for all symbols
- [ ] OpenCode plugin using `experimental.chat.system.transform`

### v0.2 — More Languages + Monorepo
- [ ] Rust, Go language support (via Kit)
- [ ] Monorepo workspace detection and scoping
- [ ] `.codebasegraphignore` support
- [ ] JSON output format option
- [ ] Hierarchy extraction (implements/extends/contains)

### v0.3 — Call Graph + Polish
- [ ] Call graph inference (import-aware function call matching)
- [ ] Optional LLM-generated module summaries (`--summarize` flag)
- [ ] Config file (`.codebasegraph.toml`) for project-specific settings
- [ ] Performance benchmarks on large repos

### v0.4 — Other Harnesses
- [ ] Claude Code integration (CLAUDE.md append or plugin if available)
- [ ] Cursor integration (.cursor/rules/*.mdc)
- [ ] Aider integration (--system-prompt-file)
- [ ] Generic static file fallback for unsupported harnesses

---

## Design Principles

1. **Offline first** — no API keys, no network calls for core functionality
2. **Fast** — cold index under 1 second, incremental under 50ms
3. **Live** — map updates before the next LLM call, not just per-session
4. **Invisible** — system prompt injection via plugin hook, agent doesn't know it's there
5. **Schema is the contract** — TOON schema is stable; parser backends are swappable (Kit/tree-sitter now, SCIP later if needed)
6. **Respect conventions** — `.gitignore`, manifest files, workspace configs
7. **Provider-agnostic** — works with OAuth (Copilot), API keys (Anthropic/OpenAI), local models — all the same

---

## Why This Works

The `experimental.chat.system.transform` hook in OpenCode operates at the prompt assembly layer — after auth is resolved, before the provider-specific HTTP request is constructed [1]. This means:

- **Copilot OAuth?** Works. The hook fires before the Copilot provider's custom `fetch()` with bearer token.
- **Anthropic API key?** Works. Same hook, different provider.
- **Local model?** Works. Same hook.
- **Mid-session updates?** Works. `readFileSync` on every call reads the latest `.codebase.md` from disk.

The plugin doesn't touch auth, doesn't touch URLs, doesn't know or care what provider is in use. It just pushes a string onto `output.system[]`.

---

## License

MIT
