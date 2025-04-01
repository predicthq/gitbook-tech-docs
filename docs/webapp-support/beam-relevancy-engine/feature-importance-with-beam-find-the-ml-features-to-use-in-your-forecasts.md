# Feature Importance With Beam - Find the ML Features to Use in Your Forecasts

**Use the View ML Features option in Beam to find important features.**

Harness the power of events in your forecast by incorporating machine learning (ML) features for events into your models. Creating new ML features can be time-consuming and expensive, often requiring significant effort from data scientists, data engineers, and others. PredictHQ provides a toolkit to allow you to easily integrate prebuilt, forecast-ready ML features with Beam, and the Features API.

To do this quickly and easily, the first step is to upload your aggregated demand data into [Beam](an-overview-of-beam-relevancy-engine.md) through the [WebApp](https://control.predicthq.com/beam) or via the [Beam API](../../api/beam/). Beam, our relevancy engine tool, returns category importance results (also known as feature importance) for individual business locations as well as large groups.

Category importance uses our underlying [Feature Importance API](../../api/beam/get-feature-importance.md) and is generated from an analysis of the relevance of the results of that API. Under the hood in Beam, we have a list of ML features and their p-values.

To improve the accuracy of your forecasts, start by incorporating event-based ML features from the Features API into your models. Open an individual Beam analysis or analysis group and you will see the "**Get Forecasting Features**" option. This provides a list of ML features that you can use to train your models. You can copy these features and use them in your code as described in our [Get ML Features ](../../getting-started/guides/features-api-guides/feature-engineering-guide.md)guide.

Below is a screenshot showing the new "Get Forecasting Features" option:

<figure><img src="../../.gitbook/assets/image (71).png" alt=""><figcaption><p>Get Forecasting Features menu under the Category Importance section</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (72).png" alt=""><figcaption><p>Get Forecasting Features example</p></figcaption></figure>

This option returns code for calling the Features API including rank filters. By default, it calls features for the next 3 months.

The other options available are:

* **Get all Event details** - Provides code for calling the Events API. By default, this option calls the Events API and is filtered on the impactful categories, the radius for the Beam analysis, and the suggested rank filter. This will give you code to return future events that are predicted to impact you based on the Beam analysis.
* **View list of Features** - Shows a list of ML Features from the Features API. This is similar to the Get Forecasting Features option but it does not include all the code to call the Features API. It's just a list of features. These features can be copied into a Jupyter notebook, or code or used in other applications.

Here’s how to use Beam and the Features API for your forecast in five simple steps:

1. [Run Beam](an-overview-of-beam-relevancy-engine.md) across your locations and [create a group](grouping-analyses-in-beam.md) to get feature importance results to identify the top 5 or 10 most impactful features.
   1. In the WebApp, open a Beam Analysis for your group and click on "**Get Forecasting Features**" to access the code to call the Features API.
   2. Copy the code.
2. Call the Features API (see the [Get ML Features](../../getting-started/guides/features-api-guides/feature-engineering-guide.md) guide) to download historical event features to train your model across all your locations (change the date range).
3. Train the ML Model.
4. Integrate calls to the Features API in your pipeline and pass values to the model for the future-facing period they are forecasting.
5. Deploy the updated model to production.

If you want to see more details than what is returned by the "**Get Forecasting Features**" option in the WebApp, you can call [Get Feature Importance](../../api/beam/get-feature-importance.md) in the Beam API.
