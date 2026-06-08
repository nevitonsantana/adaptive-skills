# Templates

Reusable starting points for authoring skills, declaring knowledge dependencies, capsuling a framework, and reporting on pilots. This index says **what each template is** and **when to reach for it**.

## Quick chooser

| You are… | Use |
|---|---|
| writing an ordinary procedural skill | [`skill/SKILL.template.md`](skill/SKILL.template.md) |
| writing a skill that consumes governed knowledge | [`skill/SKILL.template.md`](skill/SKILL.template.md) **+** [`knowledge-aware-skill-template.md`](knowledge-aware-skill-template.md) (as a content guide) **+** [`skill-knowledge-dependency.yaml`](skill-knowledge-dependency.yaml) |
| capsuling a framework or knowledge source | [`framework-capsule-template.md`](framework-capsule-template.md) |
| reporting on a consumer or efficiency pilot | [`pilot/`](pilot/) |
| running an engineering skill on a real task | [engineering hardening templates](#engineering-hardening-templates) (feedback loop, behavior-first test, module depth, domain language) |

## The templates

### `skill/SKILL.template.md` — base skill scaffold

The canonical `SKILL.md` skeleton: the **11 required sections** in order (Overview, When to Use, When NOT to Use, Core Moves, Optional Modules, Activation Triggers, Expected Output, Verification, Handoff Signals, Pairs Well With, Anti-patterns) with the front-matter convention (`name`, `description`, `metadata: { version, owner, category }`).

Use it for **every** skill. This is the structure `scripts/validate_skills.py` enforces — section names outside this list fail validation.

### `knowledge-aware-skill-template.md` — content guide for knowledge-aware skills

A guide for skills that declare knowledge dependencies and run in generic / knowledge-aware modes. It shows the *content* a knowledge-aware skill must carry: the two-mode discipline, capsule-first reasoning, `pack_id@version` citations, and fallback behavior.

> **Important — this is a content guide, not a literal `SKILL.md`.** It includes illustrative headings (`Modes`, `Knowledge Dependencies`) that are **not** in the 11 required sections. Copying it verbatim into `skills/<name>/SKILL.md` will fail `validate_skills.py`.
>
> Instead, start from `skill/SKILL.template.md` (the 11 sections) and **fold** the knowledge-aware content into them:
> - put the two modes into **Overview** and **Core Moves**;
> - put the dependency summary into **Core Moves** / **Optional Modules**;
> - set `metadata.knowledge_aware: true`;
> - ship a sibling `skill-knowledge-dependency.yaml`.
>
> See `skills/feature-value-governance/` for a worked example.

### `skill-knowledge-dependency.yaml` — dependency manifest

The sibling file every knowledge-aware skill ships next to its `SKILL.md`. Declares knowledge **slot types** (never specific source ids), the `required` / `required_when` posture of each slot, `accepted_types`, and explicit `fallback_behavior` for all four cases. See [`../docs/declaring-knowledge-dependencies.md`](../docs/declaring-knowledge-dependencies.md).

### `framework-capsule-template.md` — framework capsule

For the **knowledge-pack side**, not the skill side. Produces the operational summary an agent reasons from when a framework is resolved. A capsule is *how to use* a framework, never a paraphrase of its body. Lives in the project / org that owns the framework, not in a skill. See [`../docs/using-proprietary-frameworks-safely.md`](../docs/using-proprietary-frameworks-safely.md).

### `pilot/` — pilot report templates

- `consumer-pilot-report.md` — for a consumer-adoption pilot.
- `efficiency-pilot-report.md` — for an Efficiency Layer trio pilot.

## Engineering hardening templates

Operational worksheets that pair with the engineering skills (see [`../docs/engineering-skills-hardening-pack.md`](../docs/engineering-skills-hardening-pack.md)). Unlike the scaffolds above, these are filled out *per task*, not per skill.

- [`feedback-loop-plan.md`](feedback-loop-plan.md) — pairs with `debugging` (Feedback loop construction): plan a fast, deterministic pass/fail signal before changing code.
- [`behavior-first-test-plan.md`](behavior-first-test-plan.md) — pairs with `testing` (Behavior-first test design / Vertical test slice): design a test around public behavior that survives refactoring.
- [`module-depth-review.md`](module-depth-review.md) — pairs with `architecture-review` (Module depth review): decide whether a module earns its interface or just relocates complexity.
- [`domain-language-alignment-record.md`](domain-language-alignment-record.md) — pairs with `domain-language-alignment`: record canonical, ambiguous, and conflicting terms before implementation.

## Harness templates

Fill-in worksheets for the **harness** envelope a skill runs inside (see [`../docs/skill-harness-boundaries.md`](../docs/skill-harness-boundaries.md) and AletheIA's Agent Harness Contract).

- [`agent-harness-contract.yaml`](agent-harness-contract.yaml) — the per-**task** operating envelope (autonomy, tools, gates, sensors, rollback, human review). Field names mirror the AletheIA schema.
- [`skill-harness-requirements.yaml`](skill-harness-requirements.yaml) — the per-**skill** declaration of what operating envelope a skill needs (autonomy floor/ceiling, expected/restricted tools, approval gates, required evidence, audit). A declaration, not enforcement — see [`../docs/harness-requirements-for-skills.md`](../docs/harness-requirements-for-skills.md). Worked examples in [`../examples/harness-requirements/`](../examples/harness-requirements/).
- [`aci-tool-guideline.md`](aci-tool-guideline.md) — document one tool against the Agent-Computer Interface design bar before listing it in a contract.
- [`context-rot-checkpoint.md`](context-rot-checkpoint.md) — checkpoint a long session to keep it reviewable and restartable.
- [`harness-trace-summary.md`](harness-trace-summary.md) — human-readable summary of what the agent did within its contract.

## See also

- [`../docs/skill-model.md`](../docs/skill-model.md) — the Core + Modules + Triggers skill model.
- [`../docs/skill-knowledge-boundaries.md`](../docs/skill-knowledge-boundaries.md) — what a skill carries vs. what a knowledge pack carries.
- [`../docs/declaring-knowledge-dependencies.md`](../docs/declaring-knowledge-dependencies.md) — author-facing guide to the dependency manifest.
