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

<table><thead><tr><th width="226">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Accept</code></td><td><p>Receive results in JSON or CSV by specifying the appropriate <code>Accept</code> header.</p><p>Supported values:</p><ul><li><code>application/json</code></li><li><code>text/csv</code></li></ul></td></tr></tbody></table>

### Query Parameters

<table><thead><tr><th width="224">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>offset</code><br><br>number</td><td><p>The number of results to skip. The default is <code>0</code>.</p><p>E.g. <code>?offset=20</code></p></td></tr><tr><td><code>limit</code><br><br>number</td><td><p>The maximum number of results to return per page. </p><p>The default limit is <code>100</code> and the maximum per page is <code>100</code>. </p><p>E.g. <code>?limit=10</code></p></td></tr></tbody></table>



### Request Body

<table><thead><tr><th width="243">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>active</code><br>object</td><td><p>The date range to calculate features for. This is named "active" because it includes events that are active within the date range. A multi-day event might start or end outside the specified date range - the days the event is active within the specified range will be included in the calculations.</p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>Note that all dates here are in local time (not UTC). Features API works on specific locations.</p><p>Please also note that the maximum supported date range is 90 days. If you require features over a wider date range please make multiple API requests.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "active": {
    "gte": "2019-11-28",
    "lte": "2019-11-29"
  }
}
</code></pre></td></tr><tr><td><code>beam</code><br><br>object</td><td><p></p><p>An optional <code>beam</code> analysis object which if provided will calculate the <code>location</code>, <code>interval</code>, <code>week_start_day</code> , <code>phq_*</code> features including <code>stats</code> and <code>phq_rank</code> from the Beam analysis and optionally the Beam analysis group.</p><p></p><p>Supports the following fields:</p><ul><li><code>analysis_id</code> - Beam analysis id (Required if <code>beam</code> block is present in the request body)</li><li><code>group_id</code> - Beam analysis group id (Optional)</li></ul><p>If <code>beam.analysis_id</code> is provided, the <code>location</code>, <code>interval</code>, <code>week_start_day</code> , <code>phq_*</code> features including<code>stats</code> and <code>phq_rank</code> will be calculated from the Beam analysis.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "beam": {
    "analysis_id": "0SXAmHsoZo0"
  }
}
</code></pre><p>If both <code>beam.analysis_id</code> and <code>beam.group_id</code> are provided, all the above fields will be calculated from the Beam analysis but the <code>phq_*</code> features will be calculated from the Beam analysis Group.</p><p><strong>Note:</strong> This is useful for when you want to request features for a variety of locations while maintaining feature consistency by limiting the returned features to those of the group's feature importance results.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "beam": {
    "analysis_id": "0SXaMHsoYo0",
    "group_id": "QxE9BcLq7ZY"
  }
}
</code></pre></td></tr><tr><td><code>hour_of_day_start</code><br>object</td><td><p>Time range (per day) to calculate features for.</p><p><strong>Note:</strong> This field is currently only supported on <code>phq_viewership_*</code> features.</p><p>If your location only operates within certain hours of the day you can use this filter to only include records that are happening within those hours.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>The values are hours between 0 and 23 (i.e. 24h format).</p><p>E.g. only include events happening between 1pm and 3pm each day.</p><pre class="language-json"><code class="lang-json">{
  "hour_of_day_start": {
    "gte": 13,
    "lte": 15
  }
}
</code></pre></td></tr><tr><td><code>location</code><br>object</td><td><p>Location to calculate features for. You can specify the location as a latitude/longitude (with radius), Place ID(s) or <a href="../saved-locations/">Saved Location</a> ID(s).</p><p>We recommend using a lat/lon+radius or a saved location id (for a point and radius location) as they could define the location of your interest more accurately. To work out a suitable radius around your location we strongly recommend using our <a href="../suggested-radius/get-suggested-radius.md">Suggested Radius API</a>.<br></p><p><strong>Note:</strong> When using Place IDs or Saved Location IDs a maximum of 3 IDs may be used.</p><p><strong>Note:</strong> When using lat/lon+radius, the radius must be in the format <code>&#x3C;radius>&#x3C;radius_unit></code>, where <code>&#x3C;radius></code> is an integer or a float number up to 2 decimal places and <code>&#x3C;radius_unit></code> is one of:</p><ul><li><code>m</code> - meters</li><li><code>km</code> - kilometers</li><li><code>ft</code> - feet</li><li><code>mi</code> - miles</li></ul><p>E.g. using Place IDs:</p><pre class="language-json"><code class="lang-json">{
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

#### Available Features

{% tabs %}
{% tab title="PHQ Attendance Features" %}
PHQ Attendance features provide daily-level aggregated stats based on the number of people who we predict will attend events on a given day. This takes into account complications like distributing attendance across multi-day events.

