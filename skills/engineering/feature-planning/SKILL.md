---
name: feature-planning
description: Turn a feature request into a small, testable delivery plan with scope, risks, slices, and proof.
version: 0.1.0
owner: adaptive-skills
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

# Core Moves

1. Name the problem and target outcome.
2. Define in-scope versus out-of-scope.
3. Choose the smallest useful slice.
4. Break the work into verifiable increments.
5. Declare the evidence needed to accept the first slice.

# Optional Modules

- **Dependencies map** — Capture external systems, contracts, or approvals when delivery is not fully local.
- **Risk review** — Name the main reversible and irreversible risks.
- **Metrics hook** — Add success indicators when the feature should change observable behavior.
- **Stakeholder alignment** — Record who needs to review or sign off when multiple functions are involved.

# Activation Triggers

- Add the dependencies map when another system or team is involved.
- Run the risk review when the change is hard to reverse.
- Add metrics when the feature changes adoption, reliability, or decision quality.
- Use stakeholder alignment when the work crosses product, design, and engineering.

# Expected Output

- problem statement
- goal and non-goals
- smallest useful slice
- incremental plan
- acceptance evidence

# Verification

- The first slice is defensible on its own.
- Each slice has a clear acceptance condition.
- Main dependencies and risks are visible.
- The plan does not smuggle in hidden scope.

# Handoff Signals

- A new contract or domain boundary appears.
- The work requires a specialized review before implementation.
- The rollout depends on another team or operating system.

# Pairs Well With

- `workflow`
- `testing`
- `architecture-review`

# Anti-patterns

- Using planning as a way to hide oversized scope.
- Listing phases without a smallest useful slice.
- Leaving proof implicit until the end.
