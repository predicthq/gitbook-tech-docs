---
description: >-
  Using real-world events to improve forecasting and operational decisions
  introduces structural challenges around scope, relevance, usability, and
  trust.
---

# Event-Driven Demand

Using real-world events to improve forecasting and operational decisions introduces structural challenges. These challenges are not unique to PredictHQ. Any organisation attempting to integrate event data into live systems will encounter them.

They typically surface only after implementation has begun, and they are often underestimated at the start.

There are four recurring problem areas:

* Scope
* Relevance
* Usability
* Trust

Understanding these challenges clarifies why event data alone is insufficient for production use.

## Scope

The first problem is defining where events actually matter.

Event impact is not uniform across geography or industry. A fixed radius may be too wide, introducing noise, or too narrow, missing material demand drivers. Scope is practical, not theoretical. It determines which events are even considered candidates for impact.

In dense urban areas, demand effects may be highly localised. In regional or rural contexts, effects may extend much further. Travel behaviour, population density, venue clustering, and industry type all influence how far demand impact travels.

Incorrect scope decisions are easy to make and difficult to unwind. If scope is poorly defined, downstream modeling and feature engineering are compromised.

**How PredictHQ address scope**

* [Predicted Impact Area](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/impact-area/get-impact-area) returns an industry and location-specific boundary calibrated against real demand and event data. Unlike a fixed radius, it accounts for travel behaviour, population density, venue clustering, and industry type - returning a polygon or radius that reflects where event-driven demand impact actually occurs.
* The recommended workflow is to use [Saved Locations](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/saved-locations/overview). When you create a location using `origin_geojson` without specifying a `geojson` area, Predicted Impact Area is calculated automatically and stored against that location. You can then reference it by `location_id` across Events, Features, Forecasts, and Beam - without managing the boundary yourself.

## Relevance

Not all events within scope materially affect demand.

Event-driven demand is sparse and heavy-tailed. A small number of events drive large spikes. Others create moderate but consistent lift. Multiple event types may activate simultaneously, representing overlapping real-world activity.

Generic feature selection methods are not designed for this structure. Rare spikes can dominate statistical gain metrics. Overlapping signals can distort attribution. Moderate but real effects can be masked. Feature importance can shift depending on which major events fall inside a training window.

Relevance is not a one-time decision. Demand patterns evolve, event behaviour changes, and calibration must be revisited regularly.

**How PredictHQ addresses relevance**

* The [Beam API](what-is-beam.md) calibrates event impact against your historical demand data.
* Beam isolates true event-driven variability and identifies which event types consistently explain it.
* Calibration can be rerun as demand evolves, ensuring relevance remains current.

This reduces noise and ensures that models learn from materially impactful events rather than statistical artefacts.

## Usability

Individual events are not directly consumable by forecasting models or planning systems.

Events must be transformed into structured, numerical signals that reflect timing, scale, duration, and multi-day effects. Without structured guidance, teams often build bespoke feature engineering pipelines that become difficult to maintain and inconsistent across teams.

Operational systems require deterministic, time-series signals that can be integrated directly into models, dashboards, or AI systems without extensive post-processing.

**How PredictHQ addresses usability**

* The [Features API](what-is-the-features-api.md) converts events into aggregated, model-ready time-series signals.
* It accounts for multi-day events, lead and lag effects, attendance and spend metrics, and category-level aggregation.
* When used with a Beam Analysis ID, feature outputs reflect demand-calibrated impact.

This replaces custom feature engineering with structured, reproducible API calls.

## Trust

Even statistically accurate models can fail operationally if users do not trust them.

Forecast improvements alone rarely drive adoption. Operational teams want to understand why demand is expected to change.

Trust increases when predicted demand shifts can be linked to observable real-world drivers. Concrete explanations grounded in actual events are often more important than marginal improvements in error metrics.

Trust determines time to value. If users hesitate to act on model outputs, operational impact is delayed regardless of model quality.

**How PredictHQ addresses trust**

* The [Events API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events) provides structured, verifiable event records that can be surfaced alongside forecasts or model outputs.
* When filtered using a Beam Analysis ID, returned events reflect demand-calibrated impact rather than generic event presence.
* Forecast outputs can therefore be tied back to specific real-world drivers.

This linkage between model outputs and real-world context strengthens operational confidence.

## From Events to Production Systems

Successfully using real-world events in production systems requires solving all four challenges:

1. Defining practical impact scope
2. Isolating true event-driven demand
3. Transforming events into model-ready signals
4. Providing explainable links between demand and real-world activity

PredictHQ’s APIs map directly to these challenges:

* Scope: [Predicted Impact Area](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/impact-area/get-impact-area) and [Saved Locations](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/saved-locations/overview)
* Relevance: [Beam API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/overview)
* Usability: [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) and [Forecasts API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts/overview)
* Trust: [Events API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events) (with calibrated filtering)

These are structural problems. They do not disappear with more data or more sophisticated models. They require deliberate design across data, calibration, and delivery layers.
