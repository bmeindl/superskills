---
name: superboard-update
description: Check the installed Superboard package and any Superskills copies for updates, explain what changed, install routine updates safely, and negotiate anything that collides with local edits. Use when a "Check for updates" card runs, or the user asks whether Superboard or its skills are current.
---

# Superboard update

Superboard is a tool the user relies on daily. A click on the update card is the order to install — default is: update. Make it reversible first, resolve conflicts without escalating them, and never overwrite a file the user owns. How much to decide alone otherwise follows the workspace's own agent-user contract, if it has one.

## 1. Probe (read-only)

- Installed package: `python3 -c "import importlib.metadata as m; print(m.version('superboard'))"`.
- Latest release: `pip index versions superboard`, or `curl -s https://pypi.org/pypi/superboard/json | python3 -c "import sys,json; print(json.load(sys.stdin)['info']['version'])"`. Offline → say so and stop.
- Release notes: the package's `RELEASES.md`, or `gh release view v<latest> -R bmeindl/superboard` if `gh` is available and authenticated. Neither available → say "no notes available" and keep going.
- Installed skills: for each `SKILL.md` under the workspace's skill directory that carries a source/version comment pointing at this catalogue, compare that version against `catalog.json` (`https://raw.githubusercontent.com/bmeindl/superskills/main/catalog.json`). Also list catalogue skills the workspace doesn't have — offer them, never install unasked.
- How was Superboard installed? Check in order: `uv tool list` → `uv tool upgrade superboard`; `pipx list` → `pipx upgrade superboard`; otherwise `pip install -U superboard`. Don't assume a package manager — check which one actually owns the install.

## 2. Report

One compact block: current version → latest version, what changed (two to five bullets from the release notes), which workspace files the update could touch (normally none — package code only), any installed skill with a newer catalogue version, and any new optional skill. If everything is current, say so in one line and stop.

## 3. Local drift

- Package: a reinstall never touches the workspace; drift only matters if the user has patched the installed package's own files (check modification time against install time only if something looks off).
- Skills: diff the installed `SKILL.md` against the catalogue source at the version it was installed from. Identical → clean upgrade. Different → three-way: show the user's changes and the upstream changes side by side and propose a merged file; apply only after approval in the thread.

## 4. Safety net before touching anything

The workspace should be a git repository so an update is always revertible and any conflict is diffable.

- Not a repository yet → `git init` and commit the current state (`git add -A && git commit -m "pre-update snapshot"`, local only, no remote needed). Do this, don't ask.
- Already a repository → commit or stash the dirty state under a clear message.

Note the resulting commit hash; it is the rollback point for skill or workspace changes. (Package rollback is a plain reinstall of the old version, not a git revert.)

## 5. Act

- **Clean:** upgrade, restart the board the way it was started, then verify: the server answers, the board renders, and its action list is unchanged from before. Record the old version in case a rollback is needed.
- **Drift:** resolve it without escalating — apply the upstream change on top of the user's edits (three-way merge, keep their intent), run the same checks, and commit the result with a message that names both sides. Only stop and ask when the merge is genuinely unresolvable (contradicting intent, or the checks still fail after two honest attempts); when that happens, open the reply with `❓` and show both versions.
- **Failure after upgrade:** reinstall the previous version, restart, and report what failed with the relevant log lines.

## 6. Never

- Write to the board's own configuration or data files (its actions list, ritual definitions, board configuration, board content, or thread files) — those belong to the user and the running board, not to this skill.
- Install a new skill, or open an issue or pull request, without an explicit yes in the thread first. Feedback becomes an issue on the Superboard repository; a contribution becomes a pull request from a fork. Both need a working, authenticated git-hosting CLI, and both wait for the user's word.

## 7. Tell the user what's new

After a successful update, close with a short, friendly note on what's new — three to five bullets in the user's own terms (what they can now do, what looks different), drawn from the release notes and the diff rather than a changelog paste. Call out anything they must do themselves, such as restarting the board or re-running a setup step.

## Reply shape

First line: the result in one sentence — `Up to date (0.4.2)`, `Updated 0.4.2 → 0.5.0, verified`, or `❓ 0.5.0 available but skill X has local edits — merge proposal below`. Details follow underneath.
