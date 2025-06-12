---
description: Transforming Event Data into ML-Ready Features using SQL
---

# SQL Method Guide

## Using Snowflake SQL to recreate Features-API

This guide uses a publicly available PredictHQ event sample table called\
**PREDICTHQ\_EVENTS\_RETAIL\_LONDON**\
Please change this table name in all instances below with the name of the events data table that has been provisioned by PredictHQ as per the [Snowflake Secure Data Share](https://docs.predicthq.com/integrations/third-party-integrations/snowflake).

The rest of the guide also uses temporary tables but these tables can be turned into permanent tables as needed.

Once **SAVED\_LOCATIONS** has been created as per the parent page of this guide, the following steps are required and blocked out:

1. Modify the input input table format to use with the code in this guide
2. Generate daily aggregated statistics for each location by…
   * attendance based features
   * rank based features
   * impact based features
   * The date range in the following code examples should be updated based on the desired granularity:
     * For training a machine learning model, update the dates to get historical data for the locations
     * If running a model in production and forecasting future demand, update the dates for the visibility window of the forecast - e.g. the new week, month, or months
3. Join all features together in a single output table

## Step 1: Modify the input table format

Once the **SAVED\_LOCATIONS** input table is created, the below code shapes that table to be in a day by day format of the input called **SAVED\_LOCATIONS\_DAILY**:

{% code fullWidth="true" %}
```sql
----split the table out into having one day equals one row between the date range.
CREATE OR REPLACE TEMP TABLE saved_locations_daily AS
select
    date(date_start) + value::int as date,
    s.location,
    s.lat,
    s.lon,
    s.radius,
    lower(s.radius_unit) as radius_unit        --forcing the lower in case of data entry mistakes
   from saved_locations s,
     table(flatten(array_generate_range(0, datediff('day', date_start, date_end) + 1))) t
;
```
{% endcode %}

## Step 2: Calculating Daily Aggregated ML Features with SQL in Snowflake

Each Feature set will be calculated in blocks, see the column headers in each code block below for which Features are available to be generated.

### PHQ Attendance Features

Values are calculated as the sum of predicted attendance for the day at a given location within the defined radius.

<pre class="language-sql" data-title="PHQ Attended Features" data-full-width="true"><code class="lang-sql"><strong>----PHQ Attendance Features
</strong><strong>CREATE OR REPLACE TEMP TABLE phq_attendance_features AS
</strong>WITH events_attended AS (           --Attendance Features for main 7 categories
  SELECT 
    e.event_id,
    s.date,
    s.location,
    e.category, 
    imp.value:value::int as phq_attendance
  FROM predicthq.predicthq_events_retail_london e
  RIGHT JOIN saved_locations_daily s
    ON ST_DISTANCE(e.geo, ST_MAKEPOINT(s.lon, s.lat)) &#x3C;= 
      CASE 
        WHEN s.radius_unit = 'mi' THEN s.radius * 1609.34
        WHEN s.radius_unit = 'km' THEN s.radius * 1000
      END
    AND TO_DATE(CONVERT_TIMEZONE(CASE WHEN e.timezone IS NOT NULL THEN e.timezone ELSE 'UTC' END, e.event_start)) &#x3C;= s.date
    AND TO_DATE(CONVERT_TIMEZONE(CASE WHEN e.timezone IS NOT NULL THEN e.timezone ELSE 'UTC' END, e.event_end)) >= s.date,
  latERAL FlatTEN(INPUT => e.IMPACT_PATTERNS) vert,
  latERAL FlatTEN(INPUT => vert.value:impacts) imp
  WHERE imp.value:date_local::DATE = s.date
    AND vert.value:vertical::STRING = 'accommodation' 
    AND imp.value:position::STRING = 'event_day'
    AND e.phq_attendance IS NOT NULL
    AND e.category in ('community','concerts','conferences','expos','festivals','performing-arts','sports')
),
events_attended_other AS (          --Attendance Features for special categories
  SELECT 
    e.event_id,
    s.date,
    s.location,
    e.category, 
    e.phq_attendance,
    CASE WHEN category = 'academic' and ARRAY_CONTAINS('social'::variant, e.labels) THEN 'social'
        WHEN category = 'academic' and ARRAY_CONTAINS('social'::variant, e.labels) THEN 'graduation' 
        ELSE '' END as academic_split
  FROM predicthq.predicthq_events_retail_london e
  RIGHT JOIN saved_locations_daily s
    ON ST_DISTANCE(e.geo, ST_MAKEPOINT(s.lon, s.lat)) &#x3C;= 
      CASE 
        WHEN s.radius_unit = 'mi' THEN s.radius * 1609.34
        WHEN s.radius_unit = 'km' THEN s.radius * 1000
      END
    AND TO_DATE(CONVERT_TIMEZONE(CASE WHEN e.timezone IS NOT NULL THEN e.timezone ELSE 'UTC' END, e.event_start)) &#x3C;= s.date
    AND TO_DATE(CONVERT_TIMEZONE(CASE WHEN e.timezone IS NOT NULL THEN e.timezone ELSE 'UTC' END, e.event_end)) >= s.date
  WHERE e.phq_attendance IS NOT NULL
    AND e.category in ('school-holidays','academic')
),
attendance_group AS (               --Group the 7 main categories daily and make sure a result is displayed each day even if it's just 0
    SELECT
      data_range.date,
      data_range.location,
      SUM(CASE WHEN a.category = 'community' THEN a.phq_attendance ELSE 0 END) AS phq_attendance_community,
      SUM(CASE WHEN a.category = 'concerts' THEN a.phq_attendance ELSE 0 END) AS phq_attendance_concerts,
      SUM(CASE WHEN a.category = 'conferences' THEN a.phq_attendance ELSE 0 END)  AS phq_attendance_conferences,
      SUM(CASE WHEN a.category = 'expos' THEN a.phq_attendance ELSE 0 END) AS phq_attendance_expos,
      SUM(CASE WHEN a.category = 'festivals' THEN a.phq_attendance ELSE 0 END) AS phq_attendance_festivals,
      SUM(CASE WHEN a.category = 'performing-arts' THEN a.phq_attendance ELSE 0 END) AS phq_attendance_performing_arts,
      SUM(CASE WHEN a.category = 'sports' THEN a.phq_attendance ELSE 0 END) AS phq_attendance_sports
    FROM (SELECT date, location FROM saved_locations_daily) data_range
    LEFT JOIN events_attended a
        ON data_range.date = a.date
            AND data_range.location = a.location
    GROUP BY data_range.date, data_range.location
    ORDER BY data_range.date, data_range.location
),
attendance_group_other AS (         --Group the other categories daily and make sure a result is displayed each day even if it's just 0
    SELECT
      data_range.date,
      data_range.location, 
      SUM(CASE WHEN ao.category = 'school-holidays' THEN ao.phq_attendance ELSE 0 END) AS phq_attendance_school_holidays,
      SUM(CASE WHEN ao.academic_split = 'graduation' THEN ao.phq_attendance ELSE 0 END) AS phq_attendance_academic_graduation,
      SUM(CASE WHEN ao.academic_split = 'social' THEN ao.phq_attendance ELSE 0 END) AS phq_attendance_academic_social
    FROM (SELECT date, location FROM saved_locations_daily) data_range
    LEFT JOIN events_attended_other ao
        ON data_range.date = ao.date
            AND data_range.location = ao.location
    GROUP BY data_range.date, data_range.location
    ORDER BY data_range.date, data_range.location
)
SELECT                              --final select for phq_attendance_features
  ag.date,
  ag.location,
  ag.phq_attendance_community,
  ag.phq_attendance_concerts,
  ag.phq_attendance_conferences,
  ag.phq_attendance_expos,
  ag.phq_attendance_festivals,
  ag.phq_attendance_performing_arts,
  ag.phq_attendance_sports,
  ago.phq_attendance_school_holidays,
  ago.phq_attendance_academic_graduation,
  ago.phq_attendance_academic_social      
FROM attendance_group ag
LEFT JOIN attendance_group_other ago
    ON ag.location = ago.location
        AND ag.date = ago.date
;

SELECT * FROM phq_attendance_features order by location, date;
</code></pre>

If metrics other than SUM are desired, use the below code as a template for each column. The category name part of the code for each column (in these examples defaulted to ‘community’) will need to be replaced depending on which PHQ Attendance Feature is intended to be called. Refer to the column code above for available Feature categories.

{% code title="Count" fullWidth="true" %}
```sql
COUNT(CASE WHEN a.category = 'community' THEN 1 ELSE NULL END)
```
{% endcode %}

{% code title="Average" fullWidth="true" %}
```sql
IFNULL(ROUND(AVG(CASE WHEN a.category = 'community' THEN a.phq_attendance ELSE NULL END),2),0)Some code
```
{% endcode %}

{% code title="Median" fullWidth="true" %}
```sql
IFNULL(ROUND(MEDIAN(CASE WHEN a.category = 'community' THEN a.phq_attendance ELSE NULL END),2),0)
```
{% endcode %}

{% code title="Standard Deviation" fullWidth="true" %}
```sql
IFNULL(ROUND(STDDEV(CASE WHEN a.category = 'community' THEN a.phq_attendance ELSE NULL END),2),0)
```
{% endcode %}

{% code title="Min and Max" fullWidth="true" %}
```sql
IFNULL(MIN(CASE WHEN a.category = 'community' THEN a.phq_attendance ELSE NULL END),0)
IFNULL(MAX(CASE WHEN a.category = 'community' THEN a.phq_attendance ELSE NULL END),0)
```
{% endcode %}

### PHQ Rank Features

Values are calculated as a count of events occurring at each rank level, per day, per location. If an event occurs over multiple days, it will have a result in each day until the event is over. Each rank level is returned as its own column.

{% code title="PHQ Rank Features" fullWidth="true" %}
```sql
----PHQ Rank Features
CREATE OR REPLACE TEMP TABLE phq_rank_features as 
WITH events_ranked AS (             --Pull ranked events within range
  SELECT 
    e.event_id,
    s.date,
    s.location,
    e.category,
    e.phq_rank,
    CASE WHEN category = 'academic' and ARRAY_CONTAINS('academic-session'::variant, e.labels) THEN 'session'
        WHEN category = 'academic' and ARRAY_CONTAINS('exam'::variant, e.labels) THEN 'exam' 
        WHEN category = 'academic' and ARRAY_CONTAINS('holiday'::variant, e.labels) THEN 'holiday' 
        ELSE '' END AS academic_split,
    CASE 
      WHEN e.phq_rank between 0 and 20 THEN 1
      WHEN e.phq_rank between 21 and 40 THEN 2
      WHEN e.phq_rank between 41 and 60 THEN 3
      WHEN e.phq_rank between 61 and 80 THEN 4
      ELSE 5
    END as rank_level
  FROM predicthq.predicthq_events_retail_london e
  RIGHT JOIN saved_locations_daily s
    ON ST_DISTANCE(e.geo, ST_MAKEPOINT(s.lon, s.lat)) <= 
      CASE 
        WHEN s.radius_unit = 'mi' THEN s.radius * 1609.34
        WHEN s.radius_unit = 'km' THEN s.radius * 1000
      END
    AND TO_DATE(CONVERT_TIMEZONE(CASE WHEN e.timezone IS NOT NULL THEN e.timezone ELSE 'UTC' END, e.event_start)) <= s.date
    AND TO_DATE(CONVERT_TIMEZONE(CASE WHEN e.timezone IS NOT NULL THEN e.timezone ELSE 'UTC' END, e.event_end)) >= s.date
  WHERE e.phq_rank IS NOT NULL
    AND e.category in ('academic','public-holidays','school-holidays','observances')
 ),
 events_ranked_distinct AS (        --Get count per rank level
   SELECT 
     r.date,
     r.location,
     r.category,
     r.academic_split,
     r.rank_level,
     count(DISTINCT r.event_id) AS distinct_event_count
   FROM events_ranked r
   GROUP BY
     r.date,
     r.location,
     r.category,
     r.academic_split,
     r.rank_level
)
SELECT                             --Final formatting and select for phq_rank_features
  data_range.date,
  data_range.location,
  SUM(CASE WHEN r.category = 'observances' AND r.rank_level = 1 THEN r.distinct_event_count ELSE 0 END)  AS phq_rank_observances_rank_level1,
  SUM(CASE WHEN r.category = 'observances' AND r.rank_level = 2 THEN r.distinct_event_count ELSE 0 END)  AS phq_rank_observances_rank_level2,
  SUM(CASE WHEN r.category = 'observances' AND r.rank_level = 3 THEN r.distinct_event_count ELSE 0 END)  AS phq_rank_observances_rank_level3,
  SUM(CASE WHEN r.category = 'observances' AND r.rank_level = 4 THEN r.distinct_event_count ELSE 0 END)  AS phq_rank_observances_rank_level4,
  SUM(CASE WHEN r.category = 'observances' AND r.rank_level = 5 THEN r.distinct_event_count ELSE 0 END)  AS phq_rank_observances_rank_level5,                                   
  SUM(CASE WHEN r.category = 'public-holidays' AND r.rank_level = 1 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_public_holidays_rank_level1,
  SUM(CASE WHEN r.category = 'public-holidays' AND r.rank_level = 2 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_public_holidays_rank_level2,
  SUM(CASE WHEN r.category = 'public-holidays' AND r.rank_level = 3 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_public_holidays_rank_level3,
  SUM(CASE WHEN r.category = 'public-holidays' AND r.rank_level = 4 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_public_holidays_rank_level4,
  SUM(CASE WHEN r.category = 'public-holidays' AND r.rank_level = 5 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_public_holidays_rank_level5,      
  SUM(CASE WHEN r.category = 'school-holidays' AND r.rank_level = 1 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_school_holidays_rank_level1,
  SUM(CASE WHEN r.category = 'school-holidays' AND r.rank_level = 2 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_school_holidays_rank_level2,
  SUM(CASE WHEN r.category = 'school-holidays' AND r.rank_level = 3 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_school_holidays_rank_level3,
  SUM(CASE WHEN r.category = 'school-holidays' AND r.rank_level = 4 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_school_holidays_rank_level4,
  SUM(CASE WHEN r.category = 'school-holidays' AND r.rank_level = 5 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_school_holidays_rank_level5,                                   
  SUM(CASE WHEN r.academic_split = 'session' AND r.rank_level = 1 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_session_rank_level1,
  SUM(CASE WHEN r.academic_split = 'session' AND r.rank_level = 2 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_session_rank_level2,
  SUM(CASE WHEN r.academic_split = 'session' AND r.rank_level = 3 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_session_rank_level3,
  SUM(CASE WHEN r.academic_split = 'session' AND r.rank_level = 4 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_session_rank_level4,
  SUM(CASE WHEN r.academic_split = 'session' AND r.rank_level = 5 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_session_rank_level5,
  SUM(CASE WHEN r.academic_split = 'exam' AND r.rank_level = 1 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_exam_rank_level1,
  SUM(CASE WHEN r.academic_split = 'exam' AND r.rank_level = 2 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_exam_rank_level2,
  SUM(CASE WHEN r.academic_split = 'exam' AND r.rank_level = 3 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_exam_rank_level3,
  SUM(CASE WHEN r.academic_split = 'exam' AND r.rank_level = 4 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_exam_rank_level4,
  SUM(CASE WHEN r.academic_split = 'exam' AND r.rank_level = 5 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_exam_rank_level5,
  SUM(CASE WHEN r.academic_split = 'holiday' AND r.rank_level = 1 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_holiday_rank_level1,
  SUM(CASE WHEN r.academic_split = 'holiday' AND r.rank_level = 2 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_holiday_rank_level2,
  SUM(CASE WHEN r.academic_split = 'holiday' AND r.rank_level = 3 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_holiday_rank_level3,
  SUM(CASE WHEN r.academic_split = 'holiday' AND r.rank_level = 4 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_holiday_rank_level4,
  SUM(CASE WHEN r.academic_split = 'holiday' AND r.rank_level = 5 THEN r.distinct_event_count ELSE 0 END) AS phq_rank_academic_holiday_rank_level5                                        
FROM (SELECT date, location FROM saved_locations_daily) data_range
LEFT JOIN events_ranked_distinct r
    ON data_range.date = r.date
        AND data_range.location = r.location
GROUP BY data_range.date, data_range.location
ORDER BY data_range.date, data_range.location
;

SELECT * FROM phq_rank_features order by location, date;

```
{% endcode %}

### PHQ Impact Features

Values are calculated as MAX of the Ranks of events occurring over each day, showing the highest rank Severe Weather event of each type occurring per day.

{% code title="PHQ Impact Features" fullWidth="true" %}
```sql
----PHQ Impact Features
CREATE OR REPLACE TEMP TABLE phq_impact_features as 
WITH events_impact AS (             --Pull impact events within range
  SELECT DISTINCT
    e.event_id,
    imp.value:date_local::DATE AS date,
    s.location,
    e.category,
    imp.value:value::int AS phq_rank,
    CASE 
        WHEN ARRAY_CONTAINS('blizzard'::variant, e.labels) THEN 'blizzard'
        WHEN ARRAY_CONTAINS('snow'::variant, e.labels) THEN 'cold-wave-snow'
        WHEN ARRAY_CONTAINS('cold-wave'::variant, e.labels) AND ARRAY_CONTAINS('storm'::variant, e.labels) THEN 'cold-wave-storm'
        WHEN ARRAY_CONTAINS('cold-wave'::variant, e.labels) THEN 'cold-wave'
        WHEN ARRAY_CONTAINS('air-quality'::variant, e.labels) OR ARRAY_CONTAINS('fog'::variant, e.labels) OR ARRAY_CONTAINS('sand'::variant, e.labels) THEN 'air-quality'
        WHEN ARRAY_CONTAINS('thunderstorm'::variant, e.labels) THEN 'thunderstorm'
        WHEN ARRAY_CONTAINS('tropical-storm'::variant, e.labels) THEN 'tropical-storm'
        WHEN ARRAY_CONTAINS('tornado'::variant, e.labels) THEN 'tornado'
        WHEN ARRAY_CONTAINS('hurricane'::variant, e.labels) OR ARRAY_CONTAINS('cyclone'::variant, e.labels) OR ARRAY_CONTAINS('typhoon'::variant, e.labels) THEN 'hurricane'
        WHEN ARRAY_CONTAINS('dust'::variant, e.labels) AND ARRAY_CONTAINS('storm'::variant, e.labels) THEN 'dust-storm'
        WHEN ARRAY_CONTAINS('dust'::variant, e.labels) THEN 'dust'
        WHEN ARRAY_CONTAINS('rain'::variant, e.labels) OR  ARRAY_CONTAINS('flood'::variant, e.labels) OR ARRAY_CONTAINS('rain'::variant, e.labels) THEN 'flood'
        WHEN ARRAY_CONTAINS('heat-wave'::variant, e.labels) THEN 'heat-wave'
        WHEN ARRAY_CONTAINS('wind'::variant, e.labels) OR  ARRAY_CONTAINS('hazardous-surf'::variant, e.labels) OR ARRAY_CONTAINS('storm'::variant, e.labels) THEN 'dust-storm'
    END AS weather_category
  FROM predicthq.events_0 e
  RIGHT JOIN saved_locations_daily s
    ON ST_DISTANCE(e.geo, ST_MAKEPOINT(s.lon, s.lat)) <= 
      CASE 
        WHEN s.radius_unit = 'mi' THEN s.radius * 1609.34   
        WHEN s.radius_unit = 'km' THEN s.radius * 1000
      END
    AND TO_DATE(CONVERT_TIMEZONE(CASE WHEN e.timezone IS NOT NULL THEN e.timezone ELSE 'UTC' END, e.event_start)) <= s.date
    AND TO_DATE(CONVERT_TIMEZONE(CASE WHEN e.timezone IS NOT NULL THEN e.timezone ELSE 'UTC' END, e.event_end)) >= s.date,
  latERAL FlatTEN(INPUT => IMPACT_PATTERNS) vert,
  latERAL FlatTEN(INPUT => vert.value:impacts) imp
  WHERE vert.value:vertical::STRING = 'retail' 
    AND e.category = 'severe-weather'
    AND weather_category IS NOT NULL
 )
SELECT                          --final formatting and select for phq_impact_features
  data_range.date,
  data_range.location,
  IFNULL(MAX(CASE WHEN i.weather_category = 'air-quality' THEN i.phq_rank ELSE NULL END),0) AS phq_impact_severe_weather_air_quality_retail,
  IFNULL(MAX(CASE WHEN i.weather_category = 'blizzard' THEN i.phq_rank ELSE NULL END),0) AS phq_impact_severe_weather_blizzard_retail,
  IFNULL(MAX(CASE WHEN i.weather_category = 'cold-wave' THEN i.phq_rank ELSE NULL END),0) AS phq_impact_severe_weather_cold_wave_retail,
  IFNULL(MAX(CASE WHEN i.weather_category = 'cold-wave-snow' THEN i.phq_rank ELSE NULL END),0) AS phq_impact_severe_weather_cold_wave_snow_retail,
  IFNULL(MAX(CASE WHEN i.weather_category = 'cold-wave-storm' THEN i.phq_rank ELSE NULL END),0) AS phq_impact_severe_weather_cold_wave_storm_retail,
  IFNULL(MAX(CASE WHEN i.weather_category = 'dust' THEN i.phq_rank ELSE NULL END),0) AS phq_impact_severe_weather_dust_retail,
  IFNULL(MAX(CASE WHEN i.weather_category = 'dust-storm' THEN i.phq_rank ELSE NULL END),0) AS phq_impact_severe_weather_dust_storm_retail,
  IFNULL(MAX(CASE WHEN i.weather_category = 'flood' THEN i.phq_rank ELSE NULL END),0) AS phq_impact_severe_weather_flood_retail,
  IFNULL(MAX(CASE WHEN i.weather_category = 'heat-wave' THEN i.phq_rank ELSE NULL END),0) AS phq_impact_severe_weather_heat_wave_retail,
  IFNULL(MAX(CASE WHEN i.weather_category = 'hurricane' THEN i.phq_rank ELSE NULL END),0) AS phq_impact_severe_weather_hurricane_retail,
  IFNULL(MAX(CASE WHEN i.weather_category = 'thunderstorm' THEN i.phq_rank ELSE NULL END),0) AS phq_impact_severe_weather_thunderstorm_retail,
  IFNULL(MAX(CASE WHEN i.weather_category = 'tornado' THEN i.phq_rank ELSE NULL END),0) AS phq_impact_severe_weather_tornado_retail,
  IFNULL(MAX(CASE WHEN i.weather_category = 'tropical-storm' THEN i.phq_rank ELSE NULL END),0) AS phq_impact_severe_weather_tropical_storm_retail 
FROM (SELECT date, location FROM saved_locations_daily) data_range
LEFT JOIN events_impact i
    ON data_range.date = i.date
        AND data_range.location = i.location
GROUP BY data_range.date, data_range.location
ORDER BY data_range.date, data_range.location
;


SELECT * FROM phq_impact_features order by location, date;
```
{% endcode %}

If metrics other than MAX are desired, use the below code as a template for each column. The weather\_category name part of the code (in these examples defaulted to ‘air-quality’) will need to be replaced depending on which feature is intended to be called. Refer to the column code above for the available weather\_category features.

{% code title="Count" fullWidth="true" %}
```sql
COUNT(CASE WHEN i.weather_category = 'air-quality' THEN i.phq_rank ELSE NULL END)
```
{% endcode %}

{% code title="Average" fullWidth="true" %}
```sql
IFNULL(ROUND(AVG(CASE WHEN i.weather_category = 'air-quality' THEN i.phq_rank ELSE NULL END),2),0)
```
{% endcode %}

{% code title="Median" fullWidth="true" %}
```sql
IFNULL(ROUND(MEDIAN(CASE WHEN i.weather_category = 'air-quality' THEN i.phq_rank ELSE NULL END),2),0)
```
{% endcode %}

{% code title="Standard Deviation" fullWidth="true" %}
```sql
IFNULL(ROUND(STDDEV(CASE WHEN i.weather_category = 'air-quality' THEN i.phq_rank ELSE NULL END),2),0)
```
{% endcode %}

{% code title="Min" fullWidth="true" %}
```sql
IFNULL(MIN(CASE WHEN i.weather_category = 'air-quality' THEN i.phq_rank ELSE NULL END),0)
```
{% endcode %}

{% code title="SUM" fullWidth="true" %}
```sql
SUM(CASE WHEN i.weather_category = 'air-quality' THEN i.phq_rank ELSE 0 END)
```
{% endcode %}

## Step 3: Final Select for all Features

The following code will pull features generated above all into a single table called **ML\_FEATURES\_FOR\_LOCATIONS**.\
\
This output is intended to be used directly by Machine Learning models. If unsure what features to use, it is recommended to create a Beam analysis for the locations and leverage the category importance results with the “View ML Features” option ([see here](broken-reference)).

{% code title="Combined Table" fullWidth="true" %}
```sql
----Combine Select for viewing all in one
CREATE OR REPLACE TEMP TABLE ml_features_for_locations AS
SELECT 
  a.date, 
  a.location,
  a.phq_attendance_community,       --Attendance columns
  a.phq_attendance_concerts,
  a.phq_attendance_conferences,
  a.phq_attendance_expos,
  a.phq_attendance_festivals,
  a.phq_attendance_performing_arts,
  a.phq_attendance_sports,
  a.phq_attendance_school_holidays,
  a.phq_attendance_academic_graduation,
  a.phq_attendance_academic_social,
  r.phq_rank_observances_rank_level1,   --Rank Level columns
  r.phq_rank_observances_rank_level2,
  r.phq_rank_observances_rank_level3,
  r.phq_rank_observances_rank_level4,
  r.phq_rank_observances_rank_level5,
  r.phq_rank_public_holidays_rank_level1,
  r.phq_rank_public_holidays_rank_level2,
  r.phq_rank_public_holidays_rank_level3,
  r.phq_rank_public_holidays_rank_level4,
  r.phq_rank_school_holidays_rank_level5,
  r.phq_rank_academic_session_rank_level1,
  r.phq_rank_academic_session_rank_level2,
  r.phq_rank_academic_session_rank_level3,
  r.phq_rank_academic_session_rank_level4,
  r.phq_rank_academic_session_rank_level5,
  r.phq_rank_academic_exam_rank_level1,
  r.phq_rank_academic_exam_rank_level2,
  r.phq_rank_academic_exam_rank_level3,
  r.phq_rank_academic_exam_rank_level4,
  r.phq_rank_academic_exam_rank_level5,
  r.phq_rank_academic_holiday_rank_level1,
  r.phq_rank_academic_holiday_rank_level2,
  r.phq_rank_academic_holiday_rank_level3,
  r.phq_rank_academic_holiday_rank_level4,
  r.phq_rank_academic_holiday_rank_level5,
  i.phq_impact_severe_weather_air_quality_retail,   --Impact columns
  i.phq_impact_severe_weather_blizzard_retail,
  i.phq_impact_severe_weather_cold_wave_retail,
  i.phq_impact_severe_weather_cold_wave_snow_retail,
  i.phq_impact_severe_weather_cold_wave_storm_retail,
  i.phq_impact_severe_weather_dust_retail,
  i.phq_impact_severe_weather_dust_storm_retail,
  i.phq_impact_severe_weather_flood_retail,
  i.phq_impact_severe_weather_heat_wave_retail,
  i.phq_impact_severe_weather_hurricane_retail,
  i.phq_impact_severe_weather_thunderstorm_retail,
  i.phq_impact_severe_weather_tornado_retail,
  i.phq_impact_severe_weather_tropical_storm_retail
FROM phq_attendance_features a
JOIN phq_rank_features r
    ON a.date = r.date
        AND a.location = r.location
JOIN phq_impact_features i
    ON a.date = i.date
        AND a.location = i.location
;

SELECT * FROM ml_features_for_locations ORDER BY location, date;
```
{% endcode %}

The output table should look like this (Note: the below example is only showing the first 3 columns):

<table data-full-width="true"><thead><tr><th width="141">DATE</th><th width="119">LOCATION</th><th>PHQ_ATTENDANCE_COMMUNITY</th><th>PHQ_ATTENDANCE_CONCERTS</th><th>PHQ_ATTENDANCE_CONFERENCES</th></tr></thead><tbody><tr><td>2024-01-01</td><td>Hyde Park</td><td>68</td><td>1,839</td><td>1,578</td></tr><tr><td>2024-01-02</td><td>Hyde Park</td><td>0</td><td>469</td><td>126</td></tr><tr><td>2024-01-03</td><td>Hyde Park</td><td>200</td><td>346</td><td>139</td></tr><tr><td>2024-01-04</td><td>Hyde Park</td><td>0</td><td>2,029</td><td>324</td></tr><tr><td>2024-01-05</td><td>Hyde Park</td><td>120</td><td>691</td><td>238</td></tr></tbody></table>

### Refer Back to [Main Guide](./)
