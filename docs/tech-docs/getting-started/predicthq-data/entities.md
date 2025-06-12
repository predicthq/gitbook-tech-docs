# Entities

Entities are things with defined attributes, such as performers, music bands, venues, sports teams, and more. Our entities system is integral to our verification, enrichment, deduplication, and ranking processes. Entities allow us to accurately estimate attendance and impact given that they are stable as opposed to a moving object such as ticket sales.

For example, a concert will take place in or at a venue entity, where people will watch a performer entity. Our system will factor in the popularity of a performer like Beyoncé when we rank her concert. A Beyoncé concert would likely rank much higher than a lesser-known artist.

## **Venue entities**

A venue is a physical location where an event happens. It could be an indoor area, e.g. xx hotel - conference room; or an entire building, e.g. xx stadium; or an outdoor area, e.g. xx park.

Venues will be provided along with latitude, longitude, and address to locate the event.

A venue can be found on an event record as an array of entities with the type of `venue`.

All events happening at the same venue will have the same latitude/longitude and street address.

Below is an example of the venue entity information returned in the Events API response

```json
{
  "entity_id": "hH4zrx9zYLiETvNZQrx2de",
  "name": "Moscone Center - West",
  "type": "venue",
  "formatted_address": "800 Howard Street\nSan Francisco, CA 94103\nUnited States of America"
},
```

## **Event Group entities**

Stored within the entities section on an event, an event group identifies [recurring events](../guides/date-and-time-guides/working-with-recurring-events.md) across the PredictHQ events dataset. For example, The (Summer) Olympics repeats every four years around summer time, therefore we would have an event group that is attached to all of our Summer Olympics events.

Events that are associated with event groups have the `recurring` label and also contain an entity with the type of `event-group` within the event data.

See [working with recurring events ](../guides/date-and-time-guides/working-with-recurring-events.md)for more details.

### Residencies entities

Residencies are a subset of event groups. Residencies describe a type of concert where an artist performs at the same venue for two or more shows. This means that residencies can last for several weeks or months, as long as each instance of a performance by the same artist is within one week (7 days) of one another.

Residencies can be identified by the `residency` label attached to the event group.

```json
        {
          "entity_id": "Hi7e2hz97iXk4EwDwNmMdx",
          "name": "Sabrina Carpenter, Taylor Swift at Melbourne Cricket Ground",
          "type": "event-group",
          "category": "concerts",
          "labels": [
            "residency"
          ]
        }
```

## Organization entities

{% hint style="info" %}
Not all plans and subscriptions have access to this type of entity. [Talk to us](https://www.predicthq.com/contact/sales) if you'd like access.
{% endhint %}

Organization entities are groups of people and include sports teams (e.g. Kansas City Chiefs), and bands (e.g. Coldplay).

Below is an example of organization entities showing two sports teams playing in an NFL game event:

```json
{
    "name": "Penn State Nittany Lions",
    "entity_id": "dkDMujewgkq35ytXgE9KEe",
    "type": "organization"
},
{
    "name": "Ohio State Buckeyes",
    "entity_id": "NQ9CEvhtfZBYBFi6pdZE26",
    "type": "organization"
}
```

## People entities

{% hint style="info" %}
Not all plans and subscriptions have access to this type of entity. [Talk to us](https://www.predicthq.com/contact/sales) if you'd like access.
{% endhint %}

People entities include individual performers like singers/musicians (e.g. Beyoncé), or comedians (e.g. Bill Burr). They also include individual sports people like golfers (e.g. Tiger Woods), tennis players (e.g. Roger Federer), motorsports drivers (e.g. Lewis Hamilton), and other types of individuals.

Below is an example of people entities showing performers for a concert:

```json
{
    "entity_id": "35cav6EYSVnsykJ8cTvggTD",
    "type": "person",
    "name": "Lionel Richie"
},
{
    "entity_id": "ksqpXJDQbmBiS6aYeTeANF",
    "type": "person",
    "name": "Billy Joel"
},
{
    "entity_id": "mALZFGmtWQKpm4E6pFskha",
    "type": "person",
    "name": "Sheryl Crow"
}
```

## Getting back all events for an entity with the API

To get back all events linked to an entity you can call the Events API by entity ID. You can use this to find all events at a venue, all instances of a recurring event, or all events linked to a people or organization entity.

For example the entity ID for the "Moscone Center - West" is hH4zrx9zYLiETvNZQrx2de. So if you query the events for that ID you will get back all events held at the Moscone Center - West. You can then use other filters to narrow down the time period, ranks, or anything else.

&#x20;Here is an example of calling the events API using the Moscone Center - West entity ID:

```
GET https://api.predicthq.com/v1/events?entity.id=hH4zrx9zYLiETvNZQrx2de HTTP/1.1
Accept: application/json
Authorization: Bearer $ACCESS_TOKEN
```

Similar to finding all events for an event-group entity for recurring events you need to first find the ID for the entity. So, for example, to do that for Dreamforce first, find a Dreamforce event, then look at the event-group entity ID on that event and use that entity ID to call the API.

## How can I use entities in Snowflake

Entities information is returned in Snowflake in the ENTITIES column. That contains all the entities' information mentioned above. Customers can query that column to find all events for an entity or to retrieve the relevant entities for an event

## What is the difference between labels and entities?

The difference between labels and entities is that labels describe the type of event whereas entities provide a 'link' from an event to a venue, performer, sports team, or other type of entity. Labels will tell you what type of sport an event is for (e.g. `nfl`) but they will not tell you what venue the event is held at or if the event is recurring. For concerts or festivals, labels will tell you whether the event is a rock music concert but not what band is playing. Entities provide information on the sports team for sports events, bands for music events, and so on.
