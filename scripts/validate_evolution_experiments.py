#!/usr/bin/env python3
"""Structural validator for the Skill Evolution Validation Layer.

Checks validation cases (evolution/validation-cases/) and skill evolution
experiments (evolution/experiments/) for structural integrity and governance
guardrails. This validator is intentionally *only* structural:

  - no runtime, no benchmark engine
  - no LLM / model calls
  - no network
  - no writes to skills/ or anywhere else

It mirrors the dependency-free style of scripts/validate_evolution.py and does
not modify the existing evolution pipeline. See
docs/evolution/optimization-boundaries.md for the rules it enforces.

Rules (SDD section 6):
  1. every experiment skill_id exists under skills/ (or in registry.json);
  2. every experiment lists >=1 validation_cases, each referencing a real case;
  3. every validation case declares sensitivity;
  4. confidential/restricted/regulated cases must be synthetic_only + capsule_only
     (no raw governed content);
  5. protected_surface_touched (or a protected target_surface) requires
     human_review_required: true;
  6. no experiment declares a write target under skills/;
  7. recommendation.outcome is in the allowed set and is never approved/merged;
  8. knowledge-aware skills require human_review_required. A skill is
     knowledge-aware if it declares metadata.knowledge_aware: true in its
     SKILL.md frontmatter, is in the baseline set, or the experiment references
     a case typed knowledge_aware.
"""
from __future__ import annotations

import json
from pathlib import Path

# --- Canonical taxonomy, reused from scripts/validate_evolution.py -----------
VALID_PROTECTED_SURFACES = {
    'name', 'description', 'When to Use', 'When NOT to Use', 'Core Moves',
    'skill-domain', 'skill-category', 'skill-merge-split', 'skill-thesis',
}
VALID_PROPOSAL_TARGETS = {
    'Activation Triggers', 'Optional Modules', 'Verification', 'Anti-patterns',
    'templates/', 'checklists/', 'examples/', 'references/', 'changelog.md',
}
VALID_CHANGE_TYPES = {
    'trigger-adjustment', 'template-refinement', 'checklist-addition',
    'example-addition', 'reference-addition', 'module-candidate',
    'new-skill-candidate', 'verification-tightening', 'anti-pattern-tightening',
}

# --- Validation-layer-specific vocabulary ------------------------------------
VALID_CASE_TYPES = {'baseline', 'regression', 'edge_case', 'knowledge_aware'}
VALID_SENSITIVITIES = {'public', 'synthetic', 'internal', 'confidential', 'restricted', 'regulated'}
SENSITIVE_VALUES = {'confidential', 'restricted', 'regulated'}
VALID_SOURCE_POLICIES = {'synthetic_only', 'authorized_pack', 'public_source'}
# Outcomes align with evolution result_modes plus `defer`; never approved/merged.
VALID_OUTCOMES = {'reinforced', 'no-change', 'proposal-created', 'defer', 'rejected'}
FORBIDDEN_OUTCOMES = {'approved', 'merged'}
# Baseline fallback set. The authoritative source is each skill's own
# `metadata.knowledge_aware: true` frontmatter, loaded via
# load_knowledge_aware_skills(); this set covers skills that are knowledge-aware
# by nature even if the flag is ever absent.
KNOWLEDGE_AWARE_SKILLS = {
    'knowledge-source-evaluation', 'restricted-context-check',
    'knowledge-conflict-resolution',
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


# --- Minimal indentation-aware YAML-subset parser ----------------------------
# Handles the 2-level nesting these files use: scalars, lists (`- item`), and
# nested maps. No third-party dependency (NFR: vendor-agnostic, low weight).
def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(' '))


def _strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] in '"\'' and value[-1] == value[0]:
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> dict:
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return {}
    body: list[str] = []
    for line in lines[1:]:
        if line.strip() == '---':
            break
        if not line.strip() or line.strip().startswith('#'):
            continue
        body.append(line)
    pos = [0]
    return _parse_map(body, pos, 0)


def _parse_map(lines: list[str], pos: list[int], indent: int) -> dict:
    result: dict = {}
    while pos[0] < len(lines):
        line = lines[pos[0]]
        cur = _indent(line)
        if cur < indent or line.strip().startswith('- '):
            break
        if cur > indent:  # defensive: unexpected deeper line
            pos[0] += 1
            continue
        key, _, value = line.strip().partition(':')
        key = key.strip()
        value = value.strip()
        pos[0] += 1
        if value:
            result[key] = _strip_quotes(value)
            continue
        # No inline value: peek for a nested list or map.
        if pos[0] < len(lines):
            nxt = lines[pos[0]]
            nind = _indent(nxt)
            if nind > indent and nxt.strip().startswith('- '):
                result[key] = _parse_list(lines, pos, nind)
                continue
            if nind > indent:
                result[key] = _parse_map(lines, pos, nind)
                continue
        result[key] = ''
    return result


