---
description: Docs, guides, and API references to help you build with PredictHQ.
---

# Overview

Everything you need to integrate PredictHQ into your models, pipelines, and AI systems.

<a href="getting-started/api-quickstart.md" class="button primary">API Quickstart</a> <a href="https://app.gitbook.com/o/WGid6DiA3ccvlkmvc17s/s/kEFs8urDbSJqBmXUI3Lv/" class="button secondary">API Reference</a>

## Core APIs

* [Events API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events) - Structured, deduplicated real-world events for discovery, explainability, and building trust in AI-driven decisions
* [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) - Pre-built, model-ready demand features aggregated from real-world events
* [Forecasts API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts) - Event-driven demand forecasts without building or maintaining your own model
* [Beam API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam) - Identify the real-world events that materially move your demand
* [Saved Locations API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/saved-locations/overview) - Define and manage reusable business locations for consistent querying across Events, Features, Beam, and Forecasts APIs

## How It Fits Together

PredictHQ APIs work as a pipeline, not in isolation. The [Standard Integration Pattern](integrations/integration-guides/standard-integration-pattern.md) shows the recommended production architecture - from location setup through to forecasting and explainability.

## Example

Use your Beam Analysis ID to pull model-ready ML features for any date range - location, filters, and feature selection are applied automatically.

```python
import requests

response = requests.post(
    url="https://api.predicthq.com/v1/features/",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    },
    json={
        "beam": {
            "analysis_id": "$ANALYSIS_ID"
        },
        "active": {
            "gte": "2026-06-01",
            "lte": "2026-06-30"
        }
    }
)

print(response.json())
```

## AI & Agents

* [Build with AI](ai/build-with-ai.md) - Connect any MCP-compatible AI assistant to PredictHQ APIs through natural language
* [MCP Server](ai/mcp.md) - Query events, demand intelligence, and all PredictHQ APIs without writing code
* [Bolt](ai/bolt.md) - AI-native developer environment built into the WebApp

## Resources

* [API Overview](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/overview) - Authentication, rate limits, and API conventions
* [Guides](getting-started/guides/) - Step-by-step integration guides for core APIs and use cases
* [Python SDK](sdks/python-sdk.md) - The official Python client for the PredictHQ API
* [Data Science Notebooks](getting-started/data-science-notebooks.md) - Jupyter notebooks for Beam, Features API, and demand forecasting
* [System Status](https://www.predicthqstatus.com/) - Live status and incident history for PredictHQ services
