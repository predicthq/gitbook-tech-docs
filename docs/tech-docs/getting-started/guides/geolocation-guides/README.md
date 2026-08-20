# Geolocation Guides

How to scope PredictHQ queries to the places your business cares about.

The recommended pattern is one setup step: create a [Saved Location](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/saved-locations/overview) from a lat/lon origin and let Predicted Impact Area calculate the boundary where events actually affect that location - then reference the `location_id` everywhere. The guides in this section cover the underlying mechanics when you need them: [searching by location](searching-by-location/), [place hierarchies](understanding-place-hierarchies.md), [polygons](working-with-polygons.md), and [joining events with Placekey](join-events-using-placekey.md).

Avoid hand-picked fixed radii - they include irrelevant events and miss relevant ones. See the [overview](overview.md) for how the location methods compare.
