---
description: Delete an existing Analysis Group.
---

# Delete an Analysis Group

{% openapi-operation spec="beam-api" path="/v1/beam/analysis-groups/{group_id}" method="delete" %}
[OpenAPI beam-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/beam-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X DELETE "https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.delete(
    url="https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Beam API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Beam+API).
