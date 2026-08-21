---
description: >-
  How to interpret phq_attendance for multi-day events and avoid
  double-counting umbrella events when working with individual event records.
---

# Working with Multi-day and Umbrella Events

PredictHQ’s events data includes events of different duration, from events that may be less than an hour-long to events that can last more than a week. For our [7 attended event categories](https://www.predicthq.com/intelligence/data-enrichment/event-categories), we expose the actual or predicted attendance for events in our phq\_attendance field. The phq\_attendance field works slightly differently for different categories. For many categories, it is the total attendance for an event over its full duration. For other categories (like conferences), it reflects the daily attendance.

For example, the phq\_attendance for a big event like the [2019 Tour de France](https://events.predicthq.com/events/fXHXPzTVW5K9ZWxFnb) is 12,000,000 which represents the total attendance for the full duration of 22 days. It is not the daily attendance. The daily attendance for that event is closer to 545,000 people. Reading 12,000,000 as a single day's attendance would badly misrepresent the event's impact.

PredictHQ also handles cases where one event (child) belongs to another (parent). This type of event is called an Umbrella event. Umbrella events are often multi-day events but can also be single-day events with multiple sessions if the same attendees are expected, for example the games of a rugby sevens tournament. When looking at events it’s important to use either parent events or child events, but not both.

<figure><img src="../../../.gitbook/assets/umbrella-events.png" alt=""><figcaption></figcaption></figure>

This page covers how to interpret these events correctly when working with individual event records - event lists, explainability surfaces, and grounding corpora. For daily or weekly aggregations of any kind - model features, dashboards, analytics - use the [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features), which handles all of the complications on this page for you.

## Multi-Day Events

### Handling Attendance for Multi-Day Events

The [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) has advanced logic for handling multi-day events. For some categories, phq\_attendance is the daily attendance. For categories that have multi-day events, such as festivals, community events, expos, and sports, there is additional logic for how phq\_attendance is distributed to each day.

Below is an example of how phq\_attendance might be distributed for a golf tournament. This is a multi-day sports event so the phq\_attendance of 63,000 is the total attendance across the full duration. The daily attendance is not evenly distributed across the week as higher attendance is expected on the weekend. The Features API deals with distributing attendance across each day and takes into account uneven distributions.

<figure><img src="../../../.gitbook/assets/chart-sports.png" alt="" width="375"><figcaption></figcaption></figure>

For supported industries, the Features API goes further: [Predicted Impact Patterns](../../predicthq-data/impact-patterns.md) are daily impact curves derived from machine learning models trained on historical demand data, specific to event category and industry, extending into the lead-up and lag days around an event. This distribution logic is not reproducible with rules of thumb - which is why daily and weekly aggregations belong in the Features API rather than in your own pipeline.

### Interpreting phq\_attendance across categories

Our definition of multi-day events is: events that take place across more than one day, i.e. overlap on more than one calendar day, while single-day events take place within one day, i.e. start and end on the same calendar day.

When reading individual event records, interpret phq\_attendance as follows:

<table><thead><tr><th width="184">Category</th><th>What phq_attendance represents</th></tr></thead><tbody><tr><td>Concerts</td><td>Daily attendance. These events tend to be 1 day or less.</td></tr><tr><td>Performing Arts</td><td>Daily attendance. These events tend to be 1 day or less.</td></tr><tr><td>Conferences</td><td>Daily attendance, not total attendance.</td></tr><tr><td>Expos</td><td>Total attendance across the full event duration.</td></tr><tr><td>Sports</td><td>Total attendance across the full event duration.</td></tr><tr><td>Festivals</td><td>Total attendance across the full event duration.</td></tr><tr><td>Community</td><td>Total attendance across the full event duration.</td></tr></tbody></table>

## Umbrella Events

Umbrella events refer to the case where we have a parent event that contains one or more child events. For example, the [United States Formula 1 Grand Prix in 2019](https://events.predicthq.com/events/w7dYyrFwTUQGYE6euv) has child events for [the qualification](https://events.predicthq.com/events/hZ5fGHaxHKgJTBpqyQ), 3 practice events, [a concert](https://events.predicthq.com/events/N4LWVHvicH5YiCHQKe) that occurs at the Grand Prix, and the [actual race event](https://events.predicthq.com/events/5uRg7CqGu7DTtu4Rfk) (there are 12 child events in total). The parent event is for the entire Grand Prix that runs from the 1st of November to the 3rd of November 2019. Both the parent and child events are part of the wider Umbrella event.

Child events are indicated by the presence of the `parent_event` field. Child events will have a parent\_event\_id in this field indicating the id of the parent event. For example, the Formula 1 race child event is `5uRg7CqGu7DTtu4Rfk` and the Formula 1 parent event is `w7dYyrFwTUQGYE6euv`. The Formula 1 race child event has the following parent event info:

```json
{
  "id": "5uRg7CqGu7DTtu4Rfk",
  "parent_event": {
    "parent_event_id": "w7dYyrFwTUQGYE6euv"
  },
  "title": "Formula 1 2019 - United States Grand Prix 2019 - Race",
  "category": "sports",
  ...
}
```

{% hint style="info" %}
In the current release of Umbrella events you cannot yet find the child event IDs of a parent event via the API. This feature will be supported in a future release.
{% endhint %}

### **Why Umbrella Events Matter**

Any view built from individual event records has to account for Umbrella events, or the attendance of parent events and their child events is double-counted, producing inflated figures. For daily or weekly aggregations of any kind, use the [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) rather than aggregating records - see [Which API Should I Use?](../../core-concepts/which-api-should-i-use.md)

Looking at the earlier [US F1 Grand Prix in 2019](https://events.predicthq.com/events/w7dYyrFwTUQGYE6euv) example, the parent event spanning 3 days has a phq\_attendance of 258,000. The actual race event running for around 3 hours on the 3rd of November has a phq\_attendance of 120,000. If you count both the parent event and the race child event on the 3rd, you overcount the attendance - the same people are represented in both records.

<figure><img src="../../../.gitbook/assets/example-of-umbrella.svg" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Child event attendance may sometimes reflect more detailed attendance on the individual days of an event, rather than an even share of the parent event's total.
{% endhint %}

Another example can be seen when looking at the daily attendance for events in Las Vegas in 2019. In the example below there is the [World Rugby Sevens tournament](https://events.predicthq.com/events/iKKgf8suq5D5w89boJ) from the 1st of March 2019 to the 3rd of March 2019. The parent event is for the entire tournament and there are many child events for individual games and rounds in the tournament. By not accounting for Umbrella events you get a massive spike in attendance at that time. A peak of 1.4 million is seen around the 2nd of March because both the parent event and child events are being counted.

<figure><img src="../../../.gitbook/assets/graph-umbrella-events-double-counted.png" alt=""><figcaption><p>Example showing attendance being counted multiple times due to not handling Umbrella Events</p></figcaption></figure>

Once you take into account Umbrella events and remove double counting, the real attendance on that day is closer to 400,000.

<figure><img src="../../../.gitbook/assets/graph-umbrella-events-removed.png" alt=""><figcaption><p>Example showing correct attendance due to correct handling of Umbrella Events</p></figcaption></figure>

### **Using the Parent Filter in the Events API for Umbrella Events**

See the documentation on the [parent filter](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events) for umbrella events.

You can use this filter with the events API to only get parent events or only retrieve child events from the Events API.

Note that in the API **parent** events includes events that have child events and also events without any child events. So, for the API filter parent events also include non-umbrella events. **Child** events are defined as only those events that have a link to a parent event.

### **Definitions**

* **Parent event** - Spans the full duration of an event and may have child events as part of it. Many parent events will be multi-day events such as the Olympics, a Formula 1 weekend, or a multi-day festival. These events will have a parent event for the whole event - like an event for the entire 2020 Olympic Games in Tokyo. Other examples include an event for the entire US Formula 1 or a rugby sevens tournament.
* **Child events** - Individual events that are part of a parent event. For example, day 1 of the 2020 Olympic Games or the “Men’s 100m finals” in the Olympic Games. Or the Formula 1 qualification and practice events. All of these are examples of child events.
