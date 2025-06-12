# Find Events by Place ID

For this example, we want to find all the sports events that happened in Nottingham, England in March of 2018.

First let’s find the Nottingham Place ID by making a request to the Places endpoint:

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/places/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "q": "Nottingham,England"
    }
)

print(response.json())
```

The first result in the response (shown below) is the correct location we want:

```json
{
    "id": "2641170",
    "type": "locality",
    "name": "Nottingham",
    "county": "Nottingham",
    "region": "England",
    "country": "United Kingdom",
    "country_alpha2": "GB",
    "country_alpha3": "GBR",
    "location": [
        -1.15047,
        52.9536
    ]
}
```

Now we take the Place ID for Nottingham returned above and use it to search for Events happening in that location.

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "place.scope" : "2641170",  # Nottingham Place ID
        "active.gte" : "2018-03-01",
        "active.lte" : "2018-03-31",
        "category" : "sports",
        "sort" : "rank"
    }
)

print(response.json())
```

A snippet of the results are shown below:

```json
{
  "count": 19,
  "results": [
    {
      "id": "KWjlX366rrrb",
      "title": "Championship - Nottingham Forest vs Derby County",
      "category": "sports",
      ...
    }
  ]
}
```

We use Geonames data for our Places, so the id _2641170_ is also a Geoname ID for the same location. Please see the [official Geonames site](http://www.geonames.org/) for more information.

Using `place.scope` will return events that apply to the parent and children places of the specified place (e.g. holidays and other events that apply to a country or region). Alternatively you can use `place.exact` to return events that apply to the specified place only.
