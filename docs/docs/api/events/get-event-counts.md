---
description: Get the count of events by category, PHQ Label, and more.
---

# Get event counts

{% openapi-operation spec="events-api" path="/v1/events/count/" method="get" %}
[OpenAPI events-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/events-api.yaml)
{% endopenapi-operation %}

## OpenAPI spec

See the [Events API OpenAPI spec](https://api.predicthq.com/docs/?urls.primaryName=Events+API).

## Examples

The following examples get event counts for New Zealand:

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/events/count/?country=NZ" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $API_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/count/",
    headers={
      "Authorization": "Bearer $API_TOKEN",
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
