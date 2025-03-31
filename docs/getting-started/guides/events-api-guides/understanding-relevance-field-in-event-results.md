---
description: >-
  Understand how some parameters in Events API affect the order of results and
  the relevance field.
---

# Understanding Relevance Field in Event Results

{% hint style="info" %}
Note that the relevance field has been deprecated. Please do not rely on this field being present in Events API responses.
{% endhint %}

The `relevance` field in Events API responses is purely a sorting mechanism and is only set when using certain (relevance-affecting) parameters. By default `relevance` will be `0` but when using a parameter like `q` (full-text search) the `relevance` field will reflect the relevance of the event to the search terms used.

Throughout the guide we'll be using the scenario of adding an "Events Near Me" feature to a mobile application, with the example use case of a user wanting to find a jazz concert to attend. We'll show how information from/about the user can be translated to search parameters that help tailor results to what the user wants.

## Initial Search

Let's start by defining a basic search. We know the user is in the United States of America, so we use a `US` country filter. They've also selected concerts as the type of event they want to find in the app, so we can map that to a `concert` category filter. Finally, users of this feature aren't interested in past events, so we'll filter to events that are active on or after the `$CURRENT_DATE` (replace with the current date in `yyyy-MM-dd` format).

Perform an event search with the parameters `category=concerts&country=US&active.gte=$CURRENT_DATE`.

This will return the first page of current/future concert events in the US that fall inside your event visibility window, sorted in reverse chronological order. It's likely there's more than one page of results, and more results than your result limit allows you to fetch. Our goal is to get the concerts the user would most like to attend in the first page of results.

```python
import requests

response = requests.get(
    url = "https://api.predicthq.com/v1/events/",
    headers = {
        "Authorization": "Bearer $ACCESS_TOKEN"
    },
    params = {
        "category": "concerts",
        "country": "US",
        "active.gte": "$CURRENT_DATE"
    }
)

print(response.json())
```

## Full-Text Search

The user likes jazz music, so types "jazz" in the app's search box. A search box can be mapped to the `q` parameter.

The `q` parameter performs a text search on the title and description of events. This parameter has two effects - it filters results to events whose titles or descriptions have some similarity to the search string, and it also scores events by this similarity.

The similarity score can influence the `relevance` field of each event. By default, results are sorted by `relevance,-start` - first by `relevance`, and then by `-start` if two events have the same `relevance`. Previously all events had the same `relevance`, so results were sorted in reverse chronological order. By adding a parameter that affects `relevance` the results will be sorted so events with the highest `relevance` are returned first.

Add parameter `q=jazz` to our previous request.

{% hint style="info" %}
Parameters that can affect `relevance` are automatically included in the relevance calculation when they are used. We'll cover using the `relevance` parameter to control the components used to calculate the `relevance` field later in this guide.
{% endhint %}

```python
import requests

response = requests.get(
    url = "https://api.predicthq.com/v1/events/",
    headers = {
        "Authorization": "Bearer $ACCESS_TOKEN"
    },
    params = {
        "q": "jazz",
        "category": "concerts",
        "country": "US",
        "active.gte": "$CURRENT_DATE"
    }
)

print(response.json())
```

## Temporal Relevance

We've filtered out past events, but we're still getting events that are well in the future. The user might still want to go to them, but events that are happening sooner are more important.

We could sort by `start` ascending so earlier events are returned first. However, this _only_ takes into account the "soon-ness" of the event without considering any other factors of what the user wants, such as the relevance to the `q` parameter (and the other factors we'll introduce below).

Instead, we'll use the `start_around.origin` parameter to add proximity of an event's start date to the `$CURRENT_DATE` as a relevance component, prioritizing events that start soon.

Add parameter `start_around.origin=$CURRENT_DATE` to our previous request.

{% hint style="info" %}
The other `start_around.*` parameters can be used to tune how the relevance of an event changes as its start date moves away from the origin. See the [parameter documentation](../../../api/events/search-events.md#query-parameters) for details.
{% endhint %}

```python
import requests

response = requests.get(
    url = "https://api.predicthq.com/v1/events/",
    headers = {
        "Authorization": "Bearer $ACCESS_TOKEN"
    },
    params = {
        "start_around.origin": "$CURRENT_DATE",
        "q": "jazz",
        "category": "concerts",
        "country": "US",
        "active.gte": "$CURRENT_DATE"
    }
)

print(response.json())
```

## Spatial Relevance

We've prioritized events that are near in time, but what about near in space? We are aiming to build an "Events Near Me" feature after all.

The user's location (as reported by our app) is `40.782409,-73.971885` (`lat,lon`) - near the American Museum of Natural History in New York. We can use this as our `location_around.origin` to add the proximity of the event to the user's location as a relevance component.

We'll assume they are happy to travel a km or so, setting `location_around.offset` so all events within `1km` have the same `location_around` relevance, with the relevance reducing as the distance to the event increases beyond that.

Add parameters `location_around.origin=40.782409,-73.971885&location_around.offset=1km` to our previous request.

{% hint style="info" %}
The other `location_around.*` parameters can be used to further tune how the relevance of an event changes as its location moves away from the origin. See the [parameter documentation](../../../api/events/search-events.md#query-parameters) for details.
{% endhint %}

```python
import requests

response = requests.get(
    url = "https://api.predicthq.com/v1/events/",
    headers = {
        "Authorization": "Bearer $ACCESS_TOKEN"
    },
    params = {
        "location_around.origin": "40.782409,-73.971885",
        "location_around.offset": "1km",
        "start_around.origin": "$CURRENT_DATE",
        "q": "jazz",
        "category": "concerts",
        "country": "US",
        "active.gte": "$CURRENT_DATE"
    }
)

print(response.json())
```

## Event Rank

Our final relevance adjustment is to prioritize events with higher ranks, as they're more likely to be of interest to the user. Here we're not going to add a parameter that will start influencing relevance automatically, like we have with `q`, `start_around.*` and `location_around.*`. Instead we're going to directly change how the `relevance` field is calculated by using the `relevance` parameter.

The `relevance` parameter controls which relevance components are multiplied together to produce the final `relevance` field. When it isn't explicitly set it defaults to including all the components from the relevance-influencing parameters used in the search - in our case, `q`, `start_around`, and `location_around`.

{% hint style="info" %}
See the [relevance parameter documentation](../../../api/events/search-events.md#query-parameters) for more information about the `relevance` parameter.
{% endhint %}

We want to add the `rank` component into the mix, so we need to set the `relevance` parameter explicity. We still want the existing components, so need to include them, but we'll add `rank` as well.

Add parameter `relevance=rank,q,start_around,location_around` to our previous request.

```python
import requests

response = requests.get(
    url = "https://api.predicthq.com/v1/events/",
    headers = {
        "Authorization": "Bearer $ACCESS_TOKEN"
    },
    params = {
        "relevance": "rank,q,start_around,location_around",
        "location_around.origin": "40.782409,-73.971885",
        "location_around.offset": "1km",
        "start_around.origin": "$CURRENT_DATE",
        "q": "jazz",
        "category": "concerts",
        "country": "US",
        "active.gte": "$CURRENT_DATE"
    }
)

print(response.json())
```

And there you have it - a search that returns the most relevant results for the user, based on the user's search terms, how soon the events start, how close the events are to the user, and the events' ranks.
