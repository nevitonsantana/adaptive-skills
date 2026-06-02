---
id: vc-ux-writing-label-clarity-001
skill_id: ux-writing
case_type: baseline
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Improve a fictional audit-status label that mixes two languages and obscures its consequence.
  context: A status chip reads "Pendente review" on an audit screen. Users may misread what the label means or what happens next.
expected_behavior:
  must_do:
    - Classify the wording issue before rewriting.
    - Rewrite for precision before elegance.
    - Preserve semantic safety (the label must not imply a different consequence).
  must_not_do:
    - Prioritize a clever phrasing over an accurate one.
    - Change the meaning of the audit state.
acceptance_criteria:
  - The rewrite is single-language, scannable, and consequence-clear.
  - The audit semantics are unchanged.
failure_signals:
  - The new copy is elegant but ambiguous about the consequence.
  - The rewrite shifts what the audit state means.
related_observations:
  - obs-2026-04-13-ux-writing-crisis-monitor-clarity
notes: Synthetic scenario modeled on the Crisis Monitor mixed-language label signal. No governed content used.
---

# Validation Case

## Scenario
A fictional audit screen shows a mixed-language status chip ("Pendente review") that reduces
scan clarity. The expectation is that `ux-writing` classifies, then rewrites for precision
while preserving the audit meaning.

## Why this expectation is correct
The source observation (`obs-2026-04-13-ux-writing-crisis-monitor-clarity`) found the existing
skill already provided the right lens — classify, rewrite for precision before elegance,
preserve semantic safety. This case captures that as a baseline expectation.

## How a reviewer checks it
The rewrite must be single-language, scannable, consequence-clear, and semantically identical
to the original audit state. Elegant-but-ambiguous copy, or any meaning shift, fails.
