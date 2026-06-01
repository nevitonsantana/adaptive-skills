# Domain Pack — Product Value Governance

Bundles the skills that evaluate features as **value bets that consume permanent
complexity**, and connects them to AletheIA's
[Feature Value Governance Contract](../../../aletheia/schemas/feature-value-governance-contract.schema.json)
and [readiness gates](../../../aletheia/policies/feature-readiness-gates.md).

> A feature is not a deliverable. A feature is a value bet that consumes permanent
> complexity until it proves it deserves to exist.

## Skills in this pack

| Skill | Role | Output |
| --- | --- | --- |
| [`feature-value-governance`](../../skills/feature-value-governance/) | **Orchestrator / judge** — renders the worth-doing verdict. | Feature value analysis + decision. |
| [`revenue-lever-mapping`](../../skills/revenue-lever-mapping/) | Names the single lever and its metric. | Revenue lever map. |
| [`opportunity-tree-alignment`](../../skills/opportunity-tree-alignment/) | Connects outcomes → opportunities → levers → features. | Aligned tree, orphans flagged. |
| [`feature-complexity-audit`](../../skills/feature-complexity-audit/) | Estimates permanent cost before build. | Complexity scorecard. |
| [`sunset-decision`](../../skills/sunset-decision/) | Judges existing features for keep/limit/refactor/deprecate/remove. | Sunset decision record. |

## Design principles

- **Flat & knowledge-aware.** Each skill is a flat `skills/<name>` and declares the
  knowledge it needs (`strategic_framework`, etc.) as *types*. No proprietary framework
  content lives in these skills.
- **Pluggable value lens.** The four-layer lens (existence / growth / sustainment /
  organization) is supplied as a `strategic_framework` knowledge pack — a proprietary pack
  or the generic `example-4-layers` — never hard-coded here.
- **No inflation.** `feature-value-governance` orchestrates; the others are reusable
  capabilities it calls. They do not duplicate each other's logic.
- **Score is not truth.** Every output states evidence *and* uncertainty.

## Templates

- [`feature-value-decision-record`](../../templates/feature-value-decision-record.md)
- [`revenue-lever-map`](../../templates/revenue-lever-map.md)
- [`complexity-scorecard`](../../templates/complexity-scorecard.md)
- [`sunset-decision-record`](../../templates/sunset-decision-record.md)

## See also

- [`skill-map.md`](./skill-map.md) — which skill answers which question.
- [`orchestration-pattern.md`](./orchestration-pattern.md) — how they compose for Build / Test / Park / Kill / Sunset.
- [`examples/`](./examples/) — worked walkthroughs.
