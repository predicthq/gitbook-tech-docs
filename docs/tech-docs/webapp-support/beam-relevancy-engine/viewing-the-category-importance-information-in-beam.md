---
description: See which categories have the most impact on your demand
---

# Viewing the Category Importance Information in Beam

Beam's Category Importance feature uses advanced machine learning models to identify the event categories that have the greatest impact on your demand. This is done automatically after you create an analysis and upload demand data for an individual location. The results are a list of categories with a significance rating for each. The category importance results are for an individual analysis of the location you selected for Beam.

For example, restaurants tend to be highly impacted by sports and public holidays while hotels tend to be more impacted by conferences and concerts. By running category importance you can see how your business locations are impacted by events.

Category Importance covers the attendance and non-attended categories shown plus severe weather in the unscheduled category. It does not cover other categories not shown (such as disaster events).

Below is an example:

<figure><img src="../../.gitbook/assets/image (50).png" alt=""><figcaption><p>Category Importance example in a Beam Analysis</p></figcaption></figure>

In this example, we can see a very high impact from conferences, expos, performing arts, observances, and academic category events. The other categories have less impact on this location and as shown as "Minor" or "Marginal" impact. If a category shows a "-" then it does not have a statistically significant impact on demand based on the data uploaded or there are no events from this category taking place within the selected radius around the location.

You can use Beam to find out how different types of events are impacting your demand. If you are not sure what types of events impact your demand then create a Beam analysis with your demand data and look at the results.

Many customers use the Beam results to help decide what event-based machine learning features to add to their machine learning models.

Beam uses the[ ](../../api/beam/get-feature-importance.md)[get-feature-importance.md](../../api/beam/get-feature-importance.md "mention") API call to return sets of features related to important categories based on the category importance results for analysis. Anything that you can do in the WebApp can also be done via the [Beam API](../../api/beam/). Use the Beam API if you want to create a large number of analyses.

We also provide a "View ML Features" option for an analysis - see [Find the ML Features to use in your forecast](feature-importance-with-beam-find-the-ml-features-to-use-in-your-forecasts.md) for more info on how to use this.

### _p_-values <a href="#object-object-values" id="object-object-values"></a>

_p_-values represent statistical significance and we assign a readable label to each category based on it's _p_-value. There is a toggle to view as _p_-values for advanced users. This is intended for use by data science teams interested in digging deeper into the results.

<figure><img src="../../.gitbook/assets/image (52).png" alt=""><figcaption><p>Category Importance showing <em>p</em>-values</p></figcaption></figure>

Note: very small _p_-values will be shown as <0.001. This can refer to results that are smaller than 0.001, e.g. 0.0005. A category that is considered to have no impact on the location will show a "-" label and no _p_-value will be shown.

The mapping of _p_-values to the impact levels shown on the Category Importance graphs is below:\


<figure><img src="../../.gitbook/assets/image (54).png" alt=""><figcaption><p>Mapping of <em>p</em>-values</p></figcaption></figure>

* 0.6 ≤ _p_ < 1.0 - Marginal
* 0.1 ≤ _p_ < 0.6 - Minor
* 0.075 ≤ _p_ < 0.1 - Moderate
* 0.05 ≤ _p_ < 0.075 - High
* _p_ < 0.05 - Very high
