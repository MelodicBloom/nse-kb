---
title: "NSE Service Taxonomy — Canonical"
status: canonical
domain: system
freshness: current
last_reviewed: 2026-08-21
source_scope: internal-only
tags: [system, service-taxonomy, canonical, doctrine]
confidence: high
owner: "MelodicBloom"
version: 2
related:
  - "2026-06-22__system__taxonomy-naming-convention__canonical.md"
  - "2026-08-21__system__evidence-backed-method-model__canonical.md"
---

# NSE Service Taxonomy — Canonical

## Primary Verticals

| Vertical | Services | Platforms | Output Types |
|----------|----------|-----------|-------------|
| AI Creative Services | Design systems, generative art, LoRA training, ComfyUI pipelines, AI illustration, AI fashion models | ComfyUI, Hugging Face, Stable Diffusion, OpenAI | Prompt pipelines, model packages, design tokens, image exports |
| Civic Technology | Community workshops, regenerative urbanism, Beats & Boxes, Sensorium, neighborhood AI | Philadelphia, grant-funded | Workshop curricula, case studies, grant reports, civic tools |
| Web & Interactive | React/Next.js builds, WebGL/GLSL shader systems, Fabric.js canvas tools, p5.js generative art | Next.js, TypeScript, Three.js | Deployed sites, component libraries, shader systems, SVG exports |
| Digital Products | Downloadable assets, licensed systems, prompt packs, service packages | GitHub and product/service platforms | Downloadable assets, licensed repos, digital templates |
| Fabrication | Laser-cut SVG design, structural color simulation, physical print production | SVG toolchain, laser cutter | Cut files, print-ready exports, fabrication specs |
| Methods & Practice | Reusable decision protocols, agent skills, verification methods, governed workflows | NSE, GitHub, agent runtimes | Method dossiers, skills, case studies, validation protocols |

## Tag Vocabulary (Controlled)

### Primary Domain Tags (mutually exclusive per NSE knowledge file)

`research` | `competitor` | `technical` | `report` | `project` | `template` | `system` | `asset` | `method`

Executable `skills/**/SKILL.md` files are not NSE knowledge files and therefore do not use this domain field.

### Vertical Tags (combinable)

```text
philadelphia  civic-tech  regenerative-design  community-workshops  grants
ai-fashion  generative-art  design-systems  creative-ai  lora  comfyui  huggingface
react  nextjs  glsl  webgl  shaders  fabricjs  p5js  typescript
docker  kubernetes  github-actions
gumroad  fiverr  digital-products  licensing
laser-fabrication  svg-export  print-production
agent-governance  provenance  incident-recovery  methods  skills
```

### Function Tags

`brief` | `capture` | `analysis` | `verification` | `template` | `schema` | `decision` | `evidence` | `action` | `method` | `case-study` | `comparison` | `adaptation`

### Status-Adjacent Tags

`time-sensitive` | `recurring` | `blocked` | `deprecated` | `superseded` | `spaces-active`

## Confidence Level Guidance

| Level | Use When |
|-------|----------|
| `high` | Primary source, direct observation, reproducible receipt, or official docs support the bounded claim |
| `medium` | Secondary source, inference from evidence, or partial verification |
| `low` | Speculation, rumor, unverified claim, or single anecdotal source |

Confidence applies to the claims in a note, not to the author's enthusiasm for the method.

## Source Scope Guidance

| Scope | Use When |
|-------|----------|
| `internal-only` | Private analysis, internal decisions, grant submissions, client work |
| `external-verified` | Sourced from public data with verification trail |
| `mixed` | Internal reasoning/receipts plus external sources |

## Retrieval Priority by Status + Domain

| Domain | Highest Priority Status | Use For |
|--------|------------------------|--------|
| `system` | `canonical` | Doctrine, schema, taxonomy |
| `research` | `canonical`, `verified` | Market context, grant evidence |
| `competitor` | `capture`, `verified` | Pricing, hiring, positioning data |
| `technical` | `verified`, `canonical` | Implementation decisions |
| `report` | `canonical`, `verified`, `working` | Active deliverables and case studies |
| `project` | `working`, `canonical` | Sprint context |
| `template` | `template` | Starting new notes |
| `method` | `canonical`, `working` | Reusable evidence-backed practices |

## Method Retrieval Guidance

Method retrieval must consider both document `status` and method `maturity`.

A `status: canonical` method record is the current authoritative description of that method; it does **not** imply the method has universal evidence. A method may therefore be `status: canonical` and `maturity: field-tested` when the description is authoritative but transfer evidence is still limited.

When choosing a method for action, prefer records whose applicability boundary matches the situation over records that merely have higher maturity.
