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

<a href="getting-started/api-quickstart.md" class="button primary">API Quickstart</a>  <a href="api/overview/" class="button secondary">API Reference</a>

## Core APIs

* [Events API](api/events/) - Clean and enriched real-world event data
* [Features API](api/features/) - Pre-aggregated ML features
* [Forecasts API](api/forecasts/) - Demand forecasting, out of the box
* [Beam API](api/beam/) - Filter out the noise

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

* [API Overview](api/overview/)
* [Guides](getting-started/guides/)
* [SDKs](integrations/sdks/)
