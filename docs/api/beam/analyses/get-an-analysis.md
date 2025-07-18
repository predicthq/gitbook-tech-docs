---
description: Get an existing Analysis.
---

# Get an Analysis

## Request

### HTTP Request

<pre class="language-http"><code class="lang-http">GET https://api.predicthq.com/v1/beam/analyses/<a data-footnote-ref href="#user-content-fn-1">$analysis_id</a>
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>analysis_id</code></td><td>An existing Beam Analysis ID.</td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="219">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>name</code><br>string</td><td>Name of the Analysis.<br><br>E.g. <code>My Location Analysis 1</code></td></tr><tr><td><code>create_dt</code><br>string</td><td><p>The creation date time for the Analysis in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a> format.</p><p><br>E.g. <code>2022-04-26T11:46:24+00:00</code></p></td></tr><tr><td><code>update_dt</code><br>string</td><td><p>The last update date time for the Analysis in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a> format.</p><p><br>E.g. <code>2022-04-26T11:46:24+00:00</code></p></td></tr><tr><td><code>processed_dt</code><br>string</td><td><p>The date time the Analysis was last processed in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a> format.</p><p><br>E.g. <code>2022-04-26T11:46:25+00:00</code></p></td></tr><tr><td><code>user_id</code><br>string</td><td><p>The ID of the user who created the Analysis. This is present for Analyses created in the WebApp. For Analyses created via the API this field will not be present.</p><p><br>E.g. <code>hjqkKozgS8mm</code></p></td></tr><tr><td><code>external_id</code><br>string</td><td>External ID. Used to identify this Beam Analysis using an ID from another system.</td></tr><tr><td><code>label</code><br>array</td><td>Labels to categorize the Analysis.</td></tr><tr><td><code>access_type</code><br>string</td><td><p>Indicates whether or not your subscription has access to the provided location.</p><p>We allow creating Analyses for any location, even locations outside of your subscription. However, for locations outside of your subscription the <code>access_type</code> will be set as <code>limited</code> and certain functionality might not be available.</p><p>Possible values:</p><ul><li><code>full</code></li><li><code>limited</code></li></ul><p>E.g. <code>full</code></p></td></tr><tr><td><code>location</code><br>object</td><td><p>Location of the Analysis.</p><p></p><p>Example for the <code>saved_location_id</code> location type:</p><pre class="language-json"><code class="lang-json">{"saved_location_id": "8gZ2rn8BRcTjM_3SWdjP"}
</code></pre><p>Example for the <code>geopoint</code> location type</p><pre class="language-json"><code class="lang-json">{
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
</code></pre></td></tr><tr><td><code>demand_type</code><br>object</td><td><p>Indicates the detected type of the uploaded demand data as well as other user-defined information about the demand data.<br></p><p><strong>Fields:</strong></p><ul><li><code>interval</code> - <code>day</code> or <code>week</code></li><li><code>week_start_day</code> - e.g. <code>sunday</code>, <code>monday</code> etc. Only displayed for weekly analyses</li><li><code>industry</code> - user selected industry of the demand data.</li></ul></td></tr><tr><td><code>tz</code><br>string</td><td><p>The time zone of the Analysis in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format.</p><p>E.g. <code>Pacific/Auckland</code></p><p><strong>Note</strong>: this field is populated automatically based on the location of the Analysis.</p></td></tr><tr><td><code>readiness_checks</code><br>object</td><td><p>Beam performs a number of validation checks on the data provided. The results of some of those checks are stored in this field.</p><p>We don't recommend relying on the values in this field as the structure may change without warning. Instead, refer to the <code>readiness_status</code> field to determine whether or not the Analysis is ready (i.e. has completed processing successfully).<br><br>E.g.</p><pre class="language-json"><code class="lang-json">{
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
</code></pre></td></tr><tr><td><code>readiness_status</code><br>string</td><td><p>The value of this field determines whether or not the Analysis has successfully completed processing.</p><p>When you upload data for an Analysis the <code>readiness_status</code> will be set to <code>pending</code> until processing has completed.<br><br>Possible values:</p><ul><li><code>pending</code></li><li><code>failed</code></li><li><code>ready</code></li></ul><p>E.g. <code>ready</code></p></td></tr><tr><td><code>processing_completed</code><br>object</td><td><p>Status of the Analysis processing stages. All stages will be present here and are reset to <code>false</code> whenever the Analysis is refreshed (i.e., processing has been initiated) then set to <code>true</code> when that stage of the processing is completed.<br></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "processing_completed": {
    "correlation": true,
    "feature_importance": true
  }
}
</code></pre></td></tr><tr><td><code>status</code><br>string</td><td><p>Status of the Analysis.<br><br>Possible values:</p><ul><li><code>active</code></li></ul><p>E.g. <code>active</code></p></td></tr><tr><td><code>saved_location</code></td><td><p>Saved Location object at the time of processing the Analysis.</p><p></p><p>Contains the following fields as defined in the <a href="https://app.gitbook.com/o/WGid6DiA3ccvlkmvc17s/s/kEFs8urDbSJqBmXUI3Lv/~/changes/14/saved-locations/get-a-saved-location">Saved Locations API</a></p><ul><li><code>location_id</code></li><li><code>name</code></li><li><code>formatted_address</code></li><li><code>geojson</code></li><li><code>place_ids</code></li><li><code>places</code></li></ul></td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "name": "Analysis 1",
    "create_dt": "2023-03-01T23:03:19.403859+00:00",
    "update_dt": "2023-03-01T23:49:39.464011+00:00",
    "processed_dt": "2023-03-01T23:43:52.253150+00:00",
    "user_id": null,
    "external_id": "id1",
    "label": ["label1", "label2", "label3"],
    "location": {
        "geopoint": {
            "lat": "-36.849761",
            "lon": "174.7628903"
        },
        "radius": 1.2,
        "unit": "km"
    },
    "demand_type": {
        "interval": "week",
        "week_start_day": "monday",
        "industry": "restaurants"
    },
    "rank": {
        "type": "phq",
        "levels": {
            "phq": {
                "min": 51
            }
        }
    },
    "tz": "UTC",
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
    "access_type": "full",
    "status": "draft"
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID" \
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

* [Beam Guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/beam-guides)

[^1]: An existing Beam Analysis ID.
