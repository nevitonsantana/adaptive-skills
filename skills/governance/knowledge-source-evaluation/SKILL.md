---
name: knowledge-source-evaluation
description: Evaluate whether a candidate document can be registered as a governed knowledge pack, and at what maturity level.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: governance
  knowledge_aware: true
---

# Overview

Use this skill before adding a document, framework, policy, or persona to the knowledge registry. It checks whether the source has the metadata, ownership, and exposure rules required by the [Knowledge Governance Layer](../../../../aletheia/docs/concepts/knowledge-governance-layer.md), and recommends a maturity level (minimal, operational, governed) or refusal.

# When to Use

- A user proposes adding a base of knowledge to a project.
- A skill author wants to depend on a new framework.
- A source's review cycle has elapsed and re-evaluation is due.

# When NOT to Use

- Authoring the framework's content itself (use the source owner's process).
- Resolving conflict between already-registered sources (use `knowledge-conflict-resolution`).
- Checking restricted-exposure risk at runtime (use `restricted-context-check`).

# Core Moves

1. Identify the candidate: name, owner, link, intended use.
2. Classify type using the source taxonomy in [knowledge-source-contract](../../../../aletheia/docs/contracts/knowledge-source-contract.md).
3. Assess sensitivity and authority.
4. Determine scope: which task families, skills, agents.
5. Decide retrieval mode and exposure policy.
6. Check whether a capsule is required and exists.
7. Recommend maturity level — or refuse with reason.

# Optional Modules

- **Capsule readiness check** — verify the capsule exists and is operational, not narrative.
- **Provenance check** — confirm `source_integrity_notes` are sufficient.
- **Allowlist scoping** — recommend explicit `allowed_skills` / `allowed_agents`.

# Activation Triggers

- New source proposed.
- Existing source's review cycle expired.
- A skill declares a new dependency type not yet present in the registry.

# Expected Output

```yaml
evaluation:
  candidate:
    proposed_id: <kebab-case>
    name: <name>
    proposed_type: <source_type>
    owner: <person-or-team>
  classification:
    sensitivity: <level>
    authority_level: <level>
    scope: [<scope-tag>, ...]
  retrieval:
    retrieval_mode: <mode>
    full_text_exposure: <allowed|forbidden|conditional>
    export_allowed: <bool>
    capsule_required: <bool>
    capsule_present: <bool>
  recommendation: register_minimal | register_operational | register_governed | refuse
  refusal_reason: <if applicable>
  required_fixes: [<...>]
```

# Verification

- All required manifest fields can be populated from this evaluation.
- If recommendation is `register_governed`, a reviewer other than the author signed off.
- If the candidate is `restricted` or higher, `human_review_required_for` is non-empty.

# Handoff Signals

- If `refuse`, hand back to the proposer with the required fixes.
- If `register_minimal`, mark sources as low-maturity and exclude from required slots.

# Pairs Well With

- `restricted-context-check`
- `knowledge-conflict-resolution`

# Anti-patterns

- Registering a source without an owner.
- Registering a `confidential` or higher source without `human_review_required_for`.
- Approving a `capsule_first` source with no capsule.
- Inferring sensitivity from "feels internal" rather than from the owner's classification.
