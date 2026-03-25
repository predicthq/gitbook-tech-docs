---
description: >-
  Take the guesswork out of working out a suitable radius around your business
  when searching for events.
---

# Get Suggested Radius

The Suggested Radius API returns a radius for finding events around a business location. Rather than guessing an appropriate distance, the API calculates a radius based on factors including population density, local event patterns, and industry.

Use the returned radius as the spatial input for Events API queries, Features API calls, Beam, and demand forecasting workflows.

We recommend caching the response and refreshing monthly - the radius for a given location changes infrequently.

{% hint style="success" %}
[Predicted Impact Area](../impact-area/get-impact-area.md) is the successor to this API, providing a more accurate representation of event impact than a radius. Suggested Radius remains available and existing implementations are unaffected.
{% endhint %}

{% openapi-operation spec="suggested-radius-api" path="/v1/suggested-radius/" method="get" %}
[OpenAPI suggested-radius-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/suggested-radius-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/suggested-radius/?location.origin=37.747767,-122.455320&industry=parking&radius_unit=km" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/suggested-radius/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "location.origin": "37.747767,-122.455320",
        "industry": "parking",
        "radius_unit": "km"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Suggested Radius API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Suggested+Radius+API).

## Guides

Below are some guides relevant to this API:

* [Find Events by Latitude/Longitude and Radius](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/geolocation-guides/searching-by-location/find-events-by-latitude-longitude-and-radius)
