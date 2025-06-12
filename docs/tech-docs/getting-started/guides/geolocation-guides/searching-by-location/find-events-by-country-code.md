# Find Events by Country Code

For this example, we will find public and school holidays for the United States of America in 2018.

The Events endpoint allows you to specify a particular country by using the `country` parameter. This parameter supports the standard 2 character ISO 3166-1 country codes. A full list of these codes can be [found here](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

We use this parameter to find all _holidays_, `category=public-holidays,school-holidays`, which are happening in the _United States of America (US)_, `country=US`, in _2018_, `active.gte=2018-01-01&active.lte=2018-12-31`.

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "country" : "US",
        "active.gte" : "2018-01-01",
        "active.lte" : "2018-12-31",
        "category" : "public-holidays,school-holidays"
    }
)

print(response.json())
```

One thing you might notice in the results are multiple events with the same title - this can happen when an event applies to multiple locations or occurs at different times. For example, a public holiday might apply to a number of states but not to the whole country - in this case there would be an event per state. A good indication of what area the event applies to is the `scope` field in the event information. If the event applies to the whole country this value will be `country`, otherwise it may be `region`.

A snippet of the results are shown below:

```json
{
  "count": 468,
  "results": [
    {
      "id": "b6ca61ff6041c05d1e",
      "title": "New Year's Eve",
      "category": "public-holidays",
      ...
    }
  ]
}
```

That’s helpful, but doesn’t tell us which region the event applies to. Using the `place_hierarchies` field in event results we can get more detailed information about the place(s) the event applies to. Each hierarchy is an array of Place IDs, e.g. `["6295630","6255149","6252001","5165418"]` which is _Earth > North America > United States > Ohio_.

We can use the Places endpoint to find information about the Place IDs mentioned in the hierarchy or use the [Understanding Place Hierarchies](../understanding-place-hierarchies.md) guide.
