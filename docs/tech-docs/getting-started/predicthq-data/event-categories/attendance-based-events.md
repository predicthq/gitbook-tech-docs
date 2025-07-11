---
description: >-
  Attended Events are gatherings with a start and end date/time, where people
  come together in one location for entertainment or business.
---

# Attendance-Based Events

## Categories

### Sports

A sports competition consists of multiple players or teams. It has a certain theme or goals with its own rules to regulate and a dedicated environment as well.

#### **Labels**

Labels for a sports event provide more information about the type, league, and environment.

1.  **Sports Type**

    The most common sports types in PredictHQ dataset are: `soccer`, `basketball`, `ice-hockey`, `rugby`, `baseball`.
2.  **Sports League**

    The most popular sports leagues in the PredictHQ dataset are: `NFL`, `MLB`, `NHL`, `NBA`.
3.  **Sports Games Environment**

    The general environment where the sports game is held, or the purpose of the sports game, for example:

    * `closed-doors`: When the sports game has no physical audience in attendance. This is most commonly due to COVID-19 restrictions.
    * `outdoors`: Where the sports game is held in an outdoor area.
    * `fundraise`: A community-related sports game for fundraising purposes.
4. **Youth Sports**
   * These events have the `youth-sport` label
   * These events are defined as any sports event where competitors are younger than adult age, whether children or adolescents. Youth sports include school sports at primary and secondary level, as well as sports played outside the education system, whether informally or organized. They do not include colleague sports which are separate and can be cound with the `NCAA` label.
   * Sports covered are youth basketball, baseball, softball and soccer
   * These events are for the US (with a very small amount in Canada)
   * Youth sports include a new dynamic ranking model that predicts attendance and rank based on the type of sport, age group, level, gender, population density, student numbers, and other features

#### Date & Time

<table><thead><tr><th width="220.33333333333331">Date &#x26; Time Field</th><th width="158" align="center">Availability</th><th>Notes</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td></td></tr><tr><td>End date</td><td align="center">Yes</td><td></td></tr><tr><td>Start time</td><td align="center">Yes</td><td>Sports games are expected to have a specific start time.</td></tr><tr><td>End time</td><td align="center">Yes</td><td></td></tr><tr><td><a href="../predicted-end-times.md">Predicted end time</a></td><td align="center">Yes</td><td>For sports events where there is no official end time available, PredictHQ predicts end times using our machine learning models and intelligent algorithms.<br><br>PredictHQ’s Predicted End Times feature provides end times in the <code>predicted_end</code> field. When a predicted end time is provided, the event’s end time (in the <code>end</code> field) is set to be the same as the start time (in the <code>start</code> field).</td></tr><tr><td>Timezone</td><td align="center">Yes</td><td></td></tr></tbody></table>

Note: datetime is in UTC.

#### Location

