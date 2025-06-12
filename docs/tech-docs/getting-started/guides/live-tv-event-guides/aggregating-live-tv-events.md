# Aggregating Live TV Events

Aggregating Predicted Viewership data to create features for forecasting is an impactful way to unlock the value of Live TV Events data. You can use the Features API to aggregate Predicted Viewership data.

See the PHQ Viewership in the [endpoint documentation](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features). Using these features you can get the count, sum, min, max, avg, median, and std\_dev for any viewership feature in the features API. The features API will combine all the viewership data for a location and return these calculated values. For example, you can get the total NFL viewership and NBA viewership per day for a location as shown below

```python
import requests

data = {
    "active": {
        "gte": "2020-02-01",
        "lte": "2020-02-29"
    },
    "location": {
        "place_id": [
            5224323,
            5811704,
            4887398
        ]
    },
    "phq_viewership_sports_american_football_nfl": {
        "stats": [
            "count",
            "sum",
            "avg"
        ]
    },
    "phq_viewership_sports_basketball_nba": {
        "stats": [
            "count",
            "sum",
            "avg"
        ]
    }
}


response = requests.post(
    url="https://api.predicthq.com/v1/features/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    json=data
)

print(response.json())
```
