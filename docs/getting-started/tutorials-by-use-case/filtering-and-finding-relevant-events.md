---
description: >-
  Learn how to filter and find events relevant to your business using
  PredictHQ's Events API.
---

# Filtering and Finding Relevant Events

Events such as concerts, expos and public holidays can shift consumer behavior and [impact demand](https://www.predicthq.com/use-cases/demand-forecasting). Understanding which events are most relevant to a store or location is therefore critical for effective planning and management. By staying ahead of these events, businesses can better prepare for changes in consumer traffic and purchasing patterns, ensuring optimal staffing and inventory levels.

This tutorial will walk through the [Events API](https://www.predicthq.com/apis/event-api) while exploring an example involving a pizzeria interested in identifying major upcoming events. The goal is to learn how to effectively define query parameters, make API calls and interpret responses.

Alternatively, use [Location Insights](https://www.predicthq.com/location-insights) to monitor upcoming events around your stores or locations. Setting up a location is quick and easy in [Control Center](https://control.predicthq.com/location-insights) where you can get immediate insights for all created locations. This can also be done securely and at scale from your own environment with the [Saved Locations API](../../api/saved-locations/).

## Use Cases

Demand Forecasting, Visualization and Insights, Dynamic Pricing, Inventory Management, Workforce Optimization and Others

## Relevant Industries

Accommodation, Consumer Packaged Goods, Grocery and Supermarkets, Leisure, Travel and Tourism, Marketing and Advertising, Parking, Restaurants, Retail, Transportation and Delivery and Others

## Getting Started

A valid access token is required for calling PredictHQ’s APIs. Refer to the [API Quickstart](../api-quickstart.md) for guidance on creating an access token and quickly test our APIs with our [API Explorer](https://control.predicthq.com/explorer/events).

## Scenario

Let's take a fictional example: Tom, the owner of Tom’s Pizzeria in Downtown Seattle, Washington, has experienced overwhelming demand on several occasions, resulting in long lines and significant service delays. Suspecting nearby events were the cause of these surges, he sought to better prepare by identifying upcoming major events. To achieve this, Tom is looking into PredictHQ’s Events API to see how he can obtain this information for the next month.

## How-To Guide

The sections below will guide you through identifying the top 50 upcoming events near Tom’s Pizzeria over the next month. Follow the steps and code snippets to understand how this can be adapted to fit other business scenarios.

### Step 1. Define Query Parameters for the Events API

Given the volume of events happening all the time, choosing the right query parameters is crucial for identifying relevant events. The next section outlines the most commonly used parameters from the [Events API](../../api/events/search-events.md), providing guidance on how to use them along with Tom’s choices:

<details>

<summary>Date Range</summary>

Set the date range for the search.

* **Active**: Use the `active` parameter to include all events that are ongoing in the date range.
* **Start**: To focus on the start dates of events, the date range should be set using the `start` parameter.

#### Settings for Tom’s Pizzeria

Tom is interested in events taking place in the month of June 2024. He will configure the search to include active events from June 1st to June 30th, considering the local time zone.&#x20;

```python
params={
   "active.gte": "2024-06-01",
   "active.lte": "2024-06-30",
   "active.tz": "America/Los_Angeles"
   }
```

</details>

<details>

<summary>Location Type</summary>

Define the catchment area for the search. Refer to our [industry recommendations](../guides/industry-specific-event-filters.md#location-type) for which location type to start with.&#x20;

* **Center Point & Radius**: Define a circular area around your store or location by specifying latitude/longitude and a radius using the `within` parameter. The [Suggested Radius API](https://docs.predicthq.com/api/suggested-radius/get-suggested-radius) can assist in identifying an appropriate radius.

<!---->

* **City, State, Country**: For targeted searches across a predefined area e.g. specific cities, states or countries, use the `place` parameter and provide a place ID. The [Places API](https://docs.predicthq.com/api/places/search-places) can assist in finding correct place IDs.

<!---->

* **Country-wide**: If your interest spans an entire country, the easiest way is to use the `country` parameter and set it to the res

#### Settings for Tom’s Pizzeria

Tom is keen on monitoring events within close proximity to his pizzeria so he decides to set the search location using the center point and radius approach.

Tom first uses the [Suggested Radius API](../../api/suggested-radius/get-suggested-radius.md) to establish the optimal search radius (see below for code snippet). The Suggested Radius API recommends a 1.48 mi radius based on typical foot traffic and local demographic data for Food and Beverage/Restaurant industries in urban settings.

```python
params={
  "within": "1.48mi@47.60,-122.33"
  }
```

#### **Suggested Radius**

Tom is in the Food and Beverage/Restaurants industry and the pizzeria is located in Downtown Seattle at (47.60, -122.33).  These are the two parameters for the Suggested Radius API:

```python
import requests

response = requests.get(
  url="https://api.predicthq.com/v1/suggested-radius",
  headers={
    "Authorization": "Bearer $ACCESS_TOKEN",
    "Accept": "application/json"
    },
  params={
    "location.origin": "47.60,-122.33",
    "radius_unit": "mi",
    "industry": "restaurants"
    }
)

print(response.json())
```

```python
{
  "radius": 1.48,
  "radius_unit": "mi",
  "location": {
    "lat": "47.6",
    "lon": "-122.33"
  }
}
```

</details>

<details>

<summary>Event Type</summary>

Select the types of events for the search.

* **Relevant Event Categories**: To identify [event categories](../predicthq-data/event-categories/) that are most relevant to your location, use [Demand Analysis](https://www.predicthq.com/support/beam-overview) in [Control Center](https://control.predicthq.com/beam) or the [Beam API](../../api/beam/). Alternatively, start with our [industry recommendations](../guides/industry-specific-event-filters.md#relevant-event-categories) for which categories to start with.

<!---->

* **Specific Themes**: Use the `phq_label` parameter to focus on particular themes within a category. For example, to find baseball-related events, set `phq_label` to `baseball`.

#### Settings for Tom’s Pizzeria

For a broad initial survey of upcoming events, Tom has chosen to focus on categories that are likely to influence restaurant visits.

```python
params={
  "category": "public-holidays,performing-arts,conferences,concerts,festivals"
  } 
```

Next, Tom plans to use use [Demand Analysis](https://www.predicthq.com/support/beam-overview) in [Control Center](https://control.predicthq.com/beam) to help refine these categories further based on actual data-driven insights, tailored to his pizzeria.

</details>

<details>

<summary>Event Impact</summary>

Define the event impact for the search.

* **PHQ Rank**: Use the `rank` parameter to target events based on their [predicted impact](../predicthq-data/ranks/phq-rank.md), with values ranging from 0 to 100. This is useful for filtering out smaller events, ensuring focus on those likely to impact demand. Set the minimum rank threshold by setting rank.gte based on our [recommended industry minimums](../guides/industry-specific-event-filters.md#minimum-phq-rank).
  * The `rank_level` parameter divides the PHQ Rank into five equal bands, for simplified categorization. Levels range from 1 to 5, where 1 represents minor impact, such as a community workshop, and 5 represents major impact, like the Olympics.

<!---->

* **Local Rank**: To consider the event's impact on the local area, use `local_rank`, which also ranges from 0 to 100. By considering factors like population density, [Local Rank](../predicthq-data/ranks/local-rank.md) helps differentiate the impact of similar-sized events in different locations, such as Aspen, Colorado versus New York City.
  * The `local_rank_level` parameter divides Local Rank into five equal bands, for simplified categorization. Levels also range from 1 to 5, with 1 representing minor impact and 5 representing major impact, similar to the PHQ Rank.

<!---->

* **PHQ Attendance**: For [attendance-based events](../predicthq-data/event-categories/attendance-based-events.md), impact can be directly measured with `phq_attendance` which is the [number of people predicted to attend an event](../predicthq-data/predicted-attendance.md).

#### Settings for Tom’s Pizzeria&#x20;

To focus his resources efficiently and avoid spending time on smaller, less impactful events, Tom sets a minimum PHQ rank threshold of 30, which is recommended for his industry.

```python
params={
  "rank.gte": 30
  }
```

</details>

<details>

<summary>Event State</summary>

Track events based on their likelihood of occurring.

* **Event State**: Events classified as `active` by the `state` parameter have confirmed details including start dates and locations, whereas the details of \`predicted\` events are [subject to change](../predicthq-data/predicted-events.md) as more information becomes available. Events are marked as `deleted` if they are canceled, postponed, or otherwise removed.

Focusing primarily on `active` and `predicted` event states ensures that only events which are relevant and likely to occur are tracked

#### Settings for Tom’s Pizzeria

Tom is interested in all upcoming events in June 2024 and has decided to include `predicted` events as well.

```python
params={
  "state": "active,predicted"
  }
```

</details>

<details>

<summary>Query Modifiers</summary>

Optimize search results with useful parameters.

* **Limit**: Specify the maximum number of events per page to return, managing the volume of results and focusing on the most relevant events. Use the `next` field in the API response to navigate to additional results (refer to [#handling-paginated-api-responses](filtering-and-finding-relevant-events.md#handling-paginated-api-responses "mention") for more details).

<!---->

* **Sort**: Order the search results according to specific attributes, most commonly event impact such as `rank` or `phq_attendance`, to prioritize high impact events.

#### Settings for Tom’s Pizzeria

Tom is interested in the top 50 upcoming events for June 2024 that could impact his business. He sets the search parameters to not only manage the scope of results but also ensure that the most significant events are returned first.

```python
params={
   "limit": 50,
   "sort": "rank"
   }
```

</details>

{% hint style="info" %}
For detailed information on all query parameters (including those not shown here), please consult [Events API](../../api/events/).
{% endhint %}

### Step 2. Call Events API

With the query parameters now configured, the next step is to call the Events API. This can be done using our [API Explorer](https://control.predicthq.com/explorer/events) or via your preferred tool. Below is an example Tom's request using python:

```python
import requests

base_url = "https://api.predicthq.com/v1/events"

headers = {
    "Authorization": "Bearer $ACCESS_TOKEN",  # Replace $ACCESS_TOKEN with your actual token
    "Accept": "application/json"
}

params = {
    "within": "1.48mi@47.60,-122.33",
    "category": "public-holidays,school-holidays,conferences,concerts,performing-arts",
    "active.gte": "2024-06-01",
    "active.lte": "2024-06-30",
    "rank.gte": 30,
    "limit": 50,
    "sort": "rank",
    "state": "active,predicted"
}

response = requests.get(base_url, headers=headers, params=params)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error fetching response: {response.status_code}")
```

#### Handling Paginated API Responses

The Events API responses come in a paginated format to limit the amount of data sent in a single response. Here's how you can automatically loop through the paginated API responses to collect all available results:

```python
def fetch_all_pages(base_url=base_url, headers=headers, params=params):
    results = []
    next_url = base_url  # Start with the base URL

    while next_url:
        response = requests.get(next_url, headers=headers, params=params)
        params = None  # After the first request, prevent re-sending initial parameters
        if response.status_code == 200:
            data = response.json()
            results.extend(data['results'])
            next_url = data.get('next')  # Update the next_url from the 'next' field in the response
        else:
            print(f"Failed to fetch data: {response.status_code}, Message: {response.text}")
            break

    return results

all_events = fetch_all_pages()
print("Total events fetched:", len(all_events))

```

For information on how to search for events using our SDK, please refer to [sdks](../../integrations/sdks/ "mention").

{% hint style="info" %}
For more details, visit:

* [search-events.md](../../api/events/search-events.md "mention")
* [sdks](../../integrations/sdks/ "mention")
{% endhint %}

### Step 3. Interpret Response

Once the API call is made, the Events API returns a structured JSON response containing detailed information about the events that match the query parameters. Below is an illustrative example of what the first page of this response might look like, demonstrating initial pagination details and a sample event listing:

<details>

<summary>Example Response</summary>

```json
{
  "count": 388,
  "overflow": false,
  "next": "https://api.predicthq.com/v1/events/?active.gte=2024-06-01&active.lte=2024-06-30&category=public-holidays%2Cschool-holidays%2Cconferences%2Cconcerts%2Cperforming-arts&limit=50&offset=50&rank.gte=30&sort=rank&state=active%2Cpredicted&within=1.48mi%4047.60%2C-122.33",
  "previous": null,
  "results": [
    {
      "relevance": null,
      "id": "4hFctf3GqQ2MS5qYLW",
      "title": "Itzy",
      "alternate_titles": [
        "ITZY 2ND WORLD TOUR 'BORN TO BE'",
        "ITZY at WAMU Theater",
        "Itzy (Concert)"
      ],
      "description": "",
      "category": "concerts",
      "labels": [
        "concert",
        "music"
      ],
      "rank": 62,
      "local_rank": 77,
      "phq_attendance": 4201,
      "entities": [
        {
          "entity_id": "hckgG3yNMg5PRGsL49pNzK",
          "name": "ITZY",
          "type": "organization"
        },
        {
          "entity_id": "3AedBWTgigZjWx9NhwLsvgU",
          "name": "CenturyLink Field - WaMu Theater",
          "type": "venue",
          "formatted_address": "800 Occidental Avenue South\nSeattle, WA 98134\nUnited States of America"
        }
      ],
      "duration": 0,
      "start": "2024-06-07T03:00:00Z",
      "start_local": "2024-06-06T20:00:00",
      "end": "2024-06-07T03:00:00Z",
      "end_local": "2024-06-06T20:00:00",
      "predicted_end": "2024-06-07T07:10:00Z",
      "predicted_end_local": "2024-06-07T00:10:00",
      "updated": "2024-05-15T18:25:53Z",
      "first_seen": "2024-01-26T02:32:24Z",
      "timezone": "America/Los_Angeles",
      "location": [
        -122.3322862,
        47.5933082
      ],
      "geo": {
        "geometry": {
          "coordinates": [
            -122.3322862,
            47.5933082
          ],
          "type": "Point"
        },
        "placekey": "zzw-223@5x4-4vs-mp9"
      },
      "impact_patterns": [
        {
          "vertical": "accommodation",
          "impact_type": "phq_attendance",
          "impacts": [
            {
              "date_local": "2024-06-05",
              "value": 841,
              "position": "leading"
            },
            {
              "date_local": "2024-06-06",
              "value": 4201,
              "position": "event_day"
            },
            {
              "date_local": "2024-06-07",
              "value": 421,
              "position": "lagging"
            }
          ]
        },
        {
          "vertical": "hospitality",
          "impact_type": "phq_attendance",
          "impacts": [
            {
              "date_local": "2024-06-04",
              "value": 85,
              "position": "leading"
            },
            {
              "date_local": "2024-06-05",
              "value": 1051,
              "position": "leading"
            },
            {
              "date_local": "2024-06-06",
              "value": 4201,
              "position": "event_day"
            },
            {
              "date_local": "2024-06-07",
              "value": 127,
              "position": "lagging"
            }
          ]
        }
      ],
      "scope": "locality",
      "country": "US",
      "place_hierarchies": [
        [
          "6295630",
          "6255149",
          "6252001",
          "5815135",
          "5799783",
          "7174408",
          "5809844"
        ]
      ],
      "state": "active",
      "private": false,
      "predicted_event_spend": 325046,
      "predicted_event_spend_industries": {
        "accommodation": 77435,
        "hospitality": 188904,
        "transportation": 58707
      },
      "phq_labels": [
        {
          "label": "pop",
          "weight": 0.53
        },
        {
          "label": "other",
          "weight": 0.47
        }
      ]
    },
    {
      // More results...
    }
  ]
}
```

</details>

#### Key Response Fields

<details>

<summary>Pagination</summary>

Results are returned in a paginated format, where the number of events per page is determined by your subscription limits. The key fields related to pagination include:

* `count`: The total number of events that match the search criteria.
* `next` and `previous`: URLs that can be used to navigate to the next or previous pages of results, respectively.&#x20;
* `overflow`: If `true`, this indicates more results are available but cannot be reached through normal pagination due to subscription limits. Consider making your search query more specific to reduce the number of results returned.&#x20;

For more comprehensive guidelines on navigating paginated results, refer to [pagination.md](../../api/overview/pagination.md "mention").

</details>

<details>

<summary>Events</summary>

Events are detailed in the results section of the response, each represented as a JSON block. The amount of information provided for each event can vary depending on the type of event and other factors. A comprehensive guide that covers each available field can be found in [#response-fields](../../api/events/search-events.md#response-fields "mention"). Common response fields include:

**Dates**

* `start_local`, `end_local`: Indicates the start and end dates of the event in the local time zone. If an end date is not available, it defaults to the start date. For some events where the end date is not available, a [predicted end date](../predicthq-data/predicted-end-times.md) fills this gap with `predicted_end_local`.
* `start`, `end`, `predicted_end`: Indicates the start, end and predicted end dates in UTC.

**Location**

* `geo`: Includes the latitude/longitude coordinates of the event as well as additional location information which is especially useful for events that cover [an area](../guides/geolocation-guides/working-with-polygons.md) rather than a point, such as parades.&#x20;
* `place_hierarchies`: Lists the [place IDs](../guides/geolocation-guides/understanding-place-hierarchies.md) associated with the event location.
* `country`: Identifies the country where the event takes place.

**Event Descriptors**

* `title`: The name of the event.
* `description`: A brief description of what the event entails, if available.
* `category`: The [type of event](../predicthq-data/event-categories/), such as concerts or public holidays.
* `phq_labels`: [Tags](../predicthq-data/labels.md) that classify the event into common themes or topics. Note, `labels` is a legacy field and is no longer maintained.

**Event Impact**

* `rank`: The [predicted impact](../predicthq-data/ranks/phq-rank.md) of the event based on a globally comparable rank index.
* `local_rank`: The [predicted impact](../predicthq-data/ranks/local-rank.md) of the event, taking into account the local area.
* `phq_attendance`: The number of people [predicted to attend](../predicthq-data/predicted-attendance.md) the event, for [attendance-based events](../predicthq-data/event-categories/attendance-based-events.md).
* `impact_patterns`: The [predicted impact](../predicthq-data/impact-patterns.md) of how the event affects various industries on days surrounding the event.
* `predicted_event_spend`: The [predicted financial impact](../predicthq-data/predicted-event-spend.md) of the event on local businesses.

</details>

{% hint style="info" %}
For more details, visit:

* [pagination.md](../../api/overview/pagination.md "mention")
* [search-events.md](../../api/events/search-events.md "mention")
* [working-with-dates-times-and-timezones.md](../guides/date-and-time-guides/working-with-dates-times-and-timezones.md "mention")
* [predicthq-data](../predicthq-data/ "mention")
{% endhint %}

## Next Steps

With a clear view of upcoming events, Tom plans to leverage this information for various analytical and operational improvements at his Pizzeria:

* **Data Analysis and Reporting**: Tom will load event data into Power BI to generate detailed reports and dashboards, following [using-event-data-in-power-bi.md](using-event-data-in-power-bi.md "mention") for step-by-step instructions.
* **Relevant Events**: Tom aims to pinpoint event categories that impact his business the most by using [Demand Analysis](https://www.predicthq.com/support/beam-overview) in [Control Center](https://control.predicthq.com/beam). This will help him allocate his resources more effectively.
* **Forecast Future Orders**: Recognizing the benefits of predictive analytics, Tom is considering developing a demand forecasting model using [Power BI’s AutoML feature with PredictHQ’s event data](../../integrations/third-party-integrations/integrate-with-a-demand-forecast-in-powerbi.md). This will help him better predict customer flows and optimize resource planning.

## Conclusion

This tutorial has demonstrated how to effectively use the Events API to filter out noise and identify events that are most relevant to your business. From configuring query parameters to interpreting the responses, you now have the tools to make informed decisions and strategically plan for future opportunities.
