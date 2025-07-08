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

<table><thead><tr><th width="217">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>name</code><br>string<br><em>required</em></td><td>Name of an analysis.<br><br>E.g. <code>My Location Analysis 1</code></td></tr><tr><td><code>location.*</code><br>object<br><em>required</em></td><td><p>Supports one of the following location options:</p><ul><li><code>saved_location_id</code> to use a previously created Saved Location for your analysis as documented at <a href="https://app.gitbook.com/o/WGid6DiA3ccvlkmvc17s/s/kEFs8urDbSJqBmXUI3Lv/~/changes/14/saved-locations/create-a-saved-location">Saved Locations API</a></li></ul><ul><li><p><code>geopoint</code> with <code>radius</code> and <code>unit</code></p><ul><li><code>geopoint</code> contains <code>lat</code> and <code>lon</code> which are coordinates for your analysis, e.g. if you are creating an analysis for a store in Seattle you'd specify the latitude and longitude of your store.</li><li><code>radius</code> must be an integer or a float number up to 2 decimal places. It represents the radius of the event search around your <code>geopoint</code> to use for time series modelling and correlation. We <strong>strongly recommend</strong> using the <a href="../../suggested-radius/get-suggested-radius.md">Suggested Radius API</a> to find a suitable radius for your location/industry.</li><li><p><code>unit</code> is the unit for <code>radius</code> and must be one of:</p><ul><li><code>m</code> - meters</li><li><code>km</code> - kilometers</li><li><code>ft</code> - feet</li><li><code>mi</code> - miles</li></ul></li></ul></li></ul><p>Example for the <code>saved_location_id</code> location type:</p><pre class="language-json"><code class="lang-json">{"saved_location_id": "8gZ2rn8BRcTjM_3SWdjP"}
</code></pre><p>Example for the <code>geopoint</code> location type:</p><pre class="language-json"><code class="lang-json"><strong>{
</strong>  "geopoint": {
    "lat": "-36.849761",
    "lon": "174.7628903"
  },
  "radius": 1.22,
  "unit": "km"
}
</code></pre></td></tr><tr><td><p><code>demand_type.*</code><br>object</p><p><em>optional</em></p></td><td><p>Provides information about the demand type of the analysis.</p><ul><li><p><code>industry</code> is the industry of the demand data being analysed by Beam. Choosing the right industry is important as this will determine the type of features used in the Analysis and will impact the accuracy of the results. The default value is "other". Must be one of the following:</p><ul><li><code>accommodation</code></li><li><code>cpg</code></li><li><code>tourism</code></li><li><code>marketing</code></li><li><code>parking</code></li><li><code>restaurants</code></li><li><code>retail</code></li><li><code>transportation</code></li><li><code>other</code></li></ul></li><li><p><code>currency_code</code> is the ISO 4217 standard code representing the currency corresponding to the units of demand. The default value is "USD". Must be one of the following:</p><ul><li><code>USD</code></li><li><code>EUR</code></li><li><code>GBP</code></li><li><code>AUD</code></li><li><code>CAD</code></li></ul></li><li><code>unit_currency_multiplier</code> is a multiplier used to adjust the unit of demand to its equivalent value in the specified currency. Default value of 1.</li><li><code>unit_descriptor</code> is a description of the unit of demand, which specifies the type or measure being quantified (e.g., "Occupancy Rate", "Sales", "Number of Transactions"). The default value is "Sales".</li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "demand_type": {
    "industry": "restaurants",
    "currency_code": "USD",
    "unit_currency_multiplier": 1,
    "unit_descriptor": "Sales"
  }
}
</code></pre></td></tr><tr><td><code>external_id</code><br>string<br><em>optional</em></td><td><p>External identifier for the location. If you have an ID for the location/store/property in your other platforms, use the same ID here to easily link this specific Beam Analysis to the location.<br><br>E.g.</p><pre class="language-json"><code class="lang-json">{
  "external_id": "abc123"
}
</code></pre></td></tr><tr><td><code>label</code><br>string<br><em>optional</em></td><td><p>Comma-separated list of labels that can be used to search and filter Beam analyses.<br><br>E.g.</p><pre class="language-json"><code class="lang-json">{
  "label": ["label1", "label2", "label3"]
}
</code></pre></td></tr><tr><td><code>rank.*</code><br>object<br><em>required</em></td><td><p>Specifies which rank type to use when calculating event impacts and anomaly detection. Currently, only PHQ rank is supported (also known as "Rank") so this value should be set to <code>"phq"</code> as shown below.</p><pre class="language-json"><code class="lang-json">{
  "type": "phq"
}
</code></pre><p><strong>Possible rank type values:</strong><br><code>phq</code> - PHQ Rank<br><br>Optionally, specify the minimum rank level to use when calculating event impacts. Note: <strong>We strongly recommend</strong> not setting the rank levels and instead letting Beam define the best rank levels based on your industry.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "type": "phq",
  "levels": {
    "phq": {
      "min": 51
    }
  }
}
</code></pre></td></tr></tbody></table>

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
curl -X POST "https://api.predicthq.com/v1/beam/analyses" \
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

* [Beam Guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/beam-guides)
