# Skill Quality Gate — lean-implementation

## Proposal

- **Proposal id:** `S22-lean-implementation`
- **Proposal type:** `new_skill`
- **Target skill(s):** `none`
- **Reviewer:** `catalog reviewer`
- **Source refs:** `AletheIA S22`, `P17-R3`, `Lean Skill Doctrine`

## 1. Necessity

- Recurring problem: after planning, agents often over-expand implementation, mix cleanup with delivery, or skip validation in the name of speed.
- Recurrence evidence: source-backed by the AletheIA backlog and S20/S22 Lean Skill Doctrine follow-up.
- What breaks without it: implementation work remains split across adjacent skills without one compact method for smallest safe change and handoff.
- Existing skills considered: `workflow`, `testing`, `debugging`, `refactoring`, `architecture-review`.

**Assessment:** `partial`

## 2. Distinctness

- Adjacent skills remain protected:
  - `workflow` frames work before execution.
  - `testing` calibrates proof.
  - `debugging` investigates observed failures.
  - `refactoring` improves structure without behavior change.
  - `architecture-review` evaluates consequential structure.
- `lean-implementation` owns the implementation slice after intent/scope are clear.

**Assessment:** `strong`

## 3. Proportionality

- Core Moves: five.
- Optional modules: three trigger-scoped modules.
- Sidecars: one quality-gate record and one synthetic example.
- No runtime, benchmark harness, router, or policy engine.

**Assessment:** `strong`

## 4. Context discipline

- Minimum context: confirmed task boundary, relevant existing pattern, validation target.
- On-demand context: architecture/security/accessibility/data review only when triggered.
- Excluded: local project state, secrets, proprietary source content, AletheIA authority claims.

**Assessment:** `strong`

## 5. Verification

- Observable output: smallest implemented change, validation evidence, gaps, handoff summary.
- Failure signals: broad opportunistic refactor, skipped proof, hidden safety exception, unclear handoff.
- Handoff signal: next reviewer can see what changed, why, proof, and gaps.

**Assessment:** `strong`

## 6. Governance boundary

- The skill declares implementation behavior; it does not approve, block, merge, deploy, close a Work Slice, or enforce runtime permissions.
- AletheIA remains responsible for macro-governance when used inside governed work.
- Harness/runtime remains responsible for tool authorization and records.

**Assessment:** `strong`

## 7. Decision

`accept_as_new_skill`

## Decision rationale

- S22 explicitly called for a bounded `lean-implementation` skill after S20 quality gates.
- The skill has a distinct dominant need: execute the smallest safe change after planning.
- Safety exceptions prevent “lean” from weakening validation or governance.
- Observation return supports AletheIA compatibility without importing AletheIA authority.

## Follow-up

- **Next action:** `implement`
- **Required validation:** `python3 scripts/validate_skills.py`, projection status, relevant repository validators
- **AletheIA governance link:** `S22 Lean Implementation Skill / P17-R3`
