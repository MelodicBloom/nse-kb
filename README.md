# NSE Knowledge Base (`nse-kb`)

**Owner:** MelodicBloom / qt314wink — Narrative Systems Engineering  
**Version:** 1.1 | **Created:** 2026-06-22 | **Last foundation review:** 2026-08-21  
**Status:** Active canonical repository

---

## What this is

A governed, markdown-first knowledge and method repository for Narrative Systems Engineering across:

- AI-assisted creative services, design systems, generative media, and agent workflows
- civic technology and regenerative practice
- React / Next.js / GLSL / WebGL development
- digital products and service systems
- research, technical verification, project decisions, case studies, and reusable methods

This repo is the **canonical knowledge source of truth**. Other layers such as Notion, Wiki/MkDocs, or external research spaces are views or mirrors unless explicitly promoted as authorities.

NSE is designed to preserve not only **what is known**, but **why a reusable method exists, what evidence selected for it, what it optimizes for, what it was chosen against, where it applies, and what would cause it to change**.

---

## Authority Surfaces

NSE now distinguishes three related surfaces:

1. **Knowledge plane** — system doctrine, research, verification, reports, projects, case studies, and canonical methods.
2. **Executable plane** — compact runtime artifacts such as Agent Skills under `skills/`.
3. **Evidence plane** — project receipts, observations, exact identifiers, tests, source records, and assets supporting or challenging the knowledge plane.

Executable skills are intentionally not treated as ordinary NSE notes. A skill should remain compact enough for correct runtime discovery and execution; its rationale, alternatives, origin cases, applicability boundary, and adaptation guidance belong in the corresponding NSE method dossier.

A mature method should make this chain inspectable:

**problem → evidence → alternatives → method → application → validation → evolution**

---

## Folder Structure

```text
nse-kb/
├── 00_system/           # Doctrine, schemas, naming rules, service taxonomy
├── 01_research/         # Market scans, trend briefs, source registries
├── 02_competitors/      # Pricing captures, hiring logs, positioning snapshots
├── 03_technical/        # Stack notes, version constraints, implementation recipes
├── 04_reports/          # Grant reports, client briefs, case studies, decision memos
├── 05_projects/         # Active project contexts (one folder per project)
├── 06_templates/        # Reusable knowledge-note templates
├── 07_archive/          # Superseded material (immutable audit trail)
├── 08_assets/           # Binary assets, evidence exports, images, PDFs
├── 09_methods/          # Evidence-backed reusable methods and adaptation guidance
├── skills/              # Executable Agent Skills; separate front-matter schema
├── docs/                # Implementation plans and supporting engineering docs
├── scripts/             # Validation, sync, and diagnostic automation
└── .github/workflows/   # CI/CD pipelines
```

---

## Naming Convention

NSE knowledge notes use:

```text
YYYY-MM-DD__domain__topic__status[__variant].md
```

Examples:

```text
2026-06-18__competitor__ai-fashion-pricing__capture.md
2026-06-19__technical__nextjs-webgl-export-constraints__verified.md
2026-06-22__system__service-taxonomy__canonical.md
2026-08-21__method__recovering-governed-reconciliations__canonical.md
```

Executable skills use the Agent Skills convention:

```text
skills/<skill-name>/SKILL.md
```

---

## NSE Knowledge Front Matter

Existing NSE notes require:

```yaml
---
title: "Human-readable title"
status: canonical | draft | archive | verified | capture | working | template
domain: research | competitor | technical | report | project | template | system | asset | method
freshness: current | review-needed | archival
last_reviewed: YYYY-MM-DD
source_scope: internal-only | external-verified | mixed
tags: [tag1, tag2]
related: []
confidence: high | medium | low
owner: "operator or organization"
version: 1
---
```

New `domain: method` records additionally require:

```yaml
id: method:stable-semantic-id
maturity: candidate | field-tested | transferred | canonical | deprecated
relations:
  - type: evidenced-by
    target: case:stable-case-id
```

Stable IDs are being introduced incrementally. Legacy notes are not required to backfill IDs in v0.1.

See `00_system/2026-08-21__system__evidence-backed-method-model__canonical.md` for the full contract.

---

## First Reference Specimen

`method:recovering-governed-reconciliations` is the first complete evidence-backed method specimen.

It connects:

- a real origin incident and exact Git receipts
- a verified case study
- a canonical human-readable method dossier
- an executable Agent Skill
- explicit tradeoffs and chosen-against alternatives
- applicability boundaries and a counterexample
- pressure-test scenarios
- a maturity ceiling of `field-tested` until transfer evidence exists

The specimen is intended to test the architecture, not to justify bulk-converting every historical NSE note.

---

## Governance Rituals

| Ritual | Cadence | Action |
|--------|---------|--------|
| Freshness sweep | Weekly | Update `freshness` + `last_reviewed` where review actually occurred |
| Capture rotation | Weekly | Archive stale point-in-time captures according to domain policy |
| Template audit | Monthly | Verify templates match current schemas |
| Project hygiene | Per sprint | Reconcile or archive completed project contexts |
| Method review | On new transfer evidence | Update maturity, applicability boundaries, comparisons, and receipts |
| Schema drift check | Quarterly | Compare front-matter fields, validators, mirrors, and rendered docs |

A governance cadence is a commitment to produce evidence, not merely a label. If a review did not occur, do not advance `last_reviewed` mechanically.

---

## Validation

Knowledge notes and executable skills are validated separately:

```bash
python scripts/validate_frontmatter.py
python scripts/validate_skills.py
```

The knowledge validator enforces the legacy schema plus method-specific IDs, maturity, and typed relations. The skill validator enforces compact runtime metadata and name/directory consistency.

---

## Read / Mirror Layers

- **GitHub:** canonical versioned source
- **MkDocs:** human-readable exploration surface
- **Notion:** optional operational mirror of NSE knowledge notes
- **External research spaces:** bounded working views; never implicit authority

`skills/` and `docs/` are deliberately excluded from ordinary Notion knowledge-note sync.

---

## GitHub Secrets Used by Current Automation

| Secret | Purpose |
|--------|---------|
| `NOTION_TOKEN` | Notion internal integration token |
| `NOTION_DATABASE_ID` | Notion Notes database ID |
| `KB_WEBHOOK_TOKEN` | Auth token for wiki refresh webhook |
| `WIKI_WEBHOOK_URL` | Wiki/MkDocs deploy hook |

Repository settings: `github.com/MelodicBloom/nse-kb/settings/secrets/actions`

---

## Forking / Adapting NSE

Before adopting a method, inspect:

- the problem class
- origin evidence
- what it optimizes for
- accepted costs/tradeoffs
- chosen-against alternatives
- applicability boundary
- adjacent methods
- adaptation dimensions
- validation mechanism
- maturity and transfer evidence

The goal is not to inherit doctrine blindly. The goal is to make enough context available that another practitioner can decide whether a method fits their situation, should be simplified, or should be adapted into a different method with its own provenance.
