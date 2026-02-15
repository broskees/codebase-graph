# @codebase-graph/opencode-plugin

OpenCode plugin that injects a live codebase structural map into every LLM system prompt.

## How It Works

1. On plugin load, spawns `codebase-graph --watch` as a child process to keep `.codebase.md` up to date
2. On every LLM call, reads `.codebase.md` from disk and pushes it onto the system prompt
3. The agent always has a current structural map of the codebase — modules, symbols, hierarchies, dependencies

## Installation

### Prerequisites

Install the `codebase-graph` CLI tool so it's available on your PATH:

```bash
pip install codebase-graph
# or
pipx install codebase-graph
```

Verify it works:

```bash
codebase-graph --version
```

### Add to OpenCode

**Option A: Local plugin (recommended for now)**

Copy the plugin file into your project or global plugin directory:

```bash
# Project-level (just this project)
mkdir -p .opencode/plugins
cp plugins/opencode/index.ts .opencode/plugins/codebase-graph.ts

# Global (all projects)
cp plugins/opencode/index.ts ~/.config/opencode/plugins/codebase-graph.ts
```

Local plugins are automatically loaded at startup — no config changes needed.

**Option B: From npm (when published)**

Add the plugin to your OpenCode config (`opencode.json`):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["@codebase-graph/opencode-plugin"]
}
```

## Verifying It Works

1. Start OpenCode in a project directory
2. Check that `.codebase.md` appears in the project root (may take a moment on first run)
3. The structural map is automatically included in every LLM call — no action needed

## Troubleshooting

### `.codebase.md` not appearing

- Ensure `codebase-graph` is in your PATH: `which codebase-graph`
- Try running it manually: `codebase-graph --watch --dir .`
- Check that the project directory contains supported files (`.py`, `.ts`, `.tsx`, `.js`, `.jsx`)

### Plugin not loading

- Check OpenCode logs for plugin errors
- Ensure `@opencode-ai/plugin` peer dependency is satisfied

## How It Integrates

```
codebase-graph --watch     →  writes .codebase.md on disk
                               ↓
OpenCode plugin hook       →  reads .codebase.md on every LLM call
                               ↓
System prompt              →  agent sees live structural map
```

The plugin is ~25 lines of TypeScript. All the heavy lifting (parsing, watching, TOON serialization) happens in the `codebase-graph` binary.
