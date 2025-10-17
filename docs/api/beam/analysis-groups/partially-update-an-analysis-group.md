---
description: Partially update an existing Analysis Group.
---

# Partially Update an Analysis Group

{% openapi-operation spec="beam-api" path="/v1/beam/analysis-groups/{group_id}" method="patch" %}
[OpenAPI beam-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/beam-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X PATCH "https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     --data @<(cat <<EOF
    {
        "name": "Analysis Group 2",
    }
    EOF
    )  
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.patch(
    url="https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    },
    json={
        "name": "Analysis Group 2"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Beam API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Beam+API).
