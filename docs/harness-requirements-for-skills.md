# Harness Requirements for Skills

> AletheIA governs. Harness enforces. Adaptative Skills declares requirements.
> Knowledge Governance limits context. Audit proves.

## Goal

Give a skill a way to **declare** the operating envelope it needs to run safely — the tools it
expects, the tools it must not touch, the autonomy ceiling it should run at, the gates that guard
side effects, the evidence it must leave behind, and the minimum audit it requires.

This is a **declaration, not an enforcement mechanism**. A `harness_requirements` block does not
execute, authorize, or block anything. It states what a *correct* harness would have to provide and
guard. Whether those requirements are honored — allowed, denied, paused for approval, transformed —
is decided by the harness/runtime, and the contracts that define those decisions live in AletheIA,
not here.

This sits alongside:
- [skill-harness-boundaries.md](skill-harness-boundaries.md) — *skill vs. environment* (a skill is a
  procedure; a harness is an execution environment).
- [skill-knowledge-boundaries.md](skill-knowledge-boundaries.md) — *skill vs. content*.

Together they keep a skill free of embedded environment, embedded content, **and** embedded
enforcement.

Catalog-level creation and expansion decisions are governed separately by [Skill Catalog Governance](skill-catalog-governance.md) and the [Lean Skill Doctrine](skill-design-principles/lean-skill-doctrine.md). A harness declaration can describe required operating conditions, but it cannot justify a new skill by itself.

---

## Three layers, never merged

| Layer | Owns | Lives in |
|---|---|---|
| **Guidance** | how to think, what to ask, what to produce | the skill (`SKILL.md`) |
| **Requirements (this doc)** | what operating envelope the skill needs | `harness_requirements` declaration |
| **Policy & enforcement** | autonomy, tool risk, verdicts, audit record, the actual allow/deny | AletheIA contracts + the harness/runtime |

A skill **declares**. The harness **enforces**. AletheIA **defines the contracts** the harness
enforces against. If a skill ever starts blocking tool calls itself, the boundary has been violated.

