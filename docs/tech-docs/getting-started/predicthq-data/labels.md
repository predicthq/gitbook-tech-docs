---
description: >-
  Event labels are succinct descriptive attributes attached to events that can
  help with granular data selection and feature engineering use cases.
---

# Labels

All our events occur within a category. We also have labels that indicate the classification within a category. You can think of it as sub-category level information. Sports is a category in our system but if you want to know what type of sport an event is for that is indicated by labels (e.g. `nfl`, `mls`, `nhl`, `nba`, etc)&#x20;

For example, within the Conferences category, knowing the subject(s) covered within the conference (`science-and-technology`, `educational`, `automotive`, etc.) may help you narrow down on events that are relevant to your business.&#x20;

* Each event record has two separate label fields (`phq_labels` and the legacy `labels` field).
* All categories have the new `phq_labels` and should be used by default.&#x20;
* Event labels can be searched by using the`phq_labels` parameter.
* Some `labels` which repeats the category name such as `label: academic` have been removed.

### PHQ Labels

PHQ Labels are generated using AI and achieve a higher standard of **specificity** and **relevance** in highlighting an event's key themes than the legacy labels.

This field is named `phq_labels`.

PHQ Labels are available for the following categories:

* Concerts
* Conferences
* Expos
* Festivals
* Performing Arts
* Community
* Academic&#x20;
* Airport-delays
* Daylight-savings
* Disasters
* Health-warnings
* Observances
* Politics
* Public-holidays
* Severe weather
* School-holidays&#x20;
* Terror
* Sports

#### PHQ Label Values

