# Skill Quality Gate

Use this template before creating, expanding, splitting, merging or deprecating a skill.

## Proposal

- **Proposal id:** `<id>`
- **Proposal type:** `new_skill | optional_module | merge | split | deprecate | reject`
- **Target skill(s):** `<skill-id-or-none>`
- **Reviewer:** `<person-or-role>`
- **Source refs:** `<issue|pack|observation|proposal>`

## 1. Necessity

- What recurring problem does this solve?
- What evidence shows recurrence?
- What breaks if this skill or change does not exist?
- Is the evidence source-backed, synthetic, or still unavailable?

**Assessment:** `strong | partial | weak | unavailable`

## 2. Distinctness

- Which existing skills are adjacent?
- Why is this not an optional module of an existing skill?
- Which boundaries must remain protected?

**Assessment:** `strong | partial | weak | unavailable`

## 3. Proportionality

- Are Core Moves limited to 3–5 durable moves?
- Are Optional Modules triggered only by context?
- Are sidecars necessary, non-empty and reusable?
- Is the proposed structure smaller than the problem it solves?

**Assessment:** `strong | partial | weak | unavailable`

## 4. Context discipline

- What is the minimum context required?
- What should remain on-demand?
- What local content, proprietary source, policy text or project state must not be embedded?

**Assessment:** `strong | partial | weak | unavailable`

## 5. Verification

- What output proves the skill worked?
- What checks are observable?
- What failure signals should reviewers watch for?
- What handoff signal should be produced?

**Assessment:** `strong | partial | weak | unavailable`

## 6. Governance boundary

- Does the skill declare rather than enforce?
- Does it avoid approving, blocking, closing or mutating work?
- Does it avoid runtime policy, permission or provider-specific requirements?
- Does it align with harness requirements when operational risk exists?

**Assessment:** `strong | partial | weak | unavailable`

## 7. Decision

Choose one:

- `accept_as_new_skill`
- `convert_to_optional_module`
- `merge_into_existing_skill`
- `split_existing_skill`
- `deprecate`
- `defer_until_recurrence_is_proven`
- `reject`

## Decision rationale

Explain the decision in 3–7 bullets, with source refs.

## Follow-up

- **Next action:** `<implement|revise|observe|defer|close>`
- **Required validation:** `<scripts or review checks>`
- **AletheIA governance link:** `<contract or work-slice ref if applicable>`
