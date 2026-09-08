# Evidence-Backed Methods v0.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend NSE from a governed document repository into an evidence-backed method system that preserves why reusable methods exist, how they were validated, what they optimize for, and how executable skills relate to human-readable knowledge.

**Architecture:** Preserve the existing numbered knowledge-base structure and add a first-class `method` domain under `09_methods/`. Keep executable Agent Skills under `skills/` with their own minimal schema and validator. Link methods, case studies, projects, evidence, and skills through stable IDs and typed relations while remaining backward-compatible with legacy NSE notes.

**Tech Stack:** Markdown, YAML front matter, Python 3.11, python-frontmatter, MkDocs Material, GitHub Actions.

**Spec:** `00_system/2026-08-21__system__evidence-backed-method-model__canonical.md`

## Global Constraints

- `main` remains untouched until review/merge.
- Existing NSE notes must remain valid without mandatory backfill of stable IDs.
- Stable `id` and typed `relations` are required for the new `method` domain first.
- Executable `SKILL.md` files are validated separately from NSE knowledge notes.
- Case studies remain evidence-bearing reports, not duplicated inside executable skills.
- The first specimen is `recovering-governed-reconciliations`, derived from the Seed Loom PR #26 recovery incident.
- No public/private visibility change is included in v0.1.

---

### Task 1: Formalize the evidence-backed method model

**Files:**
- Create: `00_system/2026-08-21__system__evidence-backed-method-model__canonical.md`
- Modify: `00_system/2026-06-22__system__taxonomy-naming-convention__canonical.md`
- Modify: `00_system/2026-06-22__system__service-taxonomy__canonical.md`

**Interfaces:**
- Consumes: existing NSE status, freshness, confidence, source-scope, naming, and `related` conventions.
- Produces: stable IDs, typed relations, `method` domain semantics, and applicability/provenance rules.

- [ ] Add a canonical system note defining method, executable skill, case study, evidence, relation types, maturity, and promotion rules.
- [ ] Add `method` to the controlled domain vocabulary without invalidating existing domains.
- [ ] Define stable IDs as mandatory for new method records and optional-but-recommended for legacy records.
- [ ] Define typed relations including `derived-from`, `evidenced-by`, `implemented-as`, `compared-with`, `applied-in`, `validated-by`, `supersedes`, and `superseded-by`.

### Task 2: Add a reusable method template and first complete specimen

**Files:**
- Create: `06_templates/method-dossier-template.md`
- Create: `09_methods/recovering-governed-reconciliations/2026-08-21__method__recovering-governed-reconciliations__canonical.md`
- Create: `04_reports/case-studies/2026-08-21__report__seed-loom-pr26-recovery__verified.md`

**Interfaces:**
- Consumes: Task 1 method schema.
- Produces: one canonical method with origin case, alternatives, tradeoffs, applicability boundary, adaptation dimensions, and evidence receipts.

- [ ] Create the dossier template with problem, evidence, alternatives, chosen-against, mechanism, invariants, boundary, adaptation, validation, and evolution sections.
- [ ] Encode the reconciliation-recovery method using stable IDs and typed relations.
- [ ] Record the Seed Loom recovery as a verified case study with exact SHAs and bounded claims.

### Task 3: Add the executable skill as a separate authority surface

**Files:**
- Create: `skills/recovering-governed-reconciliations/SKILL.md`
- Create: `scripts/validate_skills.py`

**Interfaces:**
- Consumes: the canonical method conceptually, but uses Agent Skills front matter (`name`, `description`) rather than NSE note front matter.
- Produces: a discoverable executable technique plus deterministic validation.

- [ ] Add a compact executable skill focused on triggers, invariants, recovery sequence, common mistakes, and pressure scenarios.
- [ ] Validate skill directory/name consistency, required front matter, description trigger form, and description length.

### Task 4: Extend NSE validation and mirrors without breaking legacy notes

**Files:**
- Modify: `scripts/validate_frontmatter.py`
- Modify: `.github/workflows/validate-kb.yml`
- Modify: `scripts/sync_to_notion.py`

**Interfaces:**
- Consumes: Task 1 schema and Task 3 skill validator.
- Produces: CI enforcement for new method requirements plus separate skill validation.

- [ ] Add `method` to the allowed NSE domain set.
- [ ] Require `id`, `maturity`, and list-shaped `relations` for `domain: method` only.
- [ ] Validate relation entries contain `type` and `target` and reject duplicate stable method IDs.
- [ ] Exclude `skills/` from the normal NSE front-matter walk.
- [ ] Run both validators in CI.
- [ ] Update Notion domain mapping and repository fallback to `MelodicBloom/nse-kb`.

### Task 5: Make the model legible to humans

**Files:**
- Modify: `README.md`
- Modify: `mkdocs.yml`

**Interfaces:**
- Consumes: Tasks 1–4.
- Produces: a human-readable entry path for contributors, forkers, reviewers, and hiring managers.

- [ ] Explain knowledge plane vs executable plane.
- [ ] Document the evidence-backed method chain: problem → evidence → alternatives → method → application → validation → evolution.
- [ ] Add `09_methods/` and `skills/` to the repository map.
- [ ] Correct stale organization/repository references.
- [ ] Add Methods and Case Studies to MkDocs navigation.

## Verification

- [ ] `python scripts/validate_frontmatter.py` passes.
- [ ] `python scripts/validate_skills.py` passes.
- [ ] MkDocs configuration references only paths created by this branch or existing paths.
- [ ] Existing legacy notes remain valid without stable-ID migration.
- [ ] The method record points to the case-study and skill IDs/paths without duplicating their full contents.
- [ ] No changes are made to repository visibility or `main` directly.
