# Increase Accuracy with the Features API

{% embed url="https://www.youtube.com/watch?v=FpTUVdQC7hw" %}
Features API Product Demo
{% endembed %}

Once you’ve familiarized yourself with our data, you’ll likely find that focusing on individual spikes often leads to a data set too small to accurately correlate. By doing it at an aggregate level, a data science team will be looking at the volume of spike days to prove a correlation between demand and events based on category features.

Features API aggregates PHQ Attendance figures, PHQ Viewership figures and PHQ Rank counts (in buckets by rank range) for a given category feature in a particular location on a given day, and returns desired statistics. These evaluated statistics can be used to quickly gauge and understand the demand impact on a location for a given day for a particular category. For example, at a future date in Sydney, there is a major sports game, a street fair, an international film festival, the Symphony orchestra playing, and more. The combined impact of all these events might result in a total aggregate attendance (when the various category aggregated attendance values are summed up) score of 150,000 and this could be across a hundred events or more. This represents a prediction of 150,000 people attending events on that day in the location.

The Features API returns requested statistical values (`sum`, `count`, `average`, `min`, `max`, `median`, `std_dev`) per day for a specified date range, across a specified attendance category feature - _see_ [PHQ Attendance Response](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features). Similarly, Features API returns requested statistical values, across a specified viewership category feature. For non-attendance-based events the rank of those events impacting that location on those days are bucketed into a relevant rank range in the response for evaluation.

See [the API documentation](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) for more details on the API. See also [this tutorial](../tutorials/improving-demand-forecasting-models-with-event-features.md) for how to incorporate features from the Features API into demand forecasting models.

### Features API Endpoint

{% embed url="https://www.youtube.com/watch?v=zlw4ky5NjbA" %}
How to use Features API
{% endembed %}

{% hint style="success" %}
**Recommended: use `beam.analysis_id`**\
The most reliable way to call the Features API is by supplying a `beam.analysis_id`. This automatically applies the correct location boundary (from your Saved Location), selects only the event categories that materially drive demand at that location, and applies calibrated rank thresholds — no manual configuration needed. [Run Beam first](../beam-guides/), then pass the returned `analysis_id` to the Features API.
{% endhint %}

#### With a Beam Analysis ID (Recommended)

Supplying `beam.analysis_id` automatically configures the location, feature selection, and rank filters from your Beam results. You do not need to specify individual feature names or a location separately.

```python
import requests

data = {
    "active": {
        "gte": "2019-11-16",
        "lte": "2019-11-27"
    },
    "beam": {
        "analysis_id": "$ANALYSIS_ID"
    }
}

response = requests.post(
    url="https://api.predicthq.com/v1/features/",
    headers={
      "Authorization": "Bearer $API_TOKEN",
      "Accept": "application/json"
    },
    json=data
)

print(response.json())
```

#### Without Beam (Manual Configuration)

If you haven’t run Beam yet, you can configure the Features API manually by specifying a location and the feature names you want. Use a `saved_location_id` for location (preferred), or provide a `place_id` or lat/lon with radius. Choose feature names based on your industry’s [recommended categories](../industry-specific-event-filters.md) until you can run Beam.

{% tabs %}
{% tab title="python" %}
```python
import requests

data = {
    "active": {
        "gte": "2019-11-16",
        "lte": "2019-11-27"
    },
    "location": {
        "saved_location_id": "$SAVED_LOCATION_ID"
    },
    "phq_attendance_conferences": {
        "stats": [
            "min",
            "max"
        ]
    },
    "phq_attendance_sports": {
        "stats": ["count", "std_dev", "median"],
        "phq_rank": { 
            "gt": 50
        }    
    },
    "phq_attendance_concerts": True,
    "phq_rank_public_holidays": True
}

response = requests.post(
    url="https://api.predicthq.com/v1/features/",
    headers={
      "Authorization": "Bearer $API_TOKEN",
      "Accept": "application/json"
    },
    json=data
)

print(response.json())
```


{% endtab %}

{% tab title="python sdk" %}
```python
from predicthq import Client

phq = Client(access_token="$API_TOKEN")

for feature in phq.features.obtain_features(
        active__gte="2019-11-16",
        active__lte="2019-11-27",
        location__saved_location_id="$SAVED_LOCATION_ID",
        phq_attendance_conferences__stats=["min", "max"],
        phq_attendance_sports__stats=["count", "std_dev", "median"],
        phq_attendance_sports__phq_rank={
            "gt": 50
        },
        phq_attendance_concerts=True,
        phq_rank_public_holidays=True
):
    print(feature.date, feature.phq_attendance_conferences.stats.min, 
        feature.phq_attendance_conferences.stats.max,
        feature.phq_attendance_sports.stats.count,
        feature.phq_attendance_sports.stats.std_dev,
        feature.phq_attendance_sports.stats.median,
        feature.phq_attendance_concerts.stats.count,
        feature.phq_attendance_concerts.stats.sum,
        feature.phq_rank_public_holidays.rank_levels)
```


{% endtab %}
{% endtabs %}



A snippet of the full results are shown below:

```json
{
  "results": [
    {
      "date": "2020-02-01",
      "phq_attendance_community": {
        "stats": {
          "count": 24,
          "sum": 3135,
          "avg": 130.625
        }
      },
      "phq_attendance_concerts": {
        "stats": {
          "count": 38,
          "sum": 25478,
          "avg": 670.4736842105264
        }
      },
      "phq_attendance_conferences": {
        "stats": {
          "count": 2,
          "sum": 5100,
          "avg": 2550.0
        }
      },
      "phq_attendance_sports": {
        "stats": {
          "count": 6,
          "sum": 34259,
          "avg": 5709.833333333333
        }
      },
      "phq_viewership_sports_american_football_nfl": {
        "stats": {
          "count": 2,
          "sum": 16544,
          "avg": 8272
        }
      }
    },
    ...
  ]
}
```
