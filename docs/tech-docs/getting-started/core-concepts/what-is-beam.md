# What is Beam?

Beam is PredictHQ’s relevancy engine. It analyzes your historical demand data to identify which types of real-world events actually influence your business - per location. Different places respond differently to the same event types, and Beam helps you account for that.

By uncovering which event types (like Concerts, Expos, or Conferences etc) matter most for each location, Beam becomes a data-driven filter for your forecasting models, operational dashboards, and alerting systems. It cuts through irrelevant noise so you can focus only on the events that consistently move the needle.

Beam is available via both [API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam) and the PredictHQ WebApp, so you can explore results manually or automate it in your pipeline.

## Why Use Beam

Most customers integrate event data to improve demand forecasting, staffing, or pricing - but the biggest risk is using the wrong features or too many features. That leads to poor model performance, noise in dashboards, and wasted effort.

**Beam exists to prevent that**. It tells you which event types actually matter for your business, in each location or segment, based on your historical demand. You get a data-backed filter that helps you:

* Select high-signal features for forecasting and ML models
* Remove irrelevant events from operational tooling or alerting
* Tailor event selection per location, brand, or business unit
* Save months of dev time by skipping guesswork and heuristics

Beam isn’t optional - it’s how you get relevant results from PredictHQ. Without it, you risk integrating a lot of event data that adds noise instead of value.

## How It Works

Beam explains why your demand changed by identifying which event signals correlate with those changes - location by location.

Here’s the high-level flow:

1. You provide historical demand data (e.g. bookings, foot traffic, revenue) for one or more locations.
2. Beam decomposes your time series, isolating trend, seasonality, and residual (unexplained) variation.
3. It correlates those residuals with PredictHQ event features, using grouped attributes like event categories (e.g. Concerts, Sports).
4. It outputs a ranked list of features that historically impacted demand.

Beam uses this process to surface only the event features that matter. These can then be used to:

* Select relevant features for your forecasting model
* Filter or prioritize events for dashboards and alerts
* Compare importance across locations or brands

## Inputs and Outputs

### Inputs

To run Beam, you’ll need:

* Historical demand data
  * Format: aggregated daily or weekly values per location (e.g. bookings, revenue, visits)
  * Minimum recommended: 6-12 months of data per location
  * Required fields: date, demand
* Saved Location
  * Beam uses location context (lat/lon, polygon, address, etc.) to fetch relevant event features
  * Each Beam Analysis must be tied to a Saved Location (you can optionally use Beam without a Saved Location for a simple lat/lon and radius but for ease of use we strongly recommend using Saved Locations).
  * Suggested Radius - use our data-driven approach to determine the ideal area around your location.

If you don’t have demand data available, Beam can still provide insights based on similar businesses in your industry - but these are less accurate.

### Outputs

Beam returns:

* Feature Importance rankings
  * Ranked list of the most relevant features grouped into types (e.g. Concerts, Sports, Conferences).
  * Includes p-value score per feature group.
* Beam Analysis ID
  * Can be used with Features API or Events API to automatically filter to relevant features/categories for the same location.

## Best Practices

* Use Beam before building your forecasts - Don’t guess which event features to include. Run Beam first to identify the high-impact event types for each location or segment - then feed only those into your forecasting models.
* Segment by location or product group - Event impact varies by context, but going too granular (e.g. individual SKUs or store-level micro-segments) can introduce noise. We’ve found the best results come from grouping by:
  * Location
  * Brand or concept (e.g. premium vs budget)
  * Product group level (e.g. room types, product categories) - rather than individual SKUs
* Use Beam Analysis IDs to filter other APIs - Once Beam has identified the relevant features, use the beam.analysis\_id to:
  * Filter Features API results automatically
  * Filter Events API by relevant categories
* Re-run Beam at least monthly - Event dynamics shift over time - new venues open, seasonality changes, and different event types rise or fall in importance. We recommend re-running Beam at least once a month

## How Beam Powers Other APIs

Beam isn’t just a one-off analysis - it directly enhances how you use other PredictHQ APIs by making your queries smarter and more relevant.

### Features API

Use the beam.analysis\_id in your Features API request to:

* Automatically apply the Feature Importance results from Beam
* Filter down to the most relevant features (e.g. specific categories, rank thresholds, attendance ranges)
* Match the analysis location automatically using the Beam-associated Saved Location

This ensures you only pull in the event signals that actually impact your business.

### Events API

Use the beam.analysis\_id parameter to filter for events relevant to your business, based on your Beam Analysis. When included:

* The API automatically applies the location, rank, and category filters from the Beam Analysis
* If the analysis was run on a group of locations, you can optionally include beam.group\_id as well

This is the most reliable way to reduce noise and retrieve only the events that matter - without hand-tuning filters manually.

### Forecasts API

The Forecasts API uses Beam behind the scenes:

* When you submit historical demand data, Beam runs automatically to calculate Feature Importance
* Forecasts then use the most relevant event features - via the Features API - based on that Beam output

This keeps the forecasting process aligned with your actual demand drivers, without needing to configure feature selection manually.

## Common Pitfalls

* Skipping Beam entirely - Leads to irrelevant features, noisy data, and poor model performance.
* Using all event categories “just in case” - More features often means more noise. Beam helps you focus on what actually matters.
* Reusing one Beam analysis across all locations - Event impact is location-specific—what works in one place won’t work everywhere.

## Related

* [Beam API Reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam)
* [Features API Reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) (Beam uses this under the hood)
* [Forecasts API Reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts) (Forecasts uses Beam under the hood)
* [Beam Guides](../guides/beam-guides/)

## What to Do Next

Once Beam has identified the relevant event features for your locations, use the Beam Analysis ID to filter your Features API and Events API queries - or let Forecasts API apply it automatically.
