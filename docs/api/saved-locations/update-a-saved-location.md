---
description: Update (replace) an existing Saved Location.
---

# Update a Saved Location

{% openapi-operation spec="saved-locations-api" path="/v1/saved-locations/{location_id}" method="put" %}
[OpenAPI saved-locations-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/saved-locations-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl --location --request PUT 'https://api.predicthq.com/v1/saved-locations/5BcRstnNPjXl-fiB_0TQJg' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer TOKEN' \
--data '{
    "name": "S Las Vegas Blvd, Las Vegas (NV), US",
    "labels": [],
    "geojson": {
        "type": "Feature",
        "properties": {
            "radius": 1,
            "radius_unit": "mi"
        },
        "geometry": {
            "type": "Point",
            "coordinates": [
                -115.1728484,
                36.1147065
            ]
        }
    }
}'
```
{% endtab %}

{% tab title="python" %}
```python
import requests
import json

url = "https://api.predicthq.com/v1/saved-locations/5BcRstnNPjXl-fiB_0TQJg"

payload = json.dumps({
  "name": "S Las Vegas Blvd, Las Vegas (NV), US",
  "labels": [],
  "geojson": {
    "type": "Feature",
    "properties": {
      "radius": 1,
      "radius_unit": "mi"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [
        -115.1728484,
        36.1147065
      ]
    }
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer TOKEN'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Saved Locations API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Saved+Locations+API).

## Guides

Below are some guides relevant to this API:

* [Working with Location-Based Subscriptions](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/geolocation-guides/searching-by-location/working-with-location-based-subscriptions)
