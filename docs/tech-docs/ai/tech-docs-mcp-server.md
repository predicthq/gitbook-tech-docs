---
description: >-
  Search PredictHQ's technical documentation from inside your code editor or AI
  assistant.
hidden: true
---

# Tech Docs MCP Server

When building an integration, your AI coding assistant can query PredictHQ's documentation directly - looking up API parameters, understanding concepts like Beam or Predicted Impact Area, finding code examples, and surfacing the right guidance without you leaving your editor. The Tech Docs MCP server makes this possible by exposing PredictHQ's documentation through the [Model Context Protocol](https://modelcontextprotocol.io/) (MCP).

## Server Details

<table><thead><tr><th width="305.66796875"></th><th></th></tr></thead><tbody><tr><td><strong>MCP Server URL</strong></td><td><code>https://docs.predicthq.com/~gitbook/mcp</code></td></tr><tr><td><strong>Transport</strong></td><td>Streamable HTTP</td></tr><tr><td><strong>Authentication</strong></td><td>None — publicly accessible</td></tr></tbody></table>

## Available Tools

The Docs MCP server provides tools for searching PredictHQ's documentation and retrieving individual pages - covering API references, integration guides, tutorials, and conceptual content. It provides read-only access to published content only; drafts and unpublished changes are never exposed.

For the full list of available tools and capabilities, see [GitBook's MCP documentation](https://gitbook.com/docs/ai-and-search/mcp-servers-for-published-docs).

## Connect Your AI Client

### Claude Code

To add the Tech Docs MCP server for your own use:

```bash
claude mcp add --transport http predicthq-docs https://docs.predicthq.com/~gitbook/mcp
```

To share the configuration with your team via a `.mcp.json` file in your project:

```bash
claude mcp add --transport http predicthq-docs --scope project https://docs.predicthq.com/~gitbook/mcp
```

For full instructions, see [Claude Code MCP documentation](https://docs.anthropic.com/en/docs/claude-code/mcp).

### Other Clients

The Docs MCP server works with any MCP-compatible client that supports Streamable HTTP transport, including Cursor, Windsurf, and VS Code (GitHub Copilot).

Add the following to your client's MCP configuration:

```json
{
  "mcpServers": {
    "predicthq-docs": {
      "url": "https://docs.predicthq.com/~gitbook/mcp"
    }
  }
}
```

Refer to your client's documentation for specific configuration steps.

## Next Steps

* [MCP Server](https://claude.ai/ai-and-agents/mcp-server) - connect to PredictHQ's live data APIs
* [Using PredictHQ with AI Assistants](using-predicthq-with-ai-assistants.md) - understand how PredictHQ fits into AI and agent workflows
* [API Quickstart](../getting-started/api-quickstart.md) - get started with the PredictHQ API
