# Lean Implementation — synthetic example

## Scenario

A documentation page has one stale link to a renamed contract. The plan is already confirmed: update the link, do not rewrite the page, and validate references.

## Skill activation

- **Selected skill:** `lean-implementation`
- **Reason:** the implementation target is clear and the main risk is scope expansion.
- **Modules selected:** `contract change guard`, `observation return`
- **Modules rejected:** `safety exception escalation` — no security, accessibility, privacy, data integrity, or human-approval issue was introduced.

## Core moves applied

1. Smallest acceptable change: replace one stale contract link.
2. Existing pattern inspected: neighboring links use relative Markdown paths.
3. Coherent change: one link updated; no copy rewrite.
4. Validation: Markdown link inspection and repository governance check.
5. Handoff: changed file, reason, validation, gaps, next step.

## Observation-compatible result

```yaml
skill_result:
  skill_id: lean-implementation
  work_ref: synthetic-doc-link-slice
  changed_surfaces:
    - docs/example-page.md
  validation:
    - command: markdown-link-inspection
      result: passed
    - command: governance-check
      result: passed
  unavailable:
    - runtime_cost
    - user_acceptance
  boundary_notes:
    - no runtime or policy decision changed
    - no broad refactor performed
  next_safe_step: reviewer confirms the link target is the intended source
```

## Failure signals avoided

- rewriting unrelated sections;
- adding a new docs convention;
- claiming validation that was not run;
- treating the skill as authority to close the Work Slice.
