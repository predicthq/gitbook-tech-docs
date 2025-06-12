---
description: Learn how to display events on a map for a specific location.
---

# Displaying Events on a Map

Events can significantly impact businesses. Understanding when and where events are scheduled helps businesses optimize operations, marketing strategies, and resource management. Maps provide a visual representation of these events, allowing for quick identification of regions of interest and potential impact zones. For example, [a ride-sharing platform](https://www.predicthq.com/blog/4-ways-event-data-enhances-rideshare-and-mobility-app-ui) can use this data to predict areas of high demand, directing drivers to where upcoming events are likely to increase the need for rides.

This tutorial demonstrates how to create a dynamic map using PredictHQ event data to visualize events geographically. It begins with a simple JavaScript example using [Leaflet](https://leafletjs.com/) and then looks at how to retrieve relevant events using PredictHQ's Events API. The goal is to provide a straightforward example to help you incorporate events into any map view.

## Use Cases

Visualization and Insights, Workforce Optimization

## Relevant Industries

Accommodation, Consumer Packaged Goods, Grocery and Supermarkets, Leisure, Travel and Tourism, Marketing and Advertising, Parking, Restaurants, Retail, Transportation and Delivery and Others

## Example Map

This section presents a simple example demonstrating the basic functionality of a map integrated with PredictHQ data. Explore this through the following Observable notebook:

{% embed url="https://observablehq.com/@predicthq/events-map-example" %}

{% hint style="info" %}
To experiment with this example, consider[ forking the notebook](https://observablehq.com/documentation/notebooks/forking). This allows you to edit and modify the code as needed. For more information on Observable notebooks, see this[ demo](https://observablehq.com/@observablehq/demo).
{% endhint %}

### Getting Started

An Access Token is required to access PredictHQ's APIs and run the notebook. Follow these [instructions](broken-reference) to obtain one if needed.

### Event Data

The event data used in this map is sourced from PredictHQ's Events API, which provides detailed, event-level information, including the title, dates, and location. This granularity makes the data ideal for mapping.

{% hint style="info" %}
For more information on the Events API, see this [documentation](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events).
{% endhint %}

### Parameters

For this example, [events are retrieved](https://observablehq.com/@predicthq/events-map-example#fetchEvents) from the Events API based on the following criteria:

1. **Date Range**: Events taking place within the next 7 days from today are considered to ensure the data remains current and actionable.
2. **Location**: The geographical focus is on San Francisco, offering a targeted view of local events.
3. **Categories**: The focus is on sports events and their potential to draw large crowds.
4. **Event Rank**: Priority is given to events with the largest predicted attendance, as indicated by their [PHQ Rank](../../predicthq-data/ranks/phq-rank.md). This ensures the map highlights the most significant events, providing a clear view of potential major draws in the area.

{% hint style="info" %}
For guidance on effectively querying the Events API, see [#customizing-event-data](displaying-events-on-a-map.md#customizing-event-data "mention") below.
{% endhint %}

### Map

This example displays the most impactful sports event in San Francisco for the upcoming week. Interact with the map by:

* Zooming in and out to view all events.
* Clicking on specific events for more details.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdFMd0QGP6NB67jU-826iGqRO-u5vNx4o4TEAKbgk9HI0uEJFLm-l84383lOPmK78hGVIEi_m5Jz8_Ed2H-qNVwBI0qFvBwjcaLGkDAvgX6jWsyGpiTU1CMUqV95V8AYfC21U8hlCqNr1QGcXLofXG8zjBf?key=Zcee3-lj9wWgy6r9JpJLQw" alt="" width="563"><figcaption><p>Interacting with the map</p></figcaption></figure>

### Geographic Features

Event coordinates are returned by the Events API in the `geo` field. It is formatted in GeoJSON format which means longitude is returned first, then latitude e.g. Downtown San Francisco is `[-122.39, 37.79]`, not `[37.79, -122.39]`.

The main focus of this example is on `point` type events, occurring at [specific locations](https://docs.predicthq.com/getting-started/guides/geolocation-guides/overview#basic-location). Events covering larger areas, such as parades, are classified as `polygon` or `multipolygon`. All relevant geometry information needed for rendering these types of events on a map is also contained within the `geo` field.

{% hint style="info" %}
For more information on how PredictHQ events are geographically represented, see this [overview](../geolocation-guides/overview.md).
{% endhint %}

### Exporting Code

The notebook can also be[ compiled and downloaded](https://observablehq.com/documentation/embeds/advanced#notebooks-as-es-modules) as a JavaScript module. To do this:

1. Use the notebook menu to select 'Export'.
2. Then choose 'Download code' for a local copy.

## Additional Examples

For examples of maps created in Python, explore these [demo apps](../streamlit-demo-apps.md). The source code for rendering events in these apps is available on GitHub. Check out [utils/map.py](https://github.com/predicthq/streamlit-parking-demo/blob/main/utils/map.py) and [map.py](https://github.com/predicthq/streamlit-parking-demo/blob/main/map.py) for the parking demo which provides a practical example of visualizing events with Python and [Streamlit](https://streamlit.io/).&#x20;

## Customizing Event Data

The event data retrieved from the Events API can be customized by adjusting parameters such as date range, location, and categories, among others.&#x20;

For detailed guidance on configuring these parameters to meet your specific requirements, refer to the [Define Query Parameters](filtering-and-finding-relevant-events.md#step-1.-define-query-parameters-for-the-events-api) section in [Filtering and Finding Relevant Events](filtering-and-finding-relevant-events.md). This tutorial provides step-by-step instructions on how to retrieve the most relevant event data for your needs.

## Conclusion

This tutorial has demonstrated how to create a dynamic map using PredictHQ's Events API, from retrieving event data to its geographic visualization. This approach provides key insights into the impact of events, enabling data-driven decision-making. Adapt the provided example to tailor the map to your specific operational requirements.
