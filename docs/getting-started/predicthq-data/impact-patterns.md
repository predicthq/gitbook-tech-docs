# Impact Patterns

Also known as “Demand impact patterns”. This field shows the impact of leading days (days before the event), lagging days (days after an event), and the days the event occurs. For example, if someone is taking a flight to a location to attend a concert, they are typically not going to be arriving on the day of the event. They will often arrive a couple of days before and check into your hotel before the concert begins. The demand impact pattern for accommodation reflects the fact that this demand will be felt before the event starts and often after it ends. Impact patterns are industry-specific and reflect the varying leading and lagging impact of events on different industries. Below is a visual representation of impact patterns.&#x20;

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

You can use Demand Impact Patterns in your demand forecasting so that your machine learning models will take account of the impact on leading and lagging days. In our testing we have found using impact patterns increases forecasting accuracy.&#x20;

#### Vertical, type, and category mapping

Impact Patterns are available for the following industry segments and categories:

{% tabs %}
{% tab title="Accommodation" %}
| Impact Type      | Category          |
| ---------------- | ----------------- |
| `phq_rank`       | `public-holidays` |
|                  | `observances`     |
| `phq_attendance` | `community`       |
|                  | `concerts`        |
|                  | `conferences`     |
|                  | `expos`           |
|                  | `festivals`       |
|                  | `performing-arts` |
|                  | `sports`          |
{% endtab %}

{% tab title="Retail" %}
| Impact Type      | Category          |
| ---------------- | ----------------- |
| `phq_rank`       | `public-holidays` |
|                  | `observances`     |
|                  | `severe-weather`  |
| `phq_attendance` | `community`       |
|                  | `concerts`        |
|                  | `conferences`     |
|                  | `expos`           |
|                  | `festivals`       |
|                  | `performing-arts` |
|                  | `sports`          |
{% endtab %}

{% tab title="Restaurants" %}
| Impact Type      | Category          |
| ---------------- | ----------------- |
| `phq_rank`       | `public-holidays` |
|                  | `observances`     |
| `phq_attendance` | `community`       |
|                  | `concerts`        |
|                  | `conferences`     |
|                  | `expos`           |
|                  | `festivals`       |
|                  | `performing-arts` |
|                  | `sports`          |
{% endtab %}
{% endtabs %}

<table><thead><tr><th width="212.33333333333331">Vertical</th><th>Impact Type</th><th>Category</th></tr></thead><tbody><tr><td><code>retail</code></td><td><code>phq_rank</code></td><td><code>severe-weather</code></td></tr><tr><td><code>retail</code></td><td><code>phq_attendance</code></td><td><code>community</code></td></tr><tr><td><code>retail</code></td><td><code>phq_attendance</code></td><td><code>concerts</code></td></tr><tr><td><code>retail</code></td><td><code>phq_attendance</code></td><td><code>conferences</code></td></tr><tr><td><code>retail</code></td><td><code>phq_attendance</code></td><td><code>expos</code></td></tr><tr><td><code>retail</code></td><td><code>phq_attendance</code></td><td><code>festivals</code></td></tr><tr><td><code>retail</code></td><td><code>phq_attendance</code></td><td><code>performing-arts</code></td></tr><tr><td><code>retail</code></td><td><code>phq_attendance</code></td><td><code>sports</code></td></tr><tr><td><code>accommodation</code></td><td><code>phq_attendance</code></td><td><code>community</code></td></tr><tr><td><code>accommodation</code></td><td><code>phq_attendance</code></td><td><code>concerts</code></td></tr><tr><td><code>accommodation</code></td><td><code>phq_attendance</code></td><td><code>conferences</code></td></tr><tr><td><code>accommodation</code></td><td><code>phq_attendance</code></td><td><code>expos</code></td></tr><tr><td><code>accommodation</code></td><td><code>phq_attendance</code></td><td><code>festivals</code></td></tr><tr><td><code>accommodation</code></td><td><code>phq_attendance</code></td><td><code>performing-arts</code></td></tr><tr><td><code>accommodation</code></td><td><code>phq_attendance</code></td><td><code>sports</code></td></tr><tr><td><code>accommodation</code></td><td><code>phq_rank</code></td><td><code>public-holidays</code></td></tr><tr><td><code>accommodation</code></td><td><code>phq_rank</code></td><td><code>observances</code></td></tr><tr><td><code>hospitality</code> (food and beverage)</td><td><code>phq_attendance</code></td><td><code>community</code></td></tr><tr><td><code>hospitality</code> </td><td><code>phq_attendance</code></td><td><code>concerts</code></td></tr><tr><td><code>hospitality</code> </td><td><code>phq_attendance</code></td><td><code>conferences</code></td></tr><tr><td><code>hospitality</code> </td><td><code>phq_attendance</code></td><td><code>expos</code></td></tr><tr><td><code>hospitality</code> </td><td><code>phq_attendance</code></td><td><code>festivals</code></td></tr><tr><td><code>hospitality</code> </td><td><code>phq_attendance</code></td><td><code>performing-arts</code></td></tr><tr><td><code>hospitality</code> </td><td><code>phq_attendance</code></td><td><code>sports</code></td></tr><tr><td><code>hospitality</code> </td><td><code>phq_rank</code></td><td><code>public-holidays</code></td></tr><tr><td><code>hospitality</code> </td><td><code>phq_rank</code></td><td><code>observances</code></td></tr></tbody></table>

