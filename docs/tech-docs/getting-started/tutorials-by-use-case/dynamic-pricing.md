# Dynamic Pricing

From missing out on increased revenue to losing operational efficiency and even customers due to poor customer experiences, many accommodation, parking, travel, and retail vendors and service providers are painfully aware of demand fluctuations. Most companies won’t realize a demand surge is taking place until 30-50% of availability or stock has been snapped up.

<figure><img src="../../.gitbook/assets/Tutorials illustration 2.png" alt=""><figcaption></figcaption></figure>

Businesses from these industries often use PredictHQ data to fuel their sales forecasts, dynamic pricing, and business operations in advance. We have created guides for our most common use cases. We’ll start with using PredictHQ data for dynamic pricing examples by industry:

<details>

<summary>Accommodation &#x26; Hospitality</summary>

To implement PredictHQ data to inform dynamic pricing for your accommodation or hospitality business, review the options below:

* **No code:** Use PredictHQ's WebApp, to unlock demand data weeks and months in advance to inform your manual pricing updates. [Read more](https://app.gitbook.com/s/Ri9YaBiPckypV66Jggc2/tools/see-event-trends-in-the-webapp.md) about Event Trends.
* **Business Intelligence (BI) tools:** Integrate PredictHQ data with your Power BI or Tableau (or other analytics tool) dynamic pricing workflows. See the [Power BI Tutorial ](../guides/tutorials/using-event-data-in-power-bi.md)and [Tableau Tutorial](../guides/tutorials/using-event-data-in-tableau.md).
* **Load event data to your warehouse:** Take PredictHQ API data and load it into a data warehouse. [Read tutorial](../guides/tutorials/loading-event-data-into-a-data-warehouse.md).
* **Machine learning models:** Automatically and dynamically update your pricing by integrating PredictHQ data directly into your demand forecasting models. [Read tutorial.](../guides/tutorials/improving-demand-forecasting-models-with-event-features.md)

**Getting Started**

1. Quick [filters](../guides/industry-specific-event-filters.md) for accommodation and hospitality:
   1. Relevant Event Categories: `concerts`, `conferences`, `expos`, `festivals`, `performing-arts`
   2. Location Type: `Center Point & Radius`
   3. Minimum PHQ Rank: 35

**Example in Practice**

PredictHQ helps its customers master predictability with the smartest and largest event impact data stream, which can drive dynamic pricing planning and operations quickly, efficiently, and at scale.

Analyzing Demand and Pricing Adjustments

Accommodation providers find it useful to overlay room price data with event impact data and use that to help guide pricing adjustments. In the dashboard below, daily room price data is shown alongside the total number of people attending events in San Francisco. Based on this you can look for peak days and surges in demand and adjust pricing accordingly. Follow the [Power BI tutorial](../guides/tutorials/using-event-data-in-power-bi.md) or [Tableau Tutorial](../guides/tutorials/using-event-data-in-tableau.md) to integrate event data into your BI tools.

<img src="../../.gitbook/assets/Power BI Dynamic Pricing Example.png" alt="" data-size="original">

On February 24, attendance at local events reached over 590,000—significantly higher than on other days. This demand surge or peak impacts business operations. In response, a hotel owner adjusted the room price from $230 to $310. This adjustment might be done in a different application.

Pricing Strategies

Overlaying event data with business data provides a simple way to pinpoint when price adjustments are needed. For a more advanced approach, machine learning models can suggest or automatically update pricing, enhancing responsiveness to market changes.

