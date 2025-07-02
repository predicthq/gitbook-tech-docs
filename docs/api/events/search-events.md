---
description: The largest and most accurate source of global real-world event data.
---

# Search Events

{% hint style="info" %}
**Results are limited by your subscription**

Please note that you will not receive an error when requesting a date range or location that is outside of your subscription settings.

This is sometimes confused with missing data. If you're not seeing the results you expect to see then please ensure your subscription covers the location or time period you're searching for.

Your subscription settings can be viewed in our [WebApp](https://control.predicthq.com/settings/plans).
{% endhint %}

{% openapi-operation spec="events-api" path="/v1/events/" method="get" %}
[OpenAPI events-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/events-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="python sdk" %}
Make sure to properly load your access token from an environment variable or other secure method.

```python
from predicthq import Client

phq = Client(access_token="$ACCESS_TOKEN")

for event in phq.events.search(
    place__scope=[5809844],
    category=["conferences", "expos", "concerts", "festivals", "performing-arts", "community", "sports"],
    active__gte="2025-02-01",
    active__lte="2025-04-01",
):
    print(event.rank, event.category, event.title, event.start.strftime("%Y-%m-%d"))

```
{% endtab %}

{% tab title="python" %}
Make sure to properly load your access token from an environment variable or other secure method.

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "category": "conferences,expos,concerts,festivals,performing-arts,community,sports",
        "place.scope": "5809844",
        "active.gte": "2025-03-01",
        "active.lte": "2025-04-01"
    }
)

print(response.json())
```
{% endtab %}

{% tab title="curl" %}
Make sure to properly load your access token from an environment variable or other secure method.

```bash
curl -X GET "https://api.predicthq.com/v1/events/?category=conferences,expos,concerts,festivals,performing-arts,community,sports&place.scope=5809844&active.gte=2025-03-01&active.lte=2025-04-01" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Events API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Events+API).

## Guides

{% hint style="info" %}
**Airport Codes Mapping File**\
Airport codes are mapped to Place IDs. The current mapping of airport code to Place ID can be [found here](https://github.com/predicthq/api-specs/blob/main/data/airport-codes.csv).
{% endhint %}

Below are some guides relevant to this API:

* [Geolocation Guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/geolocation-guides)
* [Date and Time Guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/date-and-time-guides)
* Other [Events API Guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/events-api-guides)
