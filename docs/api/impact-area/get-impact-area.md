---
description: >-
  Determine the area around a location where events are likely to influence
  demand.
---

# Get Predicted Impact Area

Most teams start with a fixed radius when scoping events around a location. The problem is that the distance over which events influence demand varies - by industry, by location type, and by how people actually move in that area. A radius that works in one market will miss impact or introduce noise in another.

Predicted Impact Area returns a location and industry-specific boundary that reflects where event-driven demand impact actually occurs. Boundaries are calibrated against real demand and event data across industries and geographies.

Use it as the spatial input for Events API queries, Features API calls, and Beam. Getting scope right at this step improves the quality of everything downstream.

{% hint style="info" %}
Predicted Impact Area is the successor to the Suggested Radius API. It provides a more accurate representation of event impact than a radius-based approach.
{% endhint %}

### Using Predicted Impact Area

The recommended approach is to use Saved Locations. When you create a location using `origin_geojson` without specifying a `geojson` area, Predicted Impact Area is calculated automatically and stored against that location. You can then use the `location_id` across all PredictHQ APIs - Events, Features, and Beam - without needing to manage the boundary yourself.

Polygon-based filtering across PredictHQ APIs requires a saved location. To use a Predicted Impact Area boundary in API queries, create a saved location first and reference it by `location_id`.

{% openapi-operation spec="impact-area-api" path="/v1/impact-area/" method="get" %}
[OpenAPI impact-area-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/impact-area-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/impact-area/?location.origin=37.747767,-122.455320&industry=parking" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/impact-area/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "location.origin": "37.747767,-122.455320",
        "industry": "parking"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Impact Area API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Predicted+Impact+Area+API).

