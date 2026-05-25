---
description: >-
  Get your API key, make your first call, and understand how PredictHQ fits into
  a production integration.
---

# API Quickstart

## What you need

1. A PredictHQ account - [log in](https://control.predicthq.com/) or [sign up for free](https://signup.predicthq.com/).
2. An API Key - create one in the steps below.

## Create an API Key

1. Log into the [WebApp](https://control.predicthq.com/tokens) and go to **API Tools → API Tokens**
2. Click **Create Token**, enter a name, and click **Create**
3. Click **Copy Token** - store it somewhere safe, it won't be shown again

Use your API key in the `Authorization` header of every API request:

```
Authorization: Bearer $API_KEY
```

## Make Your First Call

The Events API returns structured, deduplicated real-world events. Use it to verify your API key is working and to explore what events look like in the response.

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
        "Authorization": "Bearer $API_KEY",
        "Accept": "application/json"
    },
    params={
        "place.scope": "5128581",  # New York City
        "category": "concerts,sports,conferences",
        "active.gte": "2026-06-01",
        "active.lte": "2026-06-30",
        "limit": 10
    }
)

print(response.json())
```

{% hint style="info" %}
**Note:** The Events API is for discovery and explainability - understanding which events are happening and why they matter. For demand forecasting and ML, use the Features API instead. See [Which API Should I Use](core-concepts/which-api-should-i-use.md) for guidance on which API to use for your use case.
{% endhint %}

## How PredictHQ APIs Work Together

A single API call is not a production integration. PredictHQ APIs are designed to work as a pipeline:

1. **Saved Locations** - define your business locations once using `origin_geojson`. Predicted Impact Area is calculated automatically and stored against each location.
2. **Beam** - run a Beam analysis per location using your historical demand data. Beam identifies which event categories actually drive demand at each location and returns an `analysis_id`.
3. **Features API** - call the Features API with your `analysis_id` to retrieve model-ready ML features, automatically scoped and filtered to your location.
4. **Events API** - use the Events API with your `analysis_id` to retrieve the specific events driving demand - for explainability and operational context.

The [Standard Integration Pattern](../integrations/integration-guides/standard-integration-pattern.md) shows the full recommended architecture, including refresh cadence and data storage patterns.

## What to Do Next

**I want to build a demand forecasting model** → Start with [Saved Locations](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/saved-locations/overview), then run [Beam](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/overview), then call the [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) with your `analysis_id`

**I want event-driven forecasts without building a model** → Go straight to the [Forecasts API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts/overview)

**I want to connect an AI assistant to PredictHQ** → Set up the [MCP Server](../ai/mcp.md)

**I want to understand the full integration architecture** → Read the [Standard Integration Pattern](../integrations/integration-guides/standard-integration-pattern.md)
