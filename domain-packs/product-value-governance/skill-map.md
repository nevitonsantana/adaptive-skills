# Skill Map — Product Value Governance

Which skill answers which question. Pick the narrowest one; reach for the orchestrator
when you need a verdict.

| Question | Skill |
| --- | --- |
| "Is this feature worth doing at all?" | `feature-value-governance` (orchestrator) |
| "Which lever does this move, and how would we know?" | `revenue-lever-mapping` |
| "How do these competing bets connect to outcomes and levers?" | `opportunity-tree-alignment` |
| "What permanent cost does this carry before we commit?" | `feature-complexity-audit` |
| "Should this existing feature stay, shrink, or go?" | `sunset-decision` |

## Decision → skills

| Decision | Primary path |
| --- | --- |
| **Build Now** | value-governance ← lever-mapping + complexity-audit (cost acceptable, metric set) |
| **Test First** | value-governance ← lever-mapping (evidence weak) + complexity-audit (define smallest test) |
| **Discovery First** | value-governance ← lever-mapping (lever/ICP fragile) |
| **Park** | value-governance (plausible, no capacity; record resumption trigger) |
| **Kill** | value-governance ← complexity-audit (cost ≫ value, orphan) |
| **Sunset** | `sunset-decision` (existing feature, low traction, high carry) |

## Boundaries (when NOT to use this pack)

- The decision to build is already made and only execution planning remains → `feature-planning`.
- The change is tiny, local, and obviously valuable.
- The question is structural design, not worth-doing → `architecture-review`.
- The question is what to measure once built → `observability-review`.
