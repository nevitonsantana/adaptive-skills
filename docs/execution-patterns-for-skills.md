---
title: "Execution Patterns for Skills"
description: "Reference documentation for Execution Patterns for Skills in Adaptive Skills."
---

Execution patterns define **which shape of execution** a task runs in. They are selected by
AletheIA before any skill executes (see the AletheIA repo,
`docs/contracts/execution-pattern-selection.md`). Skills do not select patterns — they **declare
compatibility** with them.

## Three axes, not one

| Axis | Question | Declared in |
|---|---|---|
| **Execution pattern** | *which shape* — topology (single agent? fan-out? loop? tournament?) | AletheIA pattern selection; skills declare compatibility here |
| **Execution mode** | *how deep* — basic / extended / high-risk / multi-agent | [execution-modes.md](https://nevitonsantana.github.io/adaptive-skills/execution-modes/) |
| **Autonomy level** | *how much authority* — observe / advise / act_with_approval / autonomous_within_bounds | [harness-requirements-for-skills.md](https://nevitonsantana.github.io/adaptive-skills/harness-requirements-for-skills/) |

Choosing a pattern says nothing about depth or authority. A skill running as one unit of a
`fan_out_and_synthesize` stage still runs at its own mode and within its own autonomy envelope.

## The ten patterns

`manual_prompt`, `single_agent`, `classify_and_act`, `fan_out_and_synthesize`,
`adversarial_verification`, `generate_and_filter`, `tournament_compare`, `loop_until_done`,
`scheduled_stateful_loop`, `human_led_workflow`.

The library — what each is and when to use it — is owned by the AletheIA repo
(`docs/concepts/execution-pattern-library.md`). This repo does not restate it; it declares how
**skills** relate to it.

## What a skill declares

A skill ships a `skill_execution_patterns` declaration
([template](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/skill-execution-patterns.yaml)):

- **compatible_patterns** — patterns the skill can run in, each with conditions and the controls
  that pattern requires (e.g. `loop_until_done` only with an objective gate and `max_iterations`);
- **incompatible_patterns** — patterns the skill must not run in, with a rationale (e.g.
  feature judgment has no objective stop condition, so `loop_until_done` is out);
- **required_evidence_by_pattern** — what evidence each pattern demands from this skill;
- **escalation_triggers** — conditions that route the run back to AletheIA
  (`objective_gate_missing`, `touches_sensitive_area`, `judgment_required`, `recurring_failure`,
  `comprehension_debt_risk`);
- **audit_requirements** — what the run must log (skill id, pattern, controls, evidence refs).

## Skills declare, they do not enforce

A skill does not decide alone that it can run in any topology, and it does not execute policy.
The declaration is consumed upstream (AletheIA selects the pattern and verifies compatibility) and
enforced downstream (harness and enforcement apply limits). This mirrors how
[harness requirements](https://nevitonsantana.github.io/adaptive-skills/harness-requirements-for-skills/) work: declaration here, authority there.

## Related

- [pattern-compatibility-guidelines.md](https://nevitonsantana.github.io/adaptive-skills/pattern-compatibility-guidelines/) — how to fill the declaration
- [looping-models-for-skills.md](https://nevitonsantana.github.io/adaptive-skills/looping-models-for-skills/) — the two loop patterns from the skill side
- [skills-in-orchestrated-workflows.md](https://nevitonsantana.github.io/adaptive-skills/skills-in-orchestrated-workflows/) — being a stage in an orchestration
- [execution-modes.md](https://nevitonsantana.github.io/adaptive-skills/execution-modes/) — the depth axis
