---
name: documentation
description: Plan, write, restructure, and validate self-service technical documentation for products, systems, APIs, libraries, and internal tools. Use when creating onboarding, manuals, tutorials, how-to guides, reference pages, explanations, troubleshooting, FAQs, changelogs, migration paths, or audience-aware documentation systems; when auditing navigation, terminology, freshness, links, or unsupported claims; or when turning a mixed corpus into progressive paths for novice, practitioner, advanced, and maintainer readers.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: docs
---

# Overview

Use this skill to make documentation understandable, findable, accurate, and actionable for readers with different levels of knowledge. Treat documentation as a self-service interface: help each reader understand the minimum necessary context, complete a useful task, verify the result, recover from predictable failure, and reach deeper material without depending on avoidable technical support.

Self-service means reducing avoidable dependency, not promising that documentation can replace every support, product, security, or ownership decision.

# When to Use

- create or restructure onboarding, manuals, tutorials, how-to guides, reference, explanation, troubleshooting, FAQ, or migration content
- design progressive paths for novice, practitioner, advanced, or maintainer readers
- plan a multi-page documentation system or improve its information architecture
- audit a documentation site or repository for broken journeys, weak recovery, duplicate content, stale claims, mixed terminology, or unsafe links
- document a release, changelog, roadmap, decision, contract, or evidence record
- make procedures clearer for international or mixed-proficiency audiences

# When NOT to Use

- implement product behavior, runtime logic, or a documentation platform without a separate engineering task
- invent capabilities, metrics, outcomes, integrations, or security guarantees that lack source evidence
- use documentation to replace a missing product decision, API contract, support channel, or owner approval
- rewrite every document when a focused correction or canonical pointer is sufficient
- claim formal compliance with a controlled-language standard without the standard, vocabulary, training, and validation required by that project

# Core Moves

1. Define the reader map and self-service outcome: identify each reader's goal, task, prerequisite knowledge, likely failure, consequence of misunderstanding, and what they should be able to do without avoidable support.
2. Ground the content in canonical sources. Separate delivered behavior, evidence, examples, advisory guidance, proposals, and deferred work; do not resolve missing product or technical decisions through prose.
3. Design the progressive journey across pages or sections: orientation, first successful result, recurring use, troubleshooting, reference, and deeper explanation. Classify each page by one primary Diátaxis type — tutorial, how-to guide, reference, or explanation — and connect adjacent types instead of mixing every purpose into one page.
4. Draft for understanding and action. Lead with the answer, use concrete examples, and apply technical storytelling only where it improves orientation: context, problem, consequence, mental model, action, and result. For procedures, make prerequisites, conditions, actions, expected results, and recovery explicit.
5. Verify the complete reader paths and publication surface. Confirm that novices can start safely, practitioners can complete and recover, advanced readers can skip basics, maintainers can find contracts and rationale, and links, routes, terminology, accessibility, freshness, and ownership remain trustworthy.

# Optional Modules

- **Reader journey and self-service** — map reader levels, entry points, first success, recurring tasks, predictable failures, recovery, escalation, and advanced shortcuts.
- **Document system and information architecture** — inventory content, assign one primary purpose per page, identify canonical explanations, group related pages, order navigation, and preserve stable routes or redirects.
- **Technical storytelling and explanation** — use a proportionate context-to-result arc to explain why something matters, how it works, and what the reader should do next without delaying the answer.
- **Controlled procedural clarity** — use consistent terms, short sentences, one primary action per step, direct instructions, conditions before actions, expected results, and recovery. These principles are inspired by controlled technical writing and do not establish ASD-STE100 compliance.
- **Editorial governance and terminology** — follow the project's language, tone, glossary, accessibility rules, contribution process, evidence boundaries, and current implementation.
- **Release and change documentation** — inspect the relevant version-control range, identify user impact and breaking changes, and produce a technical record plus a reader-facing summary linked to canonical detail.
- **Publication QA** — check rendered routes, links, headings, titles, accessibility, code examples, screenshots, freshness, unsupported claims, and maintenance ownership.

