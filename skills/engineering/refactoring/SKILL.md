---
name: refactoring
description: Improve structure and clarity incrementally while protecting behavior and rollback options.
version: 0.1.0
owner: adaptive-skills
---

# Overview

Use this skill when the code works but is too costly to reason about or change safely.

# When to Use

- structural cleanup
- duplication reduction
- local complexity reduction

# When NOT to Use

- urgent bug response without a stable repro
- large rewrites justified only by taste

# Core Moves

1. Name the reason for refactoring.
2. Define the behavior that must remain stable.
3. Choose the smallest safe sequence.
4. Validate after each meaningful step.

# Optional Modules

- **Extraction pass** — Pull out a smaller unit when a file or function does too much.
- **Naming pass** — Rename concepts once structure is clearer.
- **Rollback plan** — Clarify how to stop or revert if the cleanup becomes risky.

# Activation Triggers

- Use extraction when responsibilities are mixed.
- Use naming when the main confusion is semantic rather than structural.
- Use rollback planning when the refactor touches core paths.

# Expected Output

- clear refactoring objective
- incremental change set
- behavior-preservation evidence

# Verification

- The change removed complexity rather than moving it around.
- Behavior was checked after meaningful steps.
- The refactor stayed inside its declared boundary.

# Handoff Signals

- The cleanup exposes a larger architectural issue.
- The next safe step belongs to another owner or specialty.

# Pairs Well With

- `code-style`
- `testing`
- `architecture-review`

# Anti-patterns

- Calling a rewrite a refactor.
- Mixing cleanup and new behavior without saying so.
- Expanding scope because the codebase “needs it anyway.”
