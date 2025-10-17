---
description: Re-run the Beam Analysis Group aggregation process.
---

# Refresh an Analysis Group

{% openapi-operation spec="beam-api" path="/v1/beam/analysis-groups/{group_id}/refresh" method="post" %}
[OpenAPI beam-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/beam-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X POST "https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID/refresh" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.post(
    url="https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID/refresh",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Beam API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Beam+API).