def _parse_list(lines: list[str], pos: list[int], indent: int) -> list:
    items: list = []
    while pos[0] < len(lines):
        line = lines[pos[0]]
        if _indent(line) != indent or not line.strip().startswith('-'):
            break
        item = line.strip()[1:].strip()
        pos[0] += 1
        if item:  # skip bare `-` placeholders (templates)
            items.append(_strip_quotes(item))
    return items


# --- Helpers -----------------------------------------------------------------
def _as_bool(value: object) -> bool:
    return str(value).strip().lower() == 'true'


def load_skill_ids(root: Path) -> set[str]:
    ids = {p.parent.name for p in root.glob('skills/*/SKILL.md')}
    ids |= {p.parent.name for p in root.glob('domain-packs/*/skills/*/SKILL.md')}
    registry_path = root / 'evolution' / 'registry.json'
    if registry_path.exists():
        registry = json.loads(registry_path.read_text())
        ids |= {s.get('skill_id') for s in registry.get('skills', [])}
    return {i for i in ids if i}


def load_knowledge_aware_skills(root: Path) -> set[str]:
    """Skills declaring `metadata.knowledge_aware: true` in SKILL.md frontmatter,
    unioned with the baseline KNOWLEDGE_AWARE_SKILLS set. This makes contract R11
    (knowledge-aware experiments require human review) enforceable even when the
    paired validation case is not itself `case_type: knowledge_aware`.
    """
    aware = set(KNOWLEDGE_AWARE_SKILLS)
    for path in list(root.glob('skills/*/SKILL.md')) + list(root.glob('domain-packs/*/skills/*/SKILL.md')):
        meta = parse_frontmatter(path.read_text())
        md = meta.get('metadata')
        flag = md.get('knowledge_aware') if isinstance(md, dict) else None
        if _as_bool(flag):
            aware.add(str(meta.get('name') or path.parent.name))
    return aware


def _content_files(base: Path) -> list[Path]:
    """All *.md under base except READMEs and anything in a templates/ dir."""
    out = []
    for path in sorted(base.rglob('*.md')):
        if path.name == 'README.md':
            continue
        if 'templates' in path.relative_to(base).parts:
            continue
        out.append(path)
    return out


# --- Validators --------------------------------------------------------------
def validate_cases(root: Path, skills: set[str], errors: list[str]) -> dict[str, dict]:
    cases: dict[str, dict] = {}
    base = root / 'evolution' / 'validation-cases'
    if not base.exists():
        return cases
    for path in _content_files(base):
        rel = path.relative_to(root)
        meta = parse_frontmatter(path.read_text())
        required = ['id', 'skill_id', 'case_type', 'sensitivity', 'source_policy',
                    'input', 'expected_behavior', 'acceptance_criteria', 'failure_signals']
        missing = [k for k in required if not meta.get(k)]
        if missing:
            errors.append(f'{rel}: missing validation-case fields {missing}')
            continue
        case_id = str(meta['id'])
        cases[case_id] = meta
        if meta['skill_id'] not in skills:
            errors.append(f'{rel}: unknown skill_id {meta["skill_id"]}')
        if meta['case_type'] not in VALID_CASE_TYPES:
            errors.append(f'{rel}: invalid case_type {meta["case_type"]}')
        if meta['sensitivity'] not in VALID_SENSITIVITIES:
            errors.append(f'{rel}: invalid sensitivity {meta["sensitivity"]}')
        if meta['source_policy'] not in VALID_SOURCE_POLICIES:
            errors.append(f'{rel}: invalid source_policy {meta["source_policy"]}')
        if not isinstance(meta.get('input'), dict) or not meta['input'].get('task'):
            errors.append(f'{rel}: input.task is required')
        exp = meta.get('expected_behavior')
        if not isinstance(exp, dict) or not exp.get('must_do') or not exp.get('must_not_do'):
            errors.append(f'{rel}: expected_behavior.must_do and must_not_do are required')
        # Rule 4: sensitive cases must be synthetic_only + capsule_only (no raw content).
        if meta['sensitivity'] in SENSITIVE_VALUES:
            if meta['source_policy'] != 'synthetic_only':
                errors.append(f'{rel}: sensitivity {meta["sensitivity"]} requires source_policy: synthetic_only')
            if not _as_bool(meta.get('capsule_only')):
                errors.append(f'{rel}: sensitivity {meta["sensitivity"]} requires capsule_only: true')
    return cases


