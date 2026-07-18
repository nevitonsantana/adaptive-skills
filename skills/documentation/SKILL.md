---
name: documentation
description: Plan, write, reorganize, and validate technical documentation for products, systems, APIs, libraries, and internal tools. Use when creating guides, reference pages, architecture documentation, FAQs, changelogs, migration paths, documentation information architecture, or audience-aware content; when auditing links, headings, navigation, terminology, freshness, or unsupported claims; or when turning a mixed document corpus into a progressive reader journey.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: docs
---

# Overview

Use this skill to make documentation understandable, findable, accurate, and actionable for readers with different levels of knowledge. Treat documentation as an interface: establish the reader's goal, expose the minimum useful path, preserve source-backed truth, and provide a clear next step.

# When to Use

- create or restructure product, technical, API, architecture, or process documentation
- design progressive journeys for beginners, practitioners, advanced readers, or maintainers
- write installation, quickstart, how-to, reference, troubleshooting, FAQ, or migration content
- audit a documentation site or repository for broken links, duplicate titles, stale claims, mixed terminology, or weak navigation
- convert a flat or mixed corpus into an information architecture with canonical pages
- document a release, changelog, roadmap, decision, contract, or evidence record

# When NOT to Use

- implement product behavior, runtime logic, or a documentation platform without a separate engineering task
- invent capabilities, metrics, outcomes, integrations, or security guarantees that lack source evidence
- use documentation to replace a missing product decision, API contract, or owner approval
- rewrite every document when a focused correction or canonical pointer is sufficient

# Core Moves

1. Identify the audience, task, decision, prerequisite knowledge, and consequence of misunderstanding.
2. Establish the source of truth and classify the page as overview, guide, reference, concept, case/evidence, update, or maintainer material.
3. Design the shortest progressive path: orientation, first successful action, deeper explanation, reference, and next step.
4. Write the answer before the background. Use plain language, concrete examples, explicit prerequisites, and visible boundaries.
5. Separate delivered behavior, advisory guidance, evidence, examples, proposals, and deferred work.
6. Create one canonical explanation for each major concept; replace duplicates with summaries and links.
7. Match the format to the reader task: cards for choices, steps for procedures, tabs for equivalent variants, accordions for optional detail, tables for comparison, and diagrams only when they clarify relationships.
8. Preserve stable URLs where practical and define redirects or compatibility links before moving public pages.
9. End guides with contextual next steps, troubleshooting or failure recovery, and a verification path.

10. Classify the document using the Diátaxis model before drafting:
    - **Tutorial** — a learning-oriented path that helps a new reader achieve a first result.
    - **How-to guide** — a task-oriented procedure for a reader who already understands the basics.
    - **Reference** — precise, lookup-oriented information such as APIs, configuration, commands, or contracts.
    - **Explanation** — concepts, architecture, rationale, trade-offs, and boundaries.
    Use one primary type per page; link to adjacent types instead of mixing all purposes into one document.
11. For substantial documents, use an outline gate: confirm audience, document type, scope, source material, and proposed headings before writing the full draft. Skip the gate only for small corrections or tightly scoped reference updates.

# Optional Modules

- **Information architecture** — inventory documents, classify audiences, group pages, define canonical routes, and order navigation.
- **Beginner journey** — create What it is, why it matters, quickstart, installation, first task, FAQ, and boundaries.
- **Practitioner journey** — create task selection, workflow recipes, configuration, integration, adoption, and troubleshooting.
- **Advanced and maintainer reference** — organize concepts, contracts, ADRs, architecture, governance, evidence, and evolution.
- **Release communication** — turn technical changes into concise changelog summaries with links to the canonical record.
- **Editorial standards** — follow the project's official language, tone, terminology, contribution rules, and current implementation rather than generic assumptions.
- **Changelog and release notes** — inspect the relevant version-control range, classify changes, identify breaking changes, separate user impact from maintenance work, and produce both a technical record and a reader-facing summary.
- **Documentation QA** — check links, routes, headings, titles, language, accessibility, freshness, code examples, and unsupported claims.

# Activation Triggers

- Activate **information architecture** when readers cannot predict where to start or public navigation mixes audiences.
- Activate **beginner journey** when a new user cannot explain the product or complete a first safe task.
- Activate **practitioner journey** when users understand the product but cannot apply it to a real task.
- Activate **advanced and maintainer reference** when concepts, contracts, decisions, or operational limits are hard to locate.
- Activate **release communication** when a merge, version, or material behavior change needs a reader-facing update.
- Activate **editorial standards** when the repository provides a style guide, contribution process, terminology policy, or canonical implementation that the document must follow.
- Activate **changelog and release notes** when a release, milestone, or commit range needs to be translated into user-facing impact. Inspect version-control history before drafting; do not infer changes from filenames alone.
- Activate **documentation QA** before publication, after navigation changes, or when users report broken links, raw Markdown, duplicate titles, or stale content.

# Expected Output

- a documented audience and reader journey
- a primary Diátaxis document type and, for substantial work, an approved outline
- a clear page structure or information-architecture proposal
- accurate content with explicit prerequisites, examples, boundaries, and next steps
- canonical links and compatibility paths for moved or consolidated content
- a validation report listing checks run, failures, warnings, and follow-ups

# Verification

- A beginner can identify what the system is, why it matters, and the first safe action.
- A practitioner can complete the documented task without guessing missing prerequisites.
- Advanced readers can reach concepts, contracts, decisions, evidence, and limitations predictably.
- Every public page has a clear purpose, one visible title, useful headings, and a contextual next step.
- Internal links resolve to rendered pages or intentional external sources; links do not accidentally expose raw Markdown.
- Examples, metrics, maturity claims, security statements, and integrations are source-backed and labeled when synthetic or aspirational.
- Code, commands, screenshots, and navigation reflect the current implementation or explicitly state their version and limits.
- Changelogs and release notes distinguish user-visible changes, breaking changes, fixes, documentation-only work, and deferred or unsupported claims.
- Project-specific terminology, tone, and contribution requirements are followed when a canonical source exists.

# Handoff Signals

- The documentation exposes a product ambiguity that requires product or architecture ownership.
- A claim cannot be verified from the repository, a canonical source, or an approved evidence record.
- A URL move requires redirect, release, or publication ownership outside the current slice.
- The requested page needs a runtime, schema, API, or data change rather than documentation alone.
- A terminology conflict requires a domain or governance decision before writing can proceed.

# Pairs Well With

- `ux-writing`
- `domain-language-alignment`
- `architecture-review`
- `knowledge-source-evaluation`
- `handoff-summary`
- `qa-review`
- `testing`

# Anti-patterns

- Starting with a long index instead of a reader goal.
- Repeating the same concept across guides, reference pages, and FAQs.
- Treating a screenshot, mockup, synthetic example, or roadmap item as implementation evidence.
- Hiding prerequisites, permissions, stop conditions, failure states, or ownership boundaries.
- Using attractive language to compensate for unclear structure or unsupported claims.
- Drafting a large document before agreeing on its audience, primary document type, scope, and outline.
- Treating commit titles as a complete release narrative without checking the actual diff, affected behavior, and user impact.
- Publishing links that open repository Markdown when a rendered documentation route exists.
- Changing public routes without checking backlinks, navigation, redirects, and the live site.
