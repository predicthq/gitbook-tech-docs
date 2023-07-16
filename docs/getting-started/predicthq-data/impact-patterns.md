# Impact Patterns

Also known as “Demand impact patterns”. This field shows impact for leading days (days before the event), lagging days (days after an event) and the days the event occurs.\
\
`impact_patterns` is an array of impact pattern objects. The same event can have different impact patterns for different industry verticals. It contains the following fields:

* `vertical` - The industry vertical the impact pattern applies to. The initial release is for the retail industry so this field will show `retail`. Future releases could apply to other industries like accommodation.
* `impact_type` - Indicates the type of impact shown in the impact pattern. The current version supports PHQ rank only (`phq_rank`). Future versions could show the impact to attendance or other values.

`impacts` is an array of objects with one entry for each day that contains the following values:

* `date_local` - the date in the local timezone of the event.
* `value` - the value of the `impact_type` for that given day. For example, if the `impact_type` was `phq_rank` the value would be the PHQ Rank value on the given day.
* `position` - can be `leading`, `event_day` or `lagging`. `leading` are the days before the event occurs, `event_day` are the days the event occurs and `lagging` are the days after the event has occurred.

```json
[
  {
    "date_local": "2022-01-08",
    "value": 10,
    "position": "leading"
  },
  {
    "date_local": "2022-01-09",
    "value": 21,
    "position": "event_day"
  },
  ...
]
```
