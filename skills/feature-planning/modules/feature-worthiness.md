# Module — Feature Worthiness (feature-planning)

A pre-planning gate. Planning a feature that should be killed or parked is wasted work, so
confirm the feature was judged worth doing **before** shaping delivery.

## When to run

At the start of any non-trivial feature plan, before slicing scope.

## Check

Confirm a worth-doing judgement exists (ideally a `feature-value-governance` verdict or a
[Feature Value Governance Contract](../../../../aletheia/schemas/feature-value-governance-contract.schema.json)
record) covering:

- **Problem** — a real, relevant problem is stated.
- **ICP** — the gain lands on the right audience.
- **Lever** — a single revenue/value lever is named.
- **Evidence + uncertainty** — both are stated; the score is not treated as truth.
- **Permanent cost** — the carry is acknowledged, and if high, an exception or scope
  reduction is recorded.

## Outcome

- **Worthiness proven** → proceed to planning; carry the lever and primary metric into the
  plan's acceptance criteria.
- **Worthiness unproven or weak** → stop. Route to `feature-value-governance` for a Build /
  Test / Discovery / Park / Kill / Sunset decision. Do not plan delivery for an unjudged bet.

## Anti-patterns

- Treating "someone asked for it" as worthiness.
- Planning around a value claim nobody has examined.
- Letting a polished plan substitute for a missing decision.
