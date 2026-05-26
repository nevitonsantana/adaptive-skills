#!/usr/bin/env python3
"""Internal validator for Adaptive Skills SKILL.md files.

Enforces:
- agentskills.io spec top-level fields (`name`, `description`) per ADR-004
- library convention: `metadata.version`, `metadata.owner`, `metadata.category`
- 11 required body sections (library enrichment, outside spec scope)
- no forbidden generic references in `skills/` (case study terms live only in `domain-packs/`)
"""
from __future__ import annotations

import json
import re
from pathlib import Path

REQUIRED_TOP_LEVEL = {'name', 'description'}
REQUIRED_METADATA = {'version', 'owner', 'category'}
REQUIRED_SECTIONS = [
    'Overview',
    'When to Use',
    'When NOT to Use',
    'Core Moves',
    'Optional Modules',
    'Activation Triggers',
    'Expected Output',
    'Verification',
    'Handoff Signals',
    'Pairs Well With',
    'Anti-patterns',
]
FORBIDDEN_GENERIC_PATTERNS = [
    'Crisis Monitor',
    'AGENTS.md',
    'CLAUDE.md',
    'docs/PROJECT_STATE.md',
    '/Users/',
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_frontmatter(text: str) -> tuple[dict[str, str], dict[str, str]]:
    """Return (top_level, metadata) parsed from YAML-ish frontmatter.

    Supports a single nested block under `metadata:` with two-space indent.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return {}, {}
    top: dict[str, str] = {}
    meta: dict[str, str] = {}
    in_metadata = False
    for line in lines[1:]:
        if line.strip() == '---':
            break
        if not line.strip():
            continue
        if in_metadata and line.startswith('  ') and ':' in line:
            key, value = line.strip().split(':', 1)
            meta[key.strip()] = value.strip().strip('"')
            continue
        in_metadata = False
        if ':' not in line:
            continue
        key, value = line.split(':', 1)
        key = key.strip()
        value = value.strip().strip('"')
        if key == 'metadata' and value == '':
            in_metadata = True
            continue
        top[key] = value
    return top, meta


def validate_skill(path: Path, generic: bool) -> list[str]:
    errors: list[str] = []
    text = path.read_text()
    top, meta = parse_frontmatter(text)

    missing_top = sorted(REQUIRED_TOP_LEVEL - set(top))
    if missing_top:
        errors.append(f'{path}: missing top-level frontmatter keys: {", ".join(missing_top)}')

    missing_meta = sorted(REQUIRED_METADATA - set(meta))
    if missing_meta:
        errors.append(f'{path}: missing metadata keys: {", ".join(missing_meta)}')

    headings = set(re.findall(r'^# (.+)$', text, flags=re.M))
    for section in REQUIRED_SECTIONS:
        if section not in headings:
            errors.append(f'{path}: missing section {section}')

    if generic:
        for pattern in FORBIDDEN_GENERIC_PATTERNS:
            if pattern in text:
                errors.append(f'{path}: forbidden generic reference: {pattern}')
    return errors


def main() -> int:
    root = repo_root()
    errors: list[str] = []

    generic_skill_paths = sorted(root.glob('skills/*/SKILL.md'))
    domain_pack_paths = sorted(root.glob('domain-packs/*/skills/*/SKILL.md'))

    for path in generic_skill_paths:
        errors.extend(validate_skill(path, generic=True))
    for path in domain_pack_paths:
        errors.extend(validate_skill(path, generic=False))

    registry = json.loads((root / 'projections' / 'registry.json').read_text())
    for item in registry.get('skills', []):
        source = root / item['source_path']
        if not source.exists():
            errors.append(f"registry source missing: {item['source_path']}")

    if errors:
        print('Validation failed:')
        for err in errors:
            print(f'- {err}')
        return 1

    print(f'Validated {len(generic_skill_paths)} generic skills and {len(domain_pack_paths)} domain-pack skills.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
