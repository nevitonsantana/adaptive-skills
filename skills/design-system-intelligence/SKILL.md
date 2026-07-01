---
name: design-system-intelligence
description: Review an artifact against a declared design system source bundle, classify conformance and candidate patterns, and return source-backed evidence without promotion authority.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: design
---

# Overview

Use this skill when a work artifact should be compared with a known design system before implementation, review, or reuse decisions.

The skill is advisory. It helps the agent inspect source-backed design-system evidence, identify conformance, exceptions, and candidate issues, and decide whether a pattern deserves further human review. It does not own the design system, approve UI decisions, run scanners, or promote components.

# When to Use

- an artifact claims or should claim alignment with a design system
- a design-system source bundle, registry entry, or documented reference is available
- the task needs a conformance review before implementation or handoff
- repeated UI or interaction choices may be pattern candidates but require evidence
- AletheIA or another governance layer asks for a Design System Intelligence review

# When NOT to Use

- no design-system source or registry pointer is available
- the task is general visual exploration; use a design or product-design skill instead
- the task requires final brand, accessibility, legal, or design-system owner approval
- the task asks for automatic remediation, weekly scanning, or package adoption
- the review would copy restricted source content into unrestricted logs

# Core Moves

1. Identify the artifact, design-system source refs, scope, and non-goals.
2. Compare only source-backed primitives: tokens, components, layout rules, content rules, examples, or approved screenshots.
3. Classify observations as aligned, intentional exception, candidate issue, candidate pattern, unavailable, or human review required.
4. Apply the Pattern Generalization Gate before recommending any reusable pattern review.
5. Return a compact review with source refs, evidence gaps, owner-review needs, and a safe next step.

# Optional Modules

- **Pulso pilot mode** — Use when the declared reference is Pulso. Treat Pulso as the review source for this artifact only; do not create a structural dependency or import a package.
- **Accessibility evidence check** — Use when state colors, density, focus, contrast, motion, or interaction affordances affect usability or risk.
- **Pattern candidate review** — Use when a repeated choice appears reusable. Require comparable examples, source refs, owner review, and known counterexamples before recommending promotion.
- **Observation return** — Use when the review should be visible in AletheIA, Resource Observatory, or a Work Slice reconcile.

# Activation Triggers

- Use Pulso pilot mode when the artifact references Pulso tokens, Pulso docs, or Pulso-aligned UI decisions.
- Use accessibility evidence check when a finding touches contrast, keyboard focus, semantics, density, readability, or motion.
- Use pattern candidate review when the same design choice appears in more than one comparable artifact.
- Use observation return when the review is part of a governed slice or will inform a design-system owner.

# Expected Output

- design-system source refs used
- artifact refs reviewed
- conformance observations and confidence
- candidate findings with source refs and severity
- Pattern Generalization Gate outcome
- unavailable evidence or owner-review needs
- recommended next safe step

# Verification

- Every material claim has `source_refs` or is marked `unavailable`.
- The review does not treat generated UI, screenshots, or statistics as normative by themselves.
- Candidate patterns are not promoted without owner review and comparable evidence.
- Restricted source content is referenced by metadata, hash, or authorized summary only.
- The output separates conformance, issue, pattern candidate, and human decision.
- The skill did not add dependencies, scanners, routing engines, or remediation authority.

# Handoff Signals

- design-system source refs are missing or contradictory
- accessibility, brand, product, legal, or owner approval is required
- pattern promotion is requested without comparable evidence
- the artifact appears to fork the design system silently
- the review needs automation beyond a bounded manual pass

# Pairs Well With

- `ux-strategy`
- `heuristic-audit`
- `qa-review`
- `restricted-context-check`
- `checkpoint-review`

# Anti-patterns

- Treating a design-system review as design approval.
- Promoting a reusable pattern from one example or a percentage alone.
- Importing a design-system package just because the review mentions it.
- Copying restricted design-system content into logs or examples.
- Turning a manual review into a scanner, router, or remediation engine.
