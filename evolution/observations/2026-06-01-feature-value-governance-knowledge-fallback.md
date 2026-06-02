---
observation_id: obs-2026-06-01-feature-value-governance-knowledge-fallback
skill_id: feature-value-governance
context: skill-evolution-validation-fase6
domain: product
date: 2026-06-01
modules_activated: none
trigger_matches: a feature judgment was requested with no governed knowledge pack available, so the skill had to operate in generic mode
observed_issue_type: possible-missing-module
evidence_refs: skills/feature-value-governance/SKILL.md, docs/declaring-knowledge-dependencies.md
attribution_guess: the skill correctly fell back to general criteria and marked the inference when no pack was available, but a maintainer wondered whether an explicit generic-mode evidence-quality module would help; evidence is thin and this is the sensitive product-decision skill
result_mode: new-module-candidate
---

# Observation

## Summary
A synthetic feature-worth judgment was requested with no governed knowledge pack available.
`feature-value-governance` operated in generic mode, applied general value/lever/evidence
criteria, and marked the inference — the correct knowledge-aware fallback behavior.

## Why this attribution is plausible
The fallback worked. The open question is whether a small, explicit "generic-mode
evidence-quality" optional module would help agents be consistent when no pack is present. The
signal is a single synthetic case and the skill is knowledge-aware and product-sensitive, so
the bar for any change is high.

## Why this result mode is valid
`new-module-candidate` is the honest fit: a possible module, not a confirmed need. It is
explicitly not a rewrite of Core Moves.

## Follow-up
Look for at least one more real signal before promoting. Any experiment here is knowledge-aware
and must use synthetic/capsule-only material and require human review.
