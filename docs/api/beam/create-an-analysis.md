---
description: >-
  Creating an Analysis is the first step in understand which types of events
  impact your demand.
---

# Create an Analysis

## Request

### HTTP Request

```http
POST https://api.predicthq.com/v1/beam/analyses
```

### Request Headers

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>application/json</code></td></tr></tbody></table>

### Request Body

<table><thead><tr><th width="217">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>name</code><br>string<br><em>required</em></td><td>Name of an analysis.<br><br>E.g. <code>My Location Analysis 1</code></td></tr><tr><td><code>location.*</code><br>object<br><em>required</em></td><td><p>Contains <code>geopoint</code>, <code>radius</code> and <code>unit</code> to represent the location of your data to create the analysis.</p><ul><li><code>geopoint</code> contains <code>lat</code> and <code>lon</code> which are coordinates for your analysis, e.g. if you are creating an analysis for a store in Seattle you'd specify the latitude and longitude of your store.</li><li><code>radius</code> must be an integer or a float number up to 2 decimal places. It represents the radius of the event search around your <code>geopoint</code> to use for time series modelling and correlation. We <strong>strongly recommend</strong> using the <a href="../suggested-radius/get-suggested-radius.md">Suggested Radius API</a> to find a suitable radius for your location/industry.</li><li><p><code>unit</code> is the unit for <code>radius</code> and must be one of:</p><ul><li><code>m</code> - meters</li><li><code>km</code> - kilometers</li><li><code>ft</code> - feet</li><li><code>mi</code> - miles</li></ul></li></ul><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "geopoint": {
    "lat": "-36.849761",
    "lon": "174.7628903"
  },
  "radius": 1.22,
  "unit": "km"
}
</code></pre></td></tr><tr><td><code>demand_type.*</code><br>object<br><em>optional</em></td><td><p>Provides information about the demand type of the analysis.<br><br>Example:</p><pre class="language-json"><code class="lang-json">{
  "industry": "restaurants",
  "unit": "sales",
  "description": "Daily sales amount in USD"
}
</code></pre><p><code>industry</code> must be one of the following:</p><ul><li><code>accommodation</code></li><li><code>cpg</code></li><li><code>tourism</code></li><li><code>marketing</code></li><li><code>parking</code></li><li><code>restaurants</code></li><li><code>retail</code></li><li><code>transportation</code></li><li><code>other</code></li></ul><p>Choosing the right industry is important as this will determine the type of features used in the analysis.<br><br><code>unit</code> and <code>description</code> are arbitrary strings.</p></td></tr><tr><td><code>rank.*</code><br>object<br><em>required</em></td><td><p>Specifies which rank type to use when calculating event impacts and anomaly detection. Currently, only PHQ rank is supported (also known as "Rank") so this value should be set to <code>"phq"</code> as shown below.</p><pre class="language-json"><code class="lang-json">{
  "type": "phq"
}
</code></pre><p><strong>Possible rank type values:</strong><br><code>phq</code> - PHQ Rank<br><br>Optionally, specify the minimum rank level to use when calculating event impacts.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "type": "phq",
  "levels": {
    "phq": {
      "min": 51
    }
  }
}
</code></pre></td></tr><tr><td><code>tz</code><br>string<br><em>optional</em></td><td><p>Time zone of the location in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format.<br><br>E.g. <code>Pacific/Auckland</code></p><p><br><em>Note: this field is being used in the Control Center Beam UI for the purpose of fetching a list of relevant events in the correct time zone. It no longer has bearing on the outcome of a Beam analysis.</em></p></td></tr></tbody></table>

## Response

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
  "analysis_id": "2iJcUzm3-ZE"
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X POST https://api.predicthq.com/v1/beam/analyses \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     --data @<(cat <<EOF
    {
        "name": "Analysis 1",
        "location": {
            "geopoint": {
                "lat": "-36.849761",
                "lon": "174.7628903"
            },
            "radius": 1.2,
            "unit": "km"
        },
        "demand_type": {
            "industry": "restaurants"
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

response = requests.post(
    url="https://api.predicthq.com/v1/beam/analyses",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json"
    },
    json={
        "name": "Analysis 1",
        "location": {
            "geopoint": {
                "lat": "-36.849761",
                "lon": "174.7628903"
            },
            "radius": 1.2,
            "unit": "km"
        },
        "demand_type": {
            "industry": "restaurants"
        },
        "rank": {
            "type": "phq"
        }
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [beam-guides](../../getting-started/guides/beam-guides/ "mention")
