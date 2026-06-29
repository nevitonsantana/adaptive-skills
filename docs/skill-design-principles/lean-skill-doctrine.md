# Lean Skill Doctrine

## Purpose

Keep Adaptive Skills useful as the catalog grows. The risk S20 addresses is not a lack of skills; it
is skill sprawl, overlap, excessive context, weak activation discipline and skills becoming
mini-frameworks.

## Core thesis

A skill should be the smallest reusable behavioral unit that reliably improves a recurring task
shape without absorbing local content, runtime policy or unnecessary context.

Every new skill, module, split, merge or deprecation proposal must prove that the change is:

1. **necessary** — it solves a recurring task shape;
2. **distinct** — it is not already covered by an existing skill or module;
3. **proportional** — its structure is no heavier than the problem requires;
4. **verifiable** — a reviewer can tell whether it worked;
5. **governable** — it declares behavior without enforcing policy or approving work.

## Design principles

- Prefer improving an existing skill before creating a new one.
- Prefer an optional module when the need is contextual rather than dominant.
- Keep Core Moves to 3–5 durable moves.
- Add sidecars only when they reduce cognitive load or improve reuse.
- Keep local project rules, secrets, policies and proprietary context out of skills.
- Treat recurrence as evidence, not as a feeling.
- Preserve the boundary: Adaptive Skills declares; AletheIA governs; the harness/runtime enforces.

## Skill necessity test

A proposal passes the necessity test only when it can answer:

- What recurring problem does this skill solve?
- What evidence shows this is not a one-off local task?
- What breaks or becomes materially worse if the skill does not exist?
- Which existing skills were considered first?

Weak signals:

- “This would be nice to have.”
- “A model produced a long prompt once.”
- “A project has a local checklist.”
- “The catalog should cover this category.”

## Skill distinctness test

A proposal passes the distinctness test only when the dominant need is not already owned by another
skill.

Ask:

- Is this really a new skill, or a module inside an existing skill?
- Does it overlap an existing `When to Use` or `Core Moves` section?
- Would using both skills in one task create redundant guidance?
- Can the boundary be explained in one sentence?

If the boundary is hard to explain, defer, merge or convert to an optional module.

## Proportionality test

A skill is proportional when:

- Core Moves stay at 3–5 moves;
- Optional Modules activate only by trigger;
- examples and templates are useful, not ornamental;
- the skill can be read quickly during real work;
- the skill does not require a new runtime, catalog, policy engine or workflow system.

A small task should not need a large skill to use it safely.

## Context discipline

Skills carry method, not local context.

A skill may include:

- generic examples;
- synthetic fixtures;
- reusable templates;
- public or explicitly authorized references;
- pointers to knowledge dependency declarations.

A skill must not include:

- secrets;
- proprietary source content;
- local project state;
- customer data;
- unreviewed policy text;
- authority claims that belong to AletheIA or the harness.

## Module discipline

Use an optional module when the behavior is useful only under a recognizable condition.

A module should declare:

- the trigger that activates it;
- the extra work it adds;
- the output or evidence it changes;
- when to skip it.

Do not create a module for one-off edge cases.

## Sidecar discipline

Sidecars are allowed when they reduce cognitive load or improve reuse.

Allowed examples:

- `templates/` for repeatable output shapes;
- `examples/` for synthetic or public worked cases;
- `checklists/` for compact review surfaces;
- `references/` for small, explicitly authorized background.

Do not create empty sidecar folders. Do not add sidecars to make a skill look more complete.

## Verification discipline

Every skill must make success observable.

A reviewer should be able to answer:

- What output proves the skill was used correctly?
- What evidence should be produced?
- What failure signals indicate misuse?
- What handoff signal should the user receive?

A skill without verification is guidance theater.

## Boundary discipline

Skills declare guidance and requirements. They do not enforce.

A skill must not:

- approve, block, close or mutate a Work Slice;
- declare runtime permission decisions;
- bypass AletheIA gates;
- hide policy decisions inside triggers;
- rank itself above adjacent skills without evidence;
- weaken validation, security, accessibility or data-integrity requirements to stay “lean.”

## When to create a new skill

Create a new skill only when all are true:

- the task shape is recurring;
- the dominant need is not owned by an existing skill;
- the behavior needs its own `When to Use` and `When NOT to Use` boundary;
- the output can be verified;
- the skill can stay portable across projects;
- the quality gate decision is `accept as new skill`.

## When to add an optional module instead

Add a module when:

- the behavior is useful only under specific triggers;
- the parent skill already owns the dominant need;
- using the behavior alone would be too narrow for a standalone skill;
- the module can remain short and trigger-scoped.

## When to reject or defer

Reject or defer a proposal when:

- recurrence is unavailable or weak;
- the behavior is local project context;
- the proposal overlaps an existing skill;
- the skill would become a mini-framework;
- the proposal requires runtime enforcement;
- verification is unclear;
- the proposal removes safety or evidence to reduce complexity.

## Anti-patterns

- Creating a skill because a phrase sounds reusable.
- Creating a skill before trying an existing skill plus a module.
- Treating a long prompt as proof of a catalog gap.
- Adding sidecars without concrete reuse.
- Collapsing AletheIA governance into a skill.
- Turning skill triggers into a hidden routing engine.
- Treating “lean” as fewer words instead of clearer boundaries.

## Review checklist

Before accepting a catalog change, confirm:

- [ ] Necessity is backed by recurrence evidence or a named source pack.
- [ ] Adjacent skills were reviewed.
- [ ] New skill vs. optional module vs. merge/defer/reject is explicit.
- [ ] Core Moves remain 3–5 durable moves.
- [ ] Sidecars are non-empty and justified.
- [ ] Verification and handoff signals are visible.
- [ ] No local content, secrets or project state are embedded.
- [ ] The skill declares; it does not enforce or approve.

## Related docs

- [Skill Model](../skill-model.md)
- [Skill Catalog Governance](../skill-catalog-governance.md)
- [Harness Requirements for Skills](../harness-requirements-for-skills.md)
- [Evolution Layer](../evolution-layer.md)
- [Capability Routing Boundary](../capability-routing-boundary.md)
- [Skill Quality Gate template](../../templates/skill-quality-gate.md)
