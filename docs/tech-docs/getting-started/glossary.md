---
description: >-
  Definitions of key terms used across PredictHQ’s platform and APIs. Use as a
  reference.
---

# Glossary

## Beam

Beam is a demand calibration engine that identifies which types of real-world events materially impact your historical demand.

Event-driven demand is sparse and uneven. A small number of events can create large spikes, while others generate moderate but consistent lift. Generic feature importance methods are not designed for this structure and can produce unstable or misleading results.

Beam analyses your historical demand time series to isolate event-driven variability and quantify which event types consistently explain it. The primary output is a set of Feature Importance results that can be used to filter Events API and Features API outputs to those that are demand-relevant for a specific location.

Beam analyses are location-specific. If you operate multiple locations, impact calibration should be performed per location, as event effects vary by geography and demand profile.

Beam automates ongoing event impact calibration, reducing the need to build and maintain bespoke decomposition and feature selection pipelines.

* API Reference: [Beam](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam "mention")
* [beam-guides](guides/beam-guides/ "mention")

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

Most teams start with a fixed radius when scoping events around a location. The problem is that the distance over which events influence demand varies - by industry, by location type, and by how people actually move in that area.

Predicted Impact Area returns a location and industry-specific boundary that reflects where event-driven demand impact actually occurs. Boundaries are calibrated against real demand and event data across industries and geographies.

The recommended approach is to use Saved Locations. When you create a location using origin\_geojson without specifying a geojson area, Predicted Impact Area is calculated automatically and stored against that location. You can then use the location\_id across all PredictHQ APIs - Events, Features, and Beam - without needing to manage the boundary yourself.

Predicted Impact Area is the successor to the Suggested Radius API.

* API Reference: [Predicted Impact Area](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/impact-area/get-impact-area)

## Predicted Impact Patterns

Predicted Impact Patterns (previously referred to as Demand Impact Patterns) are event-level time series that quantify the expected distribution of impact across days leading up to, during, and following an event. These patterns are derived from machine learning models trained on historical demand data (e.g. accommodation bookings, transport usage) and are tailored by event type and industry vertical.

Rather than assuming all impact occurs on the event date, these patterns reflect real-world lead and lag behavior. For example, accommodation demand for a concert may peak 1–2 days prior to the event and persist after, reflecting typical visitor behavior. Each pattern provides an array of weighted values across a window of time, allowing temporal alignment of event-driven demand signals.

Predicted Impact Patterns are industry-specific and are intended to replace static or date-anchored features in demand forecasting models. They are designed to improve forecast accuracy by encoding time-aware event impact into supervised learning pipelines.

* Getting Started Guide: [impact-patterns.md](predicthq-data/impact-patterns.md "mention")

## Real-World Context

Real-World Context refers to structured representations of real-world activity that can materially influence demand.

This includes events, venues, performers, categories, and associated quantitative signals such as predicted attendance, spend, rankings, and temporal impact patterns. Real-world context is spatial and time-bound. It answers questions such as:

* What is happening?
* Where is it happening?
* When is it happening?
* At what scale?

Within PredictHQ’s platform, real-world context is:

* Structured and deduplicated through the Events API
* Scoped geographically using Predicted Impact Area and Saved Locations
* Transformed into model-ready signals via the Features API
* Calibrated against historical demand using Beam

Real-world context is designed for integration into forecasting models, analytics pipelines, and operational systems where external activity materially affects outcomes.

## Saved Location

Saved Location is a persistent, user-defined geographic entity consisting of a name and GeoJSON definition of a location. It may optionally include an external ID and a list of labels for filtering or grouping purposes.

Saved Locations serve as reusable identifiers in PredictHQ’s platform, allowing consistent and simplified access to features, events, and forecasts for specific business locations.

Saved Locations are recommended for managing location-specific workflows and ensuring consistent geographic definitions across APIs. They eliminate the need to repeatedly supply raw coordinates and help enforce consistency across automated forecasting and feature generation pipelines.

* API Reference: [Saved Locations](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/saved-locations "mention")
