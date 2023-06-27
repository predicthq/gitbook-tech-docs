---
description: Search for events.
---

# Events API

Events API is used primarily for Event Visibility - being able to see what events are happening where. If you're looking to use aggregated event data for forecasts or other use-cases please take a look at our Features API.

### Search Events

[RAW](https://docs.predicthq.com/resources/events)

```bash
GET /v1/events/
```

#### Example

[CURL](https://docs.predicthq.com/resources/events)[PYTHON](https://docs.predicthq.com/resources/events)[RAW](https://docs.predicthq.com/resources/events)

```bash
curl -X GET https://api.predicthq.com/v1/events/?id=5uRg7CqGu7DTtu4Rfk \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```

[JSON](https://docs.predicthq.com/resources/events)

```json
{
    "count": 1,
    "overflow": false,
    "next": null,
    "previous": null,
    "results": [
        {
            "relevance": 0.0,
            "id": "5uRg7CqGu7DTtu4Rfk",
            "parent_event": {
                "parent_event_id": "w7dYyrFwTUQGYE6euv"
            },
            "title": "Formula 1 2019 - United States Grand Prix 2019 - Race",
            "description": "The 2019 United States Grand Prix (officially known as the Formula 1 Emirates United States Grand Prix 2019) was a Formula One motor race held on 3 November 2019 at the Circuit of the Americas in Austin, Texas, United States. The race was the 19th round of the 2019 Formula One World Championship (1 - 3 Nov) and marked the 49th running of the United States Grand Prix.",
            "category": "sports",
            "labels": [
                "auto-racing",
                "f1",
                "sport"
            ],
            "rank": 92,
            "local_rank": 100,
            "aviation_rank": 93,
            "phq_attendance": 120000,
            "entities": [
                {
                    "entity_id": "MasUgUJtWz3kQFVgCG6rJU",
                    "name": "Circuit of the Americas",
                    "type": "venue",
                    "formatted_address": "9201 Circuit of the Americas Boulevard\nAustin, TX 78617\nUnited States of America"
                }
            ],
            "duration": 7200,
            "start": "2019-11-03T19:10:00Z",
            "end": "2019-11-03T21:10:00Z",
            "updated": "2022-11-10T19:50:36Z",
            "first_seen": "2019-07-04T22:14:31Z",
            "timezone": "America/Chicago",
            "location": [
                -97.63585109999997,
                30.1345808
            ],
            "geo": {
                "geometry": {
                    "coordinates": [
                        -97.63585109999997,
                        30.1345808
                    ],
                    "type": "Point"
                },
                "placekey": "222-229@8t2-fgc-z2k"
            },
            "scope": "locality",
            "country": "US",
            "place_hierarchies": [
                [
                    "6295630",
                    "6255149",
                    "6252001",
                    "4736286",
                    "4737316",
                    "4689116"
                ],
                [
                    "6295630",
                    "6255149",
                    "6252001",
                    "4736286",
                    "4737316",
                    "4671654"
                ]
            ],
            "state": "active",
            "private": false
        }
    ]
}
```

### Event Fields

Below are the fields returned by the Events endpoint. Please note that these are not the fields used for filtering - please refer to the [Search Events](https://docs.predicthq.com/resources/events/#search-events) section to discover which parameters can be used for filtering events.

JSON Schemas are available for the Events endpoint and for a single event:

* [events-response-schema.json](https://docs.predicthq.com/docs/schema/events-response-schema.json)
* [event-schema.json](https://docs.predicthq.com/docs/schema/event-schema.json)

| FIELD                                                                       | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><strong>aviation_rank</strong><br>number, null<br><em>read-only</em></p> | <p>A log scale numerical value between 0 and 100 with a <a href="https://docs.predicthq.com/resources/events#param-aviation_rank_level">five-level hierarchical impact schema</a>. Aviation Rank indicates how much an event will impact flight bookings by considering both domestic and international travel. It can be mapped to the predicted increase in demand based on people flying to an event. Therefore, events with higher Aviation Rank are expected to result in more people taking flights than lower Aviation Rank events.<br><br>Aviation Rank is calculated for events in the categories <code>concerts</code>, <code>conferences</code>, <code>expos</code>, <code>sports</code>, <code>festivals</code>, <code>performing-arts</code>, <code>observances</code>, <code>public-holidays</code>, and <code>school-holidays</code>.<br><br>If <code>aviation_rank</code> is not intended to be available for an event or we couldn't calculate it, this field will be <code>null</code>.<br>E.g. <code>85</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <p><strong>cancelled</strong><br>string, null<br><em>read-only</em></p>     | <p>The date the event was set to cancelled in the system in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br><br>All dates are in UTC.<br><br>This field will only be present for events with <code>deleted_reason</code> set to <code>cancelled</code>, and will have a <code>null</code> value if <code>cancelled</code> date is not available.<br><br>E.g. <code>2018-12-19T10:00:00Z</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <p><strong>category</strong><br>string<br><em>read-only</em></p>            | <p>The category of the event<br><strong>Possible values:</strong></p><ul><li><code>academic</code></li><li><code>school-holidays</code></li><li><code>public-holidays</code></li><li><code>observances</code></li><li><code>politics</code></li><li><code>conferences</code></li><li><code>expos</code></li><li><code>concerts</code></li><li><code>festivals</code></li><li><code>performing-arts</code></li><li><code>sports</code></li><li><code>community</code></li><li><code>daylight-savings</code></li><li><code>airport-delays</code></li><li><code>severe-weather</code></li><li><code>disasters</code></li><li><code>terror</code></li><li><code>health-warnings</code></li></ul><p>E.g. <code>concerts</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <p><strong>country</strong><br>string<br><em>read-only</em></p>             | <p>The country code in <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> format.<br>Note that the <code>country</code> value will usually be present but in some cases where the event location is not within a country (e.g. an earthquake in the middle of the ocean) it can be empty.<br><br>E.g. <code>NZ</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <p><strong>deleted_reason</strong><br>string<br><em>read-only</em></p>      | <p>The reason why the event was deleted.<br><br>Note that this field is only present for events with state <code>deleted</code>.<br><br><strong>Possible values:</strong></p><ul><li><code>cancelled</code></li><li><code>duplicate</code></li><li><code>invalid</code></li><li><code>postponed</code></li></ul><p>E.g. <code>duplicate</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <p><strong>description</strong><br>string<br><em>read-only</em></p>         | <p>A description of the event.<br>E.g. <code>See Katy Perry in concert [...]</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <p><strong>duplicate_of_id</strong><br>string<br><em>read-only</em></p>     | <p>The <code>id</code> of the active event this event is a duplicate of.<br><br>Note that this field is only present for deleted events with <code>deleted_reason</code> set to <code>duplicate</code>.<br><br>E.g. <code>z13B3870YOgv</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <p><strong>duration</strong><br>number<br><em>read-only</em></p>            | <p>The duration of the event in seconds.<br><br>E.g. <code>3600</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <p><strong>end</strong><br>string<br><em>read-only</em></p>                 | <p>The end date of the event in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br><br>All end dates are in UTC <strong>if the event time zone is provided</strong>, and in local time otherwise. For example, Independence Day falls on the 4th of July regardless of the time zone, and will have a <code>null</code> time zone.<br><br>E.g. <code>2018-12-19T10:00:00Z</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <p><strong>entities</strong><br>array<br><em>read-only</em></p>             | <p>An array of entities linked to the event.<br><br><strong>Possible types:</strong></p><ul><li><code>event-group</code></li><li><code>venue</code></li></ul><p>E.g. <code>[{"entity_id": "328DxFUbRKvaiJJGyT2gReF", "type": "venue", "name": "Spark Arena", "formatted_address": "Mahuhu Crescent\nAuckland 1010\nNew Zealand"}]</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <p><strong>first_seen</strong><br>string, null<br><em>read-only</em></p>    | <p>The date the event first entered our dataset in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format. All dates are in UTC. This value may be missing on some events, and should not be considered an event announcement date.<br><br>E.g. <code>2017-12-19T06:00:00Z</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <p><strong>id</strong><br>string<br><em>read-only</em></p>                  | <p>The unique identifier of the event.<br><br>E.g. <code>z13B3870YOgv</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <p><strong>impact_patterns</strong><br>object<br><em>read-only</em></p>     | <p>Also known as “Demand impact patterns”. This field shows impact for leading days (days before the event), lagging days (days after an event) and the days the event occurs.<br><br><code>impact_patterns</code> is an array of impact pattern objects. The same event can have different impact patterns for different industry verticals. It contains the following fields:</p><ul><li><code>vertical</code> - The industry vertical the impact pattern applies to. The initial release is for the retail industry so this field will show <code>retail</code>. Future releases could apply to other industries like accommodation.</li><li><code>impact_type</code> - Indicates the type of impact shown in the impact pattern. The current version supports PHQ rank only (<code>phq_rank</code>). Future versions could show the impact to attendance or other values.</li></ul><p><code>impacts</code> is an array of objects with one entry for each day that contains the following values:</p><ul><li><code>date_local</code> - the date in the local timezone of the event.</li><li><code>value</code> - the value of the <code>impact_type</code> for that given day. For example, if the <code>impact_type</code> was <code>phq_rank</code> the value would be the PHQ Rank value on the given day.</li><li><code>position</code> - can be <code>leading</code>, <code>event_day</code> or <code>lagging</code>. <code>leading</code> are the days before the event occurs, <code>event_day</code> are the days the event occurs and <code>lagging</code> are the days after the event has occurred.</li></ul><p>E.g. <code>{ "date_local": "2022-01-08", "value": 10, "position": "leading" }, { "date_local": "2022-01-09", "value": 21, "position": "event_day" },…</code></p> |
| <p><strong>labels</strong><br>array<br><em>read-only</em></p>               | <p>The labels associated with the event. Use the <a href="https://docs.predicthq.com/resources/events#retrieve-events-count">count endpoint</a> to fetch a list of available labels.<br><br>E.g. <code>["holiday", "holiday-national"]</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <p><strong>local_rank</strong><br>number, null<br><em>read-only</em></p>    | <p>Similar to PHQ Rank, this is a log scale numerical value between 0 and 100 with a <a href="https://docs.predicthq.com/resources/events#param-local_rank_level">five-level hierarchical impact schema</a>. It is designed to represent the potential impact of an event on its local geographical area.<br><br>Local Rank is calculated for events in the categories <code>community</code>, <code>concerts</code>, <code>conferences</code>, <code>expos</code>, <code>sports</code>, <code>festivals</code>, <code>performing-arts</code>.<br><br>If <code>local_rank</code> is not intended to be available for an event, this field will be <code>null</code>.<br>E.g. <code>72</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <p><strong>location</strong><br>array<br><em>read-only</em></p>             | <p>A 2-tuple representing the geo location of the event. Note that the longitude/latitude coordinates use the <a href="https://geojson.org/">GeoJSON order</a> [lon, lat].<br><br>E.g. <code>[174.776792, -36.847319]</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <p><strong>geo</strong><br>object<br><em>read-only</em></p>                 | <p>An object containing the geographic information about an event. This field will be used in future instead of the <strong>location</strong> field (the location field will remain in the current version of the API but could be removed in future versions).<br><br>Currently, this field has only one subfield: <strong>geometry</strong>, which represents the geometry associated with the event in the <a href="https://geojson.org/">GeoJSON format</a>.<br><br><strong>Possible types:</strong></p><ul><li><code>Point</code></li><li><code>Polygon</code></li><li><code>MultiPolygon</code></li></ul><p>E.g. <code>{"geometry": {"type: "Point", "coordinates": [174.776792, -36.847319]}}</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <p><strong>parent_event</strong><br>object<br><em>read-only</em></p>        | <p>Used to indicate if this event is part of a larger event. These types of events are called umbrella events in the system. For example, a large multi-day parent umbrella event may have individual child events for sessions on different days. For example the Formula 1 2019 United States Grand Prix has child events for the qualification, 3 practice events, a concert that occurs at the Grand Prix, and the actual race events (there are 12 child events).<br><br>See <a href="https://docs.predicthq.com/guides/multi-day-and-umbrella-events/#umbrella-events-beta">umbrella events</a> for details on this field and details on what umbrella events are.<br><br>Note that this field in this release only shows if a child event has a parent id. It does not indicate if a parent event has child events.<br><br>E.g. <code>{"parent_event_id": "w7dYyrFwTUQGYE6euv"}</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <p><strong>phq_attendance</strong><br>number<br><em>read-only</em></p>      | <p>A numerical value that reflects the predicted attendance number for supported attendance-based categories. The following categories are supported: concerts, performing arts, sports, expos, conferences, community and festivals.<br><br>phq_attendance reflects the entire attendance for multi-day events (the number of people attending across the full duration of the event) except for some categories like conferences where it is the daily attendance.<br>See <a href="https://docs.predicthq.com/guides/multi-day-and-umbrella-events/">Handling multi-day and Umbrella events</a> for more details.<br><br>E.g. <code>2511</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <p><strong>place_hierarchies</strong><br>array<br><em>read-only</em></p>    | <p>An array of place hierarchies for the event. Each hierarchy is an array of place ids (see <a href="https://docs.predicthq.com/resources/places">Places</a>). The final place in a hierarchy is a specific place the event applies to. Each place is a sub-place of the place immediately preceding it in the hierarchy.<br><br>For example, a hierarchy might contain the following places in this order: <code>Earth > Europe > United Kingdom > England > Nottingham</code><br><br>Note that the <code>place_hierarchies</code> value can be an empty array in some cases.<br><br>E.g. <code>[["6295630", "6255148", "2635167", "6269131", "3333178", "2641170"]]</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <p><strong>placekey</strong><br>string<br><em>read-only</em></p>            | <p>The Placekey (See <a href="https://www.placekey.io/">placekey.io</a>) reflects the location of an event in the format <code>what@where</code>. Placekey is part of the geo field for an event.<br><br><strong>Possible formats</strong></p><ul><li><code>{address}-{poi}@{where}</code></li><li><code>{address)@{where}</code></li><li><code>@where</code></li></ul><p>E.g. <code>"placekey": "222-229@8t2-fgc-z2k" or "placekey": "@7f7-mcy-ndv"</code><br><br>Note that Placekey applies to our <a href="https://www.predicthq.com/intelligence/data-enrichment/event-categories">attended event categories</a>. Some events do not contain a Placekey.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <p><strong>postponed</strong><br>string, null<br><em>read-only</em></p>     | <p>The date the event was set to postponed in the system in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br>All dates are in UTC.<br><br>This field will only be present for events with <code>deleted_reason</code> set to <code>postponed</code>, and will have a <code>null</code> value if <code>postponed</code> date is not available.<br><br>E.g. <code>2018-12-19T10:00:00Z</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <p><strong>predicted_end</strong><br>string<br><em>read-only</em></p>       | <p>The predicted end date of the event in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br><br>Predicted end dates are in UTC <strong>if the event time zone is provided</strong>, and in local time otherwise. For example, Independence Day falls on the 4th of July regardless of the time zone, and will have a <code>null</code> time zone.<br><br>This field will only be present if an actual <code>end</code> time is <em>not</em> available for an event and we have a predicted end time.<br><br>E.g. <code>2018-12-19T10:00:00Z</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <p><strong>rank</strong><br>number<br><em>read-only</em></p>                | <p>A log scale numerical value between 0 and 100 with a <a href="https://docs.predicthq.com/resources/events#param-rank_level">five-level hierarchical impact schema</a>. It is designed to represent the potential impact of an event independent of its geographical location.<br><br>E.g. <code>83</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <p><strong>relevance</strong><br>number, null<br><em>read-only</em></p>     | <p>Relative relevance of the event to the event search.<br>See the <a href="https://docs.predicthq.com/resources/events#param-relevance">relevance</a> parameter for information on how relevance is calculated.<br>E.g. <code>2.9654586</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <p><strong>scope</strong><br>string<br><em>read-only</em></p>               | <p>The geographical scope the events apply to.<br><strong>Possible values:</strong></p><ul><li><code>locality</code></li><li><code>localadmin</code></li><li><code>county</code></li><li><code>region</code></li><li><code>country</code></li></ul><p>E.g. <code>locality</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <p><strong>start</strong><br>string<br><em>read-only</em></p>               | <p>The start date of the event in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br><br>All start dates are in UTC <strong>if the event time zone is provided</strong>, and in local time otherwise. For example, Independence Day falls on the 4th of July regardless of the time zone, and will have a <code>null</code> time zone.<br><br>If an event has a start time of midnight (in the event time zone) this is an indication that the actual time may be unknown. You may wish to omit the time when displaying these events.<br><br>E.g. <code>2018-12-19T06:00:00Z</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <p><strong>state</strong><br>string<br><em>read-only</em></p>               | <p>The publication state of the event.<br><strong>Possible values:</strong></p><ul><li><code>active</code>: the event is published and valid.</li><li><code>deleted</code>: the event was removed, either because it was cancelled or is a duplicate.</li><li><code>predicted</code>: events that have an unconfirmed start time i.e for which the exact time the event begins is not yet known.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <p><strong>timezone</strong><br>string, null<br><em>read-only</em></p>      | <p>The time zone of the event in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format. This is helpful so you know which time zone to convert the dates to (if needed).<br><br>If the time zone is <code>null</code>, the <code>start</code> and <code>end</code> date should be regarded as time zone agnostic and already being in local time. Our <code>start</code> and <code>end</code> filters take this into account when specifying a lower and higher bound on dates.<br><br>E.g. <code>Pacific/Auckland</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <p><strong>title</strong><br>string<br><em>read-only</em></p>               | <p>The title of the event.<br><br>E.g. <code>Katy Perry</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <p><strong>updated</strong><br>string<br><em>read-only</em></p>             | <p>The last modification date of the event in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format. All dates are in UTC.<br><br>E.g. <code>2018-05-01T05:00:00Z</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### Event Counts

This endpoint accepts the same parameters as the ones described in [Search Events](https://docs.predicthq.com/resources/events#search-events) and can be used to get aggregated counts of all matching events that are available to your account.

A JSON Schema is available for the Events Count endpoint: [events-count-schema.json](https://docs.predicthq.com/docs/schema/events-count-schema.json)

#### Action

[RAW](https://docs.predicthq.com/resources/events)

```bash
GET /v1/events/count/
```

#### Example

[CURL](https://docs.predicthq.com/resources/events)[PYTHON](https://docs.predicthq.com/resources/events)[RAW](https://docs.predicthq.com/resources/events)

```bash
curl -X GET https://api.predicthq.com/v1/events/count/?country=NZ \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```

[JSON](https://docs.predicthq.com/resources/events)

```json
{
  "count": 271423,
  "top_rank": 100.0,
  "top_local_rank": 100.0,
  "top_aviation_rank": 100.0,
  "rank_levels": {
    "1": 163349,
    "2": 75098,
    "3": 17178,
    "4": 5873,
    "5": 9925
  },
  "local_rank_levels": {
    "1": 10524,
    "2": 143054,
    "3": 76958,
    "4": 16460,
    "5": 6323
  },
  "aviation_rank_levels": {
    "1": 25952,
    "2": 78,
    "3": 987,
    "4": 767,
    "5": 212
  },
  "categories": {
    "academic": 2300,
    "airport-delays": 16570,
    "community": 27100,
    "concerts": 44056,
    "conferences": 72503,
    "daylight-savings": 26,
    "disasters": 418,
    "expos": 1601,
    "festivals": 47931,
    "health-warnings": 28,
    "observances": 198,
    "performing-arts": 52698,
    "politics": 12,
    "public-holidays": 434,
    "school-holidays": 38,
    "severe-weather": 277,
    "sports": 7519,
    "terror": 14
  },
  "labels": {
    "agriculture": 60,
    "airport": 16570,
    "american-football": 10,
    "animal": 12,
    "architecture": 6,
    "arson": 11,
    "attack": 12,
    "attraction": 8904,
    "auto-racing": 7,
    "automotive": 20,
    "avalanche": 2,
    "baseball": 21,
    "basketball": 271,
    "bicycle": 1,
    "blizzard": 1,
    "bombing": 2,
    "boxing": 10,
    "business": 3364,
    "campus": 575,
    "career": 187,
    "chemical": 3,
    "closed-doors": 4,
    "clothing": 26,
    "club": 200,
    "cold-wave": 1,
    "comedy": 914,
    "comic": 15,
    "community": 4616,
    "concert": 70570,
    "conference": 72510,
    "construction": 71,
    "course": 2,
    "craft": 41,
    "cricket": 1064,
    "cyclone": 1,
    "daylight-savings": 26,
    "delay": 16570,
    "design": 6,
    "digital": 36,
    "disaster": 418,
    "drought": 3,
    "earthquake": 298,
    "education": 64667,
    "election": 7,
    "entertainment": 3253,
    "environment": 6,
    "epidemic": 1,
    "epidemic-hazard": 28,
    "expo": 1602,
    "family": 9484,
    "fashion": 165,
    "festival": 48574,
    "fire": 54,
    "flood": 106,
    "food": 824,
    "fundraiser": 2161,
    "furniture": 4,
    "gaming": 4,
    "health": 9829,
    "health-warning": 28,
    "heat-wave": 2,
    "hockey": 10,
    "holiday": 670,
    "holiday-local": 286,
    "holiday-national": 148,
    "household": 401,
    "ice-hockey": 20,
    "industrial": 93,
    "instrument": 19,
    "jewelry": 2,
    "landslide": 6,
    "lockdown": 4,
    "marathon": 210,
    "marine": 1,
    "medical": 222,
    "mineral": 2,
    "movie": 3431,
    "music": 71698,
    "natural": 2,
    "observance": 198,
    "observance-season": 52,
    "outdoor": 8663,
    "packaging": 9,
    "parliament": 7,
    "performing-arts": 55955,
    "pet": 3,
    "politics": 390,
    "print": 1,
    "product": 41,
    "rain": 13,
    "referendum": 5,
    "religion": 3234,
    "research-development": 1,
    "rugby": 1837,
    "running": 348,
    "school": 39,
    "science": 1019,
    "seminar": 4,
    "skating": 2,
    "snow": 3,
    "soccer": 3870,
    "social": 7557,
    "sport": 8159,
    "storm": 37,
    "technology": 1473,
    "tennis": 4,
    "terror": 14,
    "tornado": 42,
    "training": 1,
    "transportation": 51,
    "travel": 26,
    "tsunami": 10,
    "volcano": 28,
    "volleyball": 1,
    "weather": 277,
    "weather-warning": 6,
    "wedding": 1,
    "wildfire": 35,
    "wind": 9,
    "wrestling": 3
  }
}
```

### Events Calendar

This endpoint accepts the same parameters as the ones described in [Search Events](https://docs.predicthq.com/resources/events#search-events) and can be used to get a calendar view of all matching events that are available to your account.

Each day in the calendar contains aggregate counts of all _active_ events for that day.

A JSON Schema is available for the Events Calendar endpoint: [events-calendar-schema.json](https://docs.predicthq.com/docs/schema/events-calendar-schema.json)

#### Action

[RAW](https://docs.predicthq.com/resources/events)

```bash
GET /v1/events/calendar/
```

#### Example

[CURL](https://docs.predicthq.com/resources/events)[PYTHON](https://docs.predicthq.com/resources/events)[RAW](https://docs.predicthq.com/resources/events)

```bash
curl -X GET https://api.predicthq.com/v1/events/calendar/?active.gte=2015-12-24&active.lte=2015-12-25&active.tz=Pacific/Auckland&country=NZ \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```

[JSON](https://docs.predicthq.com/resources/events)

```json
{
  "count": 63,
  "next": null,
  "previous": null,
  "results": [
    {
      "date": "2015-12-24",
      "count": 38,
      "top_rank": 90,
      "top_local_rank": 49,
      "top_aviation_rank": 83,
      "rank_levels": {
        "1": 13,
        "2": 16,
        "3": 8,
        "4": 0,
        "5": 1
      },
      "local_rank_levels": {
        "1": 0,
        "2": 21,
        "3": 12,
        "4": 0,
        "5": 0
      },
      "aviation_rank_levels": {
        "1": 3,
        "2": 2,
        "3": 4,
        "4": 1,
        "5": 0
      },
      "categories": {
        "concerts": 13,
        "festivals": 11,
        "airport-delays": 6,
        "sports": 4,
        "politics": 1,
        "school-holidays": 1,
        "observances": 1,
        "daylight-savings": 1,
        "performing-arts": 1
      },
      "labels": {
        "concert": 13,
        "music": 13,
        "festival": 11,
        "airport": 6,
        "delay": 6,
        "sport": 4,
        "holiday": 2,
        "outdoor": 2,
        "daylight-savings": 1,
        "family": 1,
        "election": 1,
        "movie": 1,
        "observance": 1,
        "performing-arts": 1,
        "school": 1
      }
    },
    {
      "date": "2015-12-25",
      "count": 22,
      "top_rank": 90,
      "top_local_rank": 63,
      "top_aviation_rank": 81,
      "rank_levels": {
        "1": 9,
        "2": 10,
        "3": 1,
        "4": 1,
        "5": 1
      },
      "local_rank_levels": {
        "1": 0,
        "2": 8,
        "3": 6,
        "4": 1,
        "5": 0
      },
      "aviation_rank_levels": {
        "1": 5,
        "2": 6,
        "3": 2,
        "4": 2,
        "5": 0
      },
      "categories": {
        "festivals": 10,
        "sports": 5,
        "concerts": 3,
        "school-holidays": 1,
        "public-holidays": 1,
        "daylight-savings": 1,
        "conferences": 1
      },
      "labels": {
        "festival": 10,
        "sport": 5,
        "concert": 3,
        "music": 3,
        "holiday": 2,
        "outdoor": 2,
        "conference": 1,
        "daylight-savings": 1,
        "education": 1,
        "holiday-national": 1,
        "religion": 1,
        "school": 1
      }
    }
  ]
}
```

### Aggregate Event Impact

Aggregate Event Impact has been replaced by the [Features API](https://docs.predicthq.com/resources/features)

The Aggregate Event Impact API has been deprecated. It has been replaced by the Features API. We will cease support for Aggregate Event Impact in future.

Please [contact us](https://www.predicthq.com/contact) if you require assistance with event attendance aggregations.

Features API

Please see [Features API](https://docs.predicthq.com/resources/features) for more information.
