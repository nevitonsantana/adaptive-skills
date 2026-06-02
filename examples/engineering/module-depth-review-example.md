# Example — Module Depth Review

## Situation

A team proposes a `NotificationGateway` abstraction in front of a single email sender, "in case we add SMS later". The interface mirrors the email client almost method-for-method.

## Skill combination

- `architecture-review`
- `api-design`

## Why this combination

- `architecture-review` (Module depth review) tests whether the abstraction provides leverage or just a new name.
- `api-design` checks whether the interface would still make sense for a second implementation.

## Walking the checks

### Interface vs hidden complexity

The proposed interface exposes `send(subject, body, to, cc, attachments, headers)` — nearly identical to the underlying email client. Almost nothing is hidden; it is a shallow pass-through.

### Deletion test

If `NotificationGateway` is removed, callers use the email client directly with no loss of behavior. Little complexity returns — a signal the module does not yet earn its place.

### Locality

A real channel change (email field tweaks) would still ripple through the gateway and every caller, because the interface leaks the email shape. Changes are not well concentrated.

### Adapter reality

There is exactly one implementation. The SMS case is hypothetical and would not fit the current email-shaped interface anyway.

### Test surface

Verifying "a user is notified" through this interface still requires asserting email-specific fields, so the seam is not a clean place to test behavior.

## Recommendation

**reduce / defer.** Keep the direct email client now. Introduce a channel-neutral interface (`notify(recipient, message)`) only when a second real channel exists, designing the interface around the shared behavior rather than the email shape.

## What this example shows

- A small interface is not automatically a deep module.
- The deletion test exposed an abstraction that only relocated complexity.
- The seam was hypothetical, so the cost was not yet earned.
