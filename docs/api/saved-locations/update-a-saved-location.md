---
description: Update (replace) an existing Saved Location.
---

# Update a Saved Location

## Request

### HTTP Request

<pre class="language-apacheconf"><code class="lang-apacheconf">PUT https://api.predicthq.com/v1/saved-locations/<a data-footnote-ref href="#user-content-fn-1">$location_id</a>
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>location_id</code></td><td>An existing Saved Location ID.</td></tr></tbody></table>

### Request Headers

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>application/json</code></td></tr></tbody></table>

### Request Body

{% hint style="info" %}
This endpoint accepts the same request body fields as the Create a Saved Location endpoint. Please refer to the [Create a Saved Location](create-a-saved-location.md#request-body) documentation for request body parameters.

Remember this is a PUT endpoint which means you must provide all supported fields or you may lose data - you are effectively replacing the existing record with a new record containing all the fields you provide. We recommend first getting the existing record and pre-populating the request body with the current values, then change the fields you need to change.
{% endhint %}

## Response

If successful, the HTTP response code will be `204 No Content`.

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl --location --request PUT 'https://api.predicthq.com/v1/saved-locations/5BcRstnNPjXl-fiB_0TQJg' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer TOKEN' \
--data '{
    "name": "S Las Vegas Blvd, Las Vegas (NV), US",
    "labels": [],
    "geojson": {
        "type": "Feature",
        "properties": {
            "radius": 1,
            "radius_unit": "mi"
        },
        "geometry": {
            "type": "Point",
            "coordinates": [
                -115.1728484,
                36.1147065
            ]
        }
    }
}'
```
{% endtab %}

{% tab title="python" %}
```python
import requests
import json

url = "https://api.predicthq.com/v1/saved-locations/5BcRstnNPjXl-fiB_0TQJg"

payload = json.dumps({
  "name": "S Las Vegas Blvd, Las Vegas (NV), US",
  "labels": [],
  "geojson": {
    "type": "Feature",
    "properties": {
      "radius": 1,
      "radius_unit": "mi"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [
        -115.1728484,
        36.1147065
      ]
    }
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer TOKEN'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```
{% endtab %}
{% endtabs %}

[^1]: An existing Saved Location ID.
