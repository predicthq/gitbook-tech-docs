---
hidden: true
noIndex: true
---

# Search Events (OpenAPI Test)

## Schema

{% openapi src="../../.gitbook/assets/events-api.yaml" path="/v1/events/" method="get" %}
[events-api.yaml](../../.gitbook/assets/events-api.yaml)
{% endopenapi %}

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

## Guides

Below are some guides relevant to this API:

* [Geolocation Guides](../../getting-started/guides/geolocation-guides/)
* [Date and Time Guides](../../getting-started/guides/date-and-time-guides/)
* Other [Event API Guides](../../getting-started/guides/events-api-guides/)

