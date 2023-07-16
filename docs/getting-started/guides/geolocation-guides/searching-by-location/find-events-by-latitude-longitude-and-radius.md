# Find Events by Latitude/Longitude and Radius

For this example, we will find conferences and expos that happened within a 2 mile radius of a specific location, in April 2018.

{% hint style="info" %}
It can be difficult working out a suitable radius around your location so to make it easier please use our [Suggested Radius API](../../../../api/suggested-radius/get-suggested-radius.md).
{% endhint %}

The Events endpoint supports the use of a [`within`](https://docs.predicthq.com/resources/events/#param-within) parameter to allow you to set specific latitude and longitude coordinates and search for events which occur within a radius from that point.

This can be used to find all the _conferences and expos_, `category=conferences,expos`, _within 2 miles_ of my location, `within=2mi@-37.80036998,144.9715749`, that happened during _April of 2018_,`active.gte=2018-04-01&active.lte=2018-04-30`

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "within" : "2mi@-37.80036998,144.9715749",
        "active.gte" : "2018-04-01",
        "active.lte" : "2018-04-30",
        "category" : "conferences,expos",
        "sort" : "rank"
    }
)

print(response.json())
```

A snippet of the results are shown below:

```json
{
  "count": 734,
  "results": [
    {
      "id": "SwBTYbfiAHYDdbkUi7",
      "title": "Great Debate: Political Interest Society vs History Society",
      "category": "conferences",
      ...
    }
  ]
}
```
