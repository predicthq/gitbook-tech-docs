---
description: Delete an existing Saved Location.
---

# Delete a Saved Location

{% openapi-operation spec="saved-locations-api" path="/v1/saved-locations/{location_id}" method="delete" %}
[OpenAPI saved-locations-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/saved-locations-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X DELETE "https://api.predicthq.com/v1/saved-locations/$LOCATION_ID" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.delete(
    url="https://api.predicthq.com/v1/saved-locations/$LOCATION_ID",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Saved Locations API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Saved+Locations+API).

## Guides

Below are some guides relevant to this API:

* [Working with Location-Based Subscriptions](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/geolocation-guides/searching-by-location/working-with-location-based-subscriptions)
