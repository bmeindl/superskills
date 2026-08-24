---
name: transcript-intake
description: Turn a meeting recording, transcript, or pasted notes into the right durable note in a workspace, with attribution, preserved disagreement, and staged action items. Use when the user hands over a transcript file or link, asks to process a recording or a call, or wants a backlog of unprocessed recordings worked through.
---

# Transcript intake

A transcript is raw material, not a document. The job is to decide whether it carries signal at all, extract what a reader will still need in three months, and put it where that reader will look — without inventing certainty the recording does not contain.

## 1. Find the recording, then check it is whole

Check **every** transcript source the workspace has before concluding that nothing was recorded — a local recorder, a notetaker service, and the meeting platform's own export routinely disagree about which meetings exist.

Then compare the recording's length against how long the meeting actually was. Partial recordings are common and silently mislead: a 20-minute file of a 60-minute meeting is not "the meeting". Say which part is missing and look for the gap in another source.

## 2. Skim, then decide whether to extract at all

Skim speakers, length, and topics first. If a service supplies AI-generated notes, use them for this cheap skim only — never as the material you extract from (see §4).

State the gist in one line, then route by weight:

- nothing but scheduling and reiteration → record that it was low-signal and stop;
- one small durable fact → one tagged line in the workspace's capture file;
- actionable but vague → a parked item, not a document;
- decisions, commitments, or genuinely new information → full extraction.

One high-impact item is enough to justify a document. Volume is not.

## 3. Look for the destination before writing

Search existing notes for a document on the same topic and append to it. A new file is the fallback, not the default; delegate the search if it is nontrivial.

Route by decision, in order: append to a recent document on the topic → new file in an established pattern → the durable-knowledge file, if the finding stays true long-term → a person-specific note → the capture inbox, tagged with the unresolved destination. A transcript covering several topics gets **one** primary document plus one-line cross-references — never a full fan-out.

Write without asking when the routing is clear-cut. Ask first only when the answer would create a genuinely new category or top-level location.

## 4. Extract against your own biases

Every extracted document carries: insights, decisions, and commitments with named attribution; a **disagreement and unresolved questions** section that stays non-empty unless the transcript really shows alignment; topics raised outside the reason you were asked to read it; and a clear mark on anything inferred rather than said.

The failure modes worth naming, because they look like good work:

- **Summaries flatten dissent.** Clean AI notes have hidden four real disagreements that the raw transcript showed plainly. Extract from the transcript.
- **Recency bias.** If your bullets cluster in the last quarter of the meeting, re-skim the first half.
- **Framing anchor.** Do not bend ambiguous statements toward the topic you were asked about; file them as off-frame instead.
- **Examples are not decisions.** Two or three illustrations of one abstract point are one point, not three action items.
- **Authority is not accuracy.** A claim outside a speaker's domain is their read. A senior person musing is not a directive; a junior person stating something firmly is not optional.
- **No smooth narrative.** Do not insert "therefore" between bullets the conversation never connected.
- **Garbled audio.** If an attribution seems implausible for that speaker, mark it unclear rather than forcing it.

Paraphrase by default. Quote verbatim only where the wording carries the weight: commitments, contested points, dates.

## 5. Delegating a long transcript

Read the opening yourself before handing sections to sub-agents — it sets the baseline for tone and drift, and tells you what to brief them on. Require a verbatim quote for every date and commitment a sub-agent reports: relative time is where they hallucinate ("Saturday" from a source that said "tomorrow"). Sub-agents extract; you decide and you write.

## 6. Stage actions, do not commit them

An action found in a transcript becomes a **proposal**, not a task. Before proposing anything, search the task system yourself — open items and closed ones — and drop or merge duplicates silently. Never ask whether something already exists; ask only whether it should become something.

Two exceptions go straight onto the task list: a hard, near-term deadline, and an explicit request from the user. A new commitment toward a third party is never recorded as a commitment without the user saying so.

## 7. Close the loop

End every written document with its source and timestamp, so a later reader can go back to the recording. End every run with: what you wrote, where it went, how strong the signal was, and what still needs the user's decision.

**Backlog mode.** When working through a backlog, drive it from a ledger of processed and unprocessed recordings — not from "since the last run", which loses anything that arrived late. Bucket by day, run this procedure per recording, merge findings on the same topic before proposing anything, and mark a recording processed only after it has actually been routed.
