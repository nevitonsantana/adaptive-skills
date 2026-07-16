# Skills in Orchestrated Workflows

When the selected execution vehicle is an orchestrated workflow, a skill runs as a **stage** in an
orchestration contract (owned by the AletheIA repo, `docs/contracts/orchestration-contract.md`).
This page covers what participating as a stage requires from the skill. It does not restate the
orchestration contract — stages, routing, scoring, filtering, rerun, budget, and safety are
declared there.

## What a stage receives and owes

Each stage in an orchestration contract declares, among other fields: `input`, `output`,
`skill_used`, `gate`, and `evidence_required`. From the skill side that means:

- **Declared input** — the skill consumes only the stage input it declared; it does not reach into
  other stages' context (knowledge boundaries still apply, see
  [skill-knowledge-boundaries.md](skill-knowledge-boundaries.md));
- **Declared output** — the stage output is a contract: the next stage (or the synthesis) depends
  on its shape, so the skill must produce it even on partial failure (with failure marked);
- **Gate before handoff** — the stage gate verifies the output before it flows downstream;
- **Evidence** — whatever `evidence_required` lists must be attached, per the skill's
  `required_evidence_by_pattern` declaration.

A participation template is available:
[orchestration-step-requirements.yaml](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/orchestration-step-requirements.yaml).

## Escalation and handoff

A stage does not improvise when its assumptions break. The skill's `escalation_triggers`
(`objective_gate_missing`, `touches_sensitive_area`, `judgment_required`, `recurring_failure`,
`comprehension_debt_risk`) route the run back to the orchestration owner — pausing the stage, not
silently degrading it. Handoff between stages follows the same discipline as
[handoff-summary](https://github.com/nevitonsantana/adaptive-skills/blob/main/skills/handoff-summary/SKILL.md)-style compact handoffs: the next stage gets
the declared output plus evidence refs, not a transcript.

## Maker-checker inside orchestrations

When the orchestration includes an `adversarial_verification` stage, the checker stage must not be
executed by the same agent profile that produced the work (self-preferential bias), and a checker
agent is never the only gate on a critical task — see the AletheIA repo,
`docs/contracts/maker-checker-policy.md`. From the skill side: a skill compatible with
`adversarial_verification` declares whether it can act as maker, checker, or both, in its
compatibility conditions.

## Volume and comprehension debt

Fan-out, generate-and-filter, and tournament stages produce volume. Stage participation therefore
includes audit duties: log skill id, pattern, controls, and evidence refs, so the orchestration's
comprehension-debt review (who reads all this output?) has something to review.

## Related

- [execution-patterns-for-skills.md](execution-patterns-for-skills.md) — the pattern axis and what skills declare
- [pattern-compatibility-guidelines.md](pattern-compatibility-guidelines.md) — filling the declaration
- [harness-requirements-for-skills.md](harness-requirements-for-skills.md) — the authority envelope each stage still runs within
