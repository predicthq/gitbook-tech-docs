# Receive Data via Snowflake

Snowflake Secure Data Share enables companies to access PredictHQ’s data in a controlled and efficient way. Access to a Secure Share of our events means you will experience a familiar and high-performance SQL interface with an up-to-date, clean, and complete set of PredictHQ’s data.

This means you can immediately incorporate the data into your models, removing or greatly simplifying the need for ELT/ETL processes to pull event data into your data warehouse. You can check out [Introduction to Secure Data Sharing](https://docs.snowflake.com/en/user-guide/data-sharing-intro.html) page if you're interested to read more on Snowflake's Secure Data Sharing.

## Sample Data Shares

PredictHQ offers multiple up-to-date event Data Shares on Snowflake's Marketplace. This, bundled up with Snowflake's 30-day trial, offers you a commitment-free opportunity to try PredictHQ's data for free.

The sample Data Shares are not limited in terms of columns or fields making them valuable for business and data science evaluations. However, these data shares are limited to a specific location and restricted time window that might not suit your use case. These samples therefore represent a small fraction of the data we have. We also offer Customized Data Shares which are filtered to match customers' preferences.

{% embed url="https://app.snowflake.com/marketplace/listings/PredictHQ?search=predicthq" %}
PredictHQ Sample Data Shares on Snowflake Marketplace
{% endembed %}

## Customized Data Shares

Customized Data Shares can be set up to match your preferences in terms of data type, location, time window and business use case. They are secure, easy to set up and usually don't require business resources for data integrations if you're already in the Snowflake platform.

[Get in touch](https://www.predicthq.com/contact) with us to discuss your needs and we will come back to you as soon as possible.

## Backwards Compatible Changes <a href="#backwards-compatible-changes" id="backwards-compatible-changes"></a>

Be aware that we may make backwards compatible changes to the Snowflake tables from time-to-time. Examples of some changes we might make that don't break backwards compatibility and may be introduced at any time without warning:

* New columns added to existing tables.
* New tables in addition to existing tables.
* New event categories and labels.

## Frequently Asked Questions

* **How does costing work on the data shares?**\
  Snowflake's architecture separates data warehousing into different distinct layers: storage, virtual warehouses (compute), and cloud services. By using PredictHQ's data through Snowflake, you would only pay for the amount of computation that you would perform on the shared data. In other words, there is no cost for you to store the data and you would only be billed for running queries on the shared data. You can read more about [Snowflake's costing on their website](https://www.snowflake.com/pricing-page-registration-page/).
* **How frequently is the shared data updated?**\
  PredictHQ's data shares get updated at midnight in the region's timezone. This frequency is generally sufficient for most business use cases. If the business use case requires more up-to-date data, it can be provided down to minute-level frequency. However, this would incur extra computation costs.
* **Can I make a change in the shared data or re-share it?**\
  All database objects shared between accounts are read-only. They cannot be directly modified or deleted, including adding or modifying table data. Shared databases and all the objects in the database cannot be re-shared with other accounts.
