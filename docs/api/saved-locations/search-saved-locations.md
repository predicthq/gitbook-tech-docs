---
description: Search for an existing Saved Location.
---

# Search Saved Locations

## Request

### HTTP Request

```
GET https://api.predicthq.com/v1/saved-locations
```

### Query Parameters

<table><thead><tr><th width="186">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>location_id</code><br>string</td><td><p>A comma-separated string consisting of a list of 1 or more location_id's.</p><p><br>E.g. <code>?location_id=6TxvEapQeDzq9y_UKVRQCQ</code></p></td></tr><tr><td><code>q</code><br>string</td><td><p>A full-text search query that searches across the following fields:</p><ul><li><code>name</code></li><li><code>description</code></li><li><code>location_code</code></li><li><code>formatted_address</code></li><li><code>labels</code></li></ul><p><br>E.g. <code>q=alabama</code></p></td></tr><tr><td><code>sort</code><br>string</td><td><p>A comma-separated list of fields to sort results by. Use the <code>-</code> prefix to sort descending.</p><p><br>Possible values:</p><ul><li><code>name</code> - Sort by name A-Z</li><li><code>-name</code> - Sort by name Z-A</li><li><code>created</code> - Sort by created date oldest to newest</li><li><code>-created</code> - Sort by created date newest to oldest</li><li><code>updated</code> - Sort by updated date earliest to latest</li><li><code>-updated</code> - Sort by updated date latest to earliest</li><li><code>address</code> - Sort by address A-Z</li><li><code>-address</code> - Sort by address Z-A</li></ul><p>You can also sort by the summary insight values. Summary insights are calculated for different date ranges (currently only next 90 days has been implemented) and you can choose which date range to sort by. These follow the following format: </p><pre><code>&#x3C;date_range_type>.&#x3C;summary_insight_key>
</code></pre><p>For example, below are the sort options for the summary insights calculated for the next 90d:</p><ul><li><code>next_90d.phq_attendance_sum</code></li><li><code>next_90d.attended_event_count</code></li><li><code>next_90d.non_attended_event_count</code></li><li><code>next_90d.unscheduled_event_count</code></li><li><code>next_90d.demand_surge_count</code></li></ul><p>You can prefix these with a minus sign <code>-</code> to reverse the order.</p><p><br>E.g.: <code>?sort=-created</code></p></td></tr><tr><td><code>limit</code><br>string</td><td><p>The maximum number of results to return. The default limit is 10.</p><p><br>E.g. <code>?limit=50</code></p></td></tr><tr><td><code>offset</code><br>string</td><td><p>Used for paging. The number of results to skip. The default is 0.</p><p><br>E.g. <code>?offset=20</code></p></td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="190">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>count</code><br>number</td><td>Total number of results found.</td></tr><tr><td><code>locations</code><br>array</td><td><p>List of results where each item is a Saved Location.</p><p><br>Please refer to the response fields section in <a href="get-a-saved-location.md#response-fields">Get a Saved Location</a> for the structure of each record.</p></td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
  "count": 1,
  "locations": [
    {
      "location_id": "h8LbiiiTOXsxSAI0p3wEIg",
      "create_dt": "2023-03-27T22:07:00+00:00",
      "update_dt": "2023-07-03T04:31:38+00:00",
      "enrich_dt": "2023-07-03T04:31:39+00:00",
      "insights_dt": "2023-07-03T04:31:40+00:00",
      "name": "My Parking Building",
      "labels": [
          "parking"
      ],
      "geojson": {
          "type": "Feature",
          "properties": {
              "radius": 0.9,
              "radius_unit": "mi"
          },
          "geometry": {
              "type": "Point",
              "coordinates": [
                  -122.40152,
                  37.7869
              ]
          }
      },
      "formatted_address": "666 Mission St, San Francisco, CA 94105, USA",
      "places": [
          {
              "place_id": 5391959,
              "type": "locality",
              "name": "San Francisco",
              "county": "City and County of San Francisco",
              "region": "California",
              "country": "US",
              "geojson": {
                  "type": "Feature",
                  "geometry": {
                      "type": "Point",
                      "coordinates": [
                          -122.41942,
                          37.77493
                      ]
                  }
              }
          }
      ],
      "summary_insights": [
          {
              "date_range": {
                  "type": "next_90d",
                  "start_dt": "2023-07-03T04:31:40+00:00",
                  "end_dt": "2023-10-01T04:31:40+00:00"
              },
              "phq_attendance_sum": 2646606,
              "attended_event_count": 519,
              "non_attended_event_count": 85,
              "unscheduled_event_count": 0
          }
      ],
      "subscription_valid_types": [
          "events"
      ],
      "status": "active"
    }
  ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl --location 'https://api.predicthq.com/v1/saved-locations?q=alabama&limit=50' \
--header 'Authorization: Bearer TOKEN'
```
{% endtab %}

{% tab title="python" %}
```python
import requests

url = "https://api.predicthq.com/v1/saved-locations?q=alabama&limit=50"

payload={}
headers = {
  'Authorization': TOKEN
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```
{% endtab %}
{% endtabs %}
