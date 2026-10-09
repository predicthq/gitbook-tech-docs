---
description: Get an existing Analysis.
---

# Get an Analysis

{% openapi-operation spec="beam-api" path="/v1/beam/analyses/{analysis_id}" method="get" %}
[OpenAPI beam-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/beam-api.yaml)
{% endopenapi-operation %}

## Examples

Get an Analysis by its ID:

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $API_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/beam/analyses/<analysis_id>",
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

Read the [Beam API OpenAPI spec](https://api.predicthq.com/docs/?urls.primaryName=Beam+API).

## Guides

The following guides are relevant to this API:

* [Beam guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/beam-guides)
