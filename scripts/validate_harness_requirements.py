#!/usr/bin/env python3
"""Internal validator for per-skill harness_requirements declarations.

Validates the *structure* of `examples/harness-requirements/*.yaml` against the
template in `templates/skill-harness-requirements.yaml` and the contracts in
`docs/harness-requirements-for-skills.md`.

This is a declaration validator, not a policy engine. It checks shape and
vocabulary only; it does not execute, authorize, or enforce anything.

Enforces:
- top-level `harness_requirements` mapping with all required fields present;
- autonomy `floor`/`ceiling` use the canonical AletheIA vocabulary
  (no `bounded_autonomous` / unbounded `autonomous` fork);
- `expected_tools[].risk_class` in {low, medium, high, critical};
- `restricted_tools[].restriction` in {deny, require_approval, transform, log_only};
- list fields are lists; `audit_requirements` carries the required log keys.
"""
from __future__ import annotations

from pathlib import Path

import yaml

# Canonical autonomy levels — mirror AletheIA schemas/agent-harness-contract.schema.json
# and docs/concepts/autonomy-levels.md. `bounded_autonomous` and unbounded
# `autonomous` are NOT canonical and must not appear.
CANONICAL_AUTONOMY = {'observe', 'advise', 'act_with_approval', 'autonomous_within_bounds'}
FORKED_AUTONOMY = {'bounded_autonomous', 'autonomous'}

RISK_CLASSES = {'low', 'medium', 'high', 'critical'}
RESTRICTIONS = {'deny', 'require_approval', 'transform', 'log_only'}

REQUIRED_TOP = [
    'skill_id',
    'version',
    'autonomy',
    'expected_tools',
    'restricted_tools',
    'approval_gates',
    'required_evidence',
    'escalation_triggers',
    'audit_requirements',
]
REQUIRED_AUTONOMY_KEYS = {'floor', 'ceiling', 'rationale'}
REQUIRED_AUDIT_KEYS = {
    'log_skill_id',
    'log_task_id',
    'log_tool_calls',
    'log_policy_verdict',
    'log_evidence_refs',
    'log_human_approval',
}
LIST_FIELDS = [
    'expected_tools',
    'restricted_tools',
    'approval_gates',
    'required_evidence',
    'escalation_triggers',
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _check_autonomy(autonomy: object, rel: str, errors: list[str]) -> None:
    if not isinstance(autonomy, dict):
        errors.append(f'{rel}: autonomy must be a mapping')
        return
    missing = sorted(REQUIRED_AUTONOMY_KEYS - set(autonomy))
    if missing:
        errors.append(f'{rel}: autonomy missing keys: {", ".join(missing)}')
    for level_key in ('floor', 'ceiling'):
        value = autonomy.get(level_key)
        if value is None:
            continue
        if value in FORKED_AUTONOMY:
            errors.append(
                f'{rel}: autonomy.{level_key}="{value}" is not canonical; '
                f'use one of {sorted(CANONICAL_AUTONOMY)}'
            )
        elif value not in CANONICAL_AUTONOMY:
            errors.append(
                f'{rel}: autonomy.{level_key}="{value}" not in {sorted(CANONICAL_AUTONOMY)}'
            )


def _check_expected_tools(tools: object, rel: str, errors: list[str]) -> None:
    if not isinstance(tools, list):
        return  # list-ness already reported by caller
    for i, tool in enumerate(tools):
        if not isinstance(tool, dict):
            errors.append(f'{rel}: expected_tools[{i}] must be a mapping')
            continue
        for key in ('name', 'purpose', 'risk_class'):
            if key not in tool:
                errors.append(f'{rel}: expected_tools[{i}] missing "{key}"')
        rc = tool.get('risk_class')
        if rc is not None and rc not in RISK_CLASSES:
            errors.append(
                f'{rel}: expected_tools[{i}].risk_class="{rc}" not in {sorted(RISK_CLASSES)}'
            )


def _check_restricted_tools(tools: object, rel: str, errors: list[str]) -> None:
    if not isinstance(tools, list):
        return
    for i, tool in enumerate(tools):
        if not isinstance(tool, dict):
            errors.append(f'{rel}: restricted_tools[{i}] must be a mapping')
            continue
        if 'name' not in tool:
            errors.append(f'{rel}: restricted_tools[{i}] missing "name"')
        restriction = tool.get('restriction')
        if restriction is None:
            errors.append(f'{rel}: restricted_tools[{i}] missing "restriction"')
        elif restriction not in RESTRICTIONS:
            errors.append(
                f'{rel}: restricted_tools[{i}].restriction="{restriction}" '
                f'not in {sorted(RESTRICTIONS)}'
            )


def _check_audit(audit: object, rel: str, errors: list[str]) -> None:
    if not isinstance(audit, dict):
        errors.append(f'{rel}: audit_requirements must be a mapping')
        return
    missing = sorted(REQUIRED_AUDIT_KEYS - set(audit))
    if missing:
        errors.append(f'{rel}: audit_requirements missing keys: {", ".join(missing)}')


def validate_file(path: Path, root: Path) -> list[str]:
    rel = str(path.relative_to(root))
    errors: list[str] = []
    try:
        doc = yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:  # pragma: no cover - defensive
        return [f'{rel}: invalid YAML: {exc}']

    if not isinstance(doc, dict) or 'harness_requirements' not in doc:
        return [f'{rel}: missing top-level "harness_requirements" mapping']

    hr = doc['harness_requirements']
    if not isinstance(hr, dict):
        return [f'{rel}: "harness_requirements" must be a mapping']

    for field in REQUIRED_TOP:
        if field not in hr:
            errors.append(f'{rel}: missing field "{field}"')

    if not isinstance(hr.get('skill_id'), str) or not hr.get('skill_id'):
        errors.append(f'{rel}: skill_id must be a non-empty string')

    for field in LIST_FIELDS:
        if field in hr and not isinstance(hr[field], list):
            errors.append(f'{rel}: "{field}" must be a list')

    _check_autonomy(hr.get('autonomy'), rel, errors)
    _check_expected_tools(hr.get('expected_tools'), rel, errors)
    _check_restricted_tools(hr.get('restricted_tools'), rel, errors)
    _check_audit(hr.get('audit_requirements'), rel, errors)
    return errors


def main() -> int:
    root = repo_root()
    paths = sorted(root.glob('examples/harness-requirements/*.yaml'))

    if not paths:
        print('No harness_requirements examples found to validate.')
        return 0

    errors: list[str] = []
    for path in paths:
        errors.extend(validate_file(path, root))

    if errors:
        print('Validation failed:')
        for err in errors:
            print(f'- {err}')
        return 1

    print(f'Validated {len(paths)} harness_requirements declaration(s).')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
