---
description: Update (replace) an existing Analysis.
---

# Update an Analysis

{% openapi-operation spec="beam-api" path="/v1/beam/analyses/{analysis_id}" method="put" %}
[OpenAPI beam-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/beam-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X PUT "https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     --data @<(cat <<EOF
    {
        "name": "Analysis 2",
        "location": {
        "geopoint": {
            "lat": "-36.849761",
            "lon": "174.7628903"
            },
            "radius": 1.2,
            "unit": "km"
        },
        "rank": {
            "type": "phq"
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
    url="https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    },
    json={
        "name": "Analysis 2",
        "location": {
            "geopoint": {
                "lat": "-36.849761",
                "lon": "174.7628903"
            },
            "radius": 1.2,
            "unit": "km"
        },
        "rank": {
            "type": "phq"
        }
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

## OpenAPI Spec

The OpenAPI spec for Beam API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Beam+API).

## Guides

Below are some guides relevant to this API:

* [Beam Guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/beam-guides)
