---
description: Get the count of Live TV broadcasts by category, label and more.
---

# Get Broadcasts Count

{% openapi-operation spec="broadcasts-api" path="/v1/broadcasts/count/" method="get" %}
[OpenAPI broadcasts-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/broadcasts-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/broadcasts/count/?event.event_id=AdKtL974inQB7GURRd" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/broadcasts/count",
    headers={
      "Accept": "application/json",
      "Authorization": "Bearer $ACCESS_TOKEN"
    },
    params={
        "event.event_id": "AdKtL974inQB7GURRd"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Broadcasts API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Broadcasts+API).

## Guides

Below are some guides relevant to this API:

* [Live TV Event Guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/live-tv-event-guides)
