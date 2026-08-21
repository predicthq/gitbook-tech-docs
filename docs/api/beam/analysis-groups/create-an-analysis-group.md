---
description: >-
  Creating an Analysis Group allows to aggregate Feature Importance for a number
  of Analyses
---

# Create an Analysis Group

{% openapi-operation spec="beam-api" path="/v1/beam/analysis-groups" method="post" %}
[OpenAPI beam-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/beam-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X POST "https://api.predicthq.com/v1/beam/analysis-groups" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $API_TOKEN" \
     --data @<(cat <<EOF
    {
        "name": "Analysis Group 1",
        "analysis_ids": [
            "zRa_kk7MlAA",
            "3aR-gbJp98I",
            "JBb08XsZqAo",
            "q9iX2XqFBxM"
        ]
    }
    EOF
    )
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.post(
    url="https://api.predicthq.com/v1/beam/analysis-groups",
    headers={
        "Authorization": "Bearer $API_TOKEN",
        "Accept": "application/json"
    },
    json={
        "name": "Analysis Group 1",
        "analysis_ids": [
            "zRa_kk7MlAA",
            "3aR-gbJp98I",
            "JBb08XsZqAo",
            "q9iX2XqFBxM",
        ],
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Best Practices

See [ML Features by Group](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/beam-guides/ml-features-by-group) for best practices on grouping analyses.

## OpenAPI Spec

The OpenAPI spec for Beam API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Beam+API).
