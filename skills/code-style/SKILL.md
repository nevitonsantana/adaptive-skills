---
name: code-style
description: Keep code readable, cohesive, and easy to change without turning style into dogma.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: engineering
---

# Overview

Use this skill to improve the reading experience of code: naming, cohesion, file focus, and everyday maintainability.

# When to Use

- writing new code
- reviewing existing code
- small focused cleanup

# When NOT to Use

- as a substitute for architecture or testing
- to justify broad rewrites with no value proof

# Core Moves

1. Protect the intended behavior.
2. Prefer the smallest clear design.
3. Check names and reading flow.
4. Keep files and functions focused.

# Optional Modules

- **Consistency pass** — Align with established local conventions when they are sensible.
- **Debt note** — Name the most important leftover debt without opening unrelated work.
- **Extraction hint** — Suggest a follow-up refactor if cohesion is still weak after the local fix.

# Activation Triggers

- Use consistency pass when the repository already has a strong local convention.
- Add a debt note when you deliberately leave an issue behind.
- Use extraction hint when the file stays overloaded after the current change.

# Expected Output

- clearer code
- better names
- more focused structure

# Verification

- The code reads in the same order that it executes conceptually.
- Naming reflects intent rather than implementation trivia.
- The file did not become a dumping ground.

# Handoff Signals

- The file-level problem is really architectural.
- The change now requires a broader cleanup outside the current scope.

# Pairs Well With

- `refactoring`
- `testing`
- `workflow`

# Anti-patterns

- Arguing style without user or maintenance impact.
- Adding cleverness that shortens code but hurts readability.
- Hiding design problems behind formatting.
