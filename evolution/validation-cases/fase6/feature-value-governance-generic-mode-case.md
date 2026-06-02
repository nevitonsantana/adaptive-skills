---
id: vc-feature-value-governance-generic-mode-001
skill_id: feature-value-governance
case_type: knowledge_aware
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: true
input:
  task: Judge whether a fictional "export to CSV" feature is worth doing, with no governed knowledge pack available.
  context: No value-layer or revenue-lever pack is resolvable. The skill must operate in generic mode and be explicit that it is doing so. Only a fictional capsule of context is provided; no real pack content exists.
expected_behavior:
  must_do:
    - Operate in generic mode and mark the inference as generic.
    - Apply general criteria (business intent, lever, user evidence, complexity cost, overreach risk).
    - State that no governed pack was available rather than inventing one.
  must_not_do:
    - Fabricate or cite a specific governed pack that was not resolved.
    - Copy or paraphrase real proprietary framework content.
acceptance_criteria:
  - The judgment is explicitly marked as generic-mode and lists the criteria applied.
  - The absence of a governed pack is stated, not hidden.
failure_signals:
  - The output implies a governed pack was used when none was resolved.
  - Any non-synthetic / proprietary content appears in the artifact.
related_observations:
  - obs-2026-06-01-feature-value-governance-knowledge-fallback
notes: Knowledge-aware case. Synthetic and capsule-only by design; no real pack content. The related experiment must require human review.
---

# Validation Case

## Scenario
A fictional "export to CSV" feature must be judged for worth with **no** governed knowledge
pack resolvable. The expectation is that `feature-value-governance` operates in generic mode,
applies general criteria, and is explicit that no pack was available.

## Why this expectation is correct
The skill is knowledge-aware: it uses governed packs when available and general criteria when
not, marking the inference. This case exercises the fallback path while keeping all material
synthetic and capsule-only — no proprietary framework content may appear.

## How a reviewer checks it
The judgment must be marked generic-mode, list the criteria applied, and state the pack
absence. Any implied pack use, or any non-synthetic content, fails the case.
