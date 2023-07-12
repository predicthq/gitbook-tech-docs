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

<table><thead><tr><th width="223">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>active</code><br>object</td><td><p>The date range to calculate features for. This is named "active" because it includes events that are active within the date range. A multi-day event might start or end outside the specified date range - the days the event is active within the specified range will be included in the calculations.</p><p></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>Note that all dates here are in local time (not UTC). Features API works on specific locations.</p><p></p><p>Please also note that the maximum supported date range is 90 days. If you require features over a wider date range please make multiple API requests.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
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
</code></pre></td></tr><tr><td><code>location</code><br>object</td><td><p>Location to calculate features for. You can specify the location as either a latitude/longitude (with radius) or a Place ID.</p><p></p><p>We recommend using a lat/lon+radius so your location can be more accurately defined, and we strongly recommend using our <a href="../suggested-radius/get-suggested-radius.md">Suggested Radius API</a> to work out a suitable radius around your location.<br></p><p>When using Place IDs note that a maximum of 3 may be used.</p><p></p><p>E.g. using Place IDs.</p><pre class="language-json"><code class="lang-json">{
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

#### Available Features

{% tabs %}
{% tab title="PHQ Attendance Features" %}
PHQ Attendance features provide daily-level aggregated stats based on the number of people who we predict will attend events on a given day. This takes into account complications like distributing attendance across multi-day events.

<table><thead><tr><th width="431">Feature</th><th>Description</th></tr></thead><tbody><tr><td><code>phq_attendance_academic_graduation</code></td><td>Academic - Graduation</td></tr><tr><td><code>phq_attendance_academic_social</code></td><td>Academic - Social</td></tr><tr><td><code>phq_attendance_community</code></td><td>Community</td></tr><tr><td><code>phq_attendance_concerts</code></td><td>Concerts</td></tr><tr><td><code>phq_attendance_conferences</code></td><td>Conferences</td></tr><tr><td><code>phq_attendance_expos</code></td><td>Expos</td></tr><tr><td><code>phq_attendance_festivals</code></td><td>Festivals</td></tr><tr><td><code>phq_attendance_performing_arts</code></td><td>Performing Arts</td></tr><tr><td><code>phq_attendance_sports</code></td><td>Sports</td></tr><tr><td><code>phq_attendance_school_holidays</code></td><td>School Holidays</td></tr></tbody></table>

## Configuration

You can configure PHQ Attendance features using the options below.

<table><thead><tr><th width="184">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>stats</code><br>object<br>optional</td><td><p>You can optionally configure which fields are calculated for each of these features by providing the list of <code>stats</code> fields you would like.</p><p></p><p>Default fields are <code>count</code> and <code>sum</code>.</p><p></p><p>Supported fields are:</p><ul><li><code>count</code></li><li><code>sum</code></li><li><code>min</code></li><li><code>max</code></li><li><code>avg</code></li><li><code>median</code></li><li><code>std_dev</code></li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "stats": [
    "count",
    "std_dev",
    "median"
  ]
}
</code></pre></td></tr><tr><td><code>phq_rank</code><br>object<br>optional</td><td><p>Filter for events with a PHQ Rank within a certain range.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>E.g. </p><pre class="language-json"><code class="lang-json">{
  "phq_rank": {
    "gt": 50,
    "lt": 80
  }
}
</code></pre></td></tr></tbody></table>
{% endtab %}

{% tab title="PHQ Rank Features" %}
PHQ Rank features provide daily-level aggregated sum of events bucketed by PHQ Rank level (1-5).

<table><thead><tr><th width="358">Feature</th><th>Description</th></tr></thead><tbody><tr><td><code>phq_rank_daylight_savings</code></td><td>Daylight Savings</td></tr><tr><td><code>phq_rank_health_warnings</code></td><td>Health Warnings</td></tr><tr><td><code>phq_rank_observances</code></td><td>Observances</td></tr><tr><td><code>phq_rank_public_holidays</code></td><td>Public Holidays</td></tr><tr><td><code>phq_rank_school_holidays</code></td><td>School Holidays</td></tr><tr><td><code>phq_rank_politics</code></td><td>Politics</td></tr><tr><td><code>phq_rank_academic_session</code></td><td>Academic - Session</td></tr><tr><td><code>phq_rank_academic_exam</code></td><td>Academic - Exam</td></tr><tr><td><code>phq_rank_academic_holiday</code></td><td>Academic - Holiday</td></tr></tbody></table>

