---
description: Get feature importance data for an analysis.
---

# Get Feature Importance Results

This endpoint runs feature importance tests across an existing analysis, and returns a list of categories and their associated p-values. This represents each feature's statistical significance when it comes to effecting observable incremental/decremental changes in demand.

## Request

### HTTP Request

<pre class="language-apacheconf"><code class="lang-apacheconf">GET https://api.predicthq.com/v1/beam/analyses/<a data-footnote-ref href="#user-content-fn-1">$analysis_id</a>/feature-importance
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>analysis_id</code></td><td>An existing Beam Analysis ID.</td></tr></tbody></table>

## Response

A response will contain a single field `feature_importance`, which will have a list of feature groups ordered by their importance.

### Response Fields

<table><thead><tr><th width="219">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>feature_group</code><br>string</td><td>The name of the feature group<br><br>E.g. <code>severe-weather</code>, <code>concerts</code></td></tr><tr><td><code>features</code><br>list of strings</td><td>The names of the features in the feature group. <br><br>E.g. <code>phq_attendance_community</code></td></tr><tr><td><code>p_value</code><br>float</td><td>The p-value associated with this feature group for this analysis. It shows how important the features in the group are in terms of demand.<br><br>The lower the p-value, the more important the feature group is.</td></tr><tr><td><code>important</code><br>bool</td><td>A <code>true</code> of <code>false</code> value indicating whether the feature group is considered important for this analysis.<br><br>Equivalent to <code>p_value &#x3C; 0.1</code> </td></tr></tbody></table>



<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "feature_importance": [
        {
            "feature_group": "expos",
            "features": [
                "phq_attendance_expos"
            ],
            "p_value": 0.0,
            "important": true
        },
        {
            "feature_group": "school-holidays",
            "features": [
                "phq_attendance_school_holidays"
            ],
            "p_value": 0.0,
            "important": true
        },
        {
            "feature_group": "concerts",
            "features": [
                "phq_attendance_concerts"
            ],
            "p_value": 0.0002,
            "important": true
        },
        {
            "feature_group": "sports",
            "features": [
                "phq_attendance_sports"
            ],
            "p_value": 0.0039,
            "important": true
        },
        {
            "feature_group": "severe-weather",
            "features": [
                "phq_impact_severe_weather_air_quality_retail",
                "phq_impact_severe_weather_blizzard_retail",
                "phq_impact_severe_weather_cold_wave_retail",
                "phq_impact_severe_weather_cold_wave_snow_retail",
                "phq_impact_severe_weather_cold_wave_storm_retail",
                "phq_impact_severe_weather_dust_retail",
                "phq_impact_severe_weather_dust_storm_retail",
                "phq_impact_severe_weather_flood_retail",
                "phq_impact_severe_weather_heat_wave_retail",
                "phq_impact_severe_weather_hurricane_retail",
                "phq_impact_severe_weather_thunderstorm_retail",
                "phq_impact_severe_weather_tornado_retail",
                "phq_impact_severe_weather_tropical_storm_retail"
            ],
            "p_value": 0.1523,
            "important": false
        }
    ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/feature-importance \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/beam/analyses/<analysis_id>/feature-importance",
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

* [Beam Data Science Guide](../../getting-started/guides/beam-guides/beam-data-science-guide.md)

[^1]: An existing Beam Analysis ID.
