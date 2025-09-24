---
description: >-
  Take the guesswork out of working out a suitable radius around your business
  when searching for events.
---

# Get Suggested Radius

The Suggested Radius API returns a radius that can be used to find  events around a given location. When looking for events around a business location (such as a store, a hotel, or another business location) a key question is how far should you look for events. For example, should you look at events in a 0.5-mile radius, a 2-mile radius, or a 10-mile radius from your location? The Suggested Radius API answers this question by returning a radius based on a number of factors that can be used to retrieve events around a location. This radius returned by the API is commonly used as follows:

* When querying the [Events API](../events/search-events.md) using the `within` parameter.
* When calling the [Features API](../features/get-features.md) with a latitude, longitude, and radius to get aggregated features back for a location.
* For retrieving events in a data lake by setting the radius around a store or location to the suggested radius.
* In-demand forecasting when building event-based features for a location, use this radius when calculating features for a location.
* For use with our Beam product when performing a correlation analysis

The Suggested Radius API is powered by a machine learning model that looks at factors like population density, the events around a location, the customer’s industry, and many other factors to determine the ideal radius.

We'd suggest caching the Suggested Radius API response where possible. The response will only change infrequently and it would be sufficient to refresh the cache once per month.

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
