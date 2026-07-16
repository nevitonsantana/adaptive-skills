# Adaptive Skills Blume docs shell

This app is the manual Blume documentation shell for Adaptive Skills.

It reads Markdown from `../../docs`. Links to repository assets outside `docs/` remain source links unless they are promoted into the public documentation corpus in a later slice. It is intentionally not wired to automatic GitHub Pages publishing yet.

## Local commands

```bash
pnpm install
pnpm run docs:validate
pnpm run docs:build
```

## Boundary

This shell does not change skill behavior, projection behavior, routing, or repository governance. Publication automation remains a later explicit decision.
