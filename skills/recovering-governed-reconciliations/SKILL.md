---
name: recovering-governed-reconciliations
description: Use when a Git reconciliation, release candidate, or governed repository operation is interrupted by transport failure, ambiguous local or remote state, missing commits/worktrees, generated-artifact conflicts, or flaky validation where blind retry could corrupt provenance.
---

# Recovering Governed Reconciliations

## Overview

Recover uncertain repository operations by treating state, authority, evidence, transport, and validation as separate systems.

**Core principle:** Unknown execution state is a verification problem, not permission to retry.

## Use When

- a session disconnects during push/merge/rebase
- local and remote histories may have diverged
- a known SHA is absent from the current checkout
- multiple clones/worktrees may contain different state
- generated artifacts conflict during reconciliation
- focused tests pass while aggregate/concurrent suites time out
- provenance matters enough that reconstruction is risky

## Invariants

1. Freeze mutation while execution state is unknown.
2. Represent local candidate and shared authority separately.
3. Verify both sides of an interrupted operation before retry.
4. Search refs, worktrees, sibling clones/object stores, reflogs, and receipts before reconstructing work.
5. Regenerate derived artifacts from reconciled source authority when appropriate; do not default to `ours`/`theirs`.
6. Classify behavioral failure versus infrastructure/resource failure before editing product behavior.
7. Guard the next mutation with current expected identifiers.
8. Independently verify post-mutation authority.

## Recovery Sequence

### Freeze
Record working directory, branch, HEAD, working-tree state, intended operation, last known remote SHA, and base SHA. Do not reset, clean, rebase, regenerate, or force-push.

### Classify
Inspect independently:
- repository/candidate state
- remote/shared authority
- transport/infrastructure
- validation behavior

### Recover Evidence
Search exact identifiers across all relevant object stores and receipts. “Not present here” does not mean “lost.”

### Establish Authority
Write down candidate, expected parents/sources, remote head, base head, cleanliness, and protected unrelated work. Stop on unexpected drift.

### Verify Semantics
Confirm intended changes survived, derived artifacts match reconciled state, focused behavior passes, and unrelated work remains isolated.

### Promotion Guard
Immediately before mutation, re-check candidate, remote, base, and cleanliness.

### Single Mutation
Perform only the authorized state transition. Do not bundle cleanup or unrelated work.

### Independent Verification
Verify remote/shared authority, CI/evaluation state, diff/artifacts, and resulting receipt.

## Common Mistakes

- **“The stream died, so the push failed.”** Verify remote state.
- **“The SHA is missing here, so it is lost.”** Search other object databases first.
- **“The full suite timed out, so fix the app.”** Compare focused/serial behavior first.
- **“Binary conflict means choose ours.”** Regenerate if the binary is derived.
- **“Main moved, so merge main.”** Verify the actual PR/base authority relationship.

## Pressure Tests

An agent fails this skill if it creates new state before bounding the relevant unknown state. Test with interrupted push, missing SHA, generated-baseline conflicts, concurrent browser timeouts, and an unrelated moving branch.

## NSE Rationale

Canonical method rationale, tradeoffs, origin case, and adaptation guidance live in `09_methods/recovering-governed-reconciliations/`; the executable skill remains intentionally compact.
