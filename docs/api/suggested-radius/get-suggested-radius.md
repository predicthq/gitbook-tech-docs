---
description: >-
  Take the guesswork out of working out a suitable radius around your business
  when searching for events.
---

# Get Suggested Radius

The Suggested Radius API returns a radius that can be used to find attended events around a given location. When looking for events around a business location (such as a store, a hotel, or another business location) a key question is how far should you look for events. For example, should you look at events in a 0.5-mile radius, a 2-mile radius, or a 10-mile radius from your location? The Suggested Radius API answers this question by returning a radius based on a number of factors that can be used to retrieve events around a location. This radius returned by the API is commonly used as follows:

* When querying the[ Events API](../events/search-events.md) using the `within` parameter.
* When calling the [Features API](../features/get-features.md) with a latitude, longitude, and radius to get aggregated features back for a location.
* For retrieving events in a data lake by setting the radius around a store or location to the suggested radius.
* In-demand forecasting when building event-based features for a location, use this radius when calculating features for a location.
* For use with our Beam product when performing a correlation analysis

The Suggested Radius API is powered by a machine learning model that looks at factors like population density, the events around a location, the customer’s industry, and many other factors to determine the ideal radius.

We'd suggest caching the Suggested Radius API response where possible. The response will only change infrequently and it would be sufficient to refresh the cache once per month.

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/suggested-radius/
```

### Query Parameters

<table><thead><tr><th width="219">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>location.origin</code><br>geopoint</td><td><p>A comma-separated string consisting of the latitude and longitude of the location to find the optimal radius for. For example your store or hotel location.</p><p></p><p>The format is <code>&#x3C;latitude>,&#x3C;longitude></code></p><p><br>E.g. <code>?location.origin=37.747767,-122.455320</code></p></td></tr><tr><td><code>radius_unit</code><br>string</td><td><p>Unit in which the suggested radius will be returned.<br>The default unit is <code>m</code><br></p><p><strong>Possible values:</strong></p><ul><li><code>m</code> - meters (default)</li><li><code>km</code> - kilometers</li><li><code>ft</code> - feet</li><li><code>mi</code> - miles</li></ul><p>E.g. <code>?radius_unit=km</code></p></td></tr><tr><td><code>industry</code><br>string</td><td><p>The industry of interest that the radius will be calculated for. For different industries, the radii will be different based on the different types of events that would impact the location. For example, if you were getting the suggested radius around a hotel you’d specify accommodation as the industry.</p><p><br>The default industry is <code>other</code><br></p><p><strong>Possible values:</strong></p><ul><li><code>parking</code></li><li><code>restaurants</code></li><li><code>retail</code></li><li><code>accommodation</code></li><li><code>other</code>(default)</li></ul><p>E.g. <code>?industry=accommodation</code></p></td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="196">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>radius</code><br>float</td><td>The suggested radius for a given location rounded to 2 decimal places.</td></tr><tr><td><code>radius_unit</code><br>string</td><td>The unit of the radius returned. This will be the unit specified in the industry parameter in the call made.</td></tr><tr><td><code>location</code><br>object</td><td><p>A json object representing the geo location of the event.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "lat": 37.747767,
  "lon": -122.455320
}
</code></pre></td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "radius": 1.46,
    "radius_unit": "km",
    "location": {
        "lat": "37.747767",
        "lon": "-122.45532"
    }
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/suggested-radius/?location.origin=37.747767,-122.455320&industry=parking&radius_unit=km \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/suggested-radius/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "location.origin": "37.747767,-122.455320",
        "industry": "parking",
        "radius_unit": "km"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [Find Events by Latitude/Longitude and Radius](../../getting-started/guides/geolocation-guides/searching-by-location/find-events-by-latitude-longitude-and-radius.md)
