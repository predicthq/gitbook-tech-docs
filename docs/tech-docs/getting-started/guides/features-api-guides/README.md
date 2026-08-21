# Features API Guides

Guides for the Features API - model-ready demand signals engineered from real-world events. Always call it with a `beam.analysis_id`; run [Beam](../beam-guides/) first if you haven't.

Recommended order:

1. [Increase Accuracy with the Features API](increase-accuracy-with-the-features-api.md) - why engineered features beat manual event aggregation
2. [Get ML Features](feature-engineering-guide.md) - retrieving features, notebook included
3. [Improving Demand Forecasting Models with Event Features](improving-demand-forecasting-models-with-event-features.md) - the worked walkthrough, from finding relevant events to a forecasting model with event features
4. [Demand Forecasting with Event Features](demand-forecasting-data-science-guides.md) - the full modeling workflow notebook
5. [Forecasting demand in Power BI with event features](integrate-with-a-demand-forecast-in-powerbi.md) - the same workflow demonstrated end to end in Power BI AutoML
6. [Using event features with time series foundation models](using-event-features-with-time-series-foundation-models.md) - features as future covariates for pre-trained models

Remember the serving path: models trained on these features need future-dated features at every forecast run - see the [Features API reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) for training and inference windows.
