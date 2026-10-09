---
description: Use PowerBI's AutoML models to forecast demand using PredictHQ technologies.
---

# Forecasting demand in Power BI with event features

## Tools

### PredictHQ

PredictHQ tools and resources:

* [Features API](./)
* [Beam](../beam-guides/)
* [Predicted Impact Area](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/impact-area/get-impact-area)
* [WebApp](https://control.predicthq.com)
* Tutorial: [improving-demand-forecasting-models-with-event-features.md](improving-demand-forecasting-models-with-event-features.md "mention")

### Microsoft

Microsoft tools and resources:

* [PowerBI AutoML](https://learn.microsoft.com/en-us/power-bi/transform-model/dataflows/dataflows-machine-learning-integration)

## Guide

{% embed url="https://vimeo.com/905617307" %}
Xuxu Wang (CDO) demoing this approach with PowerBI
{% endembed %}

### Base model in PowerBI

The starting point is developing a base model in PowerBI (without PredictHQ data). Using a combination of historical data and time trend features, we developed a base model in PowerBI. This initial version yielded a performance of 48%, a good starting point for further enhancement.

<figure><img src="../../../.gitbook/assets/powerbi-screenshot.png" alt="PowerBI screen showing the base model's performance of 48%, built without PredictHQ data"><figcaption><p>Base model performance in PowerBI (without PredictHQ data)</p></figcaption></figure>

### Improving base model results with PredictHQ

From here, follow the [improving-demand-forecasting-models-with-event-features.md](improving-demand-forecasting-models-with-event-features.md "mention") tutorial book which helps you work out a set of PredictHQ features that are most impactful to your demand using [Beam](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam) and [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features). When we have the relevant PredictHQ features we can enhance the model's accuracy.

### Predicted Impact Area

Most teams start with a fixed radius when scoping events around a location. The problem is that the distance over which events influence demand varies—by industry, by location type, and by how people actually move in that area. A radius that works in one market will miss impact or introduce noise in another.

The Predicted Impact Area API returns a location and industry-specific polygon boundary that reflects where event-driven demand impact actually occurs. PredictHQ calibrates boundaries against real demand and event data across industries and geographies.

The recommended approach is to use Saved Locations. When you create a location using `origin_geojson` without specifying a `geojson` area, PredictHQ calculates Predicted Impact Area automatically and stores it against that location. You can then use the `location_id` across all PredictHQ APIs—Events, Features, and Beam—without needing to manage the boundary yourself.

The following example requests the Predicted Impact Area for a location:

```python
import httpx

response = httpx.get(
    "https://api.predicthq.com/v1/impact-area/",
    headers={
        "Authorization": "Bearer YOUR_PREDICTHQ_API_TOKEN",
        "Accept": "application/json",
    },
    params={
        "location.origin": "45.5051,-122.6750",
        "industry": "restaurants",
    },
)

print(response.json())
```

### Demand decomposition and anomaly detection using Beam

Next, the Beam API decomposes our demand data into baseline and remainders. This separation allows us to distinguish regular demand from anomalies and understand the factors driving these demand anomalies, providing a foundation for a more targeted forecasting approach.

<figure><img src="../../../.gitbook/assets/beam-result-screenshot.png" alt="WebApp screen showing the Beam correlation results for the demand data"><figcaption><p>Beam correlation results shown in the WebApp</p></figcaption></figure>

### Feature Importance using Beam

We then utilized Beam's [Feature Importance API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/analyses/get-feature-importance) to evaluate the impact of various events on demand fluctuations. This API helped us identify which events significantly influenced demand, informing our model about the types of events to prioritize in our forecasting.

<figure><img src="../../../.gitbook/assets/feature-importance-result-screenshot.png" alt="WebApp screen showing the Feature Importance results that rank events by their influence on demand"><figcaption><p>Feature Importance results shown in the WebApp</p></figcaption></figure>

### Forecast-Ready Features using Features API

Finally, using the insights from the Feature Importance API, we employed the Features API to integrate detailed, relevant event data into our model. This precise merging of event data directly correlated with a notable improvement in our model's performance.

<figure><img src="../../../.gitbook/assets/features-table-screenshot.png" alt="Table combining Beam results and Features API event features for each date"><figcaption><p>Beam and Features API results</p></figcaption></figure>

### Improve model performance with PredictHQ data

Upon integrating this data into PowerBI, we developed an advanced model that combined both historical data and PredictHQ's event data. The outcome was a significant leap in performance, reaching 75%.

<figure><img src="../../../.gitbook/assets/powerbi-improved-perf-screenshot.png" alt="PowerBI screen showing the improved model performance of 75% with PredictHQ data"><figcaption><p>75% performance in PowerBI using PredictHQ data</p></figcaption></figure>

### Conclusion

This demonstration not only underlines the effectiveness of combining PredictHQ's technology with PowerBI but also opens up new avenues for accurate demand forecasting across various industries.
