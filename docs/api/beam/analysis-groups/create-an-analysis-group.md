---
description: >-
  Creating an Analysis Group allows to aggregate Feature Importance for a number
  of Analyses
---

# Create an Analysis Group

## Request

### HTTP Request

```http
POST https://api.predicthq.com/v1/beam/analysis-groups
```

### Request Headers

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>application/json</code></td></tr></tbody></table>

### Request Body

<table><thead><tr><th width="217">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>name</code><br>string<br><em>required</em></td><td>Name of an analysis group.<br><br>E.g. <code>My Analysis Group 1</code></td></tr><tr><td><code>analysis_ids</code><br>string[]<br><em>required</em></td><td><p>The list of existing analysis ids to include in the group.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">"analysis_ids": [
    "zRa_kk7MlAA",
    "3aR-gbJp98I",
    "JBb08XsZqAo",
    "q9iX2XqFBxM"
]
</code></pre><p>Analyses can belong to multiple groups.<br>Analyses must have the same demand type, i.e. the <code>interval</code> must match, and in case of weekly analyses <code>week_start_day</code> must also be consistent across all analyses in the group. Every analysis in the group must have the same industry, if set.</p></td></tr></tbody></table>

## Response

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "group_id": "wyy0nguQHPs"
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X POST "https://api.predicthq.com/v1/beam/analysis-groups" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
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
        "Authorization": "Bearer $ACCESS_TOKEN",
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

Please refer to this guide for the best practices on grouping analyses: [Grouping Analyses in Beam](../../../webapp-support/beam-relevancy-engine/grouping-analyses-in-beam)
