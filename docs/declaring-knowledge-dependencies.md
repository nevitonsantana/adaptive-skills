# Declaring Knowledge Dependencies

## Goal

Explain how a skill declares the knowledge it needs **without** binding to a specific source.

The full contract lives in the AletheIA repository: see [skill-knowledge-dependency-contract](https://github.com/nevitonsantana/AletheIA/blob/main/docs/contracts/skill-knowledge-dependency-contract.md). This document is the author-facing guide for the Adaptative Skills side.

---

## The shape of a declaration

A skill ships a `skill-knowledge-dependency.yaml` alongside its `SKILL.md`. It lists *slots* the skill needs filled. Each slot describes:

- whether it is `required`, `optional`, or `required_when` a condition matches
- which `accepted_types` of source can fill it
- the minimum `authority_level` the slot accepts
- a `preferred_retrieval_mode` hint to the resolver

The slot key is meaningful to the skill (e.g. `strategic_framework`, `personas`, `accessibility_guidelines`). It is **not** a source id.

---

## Three kinds of dependency

| Kind | When to use |
|---|---|
| `required: true` | the skill cannot produce its expected output without this knowledge type |
| `required: false` | the skill is useful without it; presence improves output |
| `required_when: [...]` | required only when listed task triggers match |

Pick `required_when` when a slot activates by task shape (interface change, content decision, customer-facing experience, etc.). Most accessibility, privacy, and compliance slots are conditional.

---

## Choosing `accepted_types`

Use the source taxonomy in [knowledge-source-contract](https://github.com/nevitonsantana/AletheIA/blob/main/docs/contracts/knowledge-source-contract.md). Prefer the **broadest set** of types that genuinely satisfy the slot:

- `strategic_framework` may accept `proprietary_framework`, `product_strategy`, `business_design_framework`.
- `accessibility_guidelines` should usually accept only `accessibility_guideline`.
- `personas` may accept `persona` and `research_finding`.

Narrowing past necessity creates portability problems. Widening past necessity creates governance problems.

---

## Fallback behavior — required, not optional

Every knowledge-aware skill must declare `fallback_behavior` for the four cases:

- `missing_required_source`
- `missing_optional_source`
- `restricted_source`
- `conflicting_sources`

The skill must choose explicit values. "Silent continuation" is never one of them.

Recommended defaults:

```yaml
fallback_behavior:
  missing_required_source: stop_and_request_source
  missing_optional_source: continue_with_assumption_marker
  restricted_source: request_authorized_context_pack
  conflicting_sources: apply_source_precedence_policy
```

---

## Output expectations

A skill output should make the knowledge picture reconstructable:

- list which slots were satisfied and by which `pack_id@version`
- list which slots were unsatisfied and which fallback fired
- list which restrictions were active (capsule-only, no verbatim, etc.)
- list any conflicts detected and how precedence resolved them

This is what makes the [knowledge audit log](https://github.com/nevitonsantana/AletheIA/blob/main/docs/contracts/knowledge-audit-log-spec.md) buildable from the skill output alone.

---

## Common mistakes

- **Naming a source.** Don't list `accepted_sources: [example-4-layers]`. List a *type*.
- **Hidden requirements.** Don't write a skill that only works when a specific framework is loaded but does not declare it.
- **Greedy retrieval.** Don't set `preferred_retrieval_mode: full_source_allowed` when the skill would work with a capsule.
- **Silent generic fallback.** When a required source is missing, *say so*; do not produce a confident output as if the source were present.

---

## See also

- [skill-knowledge-boundaries.md](skill-knowledge-boundaries/)
- [using-proprietary-frameworks-safely.md](using-proprietary-frameworks-safely/)
- [skill-knowledge-dependency.yaml](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/skill-knowledge-dependency.yaml)
