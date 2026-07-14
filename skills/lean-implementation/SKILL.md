---
name: lean-implementation
description: Implement the smallest safe change that satisfies a confirmed plan while preserving validation, boundaries, and handoff evidence.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: engineering
---

# Overview

Use this skill when the intent, scope, and validation target are already clear and the work is ready for a small implementation slice.

The skill keeps implementation lean without weakening safety. It helps the agent avoid broad rewrites, speculative abstractions, hidden policy choices, and unvalidated closure.

# When to Use

- a bounded plan or Work Slice is ready for implementation
- the task needs a small code/docs/config change with explicit validation
- the main risk is implementation sprawl, not problem discovery
- the user asks to proceed after planning and the next action is a concrete change

# When NOT to Use

- intent, expected behavior, or acceptance criteria are still ambiguous
- the work is primarily debugging; use `debugging`
- the work is primarily test strategy; use `testing`
- the work is primarily structural cleanup without behavior change; use `refactoring`
- architecture, security, accessibility, data integrity, or human approval decisions are unresolved

# Core Moves

1. Restate the smallest acceptable change and its explicit boundary.
2. Inspect the existing pattern before editing.
3. Make one coherent change without opportunistic refactors.
4. Run the minimum reliable validation and record gaps.
5. Handoff what changed, why, evidence, and the next safe step.

# Optional Modules

- **Contract change guard** — Use when the slice changes a public contract, schema, API, policy, or documented behavior. Confirm compatibility, migration notes, and source references before closure.
- **Safety exception escalation** — Use when the lean path would skip security, accessibility, data integrity, privacy, or human-review obligations. Stop and route to the appropriate review skill or governance surface.
- **Observation return** — Use when the work is part of AletheIA or another governed harness. Emit a compact result with selected skill, validation evidence, unavailable fields, and boundary notes.

# Activation Triggers

- Use contract change guard when another component, user, skill, harness, or document consumes the changed surface.
- Use safety exception escalation when being “lean” would remove validation, review, rollback, accessibility, security, privacy, or data-integrity evidence.
- Use observation return when the implementation should be visible as source-backed execution evidence in AletheIA, Resource Observatory, or a handoff record.

# Expected Output

- smallest implemented change
- files or surfaces changed
- validation run and result
- known gaps or unavailable evidence
- compact handoff / observation-compatible summary

# Verification

- The change matches the declared scope and does not add unrelated work.
- Existing local patterns were reused before introducing new structure.
- Validation evidence is proportional to risk and explicitly named.
- Safety, accessibility, security, data integrity, and human-review requirements were not weakened.
- Any unavailable evidence is marked `unavailable` rather than inferred.
- The handoff is sufficient for another reviewer to understand what changed and why.

# Handoff Signals

- Intent or acceptance criteria become unclear during implementation.
- The slice requires architecture, security, accessibility, data, or governance review.
- Validation cannot be run or cannot cover the main risk.
- The smallest safe change is larger than the original boundary.

# Pairs Well With

- `workflow`
- `testing`
- `debugging`
- `refactoring`
- `architecture-review`

# Anti-patterns

- Treating “lean” as permission to skip proof.
- Expanding a small slice into broad cleanup.
- Adding abstractions before reuse pressure exists.
- Mixing implementation with unresolved product or governance decisions.
- Claiming a skill can approve, block, close, merge, or deploy work.
