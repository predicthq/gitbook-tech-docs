---
description: >-
  Loop settings are used to control how certain elements might be displayed
  inside the Loop UI.
---

# Get Loop Settings

Particularly for the Loop Links UI we take the `org_name` from Settings and display it at the top of the page.

## Request

### HTTP Request

```
GET https://api.predicthq.com/v1/loop/settings
```

## Response

### Response Fields

<table><thead><tr><th width="162">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>org_name</code><br>string</td><td>Name to display at the top of the Loop UI for end-users.<br><br>This defaults to your Org name as per your PredictHQ account, however you can customize it here to make it different.<br><br>E.g. <code>My Org Name</code></td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
  "org_name": "My Org"
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/loop/settings \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/loop/settings",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [Integrate with Loop Links](../../../getting-started/guides/loop-guides/integrate-with-loop-links.md)
