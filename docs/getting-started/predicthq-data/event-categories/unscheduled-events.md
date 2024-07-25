---
description: >-
  Live coverage of breaking events such as severe weather and terrorism. The API
  updates minute to minute to ensure accuracy.
---

# Unscheduled Events

## Categories

### Severe Weather

Severe weather is any dangerous meteorological phenomenon with the potential to cause damage, serious social disruption, or loss of human life. Types of severe weather phenomena vary, depending on the latitude, altitude, topography, and atmospheric conditions.

Severe weather warnings or alerts which may lead to disruption. Severe weather alerts include storms, extreme temperature, flood, etc. For example, a [tornado warning](https://control.predicthq.com/search/events/v3xwuouU62ZEzXhxWC) for southeastern Webster Parish in northwestern Louisiana alerts people that a severe thunderstorm along with damage in the nearby area is likely to occur in the upcoming hour.

Severe weather storm events can change over time. Events like hurricanes, tornados and other storms move across different locations and change in strength as time goes on. This can be reflected by different warning events in our system. It’s possible to have multiple warnings about the same weather condition:

* The bad weather condition lasts longer than expected. For example, a [flood advisory was issued at 11.48 AM](https://control.predicthq.com/search/events/jZEkmbAYqntSRo4Xgs) in east Tennessee that the potential threat may last until 3 PM. Another [flood advisory issued at 3.02 PM](https://control.predicthq.com/search/events/fxZjGT5Ehoe7brsCjd) that indicates additional rainfall may occur on the day and the following day, and the road closures will remain in place.
* Multiple areas can be affected. For example, On March 14th, several regions in South Dakota have issued blizzard warnings, such as [Oglala Lakota](https://control.predicthq.com/search/events/tTjDpN7ZR2WVhzw47o), [Pennington](https://control.predicthq.com/search/events/ubp47jnAvuwos5fanc), [Fall River](https://control.predicthq.com/search/events/74ucjeYRYWG89Sw5rS), and [Custer](https://control.predicthq.com/search/events/6y3py8CPSLfeN29DYq).
* Warnings may be issued hours or days in advance. The event (warning) state will change to `cancelled` if the potential threat no longer exist. For example the storm didn't hit as expected. Past events with an `active` state mean the event has happened.
* Severe weather data is updated in near real time with event details being refreshed on average every 15 mins.
* PredictHQ provides historical severe weather data that can be used for purposes like training a demand forecasting model.

**LABELS**

This category is classified into three buckets with the following labels used to identify the type of severe weather.

1.  **Storm**

    `storm`, `tornado`, `blizzard`, `dust`, `hurricane`, `cyclone`, `rain`, `wind`, `typhoon`, `sand`
2.  **Extreme Temperature**

    `cold-wave`, `heat-wave`, `air-quality`, `snow`
3.  **Flood**

    `flood`

#### Date & Time

<table><thead><tr><th width="221.33333333333331">Date &#x26; Time Field</th><th width="144" align="center">Availability</th><th>Notes</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td></td></tr><tr><td>End date</td><td align="center">Yes</td><td></td></tr><tr><td>Start time</td><td align="center">Yes</td><td>The weather warnings’ start time indicate when the warning starts to be effective.</td></tr><tr><td>End time</td><td align="center">Yes</td><td>The weather warnings’ end time indicate when the warning expires.</td></tr><tr><td>Timezone</td><td align="center">Yes</td><td></td></tr></tbody></table>

Note: Datetime is in UTC

#### Location

Severe weather is an area event. with the latitude and longitude is pointing to the center of the impacted area.

#### Entities

Severe weather events have no entities available.

#### Ranking

**PHQ Rank**

Severe weather events have PHQ Rank available.

The PHQ Rank indicates the severity of the bad weather, with using the [Common Alerting Protocol (CAP)](https://en.wikipedia.org/wiki/Common\_Alerting\_Protocol) data. CAP is an international non-proprietary digital message format for all-hazard emergency events. The benefit of using CAP is there is consistency in how it is implemented in different countries, making it easier to use. CAP alerts can be geographically targeted to a defined warning area.

CAP features evaluate the event from three aspects: urgency, severity and certainty. For example, a warning about an extreme (severity) weather condition that is likely (certainty) to happen immediately (urgency) will have a higher rank. The table below shows the weight of each value of severity, urgency, and certainty when calculating the PHQ Rank.

For example, An event with an urgency of immediate (15), a severity of severe (36), and a certainty of observed (35) would have a PHQ Rank of 86.

<table><thead><tr><th width="148">CAP Type</th><th width="175">Level</th><th width="316">Description</th><th>Weight</th></tr></thead><tbody><tr><td>Urgency</td><td><ul><li>Immediate</li><li>Expected</li><li>Future</li><li>Past</li></ul></td><td><ul><li>Responsive action should be taken immediately</li><li>Responsive action should be taken soon (within next hour)</li><li>Responsive action should be taken in the near future</li><li>Responsive action is no longer required</li></ul></td><td><ul><li>15</li><li>13</li><li>10</li><li>8</li></ul></td></tr><tr><td>Severity</td><td><ul><li>Extreme</li><li>Severe</li><li>Moderate</li><li>Minor</li></ul></td><td><ul><li>Extraordinary threat to life or property</li><li>Significant threat to life or property</li><li>Possible threat to life or property</li><li>Minimal to no known threat to life or property</li></ul></td><td><ul><li>40</li><li>36</li><li>21</li><li>5</li></ul></td></tr><tr><td>Certainty</td><td><ul><li>Observed</li><li>Likely</li><li>Possible</li><li>Unlikely</li></ul></td><td><ul><li>Determined to have occurred or to be ongoing</li><li>Likely</li><li>Possible but not likely</li><li>Not expected to occur</li></ul></td><td><ul><li>35</li><li>31</li><li>10</li><li>0</li></ul></td></tr></tbody></table>

**Local Rank**

Severe weather events have no Local Rank available as they impact an entire area instead of a specific point.

**PHQ Attendance**

Severe weather events have no PHQ Attendance available as the rank/impact only reflects its influence on an area, rather than a specific amount of attendees at a specific location.

### Disasters

Disaster events are major adverse events resulting from natural processes of the Earth, for example, earthquakes, volcanoes, tsunamis, etc. The reduction and/or limitation of social activities that are forced by COVID-19 pandemic is also classified under the disaster category.

These events tend to be high-impact disasters noticed at a regional or country level.

**Labels**

This category is classified into three buckets with the following labels used to identify the type of disasters.

1.  **Hydrological\_geophysical**

    `earthquake`, `avalanche`, `landslide`, `volcano`, `tsunami`, `ashfall`\
    \
    Note: Earthquake coverage typically includes magnitude 4 and above earthquakes.\

2.  **Climatological**

    `fire`, `wildfire`, `drought`
3.  **Lockdown**

    The government mandated stay-at-home orders during the COVID-19 pandemic that restrict or reduce social activities on different levels. Lockdown events have `health`, `lockdown` and `disaster` labels. For example, [COVID-19 - Lockdown easing - Portugal](https://control.predicthq.com/search/events/ydXTVviY5KQty98UfD), [COVID-19 - Stay at home order easing - Michigan - Phase 4](https://control.predicthq.com/search/events/Vat8acyAFAXQaNNTaK).

#### Date & Time

<table><thead><tr><th width="225.33333333333331">Date &#x26; Time Field</th><th width="146" align="center">Availability</th><th>Notes</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td></td></tr><tr><td>End date</td><td align="center">Yes</td><td>Disaster events may or may not have an end date &#x26; time.</td></tr><tr><td>Start time</td><td align="center">Yes</td><td></td></tr><tr><td>End time</td><td align="center">Yes</td><td></td></tr><tr><td>Timezone</td><td align="center">Yes</td><td></td></tr></tbody></table>

Note: Datetime is in UTC

#### Location

Disaster is an area event with the latitude and longitude pointing to the center of the impacted area.

#### Entities

Disaster events have no entities available.

#### Ranking

**PHQ Rank**

Disaster events have PHQ Rank available, which indicates the severity of the disasters.

* The natural disaster events consider [CAP](https://en.wikipedia.org/wiki/Common\_Alerting\_Protocol) information, number of injured, deaths, evacuated, etc.
* The lockdown events consider the level of restriction, the maximum number of people allowed in a public social gathering, etc.

**Local Rank**

Disaster events have no Local Rank available as they impact an entire area instead of a specific point.

**PHQ Attendance**

Disasters events have no PHQ Attendance available as the rank/impact only reflects its influence on an area, rather than a specific amount of attendees at a specific location.

### Airport Delays

Airport delays are events that indicate a scheduled flight getting delayed at a specified airport at a specified time.

**Labels**

All airport delays events have both `airport` and `delay` labels.

#### Date & Time

<table><thead><tr><th width="215.33333333333331">Date &#x26; Time Field</th><th width="141" align="center">Availability</th><th>Notes</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td></td></tr><tr><td>End date</td><td align="center">Yes</td><td></td></tr><tr><td>Start time</td><td align="center">Yes</td><td></td></tr><tr><td>End time</td><td align="center">Yes</td><td>All airport delays events are expected to have an end time as it indicates when the delay is expired.</td></tr><tr><td>Timezone</td><td align="center">Yes</td><td></td></tr></tbody></table>

Note: Datetime is in UTC

#### Location

All airport delays are point events, the latitude and longitude are pointing to the specific airport.

#### Entities

Airport delays have venue entities available.

#### Ranking

**PHQ Rank**

Airport delays events have PHQ Rank available, indicating the severity of the delay that affects passengers’ travel plans.

* Minimal airport delays events have a PHQ Rank of 20.
* Moderate airport delays events have a PHQ Rank of 40.
* Significant airport delays events have a PHQ Rank of 70.
* Severe airport delays events have a PHQ Rank of 90.

**Local Rank**

Airport delays events have no Local Rank available as they impact an entire area instead of a specific point. To be specific, the fact of the flight delay happens in an airport, but the impact is applying to a region where the passengers are from.

**PHQ Attendance**

Airport delays events have no PHQ Attendance available as the rank/impact only reflects its influence on an area, rather than a specific amount of attendees at a specific location.

### Health Warnings

This category will cover events related to infectious diseases. Some events will refer to localised outbreaks, some to nationwide epidemics, some to government mandated restrictions due to COVID-19.

Labels

This category is classified into three buckets with the following labels used to identify the type of health warnings.

1.  **Epidemic**

    Pandemic, `epidemic` or `epidemic-hazard`, for example, COVID-19, Cholera, etc
2.  **`biological-hazard`**

    Diseases and insect infestations, for example, food poisoning warnings, infection warnings, etc.
3.  **Government mandated restrictions**

    There are seven government mandated events in the US on a state level. These events indicate if a government body has mandated that the activity stays open or closed during a specified period of time.

    If no end time is specified on government mandated restriction events, the event has yet to end.

    * `bars-open` / `bars-closed` : Bars and other drinking establishment that serves alcoholic beverages are open or closed.
    * `restaurant-open` / `restaurant-closed` : On-site dining facilities are open or closed.
    * `retail-open` / `retail-closed` : On-premise / physical activity of selling goods and services to consumers are open or closed.
    * `recreation-open` / `recreation-closed` : Activity or recreation engaged in out of doors, most commonly in natural settings (gyms, pools, beaches, camping grounds) are open or closed.
    * `entertainment-open` / `entertainment-closed` : an event, performance, location or activity designed to entertain others (casinos, movie theaters, museums, galleries and aquariums) are open or closed.
    * `personal-care-open` / `personal-care-closed` : Both physical assistance and/or prompting and supervising the performance of direct personal care tasks as determined by the consumer's needs (salons, barbers, nail salons) are open or closed.
    * `worship-open` / `worship-closed` : Any building where congregations gather for prayer are open or closed.

#### Date & Time

<table><thead><tr><th width="224.33333333333331">Date &#x26; Time Field</th><th width="138" align="center">Availability</th><th>Notes</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td></td></tr><tr><td>End date</td><td align="center">Yes</td><td>Government mandated restrictions may have an end date if it’s available, it should cover the whole period in which restrictions are in place or have been lifted.</td></tr><tr><td>Start time</td><td align="center">Yes</td><td>The pandemic or epidemic hazard events use the official announcement time as the start time.</td></tr><tr><td>End time</td><td align="center">No</td><td></td></tr><tr><td>Timezone</td><td align="center">Yes</td><td></td></tr></tbody></table>

Note: Datetime is in UTC

#### Location

Health warnings events are area events. It may scope to a city, a region or a country depending on the impact. The latitude and longitude relates to the center of the impacted area.

#### Entities

Health warnings events have no entities available.

#### Ranking

**PHQ Rank**

Health warnings events have PHQ Rank available.

* It considers the severity of the disease, for example, the number of infected, death, area range, etc.
* All government mandated restrictions have a PHQ Rank of 90 as it affects all residents in the impacted area.

**Local Rank**

Health warnings events have no Local Rank available as they impact an entire area instead of a specific point.

**PHQ Attendance**

Health warnings events have no PHQ Attendance available as the rank/impact only reflects its influence, rather than a specific amount of attendees at a specific location.

### Terror

An act of terrorism committed using violence against civilians, with the intention/effect of causing mass / widespread fear and intimidation, in order to attain political, religious or ideological goals.

**Note** attempted (but failed) terror attacks are also included. This category focuses more in areas outside of designated warzones, as war zones are in a constant state of conflict.

**Labels**

Labels for a terror event provide more information about the event. The most common 5 labels are:

1. `attack`: An aggressive and violent act against a person or place with weapons or armed force.
2. `bombing` : The terrorism acts where the main injury or damage is caused by dropping or detonating a bomb somewhere, for example, [Bombing in Lahan, Nepal](https://control.predicthq.com/search/events/hnCL2axLWVJZyBN2AV).
3. `arson`: The terrorism acts also result in a fire damage, it may it may be combined with a `shooting`, `bombing`, etc.
4. `hostage-crisis`: The terrorism acts when the hostage occurs, for example, [`assassination`](https://control.predicthq.com/search/events/ywfjG46u6KDmkqqsAa), a terror threat, etc.
5. `shooting`: The terrorism acts where the main injury or damage is caused by shooting, for example, [Shooting in Sonwar, India](https://control.predicthq.com/search/events/X6D8sz2i7qWZ3VMpFh). If the shooting is on a larger scale, the `mass-shooting` label will be added, for example, [Shooting in Chicago, United States](https://control.predicthq.com/search/events/FtzZisWG6r8KZRp9Gp).

#### Date & Time

<table><thead><tr><th width="212.33333333333331">Date &#x26; Time Field</th><th width="151" align="center">Availability</th><th>Notes</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td></td></tr><tr><td>End date</td><td align="center">Yes</td><td>Terror events may have an end date and time available.</td></tr><tr><td>Start time</td><td align="center">Yes</td><td></td></tr><tr><td>End time</td><td align="center">Yes</td><td></td></tr><tr><td>Timezone</td><td align="center">Yes</td><td></td></tr></tbody></table>

Note: Datetime is in UTC

#### Location

Terror events are tracked as an event with a scope of locality. In terms of geographic information we return a latitude/longitude for the event and the address of the event. However, terror events can apply to a wider area, for example, [attempted bombing in Cipinang, Indonesia](https://control.predicthq.com/search/events/VGG78MrBvgZ4dartjv).

#### Entities

Terror events may have venue entities available such as if the attack happens in a building.

#### Ranking

**PHQ Rank**

Terror events have PHQ Rank available. It indicates the severity of the terrorism act, from the number of injured, fatalities, also if the location is a tourism country vs the war-torn country.

**Local Rank**

Terror events have no Local Rank available as they impact an entire area instead of a specific point. To be specific, the terrorism acts may happen at a specific location, but the impact is applying to all residents in the nearby area.

**PHQ Attendance**

Terror events have no PHQ Attendance available as the rank/impact only reflects its influence on an area, rather than a specific amount of attendees at a specific location.
