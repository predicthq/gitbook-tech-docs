---
description: >-
  Build the recommended PredictHQ integration on sample demand data - Saved
  Location, Beam, model-ready features - and finish with a measured forecast
  accuracy improvement you produced yourself.
---

# Measure the forecast lift on sample data

In this tutorial you build the recommended PredictHQ integration end to end, on sample demand data, and finish with a measured accuracy improvement you produced yourself. Along the way you see each piece of the platform do its job: a Saved Location scopes the geography, Beam identifies which events drive the demand, the Features API returns the model-ready features your forecasting model would consume, and a baseline comparison measures the forecast lift from PredictHQ's algorithm and event features.

It takes about 15 minutes, most of which is waiting for two short processing runs. We ran every step in this tutorial against the live API before publishing - the responses you see come from those runs. The tutorial follows this flow:

```mermaid
flowchart LR
    A["1-Create a<br>Saved Location"] --> B["2-4 Create a Beam Analysis<br>and upload sample demand"]
    B --> C["5 Feature Importance:<br>what drives demand"]
    C --> D["6 Features API:<br>the model-ready table"]
    C --> E["7 Baseline comparison:<br>the measured lift"]
    E --> F["8 Explainability:<br>the events behind it"]
```

## Before you start

You need:

* A PredictHQ account and API token - a free trial account has access to everything this tutorial uses. See the [API quickstart](../api-quickstart.md) to create a token.
* Python with the `requests` library (any recent version), or the HTTP client of your choice - every step is a plain HTTP call.
* The retail sample dataset: in your working directory, download [`tutorial_demand_retail.csv`](https://raw.githubusercontent.com/predicthq/gitbook-tech-docs/main/assets/tutorials/measure-the-forecast-lift/tutorial_demand_retail.csv). It contains 18 months of synthetic daily demand for a fictional retail store, modeled on realistic patterns - including holiday closures and demand spikes. This file is fixed for this tutorial so your responses match the ones shown; the [sample datasets](../guides/beam-guides/sample-demand-data.md) for each industry are refreshed regularly, so results from them will differ from this tutorial's.

To use your token in every step, set it once:

```python
import requests

TOKEN = "YOUR_API_TOKEN"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/json"}
```

## Step 1: Create a Saved Location

The tutorial's fictional store is on Lower Broadway in Nashville - a district dense with concerts and live events, chosen so the event effect is easy to see. Create a Saved Location for it, supplying only the origin point and the industry - PredictHQ calculates a Predicted Impact Area automatically, the boundary where events actually affect a retail location there. Don't supply a radius: fixed circles include irrelevant events and miss relevant ones. Create the Saved Location:

```python
response = requests.post(
    "https://api.predicthq.com/v1/saved-locations",
    headers=HEADERS,
    json={
        "name": "Tutorial - Nashville Broadway Retail",
        "industry": "retail",
        "origin_geojson": {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [-86.7775, 36.1612]},
        },
    },
)
location_id = response.json()["location_id"]
print(location_id)  # a short ID like "rfiTpN63KVbeuyZemz0zog"
```

Keep the `location_id` - everything else in this tutorial hangs off it.

## Step 2: Create a Beam Analysis

Beam is PredictHQ's relevancy engine: it analyzes your demand data to determine which event categories materially drive demand at this location. Create an Analysis linked to your Saved Location:

```python
response = requests.post(
    "https://api.predicthq.com/v1/beam/analyses",
    headers=HEADERS,
    json={
        "name": "Tutorial - Nashville Broadway Retail",
        "location": {"saved_location_id": location_id},
        "demand_type": {"industry": "retail", "interval": "day", "unit_descriptor": "Sales"},
    },
)
analysis_id = response.json()["analysis_id"]
print(analysis_id)
```

A new Saved Location takes a few seconds to reach Beam. If this step fails with `Saved Location not found` (a `KeyError` on `analysis_id`), wait 10 seconds and run it again.

## Step 3: Upload the sample demand data

To give Beam the data it correlates against real-world events, upload the CSV to the Analysis:

```python
with open("tutorial_demand_retail.csv", "rb") as f:
    response = requests.post(
        f"https://api.predicthq.com/v1/beam/analyses/{analysis_id}/sink",
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "text/csv"},
        data=f,
    )
print(response.status_code)  # 202 - accepted for processing
```

## Step 4: Wait for Beam to finish

Beam decomposes the demand series and runs feature importance testing. On this dataset it takes about two minutes:

```python
analysis = requests.get(
    f"https://api.predicthq.com/v1/beam/analyses/{analysis_id}", headers=HEADERS
).json()
print(analysis["readiness_status"])  # "pending" while processing, "ready" when complete
```

Run it again until it prints `ready`. If it prints `failed`, or is still `pending` well past five minutes, print the whole `analysis` object - `readiness_checks` reports what the data validation found.

Once it's ready, two things worth noticing in the full `analysis` object:

* `rank` shows Beam set a Local Rank threshold for this location itself - you didn't configure one, and you shouldn't. Manual thresholds override location-specific calibration.
* `readiness_checks` notes four missing dates in the sample data - Thanksgiving and Christmas, when the store was closed. Real demand data has gaps like these, and Beam handles them.

## Step 5: See what drives demand - and what doesn't

Retrieve Beam's Feature Importance results:

```python
response = requests.get(
    f"https://api.predicthq.com/v1/beam/analyses/{analysis_id}/feature-importance",
    headers=HEADERS,
)
for group in response.json()["feature_importance"]:
    print(f'{group["feature_group"]:18} p={group["p_value"]:<8} important={group["important"]}')
```

When we ran this, Beam found eight event groups significant for this location - concerts, conferences, public holidays, and school holidays all at p-values of zero - and rejected four. Look at what it rejected:

```
sports             p=1.0      important=False
```

Sports events don't drive this store's demand - in Nashville, home of the Titans and the Predators. This is the point of Beam: the categories a person would guess into a model aren't necessarily the ones the demand data supports, and every irrelevant category included adds noise. Your own demand data decides, not intuition.

## Step 6: Retrieve the model-ready features

This is the artifact an enterprise integration is built around. Call the Features API with the `beam.analysis_id` - nothing else. It applies the calibrated location boundary, the significant categories from step 5, and the rank thresholds automatically:

```python
response = requests.post(
    "https://api.predicthq.com/v1/features/",
    headers=HEADERS,
    json={
        "beam": {"analysis_id": analysis_id},
        "active": {"gte": "2026-04-01", "lte": "2026-04-24"},
    },
)
print(response.json()["results"][0])
```

The response contains one row per day - 24 in total for this window. The first row from our run:

```json
{
  "date": "2026-04-01",
  "phq_attendance_concerts_retail": {"stats": {"sum": 5287}},
  "phq_attendance_conferences_retail": {"stats": {"sum": 1234}},
  "phq_attendance_expos_retail": {"stats": {"sum": 1616}},
  "phq_impact_academic_exam": {"stats": {"sum": 0}},
  "phq_impact_academic_holiday": {"stats": {"sum": 0}},
  "phq_impact_observances_retail": {"stats": {"sum": 0}},
  "phq_impact_public_holidays_retail": {"stats": {"sum": 12}},
  "phq_impact_school_holidays_retail": {"stats": {"sum": 0}},
  "phq_impact_severe_weather_cold_wave_retail": {"stats": {"max": 0}},
  "phq_impact_severe_weather_cold_wave_storm_retail": {"stats": {"max": 0}},
  "phq_impact_severe_weather_flood_retail": {"stats": {"max": 0}},
  "phq_impact_severe_weather_tornado_retail": {"stats": {"max": 0}}
}
```

Each row is a date with one value per Beam-selected feature: Predicted Attendance sums for the significant attendance categories, impact values for holidays and severe weather. Scan forward two rows and Friday 2026-04-03 jumps out: 20,201 predicted concert attendees against Wednesday's 5,287 - exactly the kind of swing a model can't see in demand history alone. In production, you join this table to your demand history to train your model, then call the same endpoint with a **future-dated** window at every forecast run - the events behind these features are announced and scheduled in advance, so a future window carries known signals about what's coming rather than extrapolations of your history. That training-and-serving loop lives in your ML pipeline and is out of scope here; the [Features API reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) covers the window mechanics, and the [demand forecasting notebook](https://github.com/predicthq/phq-data-science-docs/blob/master/demand-forecasting-with-events/demand-forecasting-with-event-features.ipynb) shows a worked ML example.

## Step 7: Measure `phq-cffm` with PredictHQ features against an XGBoost baseline

You could stop here and take the feature table into your own model - in production, that's exactly what happens. But you don't need to build a model to measure the lift. The Forecasts API can create two models on your uploaded demand - one enhanced with PredictHQ features, one baseline without them - and report the accuracy difference.

The request doesn't set `algo`, so a `retail` model gets the default algorithm for its industry, `phq-cffm`. The baseline always uses `phq-xgboost` without PredictHQ features. The lift therefore measures the algorithm and the features together - see [Baseline comparison](../guides/forecasts-api-guides/understanding-forecast-accuracy-metrics.md#baseline-comparison). To measure the features alone, set `"algo": "phq-xgboost"` in the request.

To create both models, run the following code. It creates a model with `generate_baseline` enabled, uploads the same CSV, and starts a refresh:

```python
import csv

response = requests.post(
    "https://api.predicthq.com/v1/forecasts/models",
    headers=HEADERS,
    json={
        "name": "Tutorial - Nashville Broadway Retail",
        "location": {"saved_location_id": location_id},
        "demand_type": {"industry": "retail", "interval": "day"},
        "forecast_window": "7d",
        "generate_baseline": True,
    },
)
model_id = response.json()["model_id"]

with open("tutorial_demand_retail.csv") as f:
    demand = [{"date": row["date"], "demand": float(row["demand"])} for row in csv.DictReader(f)]

response = requests.post(
    f"https://api.predicthq.com/v1/forecasts/models/{model_id}/demand",
    headers=HEADERS,
    json={"demand": demand},
)
print(response.status_code)  # 201 - demand data stored

response = requests.post(
    f"https://api.predicthq.com/v1/forecasts/models/{model_id}/refresh", headers=HEADERS
)
print(response.status_code)  # 204 - refresh started
```

A refresh takes two to three minutes. Check the model until `readiness.status` prints `ready` (if it prints `failed`, the `readiness` object explains why), then read both models' error metrics:

```python
response = requests.get(
    f"https://api.predicthq.com/v1/forecasts/models/{model_id}", headers=HEADERS
)
model = response.json()["model"]
print(model["algo"])  # phq-cffm, the default for retail
print(model["readiness"]["status"])
print(model["metrics"]["accuracy"])
print(model["metrics"]["baseline_comparison"])
```

From our run:

```json
{
  "accuracy": {"mape": 7.39, "mae": 2653.8, "rmse": 4349.52, "wape": 6.25},
  "baseline_comparison": {"mape_improvement_pct": 42.02, "baseline_mape": 12.75, "baseline_mae": 4415.23, "baseline_rmse": 7169.4, "baseline_wape": 10.39}
}
```

The enhanced `phq-cffm` model's error (MAPE 7.39) beat the baseline (12.75) - a 42.0% improvement on the same demand data. That improvement comes from the algorithm and the PredictHQ features together.

Don't read that number as a benchmark. This store sits in a deliberately event-exposed district, and the demand data is synthetic - the result demonstrates the measurement workflow, not a claim about your business. Event exposure is a property of the location, and the lift depends on it. That's the point of measuring instead of assuming - this workflow measures the combined lift from PredictHQ's algorithm and event features against an XGBoost baseline at your locations, on your own demand data.

## Step 8: See the events behind the forecast

The lift has names. Retrieve the forecast with explainability - and note the date range: the sample data ends on 2026-04-24, so the forecast covers the week after that. Without an explicit date range this endpoint defaults to today onward and returns nothing:

```python
response = requests.get(
    f"https://api.predicthq.com/v1/forecasts/models/{model_id}/forecast",
    headers=HEADERS,
    params={
        "date.gte": "2026-04-25",
        "date.lte": "2026-05-01",
        "include": "phq_explainability",
    },
)
for day in response.json()["results"]:
    events = day.get("phq_explainability", {}).get("events") or []
    top = max(events, key=lambda e: e.get("local_rank") or 0, default=None)
    print(day["date"], round(day["forecast"]), "-", top["title"] if top else "no events")
```

From our run:

```
2026-04-25 47469 - Nashville Health & Fitness Expo
2026-04-26 43346 - Hayley Williams
2026-04-27 39045 - Snarky Puppy
2026-04-28 35279 - MAGIC Nashville
2026-04-29 37651 - MAGIC Nashville
2026-04-30 40008 - The Exchange
2026-05-01 50000 - Spring Exams
```

The demand drivers are real, verifiable events: expos at Local Ranks 88 and 93, concerts at Local Ranks 78 and 80, and university spring exams. Every forecast traces back to observable real-world activity - the same explainability your operators and stakeholders get in production.

## Clean up

The tutorial resources are yours to keep exploring with, or delete them:

```python
requests.delete(f"https://api.predicthq.com/v1/forecasts/models/{model_id}", headers=HEADERS)
requests.delete(f"https://api.predicthq.com/v1/beam/analyses/{analysis_id}", headers=HEADERS)
requests.delete(f"https://api.predicthq.com/v1/saved-locations/{location_id}", headers=HEADERS)
```

## What you built

You ran the recommended integration workflow end to end: a Saved Location with an automatically calibrated Predicted Impact Area, a Beam Analysis that identified which event categories drive this demand (and which don't), the model-ready feature table your own forecasting model would consume, and a measured accuracy comparison against an XGBoost baseline. What that measurement is worth is relative to the business: at enterprise scale, even a fraction of a percent less forecast error can mean millions of dollars in better staffing, inventory, and pricing decisions.

With your own demand data, the path is identical - one Saved Location and one Beam Analysis per location, refreshed monthly. To run it again closer to home first, pick [your industry's sample dataset](../guides/beam-guides/sample-demand-data.md) and change the `industry` value (steps 1, 2, and 7), the file name (steps 3 and 7), and the date windows (steps 6 and 8) to fit the dates in your file. The `industry` value also sets the default algorithm in step 7. Like `retail`, `restaurants` defaults to `phq-cffm`. Other industries default to `phq-xgboost`, and their lift measures the PredictHQ features alone. Your results will differ from the ones shown here.

## Where to go next

Continue with these pages:

* [How to use PredictHQ](../how-to-use-predicthq.md) - the recommended path for your job, from model training to grounding AI systems
* [Standard integration pattern](../../integrations/integration-guides/standard-integration-pattern.md) - the production architecture: local feature storage, refresh cadences, explainability
* [Which API should I use?](../core-concepts/which-api-should-i-use.md) - per-task API selection
* [Using event features with time series foundation models](../guides/features-api-guides/using-event-features-with-time-series-foundation-models.md) - if your models are pre-trained rather than trained in-house
