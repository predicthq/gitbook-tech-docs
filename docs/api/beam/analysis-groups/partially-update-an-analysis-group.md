---
description: Partially update an existing Analysis Group.
---

# Partially Update an Analysis Group

## Request

### HTTP Request

```http
PATCH https://api.predicthq.com/v1/beam/analysis-groups/$group_id
```

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>group_id</code></td><td>An existing Beam Analysis Group ID.</td></tr></tbody></table>

### Request Headers

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>application/json</code></td></tr></tbody></table>

### Request Body

{% hint style="info" %}
This endpoint accepts the same request body fields as the Create an Analysis endpoint. Please refer to the [Create an Analysis Group](create-an-analysis-group.md#request-body) documentation for request body parameters.

Remember this is a PATCH endpoint which means only the fields you provide will be updated.

If you wish to replace all fields please use the [PUT endpoint](update-an-analysis-group.md).
{% endhint %}

## Response

If successful, the HTTP response code will be `202 Accepted`.

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X PATCH https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     --data @<(cat <<EOF
    {
        "name": "Analysis Group 2",
    }
    EOF
    )  
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.patch(
    url="https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    },
    json={
        "name": "Analysis Group 2"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}
