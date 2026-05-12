# Role-to-Skill Consumption Example

## Goal

Show how a consumer can keep the same AletheIA mental stack across runtimes while letting Adaptive Skills handle the micro execution support.

---

## Scenario

A small feature slice needs:

- framing
- bounded implementation
- semantic review before closure

The team wants continuity between Codex and Claude Code without redefining the work every time the runtime changes.

---

## Step 1 — Orchestrator frames the slice

**Role:** `orchestrator`

Recommended skill support:

- `workflow`
- `feature-planning`

Why:

- `workflow` helps create a clean operational frame
- `feature-planning` helps shape the smallest useful slice

Output:

- goal
- bounded scope
- validation expectation
- next boundary = `implementer`

---

## Step 2 — Implementer executes the bounded change

**Role:** `implementer`

Recommended skill support:

- `testing`
- `debugging`

Optional additional support when contracts matter:

- `api-design`

Why:

- `testing` keeps closure tied to proof
- `debugging` helps diagnose failures without guesswork
- `api-design` helps if the change touches a contract edge

Output:

- bounded implementation
- explicit note about what was validated
- remaining proof gap if closure is not ready yet

---

## Step 3 — Reviewer checks whether the slice is semantically healthy

**Role:** `reviewer`

Recommended skill support:

- `architecture-review`
- `communication`

Optional additional support:

- `testing` when the review needs to challenge weak proof design

Why:

- `architecture-review` pressures structural drift and hidden coupling
- `communication` makes the critique legible for the next boundary

Output:

- explicit concern or approval posture
- recommended next step
- preserved closure expectation

---

## Cross-runtime continuity

This same flow can happen across two runtimes.

Example:

- Codex runs the `implementer` boundary using `testing` + `debugging`
- Claude Code later runs the `reviewer` boundary using `architecture-review` + `communication`

What stays stable:

- role meaning
- skill meaning
- proof expectation

What changes:

- local runtime mechanics
- projection mode
- how the consumer loads or invokes the skill

---

## Why this example matters

This is the healthy macro/micro split:

- AletheIA defines the role and boundary meaning
- Adaptive Skills supplies the micro execution support
- the consumer project controls the runtime-specific projection

No layer has to pretend to be the others.