def validate_experiments(root: Path, skills: set[str], knowledge_aware_skills: set[str], cases: dict[str, dict], errors: list[str]) -> int:
    base = root / 'evolution' / 'experiments'
    if not base.exists():
        return 0
    count = 0
    for path in _content_files(base):
        rel = path.relative_to(root)
        meta = parse_frontmatter(path.read_text())
        required = ['id', 'skill_id', 'purpose', 'source_observations', 'validation_cases',
                    'candidate_change', 'baseline_result', 'candidate_result',
                    'regression_check', 'recommendation', 'human_review_required']
        missing = [k for k in required if not meta.get(k)]
        if missing:
            errors.append(f'{rel}: missing experiment fields {missing}')
            continue
        count += 1
        # Rule 1
        if meta['skill_id'] not in skills:
            errors.append(f'{rel}: unknown skill_id {meta["skill_id"]}')
        # Rule 2
        vcs = meta['validation_cases'] if isinstance(meta['validation_cases'], list) else []
        if not vcs:
            errors.append(f'{rel}: experiment must reference at least one validation_case')
        for vc in vcs:
            if vc not in cases:
                errors.append(f'{rel}: unknown validation_case {vc}')

        change = meta['candidate_change'] if isinstance(meta['candidate_change'], dict) else {}
        target = str(change.get('target_surface', ''))
        change_type = str(change.get('change_type', ''))
        hrr = _as_bool(meta.get('human_review_required'))
        protected_touched = _as_bool(meta.get('protected_surface_touched'))

        # Rule 6: no write target under skills/
        if target.startswith('skills/') or change_type.startswith('skills/'):
            errors.append(f'{rel}: candidate_change may not target skills/ directly')
        # target surface must be an allowed proposal target or a (flagged) protected surface
        if target in VALID_PROTECTED_SURFACES:
            protected_touched = True  # naming a protected surface counts as touching it
            if not _as_bool(meta.get('protected_surface_touched')):
                errors.append(f'{rel}: target_surface {target} is protected; set protected_surface_touched: true')
        elif target not in VALID_PROPOSAL_TARGETS:
            errors.append(f'{rel}: invalid target_surface {target}')
        if change_type and change_type not in VALID_CHANGE_TYPES:
            errors.append(f'{rel}: invalid change_type {change_type}')
        # Rule 5
        if protected_touched and not hrr:
            errors.append(f'{rel}: protected_surface_touched requires human_review_required: true')

        # Rule 7
        rec = meta['recommendation'] if isinstance(meta['recommendation'], dict) else {}
        outcome = str(rec.get('outcome', ''))
        if outcome in FORBIDDEN_OUTCOMES:
            errors.append(f'{rel}: outcome {outcome} is not allowed (experiments are evidence, not decisions)')
        elif outcome not in VALID_OUTCOMES:
            errors.append(f'{rel}: invalid recommendation.outcome {outcome}')
        if not rec.get('rationale'):
            errors.append(f'{rel}: recommendation.rationale is required')

        # Rule 8: knowledge-aware skills / cases require human review.
        # A skill is knowledge-aware if it declares metadata.knowledge_aware: true
        # (loaded from frontmatter), is in the baseline set, or the experiment
        # references a case typed knowledge_aware.
        knowledge_aware = meta['skill_id'] in knowledge_aware_skills
        knowledge_aware = knowledge_aware or any(
            cases.get(vc, {}).get('case_type') == 'knowledge_aware' for vc in vcs
        )
        if knowledge_aware and not hrr:
            errors.append(f'{rel}: knowledge-aware experiment requires human_review_required: true')
    return count


def main() -> int:
    root = repo_root()
    errors: list[str] = []
    skills = load_skill_ids(root)
    knowledge_aware_skills = load_knowledge_aware_skills(root)
    cases = validate_cases(root, skills, errors)
    experiments = validate_experiments(root, skills, knowledge_aware_skills, cases, errors)

    if errors:
        print('Skill evolution validation failed:')
        for err in errors:
            print(f'- {err}')
        return 1

    print(f'Validated {len(cases)} validation case(s) and {experiments} experiment(s).')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
