# Saved Locations

{% hint style="info" %}
This endpoint is currently in beta.
{% endhint %}

The Saved Locations API is used for managing Location Insights Locations. See this [overview of Location Insights](https://www.predicthq.com/support/location-insights-overview). The name of the feature is Location Insights and the name of the API is the Saved Locations API.

You can use the Saved Locations API to implement [all of the functionality](https://www.predicthq.com/support/category/location-insights) that you'll see in PredictHQ's Control Center. If you have access to the PredictHQ APIs you will have access to use the Saved Locations API with the same permissions that you will have for Events API. E.g. if you have purchased access to Seattle and Los Angeles you will be able to use the Saved Locations API to create location insights within these geographic areas.

Note that the Saved Locations backend runs an asynchronous enrichment process. After a location is created it will be enriched with details on the number of events and the number of people attending events within a location. This process runs immediately after event creation and the location statistics are periodically updated in the background on a scheduled basis.

\
