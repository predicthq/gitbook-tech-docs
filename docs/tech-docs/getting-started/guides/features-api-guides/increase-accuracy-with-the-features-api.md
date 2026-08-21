# Increase Accuracy with the Features API

{% embed url="https://www.youtube.com/watch?v=FpTUVdQC7hw" %}
Features API Product Demo
{% endembed %}

Once you’ve familiarized yourself with our data, you’ll likely find that focusing on individual spikes often leads to a data set too small to accurately correlate. By doing it at an aggregate level, a data science team will be looking at the volume of spike days to prove a correlation between demand and events based on category features.

Features API aggregates PHQ Attendance figures, PHQ Viewership figures and PHQ Rank counts (in buckets by rank range) for a given category feature in a particular location on a given day, and returns desired statistics. These evaluated statistics can be used to quickly gauge and understand the demand impact on a location for a given day for a particular category. For example, at a future date in Sydney, there is a major sports game, a street fair, an international film festival, the Symphony orchestra playing, and more. The combined impact of all these events might result in a total aggregate attendance (when the various category aggregated attendance values are summed up) score of 150,000 and this could be across a hundred events or more. This represents a prediction of 150,000 people attending events on that day in the location.

The Features API returns requested statistical values (`sum`, `count`, `average`, `min`, `max`, `median`, `std_dev`) per day for a specified date range, across a specified attendance category feature - _see_ [PHQ Attendance Response](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features). Similarly, Features API returns requested statistical values, across a specified viewership category feature. For non-attendance-based events the rank of those events impacting that location on those days are bucketed into a relevant rank range in the response for evaluation.

See [the API documentation](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) for more details on the API. See also [this tutorial](../tutorials/improving-demand-forecasting-models-with-event-features.md) for how to incorporate features from the Features API into demand forecasting models.

### Calling the Features API

{% embed url="https://www.youtube.com/watch?v=zlw4ky5NjbA" %}
How to use Features API
{% endembed %}

{% hint style="success" %}
**Recommended: use `beam.analysis_id`**\
The most reliable way to call the Features API is by supplying a `beam.analysis_id`. This automatically applies the correct location boundary (from your Saved Location), selects only the event categories that materially drive demand at that location, and applies calibrated rank thresholds — no manual configuration needed. [Run Beam first](../beam-guides/), then pass the returned `analysis_id` to the Features API.
{% endhint %}

The [Features API reference](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/features/get-features) documents the request format with code examples for both patterns: keyed by `beam.analysis_id` (recommended), or manual configuration with a `saved_location_id` and explicit feature names while you're exploring. If you're choosing feature names manually before you can run Beam, start from your industry's [recommended categories](../industry-specific-event-filters.md).
