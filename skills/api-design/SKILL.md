---
name: api-design
description: Shape a contract so inputs, outputs, errors, names, and compatibility are clear and hard to misuse.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: engineering
---

# Overview

Use this skill to design or review interfaces between systems or modules with clarity and change-awareness.

# When to Use

- new endpoints or interfaces
- payload redesign
- public or semi-public contract changes

# When NOT to Use

- private local implementation details with no meaningful contract

# Core Moves

1. Name the contract responsibility.
2. Define inputs and outputs.
3. State failure semantics.
4. Review naming for real-world use.
5. Check compatibility cost for consumers.

# Optional Modules

- **Error taxonomy** — Expand failure classes when misuse or recovery matters.
- **Compatibility pass** — Map what breaks for current consumers.
- **Ownership note** — Clarify who owns the contract and its evolution.

# Activation Triggers

- Use the error taxonomy when clients need to react differently to failures.
- Use the compatibility pass when consumers already exist.
- Add ownership when many teams touch the contract.

# Expected Output

- contract statement
- input/output model
- error model
- compatibility note

# Verification

- The contract responsibility is singular.
- Consumers can understand success and failure clearly.
- Backwards-compatibility assumptions are explicit.

# Handoff Signals

- The contract needs product or policy review.
- The change requires coordinated rollout across teams.

# Pairs Well With

- `communication`
- `architecture-review`
- `testing`

# Anti-patterns

- Encoding ambiguity into flexible payloads.
- Changing a contract without naming compatibility cost.
- Optimizing for implementation convenience over consumer clarity.
