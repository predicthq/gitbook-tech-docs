---
description: Update (replace) an existing Loop Link.
---

# Update a Loop Link

## Request

### HTTP Request

<pre class="language-http"><code class="lang-http">PUT https://api.predicthq.com/v1/loop/links/<a data-footnote-ref href="#user-content-fn-1">$link_id</a>
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>link_id</code></td><td>An existing Loop Link ID.</td></tr></tbody></table>

### Request Headers

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>application/json</code></td></tr></tbody></table>

### Request Body

{% hint style="info" %}
This endpoint accepts the same request body fields as the Create a Loop Link endpoint. Please refer to the [Create a Loop Link](create-a-loop-link.md#request-body) documentation for request body parameters.

Remember this is a PUT endpoint which means you must provide all supported fields or you may lose data - you are effectively replacing the existing record with a new record containing all the fields you provide. We recommend first getting the existing record and pre-populating the request body with the current values, then change the fields you need to change.
{% endhint %}

## Response

If successful, the HTTP response code will be `204 No Content`.

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X PUT "https://api.predicthq.com/v1/loop/links/$LINK_ID" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     --data @<(cat <<EOF
    {
        "name": "Hotel A",
        "expire_dt": "2024-12-31T00:00:00",
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

response = requests.put(
    url="https://api.predicthq.com/v1/loop/links/$LINK_ID",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    },
    json={
        "name": "Hotel A",
        "expire_dt": "2024-12-31T00:00:00",
        "metadata": {
            "hotel_id": "123456789"
        }
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

## Guides

ow are some guides relevant to this API:

* [Integrate with Loop Links](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/integrations/integration-guides/integrate-with-loop-links)

[^1]: An existing Loop Link ID.
