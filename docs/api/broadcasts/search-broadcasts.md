---
description: Search for Live TV broadcasts happening in a location.
---

# Search Broadcasts

{% hint style="info" %}
**Results are limited by your subscription**

Please note that you will not receive an error when requesting a date range or location that is outside of your subscription settings.

This is sometimes confused with missing data. If you're not seeing the results you expect to see then please ensure your subscription covers the location or time period you're searching for.

Your subscription settings can be viewed in the [WebApp](https://control.predicthq.com/settings/plans).
{% endhint %}

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/broadcasts/
```

### Query Parameters

<table><thead><tr><th width="234">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>broadcast_id</code></td><td><p>Find broadcasts by unique identifier. Multiple values are accepted as a comma-separated list.</p><p><br>E.g. <code>?broadcast_id=tFk2LbcpzgeuLXw8dKWa3J</code></p></td></tr><tr><td><code>broadcast_status</code></td><td><p>Find broadcasts by broadcast status. Multiple values are accepted as a comma-separated list.</p><p><br><strong>Possible values:</strong></p><ul><li><code>scheduled</code></li><li><code>predicted</code></li><li><code>cancelled</code></li></ul><p>E.g. <code>?broadcast_status=scheduled</code></p></td></tr><tr><td><code>event.category</code></td><td><p>Find broadcasts by their physical event’s category.</p><p><br><strong>Possible values:</strong></p><ul><li><code>sports</code></li></ul><p>E.g. <code>?event.category=sports</code></p></td></tr><tr><td><code>event.event_id</code></td><td><p>Find broadcasts by their physical event’s unique identifier. Multiple values are accepted as a comma-separated list.<br>Events in the Broadcasts API have the same identifiers as those in the <a href="../events/search-events.md">Events API</a><br></p><p>E.g. <code>?event.event_id=svbfg9xT4YSVUeeAKp</code></p></td></tr><tr><td><code>event.entity_id</code></td><td><p>Find broadcasts by their entity's unique identifier. Multiple values are accepted as a comma-separated list.<br>Entities in the Broadcasts API have the same identifiers as those in the <a href="../events/search-events.md">Events API</a>.<br></p><p>This parameter can be used to filter broadcasts by team, e.g. <code>?event.entity_id=GduZL2z24phJQni4ktERGw</code> to retrieve the Los Angeles Lakers broadcasts, or by venue, e.g. <code>?event.entity_id=qSpch2mYLDa4iygkMdMPYu</code> to retrieve the broadcasts related to a physical game happening at the STAPLES center.<br></p><p>E.g. <code>?event.entity_id=GduZL2z24phJQni4ktERGw</code></p></td></tr><tr><td><code>event.label</code></td><td><p>Find broadcasts by their physical event’s labels. Multiple values are accepted as a comma-separated list.<br></p><p>Where multiple labels are provided, broadcasts which match any of the labels are returned.<br></p><p>Please note that all event labels are lowercase and that the search is case sensitive.<br></p><p>E.g. <code>?event.label=nfl,nba</code></p></td></tr><tr><td><code>first_seen</code></td><td><p>Find broadcasts by the time they were seen for the first time.<br>Supported suffixes are:</p><ul><li><code>gt</code>: greater than.</li><li><code>gte</code>: greater than or equal to.</li><li><code>lt</code>: less than.</li><li><code>lte</code>: less than or equal to.</li><li><code>tz</code>: time zone of the <code>first_seen</code> times uses a <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> name. Default is <code>UTC</code>.</li></ul><p>The format of <code>first_seen</code> times for this parameter is <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br></p><p>E.g. <code>?first_seen.gte=2020-11-30</code></p></td></tr><tr><td><code>limit</code></td><td><p>The maximum number of results to return per page.<br>The default limit is <code>10</code>. The maximum limit is <code>500</code>.</p><p><br>E.g. <code>?limit=50</code></p></td></tr><tr><td><code>location.place_id</code></td><td><p>Find broadcasts by their location's <code>place_id</code>. Multiple values are accepted as a comma-separated list.</p><p><br>Places in the Broadcasts API have the same identifiers as those in the <a href="../places/search-places.md">Places API</a>.</p><p><br>All broadcast location places are counties, but this parameter accepts other types of places in the hierarchy. See <a href="../places/search-places.md">Places</a> for different place types.</p><ul><li>If the <code>place_id</code> of a county is specified, broadcasts in that county will be returned.</li><li>If the <code>place_id</code> of a state (region) is specified, broadcasts in all the counties within that state will be returned. US states have the place type region.E.g. If you specify <code>location.place_id=5332921</code> (California), results will contain broadcasts for all counties in California.</li><li>For places below the county level, broadcasts in the county that the place belongs to will be returned. E.g. If you specify <code>location.place_id=5327684</code> (Berkeley), results will contain broadcasts for Alameda County; Berkeley is located within Alameda County. Some places below county level do not belong to a county, in this case, you can try using the <code>location.origin</code> param.</li></ul><p>A <a href="search-broadcasts.md#mapping-file">CSV file of broadcast counties</a> is available. It contains the <code>place_id</code> and name of all counties and states in the US.</p><p>E.g. <code>?location.place_id=5391997,5128594,5379524,5129915</code></p></td></tr><tr><td><code>location.origin</code></td><td><p>Find broadcasts in the county for the provided geopoint (a latitude and longitude coordinate). The format of the geopoint is <code>{latitude},{longitude}</code>.</p><p><br>The Broadcasts API returns broadcasts at the county level. When you specify a geopoint using <code>location.origin</code> the API returns broadcasts for the county the specified geopoint is within.</p><p><br>If you specify a geopoint within Los Angeles County then broadcasts for Los Angeles County will be returned.</p><p><br>E.g. <code>?location.origin=40.730610,-73.935242</code></p></td></tr><tr><td><code>offset</code></td><td><p>The number of results to skip.</p><p><br>The default is <code>0</code>.</p><p><br>E.g. <code>?offset=10</code></p></td></tr><tr><td><code>phq_viewership.*</code></td><td><p>Find broadcasts by their PHQ Viewership number.</p><p><br>Supported suffixes are:</p><ul><li><code>gt</code>: greater than.</li><li><code>gte</code>: greater than or equal to.</li><li><code>lt</code>: less than.</li><li><code>lte</code>: less than or equal to.</li></ul><p>E.g. <code>?phq_viewership.gte=1000&#x26;phq_viewership.lte=500000</code></p></td></tr><tr><td><code>record_status</code></td><td><p>Find broadcasts by their record status. Multiple values are accepted as a comma-separated list.</p><p><br><strong>Possible values:</strong></p><ul><li><code>active</code>: the broadcast record is valid.</li><li><code>duplicate</code>: the broadcast record is a duplicate of an active record.</li><li><code>deleted</code>: the broadcast record is no longer valid.</li></ul><p>The default is <code>active</code>.</p><p><br>E.g. <code>?record_status=deleted</code></p></td></tr><tr><td><code>sort</code></td><td><p>Fields to order the results by. Multiple values are accepted as a comma-separated list.</p><p><br>The default is <code>start</code>, which means the broadcasts with the earliest start dates are listed first.</p><p><br><strong>Possible values:</strong>*</p><ul><li><code>start</code>: <code>dates.start</code> ascending.</li><li><code>-start</code>: <code>dates.start</code> descending.</li><li><code>phq_viewership</code>: <code>phq_viewership</code> ascending.</li><li><code>-phq_viewership</code>: <code>phq_viewership</code> descending.</li><li><code>updated</code>: <code>updated</code> ascending.</li><li><code>-updated</code>: <code>updated</code> descending.</li><li><code>first_seen</code>: <code>first_seen</code> ascending.</li><li><code>-first_seen</code>: <code>first_seen</code> descending.</li></ul><p>E.g. <code>?sort=start,-updated</code></p></td></tr><tr><td><code>start.*</code></td><td><p>Find broadcasts by their start time.</p><p><br>Supported suffixes are:</p><ul><li><code>gt</code>: greater than.</li><li><code>gte</code>: greater than or equal to.</li><li><code>lt</code>: less than.</li><li><code>lte</code>: less than or equal to.</li><li><code>tz</code>: time zone of the updated times used; a <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> name. Default is <code>UTC</code>.</li></ul><p>The format of start times for this parameter is <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br></p><p>E.g. <code>?start.gte=2020-11-01T05:30:00&#x26;start.tz=America/Los_Angeles</code></p></td></tr><tr><td><code>updated</code></td><td><p>Find broadcasts by the time they were last updated.<br>Supported suffixes are:</p><ul><li><code>gt</code>: greater than.</li><li><code>gte</code>: greater than or equal to.</li><li><code>lt</code>: less than.</li><li><code>lte</code>: less than or equal to.</li><li><code>tz</code>: time zone of the updated times used; a <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> name. Default is <code>UTC</code>.</li></ul><p>E.g. <code>?updated.gte=2020-11-30</code></p></td></tr></tbody></table>

#### Mapping File

Below is a CSV of broadcast counties. It contains the `place_id` and name of all counties and states in the US.

{% file src="../.gitbook/assets/broadcast-events-place-mapping.csv" %}

## Response

### Response Fields

Below are the fields returned by the Broadcasts endpoint.

<table><thead><tr><th width="251">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>broadcast_id</code><br>string</td><td><p>The unique identifier.</p><p><br>E.g. <code>u5aCvebffuNFpGSGNQFiU4</code></p></td></tr><tr><td><code>broadcast_status</code><br>string</td><td><p>The schedule status of the broadcast.</p><p><br><strong>Possible values:</strong></p><ul><li><code>scheduled</code>: the broadcast is scheduled to be televised.</li><li><code>predicted</code>: the broadcast is predicted to be televised.</li><li><code>cancelled</code>: the broadcast is no longer scheduled to be televised.</li></ul><p>Our guide on <a href="../../getting-started/guides/live-tv-event-guides/find-broadcasts-for-specific-sport-types.md">different sport types</a> in the API explains when the <code>scheduled</code> and <code>predicted</code> statuses are used.</p><p><br>E.g. <code>scheduled</code></p></td></tr><tr><td><code>dates</code><br>object</td><td>The <code>dates</code> field contains details about the time of the broadcast. Fields in the <code>dates</code> object are described below.</td></tr><tr><td><code>dates.start</code><br>string</td><td><p>The time the broadcast is scheduled to start, in UTC. In <code>YYYY-MM-DDThh:mm:ssZ</code> format.</p><p><br>E.g. <code>2018-01-01T17:00:00Z</code></p></td></tr><tr><td><code>dates.start_local</code><br>string</td><td><p>The time the broadcast is scheduled to start in the time zone of the broadcast’s location. In <code>YYYY-MM-DDThh:mm:ss</code> format.</p><p><br>E.g. <code>2018-01-01T12:00:00</code></p></td></tr><tr><td><code>dates.timezone</code><br>string</td><td><p>The time zone of the broadcast’s location. In <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> name format.</p><p><br>E.g. <code>America/New_York</code></p></td></tr><tr><td><code>duplicate_of_id</code><br>string</td><td><p>The active record unique identifier the current broadcast is a duplicate of. Please note that this field is only present for records with record status <code>duplicate</code>.</p><p><br>E.g. <code>u5aCvebffuNFpGSGNQFiU4</code></p></td></tr><tr><td><code>event</code><br>object</td><td>The <code>event</code> field contains details about the physical event that is being televised in the broadcast. Fields in the <code>event</code> object are described below.</td></tr><tr><td><code>event.aviation_rank</code><br>number</td><td><p>The <a href="../../getting-started/predicthq-data/ranks/aviation-rank.md">Aviation Rank</a> number of the physical event. Aviation Rank represents the physical event’s impact on flight bookings by considering both domestic and international travel.</p><p><br>E.g. <code>100</code></p></td></tr><tr><td><code>event.category</code><br>string</td><td><p>The category of the physical event.</p><p><br>E.g. <code>sports</code></p></td></tr><tr><td><code>event.dates</code><br>object</td><td><p>Details about the time of the physical event.</p><p><br>Fields:</p><ul><li><code>start</code>: the start time of the physical event.</li><li><code>start_local</code>: the start time in the physical event’s time zone.</li><li><code>end</code>: the end time of the physical event.</li><li><code>end_local</code>: the end time in the physical event’s time zone.</li><li><code>predicted_end_local</code>: the time the physical event is predicted to end in the event's time zone.</li><li><code>timezone</code>: the time zone of the physical event.</li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "start": "2018-01-01T17:00:00Z",
  "end": "2018-01-01T20:43:26Z",
  "start_local": "2018-01-01T12:00:00",
  "end_local": "2018-01-01T15:43:26",
  "predicted_end_local": "2018-01-01T15:20:00",
  "timezone": "America/New_York"
}
</code></pre></td></tr><tr><td><code>event.entities</code><br>array</td><td><p>Venue entities linked to the physical event.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">[
  {
    "entity_id": "wVgG7p8ZKRKEPPrNDq4my9",
    "type": "venue",
    "name": "Hard Rock Stadium",
    "formatted_address": "347 Don Shula Dr\nMiami Gardens, FL 33056\nUnited States of America"
  }
]
</code></pre></td></tr><tr><td><code>event.event_id</code><br>string</td><td><p>The unique identifier of the physical event. Events in the Broadcasts API have the same identifiers as those in the Events API.</p><p><br>E.g. <code>svbfg9xT4YSVUeeAKp</code></p></td></tr><tr><td><code>event.labels</code><br>array</td><td><p>The labels associated with the physical event.</p><p><br>E.g. <code>["american-football", "nfl", "sport"]</code></p></td></tr><tr><td><code>event.local_rank</code><br>number</td><td><p>The Local Rank number of the physical event. Local Rank represents the physical event’s impact on its local geographical location.</p><p><br>E.g. <code>100</code></p></td></tr><tr><td><code>event.location</code><br>object</td><td><p>Details about the location of the physical event.</p><p><br>Fields:</p><ul><li><code>country</code>: the country code.</li><li><code>geopoint</code>: the latitude and longitude coordinates.</li><li><code>place_hierarchies</code>: place hierarchies of the physical event.</li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "geopoint": {
    "lon": -80.23886040000002,
    "lat": 25.9579665
  },
  "place_hierarchies": [
    [
      "6295630",
      "6255149",
      "6252001",
      "4155751",
      "4164238",
      "4161298"
    ]
  ],
  "country": "US"
}
</code></pre></td></tr><tr><td><code>event.phq_attendance</code><br>number</td><td><p>The number of people predicted to attend the physical event.</p><p><br>E.g. <code>65000</code></p></td></tr><tr><td><code>event.phq_rank</code><br>number</td><td><p>The PHQ Rank number of the physical event. PHQ Rank represents the physical event’s impact independent of its geographical location.</p><p><br>E.g. <code>100</code></p></td></tr><tr><td><code>event.title</code><br>string</td><td><p>The title of the physical event.</p><p><br>E.g. <code>Super Bowl - 49ers vs Kansas City Chiefs</code></p></td></tr><tr><td><code>first_seen</code><br>string</td><td><p>The time the broadcast was seen for the first time. In <code>YYYY-MM-DDThh:mm:ssZ</code> format.</p><p><br>E.g. <code>2020-11-30T06:58:28Z</code></p></td></tr><tr><td><code>location</code><br>object</td><td>The <code>location</code> field contains details about where the broadcast is televised. Fields in the <code>location</code> object are described below.</td></tr><tr><td><code>location.country</code><br>string</td><td><p>The country code of the location where the broadcast is televised. In <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> format.</p><p><br>E.g. <code>US</code></p></td></tr><tr><td><code>location.geopoint</code><br>object</td><td><p>The latitude and longitude coordinates of the location where the broadcast is televised.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "lon": -122.4425,
  "lat": 37.77823
}
</code></pre></td></tr><tr><td><code>location.place_hierarchies</code><br>array</td><td><p>An array of place hierarchies for the location where the broadcast is televised. A broadcast record is only televised in one location.</p><p><br>A hierarchy is an array of place ids (see <a href="../places/search-places.md">Places</a>). The final id in a hierarchy is the place_id of the place where the broadcast is televised.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">[
  [
    "6295630",
    "6255149",
    "6252001",
    "5332921",
    "5391997"
  ]
]
</code></pre></td></tr><tr><td><code>location.places</code><br>array</td><td><p>An array of place details for the place where the broadcast is televised. A broadcast record is only televised in one place.<br>A place object has these fields:</p><ul><li><code>place_id</code>: id of the place.</li><li><code>type</code>: the type of the place. Broadcasts are located at counties or county-equivalents.</li><li><code>name</code>: the name of the place.</li><li><code>county</code>: the name of the Place’s county. This is the same as the <code>name</code> if the Place is a county.</li><li><code>region</code>: the name of the Place’s region. In the US, regions represent states or federal districts.</li><li><code>country</code>: the <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> country code of the Place’s country.</li></ul><p><br>A <a href="search-broadcasts.md#mapping-file">CSV file of broadcast counties</a> is available. It contains the <code>place_id</code> and name of all counties and states in the US.</p><p>E.g.</p><pre class="language-json"><code class="lang-json">[
  {
    "place_id": "5391997",
    "type": "county",
    "name": "San Francisco County",
    "county": "City and County of San Francisco",
    "region": "California",
    "country": "US"
  }
]
</code></pre></td></tr><tr><td><code>phq_viewership</code><br>number</td><td><p>The estimated number of people in the broadcast’s location that will watch the broadcast.</p><p><br>E.g. <code>300000</code></p></td></tr><tr><td><code>record_status</code><br>string</td><td><p>The record status of the broadcast.</p><p><br><strong>Possible values:</strong></p><ul><li><code>active</code>: the broadcast record is valid.</li><li><code>duplicate</code>: the broadcast record is a duplicate of an active record.</li><li><code>deleted</code>: the broadcast record is no longer valid.</li></ul><p><br>E.g. <code>active</code></p></td></tr><tr><td><code>updated</code><br>string</td><td><p>The time the broadcast was last updated. In <code>YYYY-MM-DDThh:mm:ssZ</code> format.</p><p><br>E.g. <code>2020-11-30T06:58:28Z</code></p></td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "overflow": false,
    "results": [
        {
            "broadcast_id": "u5aCvebffuNFpGSGNQFiU4",
            "updated": "2020-11-30T06:58:28Z",
            "first_seen": "2020-11-26T01:18:24Z",
            "dates": {
                "start": "2020-02-02T23:30:00Z",
                "start_local": "2020-02-02T15:30:00",
                "timezone": "America/Los_Angeles"
            },
            "location": {
                "geopoint": {
                    "lon": -122.4425,
                    "lat": 37.77823
                },
                "place_hierarchies": [
                    ["6295630","6255149","6252001","5332921","5391997"]
                ],
                "places": [
                    {
                        "place_id": "5391997",
                        "type": "county",
                        "name": "San Francisco County",
                        "county": "City and County of San Francisco",
                        "region": "California",
                        "country": "US"
                    }
                ],
                "country": "US"
            },
            "phq_viewership": 300609,
            "record_status": "active",
            "broadcast_status": "scheduled",
            "event": {
                "event_id": "svbfg9xT4YSVUeeAKp",
                "title": "Super Bowl - 49ers vs Kansas City Chiefs",
                "category": "sports",
                "labels": [
                    "american-football",
                    "nfl",
                    "sport"
                ],
                "dates": {
                    "start": "2020-02-02T23:30:00Z",
                    "end": "2020-02-03T03:11:00Z",
                    "start_local": "2020-02-02T18:30:00",
                    "end_local": "2020-02-02T22:11:00",
                    "predicted_end_local": "2020-02-02T21:25:00",
                    "timezone": "America/New_York"
                },
                "location": {
                    "geopoint": {
                        "lon": -80.23886040000002,
                        "lat": 25.9579665
                    },
                    "place_hierarchies": [
                        ["6295630","6255149","6252001","4155751","4164238","4161298"],
                        ["6295630","6255149","6252001","4155751","4149007","4155966"]
                    ],
                    "country": "US"
                },
                "entities": [
                    {
                        "entity_id": "wVgG7p8ZKRKEPPrNDq4my9",
                        "type": "venue",
                        "name": "Hard Rock Stadium",
                        "formatted_address": "347 Don Shula Dr\nMiami Gardens, FL 33056\nUnited States of America"
                    }
                ],
                "phq_attendance": 65326,
                "phq_rank": 86,
                "local_rank": 100,
                "aviation_rank": 99
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
curl -X GET "https://api.predicthq.com/v1/broadcasts/?broadcast_id=u5aCvebffuNFpGSGNQFiU4" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/broadcasts/",
    headers={
      "Accept": "application/json",
      "Authorization": "Bearer $ACCESS_TOKEN"
    },
    params={
        "broadcast_id": "u5aCvebffuNFpGSGNQFiU4"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [Live TV Event Guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/live-tv-event-guides)
