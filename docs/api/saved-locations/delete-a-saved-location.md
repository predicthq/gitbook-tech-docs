---
description: Delete an existing Saved Location.
---

# Delete a Saved Location

## Request

### HTTP Request

<pre class="language-http"><code class="lang-http">DELETE https://api.predicthq.com/v1/saved-locations/<a data-footnote-ref href="#user-content-fn-1">$location_id</a>
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>location_id</code></td><td>An existing Saved Location ID.</td></tr></tbody></table>

## Response

If successful, the HTTP response code will be `202 Accepted`.

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X DELETE "https://api.predicthq.com/v1/saved-locations/$LOCATION_ID" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.delete(
    url="https://api.predicthq.com/v1/saved-locations/$LOCATION_ID",
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

* [Working with Location-Based Subscriptions](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/geolocation-guides/searching-by-location/working-with-location-based-subscriptions)

[^1]: An existing Saved Location ID.
