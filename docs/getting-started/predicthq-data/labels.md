# Labels

Event labels are succinct descriptive attributes attached to events that can help with **granular data selection** and **feature engineering** use cases.&#x20;

For example, within the Conferences category, knowing the subject(s) covered within the conference (`science-and-technology`, `educational`, `automotive`, etc.) may help you narrow down on events that are relevant to your business.&#x20;

Each event record has two separate label fields (`phq_labels` and `labels`).

All categories have the new `phq_labels` and will be used by default.&#x20;

Event labels can be searched by using the`phq_labels` field.&#x20;

Some `labels` which repeat the category name such as `label: academic` have been removed.

`phq_labels` will be used by default as all legacy labels have been migrated.

### PHQ Labels

PHQ Labels are generated through newer Large Language Models (LLMs) and overall achieve a higher standard of **specificity** and **relevance** in highlighting an event's key themes when compared to legacy methods.

This field is named `phq_labels`.

PHQ Labels are available for the following categories:

* Concerts
* Conferences
* Expos
* Festivals
* Performing Arts
* Community
* Acdemic&#x20;
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

We recommend using [Get Event Counts](../../api/events/get-event-counts.md) to retrieve an **up-to-date and relevant** list of PHQ Labels and the count of events labelled with each, **within your PredictHQ plan**. You could also use [Query Parameters](../../api/events/search-events.md#query-parameters) to retrieve a list and the count of PHQ Labels that match your criteria, e.g. PHQ Labels associated with the sports category or PHQ Labels of events that will be taking place in a specific time and place. Here is an example:

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/count",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    ## optional, get PHQ Labels and counts for sports category only
    # params={"category": "sports"}
)


# get PHQ Labels and the count of events having them from the response
phq_labels = response.json().get("phq_labels")

print(response.json().get("phq_labels"))
# > {'basketball': 408197,'parade': 14327, ... }


```

Alternatively, you could use the list of PHQ Labels below as a reference. Bear in mind some of the PHQ Labels below might not appear in the events within your PredictHQ plans.

<details>

<summary><strong>Possible PHQ Label Values</strong></summary>

* academic-session
* agriculture-forestry-and-fisheries
* air-quality
* airport
* alcohol
* american-football
* animal
* arson
* art-and-cultural
* ashfall
* assassination
* attack
* attraction
* australian-football
* auto-racing
* automotive
* autumn-holiday
* avalanche
* badminton
* baseball
* basketball
* beauty-and-fashion
* bicycle
* biological-hazard
* blizzard
* bombing
* boxing
* campus
* celebration
* charity
* chemical
* chemical-accident
* christmas-holiday
* circus
* civil
* climate-change
* closed-doors
* club
* coastal-event
* cold-wave
* comedy-club
* community
* community-event
* concert
* conference
* construction-and-infrastructure
* consumer-goods
* corporate
* country
* course
* cricket
* cultural
* cultural-performance
* cyclone
* design-and-furnishing
* digital
* dinner-theatre
* disaster-warning
* drought
* dust
* earthquake
* easter-holiday
* education
* education-and-careers
* educational
* election
* electronic
* entertainment
* epidemic
* epidemic-hazard
* esports
* estimated
* exam
* execution
* explosion
* expo
* extreme-weather
* f1
* family
* family-activities
* family-fun
* family-theatre
* fashion
* festival
* festivals-and-outdoor-activities
* fighting
* financial-services
* fire
* flood
* fog
* food
* food-and-beverage
* football
* fundraiser
* gaming
* general-theatre
* golf
* graduation
* gymnastics
* hail
* hazardous-surf
* hazmat
* health
* heat-wave
* hijacking
* hip-hop-and-rnb-and-soul
* hockey
* holiday
* holiday-christian
* holiday-hebrew
* holiday-hindu
* holiday-local
* holiday-local-common
* holiday-muslim
* holiday-national
* holiday-observed
* holiday-orthodox
* holiday-religious
* horse-racing
* hospitality-and-travel
* hostage-crisis
* hurricane
* hybrid-session
* ice-hockey
* in-person-session
* indycar
* ironman
* jazz-and-classical
* landslide
* legal-and-property-services
* lifestyle
* literature-film-and-theater
* lockdown
* logistics-and-transportation
* lpga
* management-and-consulting
* manufacturing-and-petroleum-products
* marathon
* marine
* market
* mass-shooting
* medical
* mining-drilling-and-metalwork
* minor-league
* mlb
* mls
* mma
* monster-truck
* motocross
* motogp
* movie
* music
* music-and-dance
* nascar
* nature-and-outdoor-activities
* nba
* nba-gleague
* ncaa
* nfl
* nhl
* nightlife
* observance
* observance-local
* observance-season
* observance-united-nations
* observance-worldwide
* olympic
* online-session
* other
* outdoor
* outdoor-sports
* parade
* parliament
* performing-arts
* pga
* politics
* pop
* president
* rain
* rallies
* referendum
* religion
* religion-and-spirituality
* research-development
* rock
* rodeo
* rugby
* running
* sales
* sand
* school
* science-and-technology
* shooting
* skating
* snow
* soccer
* social
* sport
* sports-and-gaming
* spring-holiday
* stabbing
* storm
* storm-surge
* summer-holiday
* suspected-attack
* suspected-bombing
* table-tennis
* technology
* tennis
* textile
* thanksgiving-holiday
* thunderstorm
* tornado
* tourism
* training
* transportation
* travel
* triathlon
* tropical-storm
* tsunami
* typhoon
* vehicle-accident
* visual-art
* volcano
* volleyball
* weather-warning
* wellness
* wildfire
* wind
* winter-holiday
* wnba
* wrestling
* wwe
* youth-sport

</details>

### Labels (Legacy)

Legacy labels are still returned in order to preserve backwards compatibility with existing user implementations.

This field is named `labels`

Legacy labels are available for all event categories.



### Usage

* [Labels in the Events API](../../api/events/search-events.md#query-parameters)
