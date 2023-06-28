---
description: >-
  The calendar endpoint can be useful for indicating the number and impact of
  events happening on particular days making it easy to integrate event
  visibility into your existing calendar.
---

# Get Calendar of Events

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/events/calendar/
```

### Query Parameters

{% hint style="info" %}
This endpoint accepts the same query parameters as the Search Events endpoint. Please refer to the [Search Events](search-events.md) documentation for query parameters.
{% endhint %}

## Response

<details>

<summary>Example response</summary>

Each day in the calendar contains aggregate counts of all _active_ events for that day.

```json
{
  "count": 63,
  "next": null,
  "previous": null,
  "results": [
    {
      "date": "2015-12-24",
      "count": 38,
      "top_rank": 90,
      "top_local_rank": 49,
      "top_aviation_rank": 83,
      "rank_levels": {
        "1": 13,
        "2": 16,
        "3": 8,
        "4": 0,
        "5": 1
      },
      "local_rank_levels": {
        "1": 0,
        "2": 21,
        "3": 12,
        "4": 0,
        "5": 0
      },
      "aviation_rank_levels": {
        "1": 3,
        "2": 2,
        "3": 4,
        "4": 1,
        "5": 0
      },
      "categories": {
        "concerts": 13,
        "festivals": 11,
        "airport-delays": 6,
        "sports": 4,
        "politics": 1,
        "school-holidays": 1,
        "observances": 1,
        "daylight-savings": 1,
        "performing-arts": 1
      },
      "labels": {
        "concert": 13,
        "music": 13,
        "festival": 11,
        "airport": 6,
        "delay": 6,
        "sport": 4,
        "holiday": 2,
        "outdoor": 2,
        "daylight-savings": 1,
        "family": 1,
        "election": 1,
        "movie": 1,
        "observance": 1,
        "performing-arts": 1,
        "school": 1
      }
    },
    {
      "date": "2015-12-25",
      "count": 22,
      "top_rank": 90,
      "top_local_rank": 63,
      "top_aviation_rank": 81,
      "rank_levels": {
        "1": 9,
        "2": 10,
        "3": 1,
        "4": 1,
        "5": 1
      },
      "local_rank_levels": {
        "1": 0,
        "2": 8,
        "3": 6,
        "4": 1,
        "5": 0
      },
      "aviation_rank_levels": {
        "1": 5,
        "2": 6,
        "3": 2,
        "4": 2,
        "5": 0
      },
      "categories": {
        "festivals": 10,
        "sports": 5,
        "concerts": 3,
        "school-holidays": 1,
        "public-holidays": 1,
        "daylight-savings": 1,
        "conferences": 1
      },
      "labels": {
        "festival": 10,
        "sport": 5,
        "concert": 3,
        "music": 3,
        "holiday": 2,
        "outdoor": 2,
        "conference": 1,
        "daylight-savings": 1,
        "education": 1,
        "holiday-national": 1,
        "religion": 1,
        "school": 1
      }
    }
  ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/events/calendar/?active.gte=2015-12-24&active.lte=2015-12-25&active.tz=Pacific/Auckland&country=NZ \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/calendar/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "country": "NZ",
        "active.gte": "2015-12-24",
        "active.lte": "2015-12-25",
        "active.tz": "Pacific/Auckland"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
