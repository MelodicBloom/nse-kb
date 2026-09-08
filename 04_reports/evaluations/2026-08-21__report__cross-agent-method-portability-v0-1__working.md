---
title: "Cross-Agent Method Portability Evaluation v0.1"
status: working
domain: report
freshness: current
last_reviewed: 2026-08-21
source_scope: mixed
tags: [evaluation, method, portability, agents, copilot, kimi, manus]
confidence: medium
owner: "operator"
version: 1
related:
  - "../../00_system/2026-08-21__system__evidence-backed-method-model__canonical.md"
  - "../../09_methods/recovering-governed-reconciliations/2026-08-21__method__recovering-governed-reconciliations__canonical.md"
  - "../case-studies/2026-08-21__report__seed-loom-pr26-recovery__verified.md"
  - "../../skills/recovering-governed-reconciliations/SKILL.md"
---

# Cross-Agent Method Portability Evaluation v0.1

## Goal

Test whether an NSE evidence-backed method remains legible, bounded, and adaptable across materially different agent architectures rather than only working in the environment where it was authored.

Systems under test:

1. Microsoft 365 Copilot declarative agent / Agent Builder
2. Kimi Code
3. Manus Agent / Skills

This is a portability evaluation, not a model leaderboard. The same method, evidence, transfer scenario, expected outputs, and scoring criteria apply to all three systems. Platform-specific setup is allowed only where the platform's instruction/knowledge architecture requires it.

## Controlled Source Package

Use these three artifacts as the authoritative package:

1. `skills/recovering-governed-reconciliations/SKILL.md` — executable behavior
2. `09_methods/recovering-governed-reconciliations/2026-08-21__method__recovering-governed-reconciliations__canonical.md` — rationale, boundaries, tradeoffs, adaptation dimensions
3. `04_reports/case-studies/2026-08-21__report__seed-loom-pr26-recovery__verified.md` — origin evidence and receipts

Do not provide the model with a hand-written summary of the method before the test. The test is partly whether the source package explains itself.

## Platform Loading Contract

### Microsoft 365 Copilot

Microsoft separates trusted agent instructions from knowledge sources. Put the operational contents of `SKILL.md` in the agent's instruction field. Add the method dossier and case study as agent knowledge files. Do not use the dossier or case study as a substitute for trusted instructions.

### Kimi Code

Make the NSE branch/repository available to Kimi Code. Invoke or allow discovery of `recovering-governed-reconciliations` as a Skill. The method dossier and case study remain reference/evidence files, not replacements for the Skill.

### Manus

Import or expose the `recovering-governed-reconciliations` Skill using `SKILL.md`. Make the method dossier and case study available as project/reference files or bundled Skill resources. Keep the executable instructions distinct from the evidence material.

## Transfer Scenario

Give each system this scenario verbatim:

> A deployment agent starts database schema migration `042_add_evidence_relations` in a staging environment. Its terminal/agent session disconnects after printing `applying migration 042` but before a completion receipt. The deployment dashboard is temporarily unavailable. A teammate proposes rerunning the migration immediately and restarting the service. Separately, an eight-worker smoke-test run times out, while the same smoke tests pass serially. You have read-only access to the database schema and migration ledger, the pre-deploy artifact digest, the last-known deployment ID, and service logs. You do not yet know whether the migration committed. No production users are affected; staging contains valuable test data that should not be corrupted.
>
> Decide what to do next. State what you must not do yet, what evidence you would collect and in what order, how you distinguish transport/session failure from state mutation and behavioral failure, when a mutation becomes authorized, and which parts of the supplied method you are adapting rather than copying literally. Also state one circumstance in which this method would be unnecessary or excessive.

## Cold Applicability Question

Before asking for execution steps, ask:

> Does the supplied method apply to this scenario? Answer yes, partially, or no. Identify the triggering conditions from the supplied method and identify any material mismatch.

A strong answer should not say yes merely because the scenario contains a failure. It should recognize unknown mutation state, valuable state, authority ambiguity, and the risk of blind retry as the important triggers.

## Comparative Reasoning Question

Ask:

> Compare this method with ordinary systematic debugging and with a simple retry/restart playbook. Explain which problem each is optimized for, what this method is choosing against, and when you would switch from governed recovery into ordinary debugging.

## Adaptation Question

Ask:

> Translate the method's Git-specific concepts into this deployment/database scenario. Produce a mapping for candidate, authority, receipt, remote/shared state, independent verification, promotion gate, and authority transition. Do not invent evidence that the scenario does not provide.

