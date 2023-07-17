# Working with Recurring Events

The Recurring Events feature provides a linkage between recurrences of the same event:

* Events that recur each year on the same day, such as Christmas Day.
* Events that recur each year (or month, or  other frequency) but change date and potentially location, such as the American Society of Haematology Annual Meeting.

As well as being able to see that an event is recurring, it’s also possible to find all recurrences of the same event.

{% hint style="info" %}
**Example Use Cases**

* **Demand Forecasting**: When analysing previous years transactions or bookings, you can align demand spikes with a recurring event and predict expected demand increases for future years.
* **Labour Optimization**: Knowing why you were busy last year and planning your resource requirements for the same period next year. What if the event changes location? Recurring Events allows you to get this visibility and plan accordingly.
{% endhint %}

Recurring Events are represented as an Entity of type `event-group` with recurring info in iCalendar recurring RRULE format.

Below is an example event with a recurring `event-group` Entity:

```json
{
  "count": 1,
  "results": [
    {
      "id": "3HieM5mavYqPikiHPw",
      "title": "ASH Annual Meeting",
      "category": "conferences",
      "entities": [
        {
          "entity_id": "vAtN2UDcxySFtZFwLRvqcN",
          "name": "ASH Annual Meeting",
          "type": "event-group",
          "category": "conferences",
          "labels": [
            "business",
            "conference",
            "event-group",
            "expo",
            "recurring"
          ],
          "description": "The American Society of Hematology (ASH) Annual Meeting & Exposition provides an invaluable educational experience and the opportunity to review thousands of scientific abstracts highlighting updates in the hottest topics in hematology.",
          "recurring": {
            "ical": "DTSTART;VALUE=DATE:20141206\nDURATION:P4D\nRRULE:FREQ=YEARLY;INTERVAL=1"
          }
        }
      ],
      ...
    }
  ]
}
```

## Find all Instances of a Recurring Event

The `entity.id` query parameter allows you to find all Events that are linked to the specified Entity ID. This example uses the "ASH Annual Meeting" recurring `event-group` Entity ID to find all instances of the Event.

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "entity.id" : "vAtN2UDcxySFtZFwLRvqcN",
        "sort" : "start"
    }
)

print(response.json())
```

A snippet of the results is shown below:

```json
{
  "count": 9,
  "results": [
    {
      "id": "6NYlQ7BdJdLy",
      "title": "ASH Annual Meeting",
      "start": "2014-12-06T08:00:00Z",
      "end": "2014-12-10T07:59:59Z",
      ...
    },
    {
      "id": "DGMn5WdRKg6R",
      "title": "ASH Annual Meeting",
      "start": "2015-12-05T05:00:00Z",
      "end": "2015-12-09T04:59:59Z",
      ...
    },
    {
      "id": "l3DQOqMooNQJ",
      "title": "ASH Annual Meeting",
      "start": "2016-12-03T08:00:00Z",
      "end": "2016-12-07T07:59:59Z",
      ...
    },
    {
      "id": "CMAXh5scsAcFyMhgGj",
      "title": "ASH Annual Meeting",
      "start": "2017-12-09T05:00:00Z",
      "end": "2017-12-13T04:59:59Z",
      ...
    },
    {
      "id": "K9z9hS3sXqjH3SmYwq",
      "title": "ASH Annual Meeting",
      "start": "2018-12-01T08:00:00Z",
      "end": "2018-12-05T07:59:59Z",
      ...
    },
    {
      "id": "2RxTdCucMNcLZSsEqW",
      "title": "ASH Annual Meeting",
      "start": "2019-12-07T05:00:00Z",
      "end": "2019-12-11T04:59:59Z",
      ...
    },
    {
      "id": "XDs5aBowsAAopqp5yy",
      "title": "ASH Annual Meeting",
      "start": "2021-12-11T05:00:00Z",
      "end": "2021-12-15T04:59:59Z",
      ...
    },
    {
      "id": "3HieM5mavYqPikiHPw",
      "title": "ASH Annual Meeting",
      "start": "2022-12-10T06:00:00Z",
      "end": "2022-12-14T05:59:59Z",
      ...
    },
    {
      "id": "FFRgbLAfquTFajD3Xq",
      "title": "ASH Annual Meeting and Exposition",
      "start": "2023-12-09T19:00:00Z",
      "end": "2023-12-12T22:00:00Z",
      ...
    }
  ]
}
```

## Find a Specific Recurrence of an Event

In this example we will find the 2019 instance of the "ASH Annual Meeting".

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "entity.id" : "vAtN2UDcxySFtZFwLRvqcN",
        "start.gte" : "2019-01-01",
        "start.lte": "2019-12-31"
    }
)

print(response.json())
```

A snippet of the results is shown below:

```json
{
  "count": 1,
  "results": [
    {
      "id": "2RxTdCucMNcLZSsEqW",
      "title": "ASH Annual Meeting",
      "description": "The American Society of Hematology (ASH) Annual Meeting & Exposition provides an invaluable educational experience and the opportunity to review thousands of scientific abstracts highlighting updates in the hottest topics in hematology.",
      "category": "conferences",
      "labels": [
        "conference",
        "expo",
        "health",
        "medical"
      ],
      "rank": 78,
      "local_rank": 100,
      "phq_attendance": 25000,
      "entities": [
        {
          "entity_id": "Urecg72DAWZw5abb9ZExWh",
          "name": "Orange County Convention Center",
          "type": "venue",
          "formatted_address": "9800 International Drive\nOrlando, FL 32819\nUnited States of America"
        },
        {
          "entity_id": "vAtN2UDcxySFtZFwLRvqcN",
          "name": "ASH Annual Meeting",
          "type": "event-group",
          "category": "conferences",
          "labels": [
            "business",
            "conference",
            "event-group",
            "expo",
            "recurring"
          ],
          "description": "The American Society of Hematology (ASH) Annual Meeting & Exposition provides an invaluable educational experience and the opportunity to review thousands of scientific abstracts highlighting updates in the hottest topics in hematology.",
          "recurring": {
            "ical": "DTSTART;VALUE=DATE:20141206\nDURATION:P4D\nRRULE:FREQ=YEARLY;INTERVAL=1"
          }
        }
      ],
      "duration": 345599,
      "start": "2019-12-07T05:00:00Z",
      "end": "2019-12-11T04:59:59Z",
      "updated": "2023-07-07T02:57:03Z",
      "first_seen": "2019-02-21T00:24:36Z",
      "timezone": "America/New_York",
      "location": [
        -81.4697992,
        28.4245227
      ],
      "geo": {
        "geometry": {
          "coordinates": [
            -81.4697992,
            28.4245227
          ],
          "type": "Point"
        },
        "placekey": "zzw-224@8fy-8hr-pgk"
      },
      "scope": "locality",
      "country": "US",
      "place_hierarchies": [
        [
          "6295630",
          "6255149",
          "6252001",
          "4155751",
          "4167060",
          "4178397"
        ],
        [
          "6295630",
          "6255149",
          "6252001",
          "4155751",
          "4167218",
          "4160983"
        ]
      ],
      "state": "active",
      "private": false,
      "predicted_event_spend": 19879000,
      "predicted_event_spend_industries": {
        "accommodation": 14760000,
        "hospitality": 4179000,
        "transportation": 940000
      }
    }
  ]
}
```
