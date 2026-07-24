---
id: vc-documentation-mixed-corpus-audit-001
skill_id: documentation
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Audit a fictional documentation corpus before restructuring it for self-service use.
  context: The corpus has competing `/install-old` and `/install` pages, `/faq` last reviewed two years ago, a current `/api`, and a current but unlinked `/troubleshooting` page. `workspace` and `project` name the same concept, the architecture explanation appears on three pages, and external teams link to every current URL. Repository evidence confirms `/install` matches current behavior and identifies page owners, but no owner has authorized route removal.
expected_behavior:
  must_do:
    - Identify canonical sources, unsupported or stale claims, duplicate explanations, terminology conflicts, and reader-journey gaps.
    - Propose a progressive information architecture with one primary purpose per page and a visible troubleshooting path.
    - Preserve public routes or require redirects and owner approval before consolidation or removal.
    - Produce a validation report that separates failures, warnings, unresolved evidence, and ownership handoffs.
  must_not_do:
    - Rewrite or delete every page before resolving canonical sources and route ownership.
    - Select a canonical page based only on presentation quality or recency labels.
    - Treat current HTTP success as proof that links, content, and reader paths are correct.
acceptance_criteria:
  - The audit distinguishes content truth, information architecture, publication compatibility, and ownership decisions.
  - Duplicate content is mapped to a proposed canonical explanation with summaries or links from adjacent pages.
  - Route changes remain blocked on redirect or owner decisions while safe content corrections can proceed.
failure_signals:
  - The output recommends a broad rewrite without evidence or prioritization.
  - Existing public URLs are removed without compatibility handling.
  - Broken journeys, stale claims, and duplicate concepts are reported as one undifferentiated issue list.
notes: Synthetic edge case for source, journey, and publication-boundary auditing.
---

# Validation Case

## Scenario

A fictional corpus contains accurate and inaccurate pages, duplicated concepts, weak navigation, and public routes with external consumers. The documentation skill must improve the journey without confusing presentation quality with source authority or breaking compatibility.

## Why this expectation is correct

Documentation restructuring is both an editorial and publication-boundary task. Canonical truth, reader paths, redirects, ownership, and validation must remain explicit before content is consolidated or removed.

## How a reviewer checks it

Confirm that the audit separates evidence, journey, duplication, terminology, routes, and ownership. Fail the case if it proposes an unsupported rewrite, removes routes without compatibility, or lacks prioritized handoffs.
