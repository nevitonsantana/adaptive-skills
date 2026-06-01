# Validation Cases

Concrete, reproducible expectations for a skill: given an input and context, what the
skill **must do** and **must not do**, and how a reviewer would know it succeeded.

Validation cases are the unit of evidence for the
[Skill Evolution Validation Layer](../../docs/evolution/skill-evolution-experiments.md).
They do not change any skill — experiments run *against* them.

## Directory guide

- `templates/validation-case-template.md` — canonical format (YAML frontmatter + narrative)
- `examples/` — safe, non-sensitive worked cases

## Rules (summary)

- **Synthetic-first.** Use synthetic, public, or explicitly authorized material only.
- **Declare `sensitivity`** on every case.
- `confidential` / `restricted` / `regulated` cases must set `source_policy: synthetic_only`
  and `capsule_only: true`, and may carry only simulated metadata or a fictional capsule —
  never raw governed content.
- Knowledge-aware skills force `human_review_required: true` on the related experiment.

See [validation-case-guidelines.md](../../docs/evolution/validation-case-guidelines.md) for
the full guidance, and run `python3 scripts/validate_evolution_experiments.py` to check
structure.
