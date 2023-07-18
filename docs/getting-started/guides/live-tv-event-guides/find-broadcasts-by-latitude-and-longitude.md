# Find Broadcasts by Latitude and Longitude

For this example we want to find all broadcasts televised in the county that corresponds to a geopoint (latitude and longitude coordinates).

The `location.origin` parameter allows us to filter broadcasts by a geopoint, such as the location of a store. The Broadcasts API returns broadcasts for the county the geopoint is located in. For our example, we have a store located in Union Square, San Francisco, which has a latitude of `37.7879` and longitude of `-122.4097`. So we will use `location.origin=37.7879,-122.4097`. Using these coordinates will return broadcasts for San Francisco County - the county which Union Square is in.

We can also use the `sort` parameter to order the broadcasts returned by the API. For our example, we will use `sort=-start` to return the most recently televised broadcasts first.

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/broadcasts/",
    headers={
        "Accept": "application/json",
        "Authorization": "Bearer $ACCESS_TOKEN"
    },
    params={
        "location.origin": "37.7879,-122.4097",
        "sort": "-start"
    }
)

print(response.json())
```

A snippet of the results are shown below:

```json
{
  "count": 34069,
  "next": "https://api.predicthq.com/v1/broadcasts/?location.origin=37.7879%2C-122.4097&sort=-start&offset=10",
  "previous": null,
  "overflow": false,
  "results": [
    {
      "broadcast_id": "389i57kxDfXJLeyiggv3N3c",
      "updated": "2023-07-16T04:43:08Z",
      "first_seen": "2023-07-16T02:24:50Z",
      "dates": {
        "start": "2023-07-29T23:00:00Z",
        "start_local": "2023-07-29T16:00:00",
        "timezone": "America/Los_Angeles"
      },
      "location": {
        "geopoint": {
          "lon": -122.4425,
          "lat": 37.77823
        },
        "place_hierarchies": [
          [
            "6295630",
            "6255149",
            "6252001",
            "5332921",
            "5391997"
          ]
        ],
        "places": [
          {
            "place_id": "5391997",
            "type": "county",
            "name": "San Francisco County",
            "county": "City and County of San Francisco",
            "region": "California",
            "country": "US"
          }
        ],
        "country": "US"
      },
      "phq_viewership": 7773,
      "record_status": "active",
      "broadcast_status": "scheduled",
      "event": {
        "event_id": "F8ueP8SKbHn4xi7kW3",
        "title": "New York Yankees vs Baltimore Orioles",
        "category": "sports",
        "labels": [
          "baseball",
          "mlb",
          "sport"
        ],
        "dates": {
          "start": "2023-07-29T23:05:00Z",
          "start_local": "2023-07-29T19:05:00",
          "predicted_end_local": "2023-07-29T21:55:00",
          "timezone": "America/New_York"
        },
        "location": {
          "geopoint": {
            "lon": -76.61994529999998,
            "lat": 39.2840184
          },
          "place_hierarchies": [
            [
              "6295630",
              "6255149",
              "6252001",
              "4361885",
              "4347820",
              "4347778"
            ]
          ],
          "country": "US"
        },
        "entities": [
          {
            "entity_id": "VQXSiWZ85iHaP9QEZ25Ja6",
            "type": "organisation",
            "name": "New York Yankees",
            "formatted_address": "Bronx\nUnited States of America"
          },
          {
            "entity_id": "diNLbJSNy7Zh6EgSJCe6yw",
            "type": "organisation",
            "name": "Baltimore Orioles",
            "formatted_address": "Baltimore, MD 21201\nUnited States of America"
          },
          {
            "entity_id": "5QFtRcZrNF89kaPUwNS5pU",
            "type": "venue",
            "name": "Oriole Park at Camden Yards",
            "formatted_address": "333 West Camden Street\nBaltimore, MD 21201\nUnited States of America"
          }
        ],
        "phq_attendance": 48876,
        "phq_rank": 84,
        "local_rank": 97
      }
    },
    ...
  ]
}
```
