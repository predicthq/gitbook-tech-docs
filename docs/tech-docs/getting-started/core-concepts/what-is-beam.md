# What is Beam?

Beam is PredictHQ’s relevancy engine.

It determines which types of real-world events are materially relevant to your business by analyzing your historical demand data - per location.

Event impact varies by geography, industry, and demand profile. The same event type may drive demand in one location and have little effect in another. Beam quantifies this variability and identifies which event signals consistently explain changes in your demand.

The primary output of Beam is a set of Feature Importance results that define demand-relevant event categories and signals for a specific location.

Beam is available [via API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/overview) and the PredictHQ WebApp, enabling both automated pipelines and exploratory analysis.

## Why Use Beam

Integrating event data into forecasting or operational systems introduces a structural statistical challenge.

Event-driven demand is not evenly distributed. It is sparse and heavy-tailed. A small number of events create large spikes, while others generate moderate but consistent lift. Multiple event features often activate simultaneously, representing the same underlying real-world activity. Impact varies by location, season, and demand profile.

This structure breaks many otherwise sound feature selection approaches.

Generic importance methods optimise for statistical gain. In event-driven data, rare spikes can dominate those metrics and inflate weights. When related event features activate together, importance can be split or misattributed. Moderate but real effects can be masked. Feature rankings can shift materially depending on which major events fall within a training window.

The output may appear statistically valid while becoming unstable and difficult to govern at scale.

Beam exists to address this structure.

It is purpose-built to isolate true event-driven demand impact under sparsity, overlap, and large spikes, and to produce stable, repeatable Feature Importance at the individual location level.

Building an internal pipeline requires taking ownership of this entire problem space - including decomposition, overlap handling, stability monitoring, and ongoing recalibration.

Beam provides a calibrated framework designed specifically for the statistical reality of event-driven demand.

## How It Works

Beam identifies which event signals correlate with demand variability - location by location.

High-level flow:

1. You provide historical demand data (e.g. bookings, foot traffic, revenue) for one or more locations.
2. Beam decomposes the time series to isolate residual variability beyond trend and seasonality.
3. It evaluates the relationship between that variability and PredictHQ event features, grouped by attributes such as category (e.g. Concerts, Sports, Conferences).
4. It outputs a ranked list of event feature groups that historically impacted demand.

The result is a location-specific calibration of event impact.

## Inputs and Outputs

### Inputs

To run Beam, you’ll need:

* Historical demand data
  * Aggregated daily or weekly values per location
  * Recommended: 6–12 months minimum
  * Required fields: date, demand
* Saved Location
  * Provides geographic context for event retrieval
  * When created from a lat/lon origin, Predicted Impact Area is calculated automatically and defines the geographic scope used by Beam

If historical demand data is unavailable, Beam can provide industry-based approximations. These are less precise than location-specific calibration.

### Outputs

Beam returns:

* Feature Importance rankings
  * Ranked list of the most relevant features grouped into types (e.g. Concerts, Sports, Conferences).
  * Includes statistical significance metrics
* Beam Analysis ID
  * Can be supplied to the Features API or Events API
  * Applies demand-calibrated filtering automatically

## Best Practices

* **Run Beam before building forecasts** - Identify high-impact event types first, then incorporate those signals into your models.
* **Calibrate per meaningful segment** - Impact varies by location, brand, and concept. Avoid over-fragmentation (e.g. SKU-level) unless supported by sufficient data. We’ve found the best results come from grouping by:
  * Location
  * Brand or concept (e.g. premium vs budget)
  * Product group level (e.g. room types, product categories) - rather than individual SKUs
* **Use Beam Analysis IDs across APIs** - Apply the same calibration consistently when retrieving features or events.
* **Re-run Beam regularly** - Event dynamics evolve. Monthly recalibration is recommended for most use cases.

## How Beam Integrates With Other APIs

Beam enhances other APIs by applying demand calibration to event selection.

### Features API

Use the `beam.analysis_id` in your Features API request to:

* Automatically apply Feature Importance filtering
* Filter down to the most relevant features (e.g. specific categories, rank thresholds, attendance ranges)
* Use the associated Saved Location context

This ensures model inputs reflect calibrated event impact.

### Events API

Use the `beam.analysis_id` parameter to:

* Apply category and rank filters derived from calibration
* Restrict results to demand-relevant events
* Maintain consistency with feature generation

### Forecasts API

When using the Forecasts API:

* Beam runs automatically during forecast creation
* Feature selection is based on calibrated event impact
* No manual feature filtering is required

This keeps forecast inputs aligned with historical demand drivers.

## Common Pitfalls

* **Skipping Beam entirely** - Leads to unstable feature sets and noise.
* **Including all event categories** - More features does not imply better performance.
* **Reusing one Beam analysis across dissimilar locations** - Impact varies by geography and demand profile.

## Related

* [Beam API Reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam)
* [Features API Reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) (Beam uses this under the hood)
* [Forecasts API Reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts) (Forecasts uses Beam under the hood)
* [Beam Guides](../guides/beam-guides/)

## What to Do Next

After running Beam, use the Beam Analysis ID with the Features API or Events API to retrieve demand-calibrated signals. For automated forecasting, use the Forecasts API, which applies Beam internally.
