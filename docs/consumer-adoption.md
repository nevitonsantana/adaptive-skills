---
title: "Consumer Adoption Guide"
description: "Reference documentation for Consumer Adoption Guide in Adaptive Skills."
---

## What this repository gives you

Adaptive Skills gives you a reusable micro-skill library for making AI-assisted work less improvised.
It does **not** try to replace your project's local operating system.

Use this repository when you want:
- specialist execution patterns
- clearer outputs
- better handoffs between roles or agents
- a reusable skill canon that can travel across projects
- a practical way to choose the right capability before asking an agent to act

Keep local to your project:
- ownership rules
- review gates
- release controls
- security or compliance policy
- project-specific vocabulary and domain truth

## Recommended adoption order

### 1. Learn the skill loop

Before installing many skills, read `docs/how-to-use-a-skill.md`.

The basic loop is:
1. choose the smallest skill that fits the task
2. run the core moves
3. activate only the modules that match the context
4. produce the expected output
5. verify the result before treating the task as done

### 2. Start with a small generic set

For a first consumer project, start with three engineering skills:
- `workflow`
- `feature-planning`
- `testing`

That combination is enough to improve framing, execution planning, and minimum proof without introducing too much process.

Add `premortem` when the plan has meaningful cost of failure and can still be changed before execution.

### 3. Add one domain or specialist lane only when needed

Examples:
- add `premortem` when optimistic planning may hide fragile assumptions, missing gates, or rollback risk
- add `ux-writing` when terminology and explanation are failing
- add `architecture-review` when boundaries or coupling start to matter
- add `triad-check` when decisions cross product, design, and engineering

### 4. Treat local overlays as separate

A consumer project will usually still need its own local files such as:
- `AGENTS.md`
- `CLAUDE.md`
- project decision logs
- project state docs

Those local files should reference this repository, not copy it.

## Using the library without AletheIA

Use the skill as the execution guide.

Typical loop:
1. choose the right skill
2. run its core moves
3. activate only the needed modules
4. produce the expected output
5. verify closure using the skill's verification section

For a more detailed usage guide, see `docs/how-to-use-a-skill.md`.

## Using the library with AletheIA

Use Adaptive Skills for micro execution and AletheIA for macro orchestration.

A practical split:
- **Adaptive Skills** -> execution pattern, heuristics, output discipline
- **AletheIA** -> framing, review gates, continuity, handoff, learning

AletheIA may suggest the skill, enforce minimum proof, or detect the need for handoff.
The skill itself remains independently useful.


## Using the library with AletheIA roles

If your project already uses AletheIA agent roles, treat this repository as the micro layer consumed by those roles.

Healthy split:

- **role** decides the semantic boundary
- **skill** gives the execution discipline inside that boundary
- **consumer projection** decides how the skill becomes available in Codex, Claude Code, or another runtime

Recommended entrypoint:

- `docs/agent-role-integration.md`
- `examples/aletheia/role-to-skill-consumption.md`

Do not create new generic skills just because a role exists. Prefer using the current canon through a small role-to-skill bundle first.

## Projection strategy

### Codex

Codex projection is supported as a first-class path.

Typical setup:
```bash
python3 scripts/validate_skills.py
python3 scripts/project_to_codex.py --all --dry-run
python3 scripts/project_to_codex.py --all
```

For a more operational consumer setup, see `docs/codex-consumer-setup.md`.

### Claude

Claude projection is selective in v0.
Current modes are:
- `link-only`
- `manual`
- `available-not-default`

Do not force a symmetric projection model until the consumer project actually needs it. Every skill can still be used if you decide to adopt it later.
For a practical guide, see `docs/claude-consumer-setup.md`.

## First-week success criteria

Adoption is working if, within one week:
- the team can pick a skill without confusion
- at least one real task improves clarity or proof quality
- local overlays stay local instead of leaking into generic skills
- no one feels forced to run all modules all the time

## Common failure modes

- importing too many skills at once
- copying project-local rules into generic skills
- treating modules as mandatory phases
- trying to make the library replace product or engineering judgment

## After setup: run a small pilot

Do not jump from setup directly into broad rollout.
Use `docs/first-consumer-pilot.md` and `docs/pilot-evaluation-checklist.md` to run a bounded first adoption round.

## Real consumer reference

For the first concrete small-lane pilot in production-like work, see [`docs/crisis-monitor-case-study.md`](crisis-monitor-case-study/). This is the first validation case (per [ADR-002](adr/ADR-002-domain-agnosticism/)), not the canonical reference — other consumer cases across other domains are expected.