The AletheIA side of this contract:
[`docs/contracts/agent-harness-governance-extension.md`](https://github.com/nevitonsantana/aletheia)
(tool exposure, permission decisions, audit traces) and
`docs/concepts/enforcement-boundaries.md` (behavioral vs. technical enforcement). Autonomy level,
tool-risk taxonomy, policy verdicts, and the audit record are all defined there.

---

## The `harness_requirements` block

Fill-in template: [`../templates/skill-harness-requirements.yaml`](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/skill-harness-requirements.yaml).

This is **per-skill**. It is distinct from
[`../templates/agent-harness-contract.yaml`](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/agent-harness-contract.yaml), which is the
**per-task** operating envelope. A skill says "this is what I generally need"; a task contract says
"this is the envelope for this specific run."

### Fields

- **`skill_id` / `version`** — which skill declares this, and the declaration's version.
- **`autonomy`** — `floor` and `ceiling`, plus a `rationale`. Enum values mirror AletheIA's
  canonical vocabulary exactly: `observe | advise | act_with_approval | autonomous_within_bounds`.
  *Do not invent levels.* A consultative skill sets `ceiling: advise`; an operational skill that may
  act after approval sets `ceiling: act_with_approval`.
- **`expected_tools`** — tools the skill normally needs, each with a `purpose` and a `risk_class`
  (`low | medium | high | critical`, per the AletheIA tool-risk taxonomy).
- **`restricted_tools`** — tools the skill must not use freely, each with a `restriction`
  (`deny | require_approval | transform | log_only`) and a `rationale`.
- **`approval_gates`** — named points where a side effect must pause for a human (e.g.
  `before_destructive_action`, `before_external_side_effect`, `before_schema_or_contract_change`).
- **`required_evidence`** — what the skill must leave behind before it can close (e.g. `repro_path`,
  `validated_fix`, `verdict_rationale`). This is what keeps the declaration from being "policy
  theater": a pretty YAML with no proof.
- **`escalation_triggers`** — conditions that should bump the work to a human or a stricter contract
  (e.g. `touches_auth`, `touches_data_model`, `modifies_policy`, `changes_public_contract`).
- **`audit_requirements`** — the minimum the harness should log: skill id, task id, tool calls,
  policy verdict, evidence refs, and human approval *when required*.

---

## Operational vs. consultative skills

The single most important distinction this declaration protects.

**Consultative skills** produce a recommendation, a verdict, or a decision record — and nothing more.
They must **not look like authorization to act**. `feature-value-governance` may produce a verdict on
whether a feature should advance, but it must not move the roadmap, create an issue, alter the
backlog, or execute a decision. Such a skill declares `ceiling: advise` and marks
`roadmap.update` / `issue.create` / `filesystem.write` as `deny` or `require_approval`.
See [`../examples/harness-requirements/feature-value-governance-harness-requirements.yaml`](https://github.com/nevitonsantana/adaptive-skills/blob/main/examples/harness-requirements/feature-value-governance-harness-requirements.yaml).

**Operational skills** may perform bounded action, but always with: an expected tool set, declared
risk, minimum evidence, a gate before any destructive action, and a handoff when the risk class
changes. `debugging` may run tests and propose a diff (`ceiling: act_with_approval`) but must escalate
structural or destructive changes. `testing` may run tests and read coverage but must not change
implementation — that belongs to another skill.
See [`../examples/harness-requirements/debugging-harness-requirements.yaml`](https://github.com/nevitonsantana/adaptive-skills/blob/main/examples/harness-requirements/debugging-harness-requirements.yaml)
and [`../examples/harness-requirements/testing-harness-requirements.yaml`](https://github.com/nevitonsantana/adaptive-skills/blob/main/examples/harness-requirements/testing-harness-requirements.yaml).

---

## Cross-repo map

Authority for each column lives in AletheIA; the rows are the example skills that ship a declaration
today. This map is the bridge the maintainer/reviewer reads to know, per skill, what it expects and
what is gated.

| Skill | Kind | Autonomy ceiling | Allowed tools | Restricted tools | Approval gates | Required evidence |
|---|---|---|---|---|---|---|
| `debugging` | operational | `act_with_approval` | `filesystem.read`, `shell.test`, `git.diff` | `filesystem.delete` (approval), `secret.read` (deny), `network.external_write` (approval) | destructive / schema-or-contract / dependency-upgrade | repro_path, root_cause, validated_fix, recurrence_guard |
| `testing` | operational (bounded) | `act_with_approval` | `shell.test`, `coverage.read`, `git.diff` | `filesystem.write` (approval — impl belongs to another skill), `network.external_write` (approval), `secret.read` (deny) | destructive / external-side-effect | proof_strategy, executed_evidence, validation_gaps |
| `feature-value-governance` | consultative | `advise` | `knowledge.resolve`, `docs.read` | `roadmap.update` (deny), `issue.create` (approval), `filesystem.write` (deny) | external-side-effect / sensitive-context-use | source_pack_versions, unsatisfied_slots, conflicts, verdict_rationale |

| Column | Defined by (AletheIA) |
|---|---|
| Autonomy ceiling | `docs/concepts/autonomy-levels.md` + `canonical-vocabulary.md` |
| Tool risk class | `docs/concepts/tool-risk-taxonomy.md` (+ `structured-risk-inference.md`) |
| Restriction / verdict | `docs/contracts/policy-verdicts.md` (`allow / deny / require_approval / transform / log_only`) |
| Audit fields | `docs/contracts/agent-action-audit-record.md` |

---

## Future candidate: `harness-readiness-check`

Not built. Documented here as a **candidate only**, to be created *if and only if* readiness
evaluation proves to recur across many flows. Its eventual job would be to evaluate whether a task,
skill, or agent has a sufficient harness contract before execution and return
`ready | ready_with_constraints | not_ready`. Until there is evidence of recurrence, this stays a
note — not a skill, and not a blocking mechanism.

---

## What this layer is *not*

- Not a policy engine, enforcement runtime, or sandbox.
- Not auto-execution of anything.
- Not a dependency on the Microsoft Agent Governance Toolkit, OPA, Cedar, SPIFFE, DID, mTLS, or IAM.
- Not a change to any `SKILL.md`.

It is a declaration designed to remain compatible with a later evolution to policy-as-code — without
forcing that evolution now.

## See also

- [adr/ADR-007-per-skill-harness-requirements.md](adr/ADR-007-per-skill-harness-requirements.md) — why this layer exists and what it is not.
- [skill-harness-boundaries.md](skill-harness-boundaries.md)
- [skill-knowledge-boundaries.md](skill-knowledge-boundaries.md)
- [using-skills-inside-harnesses.md](using-skills-inside-harnesses.md)
- [harness-aware-engineering-skills.md](harness-aware-engineering-skills.md)
