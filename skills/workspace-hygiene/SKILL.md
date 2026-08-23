---
name: workspace-hygiene
description: "Run a staged, reversible hygiene pass over an agent workspace: drain scratch, route loose files, repair indexes, identify stale instructions, and reduce clutter without deleting user material. Use when the workspace feels messy, files have accumulated in the wrong places, indexes drift, scratch grows large, or the user asks for cleanup or maintenance."
---

# Workspace hygiene

Reduce drift without turning cleanup into a redesign. Inspect the workspace's own README or map before moving anything.

## Staged pass

Run only the stages that have evidence of drift:

1. **Mechanical health** — malformed files, broken local links, duplicate indexes, ignored runtime data, accidental credential-shaped files.
2. **Scratch drain** — route durable facts, active work, and disposable notes; preserve attribution and source links.
3. **Loose-file routing** — propose destinations based on content and status, not filename alone.
4. **Index repair** — update the manifest or README that readers actually use.
5. **Instruction audit** — flag stale or contradictory operating rules; do not rewrite core instructions silently.
6. **Declutter** — archive or quarantine superseded artifacts; delete only when the user has explicitly approved the exact targets.

## Safety rules

- Show the proposed moves and deletions before applying them.
- Prefer a recoverable archive/trash path over permanent deletion.
- Never sweep a workspace root recursively through an unresolved variable or glob.
- Preserve unknown files and unrelated dirty changes.
- Treat active plans differently from finished one-off reports; status decides placement.
- Keep temporary run state out of durable architecture or context files.

## Finish

Verify moved links, manifests, and startup instructions. Report what changed, what was intentionally left alone, and whether any manual decision remains. A clean pass with nothing to change is a valid outcome.