Sports events are usually point events, meaning the latitude and longitude of the event represent the location of the event’s venue. The event can also impact an area or region, for example, the location of the [2016 Rio Summer Olympics](https://events.predicthq.com/events/VMDqfHDg3PAbxL3PXh) is the state of Rio de Janeiro.

#### Entities

Sports events have event group entities and venue entities available.

#### Ranking

**PHQ Rank**

Sports events have PHQ Rank available.

**Local Rank**

Sports events have Local Rank available.

**PHQ Attendance**

Sports events have PHQ Attendance available.

### Conferences

A formal meeting or forum relating to a certain topic between a group of people with shared interests. A major conference, especially an industry-related one, may last for several days and occur with regular frequency. An example of an annually occurring conference is the [ASH Annual Meeting](https://events.predicthq.com/events/2RxTdCucMNcLZSsEqW).

**LABELS**

Labels for a conference event provide more information about the event. The most common 5 labels are:

1. `business`: The conferences for a commercial purpose, for example, [Dreamforce](https://events.predicthq.com/events/HAnRjF9RUX8yFnWuGv) by Salesforce.
2. `education`: The conferences for an educational purpose, for example, [Young Social Innovators of the Year Awards](https://events.predicthq.com/events/XoEPm68yHWWNw9ysDp).
3. `health`: The conferences related to the health industry, for example, [CIOSP - Congresso Internacional de Odontologia de São Paulo](https://events.predicthq.com/events/kJ76dr1RmWPP).
4. `technology`: The conferences related to the technology topic, for example, [FPD China](https://events.predicthq.com/events/YEKd1jV29rjV).
5. `science`: The conferences related to the scientific topic, for example, [IAPM ASM](https://events.predicthq.com/events/RSJcHToM4Jy5MQcHZJ).

#### Date & Time

<table><thead><tr><th width="232">Date &#x26; Time Fields</th><th width="144.33333333333331" align="center">Availability</th><th>NOTES</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td></td></tr><tr><td>End date</td><td align="center">Yes</td><td></td></tr><tr><td>Start time</td><td align="center">Yes</td><td>Conferences are expected to have a specific start time.</td></tr><tr><td>End time</td><td align="center">Yes</td><td></td></tr><tr><td>Timezone</td><td align="center">Yes</td><td></td></tr></tbody></table>

Note: datetime is in UTC.

#### Location

Conferences events are point events, meaning the latitude and longitude of the event represents the location of the event’s venue. The smaller size conferences are usually held in a hotel, and the large conferences in convention centers.

#### Entities

Conference events have event group entities and venue entities available.

#### Ranking

**PHQ Rank**

Conference events have PHQ Rank available.

**Local Rank**

Conference events have Local Rank available.

**PHQ Attendance**

Conference events have PHQ Attendance available.

### Expos

An industrial exhibition for communicating and trading purpose between business, or a trade fair that connects business and customers.

**LABELS**

Labels for an expo event provide more information about the event. The most common 5 labels are:

1. `education`: The expos for an educational purpose or education-related topics, for example, [Riyadh International Book Fair](https://events.predicthq.com/events/cL7mv3QVd4PAwaRbvU).
2. `technology`: The expos related to topics in technology, for example, [IIMS - Indonesia International Motor Show](https://events.predicthq.com/events/SDxxc8XymZGYWZ6nrX).
3. `performing-arts`: The shows or fairs that have live performances or are art-related, for example, [Wizard World Comic Con](https://events.predicthq.com/events/i3VNEqMuZKpXUoBusH), and [Saint Louis Art Fair](https://events.predicthq.com/events/9uQWg42s8RziqNxPQb).
4. `entertainment`: The shows or fairs for entertainment purposes, for example, [The Big E (The Eastern States Exposition)](https://events.predicthq.com/events/gPmLe5eSMCbjLnYWCg).
5. `career`: A career or job fair that includes a number of businesses as well large numbers of candidates , for example, [HKTDC Education & Careers Expo](https://events.predicthq.com/events/ZkwcdaWxiMtbKZMrPK).

#### Date & Time

<table><thead><tr><th width="235">Date &#x26; Time Fields</th><th width="172" align="center">Availability</th><th>Notes</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td></td></tr><tr><td>End date</td><td align="center">Yes</td><td></td></tr><tr><td>Start time</td><td align="center">Yes</td><td></td></tr><tr><td>End time</td><td align="center">Yes</td><td></td></tr><tr><td>Timezone</td><td align="center">Yes</td><td></td></tr></tbody></table>

Note: datetime is in UTC.

#### Location

Expos events are point events, meaning the latitude and longitude of the event represents the location of the event’s venue. Expos are usually held in venues that can fit a large number of attendees such as a convention center.

#### Entities

Expos events have event group entities and venue entities available.

#### Ranking

**PHQ Rank**

Expos events have PHQ Rank available.

**Local Rank**

Expos events have Local Rank available.

**PHQ Attendance**

Expos events have PHQ Attendance available.

### Concerts

A musical performance where the primary intention of attendance is to see the musical artist or listen to music. Concerts usually last less than one day. Examples are a large [Eminem](https://events.predicthq.com/events/aYR4t59pGHA92FtNgK) concert, or a smaller nightclub event, for example, [Darude At Hq2 Nightclub Atlantic City](https://events.predicthq.com/events/xx8TPFE7XNh5pdxyRX).

**LABELS**

All concert events have a `music` label as concert events are expected to be music-related.

#### Date & Time

<table><thead><tr><th width="242">Date &#x26; Time Fields</th><th width="120.33333333333331" align="center">Availability</th><th>Notes</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td></td></tr><tr><td>End date</td><td align="center">Yes</td><td></td></tr><tr><td>Start time</td><td align="center">Yes</td><td>Concerts are expected to have a specific start time</td></tr><tr><td>End time</td><td align="center">Yes</td><td></td></tr><tr><td><a href="../predicted-end-times.md">Predicted end time</a></td><td align="center">Yes</td><td>For concert events where there is no official end time available, PredictHQ predicts end times using our machine-learning models and intelligent algorithms.<br><br>PredictHQ’s Predicted End Times feature provides end times in the <code>predicted_end</code> field. When a predicted end time is provided, the event’s end time (in the <code>end</code> field) is set to be the same as the start time (in the <code>start</code> field).</td></tr><tr><td>Timezone</td><td align="center">Yes</td><td></td></tr></tbody></table>

Note: datetime is in UTC.

#### Location

Concerts events are point events, meaning the latitude and longitude of the event represent the location of the event’s venue.

#### Entities

Concerts events have event group entities and venue entities available.

#### Ranking

**PHQ Rank**

Concerts events have PHQ Rank available.

**Local Rank**

Concerts events have Local Rank available.

**PHQ Attendance**

Concerts events have PHQ Attendance available.

### Festivals

A commonly known day or a period of time when people gather together to celebrate a specific reason; or a day or a period of time consisting of an organized series of shows and entertainment activities Festivals typically occur on a certain frequency. For example, the [Yosakoi Soran Festival](https://events.predicthq.com/events/ScR7u7EZSBuxZ8kK9J) is held annually.

**LABELS**

Labels for a festival event provide more information about the festival. The most common 5 labels are:

1. `music`: Music festivals when a large group of musical artists continuously perform over several days. Music festivals are usually held at a dedicated venue that can fit a large number of attendees, for example, the [Ultra Music Festival](https://events.predicthq.com/events/duHrbmUbpFSgwypGAK).
2. `performing-arts`: The festivals that consist of performing shows such as a costume parade or a fireworks show. Such festivals could feature traditional music, theatre, poetry and art. For example, the [National Festival of Popular Arts in Marrakech](https://events.predicthq.com/events/cxSrjK82oWZGUWUvUJ).
3. `family`: The festivals which are family-friendly and children-friendly, for example, [Magnificent Mile Lights Festival](https://events.predicthq.com/events/vFQK4H3yaujGqwnR4z).
4. `community`: Traditional festivals in the local area. Community festivals are less formal than world-wide festivals and may also include street markets and entertainment activities. The [Odunde Festival](https://events.predicthq.com/events/dkbGjQW943KSL5hT8b) is an example of a community festival.
5. `food`: Food festivals where communities or businesses trade food products, for example, [Bite of Seattle](https://events.predicthq.com/events/QDgCysY3kMnpoGYFi9).

#### Date & Time

<table><thead><tr><th width="253">Date &#x26; Time Fields</th><th width="152.33333333333331" align="center">Availability</th><th>Notes</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td></td></tr><tr><td>End date</td><td align="center">Yes</td><td></td></tr><tr><td>Start time</td><td align="center">Yes</td><td></td></tr><tr><td>End time</td><td align="center">Yes</td><td></td></tr><tr><td>Timezone</td><td align="center">Yes</td><td></td></tr></tbody></table>

Note: datetime is in UTC.

#### Location

A festival event can be a point event or an area event. The latitude and longitude of a point event represents the location of the venue where the festival takes place. The latitude and longitude of an area event is the geometric center of the area of the festival - either the area impacted by the festival, or an area where the festival takes place since its location is not fixed. An example of a festival without a fixed location is the [Norwich St. Patrick’s Day Parade and Festival](https://events.predicthq.com/events/w5PNZxwvKAKLGXGrae).

#### Entities

Festival events have event group entities and venue entities available.

#### Ranking

**PHQ Rank**

Festival events have PHQ Rank available.

**Local Rank**

Festival events have Local Rank available.

**PHQ Attendance**

Festival events have PHQ Attendance available.

### Performing Arts

A show or an exhibition of creative activities for an audience, for example, [a circus show](https://events.predicthq.com/events/EHKbvvKhLnVonwUUbD).

**EVENT TYPES**

The most common 5 types of performing-arts events are:

1.  **General Theatre**

    Theatre plays, for example, [The Nutcracker ballet show](https://events.predicthq.com/events/wunsQfMcMgbB2wXedq).
2.  **Comedy club**

    Standup comedy shows, for example, [Eddie Izzard - Wunderbar World Tour](https://events.predicthq.com/events/k2bibyMXE4B42EECnv).
3.  **Concert**

    Musical plays, for example, A [symphony](https://events.predicthq.com/events/MeswVtp3dMccSx5jEs), or an [opera](https://events.predicthq.com/events/ah6hg4UorgsaJ2PSFY), etc.
4.  **Family Theatre**

    Shows or plays where the main audience are children, for example, [Magic On Ice](https://events.predicthq.com/events/8QJfuDQeqrKQftBnB3), a [dubbing show](https://events.predicthq.com/events/sjg2xuf27oeLQLrbpt), etc.
5.  **Cultural Performances**

    Traditional or cultural activities, for example, [Sewing & Quilt Expo](https://events.predicthq.com/events/NCErdrvw9R69ocqES9), a [poetry slam](https://events.predicthq.com/events/CEE7SzC2CmrWSbbDe4), etc.

#### Date & Time

<table><thead><tr><th width="238">Date &#x26; Time Fields</th><th width="150.33333333333331" align="center">Availability</th><th>Notes</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td></td></tr><tr><td>End date</td><td align="center">Yes</td><td></td></tr><tr><td>Start time</td><td align="center">Yes</td><td>Performing-arts events are expected to have a specific start time</td></tr><tr><td>End time</td><td align="center">Yes</td><td></td></tr><tr><td><a href="../predicted-end-times.md">Predicted end time</a></td><td align="center">Yes</td><td>For performing arts events where there is no official end time available, PredictHQ predicts end times using our machine-learning models and intelligent algorithms.<br><br>PredictHQ’s Predicted End Times feature provides end times in the <code>predicted_end</code> field. When a predicted end time is provided, the event’s end time (in the <code>end</code> field) is set to be the same as the start time (in the <code>start</code> field).</td></tr><tr><td>Timezone</td><td align="center">Yes</td><td></td></tr></tbody></table>

Note: datetime is in UTC.

#### Location

Performing-arts events are point events meaning the latitude and longitude of the event is for the location of the event’s venue. Venues for these events are usually theatres, playgrounds, or clubs, etc.

#### Entities

Performing-arts events have event group entities and venue entities available.

#### Ranking

**PHQ Rank**

Performing-arts events have PHQ Rank available.

**Local Rank**

Performing-arts events have Local Rank available.

**PHQ Attendance**

Performing-arts events have PHQ Attendance available.

### Community

This category includes various types of events, for example, a [college event](https://events.predicthq.com/events/7diCQtRZ5XQdso27v3), a [community party](https://events.predicthq.com/events/pS49Cvk4tiSPKdEAJ8), an [auction](https://events.predicthq.com/events/iC5BK62w3z9CLpqvif), or a [fan meeting](https://events.predicthq.com/events/CnNAFhLqffMQMsqg4R).

**LABELS**

Labels for a community event provide more information about the event. The most common 5 labels are:

1. `music`, `concert`: Social events with musical activity, for example, a [karaoke at a bar](https://events.predicthq.com/events/TvzBomhs9m6JAdKRr3).
2. `family`: Community events which are children and family-friendly, for example, a [book club breakfast in the library](https://events.predicthq.com/events/3pTSHhuXjQErhg9nwu).
3. `food`: Social events about food or have food provided, for example, a [wine tasting event](https://events.predicthq.com/events/hk9SqnMEk2ywVAyQb9).
4. `education`: Informal training workshops or clubs that consist of a group of people that share the same interest, for example, an [installation art workshop](https://events.predicthq.com/events/9sGedbBiSzq74ERvkS).
5. `fundraiser`: Community [fundraising](https://events.predicthq.com/events/U7nFaVDxKEh6RAD5UD) events.

#### Date & Time

<table><thead><tr><th width="243">Date &#x26; Time Fields</th><th width="141.33333333333331" align="center">Availability</th><th>Notes</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td></td></tr><tr><td>End date</td><td align="center">Yes</td><td></td></tr><tr><td>Start time</td><td align="center">Yes</td><td></td></tr><tr><td>End time</td><td align="center">Yes</td><td></td></tr><tr><td>Timezone</td><td align="center">Yes</td><td></td></tr></tbody></table>

Note: datetime is in UTC.

#### Location

A community event is a point events meaning the latitude and longitude of the event represents the location of the event’s venue.

#### Entities

Community events have event group entities and venue entities available.

#### Ranking

**PHQ Rank**

Community events have PHQ Rank available.

**Local Rank**

Community events have Local Rank available.

**PHQ Attendance**

Community events have PHQ Attendance available.

### Academic

Academic Events are captured from an individual higher education institute’s academic calendar. They outline the general undergraduate activities, for example instruction period, break, exams, graduation, social, etc.

Note:

* Academic Events currently covers institutions where full-time undergraduate enrollment (or FTE, full-time equivalent) is over 5,000. The student number is campus-based instead of the overall enrollment across different locations.
* Academic Events currently covers institutions in US and top 20 institutions in UK. In future it will expand to other countries.

**LABELS / EVENT TYPES**

The Academic Events category has six main event types affecting students’ activities. The dates are retrieved from the official academic calendar and/or estimated based on the pattern. The estimated date will have an additional `estimated` label.

1. **Academic-session**
   * The compulsory academic session for students to graduate upon completion.
   * Session starts on the first day of instruction and ends on the last day of instruction.
   * Orientation, reading days, and exams are not included.
   * Session events are labeled with `academic` and `academic-session`.
   * Intensive session, the optional academic session between the normal sessions for earlier graduation where the compulsory term is not applied, is also included in this event type.
2. **Exam**
   * The exam period for the academic session.
   * Exam starts on the first day of the exam period and ends on the last day of the exam period
   * No separate exam period for the intensive session.
   * Reading days are not included.
   * Exam event is labeled with `academic` and `exam`.
3. **Holiday**
   * The break/holiday period between the sessions or within the sessions.
   * Holiday events consist of:
     * Fall break
     * Thanksgiving break
     * Winter break
     * Spring break
     * Summer break
   * Holiday events don’t cover the public holidays such as Labor day, Easter holiday, Martin Luther King Jr. Day, etc as we already have the public holiday and observance categories.
   * Holiday events cover the Thanksgiving break because institutions may have a different schedule, e.g. 9 days vs 4 days.
   * Holiday events start on the day after the instruction / exam finishes and ends before the following instruction starts.
   * Winter and summer breaks may overlap with intensive sessions as the break will affect the majority of students while the intensive session only affects a few.
   * Holiday events are labeled with `academic` and`holiday`.
4. **Graduation**
   * Graduation (also called commencement) date for undergraduate students.
   * Graduation events may have a specific start time where applicable.
   * Graduation venues may be outside the campus.
   * Graduation events include the institute’s name in the title.
   * Graduation events are labeled with `academic` and `graduation`.
5. **Social**
   * Social events currently cover homecoming where alumni come back to the campus to visit.
   * Homecoming events may last up to a week.
   * Parent/family day/weekend may be included in the future.
   * Social events is labeled with `academic` and `social`.

#### Date & Time

<table><thead><tr><th width="230.33333333333331">Date &#x26; Time Fields</th><th width="138" align="center">Availability</th><th>Notes</th></tr></thead><tbody><tr><td>Start date</td><td align="center">Yes</td><td></td></tr><tr><td>End date</td><td align="center">Yes</td><td>End date will be as same as the start date when it’s not available, e.g. an one day graduation event has end date same as start date</td></tr><tr><td>Start time</td><td align="center">Yes</td><td>Available for graduation and social events only. This is an optional data point and may not always be provided.</td></tr><tr><td>End time</td><td align="center">Yes</td><td>Available for graduation and social events only. This is an optional data point and may not always be provided.</td></tr><tr><td>Timezone</td><td align="center">Yes</td><td></td></tr></tbody></table>

Note: datetime is in UTC.

#### Location

Academic events are tracked as an event with a scope of locality. In terms of geographic information we return a latitude/longitude for the event and the address of the event. However, Academic events can apply to an entire campus or a specific location, e.g. an academic session applies to the whole campus, and a point event, e.g. graduation happens at a specific location. Use labels to distinguish these different types of events. `graduation` and `social` event are point events, `academic-session`, `holiday`, `exam` impact the whole area of the campus.

#### Entities

The Academic events have venue entities available.

#### Ranking

**PHQ Rank**

Academic events have PHQ Rank available.

* Session, exam, and holiday types use student numbers (FTE) to indicate the event’s impact as the events apply on the whole campus.
* Intensive sessions use 30% of the total student numbers (FTE) to indicate the event’s impact as the events apply to only a small population.
* Graduation and social events use the actual number of attendees to indicate the impact.

**Local Rank**

Academic events have no Local Rank available.

**PHQ Attendance**

Academic events have PHQ Attendance available for all event types. PHQ Attendance for `academic-session`, `exam`, and `holiday` event types is based on student population, e.g. the amount of students enrolled in the term. PHQ attendance on `graduation` and `social` events are based on the number of people in attendance at the event.

