# Third-party integrations

Managed delivery of PredictHQ's verified real-world context into your own environment - the foundation for model training, explainability, and [provisioned grounding](../integration-guides/internal-grounding.md), with no sync pipeline to build.

* [Snowflake](snowflake/) - shared tables, queried in place. The lowest-friction path if you're on Snowflake.
* [AWS Data Exchange](aws-data-exchange/) - full and incremental exports to S3.
* [SFTP](sftp.md) - the same export model, delivered as files.
* Destination guides: [Databricks](integrate-with-databricks.md), [BigQuery](../integration-guides/loading-event-data-into-a-data-warehouse.md) (worked warehouse-loading example), [Tableau](using-event-data-in-tableau.md), [Power BI](using-event-data-in-power-bi.md), and [Excel](connecting-to-predicthq-apis-with-microsoft-excel.md).

If none of these fit, the APIs plus [Keep data updated via API](../integration-guides/keep-data-updated-via-api.md) cover the do-it-yourself path.