{% hint style="success" %}
We recommend using impact pattern features instead of generic features if you are in one of the supported industries. See [#attended-events-impact-patterns](get-features.md#attended-events-impact-patterns "mention").
{% endhint %}

**Attended Events Generic Features**

Use the generic features in this table if you are not in one of the industries covered by the impact pattern features listed below.

<table><thead><tr><th width="431">Feature</th><th>Description</th></tr></thead><tbody><tr><td><code>phq_attendance_academic_graduation</code></td><td>Academic - Graduation</td></tr><tr><td><code>phq_attendance_academic_social</code></td><td>Academic - Social</td></tr><tr><td><code>phq_attendance_community</code></td><td>Community</td></tr><tr><td><code>phq_attendance_concerts</code></td><td>Concerts</td></tr><tr><td><code>phq_attendance_conferences</code></td><td>Conferences</td></tr><tr><td><code>phq_attendance_expos</code></td><td>Expos</td></tr><tr><td><code>phq_attendance_festivals</code></td><td>Festivals</td></tr><tr><td><code>phq_attendance_performing_arts</code></td><td>Performing Arts</td></tr><tr><td><code>phq_attendance_sports</code></td><td>Sports</td></tr><tr><td><code>phq_attendance_school_holidays</code></td><td>School Holidays</td></tr></tbody></table>

**Attended Events Impact Pattern Features**

Demand impact patterns model the impact of leading days (days before the event), lagging days (days after an event), and the days the event occurs. In the Features API, Impact Patterns are provided as different features with a feature per industry. We have impact pattern features for the accommodation, hospitality (which covers food & beverage including restaurants), and retail industries.

The features above are generic features and the features in the table below are the impact pattern features per industry. For example, if you were in the accommodation industry and wanted a feature for the conferences category you'd use `phq_attendance_conferences_accommodation`.

{% hint style="success" %}
We recommend using impact pattern features instead of generic features if you are in one of the supported industries. See [impact-patterns.md](../../getting-started/predicthq-data/impact-patterns.md "mention") for more details.
{% endhint %}

<table><thead><tr><th width="462">Feature</th><th>Description</th></tr></thead><tbody><tr><td><code>phq_attendance_community_accommodation</code></td><td>Community accommodation impact</td></tr><tr><td><code>phq_attendance_concerts_accommodation</code></td><td>Concerts accommodation impact</td></tr><tr><td><code>phq_attendance_conferences_accommodation</code></td><td>Conferences accommodation impact</td></tr><tr><td><code>phq_attendance_expos_accommodation</code></td><td>Expos accommodation impact</td></tr><tr><td><code>phq_attendance_festivals_accommodation</code></td><td>Festivals accommodation impact</td></tr><tr><td><code>phq_attendance_performing_arts_accommodation</code></td><td>Performing Arts accommodation impact</td></tr><tr><td><code>phq_attendance_sports_accommodation</code></td><td>Sports accommodation impact</td></tr><tr><td><code>phq_attendance_community_hospitality</code></td><td>Community hospitality impact</td></tr><tr><td><code>phq_attendance_concerts_hospitality</code></td><td>Concerts hospitality impact</td></tr><tr><td><code>phq_attendance_conferences_hospitality</code></td><td>Conferences hospitality impact</td></tr><tr><td><code>phq_attendance_expos_hospitality</code></td><td>Expos hospitality impact</td></tr><tr><td><code>phq_attendance_festivals_hospitality</code></td><td>Festivals hospitality impact</td></tr><tr><td><code>phq_attendance_performing_arts_hospitality</code></td><td>Performing Arts hospitality impact</td></tr><tr><td><code>phq_attendance_sports_hospitality</code></td><td>Sports hospitality impact</td></tr><tr><td><code>phq_attendance_community_retail</code></td><td>Community Retail impact</td></tr><tr><td><code>phq_attendance_concerts_retail</code></td><td>Concerts Retail impact</td></tr><tr><td><code>phq_attendance_conferences_retail</code></td><td>Conferences Retail impact</td></tr><tr><td><code>phq_attendance_expos_retail</code></td><td>Expos Retail impact</td></tr><tr><td><code>phq_attendance_festivals_retail</code></td><td>Festivals Retail impact</td></tr><tr><td><code>phq_attendance_performing_arts_retail</code></td><td>Performing Arts Retail impact</td></tr><tr><td><code>phq_attendance_sports_retail</code></td><td>Sports Retail impact</td></tr></tbody></table>

### Configuration

You can configure PHQ Attendance features using the options below.

<table><thead><tr><th width="184">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>stats</code><br>object<br>optional</td><td><p>You can optionally configure which fields are calculated for each of these features by providing the list of <code>stats</code> fields you would like.</p><p>Default fields are <code>count</code> and <code>sum</code>.</p><p>Supported fields are:</p><ul><li><code>count</code></li><li><code>sum</code></li><li><code>min</code></li><li><code>max</code></li><li><code>avg</code></li><li><code>median</code></li><li><code>std_dev</code></li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "stats": [
    "count",
    "std_dev",
    "median"
  ]
}
</code></pre></td></tr><tr><td><code>phq_rank</code><br>object<br>optional</td><td><p>Filter for events with a PHQ Rank within a certain range.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "phq_rank": {
    "gt": 50,
    "lt": 80
  }
}
</code></pre></td></tr><tr><td><code>local_rank</code><br>object<br>optional</td><td><p></p><p>Filter for events with a Local Rank within a certain range.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "local_rank": {
    "gt": 50,
    "lt": 80
  }
}
</code></pre></td></tr></tbody></table>
{% endtab %}

{% tab title="PHQ Rank Features" %}
PHQ Rank features provide the daily-level aggregated sum of events bucketed by PHQ Rank level (1-5).