## Impact Patterns in the Events API

Impact patterns are returned in the [Events API](../../api/events/) response in the `impact_patterns` field. This shows the Impact Pattern for each event. Below are the details of the data structure of that field.

`impact_patterns` is an array of impact pattern objects. The same event can have different impact patterns for different industry verticals. It contains the following fields:

* `vertical` - The industry vertical the impact pattern applies to.&#x20;
* `impact_type` - Indicates the type of impact shown in the impact pattern. This will apply to either `phq_rank` or `phq_attendance`, depending on the vertical.

`impacts` is an array of objects with one entry for each day that contains the following values:

* `date_local` - the date in the local timezone of the event.
* `value` - the value of the `impact_type` for that given day. For example, if the `impact_type` was `phq_rank` the value would be the PHQ Rank value on the given day. In the case for `accommodation` or `hospitality` where the `impact_type` is `phq_attendance`, this is what will be presented in this field.&#x20;
* `position` - can be `leading`, `event_day` or `lagging`. `leading` are the days before the event occurs, `event_day` are the days the event occurs, and `lagging` are the days after the event has occurred.

```json
"impact_patterns": [
    {
        "vertical": "accommodation",
        "impact_type": "phq_attendance",
        "impacts": [
            {"date_local": "2018-02-26", "value": 14250, "position": "leading"},
            {"date_local": "2018-02-27", "value": 14250, "position": "leading"},
            {"date_local": "2018-02-28", "value": 85500, "position": "leading"},
            {"date_local": "2018-03-01", "value": 95000, "position": "event_day"},
            {"date_local": "2018-03-02", "value": 95000, "position": "event_day"},
            {"date_local": "2018-03-03", "value": 95000, "position": "event_day"},
            {"date_local": "2018-03-04", "value": 95000, "position": "event_day"},
            {"date_local": "2018-03-05", "value": 33250, "position": "lagging"},
            {"date_local": "2018-03-06", "value": 4750, "position": "lagging"},
        ],
    }, {
        "vertical": "hospitality",
        "impact_type": "phq_attendance",
        "impacts": [
            {"date_local": "2018-02-26", "value": 16151, "position": "leading"},
            {"date_local": "2018-02-27", "value": 40850, "position": "leading"},
            {"date_local": "2018-02-28", "value": 40850, "position": "leading"},
            {"date_local": "2018-03-01", "value": 95000, "position": "event_day"},
            {"date_local": "2018-03-02", "value": 95000, "position": "event_day"},
            {"date_local": "2018-03-03", "value": 95000, "position": "event_day"},
            {"date_local": "2018-03-04", "value": 95000, "position": "event_day"},
            {"date_local": "2018-03-05", "value": 14250, "position": "lagging"},
        ],
    }
]

```

or for `retail` for severe weather events

```json
"impact_patterns": [
    {
        "vertical": "retail",
        "impact_type": "phq_rank",
        "imputed_impact_pattern": true,
        "impact_range_start_dt": "2018-02-03T15:00:00+00:00",
        "impact_range_end_dt": "2018-02-07T14:59:59+00:00",
        "impacts": [
            {"date_local": "2018-02-04", "value": 64, "position": "event_day"},
            {"date_local": "2018-02-05", "value": 64, "position": "event_day"},
            {"date_local": "2018-02-06", "value": 64, "position": "event_day"},
            {"date_local": "2018-02-07", "value": 64, "position": "event_day"},
        ],
    }
]

```

## Impact Patterns in the Features API

You can also use Demand Impact Patterns with the Features API. The features API provides pre-built machine learning features for demand forecasting. See the[ features API ](../../api/features/get-features.md#impact-patterns)documentation. Use the features for your industry to get more accurate forecasting results. We have a generic feature without impact patterns for sports called `phq_attendance_sports` but that does not include impact patterns so only shows the impact on the days of the event. In order to use impact patterns with the features API you need to use the impact pattern features. For example, if you are in the accommodation segment and are using the features API to find the impact of sports events on your location you would use `phq_attendance_sports_accommodation`.  If you were in the Hospitality Segment you would use `phq_attendance_sports_hospitality`.
