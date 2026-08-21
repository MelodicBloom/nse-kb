#!/usr/bin/env python3
"""Validate executable Agent Skills separately from NSE knowledge-note front matter."""

import re
import sys
from pathlib import Path

try:
    import frontmatter
except ImportError:
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "python-frontmatter", "-q"], check=True)
    import frontmatter

SKILLS_DIR = Path("skills")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
errors = []
checked = 0

if SKILLS_DIR.exists():
    for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        checked += 1
        try:
            post = frontmatter.load(skill_file)
            meta = post.metadata
        except Exception as exc:
            errors.append(f"{skill_file}: front-matter parse error: {exc}")
            continue

        name = meta.get("name")
        description = meta.get("description")
        directory_name = skill_file.parent.name

        if not isinstance(name, str) or not name:
            errors.append(f"{skill_file}: missing required string `name`")
        elif not NAME_RE.fullmatch(name):
            errors.append(f"{skill_file}: `name` must use lowercase letters, numbers, and hyphens")
        elif name != directory_name:
            errors.append(f"{skill_file}: `name` `{name}` must match directory `{directory_name}`")

        if not isinstance(description, str) or not description:
            errors.append(f"{skill_file}: missing required string `description`")
        else:
            if not description.startswith("Use when"):
                errors.append(f"{skill_file}: `description` must begin with `Use when`")
            if len(description) > 500:
                errors.append(f"{skill_file}: `description` exceeds 500 characters")

        unexpected = sorted(set(meta) - {"name", "description"})
        if unexpected:
            errors.append(
                f"{skill_file}: unexpected front-matter keys {unexpected}; "
                "keep executable skill metadata minimal"
            )

print(f"Checked {checked} skill(s).")
if errors:
    print(f"\n❌ {len(errors)} skill validation error(s):\n")
    for error in errors:
        print(f"  - {error}")
    sys.exit(1)

print("✅ All executable skills valid.")
