# Find Broadcasts by County Place ID

For this example we want to find all broadcasts televised in two counties in California during November 2020.

The `location.place_id` parameter allows us to filter live sports events by their broadcast locations. For the counties in our example, we will use `location.place_id=5368381,5391832`, which are the respective Place IDs for Los Angeles County and San Diego County in California.

These Place IDs were found using the [Places API](broken-reference). We provide a CSV file of broadcast counties to download, to make it easier to discover the `place_id` for all counties and states in the US.

{% file src="../../../../api/.gitbook/assets/broadcast-events-place-mapping.csv" %}

We can also use the `start.*` parameters to filter broadcasts by time. For the time range in our example, we will use `start.gte=2020-11-01` and `start.lte=2020-11-30`. Using `start.tz=America/Los_Angeles` will treat the parameter’s start dates and times in the America/Los\_Angeles time zone, otherwise the parameter dates and times will be treated as UTC.

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/broadcasts/",
    headers={
        "Accept": "application/json",
        "Authorization": "Bearer $ACCESS_TOKEN"
    },
    params={
        "location.place_id": "5368381,5391832",
        "start.gte": "2020-11-01",
        "start.lte": "2020-11-30",
        "start.tz": "America/Los_Angeles"
    }
)

print(response.json())
```

A snippet of the results are shown below:

```json
{
  "count": 501,
  "next": "https://api.predicthq.com/v1/broadcasts/?location.place_id=5368381%2C5391832&start.gte=2020-11-01&start.lte=2020-11-30&start.tz=America%2FLos_Angeles&offset=10",
  "previous": null,
  "overflow": false,
  "results": [
    {
      "broadcast_id": "56aJFMBmajvnTjM3DUB4JS",
      "dates": {
        "start": "2020-11-01T18:00:00Z",
        "start_local": "2020-11-01T10:00:00",
        "timezone": "America/Los_Angeles"
      },
      "location": {
        "geopoint": {
          "lon": -118.26102,
          "lat": 34.19801
        },
        "place_hierarchies": [
          [
            "6295630",
            "6255149",
            "6252001",
            "5332921",
            "5368381"
          ]
        ],
        "places": [
          {
            "place_id": "5368381",
            "type": "county",
            "name": "Los Angeles County",
            "county": "Los Angeles County",
            "region": "California",
            "country": "US"
          }
        ],
        "country": "US"
      },
      "phq_viewership": 566891,
      "event": {
        "event_id": "24HwKWjyPw3xLBhGza",
        "title": "Los Angeles Rams vs Miami Dolphins",
        "category": "sports",
        "labels": [
          "american-football",
          "nfl",
          "sport"
        ],
        ...
      }
    },
    ...
  ]
}
```

In this example, the Broadcasts API found 501 broadcasts. The snippet shows one of the broadcasts: an NFL game where 56,6891 people will watch the broadcast.
