---
description: Search for an existing Analysis.
---

# Search Analyses

## Request

### HTTP Request

```
GET https://api.predicthq.com/v1/beam/analyses
```

### Query Parameters

<table><thead><tr><th width="210">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>status</code><br>string<br>optional</td><td><p>Comma separated list (<code>&#x3C;status1>,&#x3C;status2></code>) used to filter Beam analyses by their status.<br><br><strong>Possible values:</strong></p><ul><li><code>draft</code></li><li><code>active</code></li><li><code>deleted</code></li></ul><p>E.g. <code>?status=draft,active</code></p></td></tr><tr><td><code>readiness_status</code><br>string<br>optional</td><td><p>Comma separated list (<code>&#x3C;readiness_status1>,&#x3C;readiness_status2></code>) used to filter Beam analyses by their readiness status.<br><br><strong>Possible values:</strong></p><ul><li><code>pending</code></li><li><code>failed</code></li><li><code>ready</code></li></ul><p>E.g. <code>?status=pending,ready</code></p></td></tr><tr><td><code>sort</code><br>string<br>optional</td><td><p>Comma separated list (<code>&#x3C;sort1>,&#x3C;sort2></code>) used to sort Beam analyses.<br><br><strong>Possible values:</strong></p><ul><li><code>name</code> - Sort by name A-Z</li><li><code>-name</code> - Sort by name Z-A</li><li><code>created</code> - Sort by created date oldest to newest</li><li><code>-created</code> - Sort by created date newest to oldest</li><li><code>updated</code> - Sort by updated date earliest to latest</li><li><code>-updated</code> - Sort by updated date latest to earliest</li></ul><p>E.g. <code>?sort=name,created</code></p></td></tr><tr><td><code>limit</code><br>number<br>optional</td><td>Limits the length of the Beam analyses list returned. The default <code>limit</code> is <code>10</code>.<br><br>E.g. <code>?limit=20</code></td></tr><tr><td><code>offset</code><br>number<br>optional</td><td>Specifies starting offset of the Beam analyses list returned. The default <code>offset</code> is <code>0</code>.<br><br>E.g. <code>?offset=3</code></td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="190">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>count</code><br>number</td><td>Total number of results found.</td></tr><tr><td><code>analyses</code><br>array</td><td><p>List of results where each item is an Analysis.</p><p><br>Please refer to the response fields section in <a href="get-an-analysis.md#response-fields">Get an Analysis</a> for the structure of each record.</p></td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "count": 1,
    "analyses": [
        {
            "name": "Analysis 1",
            "location": {
                "geopoint": {
                    "lat": "-36.85088270000001",
                    "lon": "174.7644881"
                },
                "radius": 10,
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
            "create_dt": "2021-08-19T23:46:49.172401+00:00",
            "update_dt": "2021-08-20T00:20:19.770461+00:00",
            "user_id": "user_id",
            "access_type": "full",
            "processed_dt": "2021-08-19T23:50:53.456047+00:00",
            "readiness_status": "ready",
            "readiness_checks": {
                "date_range": {
                    "start": "2021-01-01",
                    "end": "2021-12-31"
                },
                "validation_response": {
                    "missing_data_percentage": 0.0,
                    "consecutive_nan": 0
                }
            },
            "tz": "Pacific/Auckland",
            "analysis_id": "analysis_id"
        }
    ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/beam/analyses?status=draft&sort=updated \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/beam/analyses",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "status": "draft",
        "sort": "updated"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [Beam Data Science Guide](../../getting-started/guides/beam-guides/beam-data-science-guide.md)
