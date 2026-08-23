---
name: workspace-foundation
description: Assess, create, or repair a portable file-based agent workspace with a clear root, path boundaries, durable context index, scratch inbox, maintenance loop, and documented state stores. Use when starting a new Superboard workspace, when an agent is operating from the wrong folder, when context is scattered or opaque, or when the user wants to switch between Claude, Codex, or another agent without losing working knowledge.
---

# Workspace foundation

Build the smallest workspace that makes the user's work inspectable and portable. Assess first; never replace an existing structure with a template.

## 1. Establish the boundary

Report the current directory and what is already visible inside it. Ask the user to confirm:

- the high-level workspace root;
- related folders or repositories the agent may inspect;
- paths that are off-limits;
- the kinds of work that belong here.

If the current root is one narrow code repository but the board coordinates several areas, recommend a higher-level home and give the exact restart command. Never move files without approval.

## 2. Audit before proposing

Inspect existing agent instructions, context indexes, scratch/inbox files, ignore rules, and skill folders. Also identify state that lives outside the workspace, such as vendor session transcripts or product memory. Distinguish:

- durable workspace truth;
- resumable session state;
- temporary provider caches;
- undocumented or opaque memory.

Do not claim a universal “memory off” setting. Verify each agent product's current settings before recommending a change.

## 3. Propose the minimum scaffold

Fill gaps rather than rebuilding. A blank workspace usually needs only:

- `CLAUDE.md` or `AGENTS.md` — owner, startup route, path boundaries, operating rules;
- `context/README.md` — index of durable knowledge;
- `inbox/scratch.md` — low-friction capture awaiting curation;
- `.gitignore` — runtime data, temporary artifacts, local credentials.

Explain every file and show the proposed content before writing. Keep the first version short enough that the user can read it in one sitting.

## 4. Add a maintenance loop

Define one light, reversible check: inspect loose files, stale indexes, oversized scratch, broken links, and untracked secrets. Prefer moving to a review/archive area over deletion. Do not schedule automation until the manual pass has proved useful.

## 5. Verify and hand off

After approved writes:

1. start a fresh agent session from the confirmed root;
2. verify it reads the intended instructions and context index;
3. ask it to locate one known fact and one path boundary;
4. report which state remains outside the workspace and what that means for portability.

Leave the user with one short map: root, durable files, optional skills, runtime-only data, and the next maintenance check.
