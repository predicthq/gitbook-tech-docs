---
description: >-
  Working with dates, times and timezones can be hard.This guide aims to clarify
  how to work with these with PredictHQ data.
---

# Working with Dates, Times and Timezones

## Converting to Local Time

Dates and times on events provided by the Event API are in UTC - not event local time. To find out the time of the event (in the same timezone as the event, i.e. local time) you need to convert from UTC.

Below is an example of converting UTC time to local time using the `pytz` library in Python.

```python
from datetime import datetime
import pytz

# Example dates for an event retrieved from Events API.
# The rest of the event data has been stripped out for brevity.
event = {
  "start": "2023-10-23T13:00:00Z",
  "end": "2023-10-24T12:59:59Z",
  "timezone": "Australia/Sydney",
}

# Function to convert a UTC datetime string to a local datetime string using the given timezone
def convert_to_local(date_str, timezone_str):
    utc_dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    target_tz = pytz.timezone(timezone_str)
    local_dt = utc_dt.astimezone(target_tz)
    return local_dt.isoformat()

event["start_local"] = convert_to_local(event["start"], event["timezone"])
event["end_local"] = convert_to_local(event["end"], event["timezone"])

print(event)
```

Using the code above we'd see `start_local` and `end_local` as below:

```json
{
  "start": "2023-10-23T13:00:00Z",
  "end": "2023-10-24T12:59:59Z",
  
  "start_local": "2023-10-24T00:00:00+11:00",
  "end_local": "2023-10-24T23:59:59+11:00",
  
  "timezone": "Australia/Sydney"
}
```

Dates are a little more complex and the rest of this guide will help you understand how dates are represented in our data.

## Date Concepts

Internally, we have the concept of different date types for events. We don't expose these date types directly but are exposed indirectly and this guide will demonstrate how to understand dates, times and timezones on events. The different date types we refer to internally are:

* Fixed Date
* Fixed Time
* Floating Date

### Fixed Date

This concept refers to events that are known to happen on a certain date (including multi-day events) but the start and end times are not known. These events are represented in UTC and have a local start time of 00:00:00 and local end time of 23:59:59 as well as a known timezone.

```json
{
  "start": "2023-10-23T13:00:00Z",
  "end": "2023-10-24T12:59:59Z",
  "timezone": "Australia/Sydney",
  ...
}
```

The above event is happening on Tue, 24 Oct 2023 (a single day) and using the `convert_to_local` function from the earlier Python code would produce:

```json
{
  "start": "2023-10-23T13:00:00Z",
  "end": "2023-10-24T12:59:59Z",
  
  "start_local": "2023-10-24T00:00:00+11:00",
  "end_local": "2023-10-24T23:59:59+11:00",
  
  "timezone": "Australia/Sydney"
}
```

The `start_local` and `end_local` fields show the event spans the entire day of October 24th, 2023 in the Australia/Sydney timezone.

### Fixed Time

Refers to events covering an exact time range. The start and end times are known (or predicted). These events are represented in UTC and have a timezone.&#x20;

```json
{
  "start": "2023-11-09T08:00:00Z",
  "end": "2023-11-09T09:30:00Z",
  "timezone": "Australia/Melbourne",
  ...
}
```

Using the same `convert_to_local` function from earlier we get:

```json
{
  "start": "2023-11-09T08:00:00Z",
  "end": "2023-11-09T09:30:00Z",
  
  "start_local": "2023-11-09T19:00:00+11:00",
  "end_local": "2023-11-09T20:30:00+11:00",
  
  "timezone": "Australia/Melbourne",
}
```

Showing the event is scheduled from 7:00 PM to 8:30 PM on November 9th, 2023 in the Australia/Melbourne timezone.

### Floating Date

Refers to events that happen on a particular date regardless of timezone. E.g., USA Independence Day is 4th of July regardless of timezone. The way we represent this concept is by setting the `timezone` to `null` as in the following example:

```json
{
  "start": "2024-07-04T00:00:00Z",
  "end": "2024-07-04T23:59:59Z",
  "timezone": null,
  ...
}
```

When the `timezone` field is `null` like this you don't need to convert the start/end times.

## Predicted End Times

Many events don't have scheduled end times, for many of these events we provide a `predicted_end_time` field. Below is an example of what this might look like on an event. Note that the `start` and `end` values are exactly the same - this suggests we know the start time but not the scheduled end time, hence why we have provided a `predicted_end` value.

```json
{
  "start": "2024-09-29T19:05:00Z",
  "end": "2024-09-29T19:05:00Z",
  "predicted_end": "2024-09-29T21:50:00Z",
  "timezone": "America/New_York",
  ...
}
```

