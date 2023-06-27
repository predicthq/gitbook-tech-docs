# Search Events

Use the below parameters to search and filter all events that are available to your account.

{% hint style="info" %}
**Visibility Window**

Please note that you will not receive an error when requesting a date range and/or location that is outside of your subscription's broadcast visibility window. Instead, your visibility window will be automatically applied to your results.

Your plan’s visibility window is shown in your [plan summary](https://account.predicthq.com/plans/).
{% endhint %}

{% hint style="info" %}
Result Limit

Please note the number of results returned will be limited to your subscription's result limit. If more results exist, the `overflow` field will be set to true to indicate the count number has been capped to your pagination limit.

Your plan’s pagination limits are shown in your [plan summary](https://account.predicthq.com/plans/).
{% endhint %}

## test

{% swagger method="get" path="/v1/events" baseUrl="https://api.predicthq.com" summary="Search Events" expanded="true" fullWidth="true" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter in="query" name="active.*" type="date range" %}
The date from and/or to the events intersect with. Supports 

`gt`

, 

`gte`

, 

`lt`

, 

`lte`

 and 

`tz`

 suffixes.

\




\


The accepted format for this parameter is either 

`YYYY-MM-DD`

 or 

`YYYY-MM-DDThh:mm:ss`

\




\


Please note that use of a suffix is 

**required**

.

\


E.g. 

`?active.gte=2015-01-01&active.lte=2015-03-01`
{% endswagger-parameter %}

{% swagger-parameter in="query" name="aviation_rank.*" %}
Supports 

`gt`

, 

`gte`

, 

`lt`

 and 

`lte`

 suffixes.

\


Please note that use of a suffix is 

**required**

.

\


Note when filtering on 

`aviation_rank`

 events that do not have an 

`aviation_rank`

 will not be returned.

\


E.g. 

`?aviation_rank.gte=80&aviation_rank.lte=90`
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Example response" %}
```json
{
    "count": 1,
    "overflow": false,
    "next": null,
    "previous": null,
    "results": [
        {
            "relevance": 0.0,
            "id": "5uRg7CqGu7DTtu4Rfk",
            "parent_event": {
                "parent_event_id": "w7dYyrFwTUQGYE6euv"
            },
            "title": "Formula 1 2019 - United States Grand Prix 2019 - Race",
            "description": "The 2019 United States Grand Prix (officially known as the Formula 1 Emirates United States Grand Prix 2019) was a Formula One motor race held on 3 November 2019 at the Circuit of the Americas in Austin, Texas, United States. The race was the 19th round of the 2019 Formula One World Championship (1 - 3 Nov) and marked the 49th running of the United States Grand Prix.",
            "category": "sports",
            "labels": [
                "auto-racing",
                "f1",
                "sport"
            ],
            "rank": 92,
            "local_rank": 100,
            "aviation_rank": 93,
            "phq_attendance": 120000,
            "entities": [
                {
                    "entity_id": "MasUgUJtWz3kQFVgCG6rJU",
                    "name": "Circuit of the Americas",
                    "type": "venue",
                    "formatted_address": "9201 Circuit of the Americas Boulevard\nAustin, TX 78617\nUnited States of America"
                }
            ],
            "duration": 7200,
            "start": "2019-11-03T19:10:00Z",
            "end": "2019-11-03T21:10:00Z",
            "updated": "2022-11-10T19:50:36Z",
            "first_seen": "2019-07-04T22:14:31Z",
            "timezone": "America/Chicago",
            "location": [
                -97.63585109999997,
                30.1345808
            ],
            "geo": {
                "geometry": {
                    "coordinates": [
                        -97.63585109999997,
                        30.1345808
                    ],
                    "type": "Point"
                },
                "placekey": "222-229@8t2-fgc-z2k"
            },
            "scope": "locality",
            "country": "US",
            "place_hierarchies": [
                [
                    "6295630",
                    "6255149",
                    "6252001",
                    "4736286",
                    "4737316",
                    "4689116"
                ],
                [
                    "6295630",
                    "6255149",
                    "6252001",
                    "4736286",
                    "4737316",
                    "4671654"
                ]
            ],
            "state": "active",
            "private": false
        }
    ]
}
```
{% endswagger-response %}
{% endswagger %}

{% swagger src="../../.gitbook/assets/openapi (1).yaml" path="/v1/events" method="get" expanded="true" %}
[openapi (1).yaml](<../../.gitbook/assets/openapi (1).yaml>)
{% endswagger %}
