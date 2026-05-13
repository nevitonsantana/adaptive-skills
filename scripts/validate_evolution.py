#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

VALID_AUTOMATION_LEVELS = {
    'manual-assisted',
    'semi-automatic',
    'governed-autoevolution',
}
VALID_PILOT_PRIORITIES = {'now', 'later', 'hold'}
VALID_PROTECTED_SURFACES = {
    'name',
    'description',
    'When to Use',
    'When NOT to Use',
    'Core Moves',
    'skill-domain',
    'skill-category',
    'skill-merge-split',
    'skill-thesis',
}
VALID_PROPOSAL_TARGETS = {
    'Activation Triggers',
    'Optional Modules',
    'Verification',
    'Anti-patterns',
    'templates/',
    'checklists/',
    'examples/',
    'references/',
    'changelog.md',
}
VALID_RESULT_MODES = {
    'reinforced',
    'no-change',
    'proposal-created',
    'new-module-candidate',
    'new-skill-candidate',
    'rejected',
}
VALID_PROPOSAL_STATUSES = {'approved', 'rejected', 'deferred'}
VALID_CHANGE_TYPES = {
    'trigger-adjustment',
    'template-refinement',
    'checklist-addition',
    'example-addition',
    'reference-addition',
    'module-candidate',
    'new-skill-candidate',
    'verification-tightening',
    'anti-pattern-tightening',
}
LIST_KEYS = {
    'modules_activated',
    'trigger_matches',
    'evidence_refs',
    'source_observations',
    'source_proposals',
    'protected_surfaces',
    'proposal_targets',
    'result_modes',
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_frontmatter(text: str) -> dict[str, object]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return {}
    meta: dict[str, object] = {}
    for line in lines[1:]:
        if line.strip() == '---':
            break
        if ':' not in line:
            continue
        key, value = line.split(':', 1)
        key = key.strip()
        value = value.strip()
        if key in LIST_KEYS:
            meta[key] = [item.strip() for item in value.split(',') if item.strip()] if value else []
        else:
            meta[key] = value
    return meta


def load_skill_ids(root: Path) -> dict[str, dict[str, str]]:
    skills: dict[str, dict[str, str]] = {}
    for path in sorted(root.glob('skills/*/*/SKILL.md')):
        meta = parse_frontmatter(path.read_text())
        skill_id = str(meta.get('name') or path.parent.name)
        skills[skill_id] = {'scope': 'generic', 'path': str(path.relative_to(root)), 'domain': path.parts[-3]}
    for path in sorted(root.glob('domain-packs/*/skills/*/SKILL.md')):
        meta = parse_frontmatter(path.read_text())
        skill_id = str(meta.get('name') or path.parent.name)
        skills[skill_id] = {'scope': 'domain-pack', 'path': str(path.relative_to(root)), 'domain': path.parts[-4]}
    return skills


def main() -> int:
    root = repo_root()
    errors: list[str] = []
    skills = load_skill_ids(root)
    registry = json.loads((root / 'evolution' / 'registry.json').read_text())
    items = registry.get('skills', [])

    registry_ids: set[str] = set()
    for item in items:
        skill_id = item.get('skill_id')
        if skill_id in registry_ids:
            errors.append(f'duplicate registry skill_id: {skill_id}')
            continue
        registry_ids.add(skill_id)
        if skill_id not in skills:
            errors.append(f'registry references unknown skill: {skill_id}')
            continue
        if item.get('scope') not in {'generic', 'domain-pack'}:
            errors.append(f'{skill_id}: invalid scope {item.get("scope")}')
        if item.get('scope') != skills[skill_id]['scope']:
            errors.append(f'{skill_id}: registry scope does not match published skill scope')
        if item.get('domain') != skills[skill_id]['domain']:
            errors.append(f'{skill_id}: registry domain does not match published skill domain')
        if item.get('automation_level') not in VALID_AUTOMATION_LEVELS:
            errors.append(f'{skill_id}: invalid automation_level {item.get("automation_level")}')
        if item.get('pilot_priority') not in VALID_PILOT_PRIORITIES:
            errors.append(f'{skill_id}: invalid pilot_priority {item.get("pilot_priority")}')
        if item.get('scope') == 'domain-pack' and item.get('pilot_priority') != 'hold' and not item.get('pilot_priority_exception_reason'):
            errors.append(f'{skill_id}: domain-pack skills must default to hold unless an explicit exception reason is provided')
        protected = set(item.get('protected_surfaces', []))
        if not protected.issubset(VALID_PROTECTED_SURFACES):
            errors.append(f'{skill_id}: invalid protected_surfaces {sorted(protected - VALID_PROTECTED_SURFACES)}')
        targets = set(item.get('proposal_targets', []))
        if not targets.issubset(VALID_PROPOSAL_TARGETS):
            errors.append(f'{skill_id}: invalid proposal_targets {sorted(targets - VALID_PROPOSAL_TARGETS)}')
        modes = set(item.get('result_modes', []))
        if not modes.issubset(VALID_RESULT_MODES):
            errors.append(f'{skill_id}: invalid result_modes {sorted(modes - VALID_RESULT_MODES)}')

    missing = sorted(set(skills) - registry_ids)
    for skill_id in missing:
        errors.append(f'published skill missing from evolution registry: {skill_id}')

    observation_paths = [p for p in sorted((root / 'evolution' / 'observations').glob('*.md')) if p.name != 'README.md']
    observations: dict[str, dict[str, object]] = {}
    required_observation = {
        'observation_id', 'skill_id', 'context', 'domain', 'date', 'modules_activated',
        'trigger_matches', 'observed_issue_type', 'evidence_refs', 'attribution_guess', 'result_mode'
    }
    for path in observation_paths:
        meta = parse_frontmatter(path.read_text())
        missing_keys = required_observation - set(meta)
        if missing_keys:
            errors.append(f'{path.relative_to(root)}: missing observation fields {sorted(missing_keys)}')
            continue
        obs_id = str(meta['observation_id'])
        observations[obs_id] = meta
        skill_id = str(meta['skill_id'])
        if skill_id not in registry_ids:
            errors.append(f'{path.relative_to(root)}: unknown skill_id {skill_id}')
        if meta['result_mode'] not in VALID_RESULT_MODES:
            errors.append(f'{path.relative_to(root)}: invalid result_mode {meta["result_mode"]}')
        if not meta['evidence_refs']:
            errors.append(f'{path.relative_to(root)}: evidence_refs cannot be empty')

    proposal_dirs = {
        'approved': root / 'evolution' / 'proposals' / 'approved',
        'rejected': root / 'evolution' / 'proposals' / 'rejected',
        'deferred': root / 'evolution' / 'proposals' / 'deferred',
    }
    required_proposal = {
        'proposal_id', 'skill_id', 'source_observations', 'target_surface', 'change_type',
        'automation_level', 'status', 'rationale', 'global_consistency_risk'
    }
    for status, folder in proposal_dirs.items():
        for path in sorted(folder.glob('*.md')):
            if path.name == 'README.md':
                continue
            meta = parse_frontmatter(path.read_text())
            missing_keys = required_proposal - set(meta)
            if missing_keys:
                errors.append(f'{path.relative_to(root)}: missing proposal fields {sorted(missing_keys)}')
                continue
            skill_id = str(meta['skill_id'])
            if skill_id not in registry_ids:
                errors.append(f'{path.relative_to(root)}: unknown skill_id {skill_id}')
                continue
            if meta['status'] != status:
                errors.append(f'{path.relative_to(root)}: status {meta["status"]} does not match folder {status}')
            if meta['automation_level'] not in VALID_AUTOMATION_LEVELS:
                errors.append(f'{path.relative_to(root)}: invalid automation_level {meta["automation_level"]}')
            if meta['change_type'] not in VALID_CHANGE_TYPES:
                errors.append(f'{path.relative_to(root)}: invalid change_type {meta["change_type"]}')
            target = str(meta['target_surface'])
            item = next(i for i in items if i['skill_id'] == skill_id)
            if target in item.get('protected_surfaces', []):
                errors.append(f'{path.relative_to(root)}: target_surface {target} is protected for {skill_id}')
            if target not in item.get('proposal_targets', []):
                errors.append(f'{path.relative_to(root)}: target_surface {target} is not an allowed proposal target for {skill_id}')
            for obs in meta['source_observations']:
                if obs not in observations:
                    errors.append(f'{path.relative_to(root)}: unknown source observation {obs}')
            if meta['change_type'] == 'new-skill-candidate' and len(meta['source_observations']) < 2:
                errors.append(f'{path.relative_to(root)}: new-skill-candidate requires more than one source observation')

    review_paths = [p for p in sorted((root / 'evolution' / 'reviews').glob('*.md')) if p.name != 'README.md']
    required_review = {
        'review_id', 'scope', 'date', 'decision', 'source_observations',
        'source_proposals', 'what_changed', 'what_remained_local', 'why_no_change_is_valid'
    }
    for path in review_paths:
        meta = parse_frontmatter(path.read_text())
        missing_keys = required_review - set(meta)
        if missing_keys:
            errors.append(f'{path.relative_to(root)}: missing review fields {sorted(missing_keys)}')
            continue
        for obs in meta['source_observations']:
            if obs not in observations:
                errors.append(f'{path.relative_to(root)}: unknown source observation {obs}')

    if errors:
        print('Evolution validation failed:')
        for err in errors:
            print(f'- {err}')
        return 1

    print(f'Validated evolution registry for {len(registry_ids)} skills, {len(observations)} observations, {sum(1 for folder in proposal_dirs.values() for p in folder.glob("*.md") if p.name != "README.md")} proposals, and {len(review_paths)} reviews.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
