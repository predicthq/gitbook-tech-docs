# Demand Forecasting with ML Models

Demand forecasting using machine learning (ML) models involves predicting future customer demand for products or services. If you are performing demand forecasting with ML models you are always looking to increase the accuracy of your forecast. Events have a big impact on demand and updating your models to account for events can significantly improve the accuracy of your forecasts.

<figure><img src="../../.gitbook/assets/Tutorials illustration 1.png" alt=""><figcaption></figcaption></figure>

[See our tutorial](../guides/tutorials/improving-demand-forecasting-models-with-event-features.md) on incorporating event features into ML models. Learn how to automatically and dynamically update your forecast by integrating PredictHQ data directly into your demand forecasting models.

## Events Impacting Demand

Let’s look at some real-world examples of how events can impact businesses:

* **Wimbledon & British Summer Time Festival:** Accommodation demand in London surged by nearly 40%.
* **Dreamforce:** In San Francisco, hotel demand increased by 100-110%, with some coffee chains experiencing a 140-190% rise.
* **Iowa College Sports:** Retailers saw beer demand spike by about 180% during nearby college sports events.
* **London Events:** Dozens of concerts and shows within a 3-mile radius led to parking demand increases of over 60%.

{% hint style="info" %}
Where customers have updated their demand forecast to account for events we’ve seen MAPE improvements in the range of 5-10% and some even greater. For example, [Favor has seen a 5 - 6% improvement in MAPE](https://www.predicthq.com/customers/favor).
{% endhint %}

## Event Data&#x20;

Many businesses attempt to source and manage event data themselves but face challenges due to the diversity of events and many different sources. PredictHQ addresses these challenges by offering data from 19 different categories, from sports to concerts to severe weather events, all through our Features API and Events API, consolidating hundreds of data sources into a single, accessible product.

## Data Integration

Incorporating event data into forecasts can be complex. Our tools and products are designed to minimize R\&D efforts, enabling quick and easy identification of event-based ML features. Our Features API provides prebuilt, forecast-ready features, significantly reducing feature engineering time from months to days.

## Applications

[Demand forecasting](../guides/tutorials/improving-demand-forecasting-models-with-event-features.md) covers a range of use cases and industries from dynamic pricing to inventory management. See [all available use cases](./) for more information.

For a practical guide on building a demand forecasting model using PredictHQ's event data and Power BI's AutoML, see [integrate-with-a-demand-forecast-in-powerbi.md](../../integrations/third-party-integrations/integrate-with-a-demand-forecast-in-powerbi.md "mention").\
