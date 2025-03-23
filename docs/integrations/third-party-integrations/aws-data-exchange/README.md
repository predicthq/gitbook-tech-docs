# Receive Data via AWS Data Exchange

AWS Data Exchange (ADX) allows customers to access regularly updated, full and incremental exports of PredictHQ data. The data is provided as either CSV, JSON or Parquet and can be automatically copied to AWS S3 where your existing Data Warehouse, Data Science platform or other data platform natively integrates with, to keep your copy of PredictHQ data continuously up-to-date.

This means with very little setup, you can incorporate the data into your models, removing or greatly simplifying the need for ELT/ETL processes to pull event data into your data warehouse. You can check out the AWS Data Exchange Overview page if you're interested to read more on how AWS Data Exchange works.

## Overview

When setting up the AWS Data Exchange integration, we will provide an initial full data dump to ensure you have complete event coverage from the start. After the initial setup, we typically deliver daily incremental updates containing only newly added or updated events. The frequency of these incremental updates can be adjusted based on your specific requirements.

Please note: On occasion, we may need to perform a full data dump outside of the regular incremental schedule. This may occur without prior notice to ensure data accuracy and integrity.

## Samples

The sample data sets are not limited in terms of columns or fields making them valuable for business and data science evaluations. However, these data sets are limited to a specific location and restricted time window that might not suit your use case. These samples therefore represent a small fraction of the data we have available. We also offer Private Listings which are filtered to match your PredictHQ license.

{% embed url="https://aws.amazon.com/marketplace/seller-profile?id=b82dc088-06e8-4b0c-9068-42e35f9a099b" %}
PredictHQ Samples on AWS Data Exchange
{% endembed %}

## Private Listings

Private Listings can be set up to match your PredictHQ license in terms of data type, locations and time window. We can provide the data in CSV, JSON or Parquet formats and configure dumps of data at regular intervals. The files contained in the data set revisions can be automatically copied to S3 where your Data Warehouse (or other data platform) will be able to pick them up.

PredictHQ will create the Private Listing and extend an “offer” to your AWS Account ID which you can then accept to start accessing the data.

Receiving data via an ADX Private Listing is a great alternative to writing code to integrate with our APIs allowing you to get the data you need much faster. Many Data Warehouses, Data Science Platforms and other data platforms integrate natively with S3 to load data.

[Get in touch](https://www.predicthq.com/contact) with us to discuss your needs and we will come back to you as soon as possible.

## Automatic Export to S3

Below is a useful video demonstrating how to setup automatic exports of data from AWS Data Exchange to S3.

{% embed url="https://youtu.be/3sHbO5T45cE" %}
Setup automatic export of data from AWS Data Exchange to S3
{% endembed %}

## Backwards Compatible Changes <a href="#backwards-compatible-changes" id="backwards-compatible-changes"></a>

Be aware that we may make backwards compatible changes to the exports from time-to-time. Examples of some changes we might make that don't break backwards compatibility and may be introduced at any time without warning:

* New columns/fields added to existing files.
* New files in addition to existing files.
* New event categories and labels.
