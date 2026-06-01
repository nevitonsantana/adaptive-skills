# Walkthrough — Park (plausible, no capacity)

A real opportunity with a clear lever, but no capacity this cycle. The discipline is to
**record a resumption trigger** instead of silently dropping or silently committing it.

Feature: *saved-view sharing between teammates.*

## 1 — feature-value-governance frames and resolves

- Task shape: `interface_change`. Resolves `strategic_framework` → generic example pack.
- The question is sequencing, so `operating_model` is relevant for prioritization.

## 2 — revenue-lever-mapping

```yaml
revenue_lever_map:
  opportunity: Let teammates share saved views to cut duplicated setup
  mode: knowledge_aware
  primary_lever: activation
  primary_rationale: Faster team-level time-to-value on shared workflows
  metric: { name: teams with >=1 shared view in 30 days, direction: up }
  proxy: { name: "share" intent clicks, validity: intent != successful share }
  risks: [demand may be concentrated in a few large teams]
  uncertainty: true addressable demand not yet sized
```

## 3 — gate read

- Problem ✓ · ICP ✓ · Lever ✓ (activation) · Evidence ~ (moderate) · Complexity (medium,
  not yet audited in depth) · Metrics defined.
- **But:** the current cycle is committed to a higher-evidence retention bet; capacity is
  zero. Nothing here is wrong — it just isn't now.

## 4 — verdict: Park

```yaml
decision:
  verdict: park
  rationale: Plausible activation lever, moderate evidence, but no capacity this cycle.
resumption_trigger: >
  Revisit when (a) the retention bet ships and frees capacity, OR (b) >=3 mid-market teams
  request sharing within one quarter. If neither by next planning, re-evaluate or Kill.
review_dates: { day_90: 2026-09-13 }
```

## What this illustrates

- Park is a first-class, auditable outcome — not a backlog graveyard.
- The resumption trigger has concrete conditions, so the idea can't be quietly recycled by
  pressure or quietly forgotten.
- No full complexity audit was spent on something not being built now — proportional effort.
