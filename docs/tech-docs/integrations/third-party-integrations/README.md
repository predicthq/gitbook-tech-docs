# Third-Party Integrations

Managed delivery of PredictHQ's verified real-world context into your own environment - the foundation for model training and [internal grounding](../integration-guides/internal-grounding.md), with no sync pipeline to build.

* [Snowflake](snowflake/) - shared tables, queried in place. The lowest-friction path if you're on Snowflake.
* [AWS Data Exchange](aws-data-exchange/) - full and incremental exports to S3.
* [SFTP](sftp.md) - the same export model, delivered as files.
* Destination guides: [Databricks](integrate-with-databricks.md), [BigQuery](google-cloud-bigquery.md), [Tableau](tableau-data-connector.md), and [Power BI](integrate-with-a-demand-forecast-in-powerbi.md).

If none of these fit, the APIs plus [Keep Data Updated via API](../integration-guides/keep-data-updated-via-api.md) cover the do-it-yourself path.
