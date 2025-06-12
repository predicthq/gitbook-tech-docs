---
description: >-
  Learn how to integrate PredictHQ's event features into your demand forecasting
  model.
---

# Improving Demand Forecasting Models with Event Features

The inclusion of PredictHQ's event data can significantly enhance the performance of machine learning models, such as those used in demand forecasting. For example, the delivery company [Favor reported a reduction of 5-6% in their forecasting error](https://www.predicthq.com/customers/favor), with others noting decreases of up to 5-10% or more.

This tutorial will guide you through the process of identifying, retrieving and integrating relevant, demand-driving event data as features into a demand forecasting model. Follow along by running the accompanying Jupyter notebooks while referring to the provided links for more technical details. The tutorial concludes with a practical example of a demand forecasting model that incorporates PredictHQ event features.

## Use Cases

Demand Forecasting

## Relevant Industries

Accommodation, Consumer Packaged Goods, Grocery and Supermarkets, Leisure, Travel and Tourism, Marketing and Advertising, Parking, Restaurants, Retail, Transportation and Delivery and Others

## Harnessing Event Signals

### Events Driving Demand

Events, such as concerts, expos and public holidays, are known to affect consumer behavior and [drive demand](https://www.predicthq.com/use-cases/demand-forecasting). PredictHQ offers event data across [more than a dozen categories](../../predicthq-data/event-categories/), featuring a [wide range of labels](../../predicthq-data/labels.md). The [powerful data processing pipeline](https://www.predicthq.com/intelligence) ensures the delivery of high-quality, enriched event data that can be seamlessly incorporated as features into any demand forecasting model.

### Integrating Event Features

Built upon extensive event coverage, PredictHQ’s event features aggregate similar events into predefined groups for specific locations at set intervals, such as daily aggregations. These prebuilt, forecast-ready features can be added directly to machine learning models without further preprocessing. Access to an extensive library of features is available through the [Features API](https://www.predicthq.com/apis/features-api). We recommend starting with the Important Features identified by the [Beam API](https://www.predicthq.com/beam).

## How-To Guide

The sections below guide you through integrating event features into your demand forecasting models. Follow these instructions and run the accompanying Jupyter notebooks to understand how you can adapt this approach to fit your workflow and improve the accuracy of your models.

### Overview

Adding event features to a demand forecasting model involves straightforward steps. These include pulling a list of Important Features from the [Beam API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam) and retrieving prebuilt, forecast-ready features from the [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features) for a store or location.

<figure><img src="https://lh7-us.googleusercontent.com/BxTbjp8PELaPLMrh8664Jzh6W-PzBc73AyL8wvUCmL_7nm3TKIyA5tCMbyH-RmWihWLdi99JKy3RszSsIc0TJPCYeg3YtXUBPkHLclQ_uyRlk1XRa6Rmiz-2h3yLNn9w1K2IOwlrVNBkjHYNoAQjQEM" alt=""><figcaption><p>An overview of integrating event features into a machine learning model.</p></figcaption></figure>

Most steps are handled by PredictHQ APIs; you just need to provide the following for each store or location:

1. Historical demand data
2. Latitude and longitude
3. Industry

### Step 1. Select Relevant Event Features

With countless events taking place globally throughout the year, identifying events that impact demand at your location is crucial. The [Beam API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam) automatically provides a list of Important Features based on your historical demand data and location. Alternatively, you can access [Beam](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam) in our [WebApp](https://control.predicthq.com/beam) and directly [copy the Important Features](https://www.predicthq.com/blog/find-machine-learning-ml-features-to-use-in-forecasting-with-beam) from your browser.

There are two main strategies for determining a list of Important Features for a store or location: Important Features tailored specifically to the store or location, or Important Features based on a group of stores or locations. See below and choose the approach that best suits your operational needs.

<details>

<summary>Important Features by Location</summary>

If you are able to implement individual models for each store or location, the Beam API’s [Feature Importance](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/analyses/get-feature-importance) endpoint is recommended. It provides a list of Important Features tailored specifically to your store or location. Also referred to as Category Importance in our WebApp, these event features (or categories) are identified as having the greatest impact on your demand.

</details>

<details>

<summary>Important Features by Group of Locations</summary>

If you manage multiple stores or locations and require a unified set of features, the Beam API’s [Aggregated Feature Importance](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/analysis-groups/get-aggregated-feature-importance) endpoint is recommended. It provides a consolidated list of Important Features across all stores or locations within an [Analysis Group](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/analysis-groups) based on aggregating Feature Importance results from contributing stores or locations.

</details>

<details>

<summary>User Inputs</summary>

The sections below highlight what you need to provide for determining a list of Important Features. Explore the accompanying Jupyter notebooks to see how this fits together practically.

**Historical Demand Data**

Ensure you have enough time-series data that meets [Beam’s requirements](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/analyses/upload-demand-data). Demand can be quantified in any unit relevant to your forecasting model. Common examples include sales in USD for retail stores, number of orders for restaurants and revPAR for hotels.

**Industry**

Specify your industry as there are several industry-specific settings required in this step such as when using the [Suggested Radius API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/suggested-radius). If your industry is not covered, please use the default `other`:

* `accommodation`
* `retail`
* `parking`
* `food_and_beverage` (also referred to as `restaurants`)
* `other` (for all other industries)

**Location**

Define the catchment area around your store or location using a center point and radius approach. The [Suggested Radius API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/suggested-radius) recommends a radius specific to your industry and latitude/longitude. Custom configuration is also available.

**Event Rank**

Set a minimum [PHQ Rank](../../predicthq-data/ranks/phq-rank.md) based on our [industry-specific recommendations](../industry-specific-event-filters.md#minimum-phq-rank) to focus on events that are likely to influence your demand, while excluding those that are too small or irrelevant.

</details>

{% hint style="info" %}
For technical details, visit:

* [Upload Demand Data](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/analyses/upload-demand-data "mention")
* [Suggested Radius](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/suggested-radius "mention")
* [Beam](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam "mention")
* [Analysis Groups](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/analysis-groups "mention")

For practical implementation:

* [forecast-ready-features-at-scale.md](../beam-guides/forecast-ready-features-at-scale.md "mention")
* [ml-features-by-group.md](../beam-guides/ml-features-by-group.md "mention")
{% endhint %}

### Step 2. Get Features

The [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features) provides access to a library of prebuilt, forecast-ready features ready for direct integration into your machine-learning models. Simply specify the date range, location and list of features, all of which can be sourced from the [Beam API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam).

Responses from the Features API vary based on the type of feature. Most come with a suite of statistics that indicates how the underlying event data is aggregated daily for a location, e.g. sum, max, count. For `phq_rank_*` features, the response is the daily number of events for each of the [five rank bands](https://www.predicthq.com/features/rankings/phq-rank). We recommend the following aggregations:

| Feature Type       |     stat    |       other       |
| ------------------ | :---------: | :---------------: |
| `phq_attendance_*` |     sum     |    <p><br></p>    |
| `phq_impact_*`     |     max     |    <p><br></p>    |
| `phq_rank_*`       | <p><br></p> | rank-weighted sum |
| `phq_spend_*`      |     sum     |    <p><br></p>    |
| `phq_viewership_*` |     max     |    <p><br></p>    |

**Predicted Impact Patterns**

Some features consider the additional impact from events before and after scheduled dates, offering a more accurate representation of event impacts on demand. This is known as [Predicted Impact Patterns](https://www.predicthq.com/blog/use-demand-impact-patterns-to-predict-how-events-shape-consumer-behavior), which vary by event category and industry. Features including Predicted Impact Patterns are denoted with an industry suffix, such as `phq_attendance_sports_accommodation` or `phq_impact_severe_weather_air_quality_retail`.

{% hint style="info" %}
For technical details, visit:

* [Features](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features "mention")
* [Beam](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam "mention")

For practical implementation:

* [feature-engineering-guide.md](../features-api-guides/feature-engineering-guide.md "mention")
{% endhint %}

### Step 3. ML Model and Future Predictions

Event features provided by the [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features) are prebuilt, forecast-ready and ready for immediate use. They can be integrated into your existing dataset by merging based on location ID and date. Incorporating these event features can enhance your model's performance by adding valuable demand-driving event data.

For future predictions, you can access forward-facing data, such as the next two weeks or the upcoming month, by querying the [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features). Work closely with your engineering team to ensure these new features are effectively incorporated into your production pipeline.

{% hint style="info" %}
For practical implementation:

* [demand-forecasting-data-science-guides.md](../features-api-guides/demand-forecasting-data-science-guides.md "mention")
{% endhint %}

## Conclusion

By following this tutorial, you should now understand how to enhance your demand forecasting models by integrating PredictHQ's event features. As known drivers of demand, incorporating event signals can noticeably improve the accuracy of your forecasts, empowering you to make more informed decisions and strategize more effectively.
