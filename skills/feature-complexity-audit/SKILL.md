---
name: feature-complexity-audit
description: Estimate the permanent cost of a feature — cognitive, technical, operational, and governance carry — before the build commitment, producing a complexity scorecard and a reduction recommendation.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: governance
  knowledge_aware: true
---

# Overview

Use this skill to make the **permanent cost** of a feature visible *before* committing to
build. A feature is a bet that consumes complexity forever; this skill estimates that
carry across cognitive, technical, operational, and governance dimensions, and recommends
the cheapest coherent way to get the value. It produces a coarse, honest scorecard — never
a false-precision number.

# When to Use

- A feature looks valuable and complexity is becoming the deciding factor.
- Before a `build_now` verdict on anything non-trivial.
- When comparing two designs that deliver similar value at different carry.

# When NOT to Use

- The change is tiny, local, and obviously cheap.
- Value itself is unresolved (resolve the lever first).
- No scope or dependencies are known yet (nothing to estimate).

# Core Moves

1. **Frame.** State the feature and the scope being costed.
2. **Score four dimensions** (each low/medium/high with drivers):
   - **Cognitive** — surface users and the team must hold in their heads.
   - **Technical** — new dependencies, data model, integration, migration surface.
   - **Operational** — support, on-call, runbook, monitoring carry.
   - **Governance** — security, privacy, compliance, accessibility obligations.
3. **Name reversibility.** reversible / partially_reversible / one_way_door, and the
   mechanisms (flag, cohort, rollback, sunset, migration plan).
4. **Roll up to a coarse level** (low/medium/high) with the dominant driver named.
5. **Recommend reduction.** The smallest scope that keeps the value, or the explicit
   exception required if the high cost is accepted.

# Optional Modules

- **Carry-over forecast** — Estimate the ongoing yearly cost (support tickets, on-call,
  doc upkeep), not just the build cost.
- **Reduction options** — List 1–3 concrete ways to cut permanent cost without killing
  the value.
- **One-way-door check** — When reversibility is low, force a technical gate before commit.

# Activation Triggers

- Run whenever complexity is the pivotal factor in a worth-doing verdict.
- Use the one-way-door check when reversibility is `one_way_door`.
- Use reduction options whenever the rolled-up level is `high`.

# Inputs (minimum)

- Feature, scope, dependencies, UX impacted, operational footprint.

# Outputs (minimum)

- A permanent-cost score, risks, and a reduction recommendation — mapping to the
  `complexity_cost` and `reversibility` fields of the
  [Feature Value Governance Contract](../../../aletheia/schemas/feature-value-governance-contract.schema.json).
  A `high` level under a `build_now` verdict requires `decision.exception_approval`.

# Expected Output

```yaml
complexity_scorecard:
  feature: <one line>
  dimensions:
    cognitive: { level: low|medium|high, drivers: <text> }
    technical: { level: low|medium|high, drivers: <text> }
    operational: { level: low|medium|high, drivers: <text> }
    governance: { level: low|medium|high, drivers: <text> }
  reversibility:
    level: reversible | partially_reversible | one_way_door
    mechanisms: [ ... ]
  rolled_up_level: low | medium | high
  dominant_driver: <text>
  reduction_recommendation: <smallest scope that keeps value, or required exception>
  uncertainty: <what is hard to estimate>
```

# Verification

- All four dimensions are scored, not just the technical one.
- Reversibility is explicit.
- The recommendation reduces cost or names the exception — it does not hand-wave.
- The level is coarse and honest, not a fake decimal.

# Handoff Signals

- A `high` level under a build verdict → require `exception_approval` and route to human review.
- The feature should perhaps not be built at all → `feature-value-governance`.
- Structural design is the real question → `architecture-review`.

# Pairs Well With

- `feature-value-governance`
- `architecture-review`
- `premortem`

# Anti-patterns

- Scoring only build effort and ignoring forever-carry.
- A precise-looking number that hides deep uncertainty.
- Treating high complexity as an automatic veto, or as no cost at all.
