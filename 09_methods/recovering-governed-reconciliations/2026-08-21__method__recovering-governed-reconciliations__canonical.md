---
title: "Recovering Governed Reconciliations"
status: canonical
domain: method
id: "method:recovering-governed-reconciliations"
maturity: field-tested
freshness: current
last_reviewed: 2026-08-21
source_scope: mixed
tags: [method, git, provenance, incident-recovery, agent-governance, verification]
confidence: high
owner: "MelodicBloom"
version: 1
related:
  - "../../04_reports/case-studies/2026-08-21__report__seed-loom-pr26-recovery__verified.md"
  - "../../skills/recovering-governed-reconciliations/SKILL.md"
relations:
  - type: derived-from
    target: "case:seed-loom-pr26-recovery"
  - type: evidenced-by
    target: "case:seed-loom-pr26-recovery"
  - type: implemented-as
    target: "skill:recovering-governed-reconciliations"
  - type: applied-in
    target: "project:seed-loom"
---

# Recovering Governed Reconciliations

## Problem Class

Partially failed engineering operations can make execution state ambiguous at exactly the moment when blind retry is most dangerous. Examples include an agent transport disconnect during a push, a known commit appearing absent from one checkout, generated-artifact conflicts during a merge, or a full test run timing out while focused behavioral tests remain clean.

The risk is not merely failure. The risk is **creating additional state before establishing what actually happened and which state is authoritative**.

## Origin

This method was articulated during recovery of Seed Loom pull request #26 after a provenance-sensitive reconciliation was completed locally and the agent/WSL transport subsequently failed. The exact reconciliation was later recovered by SHA in two isolated clones rather than reconstructed from memory.

The origin case supports the method as `field-tested`. It does not yet establish cross-domain transfer, so the method is not `transferred` maturity.

## Evidence

| Evidence | Type | Supports / Challenges | Scope / Limitation |
|----------|------|-----------------------|--------------------|
| PR head `981e077c353dc7d5bc05acc4c93c64f7a4bb2f51` remained remote authority during transport failure | Git receipt | Supports independent verification of interrupted mutation state | One Git/GitHub incident |
| Base `c14371038cf47ee3b4a36c3a6f40a81214edc8cc` plus PR head produced reconciliation `69e6b04917c2ca1926de3be1e39bba3b8ac0acf6` | Git merge parentage | Supports explicit candidate provenance | Git-specific receipt type |
| Reconciliation SHA recovered in two isolated Seed Loom clones | local object-database search | Supports “search topology before reconstructing” | Same machine / repository family |
| 13 visual snapshot conflicts regenerated from reconciled application/test state | generated-artifact procedure | Supports regeneration over arbitrary `ours/theirs` selection | Applies when artifacts are genuinely derived |
| Focused serial suites passed while two-worker suite experienced resource timeouts | test evidence | Supports classifying behavioral vs resource failure before application edits | Requires discriminating focused tests |
| Windows HTTPS succeeded while WSL HTTPS failed under NAT/mirrored modes; VirtioProxy restored transport | network-layer experiment | Supports failure-domain decomposition | Platform-specific implementation detail, not a method invariant |

## Optimizes For

- preservation of recoverable state
- provenance and traceability
- reversibility
- authority clarity
- correct classification of failure domains
- minimal mutation under uncertainty
- independent verification of state transitions

## Costs / Tradeoffs

- slower immediate response than blind retry
- more inspection before mutation
- explicit SHA/state bookkeeping
- possible additional local references or recovery clones
- requires operators to tolerate temporary uncertainty rather than forcing convergence

## Chosen Against

| Alternative | Why plausible | Why not selected here | When it may be better |
|-------------|---------------|-----------------------|-----------------------|
| Immediately retry the interrupted command | Fast and often works | Can duplicate or conflict with an operation that actually completed | Idempotent, disposable operations with externally guaranteed semantics |
| Force-push reconstructed state | Rapidly makes remote match local intent | Rewrites authority before proving local state is correct | Explicitly authorized history repair with verified expected target |
| Recreate a missing merge from memory | Seems easier than locating old workspaces | Destroys evidence and may not reproduce semantic conflict resolution | Only after all existing object stores/receipts are exhausted |
| Treat all timeouts as product defects | Gives a concrete thing to fix | Can modify correct behavior to compensate for resource contention | Timeout is deterministic and tied to behavioral assertions |
| Resolve generated binaries with `ours`/`theirs` | Git-native and fast | Selects a parent's derived state instead of the reconciled system's state | Binary is authoritative source material rather than generated output |

## Mechanism

The method reduces compounding uncertainty by separating four questions that are often collapsed:

1. **What local candidate exists?**
2. **What shared authority exists?**
3. **Which failure domain is actually broken?**
4. **What mutation is safe given the verified state?**

Inspection is allowed while mutation is frozen. Once the relevant authority boundaries are established, exactly one bounded mutation can occur and then be independently verified.

The method's effectiveness depends on receipts being sufficiently durable to reconstruct state: commit SHAs, branch refs, run IDs, hashes, logs, or equivalent identifiers in non-Git systems.

## Invariants

An adaptation still counts as this method only if it preserves all of these:

1. Unknown execution state is verified before retry.
2. Candidate state and shared authority are represented separately.
3. Failure domains are classified before changing product behavior.
4. Existing evidence/topology is searched before reconstructing work.
5. Generated artifacts are derived from reconciled authority when regeneration is available and appropriate.
6. The next mutation is bounded by explicit preconditions.
7. Post-mutation state is independently verified.

