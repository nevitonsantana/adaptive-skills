# Template — Sunset Decision Record

Output template for `sunset-decision`. One disposition, decided on usage AND cost AND
support — never one signal alone.

| Field | Value |
| --- | --- |
| **Feature** | One-line name. |
| **Usage** | Summary + numbers. |
| **Permanent cost** | Maintenance, security, operations, upgrade blocks. |
| **Support load** | Tickets, on-call, escalations. |
| **Strategic alignment** | Fit with current direction. |
| **Dependencies** | What breaks if it changes (internal + customer-facing). |
| **Value per cost** | positive / flat / negative. |
| **Disposition** | keep / limit / refactor / deprecate / remove. |
| **Plan** | Migration/removal plan, reduced scope, or next review trigger. |
| **Churn guardrail** | What must not happen (e.g. 0 strategic accounts lost). |
| **Evidence** | The data behind the disposition. |
| **Uncertainty** | What is not yet known. |

> Deprecate/remove always carries a migration plan and a churn guardrail. Check
> strategic-account dependencies before removal.
