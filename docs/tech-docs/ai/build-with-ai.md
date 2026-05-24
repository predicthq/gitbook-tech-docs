---
description: >-
  Tools and resources for building PredictHQ integrations with AI assistants and
  coding agents.
---

# Build with AI

AI assistants can query PredictHQ's APIs in natural language, search the documentation while you code, and follow best practice integration patterns automatically - reducing the time from first API call to a production-ready integration.

## MCP Server

Connect any MCP-compatible AI assistant to PredictHQ's live APIs. Once connected, you can search events, retrieve demand intelligence, and work with Saved Locations, Beam, Features, Forecasts, and Predicted Impact Area through natural language - without leaving your AI client or writing API calls manually.

Supported clients include Claude, ChatGPT, Claude Code, Cursor, and any other client that supports the Model Context Protocol.

[Set up the MCP Server →](mcp.md)

## Tech Docs MCP Server

Give your AI coding assistant access to PredictHQ's documentation while you build. Your agent can look up API parameters, find code examples, and surface integration guidance in context - without switching to a browser.

The Tech Docs MCP server is publicly accessible with no authentication required.

[Set up the Tech Docs MCP Server →](tech-docs-mcp-server.md)

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

## Using PredictHQ with AI Assistants

New to using PredictHQ in AI workflows? The integration guide covers how PredictHQ fits into AI and agent-based systems - the architectural patterns, which APIs to use at inference time, and how to ground AI responses in verified real-world event context.

[Read the guide →](using-predicthq-with-ai-assistants.md)
