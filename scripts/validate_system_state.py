#!/usr/bin/env python3
"""Validate the compact Adaptive Skills SYSTEM_STATE first-load index."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "SYSTEM_STATE.md"
MAX_LINES = 120
REQUIRED_HEADINGS = (
    "## Project identity",
    "## Current architecture summary",
    "## Delivered baseline",
    "## Active and planned evolution",
    "## Deprecated or merged plans",
    "## Documentation health",
    "## Cognitive debt and open risks",
    "## Next safe steps",
    "## Last reviewed",
)


def main() -> int:
    text = STATE.read_text(encoding="utf-8")
    errors: list[str] = []

    if len(text.splitlines()) > MAX_LINES:
        errors.append(f"SYSTEM_STATE exceeds {MAX_LINES} lines")
    if "not a universal source of truth" not in text:
        errors.append("SYSTEM_STATE must declare its authority boundary")
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"missing heading: {heading}")

    for ref in re.findall(r"\]\(([^)]+)\)", text):
        if ref.startswith(("https://", "http://")):
            continue
        if not (ROOT / ref).resolve().exists():
            errors.append(f"local reference does not resolve: {ref}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("Adaptive Skills SYSTEM_STATE validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
