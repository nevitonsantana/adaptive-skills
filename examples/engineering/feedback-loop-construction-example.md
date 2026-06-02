# Example — Feedback Loop Construction

## Situation

An intermittent bug: a price-rounding function occasionally returns a value one cent off, but only for some inputs. Nobody can reliably reproduce it, and the team is tempted to "just add a rounding fix" by instinct.

## Skill combination

- `debugging`
- `testing`

## Why this combination

- `debugging` (Feedback loop construction) builds a deterministic pass/fail signal before any code change.
- `testing` turns the reproduced case into a behavior-level guard so the bug cannot return silently.

## Minimal flow

### 1. Name the failure

- Failure: `round_total(amount, rate)` sometimes returns a value off by one cent.
- It is intermittent — instinct-patching would be guesswork.

### 2. Find the smallest reproducible signal

Instead of clicking through the app, isolate the function with a small set of inputs that includes a known-bad case:

- input: `amount = 0.145`, `rate = 0.2`
- observed: `0.17`
- expected: `0.18`

### 3. Choose a loop type

A focused failing test is the smallest deterministic loop here (no network, no UI):

```
# loop type: failing test (example runner — any deterministic runner works)
assert round_total(0.145, 0.20) == 0.18   # currently fails -> red
```

### 4. Run and confirm the red

Run the single test. It fails predictably every time — the intermittency was really input-dependent, not random.

### 5. Fix the cause, re-run for green

Adjust the rounding to use a stable decimal strategy, then run the same loop:

- expected fail state: assertion error on `0.17`
- expected pass state: assertion passes at `0.18`

### 6. Recurrence guard

Keep the failing case (plus two boundary cases) as a permanent behavior test. The loop that proved the bug becomes the guard against its return.

## What this example shows

- A deterministic pass/fail signal replaced "intermittent → guess".
- The loop was small enough to run inside the debugging session.
- The fix was validated against the original failure path before expanding scope.
