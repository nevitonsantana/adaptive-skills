---
name: feature-planning
description: Turn a feature request into a small, testable delivery plan with scope, risks, slices, and proof.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: engineering
---

# Overview

Use this skill to convert product intent into an executable plan with a smallest useful slice, visible risks, and explicit success criteria.

# When to Use

- new feature work
- functional redesign with behavior changes
- work that needs staged delivery

# When NOT to Use

- tiny local changes with obvious scope
- tasks that still lack the basic problem framing
- the feature has **not yet been judged worth doing** — run `feature-value-governance` first; planning a feature that should be killed or parked is wasted work

# Core Moves

1. Name the problem and target outcome.
2. Define in-scope versus out-of-scope.
3. Choose the smallest useful slice.
4. Break the work into verifiable increments.
5. Declare the evidence needed to accept the first slice.

# Optional Modules

- **Specification clarification** — Mark unresolved questions with `[NEEDS CLARIFICATION]`, separate what/why from how, and ask only questions that would change the plan, proof, architecture, or readiness.
- **Dependencies map** — Capture external systems, contracts, or approvals when delivery is not fully local.
- **Risk review** — Name the main reversible and irreversible risks.
- **Metrics hook** — Add success indicators when the feature should change observable behavior.
- **Stakeholder alignment** — Record who needs to review or sign off when multiple functions are involved.
- **Traceability and anti-overengineering check** — Link requirement, decision, task, and acceptance evidence before implementation, then remove complexity that does not protect the first slice.
- **[Feature-worthiness check](modules/feature-worthiness.md)** — Before planning delivery, confirm the feature was judged worth doing (problem, ICP, lever, evidence, permanent cost). If it was not, stop and route to `feature-value-governance`.
- **[Revenue-lever fit](modules/revenue-lever-fit.md)** — Confirm the plan's first slice actually moves the declared revenue/value lever, not just adjacent activity.
- **Scope-boundaries (do-not-build)** — Make the non-build explicit: list what is deliberately *not* being built and the criterion that would change that, separating a real MVP from scope accumulation.

# Activation Triggers

- Use specification clarification when the request has ambiguity that could change scope, proof, technical direction, or readiness.
- Add the dependencies map when another system or team is involved.
- Run the risk review when the change is hard to reverse.
- Add metrics when the feature changes adoption, reliability, or decision quality.
- Use stakeholder alignment when the work crosses product, design, and engineering.
- Use traceability and anti-overengineering check when the plan starts producing many tasks, hidden implementation assumptions, or architecture before the first slice is stable.
- Use the feature-worthiness check at the start of any non-trivial plan; if worthiness is unproven, stop and route to `feature-value-governance`.
- Use revenue-lever fit when the plan risks optimizing activity that does not move the declared lever.
- Use scope-boundaries (do-not-build) when scope is creeping or stakeholders keep adding "while we're at it" asks.

# Expected Output

- problem statement
- goal and non-goals
- clarified what/why plus explicit how boundary
- unresolved questions marked with `[NEEDS CLARIFICATION]`
- smallest useful slice
- incremental plan
- requirement to decision to task to evidence trace, when needed
- acceptance evidence

# Verification

- The first slice is defensible on its own.
- Ambiguities that affect the plan are declared instead of silently resolved.
- The plan keeps what/why separate from how until the implementation boundary is explicit.
- Each slice has a clear acceptance condition.
- Main dependencies and risks are visible.
- Tasks can be traced back to a requirement, decision, and acceptance evidence when traceability is needed.
- The plan does not smuggle in hidden scope.
- The plan does not add architecture, automation, or process that is unnecessary for the smallest useful slice.

# Handoff Signals

- A new contract or domain boundary appears.
- A `[NEEDS CLARIFICATION]` item blocks the plan, proof, or readiness decision.
- The work requires a specialized review before implementation.
- The rollout depends on another team or operating system.

# Pairs Well With

- `workflow`
- `testing`
- `architecture-review`
- `premortem`

# Anti-patterns

- Using planning as a way to hide oversized scope.
- Listing phases without a smallest useful slice.
- Leaving proof implicit until the end.
- Treating unresolved ambiguity as permission to invent requirements.
- Turning every feature into a heavyweight specification ceremony.
