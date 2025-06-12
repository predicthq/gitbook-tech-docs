---
description: Docs, guides, and API references to help you build with PredictHQ.
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Introduction

PredictHQ helps you build smarter models and products with real-world demand intelligence. Access high-quality event data, ready-to-use ML features, and a forecasting API designed for real impact. See how others are using it on our [use cases page](https://www.predicthq.com/use-cases).

<a href="getting-started/api-quickstart.md" class="button primary">API Quickstart</a>  <a href="broken-reference" class="button secondary">API Reference</a>

## Core APIs

* [Events API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events) - Clean and enriched real-world event data
* [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) - Pre-aggregated ML features
* [Forecasts API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts) - Demand forecasting, out of the box
* [Beam API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam) - Filter out the noise

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

* [API Overview](broken-reference)
* [Guides](getting-started/guides/)
* [SDKs](integrations/sdks/)
