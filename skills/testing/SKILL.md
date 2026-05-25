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

# Activation Triggers

- Use the regression sweep when multiple surfaces share the same dependency.
- Use the automation check when the bug or rule is likely to return.
- Use the rollback check when failure cost is material.

# Expected Output

- proof strategy
- executed evidence
- known validation gaps

# Verification

- The proof matches the risk.
- The main path or failure path was checked intentionally.
- Unvalidated areas are explicit rather than hidden.

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
