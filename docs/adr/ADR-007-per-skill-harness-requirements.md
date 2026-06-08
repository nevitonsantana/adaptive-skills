# ADR 007 — Per-skill harness requirements (declarative layer)

| Field | Value |
|---|---|
| Status | Accepted |
| Date | 2026-06-08 |
| Author | Neviton Santana |
| Deciders | Neviton Santana |
| Related | ADR-003 (Relationship with AletheIA), ADR-006 (Knowledge-aware skills boundary), AletheIA ADR-013 (Agent Harness Contract), AletheIA ADR-011 (Agent Harness Governance Extension), AletheIA ADR-014 (Harness Enforcement Addendum reconciliation) |
| Supersedes | — |

## 1. Context

`docs/skill-harness-boundaries.md` already separates a *skill* (a procedure) from a *harness* (an
execution environment). But a skill had no structured way to state, up front, *what* envelope it
needs to run safely: which tools it expects, which it must not touch, the autonomy ceiling it should
run at, the gates that guard side effects, the evidence it must leave, and the minimum audit.

Without that, two failure modes recur: a consultative skill can be mistaken for one authorized to
act, and an operational skill can drift toward dangerous tools with no declared gate. The open
question: can a skill declare these requirements *without* turning into a policy or enforcement
mechanism, which would break portability and duplicate what the harness/runtime already owns?

The Agent Harness Enforcement Addendum (an external docs-first proposal) supplied a candidate
`harness_requirements` model. AletheIA already owns the enforcement side (ADR-011 AHGE, ADR-013 AHC).

## 2. Decision

1. **Add a per-skill `harness_requirements` declaration.** A skill may declare its operating envelope
   via a `harness_requirements` block: `autonomy` (floor/ceiling/rationale), `expected_tools`,
   `restricted_tools`, `approval_gates`, `required_evidence`, `escalation_triggers`,
   `audit_requirements`. Template: `templates/skill-harness-requirements.yaml`.
2. **Declaration only — never enforcement.** The declaration states intent. It does not execute,
   authorize, or block. Enforcement (verdicts, permission decisions, audit emission) belongs to the
   harness/runtime, and the contracts it enforces against live in AletheIA. Skills must never become
   policy engines or blocking mechanisms.
3. **This is per-skill and distinct from the per-task contract.** `harness_requirements` (per-skill)
   is upstream of, and does not merge with, `templates/agent-harness-contract.yaml` (per-task).
4. **Examples are external and synthetic.** Worked declarations live in
   `examples/harness-requirements/`, not coupled into `skills/*`, until there is evidence that
   coupling earns its cost.
5. **Autonomy vocabulary defers to AletheIA.** The autonomy enum mirrors AletheIA's canonical four
   levels (`observe`, `advise`, `act_with_approval`, `autonomous_within_bounds`). The external
   draft's `bounded_autonomous`/unbounded `autonomous` are not used (see AletheIA ADR-014).
6. **Structural validation, not policy validation.** `scripts/validate_harness_requirements.py`
   checks shape and vocabulary in CI. It validates the *declaration's structure*; it does not enforce
   the *policy* the declaration describes.
7. **`harness-readiness-check` stays a future candidate.** No new skill is created in this phase.

## 3. Consequences

**Positive**
- A reviewer can see, per skill, expected tools, gated actions, and required evidence.
- Consultative skills (e.g. `feature-value-governance`, `advise`/`advise`) no longer look authorized
  to act; operational skills carry minimum evidence and gates.
- The declaration projects cleanly onto AletheIA's richer enforcement vocabulary, keeping a path to
  policy-as-code without forcing it now.

**Negative / tradeoffs**
- A second harness-related artifact (per-skill vs per-task) is a small conceptual cost; mitigated by
  documenting the distinction in both the template and `docs/harness-requirements-for-skills.md`.
- Two risk vocabularies coexist (coarse 4-class here, authoritative 15-class in AletheIA); mitigated
  with an explicit mapping and a "the matrix wins" rule.
- The CI validator encodes the schema in code rather than a JSON Schema file, to avoid a new
  dependency and match the repo's existing hand-rolled validators.

## 4. Alternatives considered

- **Inline requirements into each `SKILL.md`.** Rejected: bloats skills, couples them to an
  environment concern, and risks auto-editing `SKILL.md`.
- **Let the per-task Agent Harness Contract carry everything.** Rejected: a per-task contract cannot
  express what a skill *generally* needs before any task exists.
- **Build a JSON Schema + `jsonschema` validation.** Deferred: adds a dependency for no gain over the
  repo's established hand-rolled validators; can be added later if the model stabilizes.
- **Create `harness-readiness-check` now.** Rejected: no evidence of recurrence yet.

## 5. Relationship

- Builds on `docs/skill-harness-boundaries.md` and ADR-006's skill/content boundary.
- Consumes AletheIA's enforcement contracts: ADR-011 (AHGE), ADR-013 (AHC), and the addendum docs
  (`autonomy-levels`, `tool-risk-taxonomy`, `policy-verdicts`, `agent-action-audit-record`).
- Vocabulary reconciliation is recorded in AletheIA ADR-014.

## 6. Review

Reopen if: a skill needs an autonomy ceiling above `act_with_approval` (revisit the schema invariant
for `autonomous_within_bounds`); coupling declarations into `skills/*` proves necessary; readiness
evaluation recurs across flows (then create `harness-readiness-check`); or AletheIA changes the
canonical autonomy/verdict/risk vocabulary this declaration projects onto.
