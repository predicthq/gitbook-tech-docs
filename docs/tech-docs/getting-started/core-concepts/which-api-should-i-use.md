# Which API Should I Use?

PredictHQ has four core APIs. Choosing the right one for each task is the most important decision in any integration - using the wrong API is the most common source of unnecessary complexity and poor results.

## The Short Answer

| Goal                                                  | API                                                                                                          |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Train or improve a demand forecasting model           | [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) with `beam.analysis_id` |
| Get event-driven forecasts without building a model   | [Forecasts API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts/overview)                           |
| Understand which events are driving demand            | [Events API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events) with `beam.analysis_id`    |
| Augment an existing forecast with event-aware outputs | [Forecasts API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts/overview)                           |
| Build a dashboard showing upcoming events             | [Events API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events)                            |
| Explain a forecast spike to a stakeholder             | [Events API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events)                            |
| Identify which event types drive demand at a location | [Beam API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/overview)                                     |

## Features API - for forecasting and ML

Use the Features API when you are building or improving a demand forecasting model, integrating event signals into an ML pipeline, or generating event-driven inputs for staffing, pricing, or inventory decisions.

The Features API produces pre-engineered, attendance-weighted, duration-adjusted, impact-pattern-aware time-series signals. It encapsulates years of domain expertise in transforming raw event data into reliable demand signals. Do not attempt to replicate this by querying the Events API and aggregating manually - naive aggregation introduces noise and degrades model performance.

**Always use `beam.analysis_id`** when calling the Features API. Without it, feature selection must be configured manually - which is error-prone and produces worse results. Run Beam first, then pass the `analysis_id` to the Features API.

{% hint style="warning" %}
The Events API is not a substitute for the Features API in forecasting pipelines. Looping over events, counting them per day, and using that count as a model feature is a common mistake that degrades forecast accuracy.
{% endhint %}

* [Features API Reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features)
* [What is the Features API?](what-is-the-features-api.md)

## Forecasts API - for ready-to-use event-driven forecasts

Use the Forecasts API when you want accurate, event-driven demand forecasts without building and maintaining your own forecasting model, or when rapid time-to-value is the priority.

The Forecasts API accepts your historical demand data, trains a model, and returns daily-level forecasts with event impact built directly into the output. Beam is applied automatically - there is no need to configure feature selection manually. A baseline comparison metric is included so you can measure the MAPE improvement attributable to PredictHQ data.

The Forecasts API is appropriate whether you are starting from scratch or augmenting an existing forecast. Use it when reducing development time and complexity matters more than owning the underlying model. For teams that require full control over model architecture and feature engineering, the Features API is the recommended alternative.

* [Forecasts API Reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts/overview)
* [Getting Started with Forecasts API](../guides/forecasts-api-guides/getting-started.md)

## Events API - for discovery and explainability

Use the Events API when a user or system needs to see specific individual events - for explainability, dashboards, operational context, or event discovery.

The Events API is for understanding what is happening and why demand shifted on a given day. It is the right tool for surfacing event context alongside forecast results, drilling into which events drove a demand spike, or building an interface that lets operators see upcoming events at their locations.

Use the Events API with `beam.analysis_id` to automatically filter results to the event categories and rank thresholds that are relevant for a given location — the same calibration applied by the Features API.

The Events API is not designed for generating model inputs. Do not loop over events, count them per day, and use those counts as features.

* [Events API Reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events)

## Beam - for demand calibration

Beam is not a data retrieval API - it is a demand calibration engine that tells you which event types drive demand at each of your locations.

Run Beam before building forecasts or configuring the Features API. The `analysis_id` Beam produces is the key input to both the Features API and Events API, automatically applying the correct location boundary, event category filters, and rank thresholds.

Beam should be run once per location and refreshed monthly. It is required for any integration that uses the Features API.

* [Beam API Reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/overview)
* [What is Beam?](what-is-beam.md)

## Common Mistakes

* **Using the Events API for ML features** - The Events API returns individual event records. Aggregating these manually introduces errors in multi-day event handling, lead/lag effects, and rank filtering. Use the Features API instead.
* **Skipping Beam** - Without Beam, feature selection in the Features API must be configured manually. This is error-prone and produces feature sets that are not calibrated to your actual demand patterns.
* **Calling Features API without `beam.analysis_id`** - Without a Beam analysis, you must manually specify location, features, and rank thresholds. This is valid for early exploration but should not be used in production.

## See Also

* [Standard Integration Pattern](../../integrations/integration-guides/standard-integration-pattern.md) - how all four APIs fit together in a production architecture
* [API Quickstart](../api-quickstart.md) - make your first API call
* [Glossary](../glossary.md) - definitions for all core concepts
