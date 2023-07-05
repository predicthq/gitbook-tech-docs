---
description: Search for events happening in an existing Saved Location.
---

# Search Events for a Saved Location

## Request

### HTTP Request

<pre class="language-apacheconf"><code class="lang-apacheconf">GET https://api.predicthq.com/v1/saved-locations/<a data-footnote-ref href="#user-content-fn-1">$location_id</a>/insights/events
</code></pre>

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td>location_id</td><td>An existing Saved Location ID.</td></tr></tbody></table>

### Query Parameters

<table><thead><tr><th width="219">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>date_range_type</code><br>string</td><td><p>Date range to fetch events for.<br><br>Currently the only supported date ranges are:</p><ul><li><code>next_90d</code></li></ul><p>E.g. <code>?date_range_type=next_90d</code></p></td></tr><tr><td><code>category</code><br>string</td><td>Comma-separated list of event categories to include.<br><br>Please refer to the <code>category</code> parameter in <a href="../events/search-events.md#query-parameters">Events API</a>.<br><br>E.g. <code>?category=sports,concerts</code></td></tr><tr><td><code>sort</code><br>string</td><td>Sort order for results.<br><br>Please refer to the <code>sort</code> parameter in Events API.<br><br>E.g. <code>?sort=phq_attendance</code></td></tr><tr><td><code>limit</code><br>number</td><td>The maximum number of results to return. The default limit is <code>10</code>.<br><br>E.g. <code>?limit=10</code></td></tr><tr><td><code>offset</code><br>number</td><td><p>The number of results to skip. The default is <code>0</code>.</p><p><br>E.g. <code>?offset=20</code></p></td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="190">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>count</code><br>number</td><td>Total number of results found.</td></tr><tr><td><code>results</code><br>array</td><td><p>List of results where each item is an Event.</p><p><br>Please refer to the response fields section in <a href="../events/search-events.md#response-fields">Search Events</a> for the structure of each record.</p></td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
  "count": 522,
  "results": [
    {
      "id": "8uPpWYtuLFKmdswgXL",
      "title": "Folsom Street Fair",
      "description": "The mission of Folsom Street Events is to create world-class leather and fetish events that unite the adult alternative lifestyle communities with safe venues for self-expression and exciting entertainment.",
      "entities": [
        {
          "formatted_address": "",
          "type": "event-group",
          "name": "Folsom Street Fair"
        }
      ],
      "place_hierarchies": [
        [
          "6295630",
          "6255149",
          "6252001",
          "5332921",
          "5391997",
          "5391959"
        ]
      ],
      "timezone": "America/Los_Angeles",
      "location": [
        -122.39231700000002,
        37.789024100000006
      ],
      "start": "2023-09-24T07:00:00Z",
      "end": "2023-09-25T06:59:59Z",
      "duration": 86399,
      "category": "festivals",
      "labels": [
        "entertainment",
        "festival"
      ],
      "phq_attendance": 400000,
      "rank": 100,
      "local_rank": 100,
      "geo": {
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                -122.39120568030553,
                37.7903973041606
              ],
              [
                -122.39089017614494,
                37.79064318446613
              ],
              [
                -122.39039841553388,
                37.790012176144934
              ],
              [
                -122.39342831969448,
                37.787650895839406
              ],
              [
                -122.39374382385508,
                37.78740501553388
              ],
              [
                -122.39423558446613,
                37.78803602385507
              ],
              [
                -122.39120568030553,
                37.7903973041606
              ]
            ]
          ]
        }
      },
      "state": "active",
      "predicted_event_spend": 51223933,
      "predicted_event_spend_industries": {
        "accommodation": 24096533,
        "hospitality": 20882800,
        "transportation": 6244600
      }
    },
    {
      "id": "6VSWpModQLPewdbDx2",
      "title": "Dreamforce",
      "description": "Dreamforce gathers the entire Salesforce community — our customers, partners, employees, and key stakeholders — for a fun family reunion.",
      "entities": [
        {
          "formatted_address": "800 Howard Street\nSan Francisco, CA 94103\nUnited States of America",
          "type": "venue",
          "name": "Moscone Center - West"
        },
        {
          "formatted_address": "",
          "type": "event-group",
          "name": "Dreamforce"
        }
      ],
      "place_hierarchies": [
        [
          "6295630",
          "6255149",
          "6252001",
          "5332921",
          "5391997",
          "5391959"
        ]
      ],
      "timezone": "America/Los_Angeles",
      "location": [
        -122.403445,
        37.783197
      ],
      "start": "2023-09-12T17:00:00Z",
      "end": "2023-09-15T01:00:00Z",
      "duration": 201600,
      "category": "conferences",
      "labels": [
        "business",
        "conference",
        "sales",
        "technology"
      ],
      "phq_attendance": 170000,
      "rank": 95,
      "local_rank": 100,
      "geo": {
        "geometry": {
          "type": "Point",
          "coordinates": [
            -122.403445,
            37.783197
          ]
        },
        "placekey": "222@5vg-7gv-3t9"
      },
      "state": "active",
      "predicted_event_spend": 163214070,
      "predicted_event_spend_industries": {
        "accommodation": 112651293,
        "hospitality": 42600912,
        "transportation": 7961865
      }
    },
    ...
  ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl --location 'https://api.predicthq.com/v1/saved-locations/0b6ZrOnTdB2Y7k4zC_9qBg/insights/events?date_range_type=next_90d&category=public-holidays%2Csports&sort=start' \
--header 'Authorization: Bearer TOKEN'
```
{% endtab %}

{% tab title="python" %}
```python
import requests

url = "https://api.predicthq.com/v1/saved-locations/0b6ZrOnTdB2Y7k4zC_9qBg/insights/events?date_range_type=next_90d&category=public-holidays,sports&sort=start"

payload={}
headers = {
  'Authorization': 'Bearer TOKEN'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```
{% endtab %}
{% endtabs %}

[^1]: An existing Saved Location ID.
