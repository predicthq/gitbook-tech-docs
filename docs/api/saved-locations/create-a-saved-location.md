---
description: Create a new Saved Location to begin seeing insights.
---

# Create a Saved Location

## Request

### HTTP Request

```http
POST https://api.predicthq.com/v1/saved-locations
```

### Request Headers

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>application/json</code></td></tr></tbody></table>

### Request Body

<table><thead><tr><th width="181">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>name</code><br>string<br><em>required</em></td><td>Name of the Saved Location.<br><br>E.g. <code>My Location</code></td></tr><tr><td><code>description</code><br>string</td><td>Description of the location.</td></tr><tr><td><code>location_code</code><br>string</td><td>An optional identifier for your location.<br><br>The intention here is to use your own identifier for the location if you have one. E.g., you might have stores/hotels/etc in your system with their own ID - use that ID here to make it easier to lookup the location later.</td></tr><tr><td><code>labels</code><br>array</td><td><p>A list of labels to help you categorize your locations. You can use these labels to search upon.<br><br>E.g. </p><pre class="language-json"><code class="lang-json">{
  "labels": ["label1", "label2"]
}
</code></pre></td></tr><tr><td><code>geojson</code><br>object</td><td><p>You can define the geolocation of the Saved Location either by GeoJSON or Place IDs.</p><p></p><p>When using GeoJSON please note the following:</p><ul><li>Currently we support <code>Point</code> type locations only.</li><li>Remember that GeoJSON coordinates are ordered longitude then latitude.</li><li>We require a radius to be defined using a special set of properties on the GeoJSON record. As in the example below, these are <code>radius</code> and <code>radius_unit</code>.</li><li>The <code>radius</code> property should be a numeric value.</li><li>The <code>radius_unit</code> property can be one of <code>m</code> (meters), <code>km</code> (kilometers), <code>ft</code> (feet), <code>mi</code> (miles).</li></ul><p>As always, we strongly recommend using our <a href="../suggested-radius/">Suggested Radius API</a> to work out a suitable radius value for your location.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
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
}
</code></pre></td></tr><tr><td><code>place_ids</code><br>array</td><td><p>You can define the geolocation of the Saved Location either by GeoJSON or Place IDs.</p><p></p><p>The Place IDs option is typically used when the location covers an entire city, county, state or country.</p><p></p><p>Use our <a href="../places/">Places API</a> to search for the correct Place ID.<br></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "place_ids": [2750405]
}
</code></pre></td></tr></tbody></table>

## Response

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
  "location_id": "K9XvW4KE32ZjcdqQ3WiPvg"
}
```

</details>

## Examples

### Create Using Point and Radius

{% tabs %}
{% tab title="curl" %}
```bash
curl --location 'https://api.predicthq.com/v1/saved-locations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer TOKEN' \
--data '{
    "name": "Example of creating a saved location",
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

url = "https://api.predicthq.com/v1/saved-locations"

payload = json.dumps({
  "name": "Example of creating a saved location",
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

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```
{% endtab %}
{% endtabs %}

### Create Using Place ID

{% tabs %}
{% tab title="curl" %}
```bash
curl --location 'https://api.predicthq.com/v1/saved-locations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer TOKEN' \
--data '{
    "name": "Test with place_id",
    "place_ids": [ 2750405 ]
}'
```
{% endtab %}

{% tab title="python" %}
```python
import requests
import json

url = "https://api.predicthq.com/v1/saved-locations"

payload = json.dumps({
  "name": "Example with place_id",
  "place_ids": [
    2750405
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer TOKEN'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [Working with Location-Based Subscriptions](../../getting-started/guides/geolocation-guides/searching-by-location/working-with-location-based-subscriptions.md)
