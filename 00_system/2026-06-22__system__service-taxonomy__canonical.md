---
title: "NSE Service Taxonomy — Canonical"
status: canonical
domain: system
freshness: current
last_reviewed: 2026-06-22
source_scope: internal-only
tags: [system, service-taxonomy, canonical, doctrine]
confidence: high
owner: "operator"
version: 1
related: ["2026-06-22__system__taxonomy-naming-convention__canonical.md"]
---

# NSE Service Taxonomy — Canonical

## Primary Verticals

| Vertical | Services | Platforms | Output Types |
|----------|----------|-----------|-------------|
| AI Creative Services | Design systems, generative art, LoRA training, ComfyUI pipelines, AI illustration, AI fashion models | ComfyUI, Hugging Face, Stable Diffusion, OpenAI | Prompt pipelines, model packages, design tokens, image exports |
| Civic Technology | Community workshops, regenerative urbanism, Beats & Boxes, Sensorium, neighborhood AI | Philadelphia, grant-funded | Workshop curricula, case studies, grant reports, civic tools |
| Web & Interactive | React/Next.js builds, WebGL/GLSL shader systems, Fabric.js canvas tools, p5.js generative art | Next.js 15, TypeScript, Three.js | Deployed sites, component libraries, shader systems, SVG exports |
| Digital Products | Gumroad downloads, Fiverr gigs, licensed design systems, prompt packs | Gumroad, Fiverr, GitHub | Downloadable assets, licensed repos, digital templates |
| Fabrication | Laser-cut SVG design, structural color simulation, physical print production | SVG toolchain, laser cutter | Cut files, print-ready exports, fabrication specs |

## Tag Vocabulary (Controlled)

### Primary Domain Tags (mutually exclusive per file)
`research` | `competitor` | `technical` | `report` | `project` | `template` | `system` | `asset`

### Vertical Tags (combinable)
```
philadelphia  civic-tech  regenerative-design  community-workshops  grants
ai-fashion  generative-art  design-systems  creative-ai  lora  comfyui  huggingface
react  nextjs  glsl  webgl  shaders  fabricjs  p5js  typescript
docker  kubernetes  github-actions
gumroad  fiverr  digital-products  licensing
laser-fabrication  svg-export  print-production
```

### Function Tags
`brief` | `capture` | `analysis` | `verification` | `template` | `schema` | `decision` | `evidence` | `action`

### Status-Adjacent Tags
`time-sensitive` | `recurring` | `blocked` | `deprecated` | `superseded` | `spaces-active`

## Confidence Level Guidance

| Level | Use When |
|-------|----------|
| `high` | Primary source, direct observation, official docs |
| `medium` | Secondary source, inferred from evidence, partial verification |
| `low` | Speculation, rumor, unverified claim, single anecdotal source |

## Source Scope Guidance

| Scope | Use When |
|-------|----------|
| `internal-only` | Private analysis, internal decisions, grant submissions, client work |
| `external-verified` | Sourced from public data with verification trail |
| `mixed` | Both internal reasoning and external sources |

## Retrieval Priority by Status + Domain

| Domain | Highest Priority Status | Use For |
|--------|------------------------|--------|
| `system` | `canonical` | Doctrine, schema, taxonomy |
| `research` | `canonical`, `verified` | Market context, grant evidence |
| `competitor` | `capture`, `verified` | Pricing, hiring, positioning data |
| `technical` | `verified`, `canonical` | Implementation decisions |
| `report` | `canonical`, `working` | Active deliverables |
| `project` | `working`, `canonical` | Sprint context |
| `template` | `template` | Starting new notes |
