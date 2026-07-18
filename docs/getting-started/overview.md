---
title: Adaptive Skills Overview
description: Understand what Adaptive Skills is, what problem it solves, how a skill works, and where it fits with AletheIA.
---

Adaptive Skills is a portable library of small capabilities for AI-assisted work. A capability is a reusable way to approach one kind of problem, such as clarifying intent, planning a feature, debugging a failure, reviewing an interface, testing a change, or handing work to another person or agent.

The library helps make AI-assisted work less improvised while keeping human judgment and project rules in control.

## The problem it solves

AI-assisted work often fails because the agent uses the wrong approach, hides assumptions, produces an output nobody can verify, or loses useful context after the session ends.

Adaptive Skills turns repeated working practices into inspectable `SKILL.md` files. Each skill explains:

- when it is useful;
- when it should not be used;
- the essential moves;
- optional depth for special situations;
- the output it should leave behind;
- how to verify that output.

## A simple example

Imagine that a team asks an AI agent to “build a new onboarding flow.” Different needs may be hidden inside that request:

| Dominant need | Appropriate skill |
|---|---|
| The intended outcome is unclear | `intent-clarification` |
| The feature needs a small delivery plan | `feature-planning` |
| The team wants to expose failure risks first | `premortem` |
| The interface needs usability review | `heuristic-audit` |
| The implementation needs proof | `testing` |
| Work must continue in another session | `handoff-summary` |

The goal is not to run all these skills. It is to choose the smallest one that improves the current decision or output.

## What Adaptive Skills is

Adaptive Skills is:

- a reusable capability library;
- readable by people and AI agents;
- installable in consumer projects;
- independent of any single product domain;
- usable with or without AletheIA;
- governed through explicit review and evolution records.

## What it is not

Adaptive Skills is not:

- an autonomous agent or runtime;
- a replacement for product, design, engineering, or business judgment;
- a project-management or approval system;
- a reason to add process to every task;
- a mechanism that silently changes its own skills.

A skill provides method and output discipline. The surrounding project or harness controls permissions, tools, approvals, and operational policy.

## How a skill works

Every skill follows a common shape:

1. **When to Use** identifies signals that the skill fits.
2. **When NOT to Use** prevents unnecessary or incorrect activation.
3. **Core Moves** defines the essential actions.
4. **Optional Modules** adds depth only when a matching condition exists.
5. **Expected Output** makes the result reviewable.
6. **Verification** defines the minimum proof before closure.
7. **Handoff Signals** explains when another capability or human decision is needed.

This model is called **Core + Modules + Triggers**. You do not need to understand the deeper architecture before using your first skill.

## Current library

The canonical library currently contains **34 generic skills across 11 categories**:

- engineering;
- design;
- planning;
- efficiency;
- cross-functional;
- product;
- business;
- governance;
- quality;
- metrics;
- docs.

The [skill catalog](https://nevitonsantana.github.io/adaptive-skills/getting-started/skill-catalog/) lists every skill, the signal that suggests using it, and its expected contribution.

## Use it standalone

Adaptive Skills works without AletheIA. Install one or more skills in a compatible AI environment, choose the capability that fits the task, and use its verification section before accepting the result.

This is the simplest adoption path.

## Use it with AletheIA

AletheIA and Adaptive Skills operate at different levels:

> AletheIA governs the work; Adaptive Skills provides reusable execution capabilities inside that work.

AletheIA may frame a Work Slice, require evidence, preserve continuity, or control a review gate. An Adaptive Skill may help plan, inspect, test, communicate, or return a structured observation. The skill does not take AletheIA's authority.

Read [AletheIA integration](https://nevitonsantana.github.io/adaptive-skills/aletheia-integration/) when you need this deeper operating model.

## Who should read what

| Reader | Recommended path |
|---|---|
| New to the project | Overview → Quickstart → First skill |
| Practitioner | Skill catalog → How to use a skill → Harness setup |
| Team adopting the library | Consumer adoption → First pilot → Evaluation checklist |
| Advanced reader | Skill model → Concepts → AletheIA integration |
| Maintainer | Evolution layer → Governance → ADRs |

## Risks and cautions

- Do not use a skill when its “When NOT to Use” section matches the task.
- Do not assume a skill grants access to tools, files, secrets, or external systems.
- Do not copy project-specific policy into the generic library.
- Do not treat a polished AI response as evidence that the skill succeeded.
- Do not activate several skills when one is enough.

## Next steps

1. [Complete the quickstart](https://nevitonsantana.github.io/adaptive-skills/getting-started/quickstart/).
2. [Run your first skill](https://nevitonsantana.github.io/adaptive-skills/getting-started/first-skill/).
3. [Browse the complete catalog](https://nevitonsantana.github.io/adaptive-skills/getting-started/skill-catalog/).
4. [Read the FAQ](https://nevitonsantana.github.io/adaptive-skills/getting-started/faq/) if you have adoption or installation questions.
