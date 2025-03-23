# Receive Data via AWS Data Exchange

AWS Data Exchange (ADX) allows customers to access regularly updated, full and incremental exports of PredictHQ data. The data is provided as either CSV, JSON or Parquet and can be automatically copied to AWS S3 where your existing Data Warehouse, Data Science platform or other data platform natively integrates with, to keep your copy of PredictHQ data continuously up-to-date.

This means with very little setup, you can incorporate the data into your models, removing or greatly simplifying the need for ELT/ETL processes to pull event data into your data warehouse. You can check out the AWS Data Exchange Overview page if you're interested to read more on how AWS Data Exchange works.

## Overview

When integrating with AWS Data Exchange, PredictHQ delivers event data as a feed of files. Here’s what you can expect:

* **Initial Full Dump** - Upon setup, you will receive a full dataset covering all events you have access to.
* **Incremental Updates** - After the initial dump, we provide incremental updates containing only the new or changed records since the last update. By default, these updates are delivered daily.
* **Occasional Full Dumps** - While incremental updates are the standard, at times (either by request or operational need), we may deliver a full dump without prior notice. You can distinguish these by the presence of `full` (not `incremental`) in the filename.

### Processing Order & Deletions

It is essential to process all ADX revisions in the order they are delivered to maintain a complete and accurate dataset. However, within a revision, the individual files can be processed in any order or in parallel.

For incremental updates, make sure to check the `change_action` column to work out what action you should take the with record (`insert`, `update` or `delete`).

### File Naming

```
<delivery_config_id>/<datetime>/<data_type>/<delivery_type>-part-<number>.<ext>
```

<table><thead><tr><th width="282.97265625">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>delivery_config_id</code></td><td>Internal PredictHQ identifier for your ADX configuration.</td></tr><tr><td><code>datetime</code></td><td>This is the date and time the data was exported (UTC).<br><br>Date format: <code>YYYYMMDD-HHMM</code><br>E.g., <code>20250324-0115</code> (24th March, 2025 at 01:15 UTC)</td></tr><tr><td><code>data_type</code></td><td><p>The data being delivered. Can be one of the following:</p><p></p><ul><li><code>event</code></li><li><code>broadcast</code></li></ul></td></tr><tr><td>delivery_type</td><td><p>The delivery is either a full export of all available data or incremental based on the previous export. Possible values:</p><p></p><ul><li><code>full</code></li><li><code>incremental</code></li></ul></td></tr><tr><td><code>number</code></td><td>When exporting, the data is separated into multiple files to keep the file size small.  File sizes will range but won't be larger than 1 GB. Files are not sequential and do not need to be processed sequentially. You are able to process the files in parallel (it's important each ADX revision is processed sequentially, but within a revision, the files can be processed in parallel).</td></tr><tr><td><code>ext</code></td><td><p>The file extension indicates the data structure and compression used.</p><p></p><p>If compression is used (configurable) the data will be compressed using Snappy and the file extension will be prefixed with <code>snappy</code>.</p><p></p><p>Possible values:</p><p></p><ul><li><code>parquet</code></li><li><code>ndjson</code> - Newline-delimited JSON</li><li><code>csv</code> - Comma separated values</li><li><code>psv</code> - Pipe separated values</li></ul><p><br>E.g., <code>snappy.parquet</code></p></td></tr></tbody></table>

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
