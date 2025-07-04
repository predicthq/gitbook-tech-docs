---
description: >-
  Retrieve results of the correlation of our event data with your transactional
  demand data.
---

# Get Correlation Results

## Request

### HTTP Request

<pre class="language-http"><code class="lang-http">GET https://api.predicthq.com/v1/beam/analyses/<a data-footnote-ref href="#user-content-fn-1">$analysis_id</a>/correlate
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>analysis_id</code></td><td>An existing Beam Analysis ID.</td></tr></tbody></table>

### Query Parameters

<table><thead><tr><th width="185">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>date.*</code><br>string<br><em>required</em></td><td>Filters out correlation data not included in the date range. The <code>date</code> parameter must have an upper (<code>lt</code> or <code>lte</code>) and lower (<code>gt</code> or <code>gte</code>) bound suffix.<br><br>The accepted format for this parameter is <code>YYYY-MM-DD</code><br><br>E.g. <code>?date.gt=2017-01-01&#x26;date.lte=2017-12-01</code></td></tr><tr><td><code>limit</code><br>number<br>optional</td><td>Limits the length of the Beam decomposition list returned. The default <code>limit</code> is <code>30</code>.<br><br>E.g. <code>?limit=20</code></td></tr><tr><td><code>offset</code><br>number<br>optional</td><td>Specifies starting offset of the Beam decomposition list returned. The default <code>offset</code> is <code>0</code>.<br><br>E.g. <code>?offset=3</code></td></tr></tbody></table>

## Response

### Response Fields

{% hint style="info" %}
:warning: Please note we have deprecated some fields in this endpoint. The deprecated fields are not intended to be used to get current feature values for use in forecasting or other use-cases. They're a snapshot of some of the data from the time the correlation process was run, so for any other purposes are immediately out-of-date. Please fetch the latest data from Features API instead.
{% endhint %}

<table><thead><tr><th width="393">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>count</code><br>number</td><td>The number of Beam decomposition dates returned.</td></tr><tr><td><code>dates</code><br>array</td><td>An array of Beam decomposition dates.</td></tr><tr><td><code>dates.date</code><br>date</td><td>The date of the Beam decomposition.</td></tr><tr><td><code>dates.actual_demand</code><br>number</td><td>The actual demand for a given date.</td></tr><tr><td><code>dates.baseline_demand</code><br>number</td><td>The expected demand for a given date.</td></tr><tr><td><code>dates.remainder</code><br>number</td><td>The difference between the <code>actual_demand</code> and the <code>baseline_demand</code> for a given date. This value may be positive or negative.</td></tr><tr><td><code>dates.impact_significance</code><br>string</td><td><p>Enum specifying how unusual the <code>remainder</code> is for a given date.<br><br><strong>Possible values:</strong></p><ul><li><code>NO_IMPACT</code></li><li><code>WEAK</code></li><li><code>MEDIUM</code></li><li><code>SIGNIFICANT</code></li></ul></td></tr><tr><td><code>dates.impact_significance_score</code><br>number</td><td><p>Number specifying how unusual the <code>remainder</code> is for a given date. This value maps to <code>impact_significance</code>.<br><br><strong>Possible values:</strong></p><ul><li><code>0</code></li><li><code>1</code></li><li><code>2</code></li><li><code>3</code></li></ul></td></tr><tr><td><code>dates.features</code><br>object<br><span data-gb-custom-inline data-tag="emoji" data-code="26a0">⚠️</span> Deprecated</td><td>A json object containing all non-zero features for a given date.</td></tr><tr><td><code>dates.features.&#x3C;feature>.count</code><br>number<br><span data-gb-custom-inline data-tag="emoji" data-code="26a0">⚠️</span> Deprecated</td><td>The number of events corresponding to this <code>&#x3C;feature></code> for a given date.</td></tr><tr><td><code>dates.features.&#x3C;feature>.sum</code><br>number<br><span data-gb-custom-inline data-tag="emoji" data-code="26a0">⚠️</span> Deprecated</td><td>The sum of the values of this <code>&#x3C;feature></code> for a given date.</td></tr><tr><td><p><code>dates.phq_impact_sum</code></p><p>number<br><span data-gb-custom-inline data-tag="emoji" data-code="26a0">⚠️</span> Deprecated</p></td><td>The sum of all <code>phq_impact</code> features for a given date</td></tr><tr><td><p><code>dates.phq_spend_sum</code></p><p>number<br><span data-gb-custom-inline data-tag="emoji" data-code="26a0">⚠️</span> Deprecated</p></td><td>The sum of all <code>phq_spend</code> features for a given date</td></tr><tr><td><p><code>dates.phq_attendance_sum</code></p><p>number<br><span data-gb-custom-inline data-tag="emoji" data-code="26a0">⚠️</span> Deprecated</p></td><td>The sum of all <code>phq_attendance</code> features for a given date</td></tr><tr><td><p><code>dates.phq_rank_sum</code></p><p>number<br><span data-gb-custom-inline data-tag="emoji" data-code="26a0">⚠️</span> Deprecated</p></td><td>The sum of all <code>phq_rank</code> features for a given date</td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "model_version": "1.1.0",
    "version": 0,
    "dates": [
        {
            "date": "2021-01-01",
            "actual_demand": 5893.0,
            "baseline_demand": 1642.8505673206673,
            "remainder": 4250.149432679333,
            "impact_significance": "MEDIUM",
            "impact_significance_score": 2
        },
        {
            "date": "2021-01-02",
            "actual_demand": 4273.0,
            "baseline_demand": 4373.972146649381,
            "remainder": -100.9721466493811,
            "impact_significance": "NO_IMPACT",
            "impact_significance_score": 0
        },
    ]
...
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/correlate?date.gte=2022-01-01&date.lte=2022-12-31" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/correlate",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "date.gte": "2022-01-01",
        "date.lte": "2022-12-31"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [Beam Guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/beam-guides)

[^1]: An existing Beam Analysis ID.