### PHQ Rank Impact Pattern Features

See the "Holidays and Observances Impact Pattern Features" under PHQ Impact in the tab above. These features cover the Accommodation, Retail, and Hospitality (Food & Beverage) industries.

{% hint style="success" %}
We recommend that if you operate in the supported industries you use the demand impact features for holidays and observances instead of the generic features as these will result in greater forecast accuracy as they include the impact before an event starts and after it finishes.
{% endhint %}

### PHQ Rank Generic Features

These are generic features that do not include demand impact patterns and should be used if you are _not_ in one of the industries that we have impact patterns for.

<table><thead><tr><th width="369">Feature</th><th>Description</th></tr></thead><tbody><tr><td><code>phq_rank_observances</code></td><td>Observances</td></tr><tr><td><code>phq_rank_public_holidays</code></td><td>Public Holidays</td></tr><tr><td><code>phq_rank_school_holidays</code></td><td>School Holidays</td></tr><tr><td><code>phq_rank_academic_session</code></td><td>Academic - Session</td></tr><tr><td><code>phq_rank_academic_exam</code></td><td>Academic - Exam</td></tr><tr><td><code>phq_rank_academic_holiday</code></td><td>Academic - Holiday</td></tr><tr><td><code>phq_rank_daylight_savings</code></td><td>Daylight savings</td></tr><tr><td><code>phq_rank_health_warnings</code></td><td>Health Warnings</td></tr><tr><td><code>phq_rank_politics</code></td><td>Politics</td></tr></tbody></table>

### Configuration

PHQ Rank features cannot currently be configured further. When requesting `phq_rank_*` features set the value as `true` indicating you require the default calculations.
{% endtab %}

{% tab title="PHQ Spend Features" %}
PHQ Spend features provide daily-level aggregated stats based on total USD we predict will be spent during events on a given day. This takes into account complications like distributing attendance across multi-day events.

You can request industry-specific features which are tuned to one of three potential industries:

* Accommodation: Event spend relating to hotels and hosts for the purposes of staying at during events. Spend can extend before and after an event actually starts/ends.
* Hospitality: Event spend on restaurants, food and drinks. Hotel restaurants are included in this industry.
* Transportation: Ground-based transportation for the purposes of getting to and from an event. Includes public and private transport, such as taxis, rails, busses and rideshares.

<table><thead><tr><th width="440">Feature</th><th>Description</th></tr></thead><tbody><tr><td><code>phq_spend_conferences</code></td><td>Conferences</td></tr><tr><td><code>phq_spend_expos</code></td><td>Expos</td></tr><tr><td><code>phq_spend_sports</code></td><td>Sports</td></tr><tr><td><code>phq_spend_community</code></td><td>Community</td></tr><tr><td><code>phq_spend_concerts</code></td><td>Concerts</td></tr><tr><td><code>phq_spend_festivals</code></td><td>Festivals</td></tr><tr><td><code>phq_spend_performing_arts</code></td><td>Performing Arts</td></tr><tr><td><code>phq_spend_conferences_accommodation</code></td><td>Conferences - Accommodation</td></tr><tr><td><code>phq_spend_expos_accommodation</code></td><td>Expos - Accommodation</td></tr><tr><td><code>phq_spend_sports_accommodation</code></td><td>Sports - Accommodation</td></tr><tr><td><code>phq_spend_community_accommodation</code></td><td>Community - Accommodation</td></tr><tr><td><code>phq_spend_concerts_accommodation</code></td><td>Concerts - Accommodation</td></tr><tr><td><code>phq_spend_festivals_accommodation</code></td><td>Festivals - Accommodation</td></tr><tr><td><code>phq_spend_performing_arts_accommodation</code></td><td>Performing Arts - Accommodation</td></tr><tr><td><code>phq_spend_conferences_hospitality</code></td><td>Conferences - Hospitality</td></tr><tr><td><code>phq_spend_expos_hospitality</code></td><td>Expos - Hospitality</td></tr><tr><td><code>phq_spend_sports_hospitality</code></td><td>Sports - Hospitality</td></tr><tr><td><code>phq_spend_community_hospitality</code></td><td>Community - Hospitality</td></tr><tr><td><code>phq_spend_concerts_hospitality</code></td><td>Concerts - Hospitality</td></tr><tr><td><code>phq_spend_festivals_hospitality</code></td><td>Festivals - Hospitality</td></tr><tr><td><code>phq_spend_performing_arts_hospitality</code></td><td>Performing Arts - Hospitality</td></tr><tr><td><code>phq_spend_conferences_transportation</code></td><td>Conferences - Transportation</td></tr><tr><td><code>phq_spend_expos_transportation</code></td><td>Expos - Transportation</td></tr><tr><td><code>phq_spend_sports_transportation</code></td><td>Sports - Transportation</td></tr><tr><td><code>phq_spend_community_transportation</code></td><td>Community - Transportation</td></tr><tr><td><code>phq_spend_concerts_transportation</code></td><td>Concerts - Transportation</td></tr><tr><td><code>phq_spend_festivals_transportation</code></td><td>Festivals - Transportation</td></tr><tr><td><code>phq_spend_performing_arts_transportation</code></td><td>Performing Arts - Transportation</td></tr></tbody></table>

