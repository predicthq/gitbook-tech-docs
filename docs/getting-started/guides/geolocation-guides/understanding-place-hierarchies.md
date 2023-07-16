# Understanding Place Hierarchies

{% hint style="info" %}
Places associated with our events are [Geonames](https://www.geonames.org/) Features, which can be either an Area, an Administrative Feature, or a Populated Place. Use our [Places API](https://docs.predicthq.com/resources/places/) to explore Places data used in our events.
{% endhint %}

The `place_hierarchies` field contains Place ids for an event. The structure is an array of array of ids; ids are strings. For example:

```json
[
  ["6295630", "6255149", "6252001", "5815135", "5799783", "5786882"]  
]
```

The array of ids is ordered, representing a parent-to-child hierarchy of places. In the above example, the id 6295630 is the parent place of 6255149; and 6255149 is the parent place of 6252001, and so on. The last id in the list is the place in which the event occurs: 5786882 in the example.

Details for each Place, such as its name can be retrieved from the [Places API](https://docs.predicthq.com/resources/places/#search-places). For the above hierarchy, calling the Places API with `?id=6295630,6255149,6252001,5815135,5799783,5786882` returns:

```json
{
  "count": 6,
  "results": [ // some fields omitted
    {"id": "6295630", "type": "planet", "name": "Earth"},
    {"id": "6255149", "type": "continent", "name": "North America"},
    {"id": "6252001", "type": "country", "name": "United States"},
    {"id": "5815135", "type": "region", "name": "Washington"},
    {"id": "5799783", "type": "county", "name": "King County"},
    {"id": "5786882", "type": "locality", "name": "Bellevue"}
  ]
```

This reveals an event with the above `place_hierarchy` occurs in Bellevue, which belongs to King County, which is in Washington state, USA.

The `place_hierarchy` value when understood with the `scope` of an event reveals if an event is a point event or an area event. Point events have a `scope` value "locality"; Area events have "localadmin", "county", "region", or "country".

Point events happen at a point (its coordinate location) in the locality-level place it is scoped to. Example: This [MLB game at Oracle Park](https://events.predicthq.com/events/97iX53YAGnCwF9TGx3) is a point event with `scope`value "locality" and `place_hierarchy` value `[["6295630","6255149","6252001","5332921","5391997","5391959"]]`. 5391959 is the place id of San Francisco City.

Area events without polygons apply to the place it is scoped to, which will either be a county-level, region-level, or country-level place. Example: This [Thanksgiving Day](https://events.predicthq.com/events/gEkxDPqErD5n) holiday is an area event with `scope` value "country" and `place_hierarchy` value `[["6295630","6255149","6252001"]]`. 6252001 is the place id of the United States.

Area events with polygons apply to the area defined by the polygon's geometry. Places in the event's `place_hierarchies` are those which overlap with the polygon.

Place hierarchies value can be an empty array in some cases.

## Multiple hierarchies

Some events can have multiple hierarchies.

Point events can have up to two hierarchies. The second hierarchy, if it exists, is a nearby major city's hierarchy within a radius of 50km. This [Bite of Seattle community festival](https://events.predicthq.com/events/QDgCysY3kMnpoGYFi9), for example, is scoped to 2 places. Its `scope` and `place_hierarchies` values are shown below. 7153941 is the place id of Denny Regrade, the neighbourhood where the festival takes place; 5809844 is the place id of Seattle, a nearby major city. `{ "scope": "locality", "place_hierarchies": [ ["6295630", "6255149", "6252001", "5815135", "5799783", "7153941"], ["6295630", "6255149", "6252001", "5815135", "5799783", "5809844"] ] }`

Area events have multiple hierarchies if the event applies to multiple counties or regions, or if its polygon overlaps with multiple counties or regions. For example: this [flood warning](https://events.predicthq.com/events/24gdWYbR9M7DzJBVdY) event's polygon overlaps with 3 counties in the state of Mississippi. Its `scope` and `place_hierarchies` values are shown below. 4421859, 4429877, 4450285 are the respective place ids for Claiborne County, Hinds County, and Warren County.

```json
{
  "scope": "county",
  "place_hierarchies": [
    [
      "6295630",
      "6255149",
      "6252001",
      "4436296",
      "4421859"
    ], [
      "6295630",
      "6255149",
      "6252001",
      "4436296",
      "4429877"
    ], [
      "6295630",
      "6255149",
      "6252001",
      "4436296",
      "4450285"
    ]
  ]
}
```

## Examples

### Fetch Place Information for Place IDs

With a given list of Place IDs, fetch the Place info using the [Places endpoint](../../../api/places/search-places.md).

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/places/",
    headers={
        "Authorization": "Bearer $ACCESS_TOKEN",
        "Accept": "application/json",
    },
    params={
        "id": "5391959,6252001,7153941,5809844,4421859,4429877,4450285",
    }
)

print(response.json())
```

The response will look like:

```json
{
  "count": 7,
  "results": [ // some fields omitted
    {
      "id": "5391959",
      "type": "locality",
      "name": "San Francisco",
      "country_alpha2": "US",
      "location": [-122.41942, 37.77493]
    },
    {
      "id": "6252001",
      "type": "country",
      "name": "United States",
      "country_alpha2": "US",
      "location": [-98.5, 39.76]
    },
    {
      "id": "7153941",
      "type": "locality",
      "name": "Denny Regrade",
      "country_alpha2": "US",
      "location": [-122.33667, 47.61611]
    },
    {
      "id": "5809844",
      "type": "locality",
      "name": "Seattle",
      "country_alpha2": "US",
      "location": [-122.33207, 47.60621]
    },
    {
      "id": "4421859",
      "type": "county",
      "name": "Claiborne County",
      "country_alpha2": "US",
      "location": [-90.91181, 31.97369]
    },
    {
      "id": "4429877",
      "type": "county",
      "name": "Hinds County",
      "country_alpha2": "US",
      "location": [-90.44282, 32.2667]
    },
    {
      "id": "4450285",
      "type": "county",
      "name": "Warren County",
      "country_alpha2": "US",
      "location": [-90.85201, 32.35723]
    }
  ]
}
```
