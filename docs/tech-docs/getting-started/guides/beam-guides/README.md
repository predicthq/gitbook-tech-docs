# Beam Guides

Working guides and notebooks for Beam, PredictHQ's relevancy engine. Run Beam before configuring features or building forecasts - the `analysis_id` it produces calibrates everything downstream.

Recommended order:

1. [Understanding Demand Variability and Event Contribution in Beam](understanding-demand-variability-and-event-contribution-in-beam.md) - how to read what Beam tells you about your demand
2. [ML features by location notebook](https://github.com/predicthq/phq-data-science-docs/blob/master/demand-forecasting-with-events/identify-location-level-features-with-beam-api.ipynb) - from analysis to model-ready features, per location
3. [ML features by group notebook](https://github.com/predicthq/phq-data-science-docs/blob/master/demand-forecasting-with-events/identify-group-level-features-with-beam-api.ipynb) - one consistent feature set across many locations sharing a model
4. [Sample Demand Data](sample-demand-data.md) - the demand data format Beam expects

New to Beam? Read [What is Beam?](../../core-concepts/what-is-beam.md) first.
