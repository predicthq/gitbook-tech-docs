---
description: Search events submitted by your organization.
---

# Search Submitted Events

For example, you can use this to display a list of events submitted via Loop Links within your application to your users. See also the [Events API documentation](../../events/search-events.md#query-parameters) for more detail on many of the parameters mentioned below.

## Request

```http
GET https://api.predicthq.com/v1/loop/events
```

{% tabs %}
{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/loop/events",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "phq_review": "approved"
    }
)

print(response.json())
```
{% endtab %}

{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/loop/events?phq_review=approved \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}
{% endtabs %}

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
  "count": 1,
  "events": [
    {
      "event_id": "tae8Mie8keiceicoMae2ie",
      "link_id": "ber7ntO0ZHuFVCfrSNsN",
      "create_dt": "2023-02-16T00:52:11.112355+00:00",
      "update_dt": "2023-05-09T02:05:51.695054Z",
      "version": 1,
      "phq_review": "approved",
      "org_review": "pending",
      "phq_auto_approved": false,
      "event": {
        "title": "Hotel A event",
        "description": "The 2023 edition of Hotel A festival.",
        "category": "festivals",
        "state": "active",
        "metadata": [
          {
            "maximum_attendance": 5000
          },
          {
            "attendance": 3215
          }
        ],
        "dates": {
          "fixed_date": {
            "start_date": "2023-06-02",
            "end_date": "2023-06-04"
          }
        },
        "labels": [
          "festival",
          "food",
          "music"
        ],
        "lat": "38.901544",
        "lon": "-119.7030036",
        "address": "859 U.S. Highway 395 North",
        "formatted_address": "859 U.S. Highway 395 North\nGardnerville, Nevada 89410\nUnited States of America",
        "city": "Gardnerville",
        "region": "Nevada",
        "postcode": "89410",
        "country": "US",
        "geometry": {
          "type": "Point",
          "coordinates": [
            -119.703022,
            38.9012446
          ]
        }
      }
    }
  ]
}
```

</details>

### Query Parameters

#### `q` (string, optional) <a href="#q" id="q"></a>

Full-text search of event information. E.g. `?q=hotel+a`

***

#### `link_id` _(_string, optional) Comma-separated list of link ids. Allows you to filter for events submitted via a specific Loop Link ID. E.g. `?link_id=m4Dk4g4DRA8Yqbp2PC54`

***

**`event_id`** _string_\
Comma-separated list of event IDs. Allows you to retrieve specific events. E.g. `?event_id=5uRg7CqGu7DTtu4Rfk`

***

**`user_id`** _string_\
Comma-separated list of user IDs that submitted the event. E.g. `?user_id=hw8Dsmv4Djg`

***

**`state`** _string_\
Comma separated list of event states. Possible values:&#x20;

* `active`
* `predicted`
* `cancelled`
* `postponed`
* `archived`

***

**`category`** _string_\
Comma separated list of event categories. E.g. `?category=expos,festivals`

***

**`label`** _string_\
Comma separated list of event labels. E.g. `?label=community,food,music`

***

**`country`** _string_\
Comma separated list of country codes. E.g. `?country=NZ,US`

***

**`start.*`** _string_\
The date from and/or to the event starts. Must be used with suffixes `lt`, `lte`, `gt` or `gte`.\
E.g. `?start.gt=2023-03-04&start.lte=2023-05-01`

***

**`end.*`** _string_\
The date from and/or to the event ends. Must be used with suffixes `lt`, `lte`, `gt` or `gte`\
E.g. `?end.gt=2023-03-04&end.lte=2023-05-01`

***

**`active.*`** _string_\
The date from and/or to the event is active. Must be used with suffixes `lt`, `lte`, `gt` or `gte`.\
E.g. `?active.gt=2023-03-04&active.lte=2023-05-01`

***

**`created.*`** _string_\
The date from and/or to the event has been created. Must be used with suffixes `lt`, `lte`, `gt` or `gte`.\
E.g. `?created.gt=2023-03-04&created.lte=2023-05-01`

***

**`updated.*`** _string_

The date from and/or to the event was last updated. Must be used with suffixes `lt`, `lte`, `gt` or `gte`.\
E.g. `?updated.gt=2023-03-04&updated.lte=2023-05-01`

***

**`private.include`** _string_\
Whether or not to include private events. Rejected & pending events will always be private. Possible values:

* `true`: private and public events
* `false` (default): only public events
* `only`: only private events

E.g `?private.include=only`

***

**`org_review`** _string_\
Filter for submitted events approved, rejected or yet to be reviewed by the your Org. Possible values: `pending`, `approved`, `rejected`. E.g `?org_review=approved`

***

**`phq_review`** _string_\
Filter for submitted events approved, rejected or yet to be reviewed by PredictHQ. Possible values: `pending`, `approved`, `rejected`. E.g `?phq_review=approved`

***

**`sort`** _string_\
Comma-separated list of sort options. Prefix the field name with `-` for reverse order (e.g., `-created`). Possible values**:**

* `created`
* `updated`
* `version`
* `relevance`

E.g. `?sort=-updated`\
Defaults to `?sort=relevance,-updated`

***

**`limit`** _number_\
The maximum number of results to return. The default limit is `10`. E.g. `?limit=10`

