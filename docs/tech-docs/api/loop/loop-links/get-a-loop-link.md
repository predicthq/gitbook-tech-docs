---
description: Get an existing Loop Link.
---

# Get a Loop Link

## Request

### HTTP Request

<pre class="language-http"><code class="lang-http">GET https://api.predicthq.com/v1/loop/links/<a data-footnote-ref href="#user-content-fn-1">$link_id</a>
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>link_id</code></td><td>An existing Loop Link ID.</td></tr></tbody></table>

## Response

### Response Fields

#### Response Fields

<table><thead><tr><th width="222">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>link_id</code><br>string</td><td>Loop Link Identifier.<br><br>E.g. <code>ber7ntO0ZHuFVCfrSNsN</code></td></tr><tr><td><code>create_dt</code><br>string</td><td>Date/time the Loop Link was created in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br><br>All dates are in UTC.<br><br>E.g. <code>2023-05-08T00:29:45.859Z</code></td></tr><tr><td><code>update_dt</code><br>string</td><td>Date/time the Loop Link was last updated in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br><br>All dates are in UTC.<br><br>E.g.<br><code>2023-05-08T00:29:45.859Z</code></td></tr><tr><td><code>expire_dt</code><br>string</td><td>Date/time the Loop Link is set to expire in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br><br>All dates are in UTC.<br><br>E.g.<br><code>2023-05-08T00:29:45.859Z</code></td></tr><tr><td><code>user_id</code><br>string</td><td>The User ID of the user who created the Loop Link (if applicable).<br><br>E.g. <code>DiwBN4A0ZHuF</code></td></tr><tr><td><code>name</code><br>string</td><td>Name of the Loop Link. This is for your own use as a way to differentiate your Loop Links.<br><br>E.g. <code>Hotel ABC</code></td></tr><tr><td><code>links</code><br>object</td><td><p>These are the links your end-users need to open to access the Loop UI for submitting missing events or feedback about existing events.<br><br>The different link types are:</p><ul><li><code>event</code>: This URL will present a page for submitting missing events.</li><li><code>event_feedback</code>: This URL will present a page for providing feedback about an existing event.</li></ul><p>When using the <code>event</code> link you can optionally provide the following query string parameters:</p><ul><li><code>email</code>: Email address of the end-user who is providing the feedback. This will be stored against the submission so the user can receive email notifications about their submission.</li></ul><p>When using the <code>event_feedback</code> link you can optionally provide the following query string parameters:</p><ul><li><code>event_id</code>: Event ID to provide the feedback for (if this is not provided, the user will be asked to enter an Event ID).</li><li><code>email</code>: Email address of the end-user who is providing the feedback. This will be stored against the submission so the user can receive email notifications about their submission.</li></ul></td></tr><tr><td><code>metadata</code><br>object</td><td>Metadata can be used to further identify Loop Links in a way that makes sense for your system.<br><br>The field is a key/value field that accepts string-based keys and string or numeric values.<br><br>This can be useful for storing additional data such as a end-user identifier or store ID etc.</td></tr><tr><td><code>status</code><br>string</td><td>Status of the loop link.<br><br>Possible values:<br><br>- <code>active</code></td></tr></tbody></table>

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
curl -X GET "https://api.predicthq.com/v1/loop/links/$LINK_ID" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/loop/links/$LINK_ID",
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

* [Integrate with Loop Links](../../../integrations/integration-guides/integrate-with-loop-links.md)

[^1]: An existing Loop Link ID.
