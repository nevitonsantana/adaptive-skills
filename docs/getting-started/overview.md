# Adaptive Skills — Overview

Adaptive Skills is a portable **capability library**: a collection of small, reusable micro-skills for AI-assisted work. Each skill defines exactly when to use it, what to do, and what a good output looks like — so agents and teams can execute with discipline instead of improvisation.

---

## The problem it solves

AI-assisted work tends to fail in predictable ways:

- The agent picks the wrong mode for the problem — debugging when it should be planning, or reviewing when it should be executing.
- Risks and assumptions stay implicit until they surface as failures.
- Useful patterns from one session disappear after the thread ends.
- Generic prompts absorb project-specific rules, making them unmaintainable.
- Teams cannot tell whether a given output was systematic or improvised.

Adaptive Skills turns repeated work patterns into small, inspectable assets. Instead of one large prompt or a vague instruction like "be strategic", you invoke the smallest skill that fits the dominant need — and it brings structure without bureaucracy.

---

## What a skill is

Every skill in the library defines:

| Element | What it answers |
|---|---|
| **When to use** | What signal says this skill is the right fit |
| **When NOT to use** | What this skill should not replace |
| **Core moves** | The few actions that should almost always happen |
| **Optional modules** | Add-ons that activate only when the context needs them |
| **Verification** | What a good output looks like |
| **Handoff signals** | When and how to pass work forward |

Skills are designed to be read and invoked directly — paste the skill into a session, reference it by name in an agent context, or install it via APM so your harness loads it automatically.

---

## What Adaptive Skills is not

- **Not an operating overlay.** Adaptive Skills provides capabilities — it does not legislate how a project decides, validates, or reports. That is AletheIA's responsibility.
- **Not an agent runtime.** The library ships SKILL.md files, not a process runner or session manager.
- **Not a squad bundle.** Skills are individual capabilities; the library does not configure a pre-built squad the way BMAD or SDD do.

See [`docs/adr/ADR-001-adaptive-skills-as-capability-library.md`](../adr/ADR-001-adaptive-skills-as-capability-library.md) for the formal definition.

---

## Practical daily benefits

| Without Adaptive Skills | With Adaptive Skills |
|---|---|
| Agent improvises the approach for each task | Invoke the right skill for the dominant need |
| Risks assumed away without visibility | `premortem` surfaces failure modes before execution starts |
| Session ends, all operating context is lost | `handoff-summary` packages state explicitly |
| Long sessions drift — wrong decisions compound | `checkpoint-review` inserts deliberate pauses |
| Cross-functional decisions collapse into one lens | `triad-check` surfaces product, design, and technical perspectives |
| Validation is informal — "looks right" | `testing` and `qa-review` calibrate the right level of proof |

---

## Current library (24 skills, 9 domains)

| Domain | Skills |
|---|---|
| Engineering | `workflow`, `feature-planning`, `testing`, `debugging`, `api-design`, `refactoring`, `architecture-review`, `code-style`, `communication` |
| Design | `ux-strategy`, `ux-provocation`, `heuristic-audit`, `ux-writing` |
| Planning | `premortem` |
| Efficiency | `task-chunking`, `checkpoint-review`, `handoff-summary` |
| Cross-functional | `triad-check` |
| Business | `business-design` |
| Quality | `qa-review` |
| Metrics | `observability-review` |

Full breakdown with trigger signals and composite flows: [`skill-catalog.md`](skill-catalog.md).

---

## Use with or without AletheIA

**Without AletheIA:** Adaptive Skills works standalone. Install via APM and invoke skills in any Claude Code, Codex, or conformant harness session. You get reusable, consistent execution discipline.

**With AletheIA:** AletheIA governs the work loop (scope, gates, handoffs, learnings); Adaptive Skills provides the specialist capabilities inside that loop. Together:

```
AletheIA decides the flow → Adaptive Skills shapes what gets done
```

See [`docs/aletheia-integration.md`](../aletheia-integration.md) for the combined setup.

---

## Telemetry and observability

Adaptive Skills includes a lightweight telemetry model so you can tell whether skills are being used, which ones generate friction, and which outputs are worth promoting to the evolution layer.

Three signals to watch:

1. **Invocation frequency** — which skills get called most often? Frequently-invoked skills are candidates for evolution.
2. **Module activation rate** — which optional modules get activated? High rates suggest a module should move into core.
3. **Handoff quality** — does the output of a skill give the next operator enough to start without re-deriving context?

You do not need instrumentation to track these — a simple evolution observation (see `evolution/observations/`) captures enough signal for the governed evolution loop.

Full model: [`docs/telemetry.md`](../telemetry.md).

---

## Risks and cautions

**Skills are not roles.** Do not assign a skill to an agent as if it were a persona. Invoke a skill for a task, then let the agent return to its default operating mode.

**Do not force a skill that does not fit.** Every skill has an explicit "When NOT to use" section. A weak fit produces a worse output than no skill at all.

**The library does not self-edit.** Changes to skills go through the evolution loop (observation → proposal → review). If you modify a skill locally, that change is not reflected upstream. Keep local adaptations in `ops/ai/skills/` in your consumer project, not inside the installed skill files.

**Domain packs are case studies, not canonical skills.** `domain-packs/crisis-management/` is field evidence from the first validation case. It is useful as a reference, but it is not the generic capability layer. See [`docs/adr/ADR-002-domain-agnosticism.md`](../adr/ADR-002-domain-agnosticism.md).

---

## Next steps

- Install the library: [`installation-guide.md`](installation-guide.md)
- Browse all skills with trigger signals and composite flows: [`skill-catalog.md`](skill-catalog.md)
- Questions? [`faq.md`](faq.md)
- Deep dive: [`docs/how-to-use-a-skill.md`](../how-to-use-a-skill.md), [`docs/skill-model.md`](../skill-model.md)
