# Premortem — Depth Profiles

Three profiles. Use the smallest one that still makes the decision reviewable.

## Lite

**Use when:** risk is low or medium, decision is reversible, impact is limited, a quick check is enough.

**Output:** 3–5 failure modes, main hidden assumption, most important plan adjustment.

**Signals that Lite is not enough:** involves AI/autonomy/agents; risk to data, security, or compliance; direct user impact; reputational risk; decision is hard to reverse; multiple stakeholders disagree on what success looks like.

---

## Standard

**Use when:** a feature, product, campaign, process, or strategy has real impact; there is meaningful cost of error; dependencies exist across areas; uncertainty about adoption, value, or execution.

**Output:** framing, context summary, 5–8 failure modes, most probable failure, most dangerous failure, hidden assumption, warning signals, recommended gates, revised plan, pre-execution checklist.

**Signals that Standard is not enough:** legal, security, privacy, or data-protection risk; impact on vulnerable users; low-reversibility decision; AI agent with operational autonomy; possible reputational damage; no rollback path; no verifiable success criterion.

---

## High-Assurance

**Use when:** cost of error is high; decision is hard or expensive to reverse; risk to security, data, governance, compliance, or reputation; critical user experience impact; AI with autonomy, recommendation, or operational action; conflict between deadline, quality, and risk; explicit human decision required.

**Output:** framing, structured context, detailed failure modes, severity/probability/detectability matrix, most probable failure, most dangerous failure, hardest-to-detect failure, critical hidden assumptions, measurable warning signals, hard gates, soft gates, review triggers, human decision gates, revised plan, pre-execution checklist, pending decisions.

**Signals that High-Assurance is excessive:** decision is simple and reversible; no meaningful impact; no critical dependencies; a longer analysis would delay more than it helps; a checklist resolves the risk.

---

## Quick selection rule

```
Low risk + reversible          → Lite
Medium risk + product/team impact  → Standard
High risk + AI/data/security/reputation/low reversibility → High-Assurance
```