# Activation Triggers

- Activate **reader journey and self-service** when documentation must support multiple knowledge levels, reduce recurring support dependency, or guide readers from orientation through recovery.
- Activate **document system and information architecture** when readers cannot predict where to start, pages mix purposes, explanations are duplicated, or navigation mixes audiences.
- Activate **technical storytelling and explanation** when readers need context, rationale, a mental model, or consequences before they can act correctly.
- Activate **controlled procedural clarity** for setup, operations, manuals, troubleshooting, safety-sensitive steps, or international and mixed-proficiency audiences.
- Activate **editorial governance and terminology** when the project provides a style guide, glossary, contribution policy, accessibility standard, or canonical implementation.
- Activate **release and change documentation** when a release, milestone, migration, or commit range must be translated into user-visible impact. Inspect source history and diffs; do not infer the narrative from filenames or commit titles alone.
- Activate **publication QA** before publication, after navigation or route changes, or when users report broken links, raw Markdown, duplicate titles, stale content, or inaccessible material.

# Expected Output

- a reader map with self-service goals, prerequisites, likely failures, and advanced shortcuts
- a progressive documentation journey and one primary Diátaxis type per page
- for substantial work, an agreed outline or documentation-system map before the full draft
- source-backed content with explicit examples, boundaries, procedures, expected results, recovery, and next steps
- canonical links and compatibility paths for moved or consolidated content
- a validation report covering reader-path success, failures, warnings, checks run, and follow-ups

# Verification

- A novice can identify what the system is, why it matters, and the first safe action.
- A practitioner can complete the documented task and handle predictable failures without guessing hidden prerequisites.
- An advanced reader can bypass introductory material and reach reference, contracts, decisions, evidence, and limitations directly.
- A maintainer can identify the canonical source, content owner, version or freshness boundary, and rationale for consequential guidance.
- Each procedure states prerequisites or conditions, one primary action per step, the expected result, and what to do when the result differs.
- Storytelling improves orientation or understanding without delaying the answer, obscuring evidence, or forcing experts through a beginner path.
- Internal links resolve to rendered pages or intentional external sources; public links do not accidentally expose raw repository content.
- Examples, metrics, maturity claims, security statements, and integrations are source-backed and labeled when synthetic or aspirational.
- Code, commands, screenshots, navigation, terminology, tone, and accessibility reflect the current implementation and project standards or explicitly state their version and limits.

# Handoff Signals

- The documentation exposes a product ambiguity that requires product or architecture ownership.
- A claim cannot be verified from the repository, a canonical source, or an approved evidence record.
- A URL move requires redirect, release, or publication ownership outside the current slice.
- The requested page needs a runtime, schema, API, data, permission, or support-process change rather than documentation alone.
- A terminology, safety, legal, or compliance conflict requires an authorized owner before writing can proceed.

# Pairs Well With

- `ux-writing`
- `domain-language-alignment`
- `architecture-review`
- `knowledge-source-evaluation`
- `handoff-summary`
- `qa-review`
- `testing`

# Anti-patterns

- Starting with a long index or narrative instead of the reader's goal and first useful answer.
- Treating a single long tutorial as the journey for every reader level.
- Forcing advanced readers through introductory content before exposing reference or contracts.
- Repeating the same concept across guides, reference pages, FAQs, and onboarding instead of using a canonical explanation.
- Treating a screenshot, mockup, synthetic example, roadmap item, or attractive story as implementation evidence.
- Hiding prerequisites, permissions, stop conditions, expected results, failure states, recovery, escalation, or ownership boundaries.
- Claiming ASD-STE100 compliance because a document uses short sentences, active voice, or consistent terminology.
- Drafting a large document before agreeing on its audience, primary type, scope, source material, and outline.
- Treating commit titles as a complete release narrative without checking the actual diff, affected behavior, and user impact.
- Changing public routes without checking backlinks, navigation, redirects, rendered pages, and the live site.
