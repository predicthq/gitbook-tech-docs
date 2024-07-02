---
description: Rerun the Beam Analysis Group aggregation process.
---

# Refresh an Analysis Group

## Request

### HTTP Request

```http
POST https://api.predicthq.com/v1/beam/analysis-groups/$group_id/refresh
```

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>group_id</code></td><td>An existing Beam Analysis Group ID.</td></tr></tbody></table>

## Response

If successful, the HTTP response code will be `202 Accepted`.

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X POST https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID/refresh \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.post(
    url="https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID/refresh",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}
