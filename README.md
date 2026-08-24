# Superskills

Optional, public-safe procedures for agent workspaces and [Superboard](https://github.com/bmeindl/superboard).

This repository is deliberately separate from Superboard. Nothing is installed automatically. A user or agent reads one named skill, previews the local adaptation, and copies it into the workspace's skill directory only after approval. The installed copy belongs to that workspace and may diverge; there is no automatic update mechanism.

## Get the catalogue

Check it out **inside** the workspace, as a sibling of the board files:

```sh
git clone https://github.com/bmeindl/superskills.git superskills
```

Superboard's setup cards then reference `superskills/skills/<slug>/SKILL.md`. Absence is a normal offline state: each card carries enough fallback guidance to continue without the catalogue, so cloning is genuinely optional.

Add `superskills/` to the workspace's `.gitignore` if the workspace itself is a git repository — the catalogue is an external checkout, not workspace content.

## Catalogue

| Skill | Use it for | Reads | Authentication |
| --- | --- | --- | --- |
| `workspace-foundation` | Establish a portable workspace and recommend useful skills, tools, and MCPs | Workspace files and available capabilities | None; connecting a recommended tool may lead the user into their own login |
| `email-digest` | Turn recent mail into a useful daily or weekly digest | Mailbox contents | Requires a mail account the user has already connected |
| `mail-triage` | Work a mailbox down in short rounds of real decisions | Mailbox contents | Requires a mail account with permission to move messages |
| `transcript-intake` | Turn a meeting recording or transcript into the right durable note | Transcripts, existing notes, the task list | None; connecting a recording source may lead the user into their own login |
| `workspace-hygiene` | Clean and repair a workspace in reversible stages | The whole workspace | None |
| `workspace-learning` | Turn real corrections and outcomes into a small set of durable rules | Authorized work history and card threads | None |

`catalog.json` carries the same information in machine-readable form, plus per-skill flags for sensitive reads, network access, external writes, and destructive operations. It is discovery metadata only — the `SKILL.md` file is the procedure. There is no installer, marketplace, dependency resolver, or update daemon.

Three entries deserve attention before installing:

- **`email-digest`** reads personal correspondence and needs a working mail connection. It never sends mail or modifies the mailbox, and it does not set up the account for you.
- **`mail-triage`** goes further: it *moves* mail, so it needs modify permission on a live account. It never deletes — anything it clears goes to an ordinary folder inside the same mailbox — and it never sends. It is the acting counterpart to `email-digest`, not a replacement: one summarizes, the other works the inbox down.
- **`workspace-hygiene`** is the only skill that can remove files. Every move is previewed, archiving beats deletion, and deletion requires approval of the exact targets.

If a user asks for "something with my email", ask what they want first — mail summarized, or mail worked down — and route to one skill. Installing both at once gives them two overlapping rituals and no reason to prefer either.

## Prerequisites

Some skills cannot work on their own. Each catalogue entry carries a `requires` list naming what the user must supply — a mail account, a transcript source, a writable rules file — and for each one *why the skill needs it* and *how to check it actually works*. Entries with prerequisites also point at a `SETUP.md` beside the skill, which says the same thing in prose and ends with a verification the user can run in a minute.

Deliberately, none of this is vendor documentation. It names capabilities, never products, and never restates a provider's own setup steps — those rot, and a stale instruction is worse than none. Connecting the account stays the user's job.


## Installing a skill

There is no installer. Copy the one skill the user asked for into the workspace's own skill directory — for Claude that is `.claude/skills/<slug>/` — after showing what the local adaptation changes.

**Install the whole `skills/<slug>/` folder**, not just `SKILL.md`. `catalog.json` names both: `path` is the procedure, `folder` is what to copy. Runners that read `agents/openai.yaml` then find it; runners that don't simply ignore it.

**Frontmatter must stay the first thing in the file.** Runners discover a skill by parsing the leading `---` block, so a provenance comment placed above it makes the skill invisible. Record the source immediately *after* the closing `---` instead:

```markdown
---
name: workspace-foundation
description: ...
---

<!-- Installed from https://github.com/bmeindl/superskills, skills/workspace-foundation/SKILL.md,
     version 0.1.0, commit <sha>, on <date>. Workspace-local copy; no auto-update. -->

# Workspace foundation
```

Adapt the copy freely afterwards. Nothing here updates it; re-copying is a deliberate act.

## Conventions

Every skill is provider-neutral and free of private workspace content: no employers, colleagues, personal paths, accounts, schedules, or learned rules from the workspace it was written next to. Skills describe capabilities ("browser automation", "mail access") rather than mandating one product, so a workspace can use whatever it already has.

A skill is one folder:

```text
skills/<slug>/
├── SKILL.md            frontmatter (name, description) + the procedure
├── SETUP.md            what the user must supply, and how to verify it — only if the skill has prerequisites
└── agents/openai.yaml  optional display metadata for runners that read it
```

## Checks

Both checks are dependency-free and run offline:

```sh
python3 tools/validate_catalog.py      # catalogue and skill files agree
python3 tools/check_public_safety.py   # no private content in tracked files
```

The safety gate is a tripwire for absent-minded commits — a copied home path, an employer's name, a token in the buffer — not a proof of safety. Read the diff too. Both run in CI on every push and pull request.

## License

MIT — see [LICENSE](LICENSE).
