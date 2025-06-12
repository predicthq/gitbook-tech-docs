---
description: >-
  Identify dates with surges in demand caused by multiple events happening at
  the same time and location.
---

# Get Demand Surges

The Demand Surge API can be used to quickly scan a period of 90 days for abnormal increases in attendance for a given area. The API calculates the mean attendance for your requested location over the next 90 days after the `date_from` date and returns all the dates where attendance is a certain number of standard deviations over the mean. This is represented by the `min_surge_intensity` parameter, that corresponds to the number of standard deviations the API will look for.

Once you have identified the dates with the surge in demand, you can use:

* Our [Events API](../events/search-events.md) to find the names, descriptions, locations, and other details of the events that constitute the surges.
* Our [Features API](../features/get-features.md) to get Machine Learning features for events in your searched date range.

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/demand-surge/
```

### Query Parameters

<table><thead><tr><th width="246">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>date_from</code><br>date</td><td>The beginning of the demand surge search window. The demand surge will be <strong>looked up over the next 90 days</strong> after the date you provide for the <code>date_from</code> parameter.<br><br>The accepted format for this parameter is <code>YYYY-MM-DD</code><br><br>E.g. <code>?date_from=2021-05-12</code></td></tr><tr><td><code>min_surge_intensity</code><br>string</td><td><p>Filters out demand surges smaller than the minimum surge intensity provided.<br><br><strong>Possible values:</strong></p><ul><li><code>s</code> - Small</li><li><code>m</code> - Medium</li><li><code>l</code> - Large</li><li><code>xl</code> - Extra Large</li></ul><p>E.g. <code>?min_surge_intensity=m</code></p></td></tr><tr><td><code>location.*</code><br>string</td><td><p>The location to use in the demand surge search window. Supports <code>place_id</code>OR <code>origin</code> and <code>radius</code> suffixes.</p><ul><li><code>place_id</code>: A comma-separated list in the format representing the place ids of a location in the format <code>&#x3C;place_id1>,&#x3C;place_id2></code> . It cannot be used with <code>origin</code> or <code>radius</code> suffixes.<br><br>E.g. <code>?location.place_id=2643743,2643744</code></li></ul><ul><li><code>origin</code>: A comma-separated coordinate (<code>&#x3C;lat>,&#x3C;lon></code>) representing the centroid of a location. It must be used with <code>radius</code> suffix and cannot be used with <code>place_id</code> suffix.<br><br>E.g. <code>?location.origin=40.7128,74.0060</code></li></ul><ul><li><p><code>radius</code>: A string representing the radius for the demand surge, in the format <code>&#x3C;radius_value>&#x3C;radius_unit></code>, where <code>&#x3C;radius_value></code> is an integer or a float number up to 2 decimal places and <code>&#x3C;radius_unit></code> is one of:</p><ul><li><code>m</code> - meters</li><li><code>km</code> - kilometers</li><li><code>ft</code> - feet</li><li><code>mi</code> - miles<br></li></ul><p>E.g. <code>?location.radius=100mi</code></p></li></ul></td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="249">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>count</code><br>number</td><td>The number of identified demand surges given the search criteria.</td></tr><tr><td><code>surge_dates</code><br>array</td><td>An array of identified demand surges.</td></tr><tr><td><code>date</code><br>date</td><td>The date of the identified demand surge.</td></tr><tr><td><code>phq_attendance_sum</code><br>number</td><td>The sum of all attendance based features in the identified demand surge.</td></tr></tbody></table>

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
curl -X GET "https://api.predicthq.com/v1/demand-surge/?date_from=2021-05-12&min_surge_intensity=m&location.place_id=2643743" \
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
        "min_surge_intensity": "m",
        "location.place_id": "2643743"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
