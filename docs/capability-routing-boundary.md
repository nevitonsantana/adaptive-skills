# Capability Routing Boundary

Adaptive Skills can help a consumer decide which capability or skill appears to fit a task, but it
does not own global routing, approval, execution or closure.

The cross-repository S10 reconciliation lives in AletheIA:

- [Capability Routing Reconciliation](https://github.com/nevitonsantana/AletheIA/blob/main/docs/contracts/capability-routing-reconciliation.md)

## Boundary

| Surface | Adaptive Skills may declare | Adaptive Skills must not declare |
|---|---|---|
| Capability | fit, risk hints, modes, dependencies, expected evidence, escalation hints | final route, approval, Work Slice state, gate result |
| Skill | method, triggers, core moves, when not to use, required output | tool permission, runtime authority, human acceptance |
| Capability graph | advisory paths and composition hints | hidden router, scheduler, scorer or optimizer |
| Execution record | observed capability use when a harness records it | success rate or ranking without comparable reviewed evidence |

## Required consumer evidence

A consumer runtime or AletheIA-compatible harness should record:

- selected capability and skill;
- reason for activation;
- execution vehicle and pattern when available;
- tools invoked by the harness, not by the skill itself;
- AHC/AHGE or equivalent action evidence;
- outcome, human review and unknown/unavailable fields without inference.

## Non-goals

- no routing engine;
- no global provider selection;
- no automatic skill ranking;
- no replacement for AletheIA gates;
- no dependency on AletheIA for the library to remain useful.
