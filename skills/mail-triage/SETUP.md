# Setup — mail triage

What the skill needs from your workspace. It is provider-neutral: any mail access the agent can drive will do.

## Required

**Mail access with read and move permission.** Something the agent can use to list, search, read, and move messages between folders or labels — an IMAP-capable tool, a mail connector, or whatever your workspace already has wired up. You supply and authenticate it; the skill does not set up accounts.

**Send permission is not required and should not be granted.** The method never sends mail. If you want reply drafts, "save as draft" is enough.

**A soft-trash folder inside the mailbox.** A normal folder — not the provider's trash or spam — where anything the agent believes is junk goes instead of being deleted. Nothing in this method is irreversible.

**A rules file** next to the installed skill. Start it empty; it grows every round with sender classes, age thresholds, and the marker for when the last round ran. This file, not the model's instinct, licenses everything that happens without asking.

**Somewhere to present decision cards** — a rendered local page, a board card, a chat message. Any surface where you can answer one line per item.

## Optional

- **A staging list** for action items pulled out of mail, kept separate from your real task tracker.
- **A dumb pre-filter** running elsewhere. This skill is the judgment layer above it, not a replacement.

## Check that it works

Run one round on your live mailbox and inspect the result before answering anything:

1. Open the soft-trash folder. Everything the silent pass cleared should be sitting there, recoverable.
2. Count the cards. If the round produced twenty single messages instead of a few bundles, it is sized to your mail rather than to your time — say so, and it should bundle harder next round.
3. Answer the cards, let the next round execute them, then open the rules file. It must have changed. If it did not, the round taught the skill nothing and the next one will ask you the same questions.
