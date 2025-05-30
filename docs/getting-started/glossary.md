---
description: >-
  Definitions of key terms used across PredictHQ’s platform and APIs. Use as a
  reference.
---

# Glossary

## Beam

Beam helps you identify what events have impacted your demand in the past, so you can focus on the events that matter to your business. Beam provides relevancy by cutting out the noise.

The primary output of Beam is a set of Feature Importance results identifying which types of events impact your specific business. Use the Feature Importance results to filter down your Features API and Events API results to only those that are relevant to your business.

If you have multiple locations/stores, events will impact them in different ways so it's vital you use Beam to analyse historical demand at each location/store and use the relevant Features/Events at each of those locations/stores.

Beam saves you weeks and weeks of work by automating the process to filter out the noise.

* Beam API Reference:[beam](../api/beam/ "mention")
* [beam-guides](guides/beam-guides/ "mention")

## Local Rank

Local Rank is PredictHQ’s location-sensitive ranking score that measures an event’s impact relative to its surrounding population density. It ranges from 0 to 100 and is presented on a logarithmic scale.

Unlike PHQ Rank, which is normalized globally, Local Rank adjusts for how concentrated or sparse a population is in the area surrounding the event. This means that a 5,000-person event in a densely populated city will receive a lower Local Rank than a 5,000-person event in a rural or sparsely populated area - because the latter has a proportionally larger impact on local demand and activity.

Local Rank is most useful for identifying events that are significant in context, such as when optimizing logistics, staffing, or marketing at a local level.

* Getting Started Guide: [local-rank.md](predicthq-data/ranks/local-rank.md "mention")

## Loop

Loop is PredictHQ’s event feedback and contribution tool that allows customers to submit missing events and report incorrect attributes on existing events. It serves as a direct input channel to improve event data quality and completeness.

Customers can use the Loop UI to provide feedback, or use Loop Links - unique URLs generated via API- to enable distributed teams or frontline staff to contribute feedback without requiring full access to PredictHQ’s WebApp.

All submitted feedback is reviewed by PredictHQ’s data team, and accepted changes are integrated into the platform, enhancing data accuracy and model performance.

* API Reference:[loop](../api/loop/ "mention")
* [Loop UI](https://loop.predicthq.com/)

## PHQ Rank

PHQ Rank is PredictHQ’s proprietary global ranking score that quantifies the potential impact of an event. It ranges from 0 to 100 and is calculated using a blend of signals such as predicted attendance, event type, and contextual features that influence demand.

The score is presented on a logarithmic scale, meaning that higher scores represent exponentially more impactful events. For example, an event with a PHQ Rank of 90 is significantly more impactful than one with a score of 80.

* Getting Started Guide: [phq-rank.md](predicthq-data/ranks/phq-rank.md "mention")

## Predicted Attendance

Predicted Attendance (aka PHQ Attendance) is a machine learning-generated estimate of how many people are expected to attend a given event. This prediction is based on a range of signals, including event attributes, location, timing, historical attendance patterns, and similar events. It is one of the core features provided by PredictHQ and is used across the Forecasts API and Features API to quantify the demand impact of events.

* Getting Started Guide:[predicted-attendance.md](predicthq-data/predicted-attendance.md "mention")

## Predicted End Times

Predicted End Time is a machine learning–generated estimate of when an event is expected to end. It is calculated by PredictHQ using historical patterns from similar events, event type, scheduled start time, and other contextual features such as venue or location.

Predicted End Time is especially useful when the original event data does not include a defined duration or end timestamp. It helps improve time-based demand modeling and enables better filtering, de-duplication, and overlap handling for events that span long periods.

* Getting Started Guide:[predicted-end-times.md](predicthq-data/predicted-end-times.md "mention")

## Predicted Event Spend

Predicted Event Spend is a model-generated estimate of the total consumer spend—across accommodation, hospitality, and transportation—expected to occur as a result of a specific event. Values are expressed in United States Dollars (USD).

This feature leverages predicted attendance, local accommodation demand, third-party economic indicators, and contextual event metadata to produce an event-attributable dollar value. It represents an approximation of spending activity in the area surrounding the event.

* Getting Started Guide: [predicted-event-spend.md](predicthq-data/predicted-event-spend.md "mention")

## Predicted Events

Predicted Events are machine-generated event records that have not yet been scheduled or publicly announced, but are predicted to occur based on historical event patterns, demand signals, and venue activity over multiple years. These events are assigned a probability-driven occurrence window (time and location) and are surfaced to support long-range planning and forecasting.

Predicted Events have a distinct `state: predicted` and can be queried via the Events API or surfaced in the WebApp using state filters. If a real event is later scheduled that matches the prediction, its state is updated automatically (e.g., to `active`), and additional confirmed details - such as start time - are added. If the predicted event does not materialize, the status may transition to `canceled` or `postponed`.

This feature helps prevent gaps in demand models by preemptively accounting for likely-but-unconfirmed events and is particularly useful in high-volume, lead-time-sensitive use cases.

* Getting Started Guide: [predicted-events.md](predicthq-data/predicted-events.md "mention")

## Predicted Impact Patterns

Predicted Impact Patterns (previously referred to as Demand Impact Patterns) are event-level time series that quantify the expected distribution of impact across days leading up to, during, and following an event. These patterns are derived from machine learning models trained on historical demand data (e.g. accommodation bookings, transport usage) and are tailored by event type and industry vertical.

Rather than assuming all impact occurs on the event date, these patterns reflect real-world lead and lag behavior. For example, accommodation demand for a concert may peak 1–2 days prior to the event and persist after, reflecting typical visitor behavior. Each pattern provides an array of weighted values across a window of time, allowing temporal alignment of event-driven demand signals.

Predicted Impact Patterns are industry-specific and are intended to replace static or date-anchored features in demand forecasting models. They’ve been shown to significantly improve forecast accuracy when used to encode time-aware event impact in supervised learning pipelines.

* Getting Started Guide: [impact-patterns.md](predicthq-data/impact-patterns.md "mention")

## Saved Location

Saved Location is a persistent, user-defined geographic entity consisting of a name and GeoJSON definition of a location. It may optionally include an external ID and a list of labels for filtering or grouping purposes.

Saved Locations serve as reusable identifiers in PredictHQ’s platform, allowing consistent and simplified access to features, events, and forecasts for specific business locations.

We strongly recommend all customers use Saved Locations to manage location-specific workflows. They eliminate the need to repeatedly supply raw coordinates and help enforce consistency across automated forecasting and feature generation pipelines.

* API Reference:[saved-locations](../api/saved-locations/ "mention")

## Suggested Radius

Suggested Radius is a machine learning–generated spatial parameter that defines the optimal radius to use when retrieving events near a specific location. It is returned by the [Suggested Radius API](../api/suggested-radius/get-suggested-radius.md), which considers population density, event distribution, customer industry, and other contextual factors to produce a location-specific value.

We recommend all customers use Suggested Radius to determine the appropriate search radius around their business locations, rather than relying on fixed or arbitrary distances. This ensures more relevant and accurate inclusion of events when building features, querying event data, or modeling demand.

The output is relatively stable over time and can be safely cached, with monthly refreshes typically sufficient unless business context or location data changes.

* API Reference:[get-suggested-radius.md](../api/suggested-radius/get-suggested-radius.md "mention")
