---
description: Update your Loop Settings.
---

# Update Loop settings

{% openapi-operation spec="loop-api" path="/v1/loop/settings" method="put" %}
[OpenAPI loop-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/loop-api.yaml)
{% endopenapi-operation %}

## Examples

Update the organization name:

{% tabs %}
{% tab title="curl" %}
```bash
curl -X PUT "https://api.predicthq.com/v1/loop/settings" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $API_TOKEN" \
     --data @<(cat <<EOF
    {
        "org_name": "My Org Name"
    }
    EOF
    )
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.put(
    url="https://api.predicthq.com/v1/loop/settings",
    headers={
        "Authorization": "Bearer $API_TOKEN",
        "Accept": "application/json"
    },
    json={
        "org_name": "My Org Name"
    }
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

## OpenAPI spec

See the [OpenAPI spec for the Loop API](https://api.predicthq.com/docs/?urls.primaryName=Loop+API).

## Guides

ow are some guides relevant to this API:

* [Integrate with Loop Links](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/integrations/integration-guides/integrate-with-loop-links)
