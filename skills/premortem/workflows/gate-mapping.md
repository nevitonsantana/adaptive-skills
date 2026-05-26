# Premortem — Gate Mapping

Convert premortem findings into decision gates. A good premortem does not end with a risk list; it defines what must be blocked, conditioned, reviewed, or decided by a human.

## Gate types

**Hard gate** — blocks progress until a minimum condition is met.

Use when the premortem finds: no success criterion; no rollback path; unevaluated legal or regulatory risk; unevaluated security risk; sensitive data without clear governance; impact on vulnerable users without mitigation; critical dependency without an owner; AI agent behavior without explicit action boundaries.

Format: `Hard gate: do not proceed until [verifiable condition] is resolved.`

---

**Soft gate** — allows progress with an explicit condition, pilot, reduced scope, or mitigation.

Use when: the hypothesis is weak but testable; there is a known risk with reasonable mitigation; impact is controllable; the plan can run as a pilot; evidence is still missing but the cost of learning is acceptable.

Format: `Soft gate: proceed only if [condition] and with [exposure limit].`

---

**Review trigger** — requires specialist review before proceeding.

Use when there is impact on: UX, accessibility, security, privacy, data protection, architecture, agent behavior, brand, or critical operations.

Format: `Review trigger: involve [specialty/role] before [milestone].`

---

**Human decision gate** — the model does not decide. It structures trade-offs and options for a human.

Use when: there is conflict between deadline and quality; reputational risk; impact on people; ethical ambiguity; strategic, political, or institutional decision; the choice depends on risk appetite.

Format: `Human decision gate: human decision needed between [options], considering [trade-off].`

---

## How to map findings to gates

For each significant failure mode, answer:

1. Does this failure block progress?
2. Can it be mitigated with a pilot or reduced scope?
3. Does it require specialist review?
4. Does it require an explicit human decision?

---

## Output format

```md
### Hard gates
- ...

### Soft gates
- ...

### Review triggers
- ...

### Human decision gates
- ...
```

If no gate is needed: `No formal gate recommended. The decision can proceed with a simple monitoring checklist.`
