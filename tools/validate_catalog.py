#!/usr/bin/env python3
"""Validate catalog.json against the skills on disk.

Deliberately small: no dependencies, no network, no installer logic. It answers
one question — would an agent that trusts catalog.json find what it promises?

Run: python3 tools/validate_catalog.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
SKILLS_DIR = ROOT / "skills"

SCHEMA = 2
SLUG_RE = re.compile(r"^[a-z][a-z0-9-]*$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")

TEXT_FIELDS = ("label", "description", "path", "folder", "version", "reads", "writes", "notes")
BOOL_FIELDS = (
    "sensitive_reads",
    "requires_authentication",
    "may_prompt_authentication",
    "network_access",
    "external_writes",
    "destructive_operations",
)


def read_frontmatter(skill_file: Path) -> dict[str, str]:
    """Parse the leading `---` block. Only top-level `key: value` pairs matter here."""
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def main() -> int:
    errors: list[str] = []

    try:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL catalog.json unreadable: {exc}")
        return 1

    if catalog.get("schema") != SCHEMA:
        errors.append(f"schema must be {SCHEMA}, found {catalog.get('schema')!r}")
    if not str(catalog.get("repository", "")).startswith("https://"):
        errors.append("repository must be an https URL so a reader can find the source")

    entries = catalog.get("skills")
    if not isinstance(entries, list) or not entries:
        print("FAIL catalog.json has no skills list")
        return 1

    seen: set[str] = set()
    for entry in entries:
        slug = entry.get("slug", "<missing slug>")
        where = f"{slug}:"

        if not SLUG_RE.match(str(slug)):
            errors.append(f"{where} slug must be lowercase-hyphenated")
        if slug in seen:
            errors.append(f"{where} duplicate entry")
        seen.add(slug)

        for field in TEXT_FIELDS:
            if not str(entry.get(field, "")).strip():
                errors.append(f"{where} missing {field}")
        for field in BOOL_FIELDS:
            if not isinstance(entry.get(field), bool):
                errors.append(f"{where} {field} must be true or false, not a guess")
        caps = entry.get("capabilities")
        if not isinstance(caps, list) or not caps:
            errors.append(f"{where} capabilities must be a non-empty list")

        if not VERSION_RE.match(str(entry.get("version", ""))):
            errors.append(f"{where} version must look like 0.1.0")

        expected_path = f"skills/{slug}/SKILL.md"
        if entry.get("path") != expected_path:
            errors.append(f"{where} path must be {expected_path}")
        if entry.get("folder") != f"skills/{slug}/":
            errors.append(f"{where} folder must be skills/{slug}/ — installing copies the folder")

        skill_file = ROOT / expected_path
        if not skill_file.is_file():
            errors.append(f"{where} {expected_path} does not exist")
            continue

        front = read_frontmatter(skill_file)
        if front.get("name") != slug:
            errors.append(f"{where} SKILL.md frontmatter name is {front.get('name')!r}")
        if len(front.get("description", "")) < 40:
            errors.append(f"{where} SKILL.md needs a description an agent can route on")

        # Honesty rule: mail/network capability without an auth flag is a false promise.
        if entry.get("network_access") and not (
            entry.get("requires_authentication") or entry.get("may_prompt_authentication")
        ):
            errors.append(f"{where} network_access without any authentication flag")

    on_disk = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}
    for orphan in sorted(on_disk - seen):
        errors.append(f"skills/{orphan}/ exists but is not in catalog.json")

    if errors:
        print("FAIL catalogue validation")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"OK catalogue: {len(entries)} skills, metadata complete and paths resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
