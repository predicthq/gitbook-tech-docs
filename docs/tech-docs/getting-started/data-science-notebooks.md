---
description: >-
  Jupyter notebooks for training and improving demand forecasting models with
  PredictHQ event features—Beam calibration, model-ready features, and worked
  forecasting examples.
---

# Data science notebooks

PredictHQ features exist to make forecasts more accurate. Adding event features to a demand forecasting model reduces forecast error in a way you can measure and attribute - and what a point of accuracy is worth is relative to your business: at enterprise scale, even a fraction of a percent less forecast error can mean millions of dollars in better staffing, inventory, and pricing decisions. These Jupyter notebooks show how to capture that lift in your own models: calibrating with Beam, retrieving model-ready features, and training and forecasting with them.

If you're new, work through the forecasting workflow notebooks in order - they follow the recommended path: Beam identifies which event categories drive demand at each location, the Features API turns them into model-ready signals, and your model (or the Forecasts API) does the rest. Before you backtest, read [Data Leakage in Backtesting](core-concepts/data-leakage-in-backtesting.md) so historical evaluation reflects what the model sees in production.

## The forecasting workflow

Work through these in order.

1. [**ML features by location with Beam**](https://github.com/predicthq/phq-data-science-docs/blob/master/demand-forecasting-with-events/identify-location-level-features-with-beam-api.ipynb) - run Beam per location and use Feature Importance to identify the relevant, forecast-ready features.
2. [**ML features by group with Beam Analysis Groups**](https://github.com/predicthq/phq-data-science-docs/blob/master/demand-forecasting-with-events/identify-group-level-features-with-beam-api.ipynb) - an aggregated feature set across several locations, for a single shared model.
3. [**Get features with the Features API**](https://github.com/predicthq/phq-data-science-docs/blob/master/demand-forecasting-with-events/get-features-with-features-api.ipynb) - retrieve model-ready features at scale, keyed by your Beam Analysis. If your data lives in Snowflake, the [Snowflake data science guide](../integrations/third-party-integrations/snowflake/snowflake-data-science-guide/) covers building features there instead.
4. [**Demand forecasting with event features**](https://github.com/predicthq/phq-data-science-docs/blob/master/demand-forecasting-with-events/demand-forecasting-with-event-features.ipynb) - incorporate the features into a demand forecasting model. Self-contained: it can be run independently of the notebooks above.
5. [**Forecasts API**](https://github.com/predicthq/phq-data-science-docs/blob/master/forecasts-api/demand_forecasting_with_phq_forecasts_api.ipynb) - the managed alternative: train a model and get event-driven forecasts without building your own, with a baseline comparison to measure the lift.

## Exploring event categories

Per-category notebook series for exploring the data itself. Each series has three parts: data engineering (extract to a DataFrame), data exploration, and feature engineering.

### Attendance-based events

Conferences, expos, concerts, festivals, performing arts, sports, and community events - see [Attendance-based events](predicthq-data/event-categories/attendance-based-events.md) for the category reference.

* [Part 1: Data Engineering](https://github.com/predicthq/phq-data-science-docs/blob/master/attended-events/part_1_data_engineering.ipynb)
* [Part 2: Data Exploration](https://github.com/predicthq/phq-data-science-docs/blob/master/attended-events/part_2_data_exploration.ipynb)
* [Part 3: Feature Engineering](https://github.com/predicthq/phq-data-science-docs/blob/master/attended-events/part_3_feature_engineering.ipynb)

### Non-attendance-based events

Observances, public holidays, and school holidays - see [Non-Attendance-based events](predicthq-data/event-categories/non-attendance-based-events.md).

* [Part 1: Data Engineering](https://github.com/predicthq/phq-data-science-docs/blob/master/unattended-events/part_1_data_engineering.ipynb)
* [Part 2: Data Exploration](https://github.com/predicthq/phq-data-science-docs/blob/master/unattended-events/part_2_data_exploration.ipynb)
* [Part 3: Feature Engineering](https://github.com/predicthq/phq-data-science-docs/blob/master/unattended-events/part_3_feature_engineering.ipynb)

### Severe weather events

See [Severe Weather](predicthq-data/event-categories/unscheduled-events.md#severe-weather) for the category reference.

* [Part 1: Data Engineering](https://github.com/predicthq/phq-data-science-docs/blob/master/severe-weather-events/part_1_data_engineering.ipynb)
* [Part 2: Data Exploration](https://github.com/predicthq/phq-data-science-docs/blob/master/severe-weather-events/part_2_data_exploration.ipynb)
* [Part 3: Feature Engineering](https://github.com/predicthq/phq-data-science-docs/blob/master/severe-weather-events/part_3_feature_engineering.ipynb)

### Academic events

* [Part 1: Data Engineering](https://github.com/predicthq/phq-data-science-docs/blob/master/academic-events/part_1_data_engineering.ipynb)
* [Part 2: Data Exploration](https://github.com/predicthq/phq-data-science-docs/blob/master/academic-events/part_2_data_exploration.ipynb)
* [Part 3: Feature Engineering](https://github.com/predicthq/phq-data-science-docs/blob/master/academic-events/part_3_feature_engineering.ipynb)

### Live TV events

Broadcast sports viewership by county in the United States - see [Live TV events](predicthq-data/event-categories/live-tv-events.md).

* [Part 1: Data Engineering](https://github.com/predicthq/phq-data-science-docs/blob/master/live-tv-events/part_1_data_engineering.ipynb)
* [Part 2: Data Exploration](https://github.com/predicthq/phq-data-science-docs/blob/master/live-tv-events/part_2_data_exploration.ipynb)
* [Part 3: Feature Engineering](https://github.com/predicthq/phq-data-science-docs/blob/master/live-tv-events/part_3_feature_engineering.ipynb)

### Venues

Events are linked to the venues they occur at - stadiums, conference centers, concert halls - stored as [entities](predicthq-data/entities.md). A major venue near your location is often a key source of demand. The [venues notebook](https://github.com/predicthq/phq-data-science-docs/blob/master/venues/venues-example.ipynb) covers extracting venue information, mapping venues, event types by venue, and estimated capacities.

All our Data Science Notebooks can be found in our [GitHub repo](https://github.com/predicthq/phq-data-science-docs/tree/master).

For the concepts behind the workflow, see [Which API should I use?](core-concepts/which-api-should-i-use.md) Using a pre-trained forecasting model instead of training your own? See [Using event features with time series foundation models](guides/features-api-guides/using-event-features-with-time-series-foundation-models.md)
