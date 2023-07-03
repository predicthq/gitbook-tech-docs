# Delete an Analysis

## Request

### HTTP Request

<pre class="language-apacheconf"><code class="lang-apacheconf">DELETE https://api.predicthq.com/v1/beam/analyses/<a data-footnote-ref href="#user-content-fn-1">$analysis_id</a>
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td>analysis_id</td><td>An existing Beam Analysis ID.</td></tr></tbody></table>

## Response

If successful, the HTTP response code will be `202 Accepted`.

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X DELETE https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.delete(
    url="https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

[^1]: An existing Beam Analysis ID.
