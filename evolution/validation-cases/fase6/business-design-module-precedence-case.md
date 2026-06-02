---
id: vc-business-design-module-precedence-001
skill_id: business-design
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Structure a fictional strategy note for a new retention play that rests on a single early interview and also touches pricing.
  context: The evidence is weak (assumption-map territory) and the work touches monetization (leverage-scan territory). It is unclear which optional module to apply first.
expected_behavior:
  must_do:
    - Separate facts, interpretations, hypotheses, and implications.
    - Surface the carrying assumptions before trusting the strategy.
    - Make the order of reasoning legible when both assumption-map and leverage-scan seem to apply.
  must_not_do:
    - Treat the single interview as strategic clarity.
    - Hide assumptions behind polished language.
    - Apply the value-layer lens / pluggable framework (out of scope for this case).
acceptance_criteria:
  - Assumptions are mapped before leverage is scanned when evidence is weak.
  - Facts and speculation are visibly separated and a decision is changed or protected.
failure_signals:
  - Leverage is scanned on top of unexamined weak assumptions.
  - The note reads as polished prose with no decision consequence.
related_observations:
  - obs-2026-06-01-business-design-assumption-leverage-trigger
notes: Synthetic. Deliberately avoids the value-layer lens so no proprietary framework / pack content is involved.
---

# Validation Case

## Scenario
A fictional retention strategy rests on one early interview and also touches pricing. Both the
assumption-map and leverage-scan modules seem to apply, and the order is ambiguous.

## Why this expectation is correct
The skill's Verification requires visibly separated evidence and a decision consequence, and
its anti-patterns warn against treating research volume as clarity. When evidence is weak,
mapping assumptions before scanning leverage is the sound order — but the current triggers do
not make that precedence explicit.

## How a reviewer checks it
Assumptions are mapped first, facts vs. speculation are separated, and a real decision is
changed or protected. Scanning leverage over unexamined assumptions, or decision-free prose,
fails the case. The value-layer lens must not be invoked here.
