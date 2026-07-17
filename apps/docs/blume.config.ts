import { defineConfig } from "blume";

export default defineConfig({
  title: "Adaptive Skills Docs",
  description: "Official documentation for Adaptive Skills micro-skills, capability metadata, projections, and governed evolution.",
  content: {
    sources: [{ type: "filesystem", root: "../../docs" }],
  },
  deployment: {
    site: "https://nevitonsantana.github.io",
    base: "/adaptive-skills",
  },
  navigation: {
    sidebar: {
      display: "page",
      items: [
        "/",
        {
          label: "Start here",
          items: [
            "/getting-started/overview",
            "/getting-started/quickstart",
            "/getting-started/installation-guide",
            "/getting-started/first-skill",
            "/how-to-use-a-skill",
            "/getting-started/faq",
          ],
        },
        {
          label: "Use Adaptive Skills",
          items: [
            "/guides/skill-selection",
            "/getting-started/skill-catalog",
            "/guides/workflow-recipes",
            "/guides/install-via-apm",
            "/codex-consumer-setup",
            "/claude-consumer-setup",
            "/consumer-adoption",
            "/first-consumer-pilot",
            "/pilot-evaluation-checklist",
            "/specification-facilitation",
          ],
        },
        {
          label: "Adaptive Skills + AletheIA",
          items: [
            "/aletheia-integration",
            "/agent-role-integration",
            "/skills-in-orchestrated-workflows",
            "/skill-observation-return-pattern",
            "/aletheia-first-test",
          ],
        },
        {
          label: "Concepts",
          items: [
            "/concepts/index",
            {
              label: "Skills",
              items: [
                "/skill-model",
                "/skill-categories",
                "/domain-taxonomy",
                "/skill-design-principles/lean-skill-doctrine",
                "/execution-patterns-for-skills",
                "/looping-models-for-skills",
                "/efficiency-layer-trio-patterns",
              ],
            },
            {
              label: "Capabilities",
              items: [
                "/capability-model",
                "/capability-graph",
                "/capability-routing-boundary",
                "/execution-modes",
                "/operational-runtime",
              ],
            },
            {
              label: "Harnesses",
              items: [
                "/skill-harness-boundaries",
                "/using-skills-inside-harnesses",
                "/harness-aware-engineering-skills",
                "/harness-requirements-for-skills",
              ],
            },
            {
              label: "Knowledge",
              items: [
                "/skill-knowledge-boundaries",
                "/declaring-knowledge-dependencies",
                "/using-proprietary-frameworks-safely",
              ],
            },
            "/concepts/ecosystem-map",
          ],
        },
        {
          label: "Cases and evidence",
          items: [
            "/cases/index",
            "/crisis-monitor-case-study",
            "/design-system-intelligence-pulso-pilot",
            "/efficiency-layer-crisis-monitor-reference",
            "/efficiency-layer-first-pilot",
            "/efficiency-layer-pilot-checklist",
            "/engineering-skills-hardening-pack",
            "/reference-maps/mattpocock-engineering-skills-map",
          ],
        },
        {
          label: "Updates and evolution",
          items: [
            "/updates/index",
            "/updates/current-state",
            "/updates/changelog",
            "/evolution-layer",
            "/telemetry",
            "/evolution/optimization-boundaries",
            "/evolution/skill-evolution-experiments",
            "/evolution/validation-case-guidelines",
            "/efficiency-layer",
            "/efficiency-layer-roadmap",
            "/efficiency-layer-candidate-skills",
            "/efficiency-layer-next-signals",
          ],
        },
        {
          label: "Maintainer reference",
          items: [
            "/maintainers/index",
            "/adr/README",
            "/adr/ADR-001-adaptive-skills-as-capability-library",
            "/adr/ADR-002-domain-agnosticism",
            "/adr/ADR-003-relationship-with-aletheia",
            "/adr/ADR-004-agentskills-io-conformance",
            "/adr/ADR-005-apm-packaging-strategy",
            "/adr/ADR-006-knowledge-aware-skills-boundary",
            "/adr/ADR-007-per-skill-harness-requirements",
            "/skill-catalog-governance",
            "/pattern-compatibility-guidelines",
          ],
        },
      ],
    },
  },
});
