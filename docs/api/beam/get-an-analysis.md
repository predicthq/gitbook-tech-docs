---
description: Get an existing Analysis.
---

# Get an Analysis

## Request

### HTTP Request

<pre class="language-apacheconf"><code class="lang-apacheconf">GET https://api.predicthq.com/v1/beam/analyses/<a data-footnote-ref href="#user-content-fn-1">$analysis_id</a>
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>analysis_id</code></td><td>An existing Beam Analysis ID.</td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="219">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>name</code><br>string</td><td>Name of the Analysis.<br><br>E.g. <code>My Location Analysis 1</code></td></tr><tr><td><code>create_dt</code><br>string</td><td><p>The creation date time for the Analysis in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a> format.</p><p><br>E.g. <code>2022-04-26T11:46:24+00:00</code></p></td></tr><tr><td><code>update_dt</code><br>string</td><td><p>The last update date time for the Analysis in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a> format.</p><p><br>E.g. <code>2022-04-26T11:46:24+00:00</code></p></td></tr><tr><td><code>processed_dt</code><br>string</td><td><p>The date time the Analysis was last processed in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a> format.</p><p><br>E.g. <code>2022-04-26T11:46:25+00:00</code></p></td></tr><tr><td><code>user_id</code><br>string</td><td><p>The ID of the user who created the Analysis. This is present for Analyses created in Control Center. For Analyses created via the API this field will not be populated.</p><p><br>E.g. <code>hjqkKozgS8mm</code></p></td></tr><tr><td><code>access_type</code><br>string</td><td><p>Indicates whether or not your subscription has access to the provided location.</p><p></p><p>We allow creating Analyses for any location, even locations outside of your subscription. However, for locations outside of your subscription the <code>access_type</code> will be set as <code>limited</code> and certain functionality might not be available.</p><p></p><p>Possible values:</p><ul><li><code>full</code></li><li><code>limited</code></li></ul><p>E.g. <code>full</code></p></td></tr><tr><td><code>location</code><br>object</td><td><p>Location of the Analysis.<br><br>E.g.</p><pre class="language-json"><code class="lang-json">{
  "location": {
    "geopoint": {
      "lat": "-36.849761",
      "lon": "174.7628903"
    },
    "radius": 1.2,
    "unit": "km"
  }
}
</code></pre></td></tr><tr><td><code>rank</code><br>object</td><td><p>Specifies which rank type was set to use when calculating event impacts and anomaly detection.<br><br>E.g.</p><pre class="language-json"><code class="lang-json">{
  "rank": {
    "type": "phq",
    "levels": {
      "phq": {
        "min": 51
      }
    }
  }
}
</code></pre></td></tr><tr><td><code>tz</code><br>string</td><td><p>The time zone of the Analysis in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format. </p><p></p><p>E.g. <code>Pacific/Auckland</code></p><p></p><p><em>Note: this field is being used in the Control Center Beam UI for the purpose of fetching a list of relevant events in the correct time zone. It no longer has bearing on the outcome of a Beam analysis.</em></p></td></tr><tr><td><code>readiness_checks</code><br>object</td><td><p>Beam performs a number of validation checks on the data provided. The results of some of those checks are stored in this field.</p><p></p><p>We don't recommend relying on the values in this field as the structure may change without warning. Instead, refer to the <code>readiness_status</code> field to determine whether or not the Analysis is ready.<br><br>E.g.</p><pre class="language-json"><code class="lang-json">{
  "readiness_checks": {
    "date_range": {
      "start": "2017-01-01",
      "end": "2017-12-31"
    },
    "validation_response": {
      "missing_data_percentage": 0.0,
      "consecutive_nan": 0
    }
  }
}
</code></pre></td></tr><tr><td><code>readiness_status</code><br>string</td><td><p>The value of this field determines whether or not the Analysis is ready for correlation.</p><p></p><p>When you upload data for an Analysis the <code>readiness_status</code> will be set to <code>pending</code> until processing has completed.<br><br>Possible values:</p><ul><li><code>pending</code></li><li><code>failed</code></li><li><code>ready</code></li></ul><p>E.g. <code>ready</code></p></td></tr><tr><td><code>status</code><br>string</td><td><p>Status of the Analysis.<br><br>Possible values:</p><ul><li><code>draft</code></li><li><code>active</code></li></ul><p>E.g. <code>active</code></p></td></tr><tr><td><code>processing_completed</code><br>object</td><td><p>Status of the analysis processing stages. Only present in newly created or refreshed analyses.<br></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "processing_completed": {
    "correlation": true,
    "feature_importance": false
  }
}
</code></pre></td></tr></tbody></table>



<details>

<summary>Example response</summary>

Below is an example response:

```json
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
        "type": "phq",
        "levels": {
            "phq": {
                "min": 51
            }
        }
    },
    "status": "draft",
    "create_dt": "2023-03-01T23:03:19.403859+00:00",
    "update_dt": "2023-03-01T23:49:39.464011+00:00",
    "user_id": null,
    "access_type": "full",
    "processed_dt": "2023-03-01T23:43:52.253150+00:00",
    "readiness_status": "ready",
    "readiness_checks": {
        "date_range": {
            "start": "2017-01-01",
            "end": "2017-12-31"
        },
        "validation_response": {
            "missing_data_percentage": 0.0,
            "consecutive_nan": 0
        }
    },
    "processing_completed": {
        "correlation": true,
        "feature_importance": true
    },
    "tz": "UTC"
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/beam/analyses/<analysis_id>",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [beam-guides](../../getting-started/guides/beam-guides/ "mention")

[^1]: An existing Beam Analysis ID.
