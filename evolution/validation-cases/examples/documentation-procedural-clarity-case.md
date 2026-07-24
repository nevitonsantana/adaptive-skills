---
id: vc-documentation-procedural-clarity-001
skill_id: documentation
case_type: regression
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Rewrite a fictional installation and recovery procedure so a mixed-proficiency operations team can execute it safely.
  context: The source says to prepare the environment as usual, update the service and configuration, restart if needed, and check that everything looks correct. Verified evidence requires the `service-operator` role, `nova backup create` with its returned backup id recorded, `nova service update --version 4.2`, configuration of `/etc/nova/service.yml` only after `UPDATE READY`, `nova service restart`, and `nova health` returning exactly `status: healthy`. If update or restart fails, stop and run `nova backup restore <backup-id>`; if restore fails, do not retry and escalate to Platform Operations.
expected_behavior:
  must_do:
    - Replace implicit prerequisites and vague terms with source-backed conditions and consistent terminology.
    - Use one primary action per step with direct instructions and place conditions before dependent actions.
    - State the expected result, stop conditions, rollback or recovery, and escalation boundary.
    - Describe the approach as controlled procedural clarity rather than formal ASD-STE100 compliance.
  must_not_do:
    - Preserve phrases such as as usual, if needed, or looks correct without defining them.
    - Combine update, configuration, restart, verification, and rollback in one step.
    - Claim ASD-STE100 compliance or invent words from an official controlled dictionary.
acceptance_criteria:
  - Every consequential step has explicit prerequisites or conditions, one primary action, and an observable expected result.
  - Failure handling distinguishes retry, stop, rollback, and authorized escalation.
  - Terminology remains consistent and no formal controlled-language compliance claim appears.
failure_signals:
  - A reader must infer permissions, ordering, success, or failure recovery.
  - Passive or vague wording hides who performs an action.
  - The output presents STE-inspired principles as certification or standards compliance.
notes: Synthetic regression case for ambiguous procedural documentation.
---

# Validation Case

## Scenario

A fictional operations procedure is technically grounded but written with hidden prerequisites, bundled actions, vague success language, and no safe recovery path. The documentation skill must convert it into an executable procedure.

## Why this expectation is correct

Self-service documentation depends on readers knowing when they may act, what to do, what success looks like, and where to stop. Controlled-language principles improve this clarity, but they do not establish formal ASD-STE100 compliance.

## How a reviewer checks it

Inspect each step for explicit conditions, one primary action, direct wording, an expected result, and appropriate recovery. Fail the case if ambiguity remains or if the output claims compliance with ASD-STE100.
