---
title: Maintainer reference
description: Find architecture decisions, catalog governance, compatibility rules, and internal publication boundaries.
---

This section is for people reviewing or evolving the library. Consumer guidance remains in Start here and Use Adaptive Skills.

## Architecture decisions

The [Architecture Decision Records index](../adr/README/) explains stable decisions behind the capability library, domain agnosticism, AletheIA relationship, conformance, packaging, knowledge boundaries, and harness requirements.

## Catalog governance

[Skill catalog governance](../skill-catalog-governance/) defines intake, module proposals, merge, split, deprecation, protected surfaces, and validation expectations. A useful example does not bypass this lifecycle.

## Compatibility

[Pattern compatibility guidelines](../pattern-compatibility-guidelines/) explain how skills participate in execution patterns without becoming a workflow engine.

Related references include [Capability routing boundary](../capability-routing-boundary/), [Harness requirements](../harness-requirements-for-skills/), [Knowledge boundaries](../skill-knowledge-boundaries/), and [Evolution](../evolution-layer/).

## Internal publication records

Editorial audits, readiness records, publication proof, and Blume authoring patterns remain source-controlled but intentionally absent from the public sidebar. They document how the site was produced; they are not product guidance.

## Maintainer checklist

1. Identify protected and proposal-safe surfaces.
2. Link source-backed evidence.
3. Preserve skill, role, harness, capability, and AletheIA boundaries.
4. Update the canonical source rather than duplicating it.
5. Run all relevant validators.
6. Update current state or changelog only when delivered truth changed.

## Next steps

- Review [Current state](../updates/current-state/).
- Read the [ADR index](../adr/README/).
- Follow [Skill catalog governance](../skill-catalog-governance/) for library changes.
