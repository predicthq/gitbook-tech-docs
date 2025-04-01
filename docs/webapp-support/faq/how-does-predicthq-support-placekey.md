# How Does PredictHQ Support Placekey?

Placekey is a free, universal standard identifier for any physical place, which enables the data pertaining to those places to be easily shared across organizations. PredictHQ provides Placekeys for events data to allow organizations to join our events data to other datasets that use Placekeys. See the [Placekey website](https://www.placekey.io/) for more information.

A common use of Placekey and events data is to provide additional information about the Point of Interest (POI) where the event took place. POI data provides detailed information about a location such as address, latitude/longitude, and open hours – and can also be enriched with data, including spend data, to reveal what’s happening at a location. The combination of events and POI data helps clarify exactly what is driving demand at a location. For example, combining events data with spend data to identify what is driving a spike in spend at a particular location.

Check out [Using Placekey to join events data and POI data](../../getting-started/guides/geolocation-guides/join-events-using-placekey.md) for a technical guide to using Placekey.

In the PredictHQ products and tools Placekey is supported in the following ways:

* You can search on Placekey in the events API using the Placekey filter – see placekey under [Event Filters](../../api/events/search-events.md) in the Events API endpoint documentation.
* The Placekey field is returned in the Events API response – see [Event fields](../../api/events/search-events.md#response-fields).
* You can try the Placekey field in the API Explorer in Control Center for the Events API.
* Placekey is returned in the [Snowflake](../../integrations/third-party-integrations/snowflake/) and [AWS Data Exchange](../../integrations/third-party-integrations/aws-data-exchange/) (ADX) integrations.
* The Placekey field is included in the [WebApp export](../getting-started/export-events-data-from-the-webapp.md)

Note that at the time of release, Placekey is returned for our 7 [attended event categories](https://www.predicthq.com/intelligence/data-enrichment/event-categories) and is published for events from 23 November 2020 onwards.
