---
title: Untitled
---



<table><thead><tr><th width="223">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>active</code><br>object</td><td><p>The date range to calculate features for. This is named "active" because it includes events that are active within the date range. A multi-day event might start or end outside the specified date range - the days the event is active within the specified range will be included in the calculations.</p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>Note that all dates here are in local time (not UTC). Features API works on specific locations.</p><p>Please also note that the maximum supported date range is 90 days. If you require features over a wider date range please make multiple API requests.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "active": {
    "gte": "2019-11-28",
    "lte": "2019-11-29"
  }
}
</code></pre></td></tr><tr><td><code>beam</code><br>object</td><td><pre class="language-json"><code class="lang-json">{
  "beam": {
    "analysis": "0SXaMhs0Yo0"
  }
}
</code></pre><p>Optionally supports a <code>beam.group_id</code></p></td></tr><tr><td><code>hour_of_day_start</code><br>object</td><td><p>Time range (per day) to calculate features for.</p><p><strong>Note:</strong> This field is currently only supported on <code>phq_viewership_*</code> features.</p><p>If your location only operates within certain hours of the day you can use this filter to only include records that are happening within those hours.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>The values are hours between 0 and 23 (i.e. 24h format).</p><p>E.g. only include events happening between 1pm and 3pm each day.</p><pre class="language-json"><code class="lang-json">{
  "hour_of_day_start": {
    "gte": 13,
    "lte": 15
  }
}
</code></pre></td></tr><tr><td><code>location</code><br>object</td><td><p>Location to calculate features for. You can specify the location as a latitude/longitude (with radius), Place ID(s) or <a href="../../api/saved-locations/">Saved Location</a> ID(s).</p><p>We recommend using a lat/lon+radius or a saved location id (for a point and radius location) as they could define the location of your interest more accurately. To work out a suitable radius around your location we strongly recommend using our <a href="../../api/suggested-radius/get-suggested-radius.md">Suggested Radius API</a>.<br></p><p><strong>Note:</strong> When using Place IDs or Saved Location IDs a maximum of 3 IDs may be used.</p><p><strong>Note:</strong> When using lat/lon+radius, the radius must be in the format <code>&#x3C;radius>&#x3C;radius_unit></code>, where <code>&#x3C;radius></code> is an integer or a float number up to 2 decimal places and <code>&#x3C;radius_unit></code> is one of:</p><ul><li><code>m</code> - meters</li><li><code>km</code> - kilometers</li><li><code>ft</code> - feet</li><li><code>mi</code> - miles</li></ul><p>E.g. using Place IDs:</p><pre class="language-json"><code class="lang-json">{
  "location": {
    "place_id": [
      5224323,
      5811704,
      4887398
    ]
  }
}
</code></pre><p>E.g. using Saved Location IDs:</p><pre class="language-json"><code class="lang-json">{
  "location": {
    "saved_location_id": [
      "BN7ZSw8xza9FviPVfyCycd",
      "X3uyTFbDOUaX2q_Qh5i31b",
      "X3uyTFbDOUhrfq_Qh5i31A"
    ]
  }
}
</code></pre><p>E.g. using a latitude/longitude and radius (recommended):</p><pre class="language-json"><code class="lang-json">{
  "location": {
    "geo": {
      "lat": 41.75038,
      "lon": -71.49978,
      "radius": "2.62mi"
    }
  }
}
</code></pre></td></tr><tr><td><code>interval</code><br>string<br>optional</td><td><p>Aggregation interval.<br><br><strong>Possible values:</strong></p><ul><li><code>day</code> (default) for daily aggregation</li><li><code>week</code> for weekly aggregation</li></ul></td></tr><tr><td><code>week_start_day</code><br>string<br>optional</td><td><p>The weekday to be treated as the start of the week.</p><p><strong>Possible values:</strong></p><ul><li><code>monday</code> (default)</li><li><code>tuesday</code></li><li><code>wednesday</code></li><li><code>thursday</code></li><li><code>friday</code></li><li><code>saturday</code></li><li><code>sunday</code></li></ul><p><br>Only applicable when <code>interval</code> is set to <code>week</code>.</p></td></tr><tr><td><code>&#x3C;feature_name></code><br>object or boolean</td><td><p>The name of the feature you're requesting. You can request multiple features in a single request.<br><br>Features can be further configured here, or you can set the value as <code>true</code> to perform the default calculations for that feature.<br><br>Please see the tables below for a list of all currently supported features and how they can be further configured.<br></p><p>E.g. requesting certain stats fields and filtering for records with a PHQ Rank over 50.</p><pre class="language-json"><code class="lang-json">{
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
