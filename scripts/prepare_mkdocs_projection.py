#!/usr/bin/env python3
"""Build a disposable MkDocs docs tree from canonical NSE source paths.

The repository root remains the canonical knowledge layout. MkDocs requires a
child `docs_dir`, so this script creates a generated read projection rather
than moving or duplicating canonical source files in version control.
"""

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / ".mkdocs-docs"

SOURCE_PATHS = [
    "README.md",
    "00_system",
    "01_research",
    "02_competitors",
    "03_technical",
    "04_reports",
    "05_projects",
    "06_templates",
    "08_assets",
    "09_methods",
    "skills",
]


def copy_source(relative_path: str) -> None:
    source = ROOT / relative_path
    if not source.exists():
        return

    destination = DEST / relative_path
    if source.is_dir():
        shutil.copytree(source, destination, dirs_exist_ok=True)
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def main() -> None:
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)

    for relative_path in SOURCE_PATHS:
        copy_source(relative_path)

    markdown_count = sum(1 for _ in DEST.rglob("*.md"))
    print(f"Prepared MkDocs projection at {DEST.relative_to(ROOT)} with {markdown_count} markdown file(s).")


if __name__ == "__main__":
    main()
