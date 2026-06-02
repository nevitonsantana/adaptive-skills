---
name: testing
description: Choose the minimum reliable proof for a change based on risk, reversibility, and impact.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: engineering
---

# Overview

Use this skill to calibrate validation. It keeps teams away from both careless closure and ritualized over-testing.

# When to Use

- before closing meaningful work
- when fixing a bug
- when changing behavior or a contract

# When NOT to Use

- as a generic ceremony disconnected from risk
- to demand exhaustive proof for tiny reversible changes

# Core Moves

1. Name what could break.
2. Choose the minimum reliable proof.
3. Run the main-path smoke when relevant.
4. Record what was actually validated.

# Optional Modules

- **Regression sweep** — Check the most likely adjacent failures when the change is broad.
- **Automation check** — Decide whether the change deserves a lasting automated test.
- **Rollback check** — Clarify how the change can be reversed if the proof is inconclusive.
- **Behavior-first test design** — Design tests around public behavior and stable interfaces, not private implementation details. A passing test should describe a capability the system provides, and should survive internal refactoring when behavior is unchanged.
- **Vertical test slice** — Work in one behavior-sized cycle at a time instead of writing tests horizontally in bulk: define the expected behavior, create the smallest failing proof, implement the smallest passing change, then refactor.

# Activation Triggers

- Use the regression sweep when multiple surfaces share the same dependency.
- Use the automation check when the bug or rule is likely to return.
- Use the rollback check when failure cost is material.
- Use behavior-first test design when a test risks coupling to private methods, incidental data shape, or internal collaborator calls.
- Use the vertical test slice when the work tempts you to write many tests at once instead of one behavior per cycle.

# Expected Output

- proof strategy
- executed evidence
- known validation gaps

# Verification

- The proof matches the risk.
- The main path or failure path was checked intentionally.
- Unvalidated areas are explicit rather than hidden.
- The test can survive internal refactoring as long as behavior stays the same.
- The test fails for the intended behavior gap, not for an incidental detail.
- The test does not rely on private method names, incidental data shape, or internal collaborator calls unless that coupling is explicitly justified.

# Handoff Signals

- A specialist needs to validate a different layer.
- The available proof is not enough for the current risk level.

# Pairs Well With

- `workflow`
- `debugging`
- `refactoring`

# Anti-patterns

- Closing work with no evidence.
- Confusing activity with validation.
- Using “manual tested” as a content-free stamp.
