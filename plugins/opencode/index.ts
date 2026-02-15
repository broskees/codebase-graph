import type { Plugin } from "@opencode-ai/plugin"
import { readFileSync } from "fs"
import { join } from "path"
import { spawn } from "child_process"

export const CodebaseGraph: Plugin = async ({ directory }) => {
  const briefingPath = join(directory, ".codebase.md")

  // Spawn watcher daemon — dies when plugin/OpenCode exits
  spawn("codebase-graph", ["--watch", "--dir", directory], {
    stdio: "ignore",
    detached: false,
  })

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
