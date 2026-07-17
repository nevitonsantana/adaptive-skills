# Harness-Aware Engineering Skills

## Goal

Connect the engineering skills hardened in the
[Engineering Skills Hardening Pack](engineering-skills-hardening-pack/) to the harness envelope:
which skills expect which **sensors** and **gates** when run under an Agent Harness Contract.

This does not modify any `SKILL.md`. It documents the harness shape each engineering skill works
best inside, so a contract author can fill `sensors` and `gates` sensibly.

---

## Skill → expected sensors and gates

| Skill | Computational sensors | Inferential sensor | Gates that usually apply |
|---|---|---|---|
| `debugging` | `failing_test`, `regression_test` | `debugging_review` | `before_write`, `before_structural_change` |
| `testing` | `test_suite`, `coverage_delta` | `testing_review` | `before_write`, `before_final_answer` |
| `architecture-review` | `schema_validation`, build/typecheck | `architecture_review`, `risk_review` | `before_structural_change`, `before_final_answer` |
| `domain-language-alignment` | — | `review_skill` | `before_final_answer` |

The principle (AletheIA: *sensor before judgment*): run the computational sensors first; consult the
inferential review only after they pass or genuinely cannot decide.

---

## Worked contracts

Two filled examples live in AletheIA:

- `examples/harness/codex-debugging-harness.md` — `debugging` + `testing`, `act_with_approval`, gated writes.
- `examples/harness/codex-testing-harness.md` — `testing`, low risk, light gates.

Start from [`../templates/agent-harness-contract.yaml`](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/agent-harness-contract.yaml)
and the table above when authoring a new one.

---

## See also

- [engineering-skills-hardening-pack.md](engineering-skills-hardening-pack/)
- [skill-harness-boundaries.md](skill-harness-boundaries/)
- [using-skills-inside-harnesses.md](using-skills-inside-harnesses/)
