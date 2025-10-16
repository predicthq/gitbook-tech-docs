---
description: Delete an existing Loop Link.
---

# Delete a Loop Link

{% openapi-operation spec="loop-api" path="/v1/loop/links/{link_id}" method="delete" %}
[OpenAPI loop-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/loop-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X DELETE "https://api.predicthq.com/v1/loop/links/$LINK_ID" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.delete(
    url="https://api.predicthq.com/v1/loop/links/$LINK_ID",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Loop API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Loop+API).

## Guides

ow are some guides relevant to this API:

* [Integrate with Loop Links](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/integrations/integration-guides/integrate-with-loop-links)
