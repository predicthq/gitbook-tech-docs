---
description: >-
  Event information changes frequently. For example, a date changes, an event
  gets cancelled or ranking is updated. It’s important to keep your data set up
  to date.
---

# Keep Data Updated via API

{% hint style="success" %}
We highly recommend using Snowflake or ADX to keep your copy of PredictHQ event data up-to-date. Using one of those methods removes all the complexity of having to implement a system using the API and results in far higher accuracy with fewer issues. Keeping up-to-date via the API is much more complicated than via Snowflake or ADX.
{% endhint %}

Events often change or get deleted because they’re cancelled, postponed, marked as duplicates or identified as spam. In February 2020, concerns about COVID-19 led to a 500% spike in cancellations and postponements of significant events when compared to February 2019. It’s important to make sure you keep your copy of PredictHQ in-sync with ours to stay up-to-date.

Our records have an `updated` field which indicates the date/time the record was last updated.

{% hint style="info" %}
For example an event for a conference that starts on 1 April 2020 may originally be created in our system on 1 Jan 2020. Then the event’s details don’t change until the 5 Feb 2020 when the event is cancelled. The event’s state field is then changed to `deleted` and the `deleted_reason` is changed to `cancelled`. The event’s updated field would show `2020-02-05T05:00:00Z` (for the cancellation change made to the event on 5 Feb 2020).
{% endhint %}

## High-level Guide to Keeping Data Updated

The best way to update your data store is to search for records that have changed since you last synced.

1. Use the `updated.*` parameters to find records that have been updated since your last fetch.
2. Make sure you’re fetching both `active` and `deleted` events e.g. `state=active,deleted`
   1. For the Broadcast API you would use `record_status=active,duplicate,deleted`
3. Ensure you won’t miss changes if records are updated while you’re fetching with `sort=-updated`
4. We recommend syncing every 24 hours or more frequently for unscheduled events if needed.

An example request in Python is below:

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "updated.gte" : "2023-07-01",
        "updated.lte" : "2023-07-10",
        "state" : "active,deleted",
        "sort": "-updated",
        "limit": 500
    }
)

print(response.json())
```

{% hint style="success" %}
Note that you can use the [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features) to directly get daily-level aggregations of the data instead of downloading large volumes of event data and keeping it up to date. The Features API provides pre-built features that save you from writing a lot of code to aggregate data and create features on your side.
{% endhint %}
