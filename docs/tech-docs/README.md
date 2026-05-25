---
description: Docs, guides, and API references to help you build with PredictHQ.
---

# Introduction

PredictHQ provides structured, verified real-world context and demand-aware features for forecasting, ML, and AI systems. The platform is designed to be integrated directly into production models and decision workflows.

See how others are using it on our [use cases page](https://www.predicthq.com/use-cases).

<a href="getting-started/api-quickstart.md" class="button primary">API Quickstart</a> <a href="https://app.gitbook.com/o/WGid6DiA3ccvlkmvc17s/s/kEFs8urDbSJqBmXUI3Lv/" class="button secondary">API Reference</a>

## Core APIs

* [Events API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events) - Structured, deduplicated real-world events for discovery, explainability, and building trust in AI-driven decisions
* [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) - Pre-built, model-ready demand features aggregated from real-world events
* [Forecasts API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts) - Event-driven demand forecasts without building or maintaining your own model
* [Beam API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam) - Identify the real-world events that materially move your demand
* [Saved Locations API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/saved-locations/overview) - Define and manage reusable business locations for consistent querying across Events, Features, Beam, and Forecasts APIs

## Example

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "q": "taylor swift"
    }
)

print(response.json())
```

## Dev Resources

* [API Overview](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/overview)
* [Guides](getting-started/guides/)
* [SDKs](/broken/pages/twewWeTyZJZV3NNEcFKM)
