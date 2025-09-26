---
description: >-
  Identify dates with surges in demand caused by multiple events happening at
  the same time and location.
---

# Get Demand Surges

The Demand Surge API can be used to quickly scan a period of 90 days for abnormal increases in attendance for a given area. The API calculates the mean attendance for your requested location over the next 90 days after the `date_from` date and returns all the dates where attendance is a certain number of standard deviations over the mean. This is represented by the `min_surge_intensity` parameter, that corresponds to the number of standard deviations the API will look for.

Once you have identified the dates with the surge in demand, you can use:

* Our [Events API](../events/search-events.md) to find the names, descriptions, locations, and other details of the events that constitute the surges.
* Our [Features API](../features/get-features.md) to get Machine Learning features for events in your searched date range.

{% openapi-operation spec="demand-surge-api" path="/v1/demand-surge/" method="get" %}
[OpenAPI demand-surge-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/demand-surge-api.yaml)
{% endopenapi-operation %}

## OpenAPI Spec

The OpenAPI spec for Demand Surge API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Demand+Surge+API).

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/demand-surge/?date_from=2021-05-12&min_surge_intensity=m&location.place_id=2643743" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/demand-surge/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "date_from": "2021-05-12",
        "min_surge_intensity": "m",
        "location.place_id": "2643743"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
