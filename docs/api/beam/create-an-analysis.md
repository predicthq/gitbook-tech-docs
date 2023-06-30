# Create an Analysis

## Request

### HTTP Request

```http
POST https://api.predicthq.com/v1/beam/analyses
```

### Query Parameters

<table><thead><tr><th width="217">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><strong>name</strong><br>string<br><em>required</em></td><td>Name of an analysis.<br><br>E.g. <code>My Location Analysis 1</code></td></tr><tr><td><strong>location.*</strong><br>object<br><em>required</em></td><td><p>This should be the location of your data. We will use this location for our time series modelling and to correlate with events in the specified area.</p><pre class="language-json"><code class="lang-json">{
  "geopoint": {
    "lat": "-36.849761",
    "lon": "174.7628903"
  },
  "radius": 1.2,
  "unit": "km"
}
</code></pre><p>We recommend using the <a href="https://docs.predicthq.com/resources/suggested-radius">Suggested Radius API</a> to find a suitable radius for your location/industry.<br><br><strong>Possible radius units:</strong><br><code>mi</code> - Miles<br><code>m</code> - Meters<br><code>km</code> - Kilometers</p></td></tr><tr><td><strong>rank.*</strong><br>object<br><em>required</em></td><td><p>Specifies which rank type to use when calculating event impacts and anomaly detection. If you're unsure which to use we recommend using <code>phq</code>.</p><pre class="language-json"><code class="lang-json">{
  "type": "phq"
}
</code></pre><p><strong>Possible rank type values:</strong><br><code>phq</code> - PHQ Rank<br><code>aviation</code> - Aviation Rank<br><br>Optionally, specify the minimum rank level to use when calculating event impacts.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "type": "phq",
  "levels": {
    "phq": {
      "min": 51
    }
  }
}
</code></pre></td></tr><tr><td><strong>tz</strong><br>string<br>optional</td><td>Time zone of the location in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format.<br><br>E.g. <code>Pacific/Auckland</code></td></tr></tbody></table>

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
        "rank": {
            "type": "phq"
        },
        "tz": "UTC"
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
        "rank": {
            "type": "phq"
        },
        "tz": "UTC"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
