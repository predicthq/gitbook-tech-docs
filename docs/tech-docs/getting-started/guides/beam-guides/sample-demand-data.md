# Sample Demand Data

If you don't have your own demand data ready, you can use one of our sample datasets to explore Beam and the Forecasts API. Each dataset contains synthetic daily demand data modelled on realistic industry patterns. Use any dataset with your own location — the industry type matters more than the specific location when getting started.

## Available Datasets

| Industry      | File                                                                                                                                                              |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Retail        | [`sample_demand_retail.csv`](https://raw.githubusercontent.com/predicthq/gitbook-tech-docs/main/assets/sample-demand-data/sample_demand_retail.csv)               |
| Restaurant    | [`sample_demand_restaurants.csv`](https://raw.githubusercontent.com/predicthq/gitbook-tech-docs/main/assets/sample-demand-data/sample_demand_restaurant.csv)      |
| Accommodation | [`sample_demand_accommodation.csv`](https://raw.githubusercontent.com/predicthq/gitbook-tech-docs/main/assets/sample-demand-data/sample_demand_accommodation.csv) |
| Parking       | [`sample_demand_parking.csv`](https://raw.githubusercontent.com/predicthq/gitbook-tech-docs/main/assets/sample-demand-data/sample_demand_parking.csv)             |
| Other         | [`sample_demand_other.csv`](https://raw.githubusercontent.com/predicthq/gitbook-tech-docs/main/assets/sample-demand-data/sample_demand_other.csv)                 |

PredictHQ supports the following named industries: `accommodation`, `cpg`, `tourism`, `marketing`, `parking`, `restaurants`, `retail`, and `transportation`. If your business doesn't fit one of these, use `other`. See [How Industry Affects Results](../how-industry-affects-results.md) for the full list and guidance on choosing the right industry.

## Using the Sample Data

### **With Beam**

Upload the sample data to an existing Beam analysis using the [Upload Demand Data](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/analyses/upload-demand-data) endpoint:

```python
import requests

analysis_id = "YOUR_ANALYSIS_ID"
PHQ_API_TOKEN = "YOUR_API_TOKEN"

with open("sample_demand_retail.csv", "rb") as f:
    response = requests.post(
        url=f"https://api.predicthq.com/v1/beam/analyses/{analysis_id}/sink",
        headers={
            "Authorization": f"Bearer {PHQ_API_TOKEN}",
            "Content-Type": "text/csv",
        },
        data=f,
    )

print("Upload successful" if response.status_code == 202 else response.json())
```

See the [Beam Guides](./) for a full walkthrough.

### **With Forecasts API**

Upload the sample data to an existing forecast model using the [Upload Demand Data](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/forecasts/demand-data/upload-demand-data) endpoint:

```python
import requests
import pandas as pd
import json

model_id = "YOUR_MODEL_ID"
PHQ_API_TOKEN = "YOUR_API_TOKEN"

df = pd.read_csv("sample_demand_retail.csv")

response = requests.post(
    url=f"https://api.predicthq.com/v1/forecasts/models/{model_id}/demand",
    headers={
        "Authorization": f"Bearer {PHQ_API_TOKEN}",
        "Content-Type": "application/json",
    },
    json={"demand": json.loads(df.to_json(orient="records"))},
)

print("Upload successful" if response.status_code == 201 else response.json())
```

See the [Getting Started with Forecasts API](../forecasts-api-guides/getting-started.md) guide for a full walkthrough including how to create a model and generate a forecast.

{% hint style="info" %}
These datasets are provided for testing and exploration purposes only. For production use, replace them with your own demand data.
{% endhint %}