### Configuration

You can configure PHQ Spend features using the options below.

<table><thead><tr><th width="184">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>stats</code><br>object<br>optional</td><td><p>You can optionally configure which fields are calculated for each of these features by providing the list of <code>stats</code> fields you would like.</p><p>Default fields are <code>count</code> and <code>sum</code>.</p><p>Supported fields are:</p><ul><li><code>count</code></li><li><code>sum</code></li><li><code>min</code></li><li><code>max</code></li><li><code>avg</code></li><li><code>median</code></li><li><code>std_dev</code></li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "stats": [
    "count",
    "std_dev",
    "median"
  ]
}
</code></pre></td></tr><tr><td><code>phq_rank</code><br>object<br>optional</td><td><p>Filter for events with a PHQ Rank within a certain range.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "phq_rank": {
    "gt": 50,
    "lt": 80
  }
}
</code></pre></td></tr><tr><td><code>local_rank</code><br>object<br>optional</td><td><p></p><p>Filter for events with a Local Rank within a certain range.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "local_rank": {
    "gt": 50,
    "lt": 80
  }
}
</code></pre></td></tr></tbody></table>
{% endtab %}

{% tab title="PHQ Viewership Features" %}
PHQ Viewership features provide daily-level aggregated stats based on the number of people who we predict will view broadcasts on a given day.

<table><thead><tr><th width="596">Feature</th><th width="385">Description</th></tr></thead><tbody><tr><td><code>phq_viewership_sports</code></td><td>Sports - (All)</td></tr><tr><td><code>phq_viewership_sports_american_football</code></td><td>American Football - (All)</td></tr><tr><td><code>phq_viewership_sports_american_football_ncaa_men</code></td><td>American Footbal - NCAA Men's</td></tr><tr><td><code>phq_viewership_sports_american_football_nfl</code></td><td>American Football - NFL</td></tr><tr><td><code>phq_viewership_sports_auto_racing</code></td><td>Automotive Racing - All</td></tr><tr><td><code>phq_viewership_sports_auto_racing_indy_car</code></td><td>Automotive Racing - Indy Car</td></tr><tr><td><code>phq_viewership_sports_auto_racing_nascar</code></td><td>Automotive Racing - NASCAR</td></tr><tr><td><code>phq_viewership_sports_baseball</code></td><td>Baseball - (All)</td></tr><tr><td><code>phq_viewership_sports_baseball_mlb</code></td><td>Baseball - MLB</td></tr><tr><td><code>phq_viewership_sports_baseball_ncaa_men</code></td><td>Baseball - NCAA Men's</td></tr><tr><td><code>phq_viewership_sports_basketball</code></td><td>Basketball - (All)</td></tr><tr><td><code>phq_viewership_sports_basketball_nba</code></td><td>Basketball - NBA</td></tr><tr><td><code>phq_viewership_sports_basketball_ncaa_men</code></td><td>Basketball - NCAA Men's</td></tr><tr><td><code>phq_viewership_sports_basketball_ncaa_women</code></td><td>Basketball - NCAA Women's</td></tr><tr><td><code>phq_viewership_sports_boxing</code></td><td>Boxing - (All)</td></tr><tr><td><code>phq_viewership_sports_golf</code></td><td>Golf - (All)</td></tr><tr><td><code>phq_viewership_sports_golf_masters</code></td><td>Golf - Masters</td></tr><tr><td><code>phq_viewership_sports_golf_pga_championship</code></td><td>Golf - PGA Championships</td></tr><tr><td><code>phq_viewership_sports_golf_pga_tour</code></td><td>Golf - PGA Tours</td></tr><tr><td><code>phq_viewership_sports_golf_us_open</code></td><td>Golf - US Open</td></tr><tr><td><code>phq_viewership_sports_horse_racing</code></td><td>Horse Racing - (All)</td></tr><tr><td><code>phq_viewership_sports_horse_racing_belmont_stakes</code></td><td>Horse Racing - Belmont Stakes</td></tr><tr><td><code>phq_viewership_sports_horse_racing_kentucky_derby</code></td><td>Horse Racing - Kentucky Derby</td></tr><tr><td><code>phq_viewership_sports_horse_racing_preakness_stakes</code></td><td>Horse Racing - Preakness Stakes</td></tr><tr><td><code>phq_viewership_sports_ice_hockey</code></td><td>Ice Hockey - (All)</td></tr><tr><td><code>phq_viewership_sports_ice_hockey_nhl</code></td><td>Ice Hockey - NHL</td></tr><tr><td><code>phq_viewership_sports_mma</code></td><td>Mixed Martial Arts - (All)</td></tr><tr><td><code>phq_viewership_sports_mma_ufc</code></td><td>Mixed Martial Arts - UFC</td></tr><tr><td><code>phq_viewership_sports_soccer</code></td><td>Soccer - (All)</td></tr><tr><td><code>phq_viewership_sports_soccer_concacaf_champions_league</code></td><td>Soccer - CONCACAF Champions League</td></tr><tr><td><code>phq_viewership_sports_soccer_concacaf_gold_cup</code></td><td>Soccer - CONCACAF Gold Cup</td></tr><tr><td><code>phq_viewership_sports_soccer_copa_america_men</code></td><td>Soccer - COPA America Men's</td></tr><tr><td><code>phq_viewership_sports_soccer_fifa_world_cup_women</code></td><td>Soccer - FIFA World Cup Women's</td></tr><tr><td><code>phq_viewership_sports_soccer_fifa_world_cup_men</code></td><td>Soccer - FIFA World Cup Men's</td></tr><tr><td><code>phq_viewership_sports_soccer_mls</code></td><td>Soccer - MLS</td></tr><tr><td><code>phq_viewership_sports_soccer_uefa_champions_league_men</code></td><td>Soccer - UEFA Champions League Men's</td></tr><tr><td><code>phq_viewership_sports_softball</code></td><td>Softball - (All)</td></tr><tr><td><code>phq_viewership_sports_softball_ncaa_women</code></td><td>Softball - NCAA Women's</td></tr><tr><td><code>phq_viewership_sports_tennis</code></td><td>Tennis - (All)</td></tr><tr><td><code>phq_viewership_sports_tennis_us_open</code></td><td>Tennis - US Open</td></tr><tr><td><code>phq_viewership_sports_tennis_wimbledon</code></td><td>Tennis - Wimbledon</td></tr></tbody></table>

