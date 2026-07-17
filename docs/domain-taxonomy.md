---
title: "Domain Taxonomy"
description: "Reference documentation for Domain Taxonomy in Adaptive Skills."
---

## Generic skills

Generic skills live under `skills/` and should work across products with little or no domain adaptation.

Current generic domains:
- engineering
- design
- business
- quality
- metrics
- cross-functional
- efficiency
- planning

Skeleton-only in v0:
- product
- governance

## Domain packs

Domain packs live under `domain-packs/`.

They are explicitly domain-specific and should stay separate from the generic library.

Current pack:
- `crisis-management`

## Decision rule

A skill belongs in the generic library only if it can be used in another project without inheriting local operating rules or domain-specific vocabulary.

If the skill depends on a specific product worldview, vocabulary, or context model, it should be a domain pack.
