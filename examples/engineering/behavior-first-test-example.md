# Example — Behavior-First Test

## Situation

A team adds a discount rule: orders over 100 currency units get a 10% discount. A first instinct is to test the internal helper `_apply_discount_rate()` directly, which would lock the test to the current private structure.

## Skill combination

- `testing`
- `feature-planning`

## Why this combination

- `testing` (Behavior-first test design + Vertical test slice) keeps the test on the public capability.
- `feature-planning` frames the behavior as a small, independently shippable slice.

## Behavior-first vs implementation-coupled

### Implementation-coupled (avoid)

```
# couples to a private helper and an internal data shape
assert cart._apply_discount_rate(order)._raw_rate == 0.10
```

If the team later renames the helper or restructures internals, this test breaks even though behavior is correct.

### Behavior-first (prefer)

```
# exercises the public interface; describes a capability
order = checkout(items=[item(price=120)])
assert order.total == 108   # 120 - 10%
```

This passes for the behavior and survives internal refactoring.

## Vertical test slice cycle

1. Define expected behavior: "orders over 100 get 10% off".
2. Smallest failing proof: the `order.total == 108` assertion (red — no discount yet).
3. Smallest passing change: implement the discount rule.
4. Refactor: clean up internals; the public test stays green.

## What this example shows

- The test describes a capability, not a private call.
- It fails for the intended behavior gap (no discount) and not for incidental detail.
- One behavior was proven per cycle instead of writing many tests at once.
