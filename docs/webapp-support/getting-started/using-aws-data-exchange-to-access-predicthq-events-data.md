# Using AWS Data Exchange to Access PredictHQ Events Data

AWS Data Exchange (ADX) makes it easy to find, subscribe to, and use third-party data in the cloud. You can use the AWS Data Exchange API to load data directly into [Amazon Simple Storage Service (S3)](https://aws.amazon.com/s3/) and use a range of AWS [analytics](https://aws.amazon.com/big-data/datalakes-and-analytics/) and [machine learning (ML)](https://aws.amazon.com/machine-learning/) services to analyze it.

If you are already using ADX or want to try using it for a new project PredictHQ allows you to use it to access our demand intelligence data. Integrating with ADX is a quick and easy way to get access to events data in your environment reducing the effort needed from your technical teams to ingest the data. This is an alternative to calling [PredictHQ's Events API](../../api/events/search-events.md) to pull the data into your data lake.

ADX allows customers to access regularly updated, full and incremental exports of PredictHQ data. The data is provided in either a CSV, JSON, or Parquet format and can be automatically copied to AWS S3 where your existing Data Warehouse, Data Science platform, or other data platform natively integrates with, to keep your copy of PredictHQ data continuously up-to-date.

This means with very little setup, you can incorporate the data into your models, removing or greatly simplifying the need for ELT/ETL processes to pull event data into your data warehouse. You can check out the [AWS Data Exchange Overview](https://aws.amazon.com/data-exchange/) page if you're interested to read more on how AWS Data Exchange works.

See PredictHQ's [AWS Data Exchange](../../integrations/third-party-integrations/aws-data-exchange/) technical documentation for details on how you can access PredictHQ's data via AWS Data Exchange.