Specific tools, Git commands, networking modes, and CI systems are configurable implementation details.

## Applicability Boundary

### Use when

- an agent or terminal session disconnects during a repository mutation
- push/merge/rebase status is uncertain
- local and remote authority may have diverged
- a known candidate SHA is absent from the current checkout
- multiple clones/worktrees may contain different state
- generated artifacts conflict during reconciliation
- focused tests pass while aggregate/concurrent tests time out
- provenance matters enough that history reconstruction would be risky

### Do not use the full protocol when

- the work is disposable and no valuable state exists
- the operation is provably idempotent and execution status does not affect later decisions
- a simple reproducible product bug exists with no ambiguous mutation state
- a standard Git branch recovery is sufficient and no wider authority/infrastructure ambiguity exists

## Adjacent Methods

| Method | Shared territory | Decision boundary |
|--------|------------------|-------------------|
| Systematic debugging | Separates symptoms from causes | Best when a reproducible behavior is wrong; this method begins earlier when execution/authority itself is uncertain |
| Verification before completion | Requires evidence before declaring success | This method also handles ambiguous intermediate state and recovery before work can be considered complete |
| Git reflog/worktree recovery | Recovers missing Git state | This method includes remote authority, infrastructure classification, generated artifacts, and promotion gates |
| Incident response | Stabilizes partially failing systems | This method is optimized for provenance-sensitive state transitions rather than service availability alone |

## Adaptation Dimensions

| Dimension | Invariant or configurable? | Examples | Risks |
|-----------|----------------------------|----------|-------|
| Authority system | Configurable | Git remote, database, deployment controller, document store | Authority must still be independently observable |
| Receipt type | Configurable | SHA, transaction ID, artifact digest, deployment ID | Weak identifiers make reconstruction ambiguous |
| Mutation gate | Configurable | shell guard, policy engine, human approval | Gate must test current state, not stale assumptions |
| Verification system | Configurable | CI, checksum, reconciliation query, review | Verification must observe the post-mutation authority |
| Risk tolerance | Configurable | high-provenance production vs disposable prototype | Over-governance can waste time in low-risk contexts |
| Freeze-on-unknown-state | Invariant | no blind retry while status is unknown | Removing this collapses the method into ordinary retry/debugging |

## Protocol

### 1. Freeze
Record current location, branch/identity, candidate state, known remote/base authority, working state, and intended operation. Do not mutate.

### 2. Classify
Independently classify repository state, remote authority, transport/infrastructure, and validation behavior.

### 3. Recover evidence
Search refs, worktrees, sibling clones/object stores, reflogs, remote refs, CI receipts, and other durable identifiers before reconstruction.

### 4. Establish authority
Write down candidate, expected parents/sources, remote/shared authority, cleanliness, and unrelated protected work. Stop on unexpected drift.

### 5. Verify semantics
Confirm intended parent/source changes survive, derived artifacts reflect reconciled state, focused behavior is correct, and unrelated work remains isolated.

### 6. Promotion guard
Immediately before mutation, verify all expected authority identifiers and cleanliness conditions again.

### 7. Single mutation
Perform only the authorized state transition. Do not bundle cleanup or unrelated work.

### 8. Independent verification
Verify remote/shared authority, CI/evaluation state, diff/artifact state, and the resulting receipt.

## Validation

Pressure-test the method with scenarios in which an operator or agent is incentivized to take a shortcut:

- interrupted push: does it verify remote state before retry?
- missing SHA: does it search other object stores before reconstructing?
- generated binary conflicts: does it regenerate from reconciled source when appropriate?
- concurrent timeout with passing serial suites: does it classify resource vs behavior before editing?
- unrelated moving branch: does it verify the actual authority relationship rather than merge everything automatically?

A failure is any response that creates new state before the relevant unknown state is bounded.

## Case Studies

### Origin Case

`case:seed-loom-pr26-recovery` — Seed Loom PR #26 reconciliation and WSL transport recovery.

### Transfer Cases

None yet. A materially different second application is required before promoting maturity to `transferred`.

## Counterexample

A disposable local prototype with one developer, no remote mutation, no valuable uncommitted state, and trivial reproducibility does not need this full protocol. Standard inspection and retry is cheaper and sufficiently safe.

## Evolution Triggers

Revise or supersede this method if:

- repeated transfer cases show that freezing all mutations is unnecessarily strict for specific idempotent systems
- stronger transactional systems can prove mutation completion without external verification
- agent runtimes expose durable execution receipts that eliminate important classes of ambiguity
- evidence shows the protocol systematically delays recovery without reducing state corruption or misdiagnosis

## Receipts

- Repository: `qt314wink/seed-loom`
- Pull request: `#26` — `fix: reconcile Filter Atlas step grids and enforce Atelier CI`
- PR head before promotion: `981e077c353dc7d5bc05acc4c93c64f7a4bb2f51`
- Reconciled base: `c14371038cf47ee3b4a36c3a6f40a81214edc8cc`
- Reconciliation merge: `69e6b04917c2ca1926de3be1e39bba3b8ac0acf6`
- Merge parents: `981e077` + `c143710`
- Focused Filter Atelier tests: 16/16 passed
- Visual serial suite: 15 passed, 1 designed skip
- Mobile intake serial suite: 3/3 passed
- Regenerated visual baselines: 13 directly inspected
- Aggregate two-worker observation: 30 passed, 1 skipped, 7 browser resource timeouts
