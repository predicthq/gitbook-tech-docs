---
description: Search for an existing Analysis Group.
---

# Search Analysis Groups

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/beam/analysis-groups
```

### Query Parameters

<table><thead><tr><th width="260">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><p><code>q</code></p><p>string</p><p>optional</p></td><td><p>Query string to be matched against Group <code>name</code>.</p><p>E.g. <code>?q=MyAnalysisGroup</code></p></td></tr><tr><td><code>status</code><br>string<br>optional</td><td><p>Comma separated list (<code>&#x3C;status1>,&#x3C;status2></code>) used to filter Analysis Groups by their status.<br><br><strong>Possible values:</strong></p><ul><li><code>active</code></li><li><code>deleted</code></li></ul><p>E.g. <code>?status=deleted,active</code></p></td></tr><tr><td><code>sort</code><br>string<br>optional</td><td><p>Comma separated list (<code>&#x3C;sort1>,&#x3C;sort2></code>) used to sort Analysis Groups.<br><br><strong>Possible values:</strong></p><ul><li><code>name</code> - Sort by name A-Z</li><li><code>-name</code> - Sort by name Z-A</li><li><code>created</code> - Sort by created date oldest to newest</li><li><code>-created</code> - Sort by created date newest to oldest</li><li><code>updated</code> - Sort by updated date earliest to latest</li><li><code>-updated</code> - Sort by updated date latest to earliest</li></ul><p>E.g. <code>?sort=name,created</code></p></td></tr><tr><td><code>demand_type.interval</code><br>string<br>optional</td><td><p>Allows to filter Analysis Groups by the demand type of their analyses.<br></p><p><strong>Possible values:</strong></p><ul><li><code>day</code> - for daily groups</li><li><code>week</code> - for weekly groups</li></ul></td></tr><tr><td><code>limit</code><br>number<br>optional</td><td>Limits the length of the returned list. The default <code>limit</code> is <code>10</code>.<br><br>E.g. <code>?limit=20</code></td></tr><tr><td><code>offset</code><br>number<br>optional</td><td>Specifies starting offset of the returned list. The default <code>offset</code> is <code>0</code>.<br><br>E.g. <code>?offset=3</code></td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="190">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>count</code><br>number</td><td>Total number of results found.</td></tr><tr><td><code>groups</code><br>array</td><td><p>List of results where each item is an Analysis Group.</p><p><br>Please refer to the response fields section in <a href="get-an-analysis-group.md">Get an Analysis Group</a> for the structure of each record.</p></td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "count": 1,
    "groups": [
        {
            "name": "My Analysis Group 1",
            "create_dt": "2024-02-26T20:58:27.746530+00:00",
            "update_dt": "2024-02-26T20:58:27.746530+00:00",
            "analysis_ids": [
                "b6_hdcGNc6A",
                "q4BelInRvIU",
                "WwSj8lDeNMU"
            ],
            "processing_completed": {
                "feature_importance": true,
                "excluded_analyses": []
            },
            "status": "active",
            "readiness_status": "ready",
            "user_id": null,
            "processed_dt": "2024-02-26T20:58:29.933984+00:00",
            "demand_type": {
                "interval": "day"
            },
            "group_id": "-NjWQkYXsng"
        }
    ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/beam/analysis-groups?status=active&sort=updated \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/beam/analysis-groups",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "status": "active",
        "sort": "updated"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
