---
description: >-
  Ground AI systems in verified real-world event data and build integrations
  faster with the MCP server, agent skills, and AI-readable docs.
---

# Build with AI

AI assistants can query PredictHQ's APIs in natural language, search the documentation while you code, and follow best practice integration patterns automatically - reducing the time from first API call to a production-ready integration.

These tools serve two distinct jobs: AI that helps you _build_ your integration (coding assistants, agent skills), and AI that PredictHQ _grounds_—assistants and agents retrieving verified real-world context at inference time.

## MCP Server

Connect any MCP-compatible AI assistant to PredictHQ's live APIs. Once connected, you can search events, retrieve demand intelligence, work with Saved Locations, Beam, Features, Forecasts, and Predicted Impact Area, and search PredictHQ's technical documentation - all through natural language, without leaving your AI client or writing API calls manually.

Supported clients include Claude, ChatGPT, Claude Code, Cursor, and any other client that supports the Model Context Protocol.

[Set up the MCP Server →](mcp.md)

## Agent Skills

Agent skills give your AI coding assistant specialised knowledge about how to integrate with PredictHQ correctly - the recommended workflow, API selection guidance, Beam best practices, and common mistakes to avoid.

Once installed, the skill is applied automatically when you work on PredictHQ integrations. No prompting required.

```bash
npx skills add predicthq/agent-skills
```

Works with Claude Code, Cursor, Gemini CLI, GitHub Copilot, and other compatible agents. Skills are available on [GitHub](https://github.com/predicthq/agent-skills).

## Plain Text Docs

Every page in PredictHQ's documentation is available as plain text Markdown - useful for pasting directly into an AI assistant or loading into a coding agent's context.

Add `.md` to the end of any documentation URL to get the plain text version. For example:

```
https://docs.predicthq.com/api/events/search-events.md
```

A full index of all documentation pages is available at [/llms.txt](https://docs.predicthq.com/llms.txt).

## Grounding

New to grounding? [Grounding LLMs in real-world event data (RAG)](grounding-llms-in-real-world-data.md) covers what grounding is, how it reduces AI hallucinations, and the two architectures - retrieval inside your environment or on demand via MCP.

For integration patterns and example workflows, see [Using PredictHQ with AI Assistants](using-predicthq-with-ai-assistants.md).
