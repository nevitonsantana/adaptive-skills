# Orchestration Pattern — Product Value Governance

How `feature-value-governance` composes the other skills to reach a Build / Test /
Discovery / Park / Kill / Sunset verdict, and how the result lands on the AletheIA
[Feature Value Governance Contract](../../../aletheia/schemas/feature-value-governance-contract.schema.json).

## Flow

```
                         ┌─────────────────────────────┐
   new feature / ──────▶ │  feature-value-governance   │ ◀── resolve strategic_framework
   opportunity           │        (orchestrator)       │     (pluggable knowledge slot)
                         └──────────────┬──────────────┘
            calls, as the question demands:
   ┌──────────────────┬──────────────────────┬───────────────────────┐
   ▼                  ▼                      ▼                       ▼
revenue-lever     opportunity-tree      feature-complexity      (existing feature)
  -mapping          -alignment             -audit                sunset-decision
   │                  │                      │                       │
   └── lever+metric   └── aligned tree       └── permanent cost      └── disposition+plan
                      orphans flagged           + reversibility
                          │
                          ▼
              ┌─────────────────────────────┐
              │  Decision + Contract record │  (gates applied; born measurable;
              │  Build/Test/Park/Kill/Sunset│   high cost → exception_approval)
              └─────────────────────────────┘
```

## Step pattern

1. **Frame & resolve.** The orchestrator states the feature and resolves the
   `strategic_framework` slot (generic if none). It decides the task shape, which sets
   conditional knowledge requirements (e.g. accessibility for interface changes).
2. **Map the lever.** If the value claim is contested, call `revenue-lever-mapping`.
3. **Align the tree.** If multiple bets compete, call `opportunity-tree-alignment` and
   flag orphans.
4. **Audit complexity.** Before any Build verdict on non-trivial work, call
   `feature-complexity-audit`. A `high` level forces a scope reduction or
   `exception_approval`.
5. **(Existing features)** For portfolio/retro questions, call `sunset-decision` instead
   of judging a new bet.
6. **Apply gates & decide.** Run the seven
   [readiness gates](../../../aletheia/policies/feature-readiness-gates.md); render one of
   the six verdicts; record it on the contract with metric, guardrail, owner, and review
   dates.

## Composition rules

- **One judge.** Only `feature-value-governance` renders the worth-doing verdict; the
  others return inputs to it. This avoids duplicated lever/complexity logic.
- **Call the narrowest skill.** Don't invoke the whole chain for a question one skill
  answers.
- **Evidence travels with the verdict.** Each called skill returns its uncertainty; the
  orchestrator must surface it, never launder it into a clean score.
- **Knowledge stays pluggable.** No skill names a specific framework; the resolver fills
  `strategic_framework` and the verdict cites `pack_id@version` (or `generic`).
