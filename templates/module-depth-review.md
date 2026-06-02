# Module Depth Review

A short review to decide whether a module earns its interface or merely relocates complexity. Pairs with the `architecture-review` skill's **Module depth review** module.

## Module or boundary under review

_The module, layer, or seam being evaluated._

## Interface

_The surface callers actually use (methods, signatures, contract size)._

## Implementation complexity hidden

_What real complexity sits behind the interface._

## Leverage

_Does the interface hide more than it exposes? Is it deep (small interface, large hidden behavior) or shallow (interface as big as what it hides)?_

## Locality

_Do related changes stay concentrated inside the module, or scatter across the codebase?_

## Deletion test

_If this module were removed, what complexity returns and where? If little returns, the module may not earn its place._

## Adapter reality

_Is the seam real (multiple concrete implementations or a genuine boundary) or hypothetical (one implementation, speculative future)?_

## Test surface

_Is this interface a good place to verify behavior, or does verification leak to internals?_

## Recommendation

- [ ] proceed
- [ ] reduce
- [ ] merge
- [ ] split
- [ ] escalate
