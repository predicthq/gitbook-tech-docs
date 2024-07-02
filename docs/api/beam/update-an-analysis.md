---
description: Update (replace) an existing Analysis.
---

# Update an Analysis

## Request

### HTTP Request

<pre class="language-http"><code class="lang-http">PUT https://api.predicthq.com/v1/beam/analyses/<a data-footnote-ref href="#user-content-fn-1">$analysis_id</a>
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>analysis_id</code></td><td>An existing Beam Analysis ID.</td></tr></tbody></table>

### Request Headers

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>application/json</code></td></tr></tbody></table>

### Request Body

{% hint style="info" %}
This endpoint accepts the same request body fields as the Create an Analysis endpoint. Please refer to the [Create an Analysis](create-an-analysis.md#request-body) documentation for request body parameters.

Remember this is a PUT endpoint which means you must provide all supported fields or you may lose data - you are effectively replacing the existing record with a new record containing all the fields you provide. We recommend first getting the existing record and pre-populating the request body with the current values, then change the fields you need to change.

If you wish to update a smaller number of fields please use the [PATCH endpoint](partially-update-an-analysis.md).
{% endhint %}

## Response

If successful, the HTTP response code will be `204 No Content`.

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X PUT https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     --data @<(cat <<EOF
    {
        "name": "Analysis 2",
        "location": {
        "geopoint": {
            "lat": "-36.849761",
            "lon": "174.7628903"
            },
            "radius": 1.2,
            "unit": "km"
        },
        "rank": {
            "type": "phq"
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
    url="https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    },
    json={
        "name": "Analysis 2",
        "location": {
            "geopoint": {
                "lat": "-36.849761",
                "lon": "174.7628903"
            },
            "radius": 1.2,
            "unit": "km"
        },
        "rank": {
            "type": "phq"
        }
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [beam-guides](../../getting-started/guides/beam-guides/ "mention")

[^1]: An existing Beam Analysis ID.
