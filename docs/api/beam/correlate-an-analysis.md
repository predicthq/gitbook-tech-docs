---
description: >-
  Retrieve results of the correlation of our event data with your transactional
  demand data.
---

# Correlate an Analysis

## Request

### HTTP Request

<pre class="language-apacheconf"><code class="lang-apacheconf">GET https://api.predicthq.com/v1/beam/analyses/<a data-footnote-ref href="#user-content-fn-1">$analysis_id</a>/correlate
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>analysis_id</code></td><td>An existing Beam Analysis ID.</td></tr></tbody></table>

### Query Parameters

<table><thead><tr><th width="185">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>date.*</code><br>string<br><em>required</em></td><td>Filters out correlation data not included in the date range. The <code>date</code> parameter must have an upper (<code>lt</code> or <code>lte</code>) and lower (<code>gt</code> or <code>gte</code>) bound suffix.<br><br>The accepted format for this parameter is <code>YYYY-MM-DD</code><br><br>E.g. <code>?date.gt=2017-01-01&#x26;date.lte=2017-12-01</code></td></tr><tr><td><code>limit</code><br>number<br>optional</td><td>Limits the length of the Beam decomposition list returned. The default <code>limit</code> is <code>30</code>.<br><br>E.g. <code>?limit=20</code></td></tr><tr><td><code>offset</code><br>number<br>optional</td><td>Specifies starting offset of the Beam decomposition list returned. The default <code>offset</code> is <code>0</code>.<br><br>E.g. <code>?offset=3</code></td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="393">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>count</code><br>number</td><td>The number of Beam decomposition dates returned.</td></tr><tr><td><code>dates</code><br>array</td><td>An array of Beam decomposition dates.</td></tr><tr><td><code>dates.date</code><br>date</td><td>The date of the Beam decomposition.</td></tr><tr><td><code>dates.actual_demand</code><br>number</td><td>The actual demand for a given date.</td></tr><tr><td><code>dates.baseline_demand</code><br>number</td><td>The expected demand for a given date.</td></tr><tr><td><code>dates.remainder</code><br>number</td><td>The difference between the <code>actual_demand</code> and the <code>baseline_demand</code> for a given date. This value may be positive or negative.</td></tr><tr><td><code>dates.impact_significance</code><br>string</td><td><p>Enum specifying how unusual the <code>remainder</code> is for a given date.<br><br><strong>Possible values:</strong></p><ul><li><code>NO_IMPACT</code></li><li><code>WEAK</code></li><li><code>MEDIUM</code></li><li><code>SIGNIFICANT</code></li></ul></td></tr><tr><td><code>dates.impact_significance_score</code><br>number</td><td><p>Number specifying how unusual the <code>remainder</code> is for a given date. This value maps to <code>impact_significance</code>.<br><br><strong>Possible values:</strong></p><ul><li><code>0</code></li><li><code>1</code></li><li><code>2</code></li><li><code>3</code></li></ul></td></tr><tr><td><code>dates.impact</code><br>number</td><td>The total impact of all the event categories for a given date.</td></tr><tr><td><code>dates.categories_impact</code><br>object</td><td>A json object containing all impact categories for a given date.</td></tr><tr><td><code>dates.categories_impact.&#x3C;category></code><br>object</td><td>A json object containing impact information for the <code>&#x3C;category></code> for a given date.</td></tr><tr><td><code>dates.categories_impact.&#x3C;category>.count</code><br>number</td><td>The number of events in this <code>&#x3C;category></code> for a given date.</td></tr><tr><td><code>dates.categories_impact.&#x3C;category>.impact</code><br>number</td><td>The impact of events in this <code>&#x3C;category></code> for a given date.</td></tr><tr><td><code>dates.categories_impact.&#x3C;category>.percentage</code><br>number</td><td>The impact percentage composition of this <code>&#x3C;category></code> to the total impact of all categories for a given date.</td></tr><tr><td><code>categories_impact</code><br>object</td><td>A json object containing all impact categories for the Beam decomposition date range returned.</td></tr><tr><td><code>categories_impact.&#x3C;category>.count</code><br>number</td><td>The number of events in this <code>&#x3C;category></code> for the Beam decomposition date range returned.</td></tr><tr><td><code>categories_impact.&#x3C;category>.impact</code><br>number</td><td>The impact of events in this <code>&#x3C;category></code> for the Beam decomposition date range returned.</td></tr><tr><td><code>categories_impact.&#x3C;category>.percentage</code><br>number</td><td>The impact percentage composition of this <code>&#x3C;category></code> to the total impact of all categories for the Beam decomposition date range returned.</td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "model_version": "0.5.0",
    "version": 0,
    "dates": [
        {
            "date": "2020-01-01",
            "actual_demand": 4637.25,
            "baseline_demand": 6768.664221719573,
            "remainder": -2131.414221719573,
            "impact_significance": "SIGNIFICANT",
            "impact_significance_score": 3,
            "impact": 0.0,
            "categories_impact": {
                "community": {
                    "count": 0,
                    "impact": 0,
                    "percentage": 0.0
                },
                "concerts": {
                    "count": 0,
                    "impact": 0,
                    "percentage": 0.0
                },
                "festivals": {
                    "count": 0,
                    "impact": 0,
                    "percentage": 0.0
                },
                "performing_arts": {
                    "count": 0,
                    "impact": 0,
                    "percentage": 0.0
                },
                "sports": {
                    "count": 0,
                    "impact": 0,
                    "percentage": 0.0
                },
                "conferences": {
                    "count": 0,
                    "impact": 0,
                    "percentage": 0.0
                },
                "expos": {
                    "count": 0,
                    "impact": 0,
                    "percentage": 0.0
                },
                "public_holidays": {
                    "count": 1,
                    "impact": 0,
                    "percentage": 0.0
                },
                "school_holidays": {
                    "count": 1,
                    "impact": 0,
                    "percentage": 0.0
                },
                "observances": {
                    "count": 0,
                    "impact": 0,
                    "percentage": 0.0
                }
            }
        }
    ],
    "count": 1,
    "categories_impact": {
        "community": {
            "count": 0,
            "impact": 0,
            "percentage": 0.0
        },
        "concerts": {
            "count": 0,
            "impact": 0,
            "percentage": 0.0
        },
        "festivals": {
            "count": 4,
            "impact": 11606.0,
            "percentage": 17.201719282644138
        },
        "performing_arts": {
            "count": 0,
            "impact": 0,
            "percentage": 0.0
        },
        "sports": {
            "count": 6,
            "impact": 16366.0,
            "percentage": 24.25670668445235
        },
        "conferences": {
            "count": 0,
            "impact": 0,
            "percentage": 0.0
        },
        "expos": {
            "count": 14,
            "impact": 39498.0,
            "percentage": 58.54157403290351
        },
        "public_holidays": {
            "count": 79,
            "impact": 0,
            "percentage": 0.0
        },
        "school_holidays": {
            "count": 387,
            "impact": 0,
            "percentage": 0.0
        },
        "observances": {
            "count": 10,
            "impact": 0,
            "percentage": 0.0
        }
    }
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/correlate?date.gte=2022-01-01&date.lte=2022-12-31 \
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

* [Beam Data Science Guide](../../getting-started/guides/beam-guides/beam-data-science-guide.md)

[^1]: An existing Beam Analysis ID.
