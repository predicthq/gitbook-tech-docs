---
description: The Account API provides read-only access to your account details.
---

# Get Account Details

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/accounts/self/
```

### Query Parameters

There are no query parameters for this endpoint.

## Response

### Response Fields

<table><thead><tr><th width="199">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>created_at</strong><br>string</td><td><p>UTC date and time of the account's creation in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format</p><p><br>E.g. <code>2014-07-16T01:35:26Z</code></p></td></tr><tr><td><strong>description</strong><br>string</td><td><p>A short description of the account.</p><p><br>E.g. <code>PredictHQ is a new global demand intelligence platform.</code></p></td></tr><tr><td><strong>id</strong><br>string</td><td><p>The unique identifier of the account.</p><p><br>E.g. <code>wJqIklAeuFVy</code></p></td></tr><tr><td><strong>industry</strong><br>object</td><td><p>The industry details for the account.</p><p><br>E.g. <code>{"id": "pzLDW2D1GAwJ", "name": "Marketing and Advertising"}</code></p></td></tr><tr><td><strong>name</strong><br>string</td><td><p>The full name of the account.</p><p><br>E.g. <code>PredictHQ Ltd</code></p></td></tr><tr><td><strong>updated_at</strong><br>string</td><td><p>UTC date and time of the last update to the account in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.</p><p><br>E.g. <code>2015-01-08T03:14:32Z</code></p></td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
  "id": "wJqIklAeuFVy",
  "name": "PredictHQ Ltd",
  "description": "PredictHQ is a new global events intelligence platform.",
  "industry": {
      "id": "pzLDW2D1GAwJ",
      "name": "Marketing and Advertising"
  },
  "created_at": "2014-07-16T01:35:26Z",
  "updated_at": "2015-01-08T03:14:32Z"
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/accounts/self/ \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/accounts/self/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
