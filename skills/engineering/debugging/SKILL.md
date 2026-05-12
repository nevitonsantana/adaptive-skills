---
name: debugging
description: Reproduce, isolate, fix, and guard against recurrence instead of patching symptoms by instinct.
version: 0.1.0
owner: adaptive-skills
---

# Overview

Use this skill when behavior is wrong and you need disciplined diagnosis rather than guesswork.

# When to Use

- runtime bugs
- failing tests
- inconsistent or surprising behavior

# When NOT to Use

- when the issue has not been observed
- when the work is actually a redesign request

# Core Moves

1. Make the failure observable.
2. Reduce the search area.
3. Form and test a plausible cause.
4. Fix the cause, not only the symptom.
5. Run proof against recurrence.

# Optional Modules

- **Instrumentation pass** — Add temporary logs or visibility when the failure is opaque.
- **Boundary check** — Inspect upstream and downstream assumptions when the issue crosses layers.
- **Recurrence guard** — Add a focused automated or procedural guard after the fix.

# Activation Triggers

- Use instrumentation when you cannot see the failure shape clearly.
- Use the boundary check when multiple systems may be contributing.
- Use the recurrence guard when the bug was expensive or likely to repeat.

# Expected Output

- repro path
- likely root cause
- validated fix
- recurrence guard or rationale for skipping one

# Verification

- The original failure is reproducible or otherwise evidenced.
- The fix changes the cause, not only the visible outcome.
- The validation exercises the failure path.

# Handoff Signals

- The issue moves outside the current technical boundary.
- A domain expert is needed to interpret the failure safely.

# Pairs Well With

- `testing`
- `code-style`

# Anti-patterns

- Changing multiple things before isolating the bug.
- Calling a symptom a root cause.
- Stopping after the error disappears once.
