#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_registry() -> list[dict]:
    return json.loads((repo_root() / "projections" / "registry.json").read_text()).get("skills", [])


def main() -> int:
    skills = load_registry()
    print("Projection status")
    print(f"Total skills: {len(skills)}")

    modes: dict[str, int] = {}
    for skill in skills:
        mode = skill.get("claude_projection", {}).get("mode", "missing")
        modes[mode] = modes.get(mode, 0) + 1

    print("Claude modes:")
    for mode in sorted(modes):
        print(f"- {mode}: {modes[mode]}")

    print("\nPer skill:")
    for skill in skills:
        codex = skill.get("codex_projection", {})
        claude = skill.get("claude_projection", {})
        codex_state = "on" if codex.get("enabled") else "off"
        print(
            f"- {skill['id']}: category={skill.get('category')} | "
            f"codex={codex_state}:{codex.get('target_name')} | "
            f"claude={claude.get('mode')}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