***

**`offset`** _number_\
The number of results to skip. The default is `0`. E.g. `?offset=20`

***

## Response

### Response Fields

<table><thead><tr><th width="190">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>count</code><br>number</td><td>Total number of results found.</td></tr><tr><td><code>events</code><br>array</td><td><p>List of results where each item is a Submitted Event.</p><p><br>Please refer to the Submitted Event Response Fields section below for the structure of each record.</p></td></tr></tbody></table>

#### Submitted Event Response Fields

<table><thead><tr><th width="286">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>event_id</code><br>string</td><td>The unique identifier of the event.<br><br>E.g. <code>z13B3870YOgv</code></td></tr><tr><td><code>link_id</code><br>string</td><td>Loop Link ID that was used to submit this event.<br><br>Will only be available on submissions that were made with a Loop Link.</td></tr><tr><td><code>create_dt</code><br>string</td><td><p>The creation date time for the record in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a> format.</p><p><br>E.g. <code>2022-04-26T11:46:24+00:00</code></p></td></tr><tr><td><code>update_dt</code><br>string</td><td><p>The last update date time for the record in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a> format.</p><p><br>E.g. <code>2022-04-26T11:46:24+00:00</code></p></td></tr><tr><td><code>version</code><br>number</td><td>Version number of the record.<br><br>This number increments automatically every time the record is updated.</td></tr><tr><td><code>phq_review</code><br>string</td><td><p>Current review status. All submissions go through a moderation process. This field refers to the PredictHQ moderators.<br><br>Possible values:</p><ul><li><code>pending</code></li><li><code>approved</code></li><li><code>rejected</code></li></ul></td></tr><tr><td><code>org_review</code><br>string</td><td><p>Current review status for customer-initiated reviews. Some organizations are able to review submissions before they're moderated by PredictHQ staff.<br><br>Possible values:</p><ul><li><code>pending</code></li><li><code>approved</code></li><li>r<code>ejected</code></li></ul></td></tr><tr><td><code>phq_auto_approved</code><br>boolean</td><td>Indicates whether or not the record was automatically approved.<br><br>Some organizations are able to have their submissions enter our automatic review process after a period of time with consistent high quality level of submissions.</td></tr><tr><td><code>event.title</code><br>string</td><td>The title of the event.<br><br>E.g. <code>Katy Perry</code></td></tr><tr><td><code>event.description</code><br>string</td><td><p>A description of the event.</p><p><br>E.g. <code>See Katy Perry in concert [...]</code></p></td></tr><tr><td><code>event.category</code><br>string</td><td><p>The category of the event.</p><p></p><p>Please see <a href="../../events/search-events.md#response-fields">Search Events</a> for a list of possible categories.</p><p></p><p>E.g. <code>concerts</code></p></td></tr><tr><td><code>event.state</code><br>string</td><td>The publication state of the event.<br><br>Please see <a href="../../events/search-events.md#response-fields">Search Events</a> for a list of possible states.</td></tr><tr><td><code>event.metadata</code><br>array</td><td><p>List of metadata associated with the event.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "metadata": [
    {
      "maximum_attendance": 5000
    },
    {
      "attendance": 3215
    }
  ]
}
</code></pre></td></tr><tr><td><code>event.dates</code><br>object</td><td><p>Event dates.<br><br>E.g.</p><pre class="language-json"><code class="lang-json">{
  "dates": {
    "fixed_date": {
      "start_date": "2023-06-02",
      "end_date": "2023-06-04"
    }
  }
}
</code></pre></td></tr><tr><td><code>event.labels</code><br>array</td><td><p>List of labels for the event.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "labels": [
    "festival",
    "food",
    "music"
  ]
}
</code></pre></td></tr><tr><td><code>event.lat</code><br>string</td><td><p>Latitude for the event.</p><p></p><p>E.g. <code>38.901544</code></p></td></tr><tr><td><code>event.lon</code><br>string</td><td>Longitude for the event.<br><br>E.g. <code>-119.7030036</code></td></tr><tr><td><code>event.address</code><br>string</td><td>Address for the event.<br><br>E.g. <code>859 U.S. Highway 395 North</code></td></tr><tr><td><code>event.formatted_address</code><br>string</td><td><p>Full formatted address for the event.</p><p></p><p>E.g.</p><pre><code>859 U.S. Highway 395 North
Gardnerville, Nevada 89410
United States of America
</code></pre></td></tr><tr><td><code>event.city</code><br>string</td><td>City of the event.</td></tr><tr><td><code>event.region</code><br>string</td><td>Region of the event.</td></tr><tr><td><code>event.postcode</code><br>string</td><td>Postcode of the event.</td></tr><tr><td><code>event.country</code><br>string</td><td>Country code in <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> format.</td></tr><tr><td><code>event.geometry</code><br>object</td><td><p>Geographic location of the event. Represented in <a href="https://geojson.org/">GeoJSON</a> format.<br></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "geometry": {
    "type": "Point",
    "coordinates": [
      -119.703022,
      38.9012446
    ]
  }
}
</code></pre></td></tr></tbody></table>

## Guides

Below are some guides relevant to this API:

* [Integrate with Loop Links](../../../integrations/integration-guides/integrate-with-loop-links.md)
