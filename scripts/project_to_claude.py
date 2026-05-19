#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_registry() -> list[dict]:
    return json.loads((repo_root() / "projections" / "registry.json").read_text()).get("skills", [])


def main() -> int:
    print("Claude projection is selective and availability-based in v0.\n")
    for skill in load_registry():
        projection = skill.get("claude_projection", {})
        print(f"- {skill['id']}: mode={projection.get('mode')} target={projection.get('target_path')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
