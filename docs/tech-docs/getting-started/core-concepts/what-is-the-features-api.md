# What is the Features API?

The Features API generates time-series signals from real-world events - structured for use in forecasting and other time-series models. It returns clean, numerical features like predicted attendance, impact scores, and spend estimates for your chosen locations and time range. These features are designed to help you quantify the potential impact of events on your business activity.

Rather than returning raw event data, the Features API provides daily or weekly metrics grouped by event type (e.g. Concerts, Sports, Public Holidays). It accounts for important factors like multi-day events, expected attendance, and lead/lag effects using PredictHQ’s intelligence, including PHQ Rank, Local Rank, Umbrella Events and Impact Patterns.

Instead of building your own event aggregation pipeline, you get structured, configurable features ready for modeling, analysis, or planning.

You can:

* Pick the metrics you need (e.g. `sum`, `count`, `avg`, `std_dev`)
* Filter by impact (e.g. `phq_rank` or `local_rank`)
* Use industry-specific features for improved accuracy
* Output results in JSON or CSV, daily or weekly

## Why Use the Features API

If you’re already using the Events API, you have access to rich, structured event data. But turning that into useful, time-aligned, numerical features for modeling is a separate challenge.

The Features API handles that for you.

It takes care of:

* Distributing Predicted Attendance across multi-day events
* Modeling leading and lagging demand effects using Predicted Impact Patterns
* Aggregating metrics (e.g. attendance, spend, event counts) by event type and date
* Filtering by relevance using rank or attendance thresholds

Use the Features API when you want to:

* Add structured event signals to forecasting, or other models
* Create demand indicators for dashboards or alerts
* Standardize feature generation across locations or markets
* Reduce time spent on feature engineering and event bucketing

You stay in control - choose the metric types, filters, and output format. Pair it with Beam to focus only on event features that matter.

The Features API saves your team time and removes guesswork so you can focus on improving model performance, not preprocessing.

## Inputs and Outputs

### Inputs

The easiest and most reliable way to use the Features API is by providing a beam.analysis\_id. This automatically applies:

* The correct location and timezone
* A precomputed set of relevant features (from Beam Feature Importance)
* Optimal rank and category filters

Using a `beam.analysis_id` removes the need to manually define your location and feature configuration - it ensures you’re only using features that matter.

If you’re not using Beam, you can also configure inputs manually:

* Location
  * Provide a saved\_location\_id (recommended), place\_id or geolocation + radius.
* Time range
  * Start and end date, aligned to local timezone.
* Features to compute
  * Choose from the full list of available features.
  * Some features have industry-specific variants that use your industry’s Predicted Impact Patterns to better reflect lead/lag behavior.
* Stat types (per feature)
  * For each feature, choose one or more stat types: sum, avg, count, std\_dev, min, max.
* Granularity
  * Day or week intervals
* Optional filters
  * Filter events included in each feature using phq\_rank or local\_rank.

### Outputs

The Features API returns a time series of feature values for each date (or week) in your request, aligned to the timezone of the location.

Each feature includes statistics (e.g. sum, avg, std\_dev) or level counts (e.g. for phq\_rank), depending on the field. The output is consistent across formats.

#### Output Formats

**JSON (default)**

* Best for programmatic use.
* Feature fields are nested by `<feature_name>` with their corresponding stats or rank\_levels.

Example:

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
    ...
  ]
}
```

**CSV**

* Best for spreadsheets or BI tools
* One row per date, one column per stat-level feature
* Column names use this pattern: `<feature_name>_stats_<stat>` or `<feature_name>_rank_levels_<rank_level>`

Example:

```csv
date,phq_attendance_concerts_stats_count,phq_attendance_concerts_stats_sum,phq_attendance_conferences_stats_min,phq_attendance_conferences_stats_max,phq_attendance_sports_stats_count,phq_attendance_sports_stats_sum,phq_attendance_sports_stats_min,phq_attendance_sports_stats_max,phq_attendance_sports_stats_avg,phq_attendance_sports_stats_median,phq_attendance_sports_stats_std_dev,phq_rank_public_holidays_rank_levels_1,phq_rank_public_holidays_rank_levels_2,phq_rank_public_holidays_rank_levels_3,phq_rank_public_holidays_rank_levels_4,phq_rank_public_holidays_rank_levels_5
2019-11-16,43,24546,11,1000,0,0,0,0,0.0,0.0,,0,0,0,0,0
2019-11-17,25,13440,11,146,0,0,0,0,0.0,0.0,,0,0,0,0,0
2019-11-18,6,2021,11,700,0,0,0,0,0.0,0.0,,0,0,0,0,0
2019-11-19,10,6047,11,171000,0,0,0,0,0.0,0.0,,0,0,0,0,0
```

Both formats are designed for downstream use with no extra post-processing - just plug into models, dashboards, or analysis workflows.

## Best Practices

To get the most value from the Features API and avoid noisy or misleading results, follow these practices:

* Use a `beam.analysis_id` whenever possible - This ensures you’re using only features that have proven impact on your business, and saves time configuring filters manually.
* Use `saved_location_id` to define locations - Saved Locations are the most robust way to reference geographies in PredictHQ. They allow consistent use across Beam, Features API, Events API, and Forecasts API.
* Use Suggested Radius to define location size - Suggested Radius is a data-backed, industry-specific recommendation for how far out to consider events for each location. Using this helps capture the right local context for demand-driving events - improving both feature accuracy and Beam relevance. Avoid guessing or applying the same radius everywhere.
* Segment by meaningful business unit or location - You’ll get the best results when your Beam Analysis and/or Features API requests are scoped to consistent demand signals e.g. a single store, hotel, area, or a product grouping. Avoid going too small (e.g. individual SKUs) or too large (e.g. entire countries or multi-state regions), as the Features API is not designed for large or fragmented geographies.
* Choose the right granularity for your model - Daily granularity works well for high-frequency decisions like staffing or delivery. Weekly works better when individual day fluctuations are less meaningful.
* Filter by event impact - Use thresholds on `phq_rank` or `local_rank` to avoid cluttering your signals with low-impact events.
* Re-run Beam regularly - Event-driven demand patterns shift. We recommend re-running Beam monthly to keep your Feature Importance results fresh and relevant.

## Common Pitfalls

* **Requesting too many features** - Pulling every available feature increases noise and reduces model performance. Use Beam or a curated set of relevant features.
* **Skipping Suggested Radius** - Manually guessed radii often miss key events - or include irrelevant ones. Use the Suggested Radius API for each location + industry.
* **Too broad or too narrow location scopes** - Very large areas (e.g. states, countries) or very small units (e.g. SKUs) dilute signal. Use Features API for city/suburb/store-scale use cases.

## Related

* [Features API Reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features)
* [What Is Beam?](what-is-beam.md)
* [Features API Guides](../guides/features-api-guides/)

## What to Do Next

* [Run Beam](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam) (if you haven’t already) - Identify which event features actually drive demand for your business. This gives you a focused feature set to use with the Features API.
* Use the [Suggested Radius API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/suggested-radius/get-suggested-radius) - Get the optimal event radius for your location and industry. This improves both Beam and Features API accuracy.
* Set up [Saved Locations](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/saved-locations) - Define your key business locations once and reuse them across PredictHQ APIs for consistency and easier re-analysis.
* Make your first [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) request - Use your beam.analysis\_id or saved\_location\_id to pull a clean time series of impactful event features for your model.
* Need help? - Check out [Features API Guides](../guides/features-api-guides/) or contact support for help tuning your request.
