---
description: >-
  A how-to guide with details on how to create machine learning features using
  PredictHQ's Features API.
---

# Feature Engineering Guide

### Overview

Our customers find that factoring events into their demand forecasting improves the accuracy of their forecasts. For example, if events are occurring near a store, hotel, parking garage, or any other location, they can impact demand. Customers use our events for different types of demand forecasting including labor forecasting, inventory, dynamic pricing, and more.

The goal of the Feature Engineering Guide notebook is to help data science teams understand and get hands-on experience querying different event-based features from PredictHQ's Features API. This guide outlines, with clear and simple examples, recommended features per event category. Data science teams can use these examples to create features easily and include them in their own demand forecasting models or any other applicable models.

See also the [API reference guide for the Features API](../../../api/features/get-features.md) for more info on the Features API. For an overview of categories see the [categories page](../../predicthq-data/event-categories/). This guide uses [PredictHQ's SDK](../../../integrations/sdks/python-sdk.md) to access the Features API.

We also provide other data science guides that go into more detail on different categories, for example, [Attendance Based Events](../events-api-guides/attendance-based-events-data-science-guides.md). Each of these guides consists of a set of notebooks. Refer to these guides if you want to do more in-depth research on specific categories.

### How to use event-based features in your models

This guide provides details on how to create event-based features using the SDK for the Features API. It assumes you are familiar with adding ML features to your models. Features are often used in demand forecasting models to forecast future demand but can be used in other types of models as well.

The features in this guide are designed to be used in a forecasting solution where you can forecast demand for each location. For example, you may forecast demand for a set of retail stores, hotels, restaurants, parking garages, or other types of locations. In this scenario, you have a set of event-based features that have a value per location and these features are used in your model to adjust the forecast for that location.

For example, the process for using event-based features may look as follows:

1. Review the different features in this guide and the other related documentation.
2. Data exploration - you may want to conduct data exploration using a sample data set around one of your locations.
3. Events ML Feature testing - you may want to get a training data set for a location or locations (see below on using a longer data range), and conduct model R\&D with events features using techniques such as model selection and cross-validation.
4. Model evaluation - you may want to compare the model accuracy on historical data before adding the event ML features and after adding the event features.
5. Update your model to use the new ML features - get your production model ready for deployment.
6. Work with your engineering team to add the features to your production pipeline - the Features API can be used by your production pipeline.
7. Deploy your new model in production with the new event-based features.

For a simple overview of how you can integrate event-based features into your system, see below. For a production implementation, we'd suggest that you store or cache the features from the Features API before you call them in production. This helps make your implementation more robust as calling services over the internet always have an element of risk. Then regularly update your copy of the features. For example, if you run your model once per day to update your forecast then you may want to refresh your copy of the Features API just before your forecast runs.

***

The section above is an extract from the notebook. [Download the full notebook here](https://github.com/predicthq/phq-data-science-docs/blob/master/feature-engineering-guide/feature\_engineering\_guide.ipynb).

See also the [Snowflake Data Science Guide](../../../integrations/third-party-integrations/snowflake/snowflake-data-science-guide/) for details on how to create ML features in Snowflake as an alternative to calling the Features API directly. Instead follow the guide but get the ML features from the table in Snowflake.

