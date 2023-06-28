---
description: >-
  The calendar endpoint can be useful for indicating the number and impact of
  events happening on particular days making it easy to integrate event
  visibility into your existing calendar.
---

# Get Calendar of Events

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/events/calendar/
```

### Query Parameters

<table><thead><tr><th width="219">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><strong>active.*</strong><br>date range</td><td>The date from and/or to the events intersect with. Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes.<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>.<br>E.g. <code>?active.gte=2015-01-01&#x26;active.lte=2015-03-01</code></td></tr><tr><td><strong>aviation_rank.*</strong><br>rank range</td><td>Supports <code>gt</code>, <code>gte</code>, <code>lt</code> and <code>lte</code> suffixes.<br>Please note that use of a suffix is <strong>required</strong>.<br>Note when filtering on <code>aviation_rank</code> events that do not have an <code>aviation_rank</code> will not be returned.<br>E.g. <code>?aviation_rank.gte=80&#x26;aviation_rank.lte=90</code></td></tr><tr><td><strong>aviation_rank_level</strong><br>number</td><td><p>A comma-separated list of numbers between 1 and 5, corresponding to the PredictHQ Aviation Rank levels.<br><strong>Possible values:</strong></p><ul><li><code>1</code> - Minor (rank between 0 and 20).</li><li><code>2</code> - Moderate (rank between 21 and 40).</li><li><code>3</code> - Important (rank between 41 and 60).</li><li><code>4</code> - Significant (rank between 61 and 80).</li><li><code>5</code> - Major (rank between 81 and 100).</li></ul><p>Note when filtering on <code>aviation_rank_level</code> events that do not have an <code>aviation_rank</code> will not be returned.<br>E.g. <code>?aviation_rank_level=4,5</code></p></td></tr><tr><td><strong>brand_unsafe.*</strong><br>brand-unsafe</td><td><p>Whether or not to <strong>exclude</strong> potentially brand-unsafe events. Potentially brand-unsafe events are included by default.<br>Currently only supports the <code>exclude</code> suffix.</p><ul><li><code>exclude</code>: whether or not to exclude potentially brand-unsafe events from results (<em>required</em>, valid options are <code>true</code> or <code>false</code>)</li></ul><p>Examples of brand-unsafe events include content that promotes hate, violence or discrimination, coarse language, content that is sexually suggestive or explicit, etc.<br>Please note that use of a suffix is <strong>required</strong>.<br>E.g. <code>?brand_unsafe.exclude=true</code></p></td></tr><tr><td><strong>cancelled.*</strong><br>date range</td><td>The date from and/or to the event was set to cancelled in the system. Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes.<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>.<br>Note when filtering on <code>cancelled</code> events that are not cancelled will not be returned.<br>E.g. <code>?cancelled.gte=2020-03-01&#x26;cancelled.lte=2020-03-15</code></td></tr><tr><td><strong>category</strong><br>string</td><td><p>A comma-separated list of categories.<br><strong>Possible values:</strong></p><ul><li><code>academic</code></li><li><code>school-holidays</code></li><li><code>public-holidays</code></li><li><code>observances</code></li><li><code>politics</code></li><li><code>conferences</code></li><li><code>expos</code></li><li><code>concerts</code></li><li><code>festivals</code></li><li><code>performing-arts</code></li><li><code>sports</code></li><li><code>community</code></li><li><code>daylight-savings</code></li><li><code>airport-delays</code></li><li><code>severe-weather</code></li><li><code>disasters</code></li><li><code>terror</code></li><li><code>health-warnings</code></li></ul><p>E.g. <code>?category=school-holidays,public-holidays</code><br>Take a look at the <a href="https://www.predicthq.com/intelligence/data-enrichment/event-categories"><code>Event Categories</code></a> page for an overview of the different categories.</p></td></tr><tr><td><strong>country</strong><br>string</td><td>A comma-separated list of country codes.<br>E.g. <code>?country=AU,NZ</code></td></tr><tr><td><strong>deleted_reason</strong><br>string</td><td><p>A comma-separated list of deleted reasons for the events.<br><strong>Possible values:</strong></p><ul><li><code>cancelled</code></li><li><code>invalid</code></li><li><code>duplicate</code></li><li><code>postponed</code></li></ul><p>E.g. <code>?deleted_reason=cancelled,duplicate</code></p></td></tr><tr><td><strong>end.*</strong><br>date range</td><td>The date from and/or to the event ends. Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes.<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>.<br>E.g. <code>?end.gte=2018-12-19&#x26;end.lte=2018-12-19</code></td></tr><tr><td><strong>end_around.*</strong><br>date around</td><td><p>Fuzzy date search around event end. Supports <code>origin</code>, <code>offset</code>, <code>scale</code>, <code>decay</code> suffixes.</p><ul><li><code>origin</code>: The date (<em>required</em>)</li><li><code>offset</code>: The number of days from the origin before the score starts to decay (<em>optional</em>, defaults to <code>0d</code>)</li><li><code>scale</code>: Distance from origin +/- offset at which the score will equal the decay value (<em>optional</em>, defaults to <code>3d</code>)</li><li><code>decay</code>: Score value at the <code>scale</code> distance (<em>optional</em>, defaults to <code>0.5</code>)</li></ul><p>Can influence <a href="https://docs.predicthq.com/resources/events#param-relevance"><code>relevance</code></a>.<br>E.g. <code>?end_around.origin=2018-12-19</code></p></td></tr><tr><td><strong>entity.id</strong><br>string</td><td>A comma-separated list of entity identifiers.<br>E.g. <code>?entity.id=XABWvihQAj8TnjvF6WNzLW</code></td></tr><tr><td><strong>first_seen</strong><br>date range</td><td><p>Find events by the time they were seen for the first time.<br>Supported suffixes are:</p><ul><li><code>gt</code>: greater than.</li><li><code>gte</code>: greater than or equal to.</li><li><code>lt</code>: less than.</li><li><code>lte</code>: less than or equal to.</li><li><code>tz</code>: time zone of the first_seen times used;</li></ul><p>a <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> name.Default is <code>UTC</code>.<br>The format of first_seen times for this parameter is <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br>E.g. <code>?first_seen.gte=2020-11-30</code></p></td></tr><tr><td><strong>id</strong><br>string</td><td>A comma-separated list of event identifiers.<br>E.g. <code>?id=z13B3870YOgv</code></td></tr><tr><td><strong>label</strong><br>string</td><td>A comma-separated list of labels. Use the <a href="https://docs.predicthq.com/resources/events#retrieve-events-count">count endpoint</a> to fetch a list of available labels.<br>Please note that all event labels are lowercase and that the search is case sensitive.<br>E.g. <code>?label=holiday,observance</code></td></tr><tr><td><strong>limit</strong><br>number</td><td>The maximum number of results to return. The default limit is <code>10</code>.<br>E.g. <code>?limit=10</code></td></tr><tr><td><strong>local_rank.*</strong><br>rank range</td><td>Supports <code>gt</code>, <code>gte</code>, <code>lt</code> and <code>lte</code> suffixes.<br>Please note that use of a suffix is <strong>required</strong>.<br>Note when filtering on <code>local_rank</code> events that do not have a <code>local_rank</code> will not be returned.<br>E.g. <code>?local_rank.gte=80&#x26;local_rank.lte=90</code></td></tr><tr><td><strong>local_rank_level</strong><br>number</td><td><p>A comma-separated list of numbers between 1 and 5, corresponding to the PredictHQ local rank levels.<br><strong>Possible values:</strong></p><ul><li><code>1</code> - Minor (rank between 0 and 20).</li><li><code>2</code> - Moderate (rank between 21 and 40).</li><li><code>3</code> - Important (rank between 41 and 60).</li><li><code>4</code> - Significant (rank between 61 and 80).</li><li><code>5</code> - Major (rank between 81 and 100).</li></ul><p>Note when filtering on <code>local_rank_level</code> events that do not have a <code>local_rank</code> will not be returned.<br>E.g. <code>?local_rank_level=4,5</code></p></td></tr><tr><td><strong>location_around.*</strong><br>location around</td><td><p>Fuzzy location search around event location.<br>Please note this affects the <a href="https://docs.predicthq.com/resources/events#param-relevance"><code>relevance</code></a> value and does not restrict search results to the specified latitude/longitude and offset. Read more in the <a href="https://docs.predicthq.com/guides/relevance">Relevance guide</a> and combine with the <a href="https://docs.predicthq.com/resources/events#param-within"><code>within</code></a> parameter to restrict results to a specified latitude/longitude and radius.<br>Supports <code>origin</code>, <code>offset</code>, <code>scale</code>, <code>decay</code> suffixes.</p><ul><li><code>origin</code>: The location in the form <code>{latitude},{longitude}</code> (<em>required</em>)</li><li><code>offset</code>: The distance before decay is applied (<em>optional</em>, defaults to <code>0km</code>)(Distance unit can be one of <code>m</code>, <code>km</code>, <code>ft</code>, <code>mi</code>)</li><li><code>scale</code>: Distance from origin + offset at which the score will equal decay value (<em>optional</em>, defaults to <code>2km</code>) (Distance unit can be one of <code>m</code>, <code>km</code>, <code>ft</code>, <code>mi</code>)</li><li><code>scale</code>: Distance from origin + offset at which the score will equal decay value (<em>optional</em>, defaults to <code>2km</code>) (Distance unit can be one of <code>m</code>, <code>km</code>, <code>ft</code>, <code>mi</code>)</li><li><code>decay</code>: Score value at <code>scale</code> value (<em>optional</em>, defaults to <code>0.5</code>)</li></ul><p>E.g. <code>?location_around.origin=40.730610,-73.935242</code></p></td></tr><tr><td><strong>offset</strong><br>number</td><td>The number of results to skip. The default is <code>0</code>.<br>E.g. <code>?offset=20</code></td></tr><tr><td><strong>parent.*</strong></td><td><p>Whether or not to include parent events / exclude child events.<br><br>Note that<br><strong>Child</strong> events are those events that have a link to a parent event.<br><strong>Parent</strong> events are all the other events, whether they have children or not.<br>See the documentation on <a href="https://docs.predicthq.com/guides/multi-day-and-umbrella-events/">umbrella events</a> for more information on parent and child events.<br><br>Currently supports the <code>include</code> suffix.<br><br><code>include</code>: Whether or not to include parent events in the response (<em>required</em>, valid options are <code>true</code>, <code>false</code> or <code>only</code>)</p><ul><li><code>true</code>: include parent events (default behaviour)</li><li><code>false</code>: exclude parent events - this will return child events only</li><li><code>only</code>: only fetch parent events (exclude child events)</li></ul><p>Default value: <code>true</code>.<br><br>Please note that use of a suffix is <strong>required</strong>.<br><br>E.g. <code>?parent.include=false</code></p></td></tr><tr><td><strong>phq_attendance.*</strong><br>number range</td><td>Supports <code>gt</code>, <code>gte</code>, <code>lt</code> and <code>lte</code> suffixes.<br>Please note that use of a suffix is <strong>required</strong>.<br>E.g. <code>?phq_attendance.gte=2000&#x26;phq_attendance.lte=10000</code></td></tr><tr><td><strong>place.*</strong><br>place</td><td><p>A comma-separated list of place ids (see <a href="https://docs.predicthq.com/resources/places">Places</a>) and/or IATA (3 character), ICAO (4 character), and UN/LOCODE (5 character) airport codes where the events occur. Supports <code>scope</code> or <code>exact</code> suffixes. A <a href="https://docs.predicthq.com/docs/csv/airport-codes.csv">CSV file</a> of all supported airport codes and their respective place ids is available to download.<br>When <code>place.scope</code> is used, results will contain events that apply to the parent and children places of the specified place. E.g. National, regional and local school holidays that apply to a region.<br><br>When <code>place.exact</code> is used, results will contain events that apply to the specified place only.E.g. Regional school holidays only.<br><br>Please note that use of a suffix is <strong>required</strong>.<br>E.g.</p><ul><li>all events that apply to the State of New York: <code>?place.scope=5128638</code></li><li>all events that apply to the place associated with San Francisco Airport: <code>?place.scope=SFO</code></li></ul></td></tr><tr><td><strong>placekey</strong><br>string</td><td><p>A comma-separated list of Placekeys (See <a href="https://www.placekey.io/">placekey.io</a>). Returns events that have a Placekey value matching this filter.<br>There are 2 parts to a Placekey: <code>what@where</code><br></p><ul><li><p><code>What:</code>Contains 2 part in the form <code>{address}-{POI}</code>.</p><ul><li>The first part represents an address.</li><li>The second part represents a Point Of Interest (E.g. named venue). This will be missing on locations that only have addresses</li></ul></li><li><code>Where:</code> An H3 hexagon index(resolution 10) of the event.</li></ul><p>This filter supports entering a full Placekey to match events having that specific Placekey or a partial Placekey (such as just the <code>@where</code> part) to perform a partial match on Placekey. You can use the following Placekey format in this filter:</p><ul><li><code>{address}-{poi}@{where}</code> - only returns events with a full matching placekey (an exact match)</li><li><code>{address}@{where}</code> - matches events where the the address and where part match (even if poi is different)</li><li><code>@{where}</code> - matches events for which the @Where part matches, ignores the {address}-{poi} parts. You can perform a partial match on the @Where part to find nearby events. The minimum amount of characters that can be matched on is 5. See <a href="https://docs.predicthq.com/guides/using-placekey-with-poi-data">using Placekey</a> for more details.</li></ul><p>Note that Placekey applies to our attended event categories. Some events do not contain a Placekey.<br><br>E.g.<code>?placekey=225@63j-rqb-j7q,@627-s8j-z2k</code></p></td></tr><tr><td><strong>postponed.*</strong><br>date range</td><td>The date from and/or to the event was set to postponed in the system. Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes.<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>.<br>Note when filtering on <code>postponed</code> events that are not postponed will not be returned.<br>E.g. <code>?postponed.gte=2020-03-01&#x26;postponed.lte=2020-03-15</code></td></tr><tr><td><strong>predicted_end.*</strong><br>date range</td><td>The date from and/or to the event predicted_end. Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes.<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>.<br>Note when filtering on <code>predicted_end</code> events that do not have a <code>predicted_end</code> will not be returned.<br>E.g. <code>?predicted_end.gte=2018-12-19&#x26;predicted_end.lte=2018-12-19</code></td></tr><tr><td><strong>q</strong><br>string</td><td>A full-text search query.<br>Can influence <a href="https://docs.predicthq.com/resources/events#param-relevance"><code>relevance</code></a>.<br>E.g. <code>?q=katy+perry</code></td></tr><tr><td><strong>rank.*</strong><br>rank range</td><td>Supports <code>gt</code>, <code>gte</code>, <code>lt</code> and <code>lte</code> suffixes.<br>Please note that use of a suffix is <strong>required</strong>.<br>E.g. <code>?rank.gte=80&#x26;rank.lte=90</code></td></tr><tr><td><strong>rank_level</strong><br>number</td><td><p>A comma-separated list of numbers between 1 and 5, corresponding to the PredictHQ rank levels.<br><strong>Possible values:</strong></p><ul><li><code>1</code> - Minor (rank between 0 and 20).</li><li><code>2</code> - Moderate (rank between 21 and 40).</li><li><code>3</code> - Important (rank between 41 and 60).</li><li><code>4</code> - Significant (rank between 61 and 80).</li><li><code>5</code> - Major (rank between 81 and 100).</li></ul><p>E.g. <code>?rank_level=4,5</code></p></td></tr><tr><td><strong>relevance</strong><br>string</td><td><p>A comma-separated list of components to include when calculating the <code>relevance</code> field of an event.The relevance components are multiplied together to produce the overall relevance.<br><strong>Parameter Components:</strong><br>These components correspond to search parameters that can influence relevance. If the parameter isn't provided as part of a search its component will be ignored.By default, <code>relevance</code> includes the components of each relevance-influencing parameter in a search.</p><ul><li><code>q</code></li><li><code>start_around</code></li><li><code>end_around</code></li><li><code>location_around</code></li></ul><p><strong>Field Components:</strong><br>These components correspond to event fields that can be included in relevance. They are not included in <code>relevance</code> by default.</p><ul><li><code>rank</code></li><li><code>local_rank</code></li><li><code>aviation_rank</code></li></ul><p><br>E.g. <code>?relevance=q,rank,location_around</code></p></td></tr><tr><td><strong>saved_location.location_id</strong><br>string</td><td>A comma-separated list of saved location identifiers. Up to a maximum of 20 identifiers. This filters the events returned to events within the locations specified. See the <a href="https://docs.predicthq.com/resources/saved-locations">Saved Locations API</a> for more details on getting location IDs for a location.<br>E.g. <code>?saved_location.location_id=sFlb8HlsLa1j-S4UDEMEkQ</code></td></tr><tr><td><strong>sort</strong><br>string</td><td><p>A comma-separated list of fields to sort results by. The default is <code>relevance,-start</code>.<br>Prefix the field name with <code>-</code> for reverse order.<br><strong>Possible values:</strong></p><ul><li><code>id</code></li><li><code>title</code></li><li><code>start</code></li><li><code>end</code></li><li><code>first_seen</code></li><li><code>predicted_end</code></li><li><code>updated</code></li><li><code>rank</code></li><li><code>local_rank</code></li><li><code>aviation_rank</code></li><li><code>phq_attendance</code></li><li><code>category</code></li><li><code>duration</code></li><li><code>country</code></li><li><code>labels</code></li><li><code>relevance</code></li></ul><p>Note when sorting on <code>predicted_end</code>, <code>local_rank</code> or <code>aviation_rank</code> (regardless of sort order), events that do not have a <code>predicted_end</code>, <code>local_rank</code> or <code>aviation_rank</code> will be placed last.<br>When sorting by <code>relevance</code> the most relevant results are sorted first, regardless of sort order.<br>E.g. <code>?sort=country,-start</code></p></td></tr><tr><td><strong>start.*</strong><br>date range</td><td>The date from and/or to the event starts. Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes.<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>.<br>E.g. <code>?start.gte=2018-12-19&#x26;start.lte=2018-12-19</code></td></tr><tr><td><strong>start_around.*</strong><br>date around</td><td><p>Fuzzy date search around event start. Supports <code>origin</code>, <code>offset</code>, <code>scale</code>, <code>decay</code> suffixes.</p><ul><li><code>origin</code>: The date (<em>required</em>)</li><li><code>offset</code>: The number of days from the origin before the score starts to decay (<em>optional</em>, defaults to <code>0d</code>)</li><li><code>scale</code>: Distance from origin +/- offset at which the score will equal the decay value (<em>optional</em>, defaults to <code>3d</code>)</li><li><code>decay</code>: Score value at the <code>scale</code> distance (<em>optional</em>, defaults to <code>0.5</code>)</li></ul><p>Can influence <a href="https://docs.predicthq.com/resources/events#param-relevance"><code>relevance</code></a>.<br>E.g. <code>?start_around.origin=2018-12-19</code></p></td></tr><tr><td><strong>state</strong><br>string</td><td>A comma-separated list of states for the events. Supports <code>active</code>, <code>deleted</code> and <code>predicted</code>. By default, returns <code>active</code> events only.<br><br>This parameter is useful in conjunction with <code>updated</code> when you cache events and are interested in retrieving a list of all events that have changed since a specific date and time.<br><br>E.g. <code>?state=active,deleted</code></td></tr><tr><td><strong>updated.*</strong><br>date range</td><td>The date from and/or to the event was last modified. Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes.<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>.<br><br>E.g. <code>?updated.gte=2018-05-01T09:55:00Z</code></td></tr><tr><td><strong>within</strong><br>area</td><td>A geo center and radius in the form <code>{radius}{unit}@{latitude},{longitude}</code>, where the radius unit can be one of: meters <code>m</code>, kilometers <code>km</code>, feet <code>ft</code>, miles <code>mi</code>. When using the units of <code>km</code> and <code>mi</code> you can enter whole numbers or floats <code>e.g. 5mi, 1.5km or 1.2mi</code>. When using the units <code>ft</code> or <code>m</code> you need to enter whole numbers (you cannot enter a fraction of a meter or foot).<br><br>Note that results may contain events that apply to a parent scope of the specified area.<br><br>Note that it can be difficult working out a suitable radius around your location so to make it easier please use our <a href="https://docs.predicthq.com/resources/suggested-radius">Suggested Radius API</a>.<br><br>E.g. National school holidays that apply to the local radius.<br>E.g. <code>?within=2.5mi@-36.844480,174.768368</code> or <code>?within=2750m@-36.844480,174.768368</code></td></tr></tbody></table>

## Response

<details>

<summary>Example response</summary>

Each day in the calendar contains aggregate counts of all _active_ events for that day.

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

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/events/calendar/?active.gte=2015-12-24&active.lte=2015-12-25&active.tz=Pacific/Auckland&country=NZ \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/calendar/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "country": "NZ",
        "active.gte": "2015-12-24",
        "active.lte": "2015-12-25",
        "active.tz": "Pacific/Auckland"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
