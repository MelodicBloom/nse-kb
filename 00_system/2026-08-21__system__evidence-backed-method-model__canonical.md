---
title: "Evidence-Backed Method Model — Canonical"
status: canonical
domain: system
freshness: current
last_reviewed: 2026-08-21
source_scope: mixed
tags: [system, method, provenance, evidence, skills, canonical]
confidence: high
owner: "MelodicBloom"
version: 1
related:
  - "2026-06-22__system__taxonomy-naming-convention__canonical.md"
  - "../06_templates/method-dossier-template.md"
---

# Evidence-Backed Method Model — Canonical

## Purpose

NSE preserves not only **what is known**, but **how knowledge became trustworthy enough to act on** and how that knowledge becomes a reusable method.

The model distinguishes three authority surfaces:

1. **Knowledge plane** — human-readable research, verification, projects, reports, decisions, case studies, and canonical methods.
2. **Executable plane** — compact agent/runtime artifacts such as `SKILL.md` files.
3. **Evidence plane** — receipts, project excerpts, exact identifiers, test results, observations, source records, and other material that supports or challenges a method.

These surfaces may refer to one another, but they must not silently duplicate or replace one another.

## Core Chain

A mature reusable method should make this chain inspectable:

**problem → evidence → alternatives → method → application → validation → evolution**

The chain is explanatory rather than merely chronological. It should let another person answer:

- Why does this exist?
- What was wrong or insufficient before it existed?
- What evidence selected for this intervention?
- What does it optimize for and what costs does it accept?
- What alternatives were considered or deliberately chosen against?
- Where should it be used, and where should it not be used?
- What parts are invariant and what parts are adaptable?
- Where has it actually been applied?
- What evidence would cause revision, deprecation, or supersession?

## Artifact Types

### Method

A reusable pattern of judgment or action with explicit applicability boundaries, invariants, tradeoffs, validation criteria, and provenance.

A method is broader than a runtime-specific implementation. One method may be implemented as multiple skills, playbooks, scripts, or organizational practices.

### Executable Skill

A compact runtime artifact optimized for discovery and correct agent execution.

Executable skills SHOULD remain concise and MUST use their runtime's required schema. They point back to NSE methods for rationale and evidence instead of embedding full project histories.

### Case Study

An evidence-bearing account of a real application. It records context, constraints, observations, decisions, outcomes, failures, and receipts. A case study can support multiple methods, and a method can have multiple case studies.

### Evidence

A bounded observation, source, receipt, exact identifier, test result, artifact, screenshot, run result, or other record used to support, falsify, qualify, or revise a claim or method.

## Stable IDs

New `domain: method` records MUST define a stable `id`.

Recommended format:

```yaml
id: method:recovering-governed-reconciliations
```

Stable IDs are semantic identifiers. Filenames remain dated audit artifacts and may move or be superseded; IDs should remain stable unless the underlying concept changes identity.

Legacy NSE notes are not required to backfill IDs in v0.1. Migration is deliberate, not automatic.

## Typed Relations

New method records MUST define `relations` as a YAML list. Each relation has:

```yaml
- type: evidenced-by
  target: case:seed-loom-pr26-recovery
```

Canonical relation types for v0.1:

| Type | Meaning |
|------|---------|
| `derived-from` | The method emerged from or was materially shaped by the target |
| `evidenced-by` | The target provides evidence supporting or qualifying the method |
| `implemented-as` | The target is an executable or operational representation |
| `compared-with` | The target is an adjacent or competing method |
| `applied-in` | The method was used in the target project/context |
| `validated-by` | The target evaluates or tests the method |
| `supersedes` | This record replaces the target as current authority |
| `superseded-by` | The target has replaced this record |

Relations should identify *how* records connect. The legacy `related` field remains valid for broad navigational cross-reference.

## Method Maturity

Methods use a separate `maturity` field so epistemic status is not overloaded.

Allowed v0.1 values:

| Maturity | Meaning |
|----------|---------|
| `candidate` | Plausible abstraction, insufficient transfer evidence |
| `field-tested` | Demonstrated in at least one real application with receipts |
| `transferred` | Demonstrated in more than one materially different context |
| `canonical` | Stable, reviewed, reusable method with clear boundaries and validation |
| `deprecated` | Retained for history but no longer recommended |

`status` continues to govern document authority/retrieval. `maturity` describes the method's evidence of reuse.

## Required Method Questions

Every canonical method dossier SHOULD answer:

### Problem
What failure class, constraint, decision pressure, or opportunity caused the method to exist?

### Evidence
What direct observations or sources support that problem definition?

### Optimizes For
What qualities are prioritized?

### Costs / Tradeoffs
What does the method make slower, harder, more explicit, or more expensive?

### Chosen Against
What plausible alternatives are deliberately not selected, and why?

### Mechanism
Why should the method produce the intended result?

### Invariants
What must remain true for an adaptation to still count as this method?

### Applicability Boundary
When is the method unnecessary, inappropriate, or actively harmful?

### Adjacent Methods
What similar approaches exist, and what decision boundary separates them?

### Adaptation Dimensions
Which parameters can vary by risk tolerance, platform, authority model, scale, or environment?

### Validation
How can another operator determine whether the method worked?

### Evolution
What new evidence would trigger revision, deprecation, or supersession?

## Promotion Rules

A method MUST NOT be promoted to canonical merely because it is well written.

Promotion requires:

1. A defined problem class.
2. Evidence or an origin case.
3. Explicit applicability boundaries.
4. At least one meaningful alternative or chosen-against configuration.
5. A validation mechanism.
6. Stable identity and typed provenance relations.
7. Review of claims that exceed the available evidence.

`field-tested` is the default maturity ceiling after one real case. `transferred` requires a second materially different application. `canonical` maturity should be reserved for methods whose invariants survive transfer and review.

## Evidence Discipline

Case studies are evidence, not decoration.

A case study SHOULD distinguish:

- observation from inference
- local candidate from shared authority
- behavioral failure from infrastructure/resource failure
- direct receipt from narrative interpretation
- what happened from what the operator learned from it

Exact identifiers such as Git SHAs, PR numbers, issue numbers, run IDs, artifact hashes, or version numbers SHOULD be preserved when they materially establish state.

## Human and Hiring-Manager Legibility

The human-facing NSE view SHOULD let a reader traverse:

**Project / incident → evidence → decision → method → executable implementation → later applications**

This makes reasoning inspectable instead of asking readers to infer competence from finished artifacts alone.

Public portfolio projections, if created, MUST be bounded views. Private canonical NSE material should not be made public solely to improve presentation.

## Non-Goals for v0.1

- Mandatory stable-ID migration of all historical NSE notes.
- Converting NSE into an agent-skill repository only.
- Duplicating complete case studies inside `SKILL.md`.
- Automatically declaring methods canonical from one successful application.
- Changing repository visibility.
