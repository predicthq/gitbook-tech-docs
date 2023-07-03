# Get an Analysis

## Request

### HTTP Request

<pre class="language-apacheconf"><code class="lang-apacheconf">GET https://api.predicthq.com/v1/beam/analyses/<a data-footnote-ref href="#user-content-fn-1">$analysis_id</a>
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td>analysis_id</td><td>An existing Beam Analysis ID.</td></tr></tbody></table>

## Response

### Response Fields

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "name": "Analysis 1",
    "location": {
        "geopoint": {
            "lat": "-36.849761",
            "lon": "174.7628903"
        },
        "radius": 1.2,
        "unit": "km"
    },
    "rank": {
        "type": "phq",
        "levels": {
            "phq": {
                "min": 51
            }
        }
    },
    "status": "draft",
    "create_dt": "2023-03-01T23:03:19.403859+00:00",
    "update_dt": "2023-03-01T23:49:39.464011+00:00",
    "user_id": null,
    "access_type": "full",
    "processed_dt": "2023-03-01T23:43:52.253150+00:00",
    "readiness_status": "ready",
    "readiness_checks": {
        "date_range": {
            "start": "2017-01-01",
            "end": "2017-12-31"
        },
        "validation_response": {
            "missing_data_percentage": 0.0,
            "consecutive_nan": 0
        }
    },
    "tz": "UTC"
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/beam/analyses/<analysis_id>",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

[^1]: An existing Beam Analysis ID.
