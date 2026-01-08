# Receive Data via SFTP

PredictHQ can deliver Event and Broadcast data via SFTP as regularly updated files. This is a good option if you want file-based delivery without using AWS Data Exchange or APIs.

SFTP delivery follows the same full + incremental data model used by our other bulk data integrations.

## Overview

When integrating via SFTP, PredictHQ delivers data as a feed of files. Here’s what you can expect (same delivery model as our AWS Data Exchange exports):

* **Initial Full Dump**: upon setup, you will receive a full dataset covering all records you have access to.
* **Incremental Updates**: after the initial dump, we provide incremental updates containing only the new or changed records since the last update. By default, these updates are delivered daily.
* **Occasional Full Dumps**: at times (either by request or operational need), we may deliver a full dump without prior notice. You can distinguish these by the presence of full (not incremental) in the filename.

## Processing Order & Change Action

To maintain a complete and accurate dataset, process deliveries in the order they are delivered (typically by the datetime folder, oldest to newest). Within a single delivery, the individual files can be processed in any order or in parallel.

For incremental updates, make sure to check the `change_action` column to work out what action you should take the with record (`insert`, `update` or `delete`).

### File Naming

```
<delivery_config_id>/<datetime>/<data_type>/<delivery_type>-part-<number>.<ext>
```

<table><thead><tr><th width="282.97265625">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>delivery_config_id</code></td><td>PredictHQ identifier for your delivery configuration.</td></tr><tr><td><code>datetime</code></td><td>UTC export timestamp in <code>YYYYMMDD-HHMM</code> format.</td></tr><tr><td><code>data_type</code></td><td><p>The data being delivered. Can be one of the following:</p><p></p><ul><li><code>event</code></li><li><code>broadcast</code></li></ul></td></tr><tr><td><code>delivery_type</code></td><td><p>The delivery is either a full export of all available data or incremental based on the previous export. Possible values:</p><p></p><ul><li><code>full</code></li><li><code>incremental</code></li></ul></td></tr><tr><td><code>number</code></td><td><p>Each delivery is split into multiple files to keep file sizes manageable. Individual files will vary in size but will not exceed approximately 1 GB.</p><p></p><p>Files within a single delivery are not ordered and do not need to be processed sequentially. They can be processed in parallel. However, deliveries themselves must be processed in chronological order to ensure data consistency.</p></td></tr><tr><td><code>ext</code></td><td><p>The file extension indicates the data structure and compression used.</p><p></p><p>If compression is used (configurable) the data will be compressed using Snappy and the file extension will be prefixed with <code>snappy</code>.</p><p></p><p>Possible values:</p><p></p><ul><li><code>parquet</code></li><li><code>ndjson</code> - Newline-delimited JSON</li><li><code>csv</code> - Comma separated values</li><li><code>psv</code> - Pipe separated values</li></ul><p><br>E.g., <code>snappy.parquet</code></p></td></tr></tbody></table>

Within a single delivery, files can be processed in any order. Deliveries themselves should be processed oldest to newest.

## Data Retention

Files on the SFTP server are retained for a limited period and are automatically deleted after that period.

Your ingestion process should fetch and persist data promptly. Do not rely on long-term availability of files on the SFTP server.

## Access and Authentication

PredictHQ will provide:

* An SFTP URL
* A private SSH key for authentication

You will use these credentials to connect to the PredictHQ-managed SFTP server and fetch data on your own schedule.

## Typical Ingestion Flow

Most customers implement an automated process that:

1. Connects to the SFTP server
2. Lists available / delivery folders
3. Selects the next unprocessed delivery
4. Downloads all files for that delivery
5. Applies records in order, using `change_action` for incrementals
6. Records the delivery as processed in their own system

## Backwards Compatible Changes <a href="#backwards-compatible-changes" id="backwards-compatible-changes"></a>

From time to time, PredictHQ may make backwards-compatible changes to SFTP exports, including:

* Adding new fields or columns
* Adding new files alongside existing ones
* Introducing new event categories or labels

Your ingestion process should tolerate these changes.

