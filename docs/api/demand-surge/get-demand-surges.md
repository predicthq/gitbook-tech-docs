---
description: >-
  Identify dates with surges in demand caused by multiple events happening at
  the same time and location.
---

# Get Demand Surges

The Demand Surge API can be used to quickly scan a period of 90 days for abnormal increases in attendance for a given area. The API calculates the mean attendance for your requested location across 90 days, then returns all the dates where attendance is a certain number of standard deviations over the mean. This is represented by the `min_surge_intensity` parameter, which corresponds to the number of standard deviations the API will look for.

Once identified, demand surges can be further explored in our [Events](https://docs.predicthq.com/resources/events) or [Features](https://docs.predicthq.com/resources/features) APIs, to find the names, descriptions and details of the events that constitute the surges.

## Request

### HTTP Request

```
GET https://api.predicthq.com/v1/demand-surge/
```

### Query Parameters

<table><thead><tr><th width="210">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><strong>date_from</strong><br>date</td><td>The start date of the demand surge search window.<br><br>The accepted format for this parameter is <code>YYYY-MM-DD</code><br><br>E.g. <code>?date_from=2021-05-12</code></td></tr><tr><td><strong>date_to</strong><br>date</td><td>The end date of the demand surge search window.<br><br>The accepted format for this parameter is <code>YYYY-MM-DD</code><br><br>E.g. <code>?date_to=2021-08-10</code></td></tr><tr><td><strong>min_surge_intensity</strong><br>string</td><td><p>Filters out demand surges smaller than the minimum surge intensity provided.<br><br><strong>Possible values:</strong></p><ul><li><code>s</code> - Small</li><li><code>m</code> - Medium</li><li><code>l</code> - Large</li><li><code>xl</code> - Extra Large</li></ul><p>E.g. <code>?min_surge_intensity=m</code></p></td></tr><tr><td><strong>location.*</strong><br>string</td><td><p>Filters out demand surges not included in the location specified. Supports <code>place_id</code>, <code>origin</code> and <code>radius</code> suffixes.</p><ul><li><code>place_id</code>: Comma separated list (<code>&#x3C;place_id1>,&#x3C;place_id2></code>) representing the place ids of a location. It cannot be used with <code>origin</code> or <code>radius</code> suffixes.<br><br>E.g. <code>?location.place_id=2643743,2643744</code></li><li><code>origin</code>: Comma separated coordinate (<code>&#x3C;lat>,&#x3C;lon></code>) representing the centroid of a location. It must be used with <code>radius</code> suffix and cannot be used with <code>place_id</code> suffix.<br><br>E.g. <code>?location.origin=40.7128,74.0060</code></li><li><p><code>radius</code>: String representing the radius (<code>&#x3C;number>&#x3C;unit></code>) of a location . It must be used with <code>origin</code> suffix and cannot be used with <code>place_id</code> suffix.<br><br><strong>Possible units:</strong></p><ul><li><code>f</code> - Feet</li><li><code>mi</code> - Miles</li><li><code>m</code> - Meters</li><li><code>km</code> - Kilometers</li></ul><p>E.g. <code>?location.radius=100mi</code></p></li></ul></td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="249">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>count</strong><br>number</td><td>The number of identified demand surges given the search criteria.</td></tr><tr><td><strong>surge_dates</strong><br>array</td><td>An array of identified demand surges.</td></tr><tr><td><strong>date</strong><br>date</td><td>The date of the identified demand surge.</td></tr><tr><td><strong>phq_attendance_sum</strong><br>number</td><td>The sum of all attendance based features in the identified demand surge.</td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "count": 2,
    "surge_dates": [
        {
            "date": "2021-08-07",
            "phq_attendance_sum": 233930
        },
        {
            "date": "2021-08-08",
            "phq_attendance_sum": 213382
        }
    ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/demand-surge/?date_from=2021-05-12&date_to=2021-08-10&min_surge_intensity=m&location.place_id=2643743 \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/demand-surge/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "date_from": "2021-05-12",
        "date_to": "2021-08-10",
        "min_surge_intensity": "m",
        "location.place_id": "2643743"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
