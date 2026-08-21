# What is the Features API?

The Features API transforms real-world events into structured time-series signals for forecasting, analytics, and other time-dependent models.

Instead of returning individual event records, it produces daily or weekly numerical aggregates grouped by event type (e.g. Concerts, Sports, Public Holidays). Aggregations incorporate predicted attendance, impact patterns, spend estimates, and ranking metrics.

Outputs are deterministic, time-aligned feature series scoped to a specific location and date range.

{% hint style="success" %}
**Why use the Features API?**\
We've built up years of expertise in transforming real-world events into meaningful demand signals. Across industries, we’ve consistently seen that naïve aggregation produces noise rather than uplift. The Features API encapsulates that experience - delivering proven, engineered signals that improve forecast accuracy without the heavy lifting.
{% endhint %}

## Why the Features API Exists

Individual events are not directly usable in forecasting models.

Correlating demand against individual events also runs into sparsity: a single event's spike rarely gives enough data points to prove anything. Aggregating by category at a daily level gives models the volume of observations that correlation requires.

Events vary in duration, scale, timing, and expected impact. Multi-day events introduce lead and lag effects. Attendance and spend signals must be aggregated consistently. Overlapping events must be handled without distortion.

Naïve aggregation often introduces noise.

The Features API standardizes how event data is transformed into numerical demand indicators. It encapsulates handling of:

* Multi-day event duration
* Lead and lag impact patterns
* Attendance and spend aggregation
* Rank-based filtering
* Category-level grouping

This replaces bespoke event feature engineering pipelines with consistent API outputs.

## What the Features API Does

The Features API:

* Aggregates event metrics by category and date
* Distributes attendance across multi-day spans
* Applies temporal impact patterns
* Supports rank-based and attendance-based filtering
* Returns daily or weekly feature values

For example, on a single future day in Sydney, a major sports game, a street fair, a film festival, and an orchestra performance might combine to an aggregate predicted attendance of 150,000 across a hundred or more events - returned as one model-ready number per category, per day.

It does not determine which features are relevant to your business. Relevance calibration is handled by Beam. The Features API focuses on transforming scoped events into structured numerical signals.

## How It Works With Beam

Using a `beam.analysis_id` is the most reliable way to configure the Features API.

When provided, the API:

* Uses the associated Saved Location
* Applies demand-calibrated feature selection
* Enforces category and rank filters derived from Beam

Without Beam, feature configuration must be defined manually.

## Inputs and Outputs

### Inputs

The easiest and most reliable way to use the Features API is by providing a `beam.analysis_id`. This automatically applies:

* The correct location and timezone
* A precomputed set of relevant features (from Beam Feature Importance)
* Optimal rank and category filters

Using a `beam.analysis_id` removes the need to manually define your location and feature configuration - it ensures you’re only using features that matter.

If you’re not using Beam, you can also configure inputs manually:

* Location
  * Provide a `saved_location_id` (recommended), `place_id` or geolocation + radius.
* Time range
  * Start and end date, aligned to local timezone.
* Features to compute
  * Choose from the full list of available features.
  * Some features have industry-specific variants that use your industry’s Predicted Impact Patterns to better reflect lead/lag behavior.
* Stat types (per feature)
  * For each feature, choose which statistics to compute.
* Granularity
  * Day or week intervals
* Optional filters
  * Filter events included in each feature using `phq_rank` or `local_rank`.

### Outputs

The Features API returns a time series of feature values for each date (or week) in your request, aligned to the timezone of the location.

Each feature includes statistics or level counts depending on the field, in JSON (best for programmatic use) or CSV (best for spreadsheets and BI tools). Both formats are designed for downstream use with no extra post-processing. For the exact field structure, column-naming pattern, and available stats, see the [Features API reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features).

## Best Practices

To get the most value from the Features API and avoid noisy or misleading results, follow these practices:

* Use a `beam.analysis_id` whenever possible - This ensures you’re using only features that have proven impact on your business, and saves time configuring filters manually.
* Use `saved_location_id` to define locations - Saved Locations are the most robust way to reference geographies in PredictHQ. They allow consistent use across Beam, Features API, Events API, and Forecasts API.
* Use Predicted Impact Area to define location scope - Predicted Impact Area provides an industry and location-specific boundary calibrated against real demand and event data. The recommended approach is to create a Saved Location using `origin_geojson`, which automatically calculates and stores the impact area - you can then reference it by `location_id` without managing the boundary yourself.
* Segment by meaningful business unit or location - You’ll get the best results when your Beam Analysis and/or Features API requests are scoped to consistent demand signals e.g. a single store, hotel, area, or a product grouping. Avoid going too small (e.g. individual SKUs) or too large (e.g. entire countries or multi-state regions), as the Features API is not designed for large or fragmented geographies.
* Choose the right granularity for your model - Daily granularity works well for high-frequency decisions like staffing or delivery. Weekly works better when individual day fluctuations are less meaningful.
* Filter by event impact - Use thresholds on `phq_rank` or `local_rank` to avoid cluttering your signals with low-impact events.
* Re-run Beam regularly - Event-driven demand patterns shift. We recommend re-running Beam monthly to keep your Feature Importance results fresh and relevant.

## Common Pitfalls

* **Requesting too many features** - Pulling every available feature increases noise and reduces model performance. Use Beam or a curated set of relevant features.
* **Skipping Predicted Impact Area** - Manually defined boundaries often miss key events or include irrelevant ones. Use Predicted Impact Area for each location and industry, ideally via Saved Locations.
* **Too broad or too narrow location scopes** - Very large areas (e.g. states, countries) or very small units (e.g. SKUs) dilute signal. Use Features API for city/suburb/store-scale use cases.

## Related

* [Features API Reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features)
* [What Is Beam?](what-is-beam.md)
* [Features API Guides](../guides/features-api-guides/)

## What to Do Next

* [Run Beam](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam) (if you haven’t already) - Identify which event features actually drive demand for your business. This gives you a focused feature set to use with the Features API.
* Set up [Predicted Impact Area](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/impact-area/get-impact-area) - Define the optimal impact boundary for your location and industry. The easiest way is via [Saved Locations](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/saved-locations/create-a-saved-location), which calculates and stores it automatically.
* Set up [Saved Locations](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/saved-locations) - Define your key business locations once and reuse them across PredictHQ APIs for consistency and easier re-analysis.
* Make your first [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) request - Use your beam.analysis\_id or saved\_location\_id to pull a clean time series of impactful event features for your model.
* See how it fits together in production - The [Standard Integration Pattern](../../integrations/integration-guides/standard-integration-pattern.md) shows how Saved Locations, Beam, the Features API, and the Events API connect as a pipeline, with the right refresh cadence and data storage patterns.
* Need help? - Check out [Features API Guides](../guides/features-api-guides/) or contact support for help tuning your request.
