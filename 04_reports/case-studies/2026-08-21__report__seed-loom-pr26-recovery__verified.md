---
title: "Case Study — Seed Loom PR #26 Reconciliation Recovery"
status: verified
domain: report
id: "case:seed-loom-pr26-recovery"
freshness: current
last_reviewed: 2026-08-21
source_scope: mixed
tags: [report, case-study, seed-loom, git, provenance, incident-recovery, verification]
confidence: high
owner: "MelodicBloom"
version: 1
related:
  - "../../09_methods/recovering-governed-reconciliations/2026-08-21__method__recovering-governed-reconciliations__canonical.md"
relations:
  - type: evidenced-by
    target: "github:qt314wink/seed-loom#26"
  - type: applied-in
    target: "project:seed-loom"
---

# Case Study — Seed Loom PR #26 Reconciliation Recovery

## Case Boundary

This record covers the local reconciliation and subsequent recovery of Seed Loom pull request #26. It is an origin case for `method:recovering-governed-reconciliations`; it is not evidence that the method is universally optimal.

## Initial Reconciliation

PR #26 had diverged from its base while carrying visual-isolation, browser-capture, CI, and generated-baseline work. The reconciled candidate became merge commit:

`69e6b04917c2ca1926de3be1e39bba3b8ac0acf6`

with parents:

- PR head: `981e077c353dc7d5bc05acc4c93c64f7a4bb2f51`
- evolved base: `c14371038cf47ee3b4a36c3a6f40a81214edc8cc`

Thirteen PNG snapshot conflicts were not resolved by selecting either parent. They were regenerated from the reconciled application/test state.

## Validation Before the Incident

- `npm run check`: passed
- Filter Atelier focused suite: 16/16 passed
- visual serial suite: 15 passed, 1 designed skip
- mobile intake serial suite: 3/3 passed
- all 13 regenerated images directly inspected and accepted
- `git diff --check`: passed
- working tree: clean
- Issue #34 governed-builder worktree: untouched

A two-worker aggregate browser run reported 30 passed, 1 skip, and 7 resource timeouts. Because the focused serial suites passed without behavioral or visual failures, the timeouts were retained as infrastructure/resource evidence rather than immediately converted into an application defect.

## Incident

After reconciliation, the agent transport disconnected. WebSockets fell back to HTTPS, which also failed with `Host is unreachable (os error 113)` inside WSL.

This created several simultaneous unknowns:

- whether a push had completed
- whether the local reconciliation still existed
- whether browser timeouts reflected product behavior
- whether OpenAI/GitHub or the local environment was unavailable
- which Seed Loom checkout contained the reconciliation

## Recovery Decisions

### 1. Freeze mutation

No reset, rebase, clean, regeneration, force-push, or blind retry was performed while execution state was unknown.

### 2. Verify remote authority independently

GitHub still reported PR #26 as open/draft with remote head `981e077`. The local reconciliation had not been pushed.

### 3. Separate Windows connectivity from WSL connectivity

Native Windows successfully reached both GitHub and OpenAI over TCP/443. Inside WSL, routing and DNS worked but outbound HTTPS failed. This bounded the failure to the WSL/virtual-network path rather than the physical network, Git, or the remote services.

### 4. Falsify networking hypotheses incrementally

- default NAT path: failed
- mirrored networking: attached WSL to the LAN but HTTPS still failed
- mirrored networking with WSL firewall integration disabled: still failed
- proxy bypass: still failed
- VirtioProxy networking: restored HTTPS

Success receipts included GitHub `HTTP/2 200` and an HTTP response from `api.openai.com`, proving transport restoration.

### 5. Recover the apparently missing merge from object topology

The ordinary checkout at `/home/melodyfire/work/seed-loom` did not contain `69e6b04`, and its only worktree was `main`. Rather than recreate the merge, local Seed Loom clones were enumerated and queried by SHA.

The exact reconciliation object existed in two repositories:

- `/home/melodyfire/work/seed-loom-governed-builder-trial`
- `/home/melodyfire/work/seed-loom-governed-builder-test`

The dedicated PR checkout was on `codex/pr-26-ci-fix`, with `69e6b04` at HEAD and the branch 13 commits ahead of `origin/fix/filter-atlas-step-grid-and-ci` at `981e077`.

## Outcome

The reconciliation was recovered exactly without:

- force-pushing
- rewriting history
- recreating the merge from memory
- modifying unrelated Issue #34 work
- changing product behavior to compensate for resource timeouts
- accepting stale generated baselines
- altering remote PR authority during uncertainty

## Distilled Findings

The case supports these bounded distinctions:

- transport failure does not prove remote mutation failure
- a missing SHA in one clone does not prove the object is lost
- passing focused behavior plus failing aggregate resources warrants classification before application edits
- generated artifacts should reflect reconciled source authority when deterministic regeneration is available
- recovery quality improves when exact identifiers survive the incident

## Hiring / Practice Interpretation

The useful signal is not “recovered a Git commit.” It is the ability to preserve decision quality during a multi-layer partial failure: separate failure domains, falsify hypotheses with discriminating tests, maintain authority boundaries, avoid irreversible actions under uncertainty, and extract a reusable method from verified receipts.

A concise formulation:

> I try not to solve uncertainty by creating more state. I establish what happened, where authority lives, and which evidence is trustworthy before making the next mutation.

## Receipts

- Repo: `https://github.com/qt314wink/seed-loom`
- PR: `https://github.com/qt314wink/seed-loom/pull/26`
- PR head: `981e077c353dc7d5bc05acc4c93c64f7a4bb2f51`
- Base: `c14371038cf47ee3b4a36c3a6f40a81214edc8cc`
- Reconciliation: `69e6b04917c2ca1926de3be1e39bba3b8ac0acf6`
