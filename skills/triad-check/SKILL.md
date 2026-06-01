---
name: triad-check
description: Bring product, design, and technical perspectives together when a decision crosses boundaries or is hard to reverse.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: cross-functional
---

# Overview

Use this skill when the right next step depends on more than one functional lens and the work should not silently continue inside one specialty.

# When to Use

- cross-functional decisions
- hard-to-reverse changes
- ambiguous ownership

# When NOT to Use

- small single-domain tasks with obvious ownership

# Core Moves

1. Name the decision under review.
2. Assess it through product, design, and technical lenses. Force the value-vs-cost tension explicitly:
   - **Product** — What value/lever does this move, for which ICP, and what is the evidence?
   - **Design** — What experience cost or benefit, and where could it dilute the value proposition?
   - **Tech** — What *permanent* complexity does this add, and how reversible is it?
3. Identify the dominant conflict.
4. Choose the leading function and the next move.

# Optional Modules

- **Owner split** — Decide whether the work continues in one thread, several threads, or a handoff.
- **Risk tie-breaker** — Use reversibility and operational risk to resolve disagreement.
- **Decision note** — Capture the rationale when the triad materially changes the plan.
- **Permanent-cost tension** — When the three lenses disagree on whether the value is worth the forever-carry, surface it as a value-governance question and route to `feature-value-governance` rather than letting one function quietly win.

# Activation Triggers

- Use owner split when more than one function must act next.
- Use risk tie-breaker when the disagreement is about speed versus caution.
- Use decision note when the outcome affects future similar work.
- Use the permanent-cost tension module when the disagreement is really about whether the value justifies the permanent complexity.

# Expected Output

- dominant function
- conflict summary
- execution recommendation

# Verification

- All three lenses were actually considered.
- The chosen next step is operational, not purely descriptive.
- Ownership is clearer after the check than before it.

# Handoff Signals

- The next action belongs to a different function.
- The work must be split across functions with explicit boundaries.

# Pairs Well With

- `workflow`
- `feature-planning`
- `communication`

# Anti-patterns

- Using triad-check for every trivial choice.
- Ending with collective ambiguity instead of a next move.
- Collapsing three lenses into one opinion.
