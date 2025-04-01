---
description: Get the count of events by category, PHQ Label and more.
---

# Get Event Counts

{% openapi src="https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/events-api.yaml" path="/v1/events/count/" method="get" %}
[https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/events-api.yaml](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/events-api.yaml)
{% endopenapi %}

## OpenAPI Spec

The OpenAPI spec for Events API can be [found here](https://github.com/predicthq/api-specs/blob/main/openapi/events-api.yaml).

### Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/events/count/?country=NZ" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/count/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "country": "NZ"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
