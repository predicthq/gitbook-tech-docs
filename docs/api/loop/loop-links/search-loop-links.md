---
description: Search existing Loop Links.
---

# Search Loop Links

## Request

### HTTP Request

```
GET https://api.predicthq.com/v1/loop/links
```

### Query Parameters

<table><thead><tr><th width="246">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>q</code><br>string</td><td>Full-text search.<br><br>E.g. <code>?q=hotel+a</code></td></tr><tr><td><code>link_id</code><br>string</td><td>Comma-separated list of <code>link_id</code>.<br><br>E.g. <code>?link_id=m4Dk4g4DRA8Yqbp2PC54</code></td></tr><tr><td><code>user_id</code><br>string</td><td>Comma-separated list of <code>user_id</code>.<br><br>E.g. <code>?user_id=hw8Dsmv4Djg</code></td></tr><tr><td><code>sort</code><br>string</td><td><p>Comma-separated list of sort options.<br><br>Prefix the field name with <code>-</code> for reverse order.<br><br><strong>Possible values:</strong></p><ul><li><code>created</code></li><li><code>updated</code></li><li><code>expires</code></li><li><code>name</code></li></ul><p><br>E.g. <code>?sort=name</code></p></td></tr><tr><td><code>limit</code><br>number</td><td>The maximum number of results to return. The default limit is <code>10</code>.<br><br>E.g. <code>?limit=10</code></td></tr><tr><td><code>offset</code><br>number</td><td>The number of results to skip. The default is <code>0</code>.<br><br>E.g. <code>?offset=20</code></td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="190">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>count</code><br>number</td><td>Total number of results found.</td></tr><tr><td><code>next</code><br>string or null</td><td>URL to the next page of results.</td></tr><tr><td><code>previous</code><br>string or null</td><td>URL to the previous page of results.</td></tr><tr><td><code>links</code><br>array</td><td><p>List of results where each item is a Loop Link.</p><p><br>Please refer to the response fields section in <a href="get-a-loop-link.md#response-fields">Get a Loop Link</a> for the structure of each record.</p></td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "links": [
    {
      "link_id": "kt9fJZXpWFXSAdky9Bunb2",
      "expire_dt": "2025-03-12T21:07:26.704000+00:00",
      "name": "Hotel A",
      "status": "active",
      "create_dt": "2023-03-12T21:12:51+00:00",
      "update_dt": "2023-03-12T21:12:51+00:00",
      "metadata": {
        "hotel_id": 123456789
      },
      "links": {
        "event": "https://loop.phq.link/event/kt9fJZXpWFXSAdky9Bunb2",
        "event_feedback": "https://loop.phq.link/event-feedback/kt9fJZXpWFXSAdky9Bunb2"
      }
    }
  ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/loop/links?sort=name \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/loop/links",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "sort": "name"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
