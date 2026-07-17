---
title: "Validation Case Guidelines"
description: "Reference documentation for Validation Case Guidelines in Adaptive Skills."
---

A **validation case** is a concrete, reproducible expectation for a skill: given an input
and context, what the skill *must do* and *must not do*, and how you would know it
succeeded or failed.

Validation cases are the unit of evidence the
[Skill Evolution Validation Layer](https://nevitonsantana.github.io/adaptive-skills/evolution/optimization-boundaries/) runs experiments against.

## Synthetic-first

Cases must use **synthetic, public, or explicitly authorized** material. This is a hard
rule, not a preference. When in doubt, invent a fictional but realistic scenario.

| You may use                         | You must NOT use                                   |
| ----------------------------------- | -------------------------------------------------- |
| a synthetic / fictional scenario    | full confidential source content                   |
| a public source                     | raw proprietary content                            |
| an explicitly authorized pack       | customer data                                      |
| a fictional capsule                 | real internal policy without authorization         |
| simulated metadata                  | a snippet copied from a restricted source          |

## Declaring sensitivity

Every case **must** declare `sensitivity`:

| value          | meaning                                          | content rule                          |
| -------------- | ------------------------------------------------ | ------------------------------------- |
| `public`       | openly shareable                                 | raw content allowed                   |
| `synthetic`    | invented for the case                            | raw content allowed (it's fictional)  |
| `internal`     | internal but non-sensitive                       | prefer paraphrase; no secrets         |
| `confidential` | sensitive                                        | **capsule/synthetic only, no raw**    |
| `restricted`   | access-controlled                                | **capsule/synthetic only, no raw**    |
| `regulated`    | legally/contractually controlled                 | **capsule/synthetic only, no raw**    |

For `confidential`, `restricted`, or `regulated`, the case must also set
`source_policy: synthetic_only` and `capsule_only: true`. The validator rejects these
sensitivities otherwise. Represent the governed source only as **simulated metadata** or
a **fictional capsule** — never as a copied excerpt.

## Knowledge-aware skills

Some skills reason over governed knowledge (e.g. `knowledge-source-evaluation`,
`restricted-context-check`, `knowledge-conflict-resolution`). For any case or experiment
involving a knowledge-aware skill:

- the case must be synthetic, public, or explicitly authorized;
- restricted sources may appear **only** as simulated metadata or a fictional capsule;
- no full confidential source may appear in any experiment artifact;
- the related experiment must set `human_review_required: true`.

## Anatomy of a validation case

See [`../../evolution/validation-cases/templates/validation-case-template.md`](https://github.com/nevitonsantana/adaptive-skills/blob/main/evolution/validation-cases/templates/validation-case-template.md).
Required frontmatter fields:

- `id`, `skill_id`, `case_type`, `sensitivity`, `source_policy`
- `input.task`, `input.context`
- `expected_behavior.must_do`, `expected_behavior.must_not_do`
- `acceptance_criteria`, `failure_signals`

`case_type` is one of: `baseline`, `regression`, `edge_case`, `knowledge_aware`.

## Writing good cases

- **One clear expectation per case.** If you are testing two behaviors, write two cases.
- **Make failure observable.** `failure_signals` should be things a reviewer can spot in
  output, not vague qualities.
- **Prefer cases tied to real observations.** Link `related_observations` when the case
  came from a real usage signal in `evolution/observations/`.
- **Keep it small.** A case is evidence, not a benchmark suite. Few strong cases win.
