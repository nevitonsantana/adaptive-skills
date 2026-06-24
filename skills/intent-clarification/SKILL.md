---
name: intent-clarification
description: Clarify the human-owned outcome, constraints, success, failure, and critical ambiguity before planning or execution without deciding intent for the human.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: planning
---

# Overview

Use this consultative skill when a request contains enough direction to discuss but not enough confirmed intent to plan or execute safely.

The skill helps a human make the intended outcome explicit. It separates desired outcomes from proposed implementation, identifies constraints and non-goals, defines success and failure, exposes critical ambiguity, and records what still needs human confirmation.

It does not choose intent, architecture, scope, priority, approval, or execution posture for the human. AletheIA or another governing system may consume its output as evidence, but the skill itself has no gate, Work Slice, or decision authority.

# When to Use

- The desired outcome is unclear, overloaded, or mixed with an assumed solution.
- Success or failure cannot yet be observed.
- Important constraints, non-goals, or connected intents are missing.
- Proceeding would require consequential guessing.
- A Work Slice needs human-owned Intent and Expectations before planning.
- Different participants appear to mean different things by the request.

# When NOT to Use

- Intent, success, failure, constraints, and ownership are already explicit enough to proceed.
- The task is a simple factual lookup or low-risk mechanical change.
- The human is asking for execution, not clarification, and no critical ambiguity remains.
- The real need is prioritization, architecture selection, risk analysis, or approval.
- Clarification would become an excuse to delay a safe, reversible next step.

# Core Moves

1. Restate the desired outcome without embedding an implementation choice.
2. Identify explicit constraints, non-goals, affected people or systems, and connected intents.
3. Define observable success and observable failure.
4. Separate human decisions from working assumptions and inferred context.
5. List evidence holes and mark unavailable information explicitly.
6. Rate guessing risk as low, medium, or high, with a short rationale.
7. Recommend one posture: proceed, clarify, or stop.
8. Ask only the smallest set of questions needed to resolve critical ambiguity.
9. Record human confirmation status and the source reference for any confirmed intent.

# Optional Modules

- **Outcome/solution split** — compare the requested result with the proposed implementation when solution fixation may hide the real need.
- **Expectation coverage** — map each success or failure expectation to the evidence that could later verify it.
- **Connected-intent check** — identify product, user, governance, system, or documentation intents that may conflict.
- **Assumption ledger** — label assumptions by owner, impact, reversibility, and confirmation need.
- **Clarification budget** — cap questions when ambiguity is low and a reversible experiment is safer than more discussion.

# Activation Triggers

- Use outcome/solution split when the request names a feature or technology but not the intended effect.
- Use expectation coverage when the output will feed an AletheIA Intent-to-Evidence extension.
- Use connected-intent check when more than one stakeholder, system, or policy boundary is affected.
- Use assumption ledger when one unverified assumption could materially change scope or risk.
- Use clarification budget when more than three questions are proposed for a reversible, low-risk task.

# Expected Output

Produce a compact clarification record containing:

- human-owned desired outcome
- constraints and non-goals
- observable success and failure
- connected intents, when relevant
- human decisions versus working assumptions
- evidence holes and unavailable information
- guessing-risk rating and rationale
- recommended posture: proceed, clarify, or stop
- critical clarification questions
- human confirmation status and source references

Use 'templates/intent-clarification-record.md' as the portable record shape.

# Verification

- The outcome describes a result, not merely an implementation.
- Success and failure are observable enough to support later evidence.
- Human decisions are not presented as agent conclusions.
- Assumptions and unavailable information are visibly distinct from confirmed facts.
- Questions are limited to ambiguities that materially affect outcome, risk, or validation.
- The recommended posture is advisory and justified.
- No approval, gate transition, architecture selection, or execution action is implied.

# Handoff Signals

- Human confirmation is missing for a critical decision — hand back for clarification.
- Guessing risk is high — stop before planning or execution.
- Intent is confirmed and expectations are observable — hand off to bounded planning or Work Slice formation.
- Multiple intents conflict — hand off to the responsible product or governance decision-maker.
- The request requires architecture, prioritization, or risk judgment — pair with the appropriate review skill rather than expanding this skill's authority.

# Pairs Well With

- 'feature-planning' — clarify human intent first, then shape a bounded executable slice.
- 'premortem' — clarify the intended outcome before stress-testing the plan.
- 'domain-language-alignment' — reconcile ambiguous terms that block intent confirmation.
- 'workflow' — carry confirmed intent into a bounded, reviewable execution flow.
- AletheIA Intent-to-Evidence — use the clarification record as consultative evidence, not as a gate decision.

# Anti-patterns

- Rewriting a vague request into a confident intent without human confirmation.
- Treating the proposed solution as the desired outcome.
- Asking exhaustive discovery questions when a small reversible step would suffice.
- Inventing success metrics, constraints, or stakeholder priorities.
- Using “proceed” as approval to execute.
- Letting the skill select architecture, create a Work Slice, pass a gate, or close evidence.
