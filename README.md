# NSE Knowledge Base (`nse-kb`)

**Owner:** qt314wink — Narrative Systems Engineer  
**Version:** 1.0 | **Created:** 2026-06-22  
**Status:** Active canonical repository

---

## What this is

A governed, markdown-first knowledge base for a Narrative Systems Engineer operating across:
- AI-assisted creative services (design systems, generative art, LoRA, ComfyUI)
- Civic technology + regenerative urbanism (Philadelphia)
- React / Next.js / GLSL / WebGL development
- Digital products (Gumroad, Fiverr, licensing)
- Grant-funded community workshops and installations

This repo is the **canonical source of truth**. All other layers (Wiki.js, Notion, Perplexity Spaces) are views or mirrors.

---

## Folder Structure

```
nse-kb/
├── 00_system/           # Doctrine, schemas, naming rules, service taxonomy
├── 01_research/         # Market scans, trend briefs, source registries
├── 02_competitors/      # Pricing captures, hiring logs, positioning snapshots
├── 03_technical/        # Stack notes, version constraints, implementation recipes
├── 04_reports/          # Grant reports, client briefs, case studies, decision memos
├── 05_projects/         # Active project contexts (one folder per project)
├── 06_templates/        # Reusable report/note templates
├── 07_archive/          # Superseded material (immutable, audit trail)
├── 08_assets/           # Binary assets (images, PDFs, exports)
├── scripts/             # Automation scripts
└── .github/workflows/   # CI/CD pipelines
```

---

## Naming Convention

```
YYYY-MM-DD__domain__topic__status[__variant].md
```

**Examples:**
```
2026-06-18__competitor__ai-fashion-pricing__capture.md
2026-06-18__research__philly-civic-tech-grants__brief.md
2026-06-19__technical__nextjs-webgl-export-constraints__verified.md
2026-06-22__system__service-taxonomy__canonical.md
```

---

## Required Front-Matter (every .md file)

```yaml
---
title: "Human-readable title"
status: canonical | draft | archive | verified | capture | working | template
domain: research | competitor | technical | report | project | template | system | asset
freshness: current | review-needed | archival
last_reviewed: YYYY-MM-DD
source_scope: internal-only | external-verified | mixed
tags: [tag1, tag2]
related: []
confidence: high | medium | low
owner: "operator"
version: 1
---
```

---

## Mobile Workflow (iPhone)

1. **Edit:** Obsidian iOS (vault = this repo folder) or GitJournal
2. **Commit/Push:** Working Copy (SSH auth to GitHub)
3. **CI runs:** Front-matter validation → Notion sync → read layer refresh
4. **Read layer:** Wiki.js (self-hosted) or MkDocs published docs

---

## Perplexity Spaces Mirror Rule

Only upload **active files** (status: canonical/verified/working, tagged `spaces-active`) to Perplexity Spaces. Keep the canonical archive here.

---

## Governance Rituals

| Ritual | Cadence | Action |
|--------|---------|--------|
| Freshness sweep | Weekly (Mon) | Update `freshness` + `last_reviewed` |
| Capture rotation | Weekly (Fri) | Archive competitor captures >2 cycles old |
| Template audit | Monthly | Verify templates match current schemas |
| Project hygiene | Per sprint | Archive completed projects |
| Schema drift check | Quarterly | Compare front-matter fields |

---

## GitHub Secrets Required

| Secret | Purpose |
|--------|--------|
| `NOTION_TOKEN` | Notion internal integration token |
| `NOTION_NOTES_DB_ID` | Notion Notes database ID |
| `KB_WEBHOOK_TOKEN` | Auth token for wiki refresh webhook |
| `WIKI_WEBHOOK_URL` | Full URL of your Wiki.js/MkDocs deploy hook |

Add at: `github.com/qt314wink/nse-kb/settings/secrets/actions`

---

## Related Perplexity Skills

| Skill | Queries |
|-------|---------|
| `deep-research` | `01_research/` |
| `competitor-monitor` | `02_competitors/` |
| `technical-verification` | `03_technical/` |
| `internal-report-automation` | `04_reports/`, `06_templates/` |
| `market-intelligence` | `01_research/`, `02_competitors/` |
