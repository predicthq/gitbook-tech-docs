---
description: Docs, guides, and API references to help you build with PredictHQ.
---

# Introduction

PredictHQ provides structured, verified real-world context and demand-aware features for forecasting, ML, and AI systems. The platform is designed to be integrated directly into production models and decision workflows.

See how others are using it on our [use cases page](https://www.predicthq.com/use-cases).

<a href="getting-started/api-quickstart.md" class="button primary">API Quickstart</a>  <a href="https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/" class="button secondary">API Reference</a>

## Core APIs

* [Events API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events) - Structured, deduplicated real-world events for forecasting, ML and AI systems
* [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) - Aggregated, model-ready event features for forecasting and ML
* [Forecasts API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts) - Event-aware demand forecasts, ready for production
* [Beam API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam) - Identify the real-world events that materially move your demand

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
* [SDKs](sdks/)
