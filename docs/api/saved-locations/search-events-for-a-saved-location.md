---
description: Search for events happening in an existing Saved Location.
---

# Search Events for a Saved Location

{% openapi-operation spec="saved-locations-api" path="/v1/saved-locations/{location_id}/insights/events" method="get" %}
[OpenAPI saved-locations-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/saved-locations-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl --location 'https://api.predicthq.com/v1/saved-locations/0b6ZrOnTdB2Y7k4zC_9qBg/insights/events?date_range_type=next_90d&category=public-holidays%2Csports&sort=start' \
--header 'Authorization: Bearer TOKEN'
```
{% endtab %}

{% tab title="python" %}
```python
import requests

url = "https://api.predicthq.com/v1/saved-locations/0b6ZrOnTdB2Y7k4zC_9qBg/insights/events?date_range_type=next_90d&category=public-holidays,sports&sort=start"

payload={}
headers = {
  'Authorization': 'Bearer TOKEN'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Saved Locations API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Saved+Locations+API).

## Guides

Below are some guides relevant to this API:

* [Working with Location-Based Subscriptions](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/geolocation-guides/searching-by-location/working-with-location-based-subscriptions)
