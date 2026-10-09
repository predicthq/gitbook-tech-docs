---
description: Search for Live TV broadcasts happening in a location.
---

# Search Broadcasts

{% hint style="info" %}
**Your subscription limits results**

Note that you don't receive an error when requesting a date range or location that is outside of your subscription settings.

This is sometimes confused with missing data. If you're not seeing the results you expect to see then ensure your subscription covers the location or time period you're searching for.

Your subscription settings can be viewed in the [WebApp](https://control.predicthq.com/settings/plans).
{% endhint %}

{% openapi-operation spec="broadcasts-api" path="/v1/broadcasts/" method="get" %}
[OpenAPI broadcasts-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/broadcasts-api.yaml)
{% endopenapi-operation %}

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/broadcasts/?broadcast_id=u5aCvebffuNFpGSGNQFiU4" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $API_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/broadcasts/",
    headers={
      "Accept": "application/json",
      "Authorization": "Bearer $API_TOKEN"
    },
    params={
        "broadcast_id": "u5aCvebffuNFpGSGNQFiU4"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## OpenAPI spec

Read the [OpenAPI spec for Broadcasts API](https://api.predicthq.com/docs/?urls.primaryName=Broadcasts+API).

## Guides

{% hint style="info" %}
**USA Counties Mapping File**\
Counties are mapped to Place IDs. Download the [county-to-Place ID mapping file](https://github.com/predicthq/api-specs/blob/main/data/broadcast-county-place-mapping.csv).
{% endhint %}

Below are some guides relevant to this API:

* [Live TV event guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/live-tv-event-guides)
