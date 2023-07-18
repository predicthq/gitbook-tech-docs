# Entities

Entities are things with defined attributes, such as performers, music bands, venues, sports teams and more. Our entities system is integral to our verification, enrichment, deduplication and ranking processes. Entities allow us to accurately estimate attendance and impact given that they are stable as opposed to a moving object such as ticket sales.

For example, a concert will take place in or at a venue entity, where people will watch a performer entity. Our system will factor in the popularity of a performer like Beyoncé when we rank her concert. A Beyoncé concert would likely rank much higher than a lesser known artist.

## **Venue**

A venue is a physical location where an event happens. It could be an indoor area, e.g. xx hotel - conference room; or an entire building, e.g. xx stadium; or an outdoor area, e.g. xx park.

Venues will be provided along with both latitude and longitude and address to locate the event.

A venue can be found on an event record as an array of entities with the type of `venue`.

All events happening at the same venue will have the same latitude/longitude and street address.

## **Event Group**

Stored within the entities section on an event, an event group identifies [recurring events](https://docs.predicthq.com/categoryinfo/recurring-events) across the PredictHQ events dataset. For example, The (Summer) Olympics repeats every four years around summer time, therefore we would have an event group that is attached to all of our Summer Olympics events.

Events that are associated with event groups have the `recurring` label and also contain an entity with the type of `event-group` within the event data.
