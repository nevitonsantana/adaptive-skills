---
id: vc-documentation-multilevel-onboarding-001
skill_id: documentation
case_type: baseline
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Design the onboarding documentation for the fictional OrbitCLI command-line tool used by first-time operators, regular practitioners, and maintainers.
  context: Verified sources specify `orbit install`, the safe first task `orbit run sample`, success output `PASS sample-001`, recurring configuration in `~/.orbit/config.yml`, and `orbit doctor` for common failures. A command reference and maintainer architecture note exist. The current material is one long README ordered by implementation history.
expected_behavior:
  must_do:
    - Define distinct self-service outcomes and prerequisites for novice, practitioner, and maintainer readers.
    - Design a progressive journey from orientation and first success through recurring use, troubleshooting, reference, and deeper explanation.
    - Assign one primary Diátaxis type to each proposed page and provide direct advanced or maintainer shortcuts.
    - Preserve source-backed boundaries and define how readers verify the first successful result.
  must_not_do:
    - Treat the existing long README as the correct journey for every reader level.
    - Force maintainers through the complete beginner tutorial before exposing reference or architecture.
    - Invent product behavior, commands, permissions, or support guarantees that are not present in the context.
acceptance_criteria:
  - The output contains a reader map, progressive page map, first-success check, recovery path, and advanced shortcuts.
  - Each proposed page has one primary purpose and links to adjacent documentation types.
  - The novice path is safe and short while practitioner and maintainer paths remain directly accessible.
failure_signals:
  - The proposal is only a table of contents with no reader outcomes or task paths.
  - Every audience receives the same linear sequence.
  - The first task has no observable success condition or troubleshooting path.
notes: Synthetic baseline case for the self-service reader-journey contract.
---

# Validation Case

## Scenario

A fictional command-line tool has accurate source material but exposes it as one implementation-ordered README. The documentation skill must turn that material into a progressive onboarding and reference system for readers with different knowledge levels.

## Why this expectation is correct

The skill should reduce avoidable support dependency without flattening every reader into a beginner. Diátaxis classifies each page, while the self-service journey connects those pages from orientation through recovery and deeper material.

## How a reviewer checks it

Confirm that the output defines reader-specific outcomes, a short first-success path, recurring and troubleshooting paths, one primary type per page, and direct advanced access. Fail the case if it only reorganizes headings or invents unsupported behavior.
