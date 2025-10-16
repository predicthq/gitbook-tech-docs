---
description: Update (replace) an existing Loop Link.
---

# Update a Loop Link

{% openapi-operation spec="loop-api" path="/v1/loop/links/{link_id}" method="put" %}
[OpenAPI loop-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/loop-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X PUT "https://api.predicthq.com/v1/loop/links/$LINK_ID" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     --data @<(cat <<EOF
    {
        "name": "Hotel A",
        "expire_dt": "2024-12-31T00:00:00",
        "metadata": {
            "hotel_id": "123456789"
        }
    }
    EOF
    )
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.put(
    url="https://api.predicthq.com/v1/loop/links/$LINK_ID",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    },
    json={
        "name": "Hotel A",
        "expire_dt": "2024-12-31T00:00:00",
        "metadata": {
            "hotel_id": "123456789"
        }
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
