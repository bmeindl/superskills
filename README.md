# Superskills

Optional, public-safe procedures for agent workspaces and Superboard.

This repository is deliberately separate from Superboard. Nothing is installed automatically. A user or agent reads one named skill, previews the local adaptation, and copies it into the workspace's skill directory only after approval. The installed copy belongs to that workspace and may diverge; there is no automatic update mechanism.

## Catalogue

| Skill | Use it for |
| --- | --- |
| `workspace-foundation` | Establish a portable workspace root, context map, boundaries, and maintenance loop |
| `mail-triage` | Design bounded inbox rounds or digests without coupling the procedure to one provider |
| `workspace-hygiene` | Clean and repair a workspace in reversible stages |
| `workspace-learning` | Turn real corrections and outcomes into a small set of durable rules |

For Superboard onboarding, check out this repository as `superskills/` inside the workspace. Setup cards then reference `superskills/skills/<slug>/SKILL.md`. Absence is a normal offline state: each card carries enough fallback guidance to continue.

Every skill is provider-neutral and contains no personal paths, accounts, employers, people, schedules, credentials, or private operating rules.
