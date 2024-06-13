# Impact Patterns

Also known as “Demand impact patterns”. This field shows the impact for leading days (days before the event), lagging days (days after an event), and the days the event occurs. Below is a visual representation of impact patterns.

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

You can use Demand Impact Patterns in your demand forecasting so that your machine learning models will take account of the impact on leading and lagging days. In our testing we have found using impact patterns increases forecasting accuracy.&#x20;

#### Vertical, type, and category mapping

Impact Patterns are available for the following industry segments and categories:

| Vertical        | Impact Type      | Category          |
| --------------- | ---------------- | ----------------- |
| `retail`        | `phq_rank`       | `severe-weather`  |
| `accommodation` | `phq_attendance` | `community`       |
|                 |                  | `concerts`        |
|                 |                  | `conferences`     |
|                 |                  | `expos`           |
|                 |                  | `festivals`       |
|                 |                  | `performing-arts` |
|                 |                  | `sports`          |
| `hospitality`   | `phq_attendance` | `community`       |
|                 |                  | `concerts`        |
|                 |                  | `conferences`     |
|                 |                  | `expos`           |
|                 |                  | `festivals`       |
|                 |                  | `performing-arts` |
|                 |                  | `sports`          |

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

## Impact pattern coverage by industry

The table below lists the categories and industries which we have impact patterns for.

<table data-header-hidden><thead><tr><th width="155"></th><th width="172"></th><th width="127"></th><th width="166"></th><th></th></tr></thead><tbody><tr><td><strong>Type</strong></td><td><strong>Category</strong></td><td><strong>Industries</strong></td><td></td><td></td></tr><tr><td></td><td></td><td>Food and Beverage</td><td>Accommodation</td><td>Retail</td></tr><tr><td>Attended</td><td>Community</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td></td><td>Concerts</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td></td><td>Conferences</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td></td><td>Expos</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td></td><td>Festivals</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td></td><td>Performing Arts</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td></td><td>Sports</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>Non-attended</td><td>Public Holidays</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td></td><td>Severe Weather</td><td> </td><td> </td><td>Y</td></tr><tr><td></td><td>Observances</td><td>Y</td><td>Y</td><td>Y</td></tr></tbody></table>
