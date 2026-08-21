# Overview

The Forecasts API delivers event-driven demand forecasts without you building or maintaining a forecasting model.

You supply historical demand data per location. The API trains a model, applies [Beam](../beam/overview.md) automatically for feature selection, and returns daily-level forecasts with the event impact behind each day available for explainability. A baseline comparison metric shows the accuracy improvement attributable to PredictHQ data, measured on your own demand.

The workflow maps to the API's resources:

1. Create a [model](models/README.md) for a Saved Location and choose an [algorithm](algorithms/README.md) (most integrations use the default).
2. Upload historical [demand data](demand-data/README.md).
3. Train the model, then retrieve [forecasts](forecasts/README.md) on your forecast cadence. Retrain as new demand data accumulates.

Use the Forecasts API when time-to-value matters more than owning the model. For full control over model architecture and feature engineering, use the [Features API](../features/get-features.md) with a `beam.analysis_id` instead.

The Forecasts API also fits multi-model setups: run it as one candidate in a champion-challenger selection or an ensemble alongside your existing forecasts, and let measured accuracy decide which wins each series. Nothing needs replacing to adopt it.

## Guides

* [Getting Started with Forecasts API](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/forecasts-api-guides/getting-started)
* [Understanding Forecast Accuracy Metrics](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/forecasts-api-guides/understanding-forecast-accuracy-metrics)
* [Troubleshooting Guide for Forecasts API](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/forecasts-api-guides/troubleshooting)
