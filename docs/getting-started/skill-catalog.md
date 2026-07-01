# Adaptive Skills — Skill Catalog

A navigable reference of the published generic skills, organized by category, with trigger signals, brief descriptions, and composite flows for common task types.

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
| [`lean-implementation`](#lean-implementation) | Confirmed plan; small safe change; implementation sprawl risk | Implement the smallest safe change with validation and handoff evidence |
| [`architecture-review`](#architecture-review) | Evaluating a design decision with long-term consequences | Surface tradeoffs, risks, and alternatives before committing |
| [`code-style`](#code-style) | Code review; style inconsistency; style guide creation | Enforce consistent style with explicit criteria, not instinct |
| [`communication`](#communication) | Writing an update, decision, or explanation for a mixed audience | Shape technical communication for the right audience and purpose |
| [`domain-language-alignment`](#domain-language-alignment) | Misaligned vocabulary between product, domain, docs, and code | Reconcile terms before agents touch code or plan |

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

### Product

| Skill | Trigger signal | One-line description |
|---|---|---|
| [`feature-value-governance`](#feature-value-governance) | Feature proposed; prioritization decision; worth-doing judgment | Judge whether a proposed feature deserves investment |
| [`opportunity-tree-alignment`](#opportunity-tree-alignment) | Competing bets; backlog without clear outcome links | Connect an opportunity tree to revenue levers and flag orphan bets |

### Business

| Skill | Trigger signal | One-line description |
|---|---|---|
| [`business-design`](#business-design) | Strategic framing; value logic; operating model decisions | Frame the business logic behind a product or initiative |
| [`revenue-lever-mapping`](#revenue-lever-mapping) | Vague value claim; competing bets; no measurable mechanism | Map which revenue or value lever an opportunity moves |

### Governance

| Skill | Trigger signal | One-line description |
|---|---|---|
| [`feature-complexity-audit`](#feature-complexity-audit) | Complexity is the deciding factor; non-trivial build commitment | Estimate the permanent cost of a feature before build |
| [`sunset-decision`](#sunset-decision) | Low-traction feature with ongoing cost; portfolio review | Decide whether to keep, limit, refactor, deprecate, or remove a feature |
| [`knowledge-source-evaluation`](#knowledge-source-evaluation) | Registering a new knowledge source; re-evaluation due | Evaluate whether a document can be a governed knowledge pack |
| [`knowledge-conflict-resolution`](#knowledge-conflict-resolution) | Sources disagree on a decision-relevant point | Resolve conflict between knowledge sources via precedence |
| [`restricted-context-check`](#restricted-context-check) | Sensitive source about to be consumed; cross-boundary task | Check a knowledge use for leakage, injection, and permission risks |

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

### lean-implementation

**When to use:** A bounded plan or Work Slice is ready for implementation and the main risk is scope expansion.

**When NOT to use:** Intent is unclear, the task is debugging, test strategy, refactoring-only, or unresolved architecture/security/accessibility/data-governance decisions remain.

**Core moves:**
1. Restate the smallest acceptable change and boundary.
2. Inspect the existing pattern before editing.
3. Make one coherent change without opportunistic refactors.
4. Run the minimum reliable validation and record gaps.
5. Handoff what changed, why, evidence, and the next safe step.

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

### domain-language-alignment

**When to use:** Before a relevant implementation or architectural change. When the request uses vague, overloaded, or inconsistent terms. When business language conflicts with names in the code.

**When NOT to use:** Trivial local changes with no shared vocabulary at stake. When domain language is already settled and consistently used.

**Core moves:**
1. Extract key terms used in the request, docs, code, and prior decisions.
2. Mark ambiguous, overloaded, missing, or conflicting terms.
3. Recommend canonical terms and where they should be recorded.
4. Flag decisions that deserve an ADR or decision record.

---

### feature-value-governance

**When to use:** A feature is proposed and someone must decide whether it is worth doing. Prioritizing a backlog where value and cost are contested. A roadmap decision needs an explicit business intent and lever.

**When NOT to use:** The decision to build is already made (use `feature-planning`). The change is tiny with obvious value. No problem framing exists yet.

**Core moves:**
1. Frame the feature and resolve knowledge context (strategic framework, personas, operating model).
2. Surface business intent and name the primary revenue/value lever.
3. Weigh user evidence; check opportunity-tree alignment.
4. Estimate complexity cost and assess overreach risk (compliance, accessibility, privacy).
5. Render a worth-doing verdict with audit trail.

---

### revenue-lever-mapping

**When to use:** An opportunity or feature has a vague value claim. Two bets compete and you need to compare levers. A roadmap item lists no measurable mechanism of value.

**When NOT to use:** The lever is already named, measured, and uncontested. No problem framing exists yet. Pure execution planning (use `feature-planning`).

**Core moves:**
1. Name the primary lever: acquisition, activation, retention, expansion, efficiency, margin, or strategic_defense.
2. Name secondary levers (if any), clearly subordinate.
3. Attach a metric that would prove the lever moved.
4. Pick a proxy for early signal.
5. State risks and uncertainty.

---

### opportunity-tree-alignment

**When to use:** A backlog has competing bets with unclear links to outcomes. An opportunity tree exists but does not connect to revenue/value levers. Sequencing across opportunities by value and evidence.

**When NOT to use:** A single obvious bet with a clear outcome. No outcomes or opportunities have been framed yet. The lever for one feature is the only question (use `revenue-lever-mapping`).

**Core moves:**
1. List opportunities under each outcome.
2. Attach a lever to each opportunity.
3. Place candidate features under the opportunity they serve.
4. Flag orphans — features with no opportunity, opportunities with no lever.
5. Reorder by value × evidence and state sequencing rationale.

---

### feature-complexity-audit

**When to use:** A feature looks valuable and complexity is the deciding factor. Before a build commitment on anything non-trivial. Comparing two designs that deliver similar value at different carry.

**When NOT to use:** The change is tiny and obviously cheap. Value itself is unresolved (resolve the lever first). No scope or dependencies are known yet.

**Core moves:**
1. Score four dimensions (each low/medium/high): cognitive, technical, operational, governance.
2. Name reversibility: reversible, partially reversible, or one-way door.
3. Roll up to a coarse level with the dominant driver named.
4. Recommend the smallest scope that keeps the value.

---

### sunset-decision

**When to use:** A feature has low traction but ongoing maintenance or security cost. Periodic portfolio review. A feature blocks a platform upgrade or widens the attack surface.

**When NOT to use:** The feature is new and has not had a fair chance. The decision is about a new feature (use `feature-value-governance`). No usage, cost, or support data exists.

**Core moves:**
1. Read traction vs. cost — is value-per-cost positive, flat, or negative?
2. Map dependencies: who/what breaks if it changes.
3. Choose a disposition: keep, limit, refactor, deprecate, or remove.
4. Attach a plan (migration for deprecate/remove; reduced scope for limit/refactor; next review trigger for keep).

---

### knowledge-source-evaluation

**When to use:** A user proposes adding a knowledge source to a project. A skill author wants to depend on a new framework. A source's review cycle has elapsed.

**When NOT to use:** Authoring the framework's content itself. Resolving conflict between already-registered sources (use `knowledge-conflict-resolution`). Checking restricted-exposure risk at runtime (use `restricted-context-check`).

**Core moves:**
1. Classify type using the source taxonomy.
2. Assess sensitivity and authority.
3. Determine scope and retrieval mode.
4. Check whether a capsule is required and exists.
5. Recommend maturity level (minimal, operational, governed) or refuse with reason.

---

### knowledge-conflict-resolution

**When to use:** Resolved context pack contains sources that disagree. A skill output would change depending on which source is authoritative. Two mandatory sources appear to conflict.

**When NOT to use:** Selecting sources in the first place. Evaluating whether a single source can be registered (use `knowledge-source-evaluation`). Checking exposure risk (use `restricted-context-check`).

**Core moves:**
1. State the conflict precisely: which sources, which decision point, which positions.
2. Locate each source in the precedence tiers.
3. Apply precedence; record prevailing and suppressed sources.
4. Re-derive the affected decision under the prevailing source.
5. Escalate to human review if precedence cannot settle it.

---

### restricted-context-check

**When to use:** A skill is about to consume a confidential, restricted, or regulated source. A task crosses a trust boundary. A new source is being used for the first time. A deliverable will be external.

**When NOT to use:** Resolving conflicts between sources (use `knowledge-conflict-resolution`). Evaluating whether a source can be registered (use `knowledge-source-evaluation`). Routine use of public sources.

**Core moves:**
1. Run five guardrail checks: data leakage, prompt injection, data poisoning, permission mismatch, context contamination.
2. Translate findings into structured restrictions or refusal.
3. Surface required human-review conditions.
4. Write an audit entry.

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

**Product and governance skills** are now published and included above.

**Evolution layer** (`evolution/`) is not a skill — it is the process by which the library improves over time. See [`docs/evolution-layer.md`](../evolution-layer.md).
