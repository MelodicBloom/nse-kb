#!/usr/bin/env python3
"""
Validate front-matter schema across all KB markdown files.
Run as pre-commit hook or CI step.

Usage:
  python3 scripts/validate_frontmatter.py
"""
import sys
from pathlib import Path

try:
    import frontmatter
except ImportError:
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "python-frontmatter", "-q"])
    import frontmatter

REQUIRED_FIELDS = [
    "title", "status", "domain", "freshness", "last_reviewed",
    "source_scope", "tags", "confidence", "version"
]
ALLOWED_STATUS     = {"canonical", "draft", "archive", "verified", "capture", "working", "template"}
ALLOWED_DOMAIN     = {"research", "competitor", "technical", "report", "project", "template", "system", "asset"}
ALLOWED_FRESHNESS  = {"current", "review-needed", "archival"}
ALLOWED_SOURCE     = {"internal-only", "external-verified", "mixed"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}

SKIP_DIRS  = {".obsidian", "07_archive", ".git", "node_modules", "__pycache__", "_site", "site"}
SKIP_FILES = {"README.md"}

errors  = []
checked = 0

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
    except Exception as e:
        errors.append(f"{md}: front-matter parse error: {e}")
        continue

    checked += 1

    for field in REQUIRED_FIELDS:
        if field not in meta:
            errors.append(f"{md}: missing required field `{field}`")

    if meta.get("status")     not in ALLOWED_STATUS:
        errors.append(f"{md}: invalid status `{meta.get('status')}` — allowed: {sorted(ALLOWED_STATUS)}")
    if meta.get("domain")     not in ALLOWED_DOMAIN:
        errors.append(f"{md}: invalid domain `{meta.get('domain')}` — allowed: {sorted(ALLOWED_DOMAIN)}")
    if meta.get("freshness")  not in ALLOWED_FRESHNESS:
        errors.append(f"{md}: invalid freshness `{meta.get('freshness')}` — allowed: {sorted(ALLOWED_FRESHNESS)}")
    if meta.get("source_scope") not in ALLOWED_SOURCE:
        errors.append(f"{md}: invalid source_scope `{meta.get('source_scope')}` — allowed: {sorted(ALLOWED_SOURCE)}")
    if meta.get("confidence") not in ALLOWED_CONFIDENCE:
        errors.append(f"{md}: invalid confidence `{meta.get('confidence')}` — allowed: {sorted(ALLOWED_CONFIDENCE)}")
    if not isinstance(meta.get("tags", []), list):
        errors.append(f"{md}: `tags` must be a YAML list, got {type(meta.get('tags'))}")
    if not isinstance(meta.get("version", 1), (int, float)):
        errors.append(f"{md}: `version` must be a number")

print(f"Checked {checked} file(s).")
if errors:
    print(f"\n\u274c {len(errors)} front-matter error(s):\n")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("\u2705 All front-matter valid.")
