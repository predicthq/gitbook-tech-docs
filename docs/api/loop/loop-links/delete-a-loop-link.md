---
description: Delete an existing Loop Link.
---

# Delete a Loop Link

## Request

### HTTP Request

<pre class="language-http"><code class="lang-http">DELETE https://api.predicthq.com/v1/loop/links/<a data-footnote-ref href="#user-content-fn-1">$link_id</a>
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>link_id</code></td><td>An existing Loop Link ID.</td></tr></tbody></table>

## Response

If successful, the HTTP response code will be `204 No Content`.

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X DELETE "https://api.predicthq.com/v1/loop/links/$LINK_ID" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.delete(
    url="https://api.predicthq.com/v1/loop/links/$LINK_ID",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [Integrate with Loop Links](../../../integrations/integration-guides/integrate-with-loop-links.md)

[^1]: An existing Loop Link ID.
