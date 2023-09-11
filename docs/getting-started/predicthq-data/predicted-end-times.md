# Predicted End Times

Many events don’t have end times, which is critical information for our transport and on-demand customers. For example, for sports events, around 80% or more of source event data doesn’t have a known end time.

This is usually because end times for a sports game or a concert are recorded after the event finishes. Yet many of our transport customers need a predicted end time for future scheduled events (which means providing the end time before the event finishes).

The end time and duration of an event is a key piece of information for event data. The goal of this feature is to increase our end-time coverage.

The Predicted End Times feature uses machine learning and our intelligent algorithms to predict event end times. The goal is that customers can use the predicted end-time value where an actual known end-time is not present.

Predicted End Times covers two categories which are [**sports**](https://docs.predicthq.com/getting-started/predicthq-data/event-categories/attendance-based-events#sports) and [**performing arts**](https://docs.predicthq.com/getting-started/predicthq-data/event-categories/attendance-based-events#performing-arts).

For sports events Predicted End Times covers 8 sports (American football, Basketball, Baseball, Ice-hockey, NASCAR, Soccer, Rugby, and Australian rules football).&#x20;

For performing arts events all performing arts events that don't have an actual end time have a predicted end time.

Example Use Cases

* **Workforce Optimization**: For transportation companies if you want to arrange transportation for people leaving an event you can use Predicted End Times.
* **Demand Forecasting**: When forecasting the impact of events in certain time periods the end time of the event is required.

## How predicted end times are calculated

We use a combination of methods which are largely determined by the availability of historical data. For event types with historical data, we use machine learning methods including linear regression and quantile regression. These models use features such as gender, season, and leagues. For event types without historical data, we use research-based methods e.g. using the mean, using track and series estimates for NASCAR. As a result, our predictions for these events may be less robust. Across all sports types, we cover Professional, College, and International types, where applicable.

| Sport               | Professional   | College        | International  |
| ------------------- | -------------- | -------------- | -------------- |
| Ice-hockey          | Model-based    | Research-based | Model-based    |
| Rugby               | Model-based    | Model-based    | Model-based    |
| Basketball          | Model-based    | Research-based | Research-based |
| Australian Football | Model-based    | Model-based    | Model-based    |
| American Football   | Model-based    | Model-based    | Research-based |
| Football/Soccer     | Research-based | Research-based | Research-based |
| Baseball            | Model-based    | Research-based | Research-based |
| NASCAR              | Research-based | Research-based | Research-based |



For performing arts events we use research-based methods to calculate predicted end times.

## Predicted End Times in PredictHQ API

The events endpoint of the PredictHQ API has been updated with changes for the Predicted End times feature:

* You can sort events on the predicted end-time value by using the `sort` parameter with a value of `predicted_end` or `-predicted_end`.
* You can filter on predicted end times by specifying a date range with the `predicted_end.*` parameter.
* Predicted end time is returned as the `predicted_end` field in the events response data. This field will only be present if an actual end time is not available for the event and we have a predicted end time. The predicted end date of the event in ISO 8601 format.

**Note**: Predicted end time and all other start and end times are in UTC if the event time zone is provided, and in local time otherwise. For example, Independence Day falls on the 4th of July regardless of the timezone and will have a null time zone.

#### How to use the API

If an event does not have a valid end time then the predicted\_end field will be present in the response. To use Predicted End Times you can implement logic that checks if the predicted\_end field is present. The logic should be: - If the `predicted_end` field is present then use `predicted_end` field value for the event end time. - If the `predicted_end` field is not present use the `end` field for the event end time.

You can also use the `sort` parameter to sort by the end time and the predicted\_end where needed.

Note

* Predicted end times is a predicted value, not an actual end time value. It is based on various machine learning models and statistical methods. We aim to have good accuracy on average but there is a margin of error in the value. Please take this into account when you use the value.
* For events that don’t have an end time the end time is set to the same as the start time in our events API response.

## Examples

### Event with a Predicted End time

```json
{
    "id": "hHkH8zLEYGA2zBH3ka",
    "title": "NBA - Los Angeles Lakers vs Sacramento Kings",
    "description": "",
    "category": "sports",
    ...
    "start": "2020-04-15T02:30:00Z",
    "end": "2020-04-15T02:30:00Z",
    "predicted_end": "2020-04-15T04:50:00Z",
    "updated": "2019-08-13T06:21:03Z",
    "first_seen": "2019-08-13T02:25:35Z",
    ...
}
```

### Event with a scheduled end time

```json
{
    "id": "vaUVM7J4nwfNVngoxy",
    "title": "Washington Nationals vs Los Angeles Dodgers",
    ...
    "start": "2019-10-04T00:37:00Z",
    "end": "2019-10-04T04:01:15Z",
    "updated": "2019-10-07T02:58:30Z",
    "first_seen": "2019-08-06T07:01:03Z",
    ...
}
```
