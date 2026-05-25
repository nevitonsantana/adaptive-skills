# Premortem Example — Quality Gates for AI-Generated Code

This is a worked example using the validation scenario from the premortem brief.

**Input:** "We want to create quality gates for projects with AI-generated code, covering engineering, security, UX, accessibility, agent behavior, and human decision."

---

## Activation check result

- Concrete plan? Yes — defining a quality gate process is a concrete process decision.
- Meaningful cost of failure? Yes — miscalibrated gates either miss serious defects or block teams with no value.
- Can direction still change? Yes — gates do not exist yet.
- Impact on security, UX, agent behavior? Yes — three domains listed directly.
- Assumptions without evidence? Likely — whether AI-specific failure modes are catchable at gate vs. in production is unknown.

**Profile selected: High-Assurance** — AI/autonomy + security impact + explicit human decision required + potential for low-reversibility process adoption.

---

## Premortem — Quality Gates for AI-Generated Code

### Framing

Six months have passed. The quality gate program was implemented. Projects continue to deliver code with serious defects. The program was suspended for generating friction without perceived value.

### Context

- **Initiative:** Define and enforce quality gates for projects using AI-generated code, covering engineering, security, UX, accessibility, agent behavior, and human decision.
- **Audience / affected parties:** Engineering teams using AI-assisted development; PMs and designers whose work is reviewed; security and accessibility reviewers; end users.
- **Success criterion:** Gates catch AI-specific defects before production; teams adopt the process without unsustainable friction.
- **Cost of failure:** High — security defects in production; accessibility violations; agent behavior without boundaries; process abandoned after investment.
- **Reversibility:** Low — once a gate program is embedded in team workflows, removing it requires explicit governance change.
- **Depth profile used:** High-Assurance.

### Failure modes

1. **Security gates are defined by engineering without security review, approving patterns that look safe but have known vulnerabilities in LLM-generated code context.**
   Engineers are not trained to identify prompt injection surfaces or unsafe deserialization patterns in AI-generated output. Without a security reviewer in the gate design, the gate becomes a false assurance.

2. **UX and accessibility gates exist on paper but no reviewer has allocated time, so they are systematically marked "approved" without real inspection.**
   Gates without a named reviewer and time allocation are theater. Reviewers agree in principle but approve by default under deadline pressure.

3. **The "agent behavior" criterion is never operationalized — no team knows what constitutes acceptable vs. unacceptable agent behavior, so the gate generates noise without signal.**
   Without a concrete rubric (e.g., "agent must not take destructive actions without confirmation"), reviewers cannot apply the gate consistently. It becomes a checkbox that different reviewers interpret differently.

4. **Hard gates block low-risk features with the same weight as critical ones, exhausting team tolerance within 8 weeks.**
   A uniform gate threshold creates disproportionate friction on simple changes. Teams start routing work around gates or marking everything as low-risk to avoid the process.

5. **The human decision gate is in the process but has no SLA — the gate accumulates pending items and becomes a bottleneck without an owner.**
   Human decision gates without a defined owner, escalation path, and response time become queues. Work stalls; teams learn to avoid triggering the gate.

6. **The gate program has no success metric — after 3 months, no one can demonstrate whether it prevented real defects or only generated overhead.**
   Without a baseline and measurement plan, the program cannot defend itself against the perception of friction. The absence of visible wins accelerates abandonment.

### Most probable failure

**#4 (uniform gate weight).** Teams that adopt a heavy gate process on all PR types burn out within one quarter. This is the most common pattern in gate program failures and requires no special bad faith — just an understandable response to friction.

### Most dangerous failure

**#1 (security gates without security reviewer).** A false sense of security is worse than no gate. Teams will reference the gate as evidence of safety review when no real security analysis occurred. This is the failure that causes a production incident and destroys program credibility simultaneously.

### Hardest to detect

**#3 (agent behavior not operationalized).** This failure is invisible until a serious agent-behavior incident occurs. The gate appears to function because reviewers fill in the checkbox. There is no signal that the review is meaningless until something goes wrong.

### Hidden assumption

The program assumes reviewers have clear criteria and allocated time for each gate domain. Neither is guaranteed. The gate design process treats reviewer availability and expertise as inputs, not as things that need to be explicitly created.

### Warning signals

- Any gate domain without a named reviewer two weeks after launch.
- Gate approval rate above 95% in the first month — likely rubber-stamping, not real review.
- More than 3 complaints per week from teams about gate friction within the first 6 weeks.
- Human decision queue with items older than 5 business days.
- No definition of "acceptable agent behavior" documented before the agent behavior gate goes live.

### Recommended gates

#### Hard gates
- Do not launch gates for any domain until that domain has a named reviewer with explicitly allocated review time.
- Do not launch the agent behavior gate until a concrete, reviewable rubric for acceptable/unacceptable agent behavior is written and agreed upon.

#### Soft gates
- Launch with a tiered risk model (low / medium / high risk) that maps gate requirements to risk level before applying uniform gates. Run for 4 weeks with one pilot team before full rollout.

#### Review triggers
- Involve Security before finalizing the security gate criteria — gate definitions should be reviewed by someone who understands LLM-specific attack surfaces.
- Involve Accessibility and Design before finalizing UX/accessibility gate criteria.

#### Human decision gates
- Leadership must decide: accept launching with partial domain coverage (only engineering + security) or delay until all 6 domains have reviewers? Trade-off: speed vs. credibility of a partial program.

### Revised plan

1. Before defining gate criteria, map which domains have a named reviewer with allocated time. Only define gates for domains that are staffed.
2. Add a risk-tier model so gate requirements scale with the risk level of the change, not uniformly across all PRs.
3. Write the agent behavior rubric before creating the agent behavior gate — gate design and rubric design are the same task.
4. Define a success metric for the gate program before launch (e.g., "X% of security issues caught at gate vs. production in 6 months").
5. Define SLA and owner for the human decision gate before it goes live.

### Pre-execution checklist

- [ ] Each gate domain has a named reviewer confirmed with allocated time.
- [ ] Risk-tier model defined and reviewed by at least one team that will use it.
- [ ] Agent behavior rubric written and reviewed by at least one engineer and one PM.
- [ ] Success metric and baseline measurement plan documented.
- [ ] Human decision gate has a named owner and SLA defined.
- [ ] Pilot team identified for 4-week trial before full rollout.

### Pending items

- Leadership decision on partial vs. full-domain launch (human decision gate above).
- Confirmation from Security that they can staff the security gate review.
- Definition of "AI-generated code" for gate scope purposes — does it include AI-assisted (copilot suggestions) or only fully AI-generated outputs?
