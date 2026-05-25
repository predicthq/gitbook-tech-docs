---
description: >-
  Definitions of key terms used across PredictHQ’s platform and APIs. Use as a
  reference.
---

# Glossary

## Beam

Beam is a demand calibration engine that identifies which types of real-world events materially impact your historical demand at a specific location.

Event-driven demand is sparse and uneven. A small number of events create large spikes, while others generate moderate but consistent lift. Generic feature importance methods are not designed for this structure and can produce unstable or misleading results.

Beam analyses your historical demand time series to isolate event-driven variability and quantify which event types consistently explain it. The primary output is a set of Feature Importance results - expressed as an `analysis_id` - that automatically configures Features API and Events API calls to use only the event categories, rank thresholds, and location scope that are relevant for that location. Without Beam, feature selection is a manual guess.

Beam analyses are location-specific and should never be shared across multiple locations. Event impact varies by geography and demand profile — one analysis per location is required.

For customers operating many locations with a single shared model, Beam Analysis Groups aggregate Feature Importance results across a set of analyses to produce a consistent feature set. Use this only when a single model requires identical inputs across locations; individual per-location analyses are preferable in most cases.

Beam should be refreshed monthly by appending new demand data to the existing analysis. Do not delete and recreate analyses - doing so loses accumulated correlation history.

* API Reference: [Beam](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam "mention")
* [beam-guides](guides/beam-guides/ "mention")

## Features API

The Features API transforms real-world events into structured, model-ready time-series signals for demand forecasting and ML pipelines.

Rather than returning individual event records, it produces daily or weekly numerical aggregates grouped by event type — concerts, sports, public holidays, school holidays, and more. Aggregations incorporate predicted attendance, impact patterns, spend estimates, and ranking metrics, encapsulating the domain expertise required to turn raw event data into reliable demand signals.

The Features API is the recommended integration surface for any use case involving forecasting, ML, staffing, pricing, or inventory decisions. It should be used in place of querying the Events API and constructing features manually — naive event aggregation introduces noise and degrades model performance.

The recommended way to call the Features API is by passing a `beam.analysis_id`, which automatically applies the correct location, rank filters, and feature selection derived from Beam. Without a `beam.analysis_id`, features must be configured manually, which is error-prone and produces worse results.

* API Reference: [Get ML Features](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features "mention")
* [features-api-guides](guides/features-api-guides/ "mention")

## Forecasts API

The Forecasts API delivers event-driven demand forecasts directly, without requiring customers to build or maintain their own forecasting models.

Customers supply historical demand data for a location. The Forecasts API trains a model, applies Beam to identify which event types drive demand at that location, and returns daily-level forecasts enriched with PHQ feature attribution and explainability outputs. A baseline comparison metric is included so customers can measure the MAPE improvement attributable to PredictHQ event data.

The Forecasts API is appropriate when rapid time-to-value is the priority, or when a team does not have the capacity to build and maintain a bespoke forecasting pipeline. For teams that require full control over the underlying model, the Features API with a `beam.analysis_id` is the recommended alternative.

* API Reference: [Overview](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts/overview "mention")
* [getting-started.md](guides/forecasts-api-guides/getting-started.md "mention")

## Local Rank

Local Rank is PredictHQ’s location-sensitive ranking score that measures an event’s impact relative to its surrounding population density. It ranges from 0 to 100 and is presented on a logarithmic scale, meaning higher scores represent exponentially greater local impact.

Unlike PHQ Rank, which is normalized globally, Local Rank adjusts for how concentrated or sparse a population is in the area surrounding the event. This means that a 5,000-person event in a densely populated city will receive a lower Local Rank than a 5,000-person event in a rural or sparsely populated area - because the latter has a proportionally larger impact on local demand and activity.

Local Rank is most useful for identifying events that are significant in context, such as when optimizing logistics, staffing, or marketing at a local level.

* Getting Started Guide: [local-rank.md](predicthq-data/ranks/local-rank.md "mention")