See [How Hoteliers Achieved a 10% RevPar Increase with HQ revenue](https://www.predicthq.com/customers/hqrevenue).

</details>

<details>

<summary>Leisure and Travel</summary>

To implement PredictHQ data to inform dynamic pricing for your leisure and travel business, review the options below:

* **No code:** Use PredictHQ's WebApp, to unlock demand data weeks and months in advance to inform your manual pricing updates. [Read more](https://app.gitbook.com/s/Ri9YaBiPckypV66Jggc2/tools/see-event-trends-in-the-webapp.md) about Event Trends.
* **Business Intelligence (BI) tools:** Integrate PredictHQ data with your Power BI or Tableau (or other analytics tool) dynamic pricing workflows. See the [Power BI Tutorial ](../guides/tutorials/using-event-data-in-power-bi.md)and [Tableau Tutorial](../guides/tutorials/using-event-data-in-tableau.md).
* **Load event data to your warehouse:** Take PredictHQ API data and load it into a data warehouse. [Read tutorial](../guides/tutorials/loading-event-data-into-a-data-warehouse.md).
* **Machine learning models:** Automatically and dynamically update your pricing by integrating PredictHQ data directly into your demand forecasting models. [Read tutorial](../guides/tutorials/improving-demand-forecasting-models-with-event-features.md).

**Getting Started**

1. Quick [filters](../guides/industry-specific-event-filters.md) for leisure and travel:
   1. Relevant Event Categories: `public holidays`, `performing-arts`, `conferences`, `conferences`, `community`
   2. Location Type: `City`
   3. Minimum PHQ Rank: 30

With PredictHQ's products and data, businesses in the leisure and travel sector gain insights into demand fluctuations well in advance. This allows them to optimize their pricing strategy effectively and make informed decisions that boost profitability while catering to the dynamic needs of travelers and event-goers.

<img src="../../.gitbook/assets/Foot Traffic.png" alt="" data-size="original">

</details>

<details>

<summary>Retail</summary>

To implement PredictHQ data to inform dynamic pricing for your retail business, review the options below:

* **No code:** Use PredictHQ's WebApp, to unlock demand data weeks and months in advance to inform your manual pricing updates. [Read more](https://app.gitbook.com/s/Ri9YaBiPckypV66Jggc2/tools/see-event-trends-in-the-webapp.md) about Event Trends.
* **Business Intelligence (BI) tools:** Integrate PredictHQ data with your Power BI (or other analytics tool) dynamic pricing workflows. See the [Power BI Tutorial ](../guides/tutorials/using-event-data-in-power-bi.md)and [Tableau Tutorial](../guides/tutorials/using-event-data-in-tableau.md).
* **Load event data to your warehouse:** Take PredictHQ API data and load it into a data warehouse. [Read tutorial](../guides/tutorials/loading-event-data-into-a-data-warehouse.md).
* **Machine learning models:** Automatically and dynamically update your pricing by integrating PredictHQ data directly into your demand forecasting models. [Read tutorial.](../guides/tutorials/improving-demand-forecasting-models-with-event-features.md)

**Getting Started**

1. Quick [filters](../guides/industry-specific-event-filters.md) for retail:
   1. Relevant Event Categories: `public holidays`, `performing-arts`, `community`, `conferences`, `festivals`
   2. Location Type: `Center Point & Radius`
   3. Minimum PHQ Rank: 50

**Example in Practice**

In the retail industry, much like in transportation and parking, failing to recognize demand fluctuations can lead to missed revenue opportunities and operational challenges. Significant events like Black Friday, Christmas, and local festivals can cause sales to surge by 50% to 100% above normal levels. Also, attended events happening nearby retail locations can drive significant fluctuations in demand. Dynamic pricing is a pivotal strategy in harnessing these surges effectively.

Optimizing ML Features

Integrating event-based ML features into forecasting models is essential for accurate demand predictions to improve your dynamic pricing. When you are considering updating a demand forecast you need to figure out which event-based machine learning features to add to your forecast. You can analyze your locations using [Beam](https://app.gitbook.com/s/Ri9YaBiPckypV66Jggc2/beam-relevancy-engine/an-overview-of-beam-relevancy-engine.md). [Upload demand data](https://app.gitbook.com/s/Ri9YaBiPckypV66Jggc2/beam-relevancy-engine/uploading-your-demand-data-to-beam.md), such as the number of units sold per day, and [view the top features](https://app.gitbook.com/s/Ri9YaBiPckypV66Jggc2/beam-relevancy-engine/feature-importance-with-beam-find-the-ml-features-to-use-in-your-forecasts.md) identified for your specific location.

Below is an example of a feature importance analysis - click to enlarge:

<img src="../../.gitbook/assets/feature-importance-result-screenshot.png" alt="" data-size="original">

Integrating Event Data

Retrieve the identified features using the [Features API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features) and incorporate them into your forecasting model by following the [demand forecasting tutorial](../guides/tutorials/improving-demand-forecasting-models-with-event-features.md).

Forecasting Demand

A London-based retailer used [Beam](https://app.gitbook.com/s/Ri9YaBiPckypV66Jggc2/beam-relevancy-engine/an-overview-of-beam-relevancy-engine.md) to evaluate the impact of events on their sales. They discovered that concerts (phq\_attendance\_concerts), sports (phq\_attendance\_sports), festivals (phq\_attendance\_festivals), conferences (phq\_attendance\_conferences), public holidays (phq\_rank\_public\_holidays), and observances (phq\_rank\_observances) significantly impacted their sales. The forecasting model was updated accordingly using the Features API, resulting in a substantial improvement in forecast accuracy. The new model shows better alignment between forecasted demand and actual sales, facilitating more effective dynamic pricing.

<img src="../../.gitbook/assets/Forecasting_graph_2.png" alt="" data-size="original">

Pricing Adjustments

With a refined forecasting model, businesses can adjust prices dynamically in response to predicted demand changes. This approach allows for pricing strategies that are both responsive and proactive, maximizing profitability during high-demand periods and maintaining competitive pricing when demand wanes.

</details>

<details>

<summary>Transportation &#x26; Parking</summary>

To implement PredictHQ data to inform dynamic pricing for your parking or transportation business, review the options below:

* **No code:** Use PredictHQ's WebApp, to unlock demand data weeks and months in advance to inform your manual pricing updates. [Read more](https://app.gitbook.com/s/Ri9YaBiPckypV66Jggc2/tools/see-event-trends-in-the-webapp.md) about Event Trends.
* **Business Intelligence (BI) tools:** Integrate PredictHQ data with your Power BI (or other analytics tool) dynamic pricing workflows. See the [Power BI Tutorial ](../guides/tutorials/using-event-data-in-power-bi.md)and [Tableau Tutorial](../guides/tutorials/using-event-data-in-tableau.md).
* **Load event data to your warehouse:** Take PredictHQ API data and load it into a data warehouse. [Read tutorial](../guides/tutorials/loading-event-data-into-a-data-warehouse.md).
* **Machine learning models:** Automatically and dynamically update your pricing by integrating PredictHQ data directly into your demand forecasting models. [Read tutorial.](../guides/tutorials/improving-demand-forecasting-models-with-event-features.md)

**Getting Started**

1. Quick [filters](../guides/industry-specific-event-filters.md) for transportation:
   1. Relevant Event Categories: `public holidays`, `performing-arts`, `conferences`, `conferences`, `community`
   2. Location Type: `City`
   3. Minimum PHQ Rank: 30
2. Quick [filters](../guides/industry-specific-event-filters.md) for parking:
   1. Relevant Event Categories: `public holidays`, `community`, `concerts`, `expos`, `performing-arts`
   2. Location Type: `Center Point & Radius`
   3. Minimum PHQ Rank: 35

**Example in Practice**

Consider a scenario where a city hosts a major sports championship and a large concert in the same week, or several small events over a weekend that collectively draw large crowds. This can lead to a significant surge in demand for transportation and parking, potentially doubling or tripling usual levels. Effectively capitalizing on these surges requires adopting dynamic pricing strategies.

Integrating Event Data

Many organizations use spreadsheets to manage pricing. To integrate PredictHQ's event data to your dynamic pricing, check out [connecting-to-predicthq-apis-with-microsoft-excel.md](../guides/tutorials/connecting-to-predicthq-apis-with-microsoft-excel.md "mention"). Follow this tutorial to connect event data for your location to Excel, ensuring it is automatically updated.

Analyzing Demand and Setting Prices

With parking inventory data in Excel, operators can compare the total attendees of nearby events against available parking spaces. For instance, the chart below shows the total daily attendance from local events (blue line) alongside parking bookings (orange line). Examining upcoming events for the next month helps adjust pricing based on anticipated demand.

![](<../../.gitbook/assets/image (95).png>)

On days like February 24th—coinciding with events such as the [San Francisco Chinese New Year Parade](https://events.predicthq.com/events/DGCqwsuA8vGgAfRNB5), [Chinatown Community Street Fair](https://events.predicthq.com/events/CrUsXRVXWaDDNbBQcR), the [Noise Pop](https://events.predicthq.com/events/DUEqiDG2U3e3yqm9Mh) festival among others—demand surges create a "perfect storm". In response, operators increase parking rates to accommodate the expected full capacity. All event details are available in the spreadsheet and can be accessed by filtering down to specific days.

Pricing Adjustments

This approach enables operators to proactively adjust pricing and accommodate expected full capacities. By analyzing past trends and upcoming events, operators can optimize pricing to maximize revenue and manage capacity effectively. This is a simple way to get event data into your tools and to easily use it for day-to-day operations.

Learn how [ParkMobile uses intelligent event data to boost parking reservations](https://www.predicthq.com/customers/parkmobile).

</details>
