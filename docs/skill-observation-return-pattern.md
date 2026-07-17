---
title: Observation and evidence return
description: Return compact source-backed skill observations without taking authority over AletheIA Work Slices.
---

## Goal

Define how an Adaptive Skill can return a compact, source-backed observation to an AletheIA-compatible harness without becoming an authority over Work Slice gates, decisions, or closure.

This is a portable return pattern, not a required runtime API. Skills remain useful without AletheIA, and a consumer may serialize the same meaning as YAML, JSON, structured Markdown, or another reviewable format.

## Boundary

- The skill supplies method, result, evidence references, risks, and a handoff signal.
- The harness records execution evidence and preserves any governed recovery pointer.
- AletheIA interprets the observation inside Work Slice governance.
- The skill does not approve, block, close, restart, or mutate a Work Slice.
- The Resource Observatory may project the return read-only; it must not infer missing fields.

The authoritative source remains the referenced execution, artifact, knowledge record, or user input. A compact return is a decision-support observation, not replacement evidence.

## Minimum return

```yaml
version: "0.1"
observation_id: <stable-observation-id>
work_slice_id: <work-slice-id>
skill:
  id: <skill-id>
  mode: <generic|knowledge_aware|execution_only>
  execution_profile: <consumer-profile-or-unavailable>
  modules_used: []
result:
  observation_class: <planning|decision_support|validation|review|handoff>
  outcome: <usable|partial|failed|unknown|unavailable>
  compact_summary: <what-matters-for-the-next-decision>
evidence_used:
  - type: <artifact|user_input|runtime_output|knowledge_pack|source_record>
    ref: <authoritative-reference>
    scope: <metadata|capsule|excerpt|full|unavailable>
risks: []
handoff:
  signal: <continue|review|escalate|stop|restart_ready|unavailable>
  reason: <why-this-signal-was-returned>
recovery:
  lossiness: <lossless|lossy_with_recovery|unavailable>
  pointer: <governed-pointer-or-null>
  sensitivity: <public|internal|confidential|restricted>
metrics:
  raw_output_size:
    value: null
    provenance: unavailable
source_refs:
  - <skill-execution-record>
```

## Recovery invariant

If `recovery.lossiness` is `lossy_with_recovery`, `recovery.pointer` is mandatory and must resolve through an authorized evidence surface. `lossy_without_recovery` is invalid.

The pointer may reference a local artifact, CI artifact, runtime trace, or source record. It must not embed prompts, secrets, personal data, or restricted source content.

## Unavailable values

Skills must not invent missing measurements, evidence, recovery, outcome, or handoff data. Optional token, cost, size, or compression values use one provenance:

- `reported`
- `estimated`
- `unavailable`

When unavailable, use `value: null` and preserve the reason when it matters to the next decision.

## Result and authority

`result.outcome` describes whether the skill produced a usable method output. It does not prove that the Work Slice succeeded.

`handoff.signal` is advisory. AletheIA or the governing consumer decides whether to continue, review, stop, or close based on gates and authoritative evidence.

## Progressive use

A consumer may render the same return at different depths:

- guided: summary, impact, and review need;
- practitioner: evidence, risk, outcome, and handoff;
- engineer: modules, recovery pointer, lossiness, and available metrics.

No rendering depth may hide an escalation signal or failed outcome.

## Validation checklist

- stable observation, Work Slice, and skill identifiers are present;
- result and handoff remain distinct;
- evidence and source references are explicit;
- lossy output has a governed recovery pointer;
- missing metrics remain unavailable;
- restricted content is metadata-only or an authorized summary;
- the record claims no gate, execution, or decision authority.

## Related material

- [AletheIA integration](aletheia-integration/)
- [Using skills inside harnesses](using-skills-inside-harnesses/)
- [Harness requirements for skills](harness-requirements-for-skills/)
- [AletheIA Observation Governance Contract](https://nevitonsantana.github.io/AletheIA/contracts/observation-governance-contract/)
