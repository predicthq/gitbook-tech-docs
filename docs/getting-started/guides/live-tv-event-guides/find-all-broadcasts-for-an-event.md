# Find all Broadcasts for an Event

In this example we want to find the broadcasts for the Super Bowl game, New England Patriots vs Los Angeles Rams, played on February 3rd 2019.

To find broadcasts for an event, we can use the `event.event_id` parameter. This parameter allows us to retrieve broadcast records for each county the game has viewership in. So, for a specific game televised nation-wide, the API would return over 3000 broadcast records with viewership per county.

The 2019 Super Bowl game's `event_id` is `ePQLUqbPnMn3mQhe35`, so we need to filter broadcasts using `event.event_id=ePQLUqbPnMn3mQhe35`. The `event_id` was found using our Events API. See our [Events API documentation](https://docs.predicthq.com/resources/events) to discover how to query for other sports events.

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/broadcasts/",
    headers={
        "Accept": "application/json",
        "Authorization": "Bearer $ACCESS_TOKEN"
    },
    params={
        "event.event_id": "ePQLUqbPnMn3mQhe35"
    }
)

print(response.json())
```

A snippet of the results is shown below:

```json
{
  "count": 3055,
  "next": "https://api.predicthq.com/v1/broadcasts/?event.event_id=ePQLUqbPnMn3mQhe35&offset=10",
  "previous": null,
  "overflow": false,
  "results": [
    {
      "broadcast_id": "RjiUnFcNRcZMdDaUX5vJkR",
      "updated": "2021-09-22T03:57:50Z",
      "first_seen": "2020-11-09T19:40:02Z",
      "dates": {
        "start": "2019-02-03T23:30:00Z",
        "start_local": "2019-02-03T17:30:00",
        "timezone": "America/Chicago"
      },
      "location": {
        "geopoint": {
          "lon": -96.15448,
          "lat": 41.29535
        },
        "place_hierarchies": [
          [
            "6295630",
            "6255149",
            "6252001",
            "5073708",
            "5067114"
          ]
        ],
        "places": [
          {
            "place_id": "5067114",
            "type": "county",
            "name": "Douglas County",
            "county": "Douglas County",
            "region": "Nebraska",
            "country": "US"
          }
        ],
        "country": "US"
      },
      "phq_viewership": 178573,
      "record_status": "active",
      "broadcast_status": "scheduled",
      "event": {
        "event_id": "ePQLUqbPnMn3mQhe35",
        "title": "Super Bowl - New England Patriots vs Los Angeles Rams",
        "category": "sports",
        "labels": [
          "american-football",
          "nfl",
          "sport"
        ],
        "dates": {
          "start": "2019-02-03T23:30:00Z",
          "start_local": "2019-02-03T18:30:00",
          "predicted_end_local": "2019-02-03T21:40:00",
          "timezone": "America/New_York"
        },
        "location": {
          "geopoint": {
            "lon": -84.40089219999999,
            "lat": 33.75540290000001
          },
          "place_hierarchies": [
            [
              "6295630",
              "6255149",
              "6252001",
              "4197000",
              "4196508",
              "4195207"
            ],
            [
              "6295630",
              "6255149",
              "6252001",
              "4197000",
              "4191014",
              "4180439"
            ]
          ],
          "country": "US"
        },
        "entities": [
          {
            "entity_id": "Bp2eZ273idefSEQcL8hYJ6",
            "type": "organisation",
            "name": "Los Angeles Rams",
            "formatted_address": "Inglewood, CA 90301\nUnited States of America"
          },
          {
            "entity_id": "cqqvB7RP56CkMANBy9pVMW",
            "type": "organisation",
            "name": "New England Patriots",
            "formatted_address": "Foxborough, MA 02035\nUnited States of America"
          },
          {
            "entity_id": "LJZrFdZT95u9qZ6p4q4ZuK",
            "type": "venue",
            "name": "Mercedes-Benz Stadium",
            "formatted_address": "1 AMB Dr NW\nAtlanta, GA 30313\nUnited States of America"
          }
        ],
        "phq_attendance": 70081,
        "phq_rank": 87,
        "local_rank": 100
      }
    },
    ...
  ]
}
```
