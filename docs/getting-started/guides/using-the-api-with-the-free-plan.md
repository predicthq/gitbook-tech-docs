---
description: How to use the API on PredictHQ's free plan
---

# Using the API with the free plan

## How to Use the API with the Free Plan

Under the free plan, users can get full API access to 2 [saved locations](https://www.predicthq.com/blog/use-location-insights-for-instant-demand-insights-for-your-business-locations), using the [Saved Locations API](https://docs.predicthq.com/api/saved-locations) and [Events API](https://docs.predicthq.com/api/events/search-events).&#x20;

The 14-day trial is intended to give you time to explore PredictHQ data and assess its impact on your operations, whether that’s a demand forecast or learning more about what events are happening around your locations, before deciding to purchase. For this reason, we provide access to a wider geographic area without location-based restrictions. But, after 14 days, your account is switched to the free plan. This plan only includes location-based access to up to 2 locations. If during the 14-day trial, you have integrated our API, you will need to use location IDs to retrieve events for your selected locations.

## I’m getting an error when I call the events API on the free plan

In the free plan, API access is limited to only using the locations you have created in the Location Insights module of our web application. To query events for these locations via the API in the free plan, you must include the saved\_location.location\_id parameter in your API query.&#x20;

Without this query parameter, all queries will return the following error:&#x20;

`{"error": "You must use one of the following filters: saved_location.location_id", "code": 400}`

## Setting Up Your Locations

In PredictHQ, locations can be stores, hotels, restaurants, offices, or any other business location you have. There are two options for adding locations:&#x20;

1. Add locations in our web application (Control Center)
2. With the [Saved Locations API](https://docs.predicthq.com/api/saved-locations).&#x20;

### Creating Locations in Control Center

If you add events in Control Center ([see here ](https://www.predicthq.com/support/how-do-i-add-a-location)for instructions), you can use the street address or the latitude & longitude of the location. After creation,  you copy the Location Insights IDs from the URL bar and use that to query the API for events. Another way to retrieve the Location ID is to query the [Search Saved Locations](https://docs.predicthq.com/api/saved-locations/search-saved-locations) API, which returns a list of locations and their respective IDs.

Example fetching Saved Locations using Python:

```python
response = requests.get(
    url="https://api.predicthq.com/v1/saved-locations",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    }
)

print(response.json())
```

See the documentation on[ Control Center](https://www.predicthq.com/support) for more details.

### Creating Locations with the Saved Locations API

If you are using the API then you will need to find the latitude and longitude (lat/long) of each location. Then, with the  [Saved Locations API](https://docs.predicthq.com/api/saved-locations), you can programmatically create new Locations. &#x20;

For multiple locations, you can create a file with a list of lat/longs and names for each store and run a script over the file to create saved locations for each while leveraging our [Suggested Radius API](https://docs.predicthq.com/api/suggested-radius/get-suggested-radius). The order of operations looks like this:&#x20;

Find the lat/long of each location:

1. Call the [Suggested Radius API](https://docs.predicthq.com/api/suggested-radius/get-suggested-radius) for each store to find the radius to use
2. Call the Create Saved Locations endpoint (`POST /saved-locations`) to create a location with the lat/long and radius you have for the location
3. Store the `location_id` returned for the location

This process only needs to be performed when you initially load in your locations or if locations change (such as a store closes or a new store opens).

## Fetching Events for Your Locations

Once you have uploaded your locations you will have a list of location\_id's for each location. To get the latest events for each location you can call the [Events API](https://docs.predicthq.com/api/events/search-events) with the `saved_location.location_id` filter to get back events for the location.

\
Example fetching events using a Saved Location ID using Python:

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "saved_location.location_id": "sFlb8HlsLa1j-S4UDEMEkQ"
    }
)

print(response.json())
```

\
You can of course use other filters in the Events API to further filter down the response. Use paging to handle multiple pages of results.

Alternatively, you can access events using the `/events` call in the [Saved Locations API](https://docs.predicthq.com/api/saved-locations/search-events-for-a-saved-location) (see[ Get a list of events for a location](https://docs.predicthq.com/api/saved-locations/search-events-for-a-saved-location)). To get a list of events for a location make the following call with the location\_id `GET /saved-locations/<location_id>/insights/events`.\
\
`E.g. GET /saved-locations/0b6ZrOnTdB2Y7k4zC_9qBg/insights/events.`

See the example below:

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/saved-locations/sFlb8HlsLa1j-S4UDEMEkQ/events",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "date_range_type": "next_90d",
        "category": "public-holidays,sports",
        "sort": "-start"
    }
)

print(response.json())
```

You can then use the events or store them in your data store. Ensure you keep events refreshed as events are dynamic and can change. For example, they can be canceled, postponed, move locations, change dates, and so on. See [Keeping Data Updated](https://docs.predicthq.com/predicthq-api/bulk-data-delivery/keep-data-updated-via-api) for more information on how we suggest you stay up-to-date.

Note: if you have location-based access, similar to the free plan, you will be required to supply a value for the `saved_location.location_id` query parameter when calling the Events API. If you do not supply a value, the API will return an error.

If you add or delete locations ensure you update the location\_id values used to query the API.

\
See also [Working with Location-Based Subscriptions](https://docs.predicthq.com/getting-started/guides/geolocation-guides/searching-by-location/working-with-location-based-subscriptions)
