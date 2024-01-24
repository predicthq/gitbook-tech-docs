---
description: Upload your demand data as CSV, line-delimited JSON or JSON.
---

# Upload Demand Data

When providing data for a Beam Analysis, the minimum amount of data required is 6 months, and the maximum is 4 years.

Uploading data replaces existing data for the same date. It's not currently possible to remove data for a particular date. The idea with this endpoint is that you're continuously adding new demand data over time.

## Request

### HTTP Request

<pre class="language-apacheconf"><code class="lang-apacheconf">POST https://api.predicthq.com/v1/beam/analyses/<a data-footnote-ref href="#user-content-fn-1">$analysis_id</a>/sink
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>analysis_id</code></td><td>An existing Beam Analysis ID.</td></tr></tbody></table>

### Request Headers

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><p>Must be one of the following:</p><p></p><ul><li><code>text/csv</code></li><li><code>application/x-ldjson</code></li><li><code>application/json</code></li></ul></td></tr></tbody></table>

### Request Body

You can upload the demand data for your analysis in any of the following formats:

{% tabs %}
{% tab title="CSV" %}
The request body should contain comma-separated values representing multiple data points with the columns named `date` and `demand` as in the following example:

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

{% tab title="Line-delimited JSON" %}
The request body should contain a list JSON objects representing multiple data points, one data point per line using the following format:

```json
{"date": "2023-01-01", "demand": 12.235}
{"date": "2023-01-02", "demand": 11.4}
{"date": "2023-01-03", "demand": 12.14}
```

The following request headers must be set:

<table><thead><tr><th width="219">Header</th><th>Value</th></tr></thead><tbody><tr><td><code>Content-Type</code></td><td><code>application/x-ldjson</code></td></tr></tbody></table>

JSON Fields:

<table><thead><tr><th width="153">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>date</code><br>string<br><em>required</em></td><td>ISO8601 Date format (<code>YYYY-MM-DD</code>)<br><br>E.g., <code>2023-01-01</code></td></tr><tr><td><code>demand</code><br>string<br><em>required</em></td><td>Number value (float or integer, must be a positive number).<br><br>Demand will typically be the demand you use in your demand forecast if you are forecasting. For example, it could be units sold, room bookings, or number of staff rostered on per day or any other unit.<br><br>E.g., <code>12.235</code></td></tr></tbody></table>
{% endtab %}

{% tab title="JSON" %}
The request body should contain a JSON object representing a single data point, only a single data point can be uploaded per request using the following example:

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
curl -X POST https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/sink \
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

* [Beam Data Science Guide](../../integrations/integration-guides/beam-data-science-guide.md)

[^1]: An existing Beam Analysis ID.
