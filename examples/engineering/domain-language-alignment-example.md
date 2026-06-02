# Example — Domain Language Alignment

## Situation

A team is about to build a "subscription cancellation" feature. In conversation, people say *cancel*, *pause*, *expire*, and *churn* interchangeably. The code already has a `deactivateAccount()` method, and the product spec talks about "ending a plan".

## Skill combination

- `domain-language-alignment`
- `feature-planning`

## Why this combination

- `domain-language-alignment` settles the vocabulary before implementation.
- `feature-planning` then scopes a slice using the agreed terms.

## Walking the moves

### 1. Context and docs

The product spec, a `CONTEXT.md`, and the billing module are the relevant sources. The change touches behavior and billing, so misalignment is risky.

### 2. Extract key terms

`cancel`, `pause`, `expire`, `churn`, `deactivateAccount`, `end a plan`.

### 3. Mark ambiguity and conflict

- *cancel* vs *pause*: ambiguous — one ends billing, the other suspends it. They are different behaviors.
- *expire* vs *churn*: *expire* is a system event; *churn* is an analytics outcome. Conflated in chat.
- `deactivateAccount()` (code) vs "end a plan" (spec): conflict — the code name is broader than the intended behavior.

### 4. Recommend canonical terms

| Term | Canonical meaning | Home |
|---|---|---|
| cancel | user ends the subscription; billing stops at period end | glossary + code |
| pause | subscription suspended, resumable, billing paused | glossary |
| expire | system event when a period ends without renewal | glossary |
| churn | analytics outcome derived from cancel/expire | analytics docs only |

### 5. ADR candidates

- Whether `cancel` stops billing immediately or at period end (constrains billing design) → ADR.
- Whether to rename `deactivateAccount()` to `cancelSubscription()` → ADR.

### 6. Handoff summary

"Build `cancel` = stop billing at period end, resumable=false. `pause` is a separate future behavior. Rename `deactivateAccount()` → `cancelSubscription()` pending ADR. `churn` stays an analytics term, not a code concept."

## What this example shows

- Distinct behaviors hiding behind interchangeable words were separated.
- A code-vs-domain naming conflict was surfaced before implementation.
- Two design-constraining decisions were routed to ADRs.
