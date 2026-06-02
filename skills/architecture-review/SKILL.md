---
name: architecture-review
description: Review boundaries, coupling, complexity, and maintenance cost before consolidating a structural decision.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: engineering
---

# Overview

Use this skill to pressure test structural choices before they quietly become long-term architecture.

# When to Use

- new cross-module design
- new dependency or adapter
- structural refactor

# When NOT to Use

- purely local stylistic changes
- problems that still need basic framing first

# Core Moves

1. State the structural decision.
2. Identify boundaries and dependencies.
3. Compare with a simpler alternative.
4. Name the dominant maintenance risk.
5. Recommend proceed, reduce, or escalate.

# Optional Modules

- **Complexity budget** — Estimate whether the added structure earns its cost. For a feature, make the **permanent cost** and **reversibility** explicit (`reversible` / `partially_reversible` / `one_way_door`, with mechanisms like flag, cohort, rollback, migration plan). Delegate to `feature-complexity-audit` for the full four-dimension scorecard; a `one_way_door` requires a technical gate, and a `high` cost approved to build requires a recorded `exception_approval` on the [Feature Value Governance Contract](../../../aletheia/schemas/feature-value-governance-contract.schema.json).
- **Operational impact** — Check deployment, ownership, or observability consequences.
- **Future change test** — Imagine the next two likely changes and whether the design helps or hurts.
- **Module depth review** — Evaluate whether a module provides leverage through a smaller interface or merely moves complexity behind a new name. A deep module hides real implementation complexity behind a simple interface; a shallow one just relocates it. Assess interface size versus behavior hidden, a deletion test (what complexity returns if the module is removed), locality (are changes concentrated or scattered), adapter reality (is the seam real or hypothetical), and test surface (is the interface a good place to verify behavior).

# Activation Triggers

- Use complexity budget when the proposal adds new layers or abstractions; make reversibility explicit and route high/irreversible cost to a technical gate or `exception_approval`.
- Use operational impact when runtime behavior or ownership will change.
- Use future change test when the decision could become a template.
- Use module depth review when an abstraction is introduced primarily for naming or layering rather than for proven leverage.

# Expected Output

- structural decision summary
- trade-off comparison
- recommendation with main risk

# Verification

- The boundary change is explicit.
- At least one simpler alternative was considered.
- Maintenance cost is visible, not implicit.
- For any new module, interface size is weighed against the behavior hidden behind it.
- A deletion test was run: the complexity that returns if the module is removed is named.
- The seam is real, not hypothetical, and the interface is a usable place to verify behavior.

# Handoff Signals

- The proposal needs product, security, or platform review.
- The chosen option affects ownership beyond the current team.

# Pairs Well With

- `feature-planning`
- `api-design`
- `triad-check`

# Anti-patterns

- Treating abstraction as proof of quality.
- Skipping alternatives because the first idea works.
- Focusing on elegance without naming operational cost.
