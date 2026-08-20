---
description: >-
  Install PredictHQ agent skills to give AI coding assistants best-practice
  integration knowledge - recommended workflow, API selection, and Beam
  guidance, applied automatically while you build.
---

# Agent skills

Agent skills are packaged integration knowledge for AI coding assistants. Installed once, the PredictHQ skill is applied automatically whenever your agent works on a PredictHQ integration - no prompting, no pasting docs into context.

The skill encodes the same guidance these docs recommend, so code written with it follows the proven path instead of a plausible-looking wrong one:

* The recommended integration workflow - Saved Locations and Predicted Impact Area first, then Beam, then features
* API selection - Features API for model inputs, Events API for explainability, and when the Forecasts API is the better fit
* Beam best practices - one analysis per location, `beam.analysis_id` on every downstream call, monthly refresh
* Common mistakes to avoid - manual event aggregation, fixed radii, skipping Beam

## Install

```bash
npx skills add predicthq/agent-skills
```

Works with Claude Code, Cursor, Gemini CLI, GitHub Copilot, and other compatible agents. The skills are open source on [GitHub](https://github.com/predicthq/agent-skills).

## Skills and the MCP server

The two are complementary and often installed together. Agent skills teach your coding assistant how to *build* the integration correctly. The [MCP server](mcp.md) gives assistants and agents live access to PredictHQ data - for exploring while you build, and for [grounding](grounding-llms-in-real-world-data.md) AI systems in production.

## Next steps

* [Build with AI](build-with-ai.md) - all the tools for building with AI assistants
* [MCP Server](mcp.md) - live API access from any MCP-compatible client
* [Which API Should I Use?](../getting-started/core-concepts/which-api-should-i-use.md) - the guidance the skill applies, in human-readable form
