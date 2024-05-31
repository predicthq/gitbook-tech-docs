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

<table><thead><tr><th width="217">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>name</code><br>string<br><em>required</em></td><td>Name of an analysis.<br><br>E.g. <code>My Location Analysis 1</code></td></tr><tr><td><code>location.*</code><br>object<br><em>required</em></td><td><pre class="language-json"><code class="lang-json">  "geopoint": {
    "lat": "-36.849761",
    "lon": "174.7628903"
  },
  "radius": 1.2,
  "unit": "km"
}
</code></pre></td></tr><tr><td><code>rank.*</code><br>object<br><em>required</em></td><td><p>Specifies which rank type to use when calculating event impacts and anomaly detection. If you're unsure which to use we recommend using <code>phq</code>.</p><pre class="language-json"><code class="lang-json">{
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
