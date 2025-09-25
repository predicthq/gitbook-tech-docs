---
description: Get the list of hierarchies for a Place.
---

# Get Place Hierarchies

{% hint style="info" %}
This endpoint is in Beta.
{% endhint %}

The currently available filters and response data change are subject to change.

This endpoint allows you to get the full place hierarchies for

* a given coordinate
* list of `place_id`.

A place hierarchy is a list of place identifiers and types from the `planet` level down to the `level` specified in your query (please note that `level` defaults to `locality` if not specified in your query).

The response might include more than one hierarchy for a given coordinate. The reason for this is that we try to match the closest place's hierarchy but we also include the closest major city's hierarchy within a radius of 50km. This only applies if the `level` is below `region` and, if it exists, the major city's hierarchy will always be the second item in the list.

For instance, if you specify `?location.origin=47.615337,-122.203981`, which is a coordinate located in Bellevue, Washington, you'll get two hierarchies, one for Bellevue but also one for [Seattle](https://en.wikipedia.org/wiki/Seattle).

{% openapi-operation spec="places-api" path="/v1/places/hierarchies" method="get" %}
[OpenAPI places-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/places-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/places/hierarchies/?location.origin=47.615337,-122.203981" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/places/hierarchies/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "location.place_id": "5809844,6252001"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Places API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Places+API).

## Guides

Below are some guides relevant to this API:

* [Understanding Place Hierarchies](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/geolocation-guides/understanding-place-hierarchies)
