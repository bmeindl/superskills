#!/usr/bin/env python3
"""Leak gate for a public catalogue.

This repository is published. Its skills are written next to a private workspace,
so the realistic failure is not a malicious commit but an absent-minded one: a
copied path, an employer's name, a colleague, a token that was in the buffer.

The gate scans every tracked text file for those shapes and fails loudly. It is a
tripwire, not a proof of safety — a human still reads the diff.

Run: python3 tools/check_public_safety.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (label, pattern, files exempt from this rule and why)
RULES: list[tuple[str, str, set[str]]] = [
    ("private workspace name", r"ground[- ]control", set()),
    # The author's name belongs in the licence and nowhere else.
    ("author name", r"\bBenjamin\b|\bMeindl\b", {"LICENSE"}),
    ("employer", r"\bIU\b|\bIU-Group\b|iu\.org|Syntea|SynteaOS", set()),
    ("private agent identity", r"Claudine|Rushing Claudine|Quintus", set()),
    ("issue tracker key", r"\bSYNT-\d+", set()),
    ("home directory path", r"/Users/[a-z]|/home/[a-z]|C:\\\\Users\\\\", set()),
    ("private host or VPN address", r"\b100\.\d{1,3}\.\d{1,3}\.\d{1,3}\b|\b204\.168\.206\.41\b|forgejo", set()),
    ("email address", r"[\w.+-]+@[\w-]+\.[a-z]{2,}", set()),
    ("credential-shaped token", r"gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[abpsr]-", set()),
    ("secret assignment", r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*['\"][^'\"]{8,}", set()),
]

SKIP_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".icns", ".pdf", ".zip", ".woff", ".woff2"}
# This file quotes the very strings it forbids.
SELF = "tools/check_public_safety.py"


def tracked_files() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    return [line for line in out.splitlines() if line]


def main() -> int:
    findings: list[str] = []
    scanned = 0

    for rel in tracked_files():
        if rel == SELF or Path(rel).suffix.lower() in SKIP_SUFFIXES:
            continue
        try:
            text = (ROOT / rel).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        scanned += 1

        for label, pattern, exempt in RULES:
            if rel in exempt:
                continue
            for match in re.finditer(pattern, text):
                line_no = text.count("\n", 0, match.start()) + 1
                findings.append(f"{rel}:{line_no}  {label}: {match.group(0)!r}")

    if findings:
        print(f"FAIL public-safety gate ({len(findings)} finding(s) in {scanned} files)")
        for finding in findings:
            print(f"  - {finding}")
        print("\nRemove the private content or, if the match is genuinely safe,")
        print("add a narrow exemption in tools/check_public_safety.py with a reason.")
        return 1

    print(f"OK public-safety gate: {scanned} tracked text files, no private content found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
