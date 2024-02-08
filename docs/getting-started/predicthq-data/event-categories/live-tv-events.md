---
description: >-
  Live TV Events covers live broadcast sports games with a large number of
  people watching at a particular time across different counties across the
  United States.
---

# Live TV Events

For example, during the basketball game [Villanova Wildcats vs Baylor Bears](https://control.predicthq.com/search/events/3pgcB4kTQdLv6FAhCb#broadcasts) on March 27, 2021, there were over 150,000 people in Cook County, Illinois watching the live broadcast of the basketball game, as well as over 130,000 people were watching the game in Los Angeles County, California, etc.

**Note**: Live TV Events covers live games. Replays of sporting events are not included.

{% hint style="info" %}
Live TV events provide viewership data that is attached to events in other categories. Initially, it was launched for the sports category. In future it will be extended to other categories. Live TV events is not actually a category itself but consists of rich information on who is watching events in different locations.

The current release of Live TV events shows the number of people watching sports events per county in the US.
{% endhint %}

Live TV events include live streaming and broadcast TV games (such as MLS Soccer games streamed on Apple TV).&#x20;

## Coverage

**Event Types**

We have two different types of broadcast information. Major sports league viewership uses one model and top viewership sports uses a different approach. This affects how the viewership is calculated and which counties viewership is shown in. For the major sports leagues, viewership per county uses TV schedule information to predict where people will watch a game. Viewership is only shown for the counties where we predict people will watch a game. Top viewership sports, unlike the major sports leagues games, will always show viewership in all counties in the US.

**7 MAJOR SPORTS LEAGUES**

All televised sports games from the following 7 sports leagues are covered in our live TV events, the broadcasts may have status of either `scheduled` or `cancelled`:

`NFL`, `NBA`, `NHL`, `MLB`, `MLS`, `D1 NCAA Basketball`, `D1 NCAA Football`

**TOP VIEWERSHIP SPORTS**

Live TV Events extends coverage to some popular sports games beyond the above seven leagues. These are events that have high viewership and are assumed to be televised nationally (in all counties). The broadcasts may have status of either `predicted` or `cancelled`

Top viewership sports are typically one-off events or are finals of their respective competitions, such as the 2019 NCAA Women's Basketball Final:

<table><thead><tr><th width="200.33333333333331">SPORTS TYPE</th><th>SPORTS LEAGUE</th><th>EVENT TYPE</th></tr></thead><tbody><tr><td><code>auto-racing</code></td><td><ul><li><code>nascar</code></li><li><code>indy-car</code></li></ul></td><td><ul><li>NASCAR Cup Series Races</li><li>Indy 500</li></ul></td></tr><tr><td><code>horse-racing</code></td><td><ul><li><code>kentucky-derby</code></li><li><code>preakness-stakes</code></li><li><code>belmont-stakes</code></li></ul></td><td><ul><li>Kentucky Derby Horse Racing</li><li>Preakness Stakes Horse Racing</li><li>Belmont Stakes Horse Racing</li></ul></td></tr><tr><td><code>basketball</code></td><td><ul><li><code>ncaa-women</code></li></ul></td><td>NCAA Women's Basketball Division 1 Tournament Semifinals and Finals</td></tr><tr><td><code>baseball</code></td><td><ul><li><code>ncaa</code></li></ul></td><td>NCAA Baseball World Series Finals</td></tr><tr><td><code>softball</code></td><td><ul><li><code>ncaa-women</code></li></ul></td><td>NCAA Softball World Series Finals</td></tr><tr><td><code>boxing</code></td><td><ul><li><code>boxing</code></li></ul></td><td>Popular boxing games, for example Premier Boxing Champions</td></tr><tr><td><code>mma</code></td><td><ul><li><code>ufc</code></li></ul></td><td>Popular UFC games, for example UFC 246</td></tr><tr><td><code>tennis</code></td><td><ul><li><code>wimbledon</code></li><li><code>us-open</code></li></ul></td><td>Men’s and Women’s Singles Finals</td></tr><tr><td><code>golf</code></td><td><ul><li><code>masters</code></li><li><code>pga-championship</code></li><li><code>us-open</code></li><li><code>pga-tour</code></li></ul></td><td><ul><li>Augusta Masters all days of competition</li><li>PGA Championship all days of competition</li><li>USA Open all days of competition</li><li>Arnold Palmer weekend days of competition</li><li>Genesis Invitational weekend days of competition</li><li>Pebble Beach weekend days of competition</li><li>BMW Championship weekend days of competition</li><li>Farmers Insurance weekend days of competition</li></ul></td></tr><tr><td><code>soccer</code></td><td><ul><li><code>fifa-world-cup-women</code></li><li><code>fifa-world-cup</code></li><li><code>uefa-champions-league</code></li><li><code>concacaf-champions-league</code></li><li><code>concacaf-gold-cup</code></li><li><code>copa-america</code></li></ul></td><td><ul><li>FIFA World Cup Semis onward</li><li>UEFA Champions League Final</li><li>CONCACAF Champions League Final</li><li>CONCACAF Gold Cup Final</li><li>Copa America Final</li><li>UWNST World Cup Playoff matches</li></ul></td></tr></tbody></table>

Note: The sports type column is shown in the `event_label` field in the broadcast record.

**Date Range Coverage**

Live TV Events via the Broadcast API covers sports games that started from November 1, 2021, to 90 days in the future (90 days from the current date).

**Location**

Live TV Events are currently available in the US at the current stage.

#### Broadcast Status

Broadcasts have three possible status values:

* **`scheduled`**\
  For those broadcasts where we know the date, time and location of a TV broadcast based on TV schedule information. We enrich our data with television listings to determine their televised time and location (county).
* **`predicted`**\
  For these broadcasts where we predict their televised time and location (county). It means we don’t have detailed TV schedule information for the sports event. These events have high viewership and are assumed to be televised nationally (in all counties), they are typically one-off events or are finals of their respective competitions.\
  \
  We calculate viewership per county based on many factors including the amount of sports fans in different counties. This information is not as precise as those with the `scheduled` broadcast status but should give a reasonably accurate prediction of who will be watching these large events. Customers may want to use the `broadcast_status` parameter to indicate the confidence of a broadcast airing; they may build this as a feature or to treat scheduled broadcasts differently from predicted.
* **`cancelled`**\
  The broadcast is no longer scheduled to be televised.

#### Date & Time

<table data-header-hidden><thead><tr><th width="188">Date &#x26; Time Field</th><th align="center">Availability - Broadcast</th><th align="center">Availability - Event</th><th>Notes</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td align="center">Yes</td><td><ul><li>Broadcast records have a start date and time in both UTC and local time where the broadcast is scheduled.</li></ul><ul><li>Physical events have a start date and time in both UTC and local time in the event timezone.</li></ul></td></tr><tr><td>End date</td><td align="center">No</td><td align="center">Yes</td><td><ul><li>The Broadcast record doesn’t have an end date or time available.</li></ul><ul><li>Physical events have an end date and time in both UTC and local time in the event timezone.</li></ul></td></tr><tr><td>Start time</td><td align="center">Yes</td><td align="center">Yes</td><td></td></tr><tr><td>End time</td><td align="center">No</td><td align="center">Yes</td><td></td></tr><tr><td>Predicted end time</td><td align="center">No</td><td align="center">Yes</td><td>For sports events where there is no official end time available, we predict end times using our machine learning models and intelligent algorithms. PredictHQ’s Predicted End Times feature provides end times for the physical event in it’s local timezone.</td></tr><tr><td>Timezone</td><td align="center">Yes</td><td align="center">Yes</td><td></td></tr></tbody></table>

#### Location / Geopoint

The broadcast record presents the number of people who are watching the live sports game in a county. The latitude and longitude provided with the broadcast record under the geopoint element references the center of the county. For example, the center of Erie County in New York state shown on the right.

The associated sports event is taking place in a physical location with the latitude and longitude pointing to the specific location. The venue name and address is also attached on the event record.

Places in any [hierarchy level](../../../api/places/get-place-hierarchies.md) can be used to search in the API or in Control Center. The results will be returned on the county level where the place is located. For example, users can search for the broadcast in Bell City, Los Angeles, and all broadcasts in Los Angeles County that match other criteria will be returned in the result.

## Ranking

**PHQ Viewership**

PHQ Viewership is the number of people who watch the live broadcast game in a county. Broadcast records have PHQ Viewership available.

```json
  "geopoint": {
      "lon": -78.77966,
      "lat": 42.75824
  },
```

#### Timeframe for broadcasts

The Live TV Events machine learning models predicted the viewership for sports games before they happen. Broadcast records are generated 90 days before a sports game starts. However, viewership is updated daily from 14 days before the event starts providing more accurate data. To get the most accurate data we recommend using the broadcast viewership from 14 days before the event or sooner. The viewership numbers generated between 90 days and 14 days can be used as a high-level less accurate indication of viewership.

#### Physical Event Details

The broadcast API also returns the physical event details accordingly with all available information. Users don’t need an event subscription to access relevant information.

* **Event ID**: `event_id` of the physical event can be used to find all broadcasts nationwide for that specific sport game.
* **Label**: `event.label` for the physical sports event provides more information about the sports type and league. It can be used to find broadcasts for the specific sports type.
* **Entity**: The physical sports events have venue entities available.
* **PHQ Rank**: The physical sports events have PHQ Rank available.
* **Local Rank**: The physical sports events have Local Rank available.
* **Aviation Rank**: The physical sports events have Aviation Rank available.
* **PHQ Attendance**: The physical sports events have PHQ Attendance available.

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "overflow": false,
    "results": [
        {
            "broadcast_id": "u5aCvebffuNFpGSGNQFiU4",
            "updated": "2020-11-30T06:58:28Z",
            "first_seen": "2020-11-26T01:29:23Z",
            "dates": {
                "start": "2020-02-02T23:30:00Z",
                "start_local": "2020-02-02T15:30:00",
                "timezone": "America/Los_Angeles"
            },
            "location": {
                "geopoint": {
                    "lon": -122.4425,
                    "lat": 37.77823
                },
                "place_hierarchies": [
                    ["6295630","6255149","6252001","5332921","5391997"]
                ],
                "places": [
                    {
                        "place_id": "5391997",
                        "type": "county",
                        "name": "San Francisco County",
                        "county": "City and County of San Francisco",
                        "region": "California",
                        "country": "US"
                    }
                ],
                "country": "US"
            },
            "phq_viewership": 300609,
            "record_status": "active",
            "broadcast_status": "scheduled",
            "event": {
                "event_id": "svbfg9xT4YSVUeeAKp",
                "title": "Super Bowl - 49ers vs Kansas City Chiefs",
                "category": "sports",
                "labels": [
                    "american-football",
                    "nfl",
                    "sport"
                ],
                "dates": {
                    "start": "2020-02-02T23:30:00Z",
                    "end": "2020-02-03T03:11:00Z",
                    "start_local": "2020-02-02T18:30:00",
                    "end_local": "2020-02-02T22:11:00",
                    "predicted_end_local": "2020-02-02T21:25:00",
                    "timezone": "America/New_York"
                },
                "location": {
                    "geopoint": {
                        "lon": -80.23886040000002,
                        "lat": 25.9579665
                    },
                    "place_hierarchies": [
                        ["6295630","6255149","6252001","4155751","4164238","4161298"],
                        ["6295630","6255149","6252001","4155751","4149007","4155966"]
                    ],
                    "country": "US"
                },
                "entities": [
                    {
                        "entity_id": "wVgG7p8ZKRKEPPrNDq4my9",
                        "type": "venue",
                        "name": "Hard Rock Stadium",
                        "formatted_address": "347 Don Shula Dr\nMiami Gardens, FL 33056\nUnited States of America"
                    }
                ],
                "phq_attendance": 65326,
                "phq_rank": 86,
                "local_rank": 100,
                "aviation_rank": 99
            }
        }
    ]
}
```

