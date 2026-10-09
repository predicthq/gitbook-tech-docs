---
description: Get relevant ML features based on a Beam Analysis.
---

# Get Feature Importance

{% hint style="info" %}
To get these ML features from the Features API for your models, use the Beam `analysis_id` in your Features API request.
{% endhint %}

{% openapi-operation spec="beam-api" path="/v1/beam/analyses/{analysis_id}/feature-importance" method="get" %}
[OpenAPI beam-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/beam-api.yaml)
{% endopenapi-operation %}

## Examples

The following examples get the Feature Importance for an Analysis:

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/feature-importance" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $API_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/beam/analyses/<analysis_id>/feature-importance",
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

See the [Beam API OpenAPI spec](https://api.predicthq.com/docs/?urls.primaryName=Beam+API).

## Guides

These guides are relevant to this API:

* [Beam guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/beam-guides)
