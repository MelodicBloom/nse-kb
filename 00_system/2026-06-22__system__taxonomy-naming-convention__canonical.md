---
title: "Taxonomy & Naming Convention — Canonical Reference"
status: canonical
domain: system
freshness: current
last_reviewed: 2026-06-22
source_scope: internal-only
tags: [system, naming-convention, taxonomy, canonical, doctrine]
confidence: high
owner: "operator"
version: 1
related: ["2026-06-22__system__service-taxonomy__canonical.md"]
---

# Taxonomy & Naming Convention — Canonical Reference

## Filename Pattern

```
YYYY-MM-DD__domain__topic__status[__variant].md
```

## Components

| Component | Format | Required | Example |
|-----------|--------|----------|---------|
| Date | ISO 8601 | Yes | `2026-06-22` |
| Domain | from taxonomy allowed set | Yes | `competitor` |
| Topic | kebab-case, ≤60 chars | Yes | `ai-fashion-pricing` |
| Status | from allowed set | Yes | `capture` |
| Variant | kebab-case, optional | No | `philadelphia` |

## Allowed Status Values

`canonical` | `draft` | `archive` | `verified` | `capture` | `working` | `template`

| Status | Meaning | Retrieval Priority |
|--------|---------|-------------------|
| `canonical` | Current authoritative version | Highest |
| `verified` | Externally confirmed by sources | High |
| `capture` | Point-in-time observation | Medium |
| `working` | Active draft, in progress | Medium |
| `draft` | Not yet reviewed | Low |
| `template` | Reusable structure | Contextual |
| `archive` | Superseded, kept for audit | Lowest |

## Allowed Domain Values

`research` | `competitor` | `technical` | `report` | `project` | `template` | `system` | `asset`

## Allowed Field Values

| Field | Allowed Values |
|-------|---------------|
| `freshness` | `current` \| `review-needed` \| `archival` |
| `source_scope` | `internal-only` \| `external-verified` \| `mixed` |
| `confidence` | `high` \| `medium` \| `low` |

## Authoring Rules

1. One note per stable concept or artifact.
2. Date = creation date (immutable). Use `last_reviewed` for updates.
3. Status is the retrieval governor — Skills filter on it first.
4. Variant distinguishes regional or contextual forks without duplicating core content.
5. Column names in schemas: snake_case, ≤4 words, semantically stable.
6. Dates in content body: ISO 8601 (`YYYY-MM-DD`) always.
7. Asset references: `../08_assets/YYYY-MM-DD__asset__name__status.ext`
8. Wikilinks for internal cross-references: `[[filename-without-extension]]`
9. `related` array: explicit filenames for programmatic graph traversal.

## Folder Map

| Folder | Purpose | Update Cadence |
|--------|---------|----------------|
| `00_system/` | Doctrine, schemas, naming rules, service taxonomy | Low |
| `01_research/` | Market scans, trend briefs, source registries | Weekly/Monthly |
| `02_competitors/` | Pricing captures, hiring logs, positioning | Weekly |
| `03_technical/` | Stack notes, version constraints, implementation recipes | As needed |
| `04_reports/` | Grant reports, client briefs, case studies, memos | Per project |
| `05_projects/` | Active project contexts | Per sprint |
| `06_templates/` | Reusable structures | Monthly audit |
| `07_archive/` | Superseded material, immutable | Occasional |
| `08_assets/` | Binary assets referenced by notes | As needed |

## Perplexity Spaces Mirror Rule

Upload only files with `status`: `canonical`, `verified`, or `working` AND tagged `spaces-active`. Upload manually when entering active use. Do not automate Spaces sync.

## Degradation Early-Warning Signs

| Symptom | Likely Cause | Fix |
|--------|-------------|-----|
| Conflicting note versions | Edits bypassing repo | Keep repo canonical; set mirrors read-only |
| Front-matter inconsistency | Manual creation bypassing templates | Run pre-commit hook; weekly schema audit |
| Stale wiki/docs | Deploy hook failed | Check webhook logs; manual refresh |
| iPhone edits not syncing | Auth/SSH issue in Working Copy | Reissue keys; test pull/push |
| Notion views missing notes | Sync script failed or schema changed | Check Actions logs; validate property mapping |
