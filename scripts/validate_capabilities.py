#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def list_values(lines: list[str], start_index: int) -> tuple[list[str], int]:
    values: list[str] = []
    index = start_index + 1
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            index += 1
            continue
        # Values for an item field are indented six spaces. A new top-level
        # collection item is indented two spaces and must stop the list.
        if line.startswith('      - '):
            values.append(stripped[2:].strip().strip('"'))
            index += 1
            continue
        break
    return values, index


def parse_items(path: Path, collection_key: str) -> list[dict[str, object]]:
    lines = path.read_text().splitlines()
    items: list[dict[str, object]] = []
    in_collection = False
    current: dict[str, object] | None = None
    index = 0

    while index < len(lines):
        raw = lines[index]
        stripped = raw.strip()
        if stripped == f'{collection_key}:':
            in_collection = True
            index += 1
            continue
        if not in_collection:
            index += 1
            continue
        if stripped and not raw.startswith('  '):
            break
        if raw.startswith('  - '):
            if current:
                items.append(current)
            current = {}
            pair = stripped[2:]
            if ':' in pair:
                key, value = pair.split(':', 1)
                current[key.strip()] = value.strip().strip('"')
            index += 1
            continue
        # Only parse direct fields on a collection item. Nested maps such as
        # `when:` are intentionally ignored by this lightweight validator.
        if current is not None and raw.startswith('    ') and not raw.startswith('      ') and ':' in stripped:
            key, value = stripped.split(':', 1)
            key = key.strip()
            value = value.strip()
            if value:
                current[key] = value.strip('"')
                index += 1
            else:
                values, next_index = list_values(lines, index)
                current[key] = values
                index = next_index
            continue
        index += 1

    if current:
        items.append(current)
    return items


def load_skill_ids(root: Path) -> set[str]:
    ids: set[str] = set()
    for path in sorted(root.glob('skills/*/*/SKILL.md')):
        ids.add(path.parent.name)
    for path in sorted(root.glob('domain-packs/*/skills/*/SKILL.md')):
        ids.add(path.parent.name)
    return ids


def main() -> int:
    root = repo_root()
    errors: list[str] = []

    capability_dir = root / 'capabilities'
    required_files = [
        capability_dir / 'catalog.yaml',
        capability_dir / 'routes.yaml',
        capability_dir / 'profiles.yaml',
        capability_dir / 'dependencies.yaml',
        capability_dir / 'schemas' / 'capability.schema.json',
        capability_dir / 'schemas' / 'execution-record.schema.json',
        capability_dir / 'schemas' / 'learning-record.schema.json',
    ]
    for path in required_files:
        if not path.exists():
            errors.append(f'missing required capability file: {path.relative_to(root)}')

    if errors:
        for error in errors:
            print(f'- {error}')
        return 1

    skills = load_skill_ids(root)
    capabilities = parse_items(capability_dir / 'catalog.yaml', 'capabilities')
    profiles = parse_items(capability_dir / 'profiles.yaml', 'profiles')
    routes = parse_items(capability_dir / 'routes.yaml', 'routes')
    relationships = parse_items(capability_dir / 'dependencies.yaml', 'relationships')

    capability_ids: set[str] = set()
    mode_ids = {str(profile.get('id')) for profile in profiles}

    required_capability_fields = {
        'id', 'kind', 'source_skill', 'category', 'default_mode', 'allowed_modes', 'intent', 'evidence'
    }
    for capability in capabilities:
        capability_id = str(capability.get('id', ''))
        if not capability_id:
            errors.append('capability missing id')
            continue
        if capability_id in capability_ids:
            errors.append(f'duplicate capability id: {capability_id}')
        capability_ids.add(capability_id)

        missing = sorted(required_capability_fields - set(capability))
        if missing:
            errors.append(f'{capability_id}: missing fields {missing}')

        if capability_id not in skills:
            errors.append(f'{capability_id}: capability id does not match a published skill id')

        source = root / str(capability.get('source_skill', ''))
        if not source.exists():
            errors.append(f'{capability_id}: source_skill not found: {capability.get("source_skill")}')

        default_mode = str(capability.get('default_mode', ''))
        allowed_modes = set(capability.get('allowed_modes', []))
        if default_mode and default_mode not in allowed_modes:
            errors.append(f'{capability_id}: default_mode must be listed in allowed_modes')
        unknown_modes = sorted(mode for mode in allowed_modes if mode not in mode_ids)
        if unknown_modes:
            errors.append(f'{capability_id}: allowed_modes reference unknown profiles {unknown_modes}')

        evidence = capability.get('evidence', [])
        if not isinstance(evidence, list) or not evidence:
            errors.append(f'{capability_id}: evidence must be a non-empty list')

    for profile in profiles:
        profile_id = str(profile.get('id', ''))
        if not profile_id:
            errors.append('profile missing id')
        for key in ('depth', 'use_when', 'requires'):
            if key not in profile:
                errors.append(f'{profile_id}: profile missing {key}')

    for route in routes:
        route_id = str(route.get('id', ''))
        activates = route.get('activates', [])
        if not isinstance(activates, list) or not activates:
            errors.append(f'{route_id}: route must activate at least one capability')
        for capability_id in activates:
            if capability_id not in capability_ids:
                errors.append(f'{route_id}: activates unknown capability {capability_id}')
        mode = str(route.get('mode', ''))
        if mode not in mode_ids:
            errors.append(f'{route_id}: route references unknown mode {mode}')

    known_nodes = capability_ids | skills
    for relationship in relationships:
        source = str(relationship.get('from', ''))
        target = str(relationship.get('to', ''))
        if source not in known_nodes:
            errors.append(f'relationship references unknown source: {source}')
        if target not in known_nodes:
            errors.append(f'relationship references unknown target: {target}')
        if 'relation' not in relationship:
            errors.append(f'relationship {source}->{target} missing relation')
        if 'reason' not in relationship:
            errors.append(f'relationship {source}->{target} missing reason')

    if errors:
        print('Capability validation failed:')
        for error in errors:
            print(f'- {error}')
        return 1

    print(
        f'Validated {len(capability_ids)} capabilities, '
        f'{len(mode_ids)} profiles, {len(routes)} routes, and {len(relationships)} relationships.'
    )
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
