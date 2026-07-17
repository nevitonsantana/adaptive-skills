# Using Skills Inside Harnesses

## Goal

Show how an ordinary skill runs *inside* a declared Agent Harness Contract (AHC) without changing
the skill itself. The harness sets the envelope; the skill executes within it.

The AHC is declared in AletheIA (`docs/contracts/agent-harness-contract.md`); a fill-in template
lives at [`../templates/agent-harness-contract.yaml`](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/agent-harness-contract.yaml).

---

## How the pieces meet

1. **`allowed_skills` / `blocked_skills`** — the harness names which skills may run. The skill does
   not decide this; the contract does.
2. **`gates`** — when a skill's core move would write, delete, call out, or change structure, the
   matching gate (`before_write`, `before_delete`, `before_external_call`, `before_structural_change`)
   applies *before* the move commits.
3. **`sensors`** — the *sensor-before-judgment* rule: a skill should run its computational sensors
   (tests, linters, type checks) before consulting an inferential one (a review skill).
4. **`observability`** — the skill's decisions and evidence feed the harness trace (see
   [`../templates/harness-trace-summary.md`](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/harness-trace-summary.md)).
5. **`rollback` / `human_review`** — for risky or irreversible work, the skill's output stays a
   draft until the contract's human review clears it.

---

## What does not change

- The skill's 11 sections, triggers, and verification stay exactly as authored.
- The skill never embeds tool permissions, autonomy, or rollback — those live in the contract.
- A skill that was safe under a light harness stays correct under a strict one; only the envelope tightens.

---

## See also

- [skill-harness-boundaries.md](skill-harness-boundaries/)
- [harness-aware-engineering-skills.md](harness-aware-engineering-skills/)
- [execution-modes.md](execution-modes/)
