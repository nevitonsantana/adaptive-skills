# Pattern Compatibility Guidelines

How to fill a `skill_execution_patterns` declaration
([template](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/skill-execution-patterns.yaml)). The governing rule: **a skill does not
decide alone that it can run in any topology.** It declares compatible and incompatible patterns;
AletheIA selects, the harness enforces.

## Filling `compatible_patterns`

For each pattern the skill supports:

- **conditions** — when the compatibility holds, stated concretely. "Only when tests or repro
  commands provide an objective stop condition" is a condition; "when appropriate" is not.
- **required_controls** — the controls that make the pattern safe for this skill
  (`objective_gate_required`, `max_iterations`, `maker_checker_required`,
  `human_review_before_merge`, `explicit_filter_criteria`, `audit_record_required`, …). If a
  control cannot be named, the pattern is not actually compatible.

Default posture is conservative: a new skill starts with `single_agent` and `classify_and_act`
compatibility and earns loop or tournament compatibility with evidence, not optimism.

## Filling `incompatible_patterns`

Incompatibility must carry a **rationale**, because it is the negative space reviewers rely on.
The two recurring rationales:

- **No objective stop condition** — judgment work (feature value, strategy, design critique) can
  not loop until done, because "done" is not verifiable;
- **Governance risk from recurrence** — a `scheduled_stateful_loop` that automates a judgment
  (e.g. recurring roadmap actions) concentrates decisions nobody reviews.

Leaving a pattern unlisted is not the same as declaring it incompatible: unlisted means
"not evaluated", and AletheIA treats it as incompatible until declared.

## Filling `required_evidence_by_pattern`

Each declared pattern names the evidence the skill must produce in that topology (e.g.
`loop_until_done` for debugging requires the failing test, the passing run, and the iteration
count). Evidence names should reuse the skill's existing `required_evidence` vocabulary from its
[harness requirements](harness-requirements-for-skills.md) where they overlap.

## Escalation triggers

The canonical set: `objective_gate_missing`, `touches_sensitive_area`, `judgment_required`,
`recurring_failure`, `comprehension_debt_risk`. Add skill-specific triggers when needed, but never
remove `objective_gate_missing` from a skill that declares any loop compatibility.

## Review checklist

- [ ] every compatible pattern has concrete conditions and at least one required control
- [ ] every incompatible pattern has a rationale
- [ ] loop compatibility (if any) names an objective gate and a bound (`max_iterations` or budget)
- [ ] evidence vocabulary consistent with the skill's harness requirements
- [ ] audit block logs skill id, pattern, controls, evidence refs

## Related

- [execution-patterns-for-skills.md](execution-patterns-for-skills.md)
- [looping-models-for-skills.md](looping-models-for-skills.md)
- worked declarations: [debugging](https://github.com/nevitonsantana/adaptive-skills/blob/main/examples/execution-patterns/debugging-patterns.yaml),
  [feature-value-governance](https://github.com/nevitonsantana/adaptive-skills/blob/main/examples/execution-patterns/feature-value-governance-patterns.yaml),
  [testing](https://github.com/nevitonsantana/adaptive-skills/blob/main/examples/execution-patterns/testing-patterns.yaml)
