# Self-service documentation checklist

Use this checklist for substantial documentation creation, restructuring, or audit work. Skip it for small editorial corrections that do not change the reader journey, evidence, procedures, navigation, or publication surface.

## Reader and outcome

- [ ] Name the novice, practitioner, advanced, and maintainer readers that materially differ.
- [ ] State the task or decision each reader needs to complete.
- [ ] Record prerequisite knowledge, access, permissions, tools, and setup.
- [ ] Define the first useful result and how the reader verifies it.
- [ ] Identify predictable failures and the support dependency the documentation should reduce.
- [ ] Preserve an escalation path for problems that documentation cannot safely resolve.

## Sources and boundaries

- [ ] Identify the canonical source for behavior, contracts, terminology, constraints, and claims.
- [ ] Separate delivered behavior, evidence, examples, guidance, proposals, and deferred work.
- [ ] Label synthetic, conceptual, aspirational, version-specific, or unverified material.
- [ ] Do not use documentation to invent a missing product, architecture, security, legal, or ownership decision.

## Journey and architecture

- [ ] Provide a visible path from orientation to first success.
- [ ] Connect first success to recurring use, troubleshooting, reference, and deeper explanation.
- [ ] Assign one primary Diátaxis type to each page: tutorial, how-to guide, reference, or explanation.
- [ ] Create one canonical explanation per major concept and link to it from adjacent pages.
- [ ] Give advanced readers a direct route to reference, contracts, decisions, and limitations.
- [ ] Preserve stable public routes or define redirects and compatibility links before moving content.

## Storytelling and explanation

- [ ] Lead with the useful answer instead of a long history or index.
- [ ] Use context, problem, consequence, mental model, action, and result only when they improve understanding.
- [ ] Keep examples concrete and clearly distinguish them from delivered evidence.
- [ ] End conceptual sections with the decision, action, or next page they enable.
- [ ] Do not force experienced readers through introductory narrative.

## Procedural clarity

- [ ] Use one consistent term for each important object, state, and action.
- [ ] State prerequisites and conditions before the step that depends on them.
- [ ] Give each step one primary action and use direct, active instructions.
- [ ] Keep sentences short enough to prevent hidden conditions or multiple interpretations.
- [ ] Show the expected result after consequential steps.
- [ ] State stop conditions, warnings, rollback, recovery, or escalation where failure matters.
- [ ] Apply equivalent clear-language principles in the document's language.

These checks are inspired by controlled technical writing. They do not implement the official ASD-STE100 writing rules or controlled English dictionary. Do not claim ASD-STE100 compliance unless the project explicitly adopts the [official standard](https://asd-ste100.org/), controlled vocabulary, training, and validation process.

## Self-service verification

- [ ] A novice can explain what the system is, why it matters, and complete the first safe task.
- [ ] A practitioner can complete a recurring task without guessing hidden prerequisites.
- [ ] A reader can recognize success and recover from at least the predictable failure paths.
- [ ] An advanced reader can bypass basics and find precise reference material.
- [ ] A maintainer can identify ownership, canonical sources, rationale, and freshness boundaries.

## Publication and maintenance

- [ ] Titles, headings, navigation, link labels, and alt text remain understandable when scanned.
- [ ] Links resolve to rendered pages or intentional external sources.
- [ ] Commands, code, screenshots, routes, and examples match the current version or state their limits.
- [ ] Accessibility, terminology, tone, and contribution rules follow canonical project standards.
- [ ] The validation report lists checks run, failures, warnings, unresolved evidence, and follow-ups.