### Configuration

You can configure PHQ Attendance features using the options below.

<table data-full-width="true"><thead><tr><th width="184">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>stats</code><br>object<br>optional</td><td><p>You can optionally configure which fields are calculated for each of these features by providing the list of <code>stats</code> fields you would like.</p><p>Default fields are <code>count</code> and <code>sum</code>.</p><p>Supported fields are:</p><ul><li><code>count</code></li><li><code>sum</code></li><li><code>min</code></li><li><code>max</code></li><li><code>avg</code></li><li><code>median</code></li><li><code>std_dev</code></li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "stats": [
    "count",
    "std_dev",
    "median"
  ]
}
</code></pre></td></tr><tr><td><code>phq_rank</code><br>object<br>optional</td><td><p>Filter for events with a PHQ Rank within a certain range.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "phq_rank": {
    "gt": 50,
    "lt": 80
  }
}
</code></pre></td></tr><tr><td><code>local_rank</code><br>object<br>optiona</td><td><p></p><p>Filter for events with a Local Rank within a certain range.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "local_rank": {
    "gt": 50,
    "lt": 80
  }
}
</code></pre></td></tr></tbody></table>
{% endtab %}

{% tab title="PHQ Impact Features" %}
PHQ Impact features provide daily-level aggregated stats based on the predicted impact of an event. This takes into account complications like Impact Patterns (leading and lagging effects of an event).

**Holidays and Observances Impact Pattern Features**

These features include the demand impact patterns for public holidays and observances. For example, these features will show when people typically arrive and book accommodation before a holiday and if they tend to leave after the holiday. See [impact-patterns.md](../../getting-started/predicthq-data/impact-patterns.md "mention")

{% hint style="success" %}
We recommend that if you operate in the industries listed below you use the demand impact features for holidays and observances instead of the generic features as these will result in greater forecast accuracy as they include the impact before an event starts and after it finishes.
{% endhint %}

<table><thead><tr><th width="375">Feature</th><th width="149">Category</th><th>Industry</th></tr></thead><tbody><tr><td><code>phq_impact_public_holidays_accommodation</code></td><td>Public holidays</td><td>Accomodation</td></tr><tr><td><code>phq_impact_observances_accommodation</code></td><td>Observances</td><td>Accomodation</td></tr><tr><td><code>phq_impact_public_holidays_retail</code></td><td>Public holidays</td><td>Retail</td></tr><tr><td><code>phq_impact_observances_retail</code></td><td>Observances</td><td>Retail</td></tr><tr><td><code>phq_impact_public_holidays_hospitality</code></td><td>Public holidays</td><td>Hospitality/Food &#x26; Beverage*</td></tr><tr><td><code>phq_impact_observances_hospitality</code></td><td>Observances</td><td>Hospitality/Food &#x26; Beverage</td></tr></tbody></table>

**Severe Weather Impact Features**

Currently supported industries are: Retail.

<table><thead><tr><th width="560">Feature</th><th width="352">Description</th><th>Industry</th></tr></thead><tbody><tr><td><code>phq_impact_severe_weather_air_quality_retail</code></td><td>Severe Weather - Air Quality</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_blizzard_retail</code></td><td>Severe Weather - Blizzard</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_cold_wave_retail</code></td><td>Severe Weather - Cold Wave - (All)</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_cold_wave_snow_retail</code></td><td>Severe Weather - Cold Wave - Snow</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_cold_wave_storm_retail</code></td><td>Severe Weather - Cold Wave - Storm</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_dust_retail</code></td><td>Severe Weather - Dust - (All)</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_dust_storm_retail</code></td><td>Severe Weather - Dust - Storm</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_flood_retail</code></td><td>Severe Weather - Flood</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_heat_wave_retail</code></td><td>Severe Weather - Heat Wave</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_hurricane_retail</code></td><td>Severe Weather - Hurricane</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_thunderstorm_retail</code></td><td>Severe Weather - Thunderstorm</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_tornado_retail</code></td><td>Severe Weather - Tornado</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_tropical_storm_retail</code></td><td>Severe Weather - Tropical Storm</td><td>Retail</td></tr></tbody></table>

