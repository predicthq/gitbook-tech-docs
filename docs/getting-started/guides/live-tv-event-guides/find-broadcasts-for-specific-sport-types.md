---
description: >-
  Better understand predicted vs scheduled broadcasts as well as different sport
  types.
---

# Find Broadcasts for Specific Sport Types

In this example we explain when the different `broadcast_status` values are used and how to search for broadcasts for different sports.

Our Broadcasts API provides broadcast and viewership data for sports with the top viewership in the US. These include broadcasts for games played in the seven top US leagues: NFL, NBA, NHL, MLB, MLS, D1 NCAA Basketball, D1 NCAA Football, and also broadcasts for other sports events with high viewership.

Broadcasts for the seven top US leagues have a `broadcast_status` of `scheduled`. We enrich our data with television listings to determine their televised time and location (county). The `scheduled` `broadcast_status` is for these broadcasts where we know the date, time and location of a TV broadcast based on TV schedule information.

Broadcasts for sports other than the seven leagues have a `broadcast_status` of `predicted` since we predict their televised time and location (county). The `predicted` `broadcast_status` means we don’t have detailed TV schedule information for the sports event. These events have high viewership and are assumed to be televised nationally (in all counties). These are typically one-off events or are finals of their respective competitions, such as the 2019 NCAA Women's Basketball Final.

For broadcasts with a `predicted` `broadcast_status`, we calculate viewership per county based on many factors including the amount of sports fans in different counties. This information is not as precise as those with the `scheduled` `broadcast_status` but should give a pretty good prediction of who will be watching these large events. Customers may want to use the `broadcast_status` to indicate the confidence of a broadcast airing; they may build this as a feature or to treat scheduled broadcasts differently from predicted.

The API returns broadcasts of all `broadcast_status` values by default. The `broadcast_status` [parameter](https://docs.predicthq.com/resources/broadcasts/#param-broadcast\_status) allows us to filter broadcasts with a particular status. The Broadcasts API also supports the `event.label` [parameter](https://docs.predicthq.com/resources/broadcasts/#param-event.label) which can be used to find broadcasts for specific sport types. In this example, we show an API query using the `broadcast_status` and `event.label` parameters which returns broadcasts for the 2019 NCAA Women’s Basketball Final amongst other matching results. You can discover available sport types and event labels by [Searching Live TV Events](https://control.predicthq.com/search/events/broadcasts) in Control Center or using the [Events API](https://docs.predicthq.com/resources/events).

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/broadcasts/",
    headers={
        "Accept": "application/json",
        "Authorization": "Bearer $ACCESS_TOKEN"
    },
    params={
        "broadcast_status": "predicted",
        "event.label": "basketball",
        "start.gte": "2019-04-01",
        "start.lt": "2019-05-01"
    }
)

print(response.json())
```
