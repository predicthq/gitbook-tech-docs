---
description: Delete an existing Analysis Group.
---

# Delete an Analysis Group

## Request

### HTTP Request

```http
DELETE https://api.predicthq.com/v1/beam/analysis-groups/$group_id
```

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>group_id</code></td><td>An existing Beam Analysis Group ID.</td></tr></tbody></table>

## Response

If successful, the HTTP response code will be `202 Accepted`.

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X DELETE "https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.delete(
    url="https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}
