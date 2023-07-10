---
description: Search for a Place.
---

# Search Places

The Places API gives you a read-only interface to PredictHQ's places data. A place represents a [Geonames](http://www.geonames.org/) Feature, which can be either an Area, an Administrative Feature, or a Populated Place.

Places can be used to search and filter events using named geographic features rather than a radius, latitude and longitude (see events' `place.scope` and `place.exact` parameters). This is helpful when searching for all events that apply to a continent, country, state, region, province, county or city.

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/places/
```

### Query Parameters

Use the below parameters to search and filter all places. Places are sorted by relevance (location or text query proximity).

A search requires at least one of the `q`, `id`, `country` or `location` parameters.

<table><thead><tr><th width="212">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>country</code><br>string</td><td>A comma-separated list of <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> country codes.<br><br>E.g. <code>?country=US</code></td></tr><tr><td><code>id</code><br>string</td><td>A comma-separated list of place identifiers.<br><br>E.g. <code>?id=5115985</code></td></tr><tr><td><code>limit</code><br>number</td><td>The maximum number of results to return. The default limit is <code>10</code>.<br><br>E.g. <code>?limit=10</code></td></tr><tr><td><code>location</code><br>coordinate</td><td>A coordinate in the form <code>@{latitude},{longitude}</code>.<br><br>E.g. <code>?location=@40.66677,-73.88236</code></td></tr><tr><td><code>q</code><br>string</td><td>A full-text search query.<br><br>E.g. <code>?q=New+York</code></td></tr><tr><td><code>type</code><br>string</td><td><p>A comma-separated list of place types.<br><br><strong>Possible values:</strong></p><ul><li><code>neighbourhood</code></li><li><code>locality</code></li><li><code>localadmin</code></li><li><code>county</code></li><li><code>region</code></li><li><code>country</code></li><li><code>continent</code></li><li><code>planet</code></li></ul><p>Supports extra types:</p><ul><li><code>local</code>: synonym for <code>neighbourhood,locality,localadmin</code></li><li><code>metro</code>: metropolitan areas</li><li><code>major</code>: major cities</li></ul><p>E.g. <code>?type=country</code></p></td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="232">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>country</code><br>string</td><td>The name of the place's administrative level 0 place, or <code>null</code> if it does not apply.<br><br>E.g. <code>United States</code></td></tr><tr><td><code>country_alpha2</code><br>string</td><td>The ISO 3166-1 alpha-2 country code, or <code>null</code> if there is no country.<br><br>E.g. <code>US</code></td></tr><tr><td><code>country_alpha3</code><br>string</td><td>The ISO 3166-1 alpha-3 country code, or <code>null</code> if there is no country.<br><br>E.g. <code>USA</code></td></tr><tr><td><code>county</code><br>string</td><td>The name of the place's administrative level 2 place, or <code>null</code> if it does not apply.<br><br>E.g. <code>Kings County</code></td></tr><tr><td><code>id</code><br>string</td><td>The unique identifier of the place.<br><br>E.g. <code>5115985</code></td></tr><tr><td><code>location</code><br>array</td><td>A 2-tuple representing the centroid of the place. Note that the longitude/latitude coordinates use the <a href="http://geojson.org/">GeoJSON order</a> [lon, lat].<br><br>E.g. <code>[-73.88236, 40.66677]</code></td></tr><tr><td><code>name</code><br>string</td><td>The name of the place.<br><br>E.g. <code>East New York</code></td></tr><tr><td><code>region</code><br>string</td><td>The name of the place's administrative level 1 place, or <code>null</code> if it does not apply.<br><br>E.g. <code>New York</code></td></tr><tr><td><code>type</code><br>string</td><td><p>The administrative level of the place.<br><br><strong>Possible values:</strong></p><ul><li><code>neighbourhood</code>: subdivision of a populated place</li><li><code>locality</code>: populated place</li><li><code>localadmin</code>: administrative level 3</li><li><code>county</code>: administrative level 2</li><li><code>region</code>: administrative level 1</li><li><code>country</code>: administrative level 0</li><li><code>continent</code>: Africa, North America, South America, Antarctica, Asia, Europe, Oceania</li><li><code>planet</code>: Earth is the only supported planet at the moment, but we will work hard to support more planets as relevant events become available!</li></ul><p>E.g. <code>locality</code></p></td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
  "count": 4,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "5128638",
      "type": "region",
      "name": "New York",
      "county": null,
      "region": "New York",
      "country": "United States",
      "country_alpha2": "US",
      "country_alpha3": "USA",
      "location": [
        -75.4999,
        43.00035
      ]
    },
    {
      "id": "5128594",
      "type": "county",
      "name": "New York County",
      "county": "New York County",
      "region": "New York",
      "country": "United States",
      "country_alpha2": "US",
      "country_alpha3": "USA",
      "location": [
        -73.96981,
        40.77427
      ]
    },
    {
      "id": "5115985",
      "type": "neighbourhood",
      "name": "East New York",
      "county": "Kings County",
      "region": "New York",
      "country": "United States",
      "country_alpha2": "US",
      "country_alpha3": "USA",
      "location": [
        -73.88236,
        40.66677
      ]
    },
    {
      "id": "5106292",
      "type": "locality",
      "name": "West New York",
      "county": "Hudson County",
      "region": "New Jersey",
      "country": "United States",
      "country_alpha2": "US",
      "country_alpha3": "USA",
      "location": [
        -74.01431,
        40.78788
      ]
    }
  ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/places/?q=New+York&limit=5 \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/places/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "q": "New York",
        "limit": 5
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
