---
description: >-
  The Features API provides features for ML Models across all types of demand
  causal factors, including attended events and non-attended events.
---

# Get Features

## Request

### HTTP Request

```
POST https://api.predicthq.com/v1/features/
```

### Request Headers

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>application/json</code></td></tr></tbody></table>

### Request Body

<table><thead><tr><th width="248">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>active</code><br>object</td><td><p>The date range to calculate features for. This is named "active" because it includes events that are active within the date range. A multi-day event might start or end outside the specified date range - the days the event is active within the specified range will be included in the calculations.</p><p></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>Note that all dates here are in local time (not UTC). Features API works on specific locations.</p><p></p><p>Please also note that the maximum supported date range is 90 days. If you require features over a wider date range please make multiple API requests.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "active": {
    "gte": "2019-11-28",
    "lte": "2019-11-29"
  }
}
</code></pre></td></tr><tr><td><code>hour_of_day_start</code><br>object</td><td><p>Time range (per day) to calculate features for.</p><p></p><p><strong>Note:</strong> This field is currently only supported on <code>phq_viewership_*</code> features.</p><p></p><p>If your location only operates within certain hours of the day you can use this filter to only include records that are happening within those hours.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>The values are hours between 0 and 23 (i.e. 24h format).</p><p></p><p>E.g. only include events happening between 1pm and 3pm each day.</p><pre class="language-json"><code class="lang-json">{
  "hour_of_day_start": {
    "gte": 13,
    "lte": 15
  }
}
</code></pre></td></tr><tr><td></td><td></td></tr><tr><td><code>location</code><br>object</td><td><p>Location to calculate features for. You can specify the location as either a latitude/longitude (with radius) or a Place ID.</p><p></p><p>We recommend using a lat/lon+radius so your location can be more accurately defined, and we strongly recommend using our <a href="../suggested-radius/get-suggested-radius.md">Suggested Radius API</a> to work out a suitable radius around your location.<br></p><p>When using Place IDs note that a maximum of 3 may be used.</p><p></p><p>E.g. using Place IDs.</p><pre class="language-json"><code class="lang-json">{
  "location": {
    "place_id": [
      5224323,
      5811704,
      4887398
    ]
  }
}
</code></pre><p></p><p>E.g. using a latitude/longitude and radius (recommended)</p><pre class="language-json"><code class="lang-json">{
  "location": {
    "geo": {
      "lat": 41.75038,
      "lon": -71.49978,
      "radius": "2.6mi"
    }
  }
}
</code></pre><p>The radius is in the format: <code>&#x3C;radius>&#x3C;radius_unit></code></p><p>Supported radius units are:</p><ul><li><code>m</code> - meters</li><li><code>km</code> - kilometers</li><li><code>ft</code> - feet</li><li><code>mi</code> - miles</li></ul><p></p></td></tr><tr><td><code>&#x3C;feature_name></code><br>object or boolean</td><td><p>The name of the feature you're requesting. You can request multiple features in a single request.<br><br>Features can be further configured here, or you can set the value as <code>true</code> to perform the default calculations for that feature.<br><br>Please see the tables below for a list of all currently supported features and how they can be further configured.<br></p><p>E.g. requesting certain stats fields and filtering for records with a PHQ Rank over 50.</p><pre class="language-json"><code class="lang-json">{
  "phq_attendance_sports": {
    "stats": ["count", "std_dev", "median"],
    "phq_rank": { 
      "gt": 50
    }
  }
}
</code></pre><p>E.g. requesting the default calculations for a feature.</p><pre class="language-json"><code class="lang-json">{
  "phq_attendance_concerts": true
}
</code></pre></td></tr></tbody></table>

### Available Features

{% tabs %}
{% tab title="PHQ Attendance Features" %}
PHQ Attendance features provide daily-level aggregated stats based on the number of people who we predict will attend events on a given day. This takes into account complications like distributing attendance across multi-day events.

<table><thead><tr><th width="396">Feature</th><th>Description</th></tr></thead><tbody><tr><td><code>phq_attendance_academic_graduation</code></td><td></td></tr><tr><td><code>phq_attendance_academic_social</code></td><td></td></tr><tr><td><code>phq_attendance_community</code></td><td></td></tr><tr><td><code>phq_attendance_concerts</code></td><td></td></tr><tr><td><code>phq_attendance_conferences</code></td><td></td></tr><tr><td><code>phq_attendance_expos</code></td><td></td></tr><tr><td><code>phq_attendance_festivals</code></td><td></td></tr><tr><td><code>phq_attendance_performing_arts</code></td><td></td></tr><tr><td><code>phq_attendance_sports</code></td><td></td></tr><tr><td><code>phq_attendance_school_holidays</code></td><td></td></tr><tr><td></td><td></td></tr></tbody></table>

## Configuration

You can configure each feature using the options below.

<table><thead><tr><th width="184">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>stats</code><br>object</td><td><p>You can optionally configure which fields are calculated for each of these features by providing the list of <code>stats</code> fields you would like.</p><p></p><p>Default fields are <code>count</code> and <code>sum</code>.</p><p></p><p>Supported fields are:</p><ul><li><code>count</code></li><li><code>sum</code></li><li><code>min</code></li><li><code>max</code></li><li><code>avg</code></li><li><code>median</code></li><li><code>std_dev</code></li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "stats": [
    "count",
    "std_dev",
    "median"
  ]
}
</code></pre></td></tr><tr><td><code>phq_rank</code><br>object</td><td><p>Filter for events with a PHQ Rank within a certain range.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>E.g. </p><pre class="language-json"><code class="lang-json">{
  "phq_rank": {
    "gt": 50,
    "lt": 80
  }
}
</code></pre></td></tr></tbody></table>
{% endtab %}

{% tab title="PHQ Rank Features" %}

{% endtab %}

{% tab title="PHQ Viewership Features" %}

{% endtab %}

{% tab title="PHQ Impact Features" %}

{% endtab %}
{% endtabs %}

## Response

### Response Fields

<details>

<summary>Example response</summary>

Below is an example response:

```json
...
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
xxx
```
{% endtab %}

{% tab title="python" %}
```python
xxx
```
{% endtab %}
{% endtabs %}
