---
name: mail-triage
description: Design and run safe, bounded email triage or digest workflows while keeping connector setup, user policy, and external actions separate. Use when the user asks to check an inbox, reach inbox zero, create an email digest, learn mail-handling rules, or turn a recurring email process into a Superboard action.
---

# Mail triage

Treat mail as a workflow plus a connector, not one opaque automation. The skill is provider-neutral; use whichever mail interface the active workspace has explicitly configured.

## 1. Define the outcome

Ask for one concrete mode:

- a bounded inbox round;
- a daily or weekly digest;
- search/read for one topic;
- draft replies for review.

Agree the mailbox, time window, stopping rule, and what counts as done. Ten-minute rounds or a fixed message count are good defaults.

## 2. Establish the connector boundary

Inspect only non-secret capability metadata first. Explain what the available connector can read, label, archive, delete, draft, or send.

- Never open credential files or extract tokens.
- Never start authentication without the user taking over the login step.
- Never send, delete, unsubscribe, purchase, or change an external account without explicit approval.
- Prefer drafts and reversible labels/archive actions.

If no connector exists, provide the exact setup step and stop before authentication.

## 3. Separate policy from mechanics

Create or update a workspace-owned policy only after observing real decisions. Keep rules small and attributable, for example:

- always surface mail from named people;
- archive a recurring machine notification after the user confirms the pattern;
- never auto-handle invoices, legal notices, account security, or travel changes.

Do not infer a permanent rule from one message. Record uncertainty and ask.

## 4. Run one bounded pass

Fetch the smallest useful batch, group similar machine mail, and present only decisions the user must make. For every proposed action, show sender, subject, why it matters, and the reversible action. Apply approved actions, then report counts and anything deferred.

## 5. Learn carefully

At the end of a round, propose at most a few new or changed rules from explicit user choices. Write only approved rules. Keep connector/account details out of the reusable skill; they belong in the local workspace configuration.
