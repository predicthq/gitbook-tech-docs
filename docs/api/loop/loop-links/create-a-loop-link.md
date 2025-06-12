---
description: Create a new Loop Link to begin submitting events and feedback.
---

# Create a Loop Link

## Request

### HTTP Request

```http
POST https://api.predicthq.com/v1/loop/links
```

### Request Headers

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>application/json</code></td></tr></tbody></table>

### Request Body

<table><thead><tr><th width="237">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>name</code><br>string</td><td>Name of the Loop Link. This is for your own use as a way to differentiate your Loop Links.<br><br>E.g. <code>Hotel ABC</code></td></tr><tr><td><p><code>expire_dt</code><br>datetime</p><p>optional</p></td><td>Date/time the Loop Link is set to expire in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br><br>All dates are in UTC.<br><br>This is an optional field - omit if not needed.<br><br>E.g. <code>2023-05-08T00:29:45.859Z</code></td></tr><tr><td><p><code>metadata</code><br>object</p><p>optional</p></td><td><p>Metadata can be used to further identify Loop Links in a way that makes sense for your system.<br><br>The field is a key/value field that accepts string-based keys and string or numeric values.<br><br>This can be useful for storing additional data such as a end-user identifier or store ID etc.<br><br>This is an optional field - omit if not needed.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "hotel_id": "123456789"
}
</code></pre></td></tr></tbody></table>

## Response

### Response Fields

{% hint style="info" %}
Please refer to the response fields section in [Get a Loop Link](get-a-loop-link.md#response-fields).
{% endhint %}

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
  "link_id": "ber7ntO0ZHuFVCfrSNsN",
  "create_dt": "2021-11-01T11:12:34",
  "update_dt": "2021-11-01T11:12:34",
  "expire_dt": "2021-11-01T11:12:34",
  "name": "Hotel A",
  "links": {
    "event": "https://loop.phq.link/event/ber7ntO0ZHuFVCfrSNsN",
    "event_feedback": "https://loop.phq.link/event-feedback/ber7ntO0ZHuFVCfrSNsN"
  },
  "metadata": {
    "hotel_id": "123456789"
  },
  "status": "active"
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X POST "https://api.predicthq.com/v1/loop/links" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     --data @<(cat <<EOF
    {
        "name": "Hotel A",
        "expire_dt": "2021-11-01T11:12:34",
        "metadata": {
            "hotel_id": "123456789"
        }
    }
    EOF
    )
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.post(
    url="https://api.predicthq.com/v1/loop/links",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    },
    json={
        "name": "Hotel A",
        "expire_dt": "2021-11-01T11:12:34",
        "metadata": {
            "hotel_id": "123456789"
        }
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [Integrate with Loop Links](../../../integrations/integration-guides/integrate-with-loop-links.md)
