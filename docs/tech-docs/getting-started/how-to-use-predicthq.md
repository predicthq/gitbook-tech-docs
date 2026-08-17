---
description: >-
  The recommended integration paths for PredictHQ: train forecasting models on
  event features, ground AI systems in verified real-world context, or get
  event-driven forecasts without building a model.
---

# How to use PredictHQ

PredictHQ is the real-world context platform powering enterprise AI decisions. Its verified events, predicted impacts, and demand-calibrated features are consumed along a recommended path for each job: train your forecasting models on event features, ground LLMs and agents in verified context at answer time, get event-driven forecasts without building a model, or analyze what drives demand at your locations. This page routes you to the right path and shows how the paths fit together.

## Start with the job you're doing

| Your job                                                | Path                                                                        |
| ------------------------------------------------------- | --------------------------------------------------------------------------- |
| Improve the accuracy of a forecasting model you own     | [Train your models on event features](#train-your-models-on-event-features) |
| Get event-driven forecasts without building a model     | [Get forecasts without building a model](#get-forecasts-without-building-a-model) |
| Stop an LLM or AI agent guessing about the real world   | [Ground your AI in verified context](#ground-your-ai-in-verified-context)   |
| Understand which events drive demand at your locations  | [Understand what drives your demand](#understand-what-drives-your-demand)   |
| Show operators the events behind a demand shift         | [Events API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events) with `beam.analysis_id` for explainability |

Whichever path you take, the first two steps are the same, and they calibrate everything downstream:

1. Create a [Saved Location](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/saved-locations/overview) for each business location using `origin_geojson` - Predicted Impact Area is calculated automatically, defining where events actually affect that location.
2. Run [Beam](core-concepts/what-is-beam.md), PredictHQ's relevancy engine, with your historical demand data. The resulting `analysis_id` scopes every downstream call to the event categories and thresholds that drive demand at that location.

## Train your models on event features

For data science teams who own a forecasting model and want it more accurate.

Retrieve model-ready features from the [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) keyed by your `beam.analysis_id`: historical windows to train on alongside your demand history, and future-dated windows at every forecast run. Because events are known in advance, the future values are real demand signals rather than estimates - no zero-filling the forecast horizon.

Using a pre-trained time series foundation model instead? There is no training step - supply the same future-dated features as covariates. See [Using event features with time series foundation models](guides/features-api-guides/using-event-features-with-time-series-foundation-models.md).

* [Which API Should I Use?](core-concepts/which-api-should-i-use.md)
* [Standard Integration Pattern](../integrations/integration-guides/standard-integration-pattern.md) - the production architecture

## Get forecasts without building a model

For teams that want event-driven forecast accuracy with rapid time-to-value, without building or maintaining a forecasting pipeline.

Supply historical demand data to the [Forecasts API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts/overview) and it trains a model, applies Beam automatically, and returns daily-level forecasts with event impact and explainability built in. A baseline comparison shows the accuracy improvement attributable to PredictHQ data - measured on your own demand.

The Forecasts API also fits multi-model setups: run it as one candidate in a champion-challenger selection or an ensemble alongside your existing forecasts, and let measured accuracy decide which wins each series. Nothing needs replacing to adopt it.

* [Getting Started with Forecasts API](guides/forecasts-api-guides/getting-started.md)

## Ground your AI in verified context

For ML platform and agent teams whose LLMs or agents make demand-related decisions, where an AI hallucination (a confident, plausible, wrong answer) carries real cost.

Grounding gives a model verified real-world facts at the moment it answers, so it responds from what is true instead of hallucinating. Retrieval-augmented generation (RAG) is one technique for achieving it. PredictHQ supports two grounding architectures; they are alternatives to each other, and which one fits is mostly a governance and maintenance question:

* **Internal grounding** - verified event context is delivered into your environment (Snowflake, AWS Data Exchange, SFTP, or API sync) and your AI systems retrieve from a store you govern. Choose this when data residency, governance, or retrieval scale matter.
* **External grounding** - your agents query the [PredictHQ MCP server](../ai/mcp.md) on demand and hold no copy of anything. Choose this when zero pipeline maintenance matters and your stack already speaks tool-calling.

* [Using PredictHQ with AI Assistants](../ai/using-predicthq-with-ai-assistants.md)
* [PredictHQ MCP in Agentic Workflows](../ai/predicthq-mcp-in-agentic-workflows.md)

## Understand what drives your demand

For analysts and data scientists who need to know which real-world events matter before committing to a build - or need evidence for what happened.

Beam's [Feature Importance](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/analyses/get-feature-importance) results rank the event categories that drive demand at each location and quantify how much of your demand variability is event-driven. PredictHQ explains more than 60 percent of real-world demand variability. Drill into the specific events behind any shift with the [Events API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events) using the same `analysis_id`.

* [Understanding Demand Variability and Event Contribution in Beam](guides/beam-guides/understanding-demand-variability-and-event-contribution-in-beam.md)

## How the paths fit together

Training improves your model before it runs. Grounding supplies verified context while it runs. The two never mix - grounding doesn't touch the training model - and the two grounding architectures are alternatives to each other, not to training. Time series foundation models don't change this split; they shrink the training step and move more of the value to inference time.

The paths share the same foundation, so they combine naturally: the Saved Locations and Beam analyses you set up for a forecasting integration are the same ones that scope a grounding corpus or an agent's MCP queries. Many production deployments run a training path and a grounding path side by side - a model trained on event features, and an AI layer that explains its outputs from verified event context.

## Next steps

* [API Quickstart](api-quickstart.md) - make your first call
* [Which API Should I Use?](core-concepts/which-api-should-i-use.md) - per-task API selection
* [Standard Integration Pattern](../integrations/integration-guides/standard-integration-pattern.md) - the production reference architecture
