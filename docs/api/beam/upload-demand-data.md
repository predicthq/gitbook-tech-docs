---
description: Upload your demand data as CSV, line-delimited JSON or JSON.
---

# Upload Demand Data

Beam Analyses support daily or weekly demand data. The type of data is detected automatically on upload.

For **daily** demand the minimum amount of data required is **6 months**, or 180 data points. Beam can impute up to 20% of missing values, provided that the minimum data requirements are satisfied and there are no more than 7 consecutive days missing.

For **weekly** demand the minimum amount of data required is **2 years**, or 104 data points. Beam can impute up to 10% of missing values, provided that the minimum data requirements are satisfied and there are no more than 5 consecutive weeks missing. All weekly data points must align with the **start of the week** and occur on the same weekday.

All data points need to be between 2017-01-01 and one year into the future from today's date (today + 365 days).

Uploading data replaces existing data for the same date. It's not currently possible to remove data for a particular date. The idea with this endpoint is that you're continuously adding new demand data over time.

{% hint style="info" %}
The data can be uploaded in chunks, but the analysis data must remain valid at all times. If a newly uploaded chunk renders the analysis data invalid (for example, by introducing a large gap between data points), the chunk will be rejected, and the previously stored demand data will be preserved.
{% endhint %}

## Request

### HTTP Request

<pre class="language-http"><code class="lang-http">POST https://api.predicthq.com/v1/beam/analyses/<a data-footnote-ref href="#user-content-fn-1">$analysis_id</a>/sink
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>analysis_id</code></td><td>An existing Beam Analysis ID.</td></tr></tbody></table>

### Request Headers

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><p>Must be one of the following:</p><ul><li><code>text/csv</code></li><li><code>application/x-ndjson</code></li><li><code>application/json</code></li><li><code>application/x-ldjson</code> (deprecated)</li></ul><p>Note: <code>application/x-ldjson</code> has been deprecated in favor of <code>application/x-ndjson</code>. However the data format is exactly the same (newline delimited JSON). We recommend using <code>application/x-ndjson</code></p></td></tr></tbody></table>

### Request Body

You can upload the demand data for your analysis in any of the following formats:

{% tabs %}
{% tab title="CSV" %}
The request body should contain comma-separated values that represent multiple data points with the column names (in lowercase) as `date` and `demand`, demonstrated by the example below:

```csv
date,demand
2023-01-01,12.235
2023-01-02,11.4
2023-01-03,12.14
```

The following request headers must be set:

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>text/csv</code></td></tr></tbody></table>

Column Types:

<table><thead><tr><th width="153">Column</th><th>Description</th></tr></thead><tbody><tr><td><code>date</code><br>string<br><em>required</em></td><td>ISO8601 Date format (<code>YYYY-MM-DD</code>)<br><br>E.g., <code>2023-01-01</code></td></tr><tr><td><code>demand</code><br>number<br><em>required</em></td><td>Number value (float or integer, must be a positive number).<br><br>Demand will typically be the demand you use in your demand forecast if you are forecasting. For example, it could be units sold, room bookings, or number of staff rostered on per day or any other unit.<br><br>E.g., <code>12.235</code></td></tr></tbody></table>
{% endtab %}

{% tab title="Newline-delimited JSON" %}
The request body should consist of line-delimited JSON objects, each representing a distinct data point. Ensure that the fields within these objects are named `date` and `demand` (lowercase). The format should follow the example given below:

```json
{"date": "2023-01-01", "demand": 12.235}
{"date": "2023-01-02", "demand": 11.4}
{"date": "2023-01-03", "demand": 12.14}
```

The following request headers must be set:

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>application/x-ndjson</code></td></tr></tbody></table>

JSON Fields:

<table><thead><tr><th width="153">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>date</code><br>string<br><em>required</em></td><td>ISO8601 Date format (<code>YYYY-MM-DD</code>)<br><br>E.g., <code>2023-01-01</code></td></tr><tr><td><code>demand</code><br>string<br><em>required</em></td><td>Number value (float or integer, must be a positive number).<br><br>Demand will typically be the demand you use in your demand forecast if you are forecasting. For example, it could be units sold, room bookings, or number of staff rostered on per day or any other unit.<br><br>E.g., <code>12.235</code></td></tr></tbody></table>
{% endtab %}

{% tab title="JSON" %}
Note that this format is only suitable for appending data to an already valid data set.

The request body should contain a JSON object that represents a single data point. For each request, only one data point is permitted. Ensure that the fields are named `date` and `demand` (lowercase), as demonstrated in the example below:

```json
{
  "date": "2023-01-01",
  "demand": 12.235
}
```

The following request headers must be set:

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>application/json</code></td></tr></tbody></table>

JSON Fields:

<table><thead><tr><th width="153">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>date</code><br>string<br><em>required</em></td><td>ISO8601 Date format (<code>YYYY-MM-DD</code>)<br><br>E.g., <code>2023-01-01</code></td></tr><tr><td><code>demand</code><br>string<br><em>required</em></td><td>Number value (float or integer, must be a positive number).<br><br>Demand will typically be the demand you use in your demand forecast if you are forecasting. For example, it could be units sold, room bookings, or number of staff rostered on per day or any other unit.<br><br>E.g., <code>12.235</code></td></tr></tbody></table>
{% endtab %}
{% endtabs %}

## Response

If successful, the HTTP response code will be `202 Accepted`.

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X POST "https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/sink" \
     -H "Content-Type: text/csv" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     --data @data.csv
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.post(
    url="https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/sink",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Content-Type": "text/csv"
    },
    data=open("data.csv")
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [beam-guides](../../getting-started/guides/beam-guides/ "mention")

[^1]: An existing Beam Analysis ID.
