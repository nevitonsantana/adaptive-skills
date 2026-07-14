# Design System Intelligence — Pulso Pilot

This note describes the first Adaptive Skills side of S24. It introduces one bounded skill, `design-system-intelligence`, for manual design-system review.

## Boundary

The skill provides a review method. It does not:

- own Pulso;
- make Pulso a dependency of Adaptive Skills;
- approve visual decisions;
- promote components or tokens;
- run automatic scans;
- remediate code;
- decide AletheIA gates.

## Pulso pilot mode

Pulso is the first lab because it is a known design-system context in the user's ecosystem. In this mode, the skill should:

1. load only the relevant Pulso source refs or registry pointers;
2. compare the artifact against source-backed primitives;
3. separate conformance, intentional exceptions, candidate issues, and candidate patterns;
4. apply a Pattern Generalization Gate before recommending any reusable pattern review;
5. return source-backed observations for AletheIA or a consumer harness.

## Pattern Generalization Gate

A repeated pattern is only a signal. Promotion requires a design-system owner or reviewer, comparable artifacts, source refs, accessibility implications, and known uncertainty.

If those are missing, the safe result is `needs_more_evidence`, `hold`, or `human_review_required`.

## Expected evidence

- `design_system_ref`
- `artifact_refs`
- `source_refs`
- conformance observations
- candidate findings
- Pattern Generalization Gate outcome
- unavailable evidence and owner-review needs

## AletheIA relationship

AletheIA remains the macro-governance surface. Adaptive Skills declares the method and observation shape; AletheIA decides whether the review is sufficient for a Work Slice gate, reconcile, or later evolution proposal.
