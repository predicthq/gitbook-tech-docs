---
description: >-
  Deploy PredictHQ's verified real-world context into Databricks via S3 or
  Snowflake for model training, inference-time features, and grounding AI
  systems.
---

# Integrate with Databricks

Databricks is where many teams train demand forecasting models and build AI systems - and both jobs need verified real-world context in the lakehouse. PredictHQ data lands in Databricks through two natively supported paths, both continuously updated and neither requiring a custom pipeline:

* **AWS Data Exchange to S3** - full and incremental exports [delivered to S3](aws-data-exchange/), which Databricks reads directly.
* **Snowflake shared tables** - a [Secure Data Share](snowflake/) queried from Databricks over the native Snowflake connector.

[Get in touch](https://www.predicthq.com/contact) with us to set up delivery via ADX or Snowflake. PredictHQ can also deliver Features API output per Beam Analysis through the same channels, so model-ready features arrive alongside the event records.

Once landed, the data serves each integration path:

* **Model training** - join event features to your demand history and train in your existing Databricks ML workflow. Features are keyed by a `beam.analysis_id`, so feature selection reflects what actually drives demand at each location.
* **Inference** - retrieve future-dated features at every forecast run, whether your models are bespoke or [pre-trained time series foundation models](../../getting-started/guides/features-api-guides/using-event-features-with-time-series-foundation-models.md) consuming them as covariates.
* **Internal grounding** - the event tables double as the retrieval corpus for LLMs and agents built on Databricks, so AI systems answer from verified real-world context governed by your own platform - see [Grounding paths](../integration-guides/standard-integration-pattern.md#grounding-paths).

Databricks resources for reading data from S3 or Snowflake:

{% embed url="https://docs.databricks.com/en/storage/amazon-s3.html" %}

{% embed url="https://docs.databricks.com/en/external-data/amazon-s3-select.html" %}

{% embed url="https://docs.databricks.com/en/external-data/snowflake.html" %}
