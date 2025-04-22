---
description: Get the count of events by category, PHQ Label and more.
---

# Get Event Counts

{% openapi-operation spec="events-api" path="/v1/events/count/" method="get" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

## OpenAPI Spec

The OpenAPI spec for Events API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Events+API).

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/events/count/?country=NZ" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/count/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "country": "NZ"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
