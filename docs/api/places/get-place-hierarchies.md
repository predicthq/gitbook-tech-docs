# Get Place Hierarchies

{% hint style="info" %}
This endpoint is in Beta.
{% endhint %}

The currently available filters and response data change are subject to change.

This endpoint allows you to get the full place hierarchies for

* a given coordinate
* list of `place_id`.

A place hierarchy is a list of place identifiers and types from the `planet` level down to the `level` specified in your query (please note that `level` defaults to `locality` if not specified in your query).

The response might include more than one hierarchy for a given coordinate. The reason for this is that we try to match the closest place's hierarchy but we also include the closest major city's hierarchy within a radius of 50km. This only applies if the `level` is below `region` and, if it exists, the major city's hierarchy will always be the second item in the list.

For instance, if you specify `?location.origin=47.615337,-122.203981`, which is a coordinate located in [Bellevue, Washington](https://en.wikipedia.org/wiki/Bellevue,\_Washington), you'll get two hierarchies, one for Bellevue but also one for [Seattle](https://en.wikipedia.org/wiki/Seattle).

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/places/hierarchies/
```

### Query Parameters

<table><thead><tr><th width="227">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><strong>country</strong><br>string</td><td>An <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> country code.<br><br>E.g. <code>?country=US</code></td></tr><tr><td><strong>location.origin</strong><br>coordinate</td><td><p>A coordinate in the form <code>{latitude},{longitude}</code>.<br></p><p>Please note that you must specify either <code>location.origin</code> or <code>location.place_id</code> in your request.</p><p><br>E.g. <code>?location.origin=47.615337,-122.203981</code></p></td></tr><tr><td><strong>location.place_id</strong><br>string</td><td>A list of <code>place_id</code> in the form <code>{place_id1},{place_id2},...</code>.<br><br>Please note that you must specify either <code>location.origin</code> or <code>location.place_id</code> in your request.<br><br>E.g. <code>?location.place_id=5809844,6252001</code></td></tr><tr><td><strong>level</strong><br>string</td><td><p>A place level.<br><br><strong>Possible values:</strong></p><ul><li><code>neighbourhood</code></li><li><code>locality</code></li><li><code>localadmin</code></li><li><code>county</code></li><li><code>region</code></li><li><code>country</code></li><li><code>continent</code></li><li><code>planet</code></li></ul><p>Defaults to <code>locality</code>.<br><br>E.g. <code>?level=county</code></p></td></tr></tbody></table>

## Response

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "place_hierarchies": [
        [
            {
                "type": "planet",
                "place_id": "6295630"
            },
            {
                "type": "continent",
                "place_id": "6255149"
            },
            {
                "type": "country",
                "place_id": "6252001"
            },
            {
                "type": "region",
                "place_id": "5815135"
            },
            {
                "type": "county",
                "place_id": "5799783"
            },
            {
                "type": "locality",
                "place_id": "5786882"
            }
        ],
        [
            {
                "type": "planet",
                "place_id": "6295630"
            },
            {
                "type": "continent",
                "place_id": "6255149"
            },
            {
                "type": "country",
                "place_id": "6252001"
            },
            {
                "type": "region",
                "place_id": "5815135"
            },
            {
                "type": "county",
                "place_id": "5799783"
            },
            {
                "type": "locality",
                "place_id": "5809844"
            }
        ]
    ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/places/hierarchies/?location.origin=47.615337,-122.203981 \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/places/hierarchies/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "location.place_id": "5809844,6252001"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