## Configuration

PHQ Rank features cannot currently be configured further. When requesting `phq_rank_*` features set the value as `true` indicating you require the default calculations.
{% endtab %}

{% tab title="PHQ Viewership Features" %}
PHQ Viewership features provide daily-level aggregated stats based on the number of people who we predict will view broadcasts on a given day.

<table><thead><tr><th width="596">Feature</th><th width="385">Description</th></tr></thead><tbody><tr><td><code>phq_viewership_sports</code></td><td>Sports - (All)</td></tr><tr><td><code>phq_viewership_sports_american_football</code></td><td>American Football - (All)</td></tr><tr><td><code>phq_viewership_sports_american_football_ncaa_men</code></td><td>American Footbal - NCAA Men's</td></tr><tr><td><code>phq_viewership_sports_american_football_nfl</code></td><td>American Football - NFL</td></tr><tr><td><code>phq_viewership_sports_auto_racing</code></td><td>Automotive Racing - All</td></tr><tr><td><code>phq_viewership_sports_auto_racing_indy_car</code></td><td>Automotive Racing - Indy Car</td></tr><tr><td><code>phq_viewership_sports_auto_racing_nascar</code></td><td>Automotive Racing - NASCAR</td></tr><tr><td><code>phq_viewership_sports_baseball</code></td><td>Baseball - (All)</td></tr><tr><td><code>phq_viewership_sports_baseball_mlb</code></td><td>Baseball - MLB</td></tr><tr><td><code>phq_viewership_sports_baseball_ncaa_men</code></td><td>Baseball - NCAA Men's</td></tr><tr><td><code>phq_viewership_sports_basketball</code></td><td>Basketball - (All)</td></tr><tr><td><code>phq_viewership_sports_basketball_nba</code></td><td>Basketball - NBA</td></tr><tr><td><code>phq_viewership_sports_basketball_ncaa_men</code></td><td>Basketball - NCAA Men's</td></tr><tr><td><code>phq_viewership_sports_basketball_ncaa_women</code></td><td>Basketball - NCAA Women's</td></tr><tr><td><code>phq_viewership_sports_boxing</code></td><td>Boxing - (All)</td></tr><tr><td><code>phq_viewership_sports_golf</code></td><td>Golf - (All)</td></tr><tr><td><code>phq_viewership_sports_golf_masters</code></td><td>Golf - Masters</td></tr><tr><td><code>phq_viewership_sports_golf_pga_championship</code></td><td>Golf - PGA Championships</td></tr><tr><td><code>phq_viewership_sports_golf_pga_tour</code></td><td>Golf - PGA Tours</td></tr><tr><td><code>phq_viewership_sports_golf_us_open</code></td><td>Golf - US Open</td></tr><tr><td><code>phq_viewership_sports_horse_racing</code></td><td>Horse Racing - (All)</td></tr><tr><td><code>phq_viewership_sports_horse_racing_belmont_stakes</code></td><td>Horse Racing - Belmont Stakes</td></tr><tr><td><code>phq_viewership_sports_horse_racing_kentucky_derby</code></td><td>Horse Racing - Kentucky Derby</td></tr><tr><td><code>phq_viewership_sports_horse_racing_preakness_stakes</code></td><td>Horse Racing - Preakness Stakes</td></tr><tr><td><code>phq_viewership_sports_ice_hockey</code></td><td>Ice Hockey - (All)</td></tr><tr><td><code>phq_viewership_sports_ice_hockey_nhl</code></td><td>Ice Hockey - NHL</td></tr><tr><td><code>phq_viewership_sports_mma</code></td><td>Mixed Martial Arts - (All)</td></tr><tr><td><code>phq_viewership_sports_mma_ufc</code></td><td>Mixed Martial Arts - UFC</td></tr><tr><td><code>phq_viewership_sports_soccer</code></td><td>Soccer - (All)</td></tr><tr><td><code>phq_viewership_sports_soccer_concacaf_champions_league</code></td><td>Soccer - CONCACAF Champions League</td></tr><tr><td><code>phq_viewership_sports_soccer_concacaf_gold_cup</code></td><td>Soccer - CONCACAF Gold Cup</td></tr><tr><td><code>phq_viewership_sports_soccer_copa_america_men</code></td><td>Soccer - COPA America Men's</td></tr><tr><td><code>phq_viewership_sports_soccer_fifa_world_cup_women</code></td><td>Soccer - FIFA World Cup Women's</td></tr><tr><td><code>phq_viewership_sports_soccer_fifa_world_cup_men</code></td><td>Soccer - FIFA World Cup Men's</td></tr><tr><td><code>phq_viewership_sports_soccer_mls</code></td><td>Soccer - MLS</td></tr><tr><td><code>phq_viewership_sports_soccer_uefa_champions_league_men</code></td><td>Soccer - UEFA Champions League Men's</td></tr><tr><td><code>phq_viewership_sports_softball</code></td><td>Softball - (All)</td></tr><tr><td><code>phq_viewership_sports_softball_ncaa_women</code></td><td>Softball - NCAA Women's</td></tr><tr><td><code>phq_viewership_sports_tennis</code></td><td>Tennis - (All)</td></tr><tr><td><code>phq_viewership_sports_tennis_us_open</code></td><td>Tennis - US Open</td></tr><tr><td><code>phq_viewership_sports_tennis_wimbledon</code></td><td>Tennis - Wimbledon</td></tr></tbody></table>

