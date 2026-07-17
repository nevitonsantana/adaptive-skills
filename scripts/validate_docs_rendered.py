#!/usr/bin/env python3
"""Validate the rendered Blume documentation quality baseline."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    dist = root / "apps" / "docs" / "dist"
    errors: list[str] = []
    pages = sorted(dist.rglob("index.html"))

    if not pages:
        print("Rendered documentation validation failed:")
        print("- no index.html pages found; run the documentation build first")
        return 1

    for page in pages:
        text = page.read_text(errors="ignore")
        relative = page.relative_to(dist)
        h1_count = len(re.findall(r"<h1(?:\\s|>)", text))
        if h1_count != 1:
            errors.append(f"{relative}: expected exactly one visible H1, found {h1_count}")

        heading_levels = [int(level) for level in re.findall(r"<h([1-6])(?:\\s|>)", text)]
        for previous, current in zip(heading_levels, heading_levels[1:]):
            if current > previous + 1:
                errors.append(
                    f"{relative}: heading hierarchy jumps from H{previous} to H{current}"
                )
                break

        for href in re.findall(r'href="([^"]+)"', text):
            parsed = urlparse(href)
            if parsed.scheme or parsed.netloc:
                continue
            target = parsed.path.lower()
            if target.endswith((".md", ".mdx")):
                errors.append(f"{relative}: local link opens Markdown instead of a rendered route: {href}")

    if errors:
        print("Rendered documentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Validated {len(pages)} rendered documentation pages: "
        "one H1 each, continuous heading hierarchy, and no local Markdown links."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