## Loop

Loop is PredictHQ’s event feedback and contribution tool that allows customers to submit missing events and report incorrect attributes on existing events. It serves as a direct input channel to improve event data quality and completeness.

Customers can use the Loop UI to provide feedback, or use Loop Links - unique URLs generated via API- to enable distributed teams or frontline staff to contribute feedback without requiring full access to PredictHQ’s WebApp.

All submitted feedback is reviewed by PredictHQ’s data team, and accepted changes are integrated into the platform, enhancing data accuracy and model performance.

* API Reference: [Loop](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/loop "mention")
* [Loop UI](https://loop.predicthq.com/)

## PHQ Labels

PHQ Labels are AI-generated sub-category classification tags applied to events, providing more granular and semantically consistent classification than legacy event labels.

Where legacy labels are manually assigned and inconsistent in coverage, PHQ Labels are generated by machine learning models trained across the full event catalogue and cover all event categories. They enable more precise filtering - for example, distinguishing a charity run from a marathon within the broader sports category, or a product launch from an industry summit within conferences.

PHQ Labels are available via the `phq_labels` field in the Events API response. They are particularly useful for customers who need fine-grained event segmentation in demand models or operational dashboards.

* Getting Started Guide: [#phq-labels](predicthq-data/labels.md#phq-labels "mention")

## PHQ Rank

PHQ Rank is PredictHQ’s proprietary global ranking score that quantifies the potential relative impact of an event at a global level. It ranges from 0 to 100 and is calculated using a blend of signals such as predicted attendance, event type, and contextual features that influence demand.

The score is presented on a logarithmic scale, meaning that higher scores represent exponentially more impactful events. For example, an event with a PHQ Rank of 90 is significantly more impactful than one with a score of 80.

* Getting Started Guide: [phq-rank.md](predicthq-data/ranks/phq-rank.md "mention")

## Predicted Attendance

Predicted Attendance (aka PHQ Attendance) is a machine learning-generated estimate of how many people are expected to attend a given event. This prediction is based on a range of signals, including event attributes, location, timing, historical attendance patterns, and similar events. It is a core event-level metric used across the Events API, Features API and Forecasts API to quantify potential demand impact.

* Getting Started Guide: [predicted-attendance.md](predicthq-data/predicted-attendance.md "mention")

## Predicted End Times

Predicted End Time is a machine learning–generated estimate of when an event is expected to end. It is calculated by PredictHQ using historical patterns from similar events, event type, scheduled start time, and other contextual features such as venue or location.

Predicted End Time is especially useful when the original event data does not include a defined duration or end timestamp. It helps improve time-based demand modeling and enables better filtering, de-duplication, and overlap handling for events that span long periods.

* Getting Started Guide: [predicted-end-times.md](predicthq-data/predicted-end-times.md "mention")

## Predicted Event Spend

Predicted Event Spend is a model-generated estimate of the total consumer spend—across accommodation, hospitality, and transportation—expected to occur as a result of a specific event. Values are expressed in United States Dollars (USD).

This feature leverages predicted attendance, local accommodation demand, third-party economic indicators, and contextual event metadata to produce an event-attributable dollar value. It represents an approximation of spending activity in the area surrounding the event.

* Getting Started Guide: [predicted-event-spend.md](predicthq-data/predicted-event-spend.md "mention")

## Predicted Events

Predicted Events are machine-generated event records that have not yet been scheduled or publicly announced, but are predicted to occur based on historical event patterns, demand signals, and venue activity over multiple years. These events are assigned a probability-driven occurrence window (time and location) and are surfaced to support long-range planning and forecasting.

Predicted Events have a distinct `state: predicted` and can be queried via the Events API or surfaced in the WebApp using state filters. If a real event is later scheduled that matches the prediction, its state is updated automatically (e.g., to `active`), and additional confirmed details - such as start time - are added. If the predicted event does not materialize, the status may transition to `canceled` or `postponed`.

This feature helps prevent gaps in demand models by preemptively accounting for likely-but-unconfirmed events and is particularly useful in high-volume, lead-time-sensitive use cases.

* Getting Started Guide: [predicted-events.md](predicthq-data/predicted-events.md "mention")

## Predicted Impact Area

Most integrations start with a fixed radius when scoping events around a location. The problem is that the distance over which events influence demand varies by industry, location type, and how people actually move in that area - a fixed circle is an approximation that can include irrelevant events and exclude relevant ones.

Predicted Impact Area returns a location and industry-specific boundary that reflects where event-driven demand impact actually occurs. Boundaries are calibrated against real demand and event data across industries and geographies, and account for real-world constraints such as bodies of water, terrain, and road networks.

The recommended approach is to create a Saved Location using `origin_geojson` without specifying a `geojson` area — Predicted Impact Area is then calculated automatically and stored against the location. The resulting `location_id` can be passed directly to Events API, Features API, Beam, and Forecasts API without needing to manage the boundary separately.

Predicted Impact Area replaces the Suggested Radius API for all new integrations.

* API Reference: [Predicted Impact Area](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/impact-area/get-impact-area)

## Predicted Impact Patterns

Predicted Impact Patterns (previously referred to as Demand Impact Patterns) are event-level time series that quantify the expected distribution of impact across days leading up to, during, and following an event. These patterns are derived from machine learning models trained on historical demand data (e.g. accommodation bookings, transport usage) and are tailored by event type and industry vertical.

Rather than assuming all impact occurs on the event date, these patterns reflect real-world lead and lag behavior. For example, accommodation demand for a concert may peak 1–2 days prior to the event and persist after, reflecting typical visitor behavior. Each pattern provides an array of weighted values across a window of time, allowing temporal alignment of event-driven demand signals.

Predicted Impact Patterns are industry-specific and are designed to improve upon static or date-anchored features in demand forecasting models. They are designed to improve forecast accuracy by encoding time-aware event impact into supervised learning pipelines.

* Getting Started Guide: [impact-patterns.md](predicthq-data/impact-patterns.md "mention")

## Real-World Context

Real-world context refers to structured, verified representations of real-world activity that materially influence demand - events, venues, performers, and associated quantitative signals such as predicted attendance, spend, rankings, and temporal impact patterns.

Within PredictHQ's platform, real-world context flows through a layered architecture:

* **Events API** - structured and deduplicated event records for discovery and explainability
* **Saved Locations + Predicted Impact Area** - geographic scoping calibrated to where impact actually occurs
* **Beam** - demand calibration to identify which events drive demand at each location
* **Features API** - event signals transformed into model-ready time-series features
* **Forecasts API** - event-aware demand forecasts for customers who do not build their own models
* [Core Concepts](core-concepts/)

## Saved Location

Saved Location is a persistent, user-defined geographic entity consisting of a name and GeoJSON definition of a location. It may optionally include an external ID and a list of labels for filtering or grouping purposes.

Saved Locations serve as reusable identifiers in PredictHQ’s platform, allowing consistent and simplified access to features, events, and forecasts for specific business locations.

Saved Locations are recommended for managing location-specific workflows and ensuring consistent geographic definitions across APIs. They eliminate the need to repeatedly supply raw coordinates and help enforce consistency across automated forecasting and feature generation pipelines.

* API Reference: [Saved Locations](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/saved-locations "mention")

## Suggested Radius

**Deprecated.** Suggested Radius was a PredictHQ API that returned a recommended search radius around a point location for a given industry. It has been superseded by Predicted Impact Area, which provides a more accurate, data-driven geographic boundary that accounts for real-world geography rather than a fixed circle.

Existing integrations using Suggested Radius will continue to work, but new integrations should use Predicted Impact Area via Saved Locations instead.

* See: [Get Predicted Impact Area](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/impact-area/get-impact-area "mention")
