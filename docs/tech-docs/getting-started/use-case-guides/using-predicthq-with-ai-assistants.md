# Using PredictHQ with AI Assistants

AI assistants and agent-based systems are increasingly embedded in operational workflows. These systems generate forecasts, recommend actions, answer analytical questions, and explain demand shifts in real time.

Large language models are strong at reasoning over text and structured inputs. They are not inherently reliable at understanding time-bound, location-specific real-world activity.

PredictHQ provides structured real-world context that can be retrieved at inference time and supplied to AI systems as grounded inputs.

## The Role of Real-World Context in AI Systems

AI assistants frequently encounter questions such as:

* Why is demand forecasted to increase next week?
* What external factors may affect performance in this location?
* Why are prices elevated this weekend?
* What events could impact staffing levels?

Without structured context, language models generate plausible explanations based on general knowledge. These responses may be incomplete, outdated, or misaligned with the specific location and time window in question.

PredictHQ supplies:

* Verified, structured event records
* Location-scoped context
* Quantified signals such as attendance and rank
* Demand-calibrated filtering via Beam

This enables AI systems to reference concrete, time-bound drivers rather than relying on generic assumptions.

## Architectural Pattern

A typical integration pattern is:

1. A user asks a question or requests a forecast.
2. The AI assistant determines that external context is required.
3. The assistant calls PredictHQ APIs for a specified location and time range.
4. Structured context is returned.
5. The assistant incorporates that context into its reasoning or response.

PredictHQ APIs are stateless and deterministic. The same request returns the same result. This makes them suitable for use at inference time inside AI systems.

## Scope, Relevance, and Usability

AI systems that consume real-world context must address the same structural challenges described in [Event-Driven Demand](../core-concepts/event-driven-demand.md):

* Scope: defining where events matter
* Relevance: identifying which events materially impact demand
* Usability: transforming events into structured signals
* Trust: explaining decisions in terms of observable real-world drivers

PredictHQ’s APIs map directly to these challenges:

* Predicted Impact Area defines practical geographic scope.
* Beam calibrates event relevance using historical demand.
* The Features API converts events into model-ready time-series signals.
* The Events API provides verifiable event records that can be surfaced in explanations.

This separation allows AI assistants to retrieve either raw event context or calibrated signals depending on the workflow.

## Example Workflows

### Demand Explanation

An AI assistant receives a forecasted spike for a hotel location.

It retrieves event context for the relevant dates and identifies:

* A major concert with high predicted attendance
* A regional conference overlapping the same period

The assistant explains the forecast increase by referencing those specific events.

### Operational Copilot

A retail operations assistant evaluates staffing levels for an upcoming weekend.

It retrieves demand-calibrated event signals via the Features API and flags elevated local activity driven by sports and entertainment events.

### Planning and Scenario Analysis

An AI system assesses exposure to future demand drivers across multiple locations.

It retrieves scoped event context and identifies concentrations of high-impact events in certain regions.

## When to Use PredictHQ in AI Workflows

Use PredictHQ when:

* Decisions depend on external, time-bound real-world activity
* Explanations must reference concrete events
* Forecasts need structured external context
* Agent systems require deterministic, queryable signals

PredictHQ is designed to integrate cleanly into forecasting models, analytics pipelines, and AI systems that operate at decision time.

## Next Steps

* Define [Saved Locations](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/saved-locations/overview) for consistent geographic scope
* Use [Predicted Impact Area](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/impact-area/get-impact-area) to establish practical boundaries
* Run [Beam](../core-concepts/what-is-beam.md) to calibrate event relevance (if historical demand is available)
* Retrieve structured context via the [Events](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events) or [Features APIs](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features)
