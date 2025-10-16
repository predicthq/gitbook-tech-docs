---
description: Create a new Loop Link to begin submitting events and feedback.
---

# Create a Loop Link

{% openapi-operation spec="loop-api" path="/v1/loop/links" method="post" %}
[OpenAPI loop-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/loop-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X POST "https://api.predicthq.com/v1/loop/links" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     --data @<(cat <<EOF
    {
        "name": "Hotel A",
        "expire_dt": "2021-11-01T11:12:34",
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

response = requests.post(
    url="https://api.predicthq.com/v1/loop/links",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    },
    json={
        "name": "Hotel A",
        "expire_dt": "2021-11-01T11:12:34",
        "metadata": {
            "hotel_id": "123456789"
        }
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Loop API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Loop+API).

## Guides

Below are some guides relevant to this API:

* [Integrate with Loop Links](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/integrations/integration-guides/integrate-with-loop-links)