## Configuration

You can configure PHQ Attendance features using the options below.

<table data-full-width="true"><thead><tr><th width="184">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>stats</code><br>object<br>optional</td><td><p>You can optionally configure which fields are calculated for each of these features by providing the list of <code>stats</code> fields you would like.</p><p></p><p>Default fields are <code>count</code> and <code>sum</code>.</p><p></p><p>Supported fields are:</p><ul><li><code>count</code></li><li><code>sum</code></li><li><code>min</code></li><li><code>max</code></li><li><code>avg</code></li><li><code>median</code></li><li><code>std_dev</code></li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "stats": [
    "count",
    "std_dev",
    "median"
  ]
}
</code></pre></td></tr><tr><td><code>phq_rank</code><br>object<br>optional</td><td><p>Filter for events with a PHQ Rank within a certain range.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>E.g. </p><pre class="language-json"><code class="lang-json">{
  "phq_rank": {
    "gt": 50,
    "lt": 80
  }
}
</code></pre></td></tr></tbody></table>
{% endtab %}

{% tab title="PHQ Impact Features" %}
PHQ Impact features provide daily-level aggregated stats based on the predicted impact of an event. This takes into account complications like Impact Patterns (leading and lagging effects of an event). Currently supported industries are: Retail.

<table><thead><tr><th width="560">Feature</th><th width="352">Description</th><th>Industry</th></tr></thead><tbody><tr><td><code>phq_impact_severe_weather_air_quality_retail</code></td><td>Severe Weather - Air Quality</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_blizzard_retail</code></td><td>Severe Weather - Blizzard</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_cold_wave_retail</code></td><td>Severe Weather - Cold Wave - (All)</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_cold_wave_snow_retail</code></td><td>Severe Weather - Cold Wave - Snow</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_cold_wave_storm_retail</code></td><td>Severe Weather - Cold Wave - Storm</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_dust_retail</code></td><td>Severe Weather - Dust - (All)</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_dust_storm_retail</code></td><td>Severe Weather - Dust - Storm</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_flood_retail</code></td><td>Severe Weather - Flood</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_heat_wave_retail</code></td><td>Severe Weather - Heat Wave</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_hurricane_retail</code></td><td>Severe Weather - Hurricane</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_thunderstorm_retail</code></td><td>Severe Weather - Thunderstorm</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_tornado_retail</code></td><td>Severe Weather - Tornado</td><td>Retail</td></tr><tr><td><code>phq_impact_severe_weather_tropical_storm_retail</code></td><td>Severe Weather - Tropical Storm</td><td>Retail</td></tr></tbody></table>