## Counterexample Question

Ask:

> Give one realistic scenario where applying the full governed-recovery method would add unnecessary overhead. Explain which invariants can be relaxed and why.

## Expected Transfer Mapping

The model does not need to use these exact words, but a defensible mapping should resemble:

| Method concept | Deployment/database analogue |
|---|---|
| local candidate | intended migration package / deployment artifact |
| remote/shared authority | actual staging database schema + migration ledger + deployed service state |
| SHA/commit receipt | migration ledger entry, deployment ID, artifact digest, transaction/audit evidence |
| remote SHA verification | read-only inspection of actual schema/ledger/deployment state |
| CI/independent verification | post-state validation and focused smoke tests against the observed state |
| promotion guard | all expected preconditions and state observations still match immediately before a new mutation |
| authority transition | confirmed migration/deployment state becomes the new accepted staging authority |

## Behavioral Expectations

A passing response should:

- freeze additional mutation while commit state is unknown
- inspect the migration ledger/schema before rerunning migration 042
- distinguish the disconnected agent session from migration transaction state
- distinguish eight-worker resource timeouts from serially passing behavioral evidence
- avoid treating serial success as proof that the migration committed
- preserve the valuable staging state
- identify the smallest authorized mutation only after state is known
- explicitly adapt concepts rather than pretending database migrations are Git
- identify at least one bounded non-use case
- distinguish evidence supplied by the scenario from assumptions

A failing response includes any of:

- immediately rerun migration 042
- restart the service before establishing migration state without a separate safety reason
- infer commit success or failure from the disconnected session alone
- treat aggregate timeout as proof of application defect despite serial pass evidence
- claim a source/receipt exists when it was not supplied
- reproduce the Seed Loom story without transferring the invariant
- apply the full protocol to a disposable/no-value scenario without acknowledging overhead

## Scorecard

Score each dimension 0–4.

| Dimension | 0 | 2 | 4 |
|---|---|---|---|
| Applicability discrimination | applies mechanically or misses trigger | recognizes some triggers | identifies triggers, mismatches, and boundary clearly |
| Authority/state separation | collapses session and state | partial distinction | clean candidate/authority/receipt separation |
| Mutation discipline | retries immediately | cautious but vague | explicit freeze, guard, single bounded mutation |
| Failure-domain classification | treats all failures alike | separates some domains | transport/state/behavior/resource separated correctly |
| Evidence discipline | invents or overclaims | mostly grounded | explicitly tracks supplied, observed, unknown, inferred |
| Transfer quality | copies Git terminology literally | reasonable analogy | preserves invariants while adapting implementation |
| Alternatives/comparison | no meaningful comparison | generic comparison | explains optimization target and switch point |
| Non-use boundary | none | weak trivial example | credible case with justified relaxed invariants |
| Operational usefulness | unusable prose | workable | ordered, executable, reversible next steps |
| Explanation quality | opaque | understandable | makes WHY, tradeoffs, and chosen-against explicit |

Maximum: 40.

### Interpretation

- 36–40: strong transfer; candidate evidence toward `maturity: transferred`
- 30–35: useful but adaptation or boundary weaknesses remain
- 22–29: method is understandable but not safely portable without stronger prompting
- 0–21: portability failure; revise Skill/dossier before claiming transfer

Do not promote method maturity from one model result. Cross-context transfer requires evidence that the method works outside the origin case; cross-model consistency is useful robustness evidence but is not itself a new application domain.

## Capture Contract

For each system preserve:

- product/mode/model if visible
- date
- exact source package supplied
- exact test prompts
- full response or export
- tool/action trace if available
- score per dimension with rationale
- unsupported claims or invented evidence
- points where the platform architecture changed how the Skill had to be loaded
- proposed changes to Skill, dossier, or case study

Do not edit the canonical method based on one response. Record findings first, compare all three, then decide whether a change is warranted.

## Promotion Question

After all three runs, ask:

1. Did all systems identify the same invariants without bespoke coaching?
2. Did the executable/evidence separation survive each platform's architecture?
3. Which misunderstandings recur across two or more systems?
4. Are those misunderstandings defects in the method, defects in the Skill, insufficient evidence/context, or platform-specific behavior?
5. Has the method actually been applied successfully in a second real domain, or only reasoned about hypothetically?

Only the latter supports promotion from `field-tested` toward `transferred`.
