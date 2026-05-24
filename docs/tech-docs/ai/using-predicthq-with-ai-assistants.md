# Using PredictHQ with AI Assistants

PredictHQ provides structured real-world context that AI assistants and agent-based systems can retrieve at inference time - grounding responses, forecasts, and recommendations in verified, location-specific event data.

### The Role of Real-World Context in AI Systems

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

### Architectural Pattern

A typical integration pattern is:

1. A user asks a question or requests a forecast.
2. The AI assistant determines that external context is required.
3. The assistant calls PredictHQ APIs for a specified location and time range.
4. Structured context is returned.
5. The assistant incorporates that context into its reasoning or response.

PredictHQ APIs are stateless and deterministic. The same request always returns the same result, making them well-suited for use at inference time inside AI systems.

The [MCP Server](mcp.md) is the simplest way to implement this pattern - it connects any MCP-compatible AI assistant directly to PredictHQ's APIs without requiring custom integration code.

### Scope, Relevance, and Usability

AI systems that consume real-world context must address the same structural challenges described in [Event-Driven Demand](../getting-started/core-concepts/event-driven-demand.md):

* **Scope** - defining where events matter
* **Relevance** - identifying which events materially impact demand
* **Usability** - transforming events into structured signals
* **Trust** - explaining decisions in terms of observable real-world drivers

PredictHQ's APIs map directly to these challenges:

* Predicted Impact Area defines practical geographic scope.
* Beam calibrates event relevance using historical demand.
* The Features API converts events into model-ready time-series signals.
* The Events API provides verifiable event records that can be surfaced in explanations.

This separation allows AI assistants to retrieve either raw event context or calibrated signals depending on the workflow.

### Example Workflows

#### Demand Explanation

An AI assistant receives a forecasted spike for a hotel location.

It retrieves event context for the relevant dates and identifies a major concert with high predicted attendance and a regional conference overlapping the same period. The assistant explains the forecast increase by referencing those specific events.

#### Operational Copilot

A retail operations assistant evaluates staffing levels for an upcoming weekend.

It retrieves demand-calibrated event signals via the Features API and flags elevated local activity driven by sports and entertainment events.

#### Planning and Scenario Analysis

An AI system assesses exposure to future demand drivers across multiple locations.

It retrieves scoped event context and identifies concentrations of high-impact events in certain regions.

### When to Use PredictHQ in AI Workflows

Use PredictHQ when:

* Decisions depend on external, time-bound real-world activity
* Explanations must reference concrete events
* Forecasts need structured external context
* Agent systems require deterministic, queryable signals

### Next Steps

* [Build with AI](build-with-ai.md) - tools and resources for building PredictHQ integrations with AI assistants and coding agents
* [MCP Server](mcp.md) - connect an AI assistant to PredictHQ's APIs directly
* [Agent Skills](build-with-ai.md#agent-skills) - install PredictHQ integration best practices into your coding agent
