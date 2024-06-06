---
description: >-
  Learn how to create a heatmap-styled calendar to display event attendance for
  a location.
---

# Displaying Events in a Heatmap Calendar

Event data provides critical insights into activities that can impact businesses. By tracking when and where events occur, businesses can optimize operations, marketing, and resource allocation. For instance, a surge in local events could indicate an increase in customer traffic, enabling businesses to adjust staffing and inventory levels accordingly.

This tutorial demonstrates how to use PredictHQ event data to build a heatmap calendar, starting with a simple build using [JavaScript D3](https://d3js.org/), followed by guidance on filtering and retrieving the underlying event data from PredictHQ's Features API. The goal is to provide a simple example so you can incorporate events into your own calendar view.

## Use Cases

Visualization and Insights

## Relevant Industries

Accommodation, Consumer Packaged Goods, Grocery and Supermarkets, Leisure, Travel and Tourism, Marketing and Advertising, Parking, Restaurants, Retail, Transportation and Delivery and Others

## Heatmap Calendars

Heatmap calendars display data density over time, making it easier to identify patterns and trends, such as busy days. This visual tool allows users to quickly view upcoming peak periods at a glance. For example, a hotel booking platform might use a heatmap calendar to visualize peak booking periods associated with local events, aiding in pricing strategy, inventory management, and customer satisfaction by preempting high-demand times.

## Example Calendar

This section goes through a simple example to demonstrate the basic functionality of a heatmap calendar and the integration of PredictHQ data. Explore the example through the following Observable notebook:

{% embed url="https://observablehq.com/@predicthq/features_api_heatmap" %}

{% hint style="info" %}
To experiment with this example, consider [forking the notebook](https://observablehq.com/documentation/notebooks/forking). This allows you to edit and modify the code as needed. For more information on Observable notebooks, see this [demo](https://observablehq.com/@observablehq/demo).
{% endhint %}

### Getting Started

An Access Token is required to access PredictHQ's APIs and run the notebook. Follow these [instructions](../../api-quickstart.md) to obtain one if needed.

### Event Data

Powered by aggregated event data from the [Features API](https://www.predicthq.com/apis/features-api), the heatmap calendar displays the total attendance per day. Selecting a specific day reveals additional event details via the [Events API](https://www.predicthq.com/apis/event-api), adding an interactive layer to the experience.

To view the code used to call the Features API, Events API, and other functions (if not already pinned):

* Click on the left margin of the cells in the Observable notebook.
* Alternatively, click 'Edit' in the cell menu.

{% hint style="info" %}
For more information on the Features API, see this [intro guide](../features-api-guides/increase-accuracy-with-the-features-api.md).
{% endhint %}

### Specifying Parameters

* Start Date: Set the start date for the period of interest.
* Location: Select one of the predefined locations.&#x20;
* Categories: Choose the event categories to consider.&#x20;

{% hint style="info" %}
For guidance on effectively querying the Features API, see [#customizing-event-data](displaying-events-in-a-heatmap-calendar.md#customizing-event-data "mention") below.
{% endhint %}

### Calendar

The calendar updates automatically based on the specified parameters. In this example, the intensity of the shading on the calendar reflects the total attendance for each day, reflecting how busy each day is. Interact with the calendar by:

* Hovering over the days to reveal more detailed information about the events.
* Clicking on specific days to surface the specific events occurring, providing more granular details.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXe91XOWCl6CkoPUeqz46MlUxCvuzyakT2cKIeKaRUhM8LNXaZf-dkjDmKZ66xSHw8OrJmvlLQcZrP4ZlwU4LC9A7O83H1bGpJ4vEdpJwHwXcceBx-adNwQV7GcBHdMU5NssX8zGHEkraTe28PGHZqLdFpGI?key=yHYQOK_XUxkGtvg9Am0g5g" alt="" width="563"><figcaption><p>Interacting with the heatmap calendar</p></figcaption></figure>

### Exporting Code

The notebook can also be [compiled and downloaded](https://observablehq.com/documentation/embeds/advanced#notebooks-as-es-modules) as a JavaScript module. To do this:

1. Use the notebook menu to select 'Export'.
2. Then choose 'Download code' for a local copy.

### Extension

Another approach to using calendars is to showcase the most impactful events, including links to their respective pages on Control Center. This method involves fetching event data from the [Events API](../../../api/events/search-events.md), sorting by attendance, and then directly displaying the top events on the calendar.

{% hint style="info" %}
For more information on using the Events API, see [filtering-and-finding-relevant-events.md](filtering-and-finding-relevant-events.md "mention").
{% endhint %}

## Customizing Event Data

This section provides guidance on how to customize the underlying event data using the Features API. Tailor your event data by specifying the following [fields](../../../api/features/get-features.md#request-body):

### Date Range

* Define a date range for the period of interest.
* Configuration: Use the `active` field.

### Location of Interest

* Determine the geographical area for which event data is required.&#x20;
* Configuration: Use the `location` field to specify a latitude, longitude, and radius or place ID for a specific city or region (as in the above example).
* Guidance: For details on how to set locations, refer to [#location-type](../industry-specific-event-filters.md#location-type "mention").&#x20;

### Event Categories

* Identify the types of events of interest, such as concerts, sports, or community events.
* Configuration: Add `<feature_name>` to the request body, specifying `stat` and `phq_rank` as needed (see next).&#x20;
* Guidance: Start with [features](../../../api/features/get-features.md#available-features) prefixed by `phq_attendance` for [attendance-based categories](../../predicthq-data/event-categories/attendance-based-events.md); other categories may require additional adjustments. For details on how to set event categories, refer to [#relevant-event-categories](../industry-specific-event-filters.md#relevant-event-categories "mention").

### Aggregation Statistic

* Choose how to aggregate event data at the daily level.
* Configuration: Use the `stat` field under `<feature_name>`.
* Guidance: Set as `sum` for visualizing the total daily attendance, which offers insights into people movement. Set as `count` to monitor the daily count of events, though it should be noted that this does not reflect event attendance or size.

### Minimum Event Rank

* Set a threshold to filter out small events that are unlikely to have a significant impact based on [PHQ Rank](https://docs.predicthq.com/getting-started/predicthq-data/ranks/phq-rank).
* Configuration: Use the `phq_rank` field under `<feature_name>`.
* Guidance: For details on how to set the minimum event rank, refer to [#minimum-phq-rank](../industry-specific-event-filters.md#minimum-phq-rank "mention").

{% hint style="info" %}
For an example of calling the API in JavaScript, see [here](https://observablehq.com/@predicthq/features\_api\_heatmap#data). For more information on using the Features API, see these [guides](../features-api-guides/).
{% endhint %}

## Conclusion

This tutorial has demonstrated how to create a heatmap calendar with PredictHQ’s APIs, from fetching event data to visualizing it interactively. These techniques provide valuable insights into event impact, supporting informed, data-driven decisions. Adapt the provided example and customize the heatmap to align with your specific operational needs.&#x20;

\