**Attended Events Impact Features**

See [#attended-events-impact-pattern-features](get-features.md#attended-events-impact-pattern-features "mention")

### Configuration

You can configure PHQ Impact features using the options below.

<table><thead><tr><th width="184">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>stats</code><br>object<br>optional</td><td><p>You can optionally configure which fields are calculated for each of these features by providing the list of <code>stats</code> fields you would like.</p><p>Default fields are <code>count</code> and <code>sum</code>.</p><p>Supported fields are:</p><ul><li><code>count</code></li><li><code>sum</code></li><li><code>min</code></li><li><code>max</code></li><li><code>avg</code></li><li><code>median</code></li><li><code>std_dev</code></li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "stats": [
    "count",
    "std_dev",
    "median"
  ]
}
</code></pre></td></tr><tr><td><code>phq_rank</code><br>object<br>optional</td><td><p>Filter for events with a PHQ Rank within a certain range.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "phq_rank": {
    "gt": 50,
    "lt": 80
  }
}
</code></pre></td></tr><tr><td><code>local_rank</code><br>object<br>optional</td><td><p></p><p>Filter for events with a Local Rank within a certain range.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "local_rank": {
    "gt": 50,
    "lt": 80
  }
</code></pre></td></tr></tbody></table>
{% endtab %}
{% endtabs %}

## Response

### Response Fields

<table><thead><tr><th width="203">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>results</code><br>array</td><td><p>List of results where each item is a Feature.</p><p><br>Please refer to the Feature Response Fields section below for the structure of each record.<br><br>Note that pagination is not required in this API.</p></td></tr></tbody></table>

#### Feature Response Fields

Other than the date, the structure of each result here will depend on how you configured the feature in your request and the type of feature.

{% tabs %}
{% tab title="PHQ Attendance Features" %}
<table><thead><tr><th width="221">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>date</code><br>string</td><td>Date in local time.<br><br>E.g. <code>2023-10-01</code></td></tr><tr><td><code>&#x3C;phq_attendance_*></code><br>object</td><td><p>Daily-level feature result. The structure of the result here will depend on how you configured the feature in your request.</p><p>PHQ Attendance features are stats-based.</p><p>Default fields are <code>count</code> and <code>sum</code>.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "stats": {
    "count": 5,
    "sum": 17307,
    "min": 1000,
    "max": 9215,
    "avg": 3461.4,
    "median": 2620.0,
    "std_dev": 2978.810473997968
  }
}
</code></pre></td></tr></tbody></table>
{% endtab %}

{% tab title="PHQ Rank Features" %}
<table><thead><tr><th width="196">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>date</code><br>string</td><td>Date in local time.<br><br>E.g. <code>2023-10-01</code></td></tr><tr><td><code>&#x3C;phq_rank_*></code><br>object</td><td><p>Daily-level feature result. The structure of the result here is always the same as PHQ Rank features cannot currently be configured.</p><p>Will contain a <code>rank_levels</code> field which indicates the sum of matching events active on the date at each PHQ Rank level.</p><p>PHQ Rank is on a scale of 0 to 100 and the levels are bucketed as:</p><ul><li><code>1</code> - Minor (rank between 0 and 20).</li><li><code>2</code> - Moderate (rank between 21 and 40).</li><li><code>3</code> - Important (rank between 41 and 60).</li><li><code>4</code> - Significant (rank between 61 and 80).</li><li><code>5</code> - Major (rank between 81 and 100).</li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "rank_levels": {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 2,
    "5": 0
  }
}
</code></pre></td></tr></tbody></table>
{% endtab %}

{% tab title="PHQ Spend Features" %}
<table><thead><tr><th width="221">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>date</code><br>string</td><td>Date in local time.<br><br>E.g. <code>2023-10-01</code></td></tr><tr><td><code>&#x3C;phq_spend_*></code><br>object</td><td><p>Daily-level feature result. The structure of the result here will depend on how you configured the feature in your request.</p><p>PHQ Spend features are stats-based.</p><p>Default fields are <code>count</code> and <code>sum</code>.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "stats": {
    "count": 5,
    "sum": 17307,
    "min": 1000,
    "max": 9215,
    "avg": 3461.4,
    "median": 2620.0,
    "std_dev": 2978.810473997968
  }
}
</code></pre></td></tr></tbody></table>
{% endtab %}

{% tab title="PHQ Viewership Features" %}
<table><thead><tr><th width="235">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>date</code><br>string</td><td>Date in local time.<br><br>E.g. <code>2023-10-01</code></td></tr><tr><td><code>&#x3C;phq_viewership_*></code><br>object</td><td><p>Daily-level feature result. The structure of the result here will depend on how you configured the feature in your request.</p><p>PHQ Viewership features are stats-based.</p><p>Default fields are <code>count</code> and <code>sum</code>.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "stats": {
    "count": 5,
    "sum": 17307,
    "min": 1000,
    "max": 9215,
    "avg": 3461.4,
    "median": 2620.0,
    "std_dev": 2978.810473997968
  }
}
</code></pre></td></tr></tbody></table>
{% endtab %}

