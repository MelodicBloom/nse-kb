#!/usr/bin/env python3
"""
Validate NSE knowledge-note front-matter schema.

Executable Agent Skills under `skills/` use a separate schema and are checked
by `scripts/validate_skills.py`. Implementation/planning docs under `docs/`
are likewise outside the canonical NSE note schema.
"""

import sys
from pathlib import Path

try:
    import frontmatter
except ImportError:
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "python-frontmatter", "-q"], check=True)
    import frontmatter

REQUIRED_FIELDS = [
    "title", "status", "domain", "freshness", "last_reviewed",
    "source_scope", "tags", "confidence", "version"
]
ALLOWED_STATUS = {"canonical", "draft", "archive", "verified", "capture", "working", "template"}
ALLOWED_DOMAIN = {"research", "competitor", "technical", "report", "project", "template", "system", "asset", "method"}
ALLOWED_FRESHNESS = {"current", "review-needed", "archival"}
ALLOWED_SOURCE = {"internal-only", "external-verified", "mixed"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}
ALLOWED_METHOD_MATURITY = {"candidate", "field-tested", "transferred", "canonical", "deprecated"}
ALLOWED_RELATION_TYPES = {
    "derived-from", "evidenced-by", "implemented-as", "compared-with",
    "applied-in", "validated-by", "supersedes", "superseded-by"
}

SKIP_DIRS = {
    ".obsidian", "07_archive", ".git", "node_modules", "__pycache__",
    "_site", "site", "skills", "docs"
}
SKIP_FILES = {"README.md"}

errors = []
checked = 0
method_ids = {}

for md in sorted(Path(".").rglob("*.md")):
    if any(skip in md.parts for skip in SKIP_DIRS):
        continue
    if md.name in SKIP_FILES:
        continue
    if md.parent == Path("."):
        continue

    try:
        post = frontmatter.load(md)
        meta = post.metadata
    except Exception as exc:
        errors.append(f"{md}: front-matter parse error: {exc}")
        continue

    checked += 1

    for field in REQUIRED_FIELDS:
        if field not in meta:
            errors.append(f"{md}: missing required field `{field}`")

    if meta.get("status") not in ALLOWED_STATUS:
        errors.append(f"{md}: invalid status `{meta.get('status')}` — allowed: {sorted(ALLOWED_STATUS)}")
    if meta.get("domain") not in ALLOWED_DOMAIN:
        errors.append(f"{md}: invalid domain `{meta.get('domain')}` — allowed: {sorted(ALLOWED_DOMAIN)}")
    if meta.get("freshness") not in ALLOWED_FRESHNESS:
        errors.append(f"{md}: invalid freshness `{meta.get('freshness')}` — allowed: {sorted(ALLOWED_FRESHNESS)}")
    if meta.get("source_scope") not in ALLOWED_SOURCE:
        errors.append(f"{md}: invalid source_scope `{meta.get('source_scope')}` — allowed: {sorted(ALLOWED_SOURCE)}")
    if meta.get("confidence") not in ALLOWED_CONFIDENCE:
        errors.append(f"{md}: invalid confidence `{meta.get('confidence')}` — allowed: {sorted(ALLOWED_CONFIDENCE)}")
    if not isinstance(meta.get("tags", []), list):
        errors.append(f"{md}: `tags` must be a YAML list, got {type(meta.get('tags'))}")
    if not isinstance(meta.get("version", 1), (int, float)):
        errors.append(f"{md}: `version` must be a number")

    relations = meta.get("relations")
    if relations is not None:
        if not isinstance(relations, list):
            errors.append(f"{md}: `relations` must be a YAML list")
        else:
            for index, relation in enumerate(relations):
                if not isinstance(relation, dict):
                    errors.append(f"{md}: relations[{index}] must be a mapping")
                    continue
                relation_type = relation.get("type")
                target = relation.get("target")
                if relation_type not in ALLOWED_RELATION_TYPES:
                    errors.append(
                        f"{md}: relations[{index}].type `{relation_type}` invalid — "
                        f"allowed: {sorted(ALLOWED_RELATION_TYPES)}"
                    )
                if not isinstance(target, str) or not target.strip():
                    errors.append(f"{md}: relations[{index}].target must be a non-empty string")

    if meta.get("domain") == "method":
        method_id = meta.get("id")
        maturity = meta.get("maturity")

        if not isinstance(method_id, str) or not method_id.startswith("method:"):
            errors.append(f"{md}: method records require stable `id` beginning with `method:`")
        else:
            if method_id in method_ids:
                errors.append(f"{md}: duplicate method id `{method_id}` also used by {method_ids[method_id]}")
            else:
                method_ids[method_id] = md

        if maturity not in ALLOWED_METHOD_MATURITY:
            errors.append(
                f"{md}: method records require valid `maturity` — "
                f"allowed: {sorted(ALLOWED_METHOD_MATURITY)}"
            )

        if not isinstance(relations, list):
            errors.append(f"{md}: method records require a `relations` YAML list")

print(f"Checked {checked} NSE knowledge file(s).")
if errors:
    print(f"\n❌ {len(errors)} front-matter error(s):\n")
    for error in errors:
        print(f"  - {error}")
    sys.exit(1)

print("✅ All NSE knowledge-note front-matter valid.")
