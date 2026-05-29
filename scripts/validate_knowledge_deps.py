#!/usr/bin/env python3
"""Validator for skill knowledge-dependency manifests.

Checks authored `skill-knowledge-dependency.yaml` files (and the template)
against the Skill Knowledge Dependency contract. The canonical schema lives in
AletheIA:

  aletheia/schemas/aletheia-skill-knowledge-dependency.schema.json
  aletheia/docs/contracts/skill-knowledge-dependency-contract.md

The rules are mirrored here as Python constants so this repo's CI stays
self-contained (no cross-repo checkout). Keep these enums in sync with the
AletheIA schema when it changes.

Scope is bounded to structural validation. It does NOT resolve sources, fetch
packs, or evaluate permissions — that is the AletheIA resolver's job.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

VERSION_RE = r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$"

ACCEPTED_TYPES = {
    "compliance_policy",
    "security_policy",
    "privacy_policy",
    "accessibility_guideline",
    "operating_model",
    "product_strategy",
    "proprietary_framework",
    "business_design_framework",
    "design_system",
    "persona",
    "research_finding",
    "benchmark",
    "stakeholder_input",
}

AUTHORITY_LEVELS = {
    "mandatory",
    "normative",
    "procedural",
    "strategic",
    "interpretive",
    "evidence_proxy",
    "evidential",
    "comparative",
    "contextual",
}

RETRIEVAL_MODES = {
    "capsule_first",
    "excerpt_only",
    "metadata_only",
    "full_source_allowed",
    "human_review_required",
    "blocked",
}

FALLBACK_ENUMS = {
    "missing_required_source": {
        "stop_and_request_source",
        "continue_in_generic_mode",
        "abort",
    },
    "missing_optional_source": {
        "continue_with_assumption_marker",
        "omit_silently",
    },
    "restricted_source": {
        "request_authorized_context_pack",
        "downgrade_to_capsule",
        "refuse",
    },
    "conflicting_sources": {
        "apply_source_precedence_policy",
        "escalate_to_human_review",
    },
}

TOP_LEVEL_ALLOWED = {
    "skill",
    "version",
    "knowledge_dependencies",
    "fallback_behavior",
    "output_requirements",
}
TOP_LEVEL_REQUIRED = {"skill", "version", "knowledge_dependencies", "fallback_behavior"}

SLOT_ALLOWED = {
    "required",
    "required_when",
    "accepted_types",
    "min_authority",
    "preferred_retrieval_mode",
    "notes",
}

OUTPUT_REQ_KEYS = {
    "cite_satisfying_packs",
    "cite_unsatisfied_slots",
    "list_active_restrictions",
    "list_conflicts_and_resolutions",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def validate_manifest(path: Path) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(repo_root())

    try:
        data = yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:  # pragma: no cover - defensive
        return [f"{rel}: invalid YAML: {exc}"]

    if not isinstance(data, dict):
        return [f"{rel}: top level must be a mapping"]

    unknown_top = sorted(set(data) - TOP_LEVEL_ALLOWED)
    if unknown_top:
        errors.append(f"{rel}: unknown top-level keys: {', '.join(unknown_top)}")

    missing_top = sorted(TOP_LEVEL_REQUIRED - set(data))
    if missing_top:
        errors.append(f"{rel}: missing required keys: {', '.join(missing_top)}")

    if data.get("skill") in (None, ""):
        errors.append(f"{rel}: 'skill' must be a non-empty string")

    version = data.get("version")
    if not isinstance(version, str) or not re.match(VERSION_RE, version):
        errors.append(f"{rel}: 'version' must match semver pattern (got {version!r})")

    errors.extend(_validate_dependencies(rel, data.get("knowledge_dependencies")))
    errors.extend(_validate_fallback(rel, data.get("fallback_behavior")))
    errors.extend(_validate_output_requirements(rel, data.get("output_requirements")))
    return errors


def _validate_dependencies(rel: Path, deps: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(deps, dict) or not deps:
        errors.append(f"{rel}: 'knowledge_dependencies' must be a non-empty mapping")
        return errors

    for name, slot in deps.items():
        loc = f"{rel}: knowledge_dependencies.{name}"
        if not isinstance(slot, dict):
            errors.append(f"{loc}: must be a mapping")
            continue

        unknown = sorted(set(slot) - SLOT_ALLOWED)
        if unknown:
            errors.append(f"{loc}: unknown keys: {', '.join(unknown)}")

        if "required" not in slot and "required_when" not in slot:
            errors.append(f"{loc}: must declare 'required' or 'required_when'")

        if "required" in slot and not isinstance(slot["required"], bool):
            errors.append(f"{loc}: 'required' must be a boolean")

        if "required_when" in slot:
            rw = slot["required_when"]
            if not isinstance(rw, list) or not rw or not all(
                isinstance(x, str) and x for x in rw
            ):
                errors.append(f"{loc}: 'required_when' must be a non-empty list of strings")

        accepted = slot.get("accepted_types")
        if not isinstance(accepted, list) or not accepted:
            errors.append(f"{loc}: 'accepted_types' is required and must be non-empty")
        else:
            bad = sorted(set(accepted) - ACCEPTED_TYPES)
            if bad:
                errors.append(f"{loc}: invalid accepted_types: {', '.join(bad)}")

        if "min_authority" in slot and slot["min_authority"] not in AUTHORITY_LEVELS:
            errors.append(f"{loc}: invalid min_authority: {slot['min_authority']!r}")

        if (
            "preferred_retrieval_mode" in slot
            and slot["preferred_retrieval_mode"] not in RETRIEVAL_MODES
        ):
            errors.append(
                f"{loc}: invalid preferred_retrieval_mode: {slot['preferred_retrieval_mode']!r}"
            )
    return errors


def _validate_fallback(rel: Path, fallback: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(fallback, dict):
        errors.append(f"{rel}: 'fallback_behavior' must be a mapping")
        return errors

    unknown = sorted(set(fallback) - set(FALLBACK_ENUMS))
    if unknown:
        errors.append(f"{rel}: fallback_behavior unknown keys: {', '.join(unknown)}")

    for key, allowed in FALLBACK_ENUMS.items():
        if key not in fallback:
            errors.append(f"{rel}: fallback_behavior missing '{key}'")
        elif fallback[key] not in allowed:
            errors.append(
                f"{rel}: fallback_behavior.{key} invalid: {fallback[key]!r}"
            )
    return errors


def _validate_output_requirements(rel: Path, output_req: object) -> list[str]:
    if output_req is None:
        return []
    errors: list[str] = []
    if not isinstance(output_req, dict):
        return [f"{rel}: 'output_requirements' must be a mapping"]
    unknown = sorted(set(output_req) - OUTPUT_REQ_KEYS)
    if unknown:
        errors.append(f"{rel}: output_requirements unknown keys: {', '.join(unknown)}")
    for key, value in output_req.items():
        if key in OUTPUT_REQ_KEYS and not isinstance(value, bool):
            errors.append(f"{rel}: output_requirements.{key} must be a boolean")
    return errors


def main() -> int:
    root = repo_root()
    paths = sorted(root.glob("skills/*/skill-knowledge-dependency.yaml"))
    template = root / "templates" / "skill-knowledge-dependency.yaml"
    if template.exists():
        paths.append(template)

    if not paths:
        print("No skill-knowledge-dependency.yaml manifests found; nothing to validate.")
        return 0

    errors: list[str] = []
    for path in paths:
        errors.extend(validate_manifest(path))

    if errors:
        print("Knowledge-dependency validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"Validated {len(paths)} knowledge-dependency manifest(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