{% tab title="PHQ Impact Features" %}
<table><thead><tr><th width="235">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>date</code><br>string</td><td>Date in local time.<br><br>E.g. <code>2023-10-01</code></td></tr><tr><td><code>&#x3C;phq_impact_*></code><br>object</td><td><p>Daily-level feature result. The structure of the result here will depend on how you configured the feature in your request.</p><p>PHQ Impact features are stats-based.</p><p>Default fields are <code>count</code> and <code>sum</code>.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "stats": {
    "count": 5,
    "sum": 17307,
    "min": 1000,
    "max": 9215,
    "avg": 3461.4,
    "median": 2620.0,
    "std_dev": 2978.810473997968
  }
}
</code></pre></td></tr></tbody></table>
{% endtab %}
{% endtabs %}

### Response Format

You can receive responses formatted as JSON (default) or CSV. Use the `Accept` header when performing your request to define which format you would like to receive.

{% tabs %}
{% tab title="JSON" %}
With the `Accept` header set to `application/json` you will receive the results as JSON like the example below:

```json
{
  "results": [
    {
      "date": "2019-11-16",
      "phq_attendance_concerts": {
        "stats": {
          "count": 20,
          "sum": 6751
        }
      },
      "phq_attendance_conferences": {
        "stats": {
          "min": 1500,
          "max": 1500
        }
      },
      "phq_attendance_sports": {
        "stats": {
          "count": 5,
          "sum": 17307,
          "min": 1000,
          "max": 9215,
          "avg": 3461.4,
          "median": 2620.0,
          "std_dev": 2978.810473997968
        }
      },
      "phq_rank_public_holidays": {
        "rank_levels": {
          "1": 0,
          "2": 0,
          "3": 0,
          "4": 0,
          "5": 0
        }
      }
    },
    {
      "date": "2019-11-17",
      "phq_attendance_concerts": {
        "stats": {
          "count": 2,
          "sum": 241
        }
      },
      "phq_attendance_conferences": {
        "stats": {
          "min": 67,
          "max": 67
        }
      },
      "phq_attendance_sports": {
        "stats": {
          "count": 1,
          "sum": 852,
          "min": 852,
          "max": 852,
          "avg": 852.0,
          "median": 852.0,
          "std_dev": 0.0
        }
      },
      "phq_rank_public_holidays": {
        "rank_levels": {
          "1": 0,
          "2": 0,
          "3": 0,
          "4": 0,
          "5": 0
        }
      }
    }
  ]
}
```
{% endtab %}

{% tab title="CSV" %}
With the `Accept` header set to `text/csv` you will receive the results as CSV like the example below:

```csv
date,phq_attendance_concerts_stats_count,phq_attendance_concerts_stats_sum,phq_attendance_conferences_stats_min,phq_attendance_conferences_stats_max,phq_attendance_sports_stats_count,phq_attendance_sports_stats_sum,phq_attendance_sports_stats_min,phq_attendance_sports_stats_max,phq_attendance_sports_stats_avg,phq_attendance_sports_stats_median,phq_attendance_sports_stats_std_dev,phq_rank_public_holidays_rank_levels_1,phq_rank_public_holidays_rank_levels_2,phq_rank_public_holidays_rank_levels_3,phq_rank_public_holidays_rank_levels_4,phq_rank_public_holidays_rank_levels_5
2019-11-16,43,24546,11,1000,0,0,0,0,0.0,0.0,,0,0,0,0,0
2019-11-17,25,13440,11,146,0,0,0,0,0.0,0.0,,0,0,0,0,0
2019-11-18,6,2021,11,700,0,0,0,0,0.0,0.0,,0,0,0,0,0
2019-11-19,10,6047,11,171000,0,0,0,0,0.0,0.0,,0,0,0,0,0
2019-11-20,14,59704,11,171000,0,0,0,0,0.0,0.0,,0,0,0,0,0
2019-11-21,21,60851,11,171000,0,0,0,0,0.0,0.0,,0,0,0,0,0
2019-11-22,35,25760,11,171000,0,0,0,0,0.0,0.0,,0,0,0,0,0
2019-11-23,29,25425,11,394,0,0,0,0,0.0,0.0,,0,0,0,0,0
2019-11-24,18,23410,11,500,0,0,0,0,0.0,0.0,,0,0,0,0,0
2019-11-25,6,5122,11,1000,1,18064,18064,18064,18064.0,18064.0,0.0,0,0,0,0,0
2019-11-26,8,6861,11,1000,0,0,0,0,0.0,0.0,,0,0,0,0,0
2019-11-27,12,6225,11,500,1,18064,18064,18064,18064.0,18064.0,0.0,0,0,0,0,0
```

The same data represented as a table:

