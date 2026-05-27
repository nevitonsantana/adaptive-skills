# Adaptive Skills — Skill Catalog

A navigable reference of all 24 published skills, organized by category, with trigger signals, brief descriptions, and composite flows for common task types.

**How to use this catalog:**  
Start from the task, not from the list. Identify the dominant need of the work, then find the skill that fits that need. The composite flows section at the bottom shows how multiple skills combine for common task types.

---

## Skill index by category

### Engineering

| Skill | Trigger signal | One-line description |
|---|---|---|
| [`workflow`](#workflow) | Starting non-trivial work; returning from a handoff | Frame the task with explicit scope, proof, and next step before execution starts |
| [`feature-planning`](#feature-planning) | New feature; redesign with behavior changes; staged delivery | Turn a feature request into a small, testable delivery plan |
| [`testing`](#testing) | Before closing meaningful work; after a bug fix; behavior change | Choose the minimum reliable proof for a change |
| [`debugging`](#debugging) | Runtime bug; failing test; inconsistent behavior | Reproduce, isolate, fix, and guard against recurrence |
| [`api-design`](#api-design) | Designing or reviewing a contract between components | Shape a clear, stable API contract before implementation |
| [`refactoring`](#refactoring) | Improving structure without changing behavior | Restructure code with explicit scope and a safety net |
| [`architecture-review`](#architecture-review) | Evaluating a design decision with long-term consequences | Surface tradeoffs, risks, and alternatives before committing |
| [`code-style`](#code-style) | Code review; style inconsistency; style guide creation | Enforce consistent style with explicit criteria, not instinct |
| [`communication`](#communication) | Writing an update, decision, or explanation for a mixed audience | Shape technical communication for the right audience and purpose |

### Design

| Skill | Trigger signal | One-line description |
|---|---|---|
| [`ux-strategy`](#ux-strategy) | Framing a new product experience; direction-setting session | Define the experience goal before UI decisions are made |
| [`ux-provocation`](#ux-provocation) | Design review; design that feels safe or predictable | Challenge design assumptions to surface stronger alternatives |
| [`heuristic-audit`](#heuristic-audit) | Evaluating an existing UI for usability gaps | Review an interface against established usability heuristics |
| [`ux-writing`](#ux-writing) | UI copy; error messages; labels; onboarding content | Improve product language for clarity, tone, and intent |

### Planning

| Skill | Trigger signal | One-line description |
|---|---|---|
| [`premortem`](#premortem) | Consequential plan; launch; commitment; high cost of failure | Assume failure already happened; work backwards to causes |

### Efficiency

| Skill | Trigger signal | One-line description |
|---|---|---|
| [`task-chunking`](#task-chunking) | Large or unclear scope; work that could sprawl | Break a large task into explicitly bounded slices |
| [`checkpoint-review`](#checkpoint-review) | Long session; task changed shape mid-round; continue-or-stop decision | Insert a deliberate pause before the next move |
| [`handoff-summary`](#handoff-summary) | Session ending; switching agents or people; boundary crossing | Package state so the next operator starts without re-deriving context |

### Cross-functional

| Skill | Trigger signal | One-line description |
|---|---|---|
| [`triad-check`](#triad-check) | Decision crossing product, design, and engineering; hard-to-reverse change | Surface all three perspectives before committing |

### Business

| Skill | Trigger signal | One-line description |
|---|---|---|
| [`business-design`](#business-design) | Strategic framing; value logic; operating model decisions | Frame the business logic behind a product or initiative |

### Quality

| Skill | Trigger signal | One-line description |
|---|---|---|
| [`qa-review`](#qa-review) | Pre-release readiness; cross-layer review; quality gate | Review for correctness, completeness, and edge cases |

### Metrics

| Skill | Trigger signal | One-line description |
|---|---|---|
| [`observability-review`](#observability-review) | Adding telemetry; reviewing instrumentation; deciding what to measure | Design observable, decision-linked signals |

---

## Skill details

### workflow

**When to use:** Starting a non-trivial task. Returning from a handoff or session compaction. Work that can sprawl across multiple files or decisions.

**When NOT to use:** Simple, single-step tasks. Quick lookups. Work where you already have a clear, short execution path.

**Core moves:**
1. State the goal in one sentence.
2. Declare the scope boundary — what is in and what is not.
3. State the proof required to close the task.
4. Name the next concrete step.

**Good first skill for:** any session where the task is unclear or the agent might drift.

---

### feature-planning

**When to use:** New feature work. Functional redesign with behavior changes. Work that needs staged delivery.

**When NOT to use:** Bug fixes (use `debugging`). Pure refactoring (use `refactoring`). Exploratory spikes where the output is learning, not a deliverable.

**Core moves:**
1. Identify the smallest useful slice.
2. State success criteria.
3. Surface risks and dependencies explicitly.
4. Define the validation required to ship.

---

### testing

**When to use:** Before closing meaningful work. After fixing a bug. When changing behavior or a contract.

**When NOT to use:** Pure exploration. Work with no downstream consequence. When the right validation is already obvious and unambiguous.

**Core moves:**
1. Identify what changed and what could break.
2. Choose the minimum proof level for the risk: unit, integration, smoke, or manual.
3. Write or confirm the tests before marking done.
4. Check that failure modes are covered, not just happy paths.

---

### debugging

**When to use:** Runtime bugs. Failing tests. Inconsistent or surprising behavior.

**When NOT to use:** Performance profiling (a different discipline). Feature gaps — the code works as designed, but the design is wrong.

**Core moves:**
1. Reproduce the bug reliably before touching code.
2. Isolate the smallest failing case.
3. Form and test a hypothesis; do not patch symptoms.
4. Add a regression test or note so this failure mode does not recur silently.

---

### api-design

**When to use:** Designing a new interface between components or services. Reviewing an existing API before it becomes hard to change.

**When NOT to use:** Internal implementation details with no external consumers. When the contract is already settled and the work is purely implementation.

**Core moves:**
1. State the consumer's perspective — what does the caller need?
2. Define the contract: inputs, outputs, errors, and invariants.
3. Surface backward-compatibility implications.
4. Identify the simplest contract that satisfies the need.

---

### refactoring

**When to use:** Improving structure without changing behavior. Reducing complexity before adding a feature. Paying down explicit technical debt.

**When NOT to use:** Mixing structural change with behavior change in the same step — split them. Refactoring as a way to delay a harder decision.

**Core moves:**
1. Confirm the behavior to preserve (existing tests or a characterization test).
2. State the specific structural goal.
3. Make one type of change at a time (rename, extract, move, simplify).
4. Verify behavior is preserved after each step.

---

### architecture-review

**When to use:** Evaluating a design decision with long-term consequences. Choosing between structural approaches. Reviewing a proposal before committing to implementation.

**When NOT to use:** Short-term tactical decisions with low reversal cost. When the decision is already made and the work is implementation.

**Core moves:**
1. State the decision being made and the alternatives considered.
2. Identify the tradeoffs for each option.
3. Surface what would make this decision wrong in 6–12 months.
4. State a clear recommendation with reasoning.

---

### code-style

**When to use:** Code review with style inconsistencies. Creating or enforcing a style guide. Onboarding a new contributor.

**When NOT to use:** Structural or correctness issues — those belong in `refactoring` or `debugging`. Personal preference without team consensus.

**Core moves:**
1. Reference the explicit style rules being applied.
2. Flag deviations with the rule and a fix.
3. Distinguish enforceable rules (automated) from conventions (reviewed).

---

### communication

**When to use:** Writing a technical update for a mixed audience. Documenting a decision for stakeholders. Explaining something complex without assuming shared context.

**When NOT to use:** Internal technical notes where precision matters more than accessibility. Quick Slack messages with no downstream consequence.

**Core moves:**
1. Identify the audience and their context.
2. Lead with the conclusion — do not bury it.
3. Separate what changed, why it changed, and what the reader should do.
4. Remove jargon that the audience does not share.

---

### ux-strategy

**When to use:** Framing a new product experience. Direction-setting session before UI decisions are made. Aligning on the experience goal before design starts.

**When NOT to use:** Detailed UI implementation. Individual screen-level decisions with well-established context.

**Core moves:**
1. Identify the primary user and the job they are doing.
2. State the experience goal in terms of user outcome, not feature delivery.
3. Define what success looks like from the user's perspective.
4. Name the constraints that cannot be traded away.

---

### ux-provocation

**When to use:** Design review when the current direction feels safe or predictable. When you want to stress-test an idea before committing.

**When NOT to use:** Final review of a settled design. When the goal is polish, not direction.

**Core moves:**
1. State what assumption the current design makes.
2. Challenge each assumption with a "what if the opposite were true?" reframe.
3. Generate at least one alternative direction from each challenge.
4. Evaluate the alternatives against the experience goal, not design preference.

---

### heuristic-audit

**When to use:** Evaluating an existing UI for usability gaps. Pre-release readiness review. Onboarding a new team member to a product's UX issues.

**When NOT to use:** Early exploration — heuristics apply to concrete designs, not wireframes or sketches.

**Core moves:**
1. Apply each relevant heuristic to the UI under review.
2. Flag violations with the heuristic, the location, and the severity.
3. Distinguish critical issues (breaks the task) from minor ones (creates friction).
4. Prioritize by user impact.

---

### ux-writing

**When to use:** UI copy, error messages, empty states, labels, onboarding content.

**When NOT to use:** Marketing or brand copy — those follow different constraints.

**Core moves:**
1. State the user's context — what just happened, what they need to do next.
2. Write for the mental state of the moment — not the ideal, calm user.
3. Prefer action over description: "Try again" not "An error has occurred."
4. Check for jargon, passive voice, and assumed knowledge.

---

### premortem

**When to use:** Consequential plans, launches, commitments, or strategies with a high cost of failure. When there is still time to adjust.

**When NOT to use:** Decisions already made and irreversible. Exploratory, low-stakes work.

**Core moves:**
1. Reframe: assume the plan has already failed.
2. Work backwards: why did it fail? List specific, causal failure modes — not vague risks.
3. Identify fragile assumptions — things that must be true for the plan to work.
4. Define observable warning signals — early indicators that the failure is on track.
5. Propose preventive adjustments or gates before execution.

---

### task-chunking

**When to use:** Large or unclear scope. Work that could sprawl. Session with multiple distinct goals.

**When NOT to use:** Small, well-defined tasks with a clear single output.

**Core moves:**
1. List all the work implied by the task.
2. Group into explicitly bounded chunks — each chunk has one output.
3. Order by dependency and risk.
4. Confirm the first chunk before starting.

---

### checkpoint-review

**When to use:** Long session getting heavy. Task changed shape mid-round. The team needs to decide whether to continue, stop, or hand off.

**When NOT to use:** After every round as a ritual — checkpoints are for genuine inflection points.

**Core moves:**
1. State what was accomplished in this round.
2. State what the original goal was — has it changed?
3. Evaluate: continue, adjust scope, stop, or hand off?
4. If continuing, state the next concrete step.

---

### handoff-summary

**When to use:** Session ending. Switching agents or people. Crossing a meaningful boundary.

**When NOT to use:** Short sessions with trivial state. Work that will be resumed by the same person in the same session.

**Core moves:**
1. State what was worked on and why.
2. State what is done, what is in progress, what is blocked.
3. State the next concrete steps for the person or agent resuming.
4. List open questions that need human input.

---

### triad-check

**When to use:** Cross-functional decisions. Hard-to-reverse changes. Ambiguous ownership between product, design, and engineering.

**When NOT to use:** Single-function decisions with clear ownership. When the tradeoffs are already well-understood by all parties.

**Core moves:**
1. State the decision to be made.
2. Apply each lens: what does product care about? design? engineering?
3. Identify where the lenses conflict.
4. Surface the tradeoff and who should make the call.

---

### business-design

**When to use:** Strategic framing for a product or initiative. Operating model questions. Value logic that is implicit and needs to be made explicit.

**When NOT to use:** Tactical execution decisions. Pure technical or design questions.

**Core moves:**
1. State the value proposition in one sentence.
2. Identify who captures value and how.
3. Surface the operating assumptions that must hold for the model to work.
4. Name the biggest risk to the model.

---

### qa-review

**When to use:** Pre-release readiness. Cross-layer review (behavior, contract, edge cases). Quality gate for consequential work.

**When NOT to use:** Replacing domain-specific testing with a generic review. Quick internal changes with low consequence.

**Core moves:**
1. Review for correctness: does it do what was specified?
2. Review for completeness: are edge cases covered?
3. Review for consistency: does it match the project's established patterns?
4. Surface open issues with severity — critical (must fix) vs. minor (should fix before release).

---

### observability-review

**When to use:** Adding telemetry. Reviewing existing instrumentation. Deciding what to measure for a new feature.

**When NOT to use:** Pure implementation work with no observability requirement. When observability has already been defined and the work is just adding metrics.

**Core moves:**
1. Identify the decision the metric should inform — not "what can we measure?" but "what do we need to know?"
2. Define the signal: what event, rate, or state matters?
3. Link the metric to an action threshold — at what value does a human or system act?
4. Confirm the metric is actionable: a metric nobody acts on is noise.

---

## Composite flows

These flows show how multiple skills combine for common task types. They are starting points, not rigid sequences — adapt to your context.

### 1. Starting a new feature from scratch

**Goal:** turn a vague feature request into a disciplined delivery.

```
workflow          → Frame the task with scope and proof before starting
feature-planning  → Turn intent into a smallest slice with risks and success criteria  
premortem         → Assume the feature has already failed; surface fragile assumptions
testing           → Define the minimum validation before closing
```

When to skip `premortem`: small, low-risk features with clear requirements and fast reversal.

---

### 2. Debugging a production issue

**Goal:** fix the root cause, not the symptom, and prevent recurrence.

```
workflow          → Declare scope (what system? what behavior?) before touching code
debugging         → Reproduce, isolate, hypothesize, fix
testing           → Add a regression test so this failure mode does not recur silently
handoff-summary   → Package state if the session ends before the fix is shipped
```

---

### 3. Stress-testing a plan before execution

**Goal:** surface failure modes and fragile assumptions before committing.

```
premortem         → Work backwards from assumed failure to specific causes
triad-check       → Validate the plan from product, design, and engineering lenses
checkpoint-review → Decide whether to proceed, adjust, or stop after the review
```

---

### 4. Closing a long session cleanly

**Goal:** leave behind enough context for the next session to start without re-deriving.

```
checkpoint-review → Evaluate what was accomplished and what remains
task-chunking     → If scope has sprawled, re-bound the remaining work explicitly  
handoff-summary   → Package state, decisions, and next steps for the next operator
```

---

### 5. UX design review

**Goal:** evaluate and improve an existing design before it is built.

```
ux-strategy       → Confirm the experience goal the design is trying to achieve
ux-provocation    → Challenge assumptions and surface stronger alternatives
heuristic-audit   → Review the UI against usability heuristics
ux-writing        → Review and improve copy for clarity, tone, and intent
```

---

### 6. Architecture decision before committing

**Goal:** choose between structural approaches with explicit tradeoffs.

```
premortem         → Assume the chosen architecture fails — why did it fail?
architecture-review → Evaluate each option with tradeoffs and a recommendation
triad-check       → Validate the decision from product, design, and engineering perspectives
communication     → Document the decision with reasoning for stakeholders
```

---

### 7. Shipping a quality gate

**Goal:** confirm the work is ready to ship with proportional validation.

```
testing           → Calibrate validation level against risk and reversibility
qa-review         → Cross-layer review for correctness, completeness, consistency
observability-review → Confirm the shipped change has the right telemetry to be monitored
handoff-summary   → Document the decision to ship with open items captured
```

---

## What is not in this catalog

**Domain packs** (e.g., `crisis-management`) are case studies for specific domains, not generic capability surface. They are excluded from the standard APM package. See [`docs/adr/ADR-002-domain-agnosticism.md`](../adr/ADR-002-domain-agnosticism.md).

**Skeleton-only domains** (`product`, `governance`) have no published skills yet. Check [`docs/skill-categories.md`](../skill-categories.md) for the backlog.

**Evolution layer** (`evolution/`) is not a skill — it is the process by which the library improves over time. See [`docs/evolution-layer.md`](../evolution-layer.md).
