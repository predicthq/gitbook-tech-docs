---
description: Update your Loop Settings.
---

# Update Loop Settings

## Request

### HTTP Request

```
PUT https://api.predicthq.com/v1/loop/settings
```

### Request Headers

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>application/json</code></td></tr></tbody></table>

### Request Body

<table><thead><tr><th width="162">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>org_name</code><br>string</td><td>Name to display at the top of the Loop UI for end-users.<br><br>This defaults to your Org name as per your PredictHQ account, however you can customize it here to make it different.<br><br>E.g. <code>My Org Name</code></td></tr></tbody></table>

## Response

If successful, the HTTP response code will be `204 No Content`.

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X PUT https://api.predicthq.com/v1/loop/settings \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     --data @<(cat <<EOF
    {
        "org_name": "My Org Name"
    }
    EOF
    )
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.put(
    url="https://api.predicthq.com/v1/loop/settings",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    },
    json={
        "org_name": "My Org Name"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}