<table><thead><tr><th width="139">date</th><th width="335">phq_attendance_concerts_stats_count</th><th width="322">phq_attendance_concerts_stats_sum</th><th width="344">phq_attendance_conferences_stats_min</th><th width="350">phq_attendance_conferences_stats_max</th><th width="309">phq_attendance_sports_stats_count</th><th width="303">phq_attendance_sports_stats_sum</th><th width="299">phq_attendance_sports_stats_min</th><th width="300">phq_attendance_sports_stats_max</th><th width="306">phq_attendance_sports_stats_avg</th><th width="331">phq_attendance_sports_stats_median</th><th width="328">phq_attendance_sports_stats_std_dev</th><th width="337" data-type="number">phq_rank_public_holidays_rank_levels_1</th><th width="347" data-type="number">phq_rank_public_holidays_rank_levels_2</th><th width="358" data-type="number">phq_rank_public_holidays_rank_levels_3</th><th width="353" data-type="number">phq_rank_public_holidays_rank_levels_4</th><th width="341" data-type="number">phq_rank_public_holidays_rank_levels_5</th></tr></thead><tbody><tr><td>2019-11-16</td><td>43</td><td>24546</td><td>11</td><td>1000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0</td><td>0.0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2019-11-17</td><td>25</td><td>13440</td><td>11</td><td>146</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0</td><td>0.0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2019-11-18</td><td>6</td><td>2021</td><td>11</td><td>700</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0</td><td>0.0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2019-11-19</td><td>10</td><td>6047</td><td>11</td><td>171000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0</td><td>0.0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2019-11-20</td><td>14</td><td>59704</td><td>11</td><td>171000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0</td><td>0.0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2019-11-21</td><td>21</td><td>60851</td><td>11</td><td>171000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0</td><td>0.0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2019-11-22</td><td>35</td><td>25760</td><td>11</td><td>171000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0</td><td>0.0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2019-11-23</td><td>29</td><td>25425</td><td>11</td><td>394</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0</td><td>0.0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2019-11-24</td><td>18</td><td>23410</td><td>11</td><td>500</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0</td><td>0.0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2019-11-25</td><td>6</td><td>5122</td><td>11</td><td>1000</td><td>1</td><td>18064</td><td>18064</td><td>18064</td><td>18064.0</td><td>18064.0</td><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2019-11-26</td><td>8</td><td>6861</td><td>11</td><td>1000</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.0</td><td>0.0</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2019-11-27</td><td>12</td><td>6225</td><td>11</td><td>500</td><td>1</td><td>18064</td><td>18064</td><td>18064</td><td>18064.0</td><td>18064.0</td><td>0.0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></tbody></table>
{% endtab %}
{% endtabs %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X POST "https://api.predicthq.com/v1/features/?offset=0&limit=100" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     --data @<(cat <<EOF
    {
        "active": {
            "gte": "2019-11-16",
            "lte": "2019-11-17"
        },
        "location": {
            "geo": {
                "lat": "37.78428",
                "lon": "-122.40075",
                "radius": "2.6mi"
            }
        },
        "phq_attendance_conferences": {
            "stats": [
                "min",
                "max"
            ]
        },
        "phq_attendance_sports": {
            "stats": ["count", "std_dev", "median"],
            "phq_rank": { 
                "gt": 50
            }    
        },
        "phq_attendance_concerts": true,
        "phq_rank_public_holidays": true
    }
    EOF
    )
```
{% endtab %}

{% tab title="python" %}
```python
import requests

data = {
    "active": {
        "gte": "2019-11-16",
        "lte": "2019-11-27"
    },
    "location": {
        "geo": {
            "lat": "37.78428",
            "lon": "-122.40075",
            "radius": "2.6mi"
        }
    },
    "phq_attendance_conferences": {
        "stats": [
            "min",
            "max"
        ]
    },
    "phq_attendance_sports": {
        "stats": ["count", "std_dev", "median"],
        "phq_rank": { 
            "gt": 50
        }    
    },
    "phq_attendance_concerts": True,
    "phq_rank_public_holidays": True
}

response = requests.post(
    url="https://api.predicthq.com/v1/features/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
      "offset": 0,
      "limit": 100
    },
    json=data
)

print(response.json())
```
{% endtab %}

{% tab title="python sdk" %}
```python
from predicthq import Client

phq = Client(access_token="$ACCESS_TOKEN")

for feature in phq.features.obtain_features(
        active__gte="2019-11-16",
        active__lte="2019-11-27",
        location__geo={
            "lat": "37.78428",
            "lon": "-122.40075",
            "radius": "2.6mi"
        },
        phq_attendance_conferences__stats=["min", "max"],
        phq_attendance_sports__stats=["count", "std_dev", "median"],
        phq_attendance_sports__phq_rank={
            "gt": 50
        },
        phq_attendance_concerts=True,
        phq_rank_public_holidays=True
):
    print(feature.date, feature.phq_attendance_conferences.stats.min, 
        feature.phq_attendance_conferences.stats.max,
        feature.phq_attendance_sports.stats.count,
        feature.phq_attendance_sports.stats.std_dev,
        feature.phq_attendance_sports.stats.median,
        feature.phq_attendance_concerts.stats.count,
        feature.phq_attendance_concerts.stats.sum,
        feature.phq_rank_public_holidays.rank_levels)
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [increase-accuracy-with-the-features-api.md](../../getting-started/guides/features-api-guides/increase-accuracy-with-the-features-api.md "mention")
* [feature-engineering-guide.md](../../getting-started/guides/features-api-guides/feature-engineering-guide.md "mention")
* [demand-forecasting-data-science-guides.md](../../getting-started/guides/features-api-guides/demand-forecasting-data-science-guides.md "mention")
* [aggregating-live-tv-events.md](../../getting-started/guides/live-tv-event-guides/aggregating-live-tv-events.md "mention")
