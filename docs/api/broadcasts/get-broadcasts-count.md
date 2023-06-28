# Get Broadcasts Count

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/broadcasts/count/
```

### Query Parameters

{% hint style="info" %}
This endpoint accepts the same query parameters as the Search Broadcasts endpoint. Please refer to the [Search Broadcasts](search-broadcasts.md) documentation for query parameters.
{% endhint %}

## Response

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "count": 3142
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/broadcasts/count/?event.event_id=AdKtL974inQB7GURRd \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/broadcasts/count",
    headers={
      "Accept": "application/json",
      "Authorization": "Bearer $ACCESS_TOKEN"
    },
    params={
        "event.event_id": "AdKtL974inQB7GURRd"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

