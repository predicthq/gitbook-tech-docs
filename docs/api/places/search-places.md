---
description: Search for a Place.
---

# Search Places

The Places API gives you a read-only interface to PredictHQ's places data. A place represents a [Geonames](http://www.geonames.org/) Feature, which can be either an Area, an Administrative Feature, or a Populated Place.

Places can be used to search and filter events using named geographic features rather than a radius, latitude and longitude (see events' `place.scope` and `place.exact` parameters). This is helpful when searching for all events that apply to a continent, country, state, region, province, county or city.

{% openapi-operation spec="places-api" path="/v1/places" method="get" %}
[OpenAPI places-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/places-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/places/?q=New+York&limit=5" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/places/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "q": "New York",
        "limit": 5
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
* [Find Events by Place ID](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/geolocation-guides/searching-by-location/find-events-by-place-id)
* [Find Broadcasts by County Place ID](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/live-tv-event-guides/find-broadcasts-by-county-place-id)
