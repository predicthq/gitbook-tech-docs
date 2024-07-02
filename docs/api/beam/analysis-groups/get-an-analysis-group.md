---
description: Get an existing Analysis Group.
---

# Get an Analysis Group

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/beam/analysis-groups/$group_id
```

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>group_id</code></td><td>An existing Beam Analysis Group ID.</td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="219">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>name</code><br>string</td><td>Name of the Analysis Group.<br><br>E.g. <code>My Analysis Group 1</code></td></tr><tr><td><code>create_dt</code><br>string</td><td><p>The creation date time for the Analysis Group in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>.</p><p><br>E.g. <code>2022-04-26T11:46:24+00:00</code></p></td></tr><tr><td><code>update_dt</code><br>string</td><td><p>The last update date time for the Analysis Group in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>.</p><p><br>E.g. <code>2022-04-26T11:46:24+00:00</code></p></td></tr><tr><td><code>processed_dt</code><br>string</td><td><p>The date time the Analysis Group was last processed in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>.</p><p><br>E.g. <code>2022-04-26T11:46:25+00:00</code></p></td></tr><tr><td><code>user_id</code><br>string</td><td><p>The ID of the user who created the Analysis Group. This is present for Analysis Groups created in Control Center. For Analysis Groups created via the API this field will not be populated.</p><p><br>E.g. <code>hjqkKozgS8mm</code></p></td></tr><tr><td><code>analysis_ids</code><br>string[]</td><td><p>A list of strings containing the IDs of Analyses included in this Group.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
    "analysis_ids": [
        "0GTpLZ522Bc",
        "6OK88wZ_Pv0"
    ]
}
</code></pre></td></tr><tr><td><code>processing_completed</code><br>object</td><td><p>The value of this field determines whether or not the aggregated Feature Importance is ready to be viewed for an Analysis Group.</p><p>It also includes an optional list of Analyses which were excluded from processing for various reasons.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">{ 
  "processing_completed": { 
    "feature_importance": true, 
    "excluded_analyses": [ 
      { 
        "analysis_id": "0GTpLZ522Bc", 
        "reason": "analysis_failed" 
      }, 
      { 
        "analysis_id": "6OK88wZ_Pv0", 
        "reason": "analysis_deleted" 
      } 
    ] 
  } 
}
</code></pre><p>Possible values for <code>reason</code>:</p><ul><li><code>analysis_not_ready</code></li><li><code>analysis_feature_importance_incomplete</code></li><li><code>analysis_failed</code></li><li><code>analysis_deleted</code></li><li><code>analysis_not_found</code></li></ul></td></tr><tr><td><code>readiness_status</code><br>string</td><td><p>The value of this field determines whether or not the Analysis Group has finished processing.</p><p>When you create an Analysis Group, modify it or any of the Analyses that are part of it, or refresh it, the <code>readiness_status</code> will be set to <code>pending</code> until processing has completed.</p><p><br>Possible values:</p><ul><li><code>pending</code></li><li><code>failed</code></li><li><code>ready</code></li></ul><p>E.g. <code>ready</code></p></td></tr><tr><td><code>status</code><br>string</td><td><p>Status of the Analysis Group.<br><br>Possible values:</p><ul><li><code>active</code></li><li><code>deleted</code></li></ul><p>E.g. <code>active</code></p></td></tr><tr><td><code>demand_type</code><br>object</td><td><p>Indicates the demand type of the Analyses within the group.<br></p><p><strong>Fields:</strong></p><ul><li><code>interval</code> - <code>day</code> or <code>week</code></li><li><code>week_start_day</code> - e.g. <code>sunday</code>, <code>monday</code> etc. Only displayed for weekly Analysis Groups</li></ul></td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "name": "My Analysis Group 1",
    "create_dt": "2024-02-23T01:37:34.784468+00:00",
    "update_dt": "2024-02-23T01:37:34.784468+00:00",
    "analysis_ids": [
        "0GTpLZ522Bc",
        "6OK88wZ_Pv0"
    ],
    "processing_completed": {
        "feature_importance": true,
        "excluded_analyses": [
            {
                "analysis_id": "0GTpLZ522Bc",
                "reason": "analysis_failed"
            },
            {
                "analysis_id": "6OK88wZ_Pv0",
                "reason": "analysis_failed"
            }
        ]
    },
    "status": "active",
    "readiness_status": "failed",
    "user_id": "MT_KIk17j-w",
    "demand_type": {
        "interval": "day"
    },
    "processed_dt": "2024-02-23T01:37:37.181042+00:00"
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
