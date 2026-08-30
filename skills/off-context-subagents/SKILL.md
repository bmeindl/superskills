---
name: off-context-subagents
description: Decide when a task should run in an off-context sub-agent instead of the main session, brief it so it can succeed without you, and validate what comes back. Use when research, bulk file reading, or a second opinion would flood the main context, when model diversity is wanted as a cross-check, or when setting up the sub-agent-mcp server for a workspace.
---

# Off-context sub-agents

The main agent's context window is the scarce resource. Native sub-agent calls stream everything back into it; an *off-context* sub-agent runs as a separate process and returns only its final answer. This skill is the procedure; the server that makes it possible is [sub-agent-mcp](https://github.com/bmeindl/sub-agent-mcp) (MCP server that hands tasks to background [opencode](https://opencode.ai) processes, any model, default-deny filesystem). This catalogue does not ship or install the server — it links to it.

## 1. Delegate or not

Delegate when the *work* is heavy but the *answer* is small: multi-file research, log or transcript digestion, isolated web research, mechanical bulk edits, or a second opinion from a different model. Keep in the main session when the task needs your other tools (ticketing, docs, analytics MCPs — sub-agents only see opencode's built-ins), when watching the reasoning is the point, or when you would finish in a handful of tool calls yourself. Delegate tasks, never responsibility: a sub-agent that reports "all fine" delivers input, not a verdict.

## 2. Brief

A fresh agent knows nothing. Give it: the goal and WHY it matters, the exact deliverable (format, length), file paths it may read, the framing or persona ("skeptical senior engineer", "ex-Bloomberg designer"), and what it should NOT do. For a second opinion, state the options and ask for a verdict first, no hedging. Parallel sub-agents on the same question get *distinct* personas — otherwise they converge.

## 3. Choose the model

Pick by capability tier, not by name: a mid-tier model is the workhorse for research and mechanics; top-tier only where judgement hangs (review, challenge, creative work); a cheap fast model only for simple scans. For validation, deliberately use a model from a *different* vendor than the main session.

## 4. Scope the sandbox

Grant the narrowest read/write directories that let the task succeed; the server denies everything else by default. Never point a sub-agent at credential folders. If it must write, give it a scratch directory and review before merging anything into the workspace.

## 5. Validate

Read the result as evidence, not as truth: cross-check any specific it asserts (dates, hashes, "it's nothing") before acting on it, especially when a single sub-agent sounds confident. Never end a turn with a sub-agent still running — its result lands on disk and nobody reads it. Record 2–3 lines of what it found in the working state if that appears in no file.

## Setting up the server

Follow the Quick start in the [sub-agent-mcp README](https://github.com/bmeindl/sub-agent-mcp#readme): install opencode, register the MCP server in the client's MCP config, and map tiers to models in a private `tiers.toml` outside the workspace. The server ships no provider defaults; the model mapping is the user's, and connecting a provider is their own login step.