PHQ Labels are continuously improved and updated, so the set of values grows over time. The [full list of PHQ Label values](#all-phq-label-values) is on this page, refreshed daily, along with a CSV download. To see which labels appear on the events **within your PredictHQ plan** - and the count of events carrying each - use [Get event counts](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/get-event-counts).

Here is an example, for [Taylor Swift and Sabrina Carpenter](https://events.predicthq.com/events/ssZCJhGGKUswicJswa) at the Melbourne Cricket Ground in 2024 it has the following PHQ labels (pop, country, and rock) in the API response:

```json
"phq_labels": [
  { "label": "pop", "weight": 0.51 },
  { "label": "country", "weight": 0.25 },
  { "label": "rock", "weight": 0.25 }
]
```

You could also use [Query Parameters](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/get-event-counts) to retrieve a list and the count of PHQ Labels that match your criteria, e.g. PHQ Labels associated with the sports category or PHQ Labels of events that will be taking place in a specific time and place. Here is an example:

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/count",
    headers={
      "Authorization": "Bearer $API_TOKEN",
      "Accept": "application/json"
    },
    ## optional, get PHQ Labels and counts for sports category only
    # params={"category": "sports"}
)


# get PHQ Labels and the count of events having them from the response
phq_labels = response.json().get("phq_labels")

print(phq_labels)
# > {'basketball': 408197,'parade': 14327, ... }


```

You can also see a list of PHQ Labels in the "Labels" field on the [Search events](https://control.predicthq.com/search/events) page of the WebApp:

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-09 at 10.36.38 AM.png" alt=""><figcaption><p>The "Labels" field in the WebApp Search Events Page contains a list of PHQ Labels </p></figcaption></figure>

#### All PHQ Label values

The full list of 248 PHQ Label values, refreshed daily from the live API. Prefer a CSV? Download [phq-labels.csv](https://raw.githubusercontent.com/predicthq/gitbook-tech-docs/main/assets/phq-labels.csv).

|   |   |   |   |
| --- | --- | --- | --- |
| `academic-session` | `academic-social` | `agriculture-forestry-and-fisheries` | `air-quality` |
| `airport` | `alcohol` | `american-football` | `arson` |
| `art-and-cultural` | `ashfall` | `assassination` | `attack` |
| `australian-football` | `auto-racing` | `automotive` | `autumn-holiday` |
| `avalanche` | `badminton` | `bars-closed` | `bars-open` |
| `baseball` | `basketball` | `beauty-and-fashion` | `bicycle` |
| `biological-hazard` | `blizzard` | `bombing` | `boxing` |
| `business` | `celebration` | `charity` | `chemical` |
| `chemical-accident` | `christmas-holiday` | `circus` | `civil` |
| `climate-change` | `closed-doors` | `coastal-event` | `cold-wave` |
| `comedy` | `comedy-club` | `community-event` | `concert` |
| `conference` | `construction-and-infrastructure` | `consumer-goods` | `country` |
| `cricket` | `cultural` | `cultural-performance` | `cyclone` |
| `delay` | `design-and-furnishing` | `digital` | `dinner-theatre` |
| `disaster-warning` | `disasters-health` | `drought` | `dust` |
| `earthquake` | `easter-holiday` | `education` | `education-and-careers` |
| `educational` | `election` | `electronic` | `entertainment` |
| `entertainment-closed` | `entertainment-open` | `epidemic` | `epidemic-hazard` |
| `esports` | `estimated` | `exam` | `execution` |
| `explosion` | `expo` | `extreme-weather` | `f1` |
| `family` | `family-activities` | `family-fun` | `family-theatre` |
| `festival` | `festivals-and-outdoor-activities` | `fighting` | `financial-services` |
| `fire` | `flood` | `fog` | `food` |
| `food-and-beverage` | `football` | `general-theatre` | `golf` |
| `graduation` | `gymnastics` | `hail` | `hazardous-surf` |
| `hazmat` | `health` | `health-warning` | `heat-wave` |
| `hijacking` | `hip-hop-and-rnb-and-soul` | `hockey` | `holiday` |
| `holiday-christian` | `holiday-hebrew` | `holiday-hindu` | `holiday-local` |
| `holiday-local-common` | `holiday-muslim` | `holiday-national` | `holiday-observed` |
| `holiday-orthodox` | `holiday-religious` | `horse-racing` | `hospitality-and-travel` |
| `hostage-crisis` | `hurricane` | `hybrid-session` | `ice-hockey` |
| `in-person-session` | `industrial` | `indycar` | `ironman` |
| `jazz-and-classical` | `landslide` | `legal-and-property-services` | `lifestyle` |
| `literature-film-and-theater` | `lockdown` | `logistics-and-transportation` | `lpga` |
| `management-and-consulting` | `manufacturing-and-petroleum-products` | `marathon` | `market` |
| `mass-shooting` | `medical` | `mining-drilling-and-metalwork` | `minor-league` |
| `mlb` | `mls` | `mma` | `monster-truck` |
| `motocross` | `motogp` | `movie` | `music` |
| `music-and-dance` | `nascar` | `nature-and-outdoor-activities` | `nba` |
| `nba-gleague` | `nba-summer-league` | `ncaa` | `nfl` |
| `nhl` | `nightlife` | `nuclear` | `observance` |
| `observance-local` | `observance-season` | `observance-united-nations` | `observance-worldwide` |
| `olympic` | `online-session` | `other` | `outdoor` |
| `outdoor-sports` | `parade` | `parliament` | `performing-arts` |
| `personal-care-closed` | `personal-care-open` | `pga` | `pop` |
| `post-season` | `pre-season` | `president` | `rain` |
| `rallies` | `recreation-closed` | `recreation-open` | `referendum` |
| `regular-season` | `religion` | `religion-and-spirituality` | `restaurant-closed` |
| `restaurant-open` | `retail-closed` | `retail-open` | `rock` |
| `rodeo` | `rugby` | `running` | `sand` |
| `science-and-technology` | `shooting` | `skating` | `snow` |
| `soccer` | `softball` | `sport` | `sport-fundraiser` |
| `sport-marine` | `sports-and-gaming` | `spring-holiday` | `stabbing` |
| `storm` | `storm-surge` | `summer-holiday` | `suspected-attack` |
| `suspected-bombing` | `table-tennis` | `tennis` | `terror-politics` |
| `terror-tourism` | `terror-transportation` | `terror-travel` | `textile` |
| `thanksgiving-holiday` | `thunderstorm` | `tornado` | `training` |
| `transportation` | `triathlon` | `tropical-storm` | `tsunami` |
| `typhoon` | `vehicle-accident` | `visual-art` | `volcano` |
| `volleyball` | `weather-warning` | `wellness` | `wildfire` |
| `wind` | `winter-holiday` | `wnba` | `worship-closed` |
| `worship-open` | `wrestling` | `wwe` | `youth-sport` |

### Labels (Legacy)

Legacy labels are still returned in order to preserve backward compatibility with existing user implementations.

This field is named `labels`.&#x20;

Legacy labels are available for all event categories but are only available to customers who already had access. Download the full list of legacy label values: [legacy-labels.csv](https://raw.githubusercontent.com/predicthq/gitbook-tech-docs/main/assets/legacy-labels.csv).

### Usage

* [Labels in the Events API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events)
