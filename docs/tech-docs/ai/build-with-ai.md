---
description: >-
  Ground AI systems in verified real-world event data and build integrations
  faster with the MCP server, agent skills, and AI-readable docs.
---

# Build with AI

AI assistants can query PredictHQ's APIs in natural language, search the documentation while you code, and follow best practice integration patterns automatically - reducing the time from first API call to a production-ready integration.

These tools serve two distinct jobs: AI that helps you _build_ your integration (coding assistants, agent skills), and AI that PredictHQ _grounds_—assistants and agents retrieving verified real-world context at inference time.

## MCP server

Connect any MCP-compatible AI assistant to PredictHQ's live APIs. Once connected, you can search events, retrieve demand intelligence, work with Saved Locations, Beam, Features, Forecasts, and Predicted Impact Area, and search PredictHQ's technical documentation - all through natural language, without leaving your AI client or writing API calls manually.

Supported clients include Claude, ChatGPT, Claude Code, Cursor, and any other client that supports the Model Context Protocol.

[Set up the MCP server →](mcp.md)

## Agent skills

Agent skills give your AI coding assistant specialized knowledge about how to integrate with PredictHQ correctly - the recommended workflow, API selection guidance, Beam best practices, and common mistakes to avoid. Once installed, your assistant applies the skill automatically when you work on PredictHQ integrations. To install the skills, run:

```bash
npx skills add predicthq/agent-skills
```

[Set up agent skills →](agent-skills.md)

## Plain text docs

Every page in PredictHQ's documentation is available as plain text Markdown - useful for pasting directly into an AI assistant or loading into a coding agent's context.

To get the plain text version, add `.md` to the end of any documentation URL. For example:

```
https://docs.predicthq.com/api/events/search-events.md
```

A full index of all documentation pages is available at [llms.txt documentation index](https://docs.predicthq.com/llms.txt).

## Grounding

New to grounding? [Grounding with PredictHQ](grounding-with-predicthq.md) covers what grounding is, how it reduces AI hallucinations, and the two architectures - retrieval inside your environment or on demand via MCP.

For the assistant request flow and how the APIs map to scope, relevance, usability, and trust, see [Using PredictHQ with AI assistants](grounding-with-predicthq.md#using-predicthq-with-ai-assistants).
