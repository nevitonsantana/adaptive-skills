#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

REQUIRED_FRONTMATTER = {'name', 'description', 'version', 'owner'}
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


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return {}
    meta = {}
    for line in lines[1:]:
        if line.strip() == '---':
            break
        if ':' not in line:
            continue
        key, value = line.split(':', 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta


def validate_skill(path: Path, generic: bool) -> list[str]:
    errors = []
    text = path.read_text()
    meta = parse_frontmatter(text)
    missing = sorted(REQUIRED_FRONTMATTER - set(meta))
    if missing:
        errors.append(f'{path}: missing frontmatter keys: {", ".join(missing)}')

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

    generic_skill_paths = sorted(root.glob('skills/*/*/SKILL.md'))
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