## Configuration

You can configure PHQ Impact features using the options below.

<table><thead><tr><th width="184">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>stats</code><br>object<br>optional</td><td><p>You can optionally configure which fields are calculated for each of these features by providing the list of <code>stats</code> fields you would like.</p><p></p><p>Default fields are <code>count</code> and <code>sum</code>.</p><p></p><p>Supported fields are:</p><ul><li><code>count</code></li><li><code>sum</code></li><li><code>min</code></li><li><code>max</code></li><li><code>avg</code></li><li><code>median</code></li><li><code>std_dev</code></li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "stats": [
    "count",
    "std_dev",
    "median"
  ]
}
</code></pre></td></tr><tr><td><code>phq_rank</code><br>object<br>optional</td><td><p>Filter for events with a PHQ Rank within a certain range.<br></p><p>Supports the following fields:</p><ul><li><code>gt</code> - greater than</li><li><code>gte</code> - greater than or equal</li><li><code>lt</code> - less than</li><li><code>lte</code> - less than or equal</li></ul><p>E.g. </p><pre class="language-json"><code class="lang-json">{
  "phq_rank": {
    "gt": 50,
    "lt": 80
  }
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
<table><thead><tr><th width="235">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>date</code><br>string</td><td>Date in local time.<br><br>E.g. <code>2023-10-01</code></td></tr><tr><td><code>&#x3C;phq_attendance_*></code><br>object</td><td><p>Daily-level feature result. The structure of the result here will depend on how you configured the feature in your request.</p><p></p><p>PHQ Attendance features are stats-based.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
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
<table><thead><tr><th width="196">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>date</code><br>string</td><td>Date in local time.<br><br>E.g. <code>2023-10-01</code></td></tr><tr><td><code>&#x3C;phq_rank_*></code><br>object</td><td><p>Daily-level feature result. The structure of the result here is always the same as PHQ Rank features cannot currently be configured.</p><p></p><p>Will contain a <code>rank_levels</code> field which indicates the sum of matching events active on the date at each PHQ Rank level.</p><p></p><p>PHQ Rank is on a scale of 0 to 100 and the levels are bucketed as:</p><ul><li><code>1</code> - Minor (rank between 0 and 20).</li><li><code>2</code> - Moderate (rank between 21 and 40).</li><li><code>3</code> - Important (rank between 41 and 60).</li><li><code>4</code> - Significant (rank between 61 and 80).</li><li><code>5</code> - Major (rank between 81 and 100).</li></ul><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
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

{% tab title="PHQ Viewership Features" %}
<table><thead><tr><th width="235">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>date</code><br>string</td><td>Date in local time.<br><br>E.g. <code>2023-10-01</code></td></tr><tr><td><code>&#x3C;phq_viewership_*></code><br>object</td><td><p>Daily-level feature result. The structure of the result here will depend on how you configured the feature in your request.</p><p></p><p>PHQ Viewership features are stats-based.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
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
<table><thead><tr><th width="235">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>date</code><br>string</td><td>Date in local time.<br><br>E.g. <code>2023-10-01</code></td></tr><tr><td><code>&#x3C;phq_impact_*></code><br>object</td><td><p>Daily-level feature result. The structure of the result here will depend on how you configured the feature in your request.</p><p></p><p>PHQ Impact features are stats-based.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
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

<details>

<summary>Example response</summary>

Below is an example response:

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

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X POST https://api.predicthq.com/v1/features/ \
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
    json=data
)

print(response.json())
```
{% endtab %}
{% endtabs %}
