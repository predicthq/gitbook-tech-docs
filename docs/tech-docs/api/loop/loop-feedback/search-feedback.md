---
description: Search feedback conversations submitted by your organization.
---

# Search Feedback

Conversations are used to track feedback on existing events for example feedback on incorrect attendance or start and end dates for an event. Each piece of feedback submitted by a user is tracked as a conversation and will be returned by this endpoint. You can use this to display a list of event feedback conversations submitted with Loop Links by users in your application.

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/loop/feedback/conversations
```

### Query Parameters

<table><thead><tr><th width="219">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>q</code><br>string</td><td>Full-text search over conversations.<br><br>E.g. <code>?q=event+a+cancelled</code></td></tr><tr><td><code>link_id</code><br>string</td><td>Comma separated list of Loop Link IDs through which conversations were created.<br><br>E.g <code>?link_id=m4Dk4g4DRA8Yqbp2PC54</code></td></tr><tr><td><code>conversation_id</code><br>string</td><td>Comma separated list of conversation IDs.<br><br>E.g <code>?conversation_id=Eeh4ahnohghah0deeshahda</code></td></tr><tr><td><code>record_id</code><br>string</td><td><p>Comma separated list of Record IDs.</p><p></p><p>Record IDs can refer to either an Event ID (record type <code>event-public</code>) or a Loop Submission (record type <code>event-loop</code>). <br><br>E.g <code>?record_id=5uRg7CqGu7DTtu4Rfk</code></p></td></tr><tr><td><code>record_type</code><br>string</td><td><p>Comma separated list of record types for which to filter on.<br><br>Possible values:</p><ul><li><code>event-public</code> - Event ID available via <a href="../../events/search-events.md">Events API</a>.</li><li><code>event-loop</code> - Loop Submission ID.</li></ul><p>E.g <code>?record_type=event-public</code></p></td></tr><tr><td><code>feedback_type</code><br>string</td><td><p>Comma separated list of feedback types.<br><br>Possible values:</p><ul><li><code>attendance_or_rank</code></li><li><code>category</code></li><li><code>dates</code></li><li><code>general</code></li><li><code>polygon</code></li><li><code>venue</code></li></ul><p>E.g <code>?feedback_type=general</code></p></td></tr><tr><td><code>user_id</code><br>string</td><td>Comma separated list of User IDs.<br><br>E.g. <code>?user_id=hw8Dsmv4Djg</code></td></tr><tr><td><code>status</code><br>string</td><td><p>Comma separated list of feedback status.<br><br>Possible values:</p><ul><li><code>open</code></li><li><code>closed</code></li></ul><p>E.g <code>?status=open</code></p></td></tr><tr><td><code>created</code><br>string</td><td><p>The date from and/or to the feedback has been created.<br><br>Must be used with one of more of the suffixes:</p><ul><li><code>lt</code></li><li><code>lte</code></li><li><code>gt</code></li><li><code>gte</code></li></ul><p>E.g. <code>?created.gt=2023-03-04&#x26;created.lte=2023-05-01</code></p></td></tr><tr><td><code>updated</code><br>string</td><td><p>The date from and/or to the feedback has been updated.</p><p></p><p>Must be used with one of more of the suffixes:</p><ul><li><code>lt</code></li><li><code>lte</code></li><li><code>gt</code></li><li><code>gte</code></li></ul><p>E.g. <code>?updated.gt=2023-03-04&#x26;updated.lte=2023-05-01</code></p></td></tr><tr><td><code>sort</code><br>string</td><td><p>Comma-separated list of sort options.<br><br>Prefix the field name with <code>-</code> for reverse order.<br><br>Possible values:</p><ul><li><code>created</code></li><li><code>updated</code></li><li><code>relevance</code></li></ul><p>Default value is <code>?sort=relevance,created</code></p><p><br>E.g. <code>?sort=-updated</code></p></td></tr><tr><td><code>limit</code><br>number</td><td><p>The maximum number of results to return.</p><p></p><p>The default limit is <code>10</code>.<br><br>E.g. <code>?limit=10</code></p></td></tr><tr><td><code>offset</code><br>number</td><td><p>The number of results to skip.</p><p></p><p>The default is <code>0</code>.<br><br>E.g. <code>?offset=20</code></p></td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="190">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>count</code><br>number</td><td>Total number of results found.</td></tr><tr><td><code>conversations</code><br>array</td><td><p>List of results where each item is a Conversation.</p><p><br>Please refer to the Conversation Response Fields section below for the structure of each record.</p></td></tr></tbody></table>

#### Conversation Response Fields

<table><thead><tr><th width="245">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>conversation_id</code><br>string</td><td>The unique identifier of the conversation.<br><br>E.g. <code>Eeh4ahnohghah0deeshahda</code></td></tr><tr><td><code>create_dt</code><br>string</td><td><p>The creation date time for the record in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a> format.</p><p><br>E.g. <code>2022-04-26T11:46:24+00:00</code></p></td></tr><tr><td><code>update_dt</code><br>string</td><td><p>The last update date time for the location in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a> format.</p><p><br>E.g. <code>2022-04-26T11:46:24+00:00</code></p></td></tr><tr><td><code>link_id</code><br>string</td><td>Loop Link ID that was used to submit this feedback.<br><br>Will only be available on feedback created with a Loop Link.<br><br>E.g. <code>m4Dk4g4DRA8Yqbp2PC54</code></td></tr><tr><td><code>record_id</code><br>string</td><td>Record ID this feedback is in reference to.<br><br>This could be either an Event ID (record type <code>event-public</code>) or a Loop Submission (record type <code>event-loop</code>). The <code>record_type</code> value defines what type of Record ID this is.<br><br>E.g. <code>5uRg7CqGu7DTtu4Rfk</code></td></tr><tr><td><code>record_type</code><br>string</td><td><p>Record type this feedback is in reference to.</p><p></p><p>Possible types:</p><ul><li><code>event-public</code></li><li><code>event-loop</code></li></ul><p>E.g. <code>event-public</code><br></p></td></tr><tr><td><code>feedback</code><br>object</td><td><p>Feedback can be provided for different fields.</p><p></p><p>Possible types:</p><ul><li><code>attendance_or_rank</code> - Attendance or Rank</li><li><code>category</code> - Category might need adjusting</li><li><code>dates</code> - Dates might need adjusting</li><li><code>duplicate</code> - Record might be a duplicate</li><li><code>general</code> - Other feedback</li><li><code>polygon</code> - Polygon might need adjusting</li><li><code>submitted</code> - Feedback about an existing Loop submission</li><li><code>venue</code> - Venue might need adjusting</li></ul><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "feedback": {
    "type": "submitted"
  }
}
</code></pre></td></tr><tr><td><code>log</code><br>array</td><td><p>Log of actions taken with the feedback.<br></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "log": [
    {
      "action": {
        "type": "comment"
      },
      "timestamp": "2023-05-30T02:59:11+00:00",
      "creator": {
        "type": "user",
        "user_id": "hw8Dsmv4Djg"
      },
      "note": "Thank you for your feedback. Someone from PredictHQ will pick this up."
    }
  ]
}
</code></pre></td></tr><tr><td><code>status</code><br>string</td><td><p>Status of the feedback.<br></p><p>Possible values:</p><ul><li><code>open</code></li><li><code>closed</code></li></ul><p>E.g. <code>open</code></p></td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
  "count": 1,
  "conversations": [
    {
      "conversation_id": "Eeh4ahnohghah0deeshahda",
      "create_dt": "2021-05-25T05:33:53+00:00",
      "update_dt": "2021-05-25T05:38:08+00:00",
      "link_id": "m4Dk4g4DRA8Yqbp2PC54",
      "record_id": "5uRg7CqGu7DTtu4Rfk",
      "record_type": "event-public",
      "feedback": {
        "type": "submitted"
      },
      "log": [
        {
          "action": {
            "type": "created"
          },
          "timestamp": "2023-05-30T02:44:46+00:00",
          "creator": {
            "type": "unauthenticated_user",
            "link_id": "m4Dk4g4DRA8Yqbp2PC54"
          },
          "note": "This event title should be different"
        },
        {
          "action": {
            "type": "comment"
          },
          "timestamp": "2023-05-30T02:59:11+00:00",
          "creator": {
            "type": "user",
            "user_id": "hw8Dsmv4Djg"
          },
          "note": "Thank you for your feedback. Someone from PredictHQ will pick this up."
        },
        {
          "action": {
            "type": "comment"
          },
          "timestamp": "2023-05-30T03:41:06+00:00",
          "creator": {
            "type": "moderator"
          },
          "note": "Absolutely, we'll change this right away "
        }
      ],
      "status": "open"
    }
  ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/loop/feedback/conversations?link_id=m4Dk4g4DRA8Yqbp2PC54" \
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
        "link_id": "m4Dk4g4DRA8Yqbp2PC54"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [Integrate with Loop Links](../../../integrations/integration-guides/integrate-with-loop-links.md)
