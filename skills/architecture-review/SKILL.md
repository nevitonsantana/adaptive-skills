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

- **Complexity budget** — Estimate whether the added structure earns its cost.
- **Operational impact** — Check deployment, ownership, or observability consequences.
- **Future change test** — Imagine the next two likely changes and whether the design helps or hurts.

# Activation Triggers

- Use complexity budget when the proposal adds new layers or abstractions.
- Use operational impact when runtime behavior or ownership will change.
- Use future change test when the decision could become a template.

# Expected Output

- structural decision summary
- trade-off comparison
- recommendation with main risk

# Verification

- The boundary change is explicit.
- At least one simpler alternative was considered.
- Maintenance cost is visible, not implicit.

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
