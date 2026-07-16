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
});
