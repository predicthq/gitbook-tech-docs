---
description: Search for an existing Analysis.
---

# Search Analyses

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/beam/analyses
```

### Query Parameters

<table><thead><tr><th width="248">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>status</code><br>string</td><td><p>Comma separated list (<code>&#x3C;status1>,&#x3C;status2></code>) used to filter Beam analyses by their status.<br><br><strong>Possible values:</strong></p><ul><li><code>active</code></li><li><code>deleted</code></li></ul><p>E.g. <code>?status=active,deleted</code></p></td></tr><tr><td><code>readiness_status</code><br>string</td><td><p>Comma separated list (<code>&#x3C;readiness_status1>,&#x3C;readiness_status2></code>) used to filter Beam analyses by their readiness status.<br><br><strong>Possible values:</strong></p><ul><li><code>pending</code></li><li><code>failed</code></li><li><code>ready</code></li></ul><p>E.g. <code>?status=pending,ready</code></p></td></tr><tr><td><code>group_id</code><br>string</td><td>Comma separated list of Analysis Group ID. Analyses that belong to this group will be returned.<br><br>E.g., <code>?group_id=H3ED1zxXqAY</code></td></tr><tr><td><code>demand_type.interval</code><br>string</td><td><p>Allows to filter analyses by their detected demand type.<br></p><p><strong>Possible values:</strong></p><ul><li><code>day</code> - for daily analyses. Note that empty analyses are assumed to be daily</li><li><code>week</code> - for weekly analyses</li></ul></td></tr><tr><td><code>demand_type.industry</code><br>string</td><td><p>Allows to filter analyses by one or more industries.<br></p><p>Possible values:</p><ul><li><code>accommodation</code></li><li><code>cpg</code></li><li><code>tourism</code></li><li><code>marketing</code></li><li><code>parking</code></li><li><code>restaurants</code></li><li><code>retail</code></li><li><code>transportation</code></li><li><code>other</code></li></ul><p>E.g. <code>?demand_type.industry=accommodation,tourism</code></p></td></tr><tr><td><p><code>external_id</code></p><p>string</p></td><td>Comma-separated list of External IDs.<br><br>E.g., <code>?external_id=id1,id2</code></td></tr><tr><td><p><code>label</code></p><p>string</p></td><td><p>Comma-separated list of labels.</p><p>E.g. <code>?label=label1,label2,label3</code></p></td></tr><tr><td><code>sort</code><br>string</td><td><p>Comma separated list (<code>&#x3C;sort1>,&#x3C;sort2></code>) used to sort Beam analyses.<br><br><strong>Possible values:</strong></p><ul><li><code>name</code> - Sort by name A-Z</li><li><code>-name</code> - Sort by name Z-A</li><li><code>created</code> - Sort by created date oldest to newest</li><li><code>-created</code> - Sort by created date newest to oldest</li><li><code>updated</code> - Sort by updated date earliest to latest</li><li><code>-updated</code> - Sort by updated date latest to earliest</li></ul><p>E.g. <code>?sort=name,created</code></p></td></tr><tr><td><code>limit</code><br>number</td><td>Limits the length of the Beam analyses list returned. The default <code>limit</code> is <code>10</code>.<br><br>E.g. <code>?limit=20</code></td></tr><tr><td><code>offset</code><br>number</td><td>Specifies starting offset of the Beam analyses list returned. The default <code>offset</code> is <code>0</code>.<br><br>E.g. <code>?offset=3</code></td></tr></tbody></table>

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
            "demand_type": {
                "interval": "week",
                "week_start_day": "sunday"
            },
            "analysis_id": "analysis_id",
            "external_id": "external_id",
            "label": ["label1", "label2", "label3"]
        }
    ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/beam/analyses?status=draft&sort=updated" \
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

* [beam-guides](../../getting-started/guides/beam-guides/ "mention")
