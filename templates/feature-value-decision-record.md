# Template — Feature Value Decision Record

Fill one per feature, opportunity, or relevant increment. Maps 1:1 to the AletheIA
[Feature Value Governance Contract](../../aletheia/schemas/feature-value-governance-contract.schema.json).
The score is a decision aid, never the decision.

| Field | Value |
| --- | --- |
| **Feature name** | Short, traceable name. |
| **Real problem** | The pain or opportunity that justifies the discussion. |
| **ICP affected** | Who gains value primarily. |
| **Revenue lever** | acquisition / activation / retention / expansion / efficiency / margin / strategic_defense. |
| **Expected outcome** | The behavioral or business change expected. |
| **Evidence** | Data, research, tickets, lost deals, interviews, benchmark. |
| **Uncertainty** | What is *not* known yet. Required — keeps the score from posing as truth. |
| **Permanent cost** | UX, support, QA, documentation, operations, security, maintenance. |
| **Reversibility** | flag / cohort / rollback / sunset / migration plan. |
| **Primary metric** | The metric that proves success (with direction). |
| **Guardrails** | Metrics that must not get worse. |
| **Strategic framework** | `pack_id@version` of the value-lens pack used, or `generic`. |
| **Decision** | Build / Test / Discovery / Park / Kill / Sunset. |
| **Exception approval** | Required if permanent cost is high and decision is Build. |
| **Owner & review** | Responsible person and 30/90-day review dates. |

> Born measurable: a Build or Test decision must carry a primary metric, a guardrail, an
> owner, and review dates before it ships.
