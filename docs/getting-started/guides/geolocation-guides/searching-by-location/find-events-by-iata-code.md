# Find Events by IATA Code

For this example, we will use an IATA airport code to search for events around Los Angeles Airport on March the 3rd, 2018.

The `/events` API endpoint supports the use of IATA (3 character), ICAO (4 character), and UN/LOCODE (5 character) airport codes. A CSV file with all supported airport codes and their respective place ids is available to download.

{% file src="../../../../.gitbook/assets/airport-codes.csv" %}

We can use the IATA code for _Los Angeles Airport (LAX)_, `place.scope=LAX`, to find all the _concerts_ events, `category=concerts`, which are active on _3rd of March, 2018_, `active.gte=2018-03-03` and `active.lte=2018-03-03`.

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "place.scope" : "LAX",
        "active.gte" : "2018-03-03",
        "active.lte" : "2018-03-03",
        "category" : "concerts",
        "sort" : "rank"
    }
)

print(response.json())
```

A snippet of the results are shown below:

```json
{
  "count": 73,
  "results": [
    {
      "id": "XS5tQbpjKtFeUShTPt",
      "title": "Demi Lovato with DJ Khaled and Kehlani",
      "category": "concerts",
      ...
    }
  ]
}
```
