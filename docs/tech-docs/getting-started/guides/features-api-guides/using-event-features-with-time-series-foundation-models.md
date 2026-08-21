---
description: >-
  Supply PredictHQ event features as future covariates to pre-trained
  forecasting models such as Chronos, TimesFM, and TimeGPT.
---

# Using event features with time series foundation models

Pre-trained forecasting models are applied zero-shot or with light fine-tuning - there is no per-location training step. They learn temporal patterns from large generic corpora, which means real-world drivers such as concerts, sports fixtures, and holidays are invisible to them unless supplied as covariates. Because events are known in advance, PredictHQ features provide real covariate values across the forecast horizon - no zero-filling or lagged proxies.

Most foundation model interfaces accept these as known future covariates - variously called future covariates, exogenous variables, or dynamic features depending on the model. Support varies by model and version: some accept covariates natively, some only through a wrapper framework, and some not at all - so check your model's documentation rather than assuming the covariates are being used.

## Prepare the covariates

1. Run [Beam](../../core-concepts/what-is-beam.md) for each location to get an `analysis_id`. Foundation model covariate mechanisms are lightweight, and published evaluations show accuracy degrading when they're fed noisy or irrelevant series - Beam limits the covariate set to the event signals that drive demand at that location.
2. Retrieve historical features covering the same period as the demand history you pass to the model:

```json
{
  "beam": { "analysis_id": "$ANALYSIS_ID" },
  "active": { "gte": "$HISTORY_START", "lte": "$NOW" }
}
```

3. Retrieve future features covering the forecast horizon:

```json
{
  "beam": { "analysis_id": "$ANALYSIS_ID" },
  "active": { "gte": "$NOW", "lte": "$FORECAST_END" }
}
```

4. Join both windows to your demand series on date, and pass them through the model's covariates interface alongside the demand history.

## Keep the covariates fresh

Retrieve future features ahead of each forecast run rather than caching them: new events are announced inside the forecast horizon continuously, attendance predictions are revised as events approach, and events are cancelled. Refresh the Beam Analysis monthly by appending new demand data - see the [Standard integration pattern](../../../integrations/integration-guides/standard-integration-pattern.md) for the production architecture and refresh cadences.

## Related

* [Features API reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) - available features and configuration
* [What is the Features API?](../../core-concepts/what-is-the-features-api.md)
* [Data Leakage in Backtesting](../../core-concepts/data-leakage-in-backtesting.md) - why forward-looking features don't leak future information into evaluation
