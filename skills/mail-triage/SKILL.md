---
name: mail-triage
description: Work a mailbox down in short timeboxed rounds — clear machine mail by rules that grow, present only genuine decisions as a small set of cards, and execute the answers in the next round. Use when the user wants inbox zero, a triage round, a backlog of old mail worked through, or mail turned into decisions rather than a summary.
---

# Mail triage

This skill *acts* on a mailbox. Its sibling `email-digest` only summarizes; if the user wants to read rather than decide, use that one instead.

The unit of work is a round of roughly ten minutes of the user's attention — not an empty inbox. A good round moves the flow forward, takes a bite out of the backlog, and leaves the rules file smarter than it found it.

## 1. Load the rules before touching anything

A rules file next to the skill is the single source of truth for what may happen without asking. Your instinct is not. It holds sender classes, age thresholds, destination buckets, and a marker for when the last round ran — so you know the real gap instead of assuming "since yesterday".

If the user pasted back decisions from the previous round, execute those first, then continue.

## 2. Silent pass

Apply only what the rules file already licenses: machine mail past its age threshold, notifications the user has demonstrably read and ignored. Report these as a log line, never as a question.

Age cuts differently by sender: machine mail gets *safer* to clear as it ages, human mail does not. Anything from a person with a real request, or carrying a deadline, money, a signature, or a contract, stays out of the silent pass regardless of age.

## 3. The flow

Take new mail since the last round that the silent pass did not catch. Produce a card only for what you genuinely cannot decide — not for what you would like covering for.

Two heuristics carry most of the ambiguous cases:

- If the mail asks something **of** the user and has been sitting a while, it is usually already resolved elsewhere: default to archiving.
- If something is owed **to** the user — money, a claim, a benefit — surface it even when the deadline looks expired.

Mail containing an action gets staged as a suggested follow-up and the mail itself is archived. That is a fixed rule, not a per-item judgment: promoting straight into the task system is reserved for hard near-term deadlines or an explicit request.

## 4. Backlog, newest first

Work the backlog last-in-first-out. Recency correlates with continued relevance; the older something is, the cheaper it is to default-archive.

Before building several similar cards, bundle them into one question — "23 messages from this sender, archive all?" Bundling is the main lever against backlog volume, and a good bundle doubles as a calibration question about a whole category.

## 5. Present decisions, sized to time

Render a small set of cards, sized to the user's ten minutes rather than to the number of messages: thirty cards cost the whole round, one bundle of thirty costs a click. Each card says in a sentence or two *why it is a decision* — repeating the subject line is not a summary — and carries a stable handle (mailbox folder plus message id) so the next round can execute the answer unambiguously.

The user answers with one line per item: handle, chosen action, optional comment.

## 6. Execute, then learn

Execute the moves, then update the rules file — always. Every deviation from what you proposed is a learning signal, and every free-text comment is a candidate rule. **A round that did not update the rules file was a wasted round.**

## Rails

- **Never delete.** What you believe is junk moves to a designated soft-trash folder inside the same mailbox, never to the provider's trash or spam. This is the standing scar of an over-eager filter that destroyed a real inbox; a tool-level guard is a backstop, not the safeguard.
- **Autonomy is a ladder.** Propose moving up a rung; never grant yourself one. Every override by the user is a step back down, not noise.
- **Buy autonomy with auditability.** The more you handle silently, the more the round must show a random sample of it — spread across your different auto-rules, not the safest-looking ones — so an error can be caught after the fact.
- **Never send.** Replies are out of scope by default. If one is genuinely warranted, leave a draft and mark it as written by an agent rather than by the user personally.
- **Do not make this unattended.** The round runs when the user triggers it. Automatic runs accumulate unnoticed mistakes in exactly the place they hurt most.
