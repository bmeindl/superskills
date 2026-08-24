# Setup — transcript-intake

What the skill needs from your workspace. It is provider-neutral on purpose: bring whatever you already use.

## Required

**A transcript source.** At least one of: a local recorder that writes transcript files, a notetaker service with an API or connector, or your meeting platform's own transcript export. More than one is better — the skill's first step is checking sources against each other — but one is enough; with a single source, treat the cross-check step as a no-op.

**A place to write.** A notes or knowledge structure the agent can read *and* append to, so it can route a finding to an existing document instead of creating a new one every time.

**A staging place for action items.** Anywhere you can keep "proposed" separate from "committed", and where already-decided items remain visible — the skill deduplicates against them before proposing anything. A flat file is enough.

## Optional

- **A ledger of processed vs. unprocessed recordings**, if you want backlog mode rather than one transcript at a time.
- **Sub-agents**, if your transcripts are long enough to need splitting.
- **A note in your workspace instructions** about the language and tone the notes should be written in.

## Check that it works

Hand the agent one meeting you attended and remember well, then check three things in what comes back:

1. Does it name **which source** the transcript came from, and whether the recording covers the whole meeting?
2. Does the disagreement section contain the disagreement you remember — or does the document read smoother than the meeting was?
3. Are the action items **proposals** you still have to accept, rather than items already sitting in your task system?

If all three hold on a meeting you can verify from memory, the setup is sound. If the third fails, the skill has write access somewhere it should not have.
