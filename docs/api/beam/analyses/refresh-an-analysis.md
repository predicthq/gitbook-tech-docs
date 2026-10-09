---
description: Rerun the Beam correlation and analysis process.
---

# Refresh an Analysis

{% openapi-operation spec="beam-api" path="/v1/beam/analyses/{analysis_id}/refresh" method="post" %}
[OpenAPI beam-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/beam-api.yaml)
{% endopenapi-operation %}

## Examples

The following examples refresh an Analysis:

{% tabs %}
{% tab title="curl" %}
```bash
curl -X POST "https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/refresh" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $API_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.post(
    url="https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/refresh",
    headers={
        "Authorization": "Bearer $API_TOKEN",
        "Accept": "application/json"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

## OpenAPI spec

Read the [Beam API OpenAPI spec](https://api.predicthq.com/docs/?urls.primaryName=Beam+API).

## Guides

The following guides are relevant to this API:

* [Beam guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/beam-guides)
