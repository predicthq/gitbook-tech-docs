---
description: Get Feature Importance data for an Analysis Group.
---

# Get Feature Importance for an Analysis Group

This endpoint provides Feature Importance results aggregated across the Analyses in an existing Analysis Group, and returns a list of feature groups with associated Features API features and group p-values.

{% openapi-operation spec="beam-api" path="/v1/beam/analysis-groups/{group_id}/feature-importance" method="get" %}
[OpenAPI beam-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/beam-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID/feature-importance" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID/feature-importance",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Beam API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Beam+API).
