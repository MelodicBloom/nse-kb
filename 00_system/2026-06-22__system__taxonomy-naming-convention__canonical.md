---
title: "Taxonomy & Naming Convention — Canonical Reference"
status: canonical
domain: system
freshness: current
last_reviewed: 2026-08-21
source_scope: internal-only
tags: [system, naming-convention, taxonomy, canonical, doctrine]
confidence: high
owner: "MelodicBloom"
version: 2
related:
  - "2026-06-22__system__service-taxonomy__canonical.md"
  - "2026-08-21__system__evidence-backed-method-model__canonical.md"
---

# Taxonomy & Naming Convention — Canonical Reference

## Filename Pattern

```text
YYYY-MM-DD__domain__topic__status[__variant].md
```

## Components

| Component | Format | Required | Example |
|-----------|--------|----------|---------|
| Date | ISO 8601 | Yes | `2026-08-21` |
| Domain | from taxonomy allowed set | Yes | `method` |
| Topic | kebab-case, ≤60 chars | Yes | `recovering-governed-reconciliations` |
| Status | from allowed set | Yes | `canonical` |
| Variant | kebab-case, optional | No | `public` |

## Allowed Status Values

`canonical` | `draft` | `archive` | `verified` | `capture` | `working` | `template`

| Status | Meaning | Retrieval Priority |
|--------|---------|-------------------|
| `canonical` | Current authoritative version | Highest |
| `verified` | Confirmed against the declared evidence/source scope | High |
| `capture` | Point-in-time observation | Medium |
| `working` | Active synthesis, in progress | Medium |
| `draft` | Not yet reviewed | Low |
| `template` | Reusable structure | Contextual |
| `archive` | Superseded, kept for audit | Lowest |

## Allowed Domain Values

`research` | `competitor` | `technical` | `report` | `project` | `template` | `system` | `asset` | `method`

`method` is reserved for reusable patterns of judgment or action with explicit provenance, applicability boundaries, tradeoffs, and validation. Executable Agent Skills remain under `skills/` and use their runtime schema rather than `domain: method` front matter.

## Allowed Field Values

| Field | Allowed Values |
|-------|---------------|
| `freshness` | `current` \| `review-needed` \| `archival` |
| `source_scope` | `internal-only` \| `external-verified` \| `mixed` |
| `confidence` | `high` \| `medium` \| `low` |

## Stable IDs

New `domain: method` notes MUST define a stable semantic `id` independent of filename/path.

Recommended pattern:

```yaml
id: method:recovering-governed-reconciliations
```

Legacy notes are not required to backfill stable IDs in v0.1. New non-method records SHOULD add IDs when they become graph-critical or need durable cross-repository references.

## Typed Relations

Method records MUST use a `relations` list for provenance-bearing edges. Each entry contains `type` and `target`.

```yaml
relations:
  - type: derived-from
    target: case:seed-loom-pr26-recovery
  - type: implemented-as
    target: skill:recovering-governed-reconciliations
```

The legacy `related` array remains valid for broad navigation and backward compatibility. `related` answers “what else may be useful?”; `relations` answers “how are these records connected?”

## Authoring Rules

1. One note per stable concept or artifact.
2. Date = creation date (immutable). Use `last_reviewed` for updates.
3. Status is the retrieval governor — retrieval layers filter on it first.
4. Variant distinguishes regional, public/private, or contextual forks without duplicating core content.
5. Column names in schemas: snake_case, ≤4 words, semantically stable.
6. Dates in content body: ISO 8601 (`YYYY-MM-DD`) always.
7. Asset references: `../08_assets/YYYY-MM-DD__asset__name__status.ext` or a more specific descendant path when evidence is grouped.
8. Wikilinks may be used for human navigation; stable IDs and typed relations are preferred for durable programmatic graph edges.
9. `related` array: explicit filenames/paths for backward-compatible graph traversal.
10. `domain: method` records must comply with `2026-08-21__system__evidence-backed-method-model__canonical.md`.
11. Executable `skills/**/SKILL.md` files are not NSE knowledge notes and are validated separately.

## Folder Map

| Folder | Purpose | Update Cadence |
|--------|---------|----------------|
| `00_system/` | Doctrine, schemas, naming rules, service taxonomy | Low |
| `01_research/` | Market scans, trend briefs, source registries | Weekly/Monthly |
| `02_competitors/` | Pricing captures, hiring logs, positioning | Weekly |
| `03_technical/` | Stack notes, version constraints, implementation recipes | As needed |
| `04_reports/` | Grant reports, client briefs, case studies, memos | Per project |
| `05_projects/` | Active project contexts | Per sprint |
| `06_templates/` | Reusable knowledge-note structures | Monthly audit |
| `07_archive/` | Superseded material, immutable | Occasional |
| `08_assets/` | Binary assets and evidence referenced by notes | As needed |
| `09_methods/` | Evidence-backed reusable methods and adaptation guidance | As methods mature |
| `skills/` | Executable agent/runtime skills; separate schema | As methods become executable |

## Perplexity Spaces Mirror Rule

Upload only knowledge notes with `status`: `canonical`, `verified`, or `working` AND tagged `spaces-active`. Upload manually when entering active use. Do not automatically mirror executable `skills/` unless the target runtime specifically consumes that format.

## Degradation Early-Warning Signs

| Symptom | Likely Cause | Fix |
|--------|-------------|-----|
| Conflicting note versions | Edits bypassing repo | Keep repo canonical; set mirrors read-only |
| Front-matter inconsistency | Manual creation bypassing templates | Run validators; weekly schema audit |
| Duplicate stable IDs | Copying method records without changing identity | Fail CI; reconcile identity before merge |
| Untyped provenance | `related` used where causal/evidence semantics matter | Add typed `relations` |
| Method overclaim | One successful case promoted as universal | Keep maturity at `field-tested`; seek transfer case |
| Stale wiki/docs | Deploy hook failed | Check webhook logs; manual refresh |
| iPhone edits not syncing | Auth/SSH issue in Working Copy | Reissue keys; test pull/push |
| Notion views missing notes | Sync script failed or schema changed | Check Actions logs; validate property mapping |
