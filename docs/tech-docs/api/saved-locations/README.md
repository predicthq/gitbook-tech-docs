# Saved Locations

{% hint style="info" %}
This endpoint is currently in beta.
{% endhint %}

Saved Locations are persistent, user-defined geographic entities that serve as reusable identifiers across PredictHQ’s platform. Defined using a name and a GeoJSON location shape, they may also include an external ID and optional labels for filtering or grouping.

Saved Locations simplify how you access event data, generate features, and run forecasts by eliminating the need to repeatedly supply raw coordinates or radius settings in each API call. We strongly recommend all customers use Saved Locations to ensure consistency and scalability across location-specific workflows, especially when managing large sets of business locations.
