---
description: Rerun the Beam correlation and analysis process.
---

# Refresh an Analysis

## Request

### HTTP Request

<pre class="language-http"><code class="lang-http">POST https://api.predicthq.com/v1/beam/analyses/<a data-footnote-ref href="#user-content-fn-1">$analysis_id</a>/refresh
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>analysis_id</code></td><td>An existing Beam Analysis ID.</td></tr></tbody></table>

## Response

If successful, the HTTP response code will be `202 Accepted`.

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X POST "https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/refresh" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.post(
    url="https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/refresh",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [beam-guides](../../../getting-started/guides/beam-guides/ "mention")

[^1]: An existing Beam Analysis ID.
