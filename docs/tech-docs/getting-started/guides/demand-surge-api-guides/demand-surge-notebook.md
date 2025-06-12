# Demand Surge Notebook

Demand surges reflect an unusual increase in daily event impact for a location and date range. In this notebook, we use the Features API to scan and identify potential surge or outlier dates by looking at the total daily attendance of Attended Events.

Surge dates are defined as dates where the total daily attendance value is more than 3 standard deviations away from the mean (for a location and date range). If one or more surge dates are identified, the total daily attendance and examples of top events are returned per date. Running the notebook is simple and only requires a location, date range and Access Token.

{% embed url="https://www.youtube.com/watch?v=ja_rhf-sjNA" %}
Tracking Demand Surges
{% endembed %}

Run through the [Demand Surge notebook](https://github.com/predicthq/phq-data-science-docs/blob/master/demand-surge/demand-surge-notebook.ipynb) or even easier, use our new [Demand Surge API](broken-reference).
