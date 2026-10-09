---
description: >-
  Loop settings control how the Loop UI displays certain elements.
---

# Get Loop settings

Particularly for the Loop Links UI we take the `org_name` from Settings and display it at the top of the page.

{% openapi-operation spec="loop-api" path="/v1/loop/settings" method="get" %}
[OpenAPI loop-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/loop-api.yaml)
{% endopenapi-operation %}

## Examples

The following examples get the Loop settings:

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/loop/settings" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $API_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/loop/settings",
    headers={
      "Authorization": "Bearer $API_TOKEN",
      "Accept": "application/json"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## OpenAPI spec

See the [Loop API OpenAPI spec](https://api.predicthq.com/docs/?urls.primaryName=Loop+API).

## Guides

ow are some guides relevant to this API:

* [Integrate with Loop Links](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/integrations/integration-guides/integrate-with-loop-links)
