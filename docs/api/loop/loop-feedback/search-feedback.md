---
description: Search feedback conversations submitted by your organization.
---

# Search Feedback

Conversations are used to track feedback on existing events for example feedback on incorrect attendance or start and end dates for an event. Each piece of feedback submitted by a user is tracked as a conversation and will be returned by this endpoint. You can use this to display a list of event feedback conversations submitted with Loop Links by users in your application.

{% openapi-operation spec="loop-api" path="/v1/loop/feedback/conversations" method="get" %}
[OpenAPI loop-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/loop-api.yaml)
{% endopenapi-operation %}

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

## OpenAPI Spec

The OpenAPI spec for Loop API can be [found here](https://api.predicthq.com/docs/?urls.primaryName=Loop+API).

## Guides

ow are some guides relevant to this API:

* [Integrate with Loop Links](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/integrations/integration-guides/integrate-with-loop-links)
