---
description: Create a new Saved Location to begin seeing insights.
---

# Create a Saved Location

{% openapi-operation spec="saved-locations-api" path="/v1/saved-locations" method="post" %}
[OpenAPI saved-locations-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/saved-locations-api.yaml)
{% endopenapi-operation %}

## Examples

### Create using point and radius

To create a Saved Location from a point and radius, use this request:

{% tabs %}
{% tab title="curl" %}
```bash
curl --location 'https://api.predicthq.com/v1/saved-locations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer TOKEN' \
--data '{
    "name": "Example of creating a saved location",
    "geojson": {
        "type": "Feature",
        "properties": {
            "radius": 2.23,
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

url = "https://api.predicthq.com/v1/saved-locations"

payload = json.dumps({
  "name": "Example of creating a saved location",
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

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```
{% endtab %}
{% endtabs %}

### Create using place ID

To create a Saved Location from a Place ID, use this request:

{% tabs %}
{% tab title="curl" %}
```bash
curl --location 'https://api.predicthq.com/v1/saved-locations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer TOKEN' \
--data '{
    "name": "Test with place_id",
    "place_ids": [ 2750405 ]
}'
```
{% endtab %}

{% tab title="python" %}
```python
import requests
import json

url = "https://api.predicthq.com/v1/saved-locations"

payload = json.dumps({
  "name": "Example with place_id",
  "place_ids": [
    2750405
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer TOKEN'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```
{% endtab %}
{% endtabs %}

## OpenAPI spec

See the [Saved Locations API OpenAPI spec](https://api.predicthq.com/docs/?urls.primaryName=Saved+Locations+API).

## Guides

These guides are relevant to this API:

* [Working with location-based subscriptions](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/geolocation-guides/searching-by-location/working-with-location-based-subscriptions)
