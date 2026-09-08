#!/usr/bin/env python3
"""
Sync changed NSE knowledge markdown files to a Notion Notes database.
Triggered by GitHub Actions on push to main.

Executable skills and implementation/planning docs are intentionally excluded;
they are separate authority surfaces, not ordinary NSE knowledge notes.

Required env vars:
  NOTION_TOKEN        -- Notion internal integration token
  NOTION_DATABASE_ID  -- Notes database ID (from URL)
  GITHUB_REPOSITORY   -- set automatically by GitHub Actions
"""
import os
import subprocess
import sys
from pathlib import Path

try:
    import frontmatter
    from notion_client import Client
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install",
                    "python-frontmatter", "notion-client", "-q"], check=True)
    import frontmatter
    from notion_client import Client

NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "")
DB_ID = os.environ.get("NOTION_DATABASE_ID", "")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "MelodicBloom/nse-kb")

if not NOTION_TOKEN or not DB_ID:
    print("NOTION_TOKEN or NOTION_DATABASE_ID not set — skipping Notion sync.")
    sys.exit(0)

notion = Client(auth=NOTION_TOKEN)

STATUS_MAP = {"canonical": "Canonical", "verified": "Verified", "capture": "Capture",
              "draft": "Draft", "working": "Working", "template": "Template", "archive": "Archive"}
DOMAIN_MAP = {"research": "Research", "competitor": "Competitor", "technical": "Technical",
              "report": "Report", "project": "Project", "template": "Template",
              "system": "System", "asset": "Asset", "method": "Method"}
FRESHNESS_MAP = {"current": "Current", "review-needed": "Review Needed", "archival": "Archival"}
SOURCE_MAP = {"internal-only": "Internal Only", "external-verified": "External Verified", "mixed": "Mixed"}
CONFIDENCE_MAP = {"high": "High", "medium": "Medium", "low": "Low"}
EXCLUDED_PREFIXES = ("skills/", "docs/", "07_archive/")


def get_changed_files():
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD", "--", "*.md"],
        capture_output=True, text=True, check=False
    )
    return [
        path.strip()
        for path in result.stdout.split("\n")
        if path.strip()
        and os.path.exists(path.strip())
        and not path.strip().startswith(EXCLUDED_PREFIXES)
        and Path(path.strip()).name != "README.md"
    ]


def build_props(meta, filepath):
    filename = Path(filepath).name
    date_str = filename.split("__")[0] if "__" in filename else None
    file_url = f"https://github.com/{GITHUB_REPO}/blob/main/{filepath}"

    props = {
        "Title": {"title": [{"text": {"content": meta.get("title", Path(filepath).stem)}}]},
        "Status": {"select": {"name": STATUS_MAP.get(meta.get("status", "draft"), "Draft")}},
        "Domain": {"select": {"name": DOMAIN_MAP.get(meta.get("domain", "system"), "System")}},
        "Freshness": {"select": {"name": FRESHNESS_MAP.get(meta.get("freshness", "current"), "Current")}},
        "Source Scope": {"select": {"name": SOURCE_MAP.get(meta.get("source_scope", "mixed"), "Mixed")}},
        "Confidence": {"select": {"name": CONFIDENCE_MAP.get(meta.get("confidence", "medium"), "Medium")}},
        "Version": {"number": int(meta.get("version", 1))},
        "Tags": {"multi_select": [{"name": str(tag)} for tag in meta.get("tags", [])]},
        "File Path": {"url": file_url},
        "Owner": {"rich_text": [{"text": {"content": meta.get("owner", "operator")}}]},
    }
    if date_str:
        props["Date Created"] = {"date": {"start": date_str}}
    if meta.get("last_reviewed"):
        props["Last Reviewed"] = {"date": {"start": str(meta["last_reviewed"])}}
    related = meta.get("related", [])
    if related:
        props["Related"] = {"rich_text": [{"text": {"content": ", ".join(str(item) for item in related)}}]}
    return props


def upsert(filepath):
    with open(filepath) as handle:
        post = frontmatter.load(handle)
    props = build_props(post.metadata, filepath)

    existing = notion.databases.query(
        database_id=DB_ID,
        filter={"property": "File Path", "url": {"equals": props["File Path"]["url"]}}
    )
    if existing["results"]:
        page_id = existing["results"][0]["id"]
        notion.pages.update(page_id=page_id, properties=props)
        print(f"  Updated: {filepath}")
    else:
        notion.pages.create(parent={"database_id": DB_ID}, properties=props)
        print(f"  Created: {filepath}")


def main():
    files = get_changed_files()
    if not files:
        print("No changed NSE knowledge .md files detected.")
        return
    print(f"Syncing {len(files)} file(s) to Notion...")
    for filepath in files:
        try:
            upsert(filepath)
        except Exception as exc:
            print(f"  ERROR on {filepath}: {exc}")


if __name__ == "__main__":
    main()
