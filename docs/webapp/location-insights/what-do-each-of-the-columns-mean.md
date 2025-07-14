---
description: Understanding the Location Insights statistics
---

# What Do Each of the Columns Mean?

Location Insights shows a summary of all event information happening in the next 90 days at a location. This data is shown in the list view and on the location insights pages for each saved location. For a **Center point & radius** location, this covers all events occurring within the radius or overlapping the radius.

* **Predicted attendance** shows the number of people our advanced demand intelligence system predicts will attend all the attended events at a location in the next 90 days. This includes our seven attended event categories: sports, conferences, expos, concerts, festivals, performing arts, and community events. See attended-based events on our [event categories page](https://www.predicthq.com/intelligence/data-enrichment/event-categories). Under the hood, we use our [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features) which has advanced logic for aggregating all the attended events together. See also: [Predicted Attendance](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/predicthq-data/predicted-attendance).
* **Attended events** are the count of all attended events happening at the location in the next 90 days. These are the same seven attended categories used for Predicted attendance. See the [event categories page](https://www.predicthq.com/intelligence/data-enrichment/event-categories) for more details.
* **Non-attended events** show the count of all non-attended events happening at the location in the next 90 days. This includes public holidays, observances, school holidays, Academic Events, Politics, and Daylight Savings. See Non-Attendance-Based Events on the [event categories page](https://www.predicthq.com/intelligence/data-enrichment/event-categories) for more details.
* **Unscheduled events** show the count of all unscheduled events happening at the location in the next 90 days. This includes the following categories: severe weather, disasters, terror, health warnings, and airport delays. See Unscheduled Events on the [event categories page](https://www.predicthq.com/intelligence/data-enrichment/event-categories) for more details.
* **Predicted Event Spend** shows the total spend for the location for the next 90 days across all supported industries. This is based on the sum of spend for all the events happening at the location. See [Predicted Event Spend](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/predicthq-data/predicted-event-spend) for more details.

This data is typically updated every hour with any event changes – for example; canceled events, or new events that are found at the location.
