---
description: Get an existing Saved Location.
---

# Get a Saved Location

{% openapi-operation spec="saved-locations-api" path="/v1/saved-locations/{location_id}" method="get" %}
[OpenAPI saved-locations-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/saved-locations-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl --location 'https://api.predicthq.com/v1/saved-locations/_4Dl3p4Q2zl4ifMjG4Z3ew' \
--header 'Authorization: Bearer TOKEN'
```
{% endtab %}

{% tab title="python" %}
```python
import requests

url = "https://api.predicthq.com/v1/saved-locations/_4Dl3p4Q2zl4ifMjG4Z3ew"
headers = {
  'Authorization': 'Bearer TOKEN'
}

response = requests.request("GET", url, headers=headers)

print(response.text)
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Saved Locations API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Saved+Locations+API).

## Guides

Below are some guides relevant to this API:

* [Working with Location-Based Subscriptions](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/geolocation-guides/searching-by-location/working-with-location-based-subscriptions)
