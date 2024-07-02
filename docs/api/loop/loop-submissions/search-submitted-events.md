---
description: Search events submitted by your organization.
---

# Search Submitted Events

For example, you can use this to display a list of events submitted via Loop Links within your application to your users. See also the [Events API documentation](../../events/search-events.md#query-parameters) for more detail on many of the parameters mentioned below.

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/loop/events
```

### Query Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>q</code><br>string</td><td>Full-text search of event information.<br><br>E.g. <code>?q=hotel+a</code></td></tr><tr><td><code>link_id</code><br>string</td><td>Comma-separated list of link ids. Allows you to filter on events submitted via a specific Loop Link link id.<br><br>E.g. <code>?link_id=m4Dk4g4DRA8Yqbp2PC54</code></td></tr><tr><td><code>event_id</code><br>string</td><td>Comma-separated list of event ids. Allows you to retrieve specific events.<br><br>E.g. <code>?event_id=5uRg7CqGu7DTtu4Rfk</code></td></tr><tr><td><code>user_id</code><br>string</td><td>Comma-separated list of user ids that submitted events.<br><br>E.g. <code>?user_id=hw8Dsmv4Djg</code></td></tr><tr><td><code>state</code><br>string</td><td><p>Comma separated list of event states.<br><br><strong>Possible values</strong>: </p><ul><li><code>active</code></li><li><code>predicted</code></li><li><code>cancelled</code></li><li><code>postponed</code></li><li><code>archived</code></li></ul></td></tr><tr><td><code>category</code><br>string</td><td>Comma separated list of event categories.<br><br>E.g. <code>?category=expos,festivals</code></td></tr><tr><td><code>label</code><br>string</td><td>Comma separated list of event labels.<br><br>E.g. <code>?label=community,food,music</code></td></tr><tr><td><code>country</code><br>string</td><td>Comma separated list of country codes.<br><br>E.g. <code>?country=NZ,US</code></td></tr><tr><td><code>start.*</code><br>string</td><td>The date from and/or to the event starts.<br><br>Must be used with suffixes <code>lt</code>, <code>lte</code>, <code>gt</code> or <code>gte</code>.<br><br>E.g. <code>?start.gt=2023-03-04&#x26;start.lte=2023-05-01</code></td></tr><tr><td><code>end.*</code><br>string</td><td>The date from and/or to the event ends.<br><br>Must be used with suffixes <code>lt</code>, <code>lte</code>, <code>gt</code> or <code>gte</code><br><br>E.g. <code>?end.gt=2023-03-04&#x26;end.lte=2023-05-01</code></td></tr><tr><td><code>active.*</code><br>string</td><td>The date from and/or to the event is active.<br><br>Must be used with suffixes <code>lt</code>, <code>lte</code>, <code>gt</code> or <code>gte</code>.<br><br>E.g. <code>?active.gt=2023-03-04&#x26;active.lte=2023-05-01</code></td></tr><tr><td><code>created.*</code><br>string</td><td>The date from and/or to the event has been created.<br><br>Must be used with suffixes <code>lt</code>, <code>lte</code>, <code>gt</code> or <code>gte</code>.<br><br>E.g. <code>?created.gt=2023-03-04&#x26;created.lte=2023-05-01</code></td></tr><tr><td><code>updated.*</code><br>string</td><td>The date from and/or to the event has been updated.<br><br>Must be used with suffixes <code>lt</code>, <code>lte</code>, <code>gt</code> or <code>gte</code>.<br><br>E.g. <code>?updated.gt=2023-03-04&#x26;updated.lte=2023-05-01</code></td></tr><tr><td><code>private.include</code><br>string</td><td><p>Whether or not to include private events.<br><br>Rejected &#x26; pending submitted events will always be private.<br><br><strong>Possible values</strong>: <code>true</code>, <code>false</code>, <code>only</code>.E.g <code>?private.include=only</code></p><ul><li><code>true</code>: private and public events</li><li><code>false</code> (default): only public events</li><li><code>only</code>: only private events</li></ul></td></tr><tr><td><code>org_review</code><br>string</td><td>Filter for submitted events approved, rejected or yet to be treated by the related org.<br><br><strong>Possible values</strong>: <code>pending</code>, <code>approved</code>, <code>rejected</code>.<br><br>E.g <code>?org_review=approved</code></td></tr><tr><td><code>phq_review</code><br>string</td><td>Filter for submitted events approved, rejected or yet to be treated by PHQ.<br><br><strong>Possible values</strong>: <code>pending</code>, <code>approved</code>, <code>rejected</code>.<br><br>E.g <code>?phq_review=approved</code></td></tr><tr><td><code>sort</code><br>string</td><td><p>Comma-separated list of sort options.<br><br>Prefix the field name with <code>-</code> for reverse order.<br><br><strong>Possible values:</strong></p><ul><li><code>created</code></li><li><code>updated</code></li><li><code>version</code></li><li><code>relevance</code></li></ul><p><br>E.g. <code>?sort=-updated</code><br><br>Defaults to <code>?sort=relevance,-updated</code></p></td></tr><tr><td><code>limit</code><br>number</td><td>The maximum number of results to return. The default limit is <code>10</code>.<br><br>E.g. <code>?limit=10</code></td></tr><tr><td><code>offset</code><br>number</td><td>The number of results to skip. The default is <code>0</code>.<br><br>E.g. <code>?offset=20</code></td></tr></tbody></table>

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

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/loop/events?phq_review=approved \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

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
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [Integrate with Loop Links](../../../integrations/integration-guides/integrate-with-loop-links.md)
