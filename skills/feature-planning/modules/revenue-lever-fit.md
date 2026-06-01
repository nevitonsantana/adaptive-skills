# Module — Revenue-Lever Fit (feature-planning)

Confirms the plan's first slice actually moves the **declared revenue/value lever** — not
just adjacent activity that looks like progress.

## When to run

When the plan risks optimizing something measurable but beside the point (e.g. shipping a
dashboard when the lever is retention).

## Check

1. Restate the declared primary lever (from `revenue-lever-mapping` or the contract's
   `revenue_lever`).
2. For the **smallest useful slice**, ask: does *this slice* plausibly move *that lever*?
   If the slice only moves a proxy, name the proxy and the condition under which it
   diverges from the lever.
3. Tie the slice's acceptance evidence to the lever's primary metric, with a direction.

## Outcome

- **Fit** → the slice's acceptance criterion references the lever's primary metric.
- **No fit** → reshape the slice, or flag that the plan is optimizing activity and route
  back to `feature-value-governance` / `revenue-lever-mapping`.

## Anti-patterns

- Accepting a slice because it ships, not because it moves the lever.
- Measuring activity (clicks, page views) as if it were the lever.
- Carrying no metric into the plan, then declaring success by vibes.
