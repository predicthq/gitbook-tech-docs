---
description: >-
  Search for events happening in a location and date range. Use our extensive
  filters to narrow down your results.
---

# Search Events



{% hint style="info" %}
&#x20;**Results are limited by your subscription**

Please note that you will not receive an error when requesting a date range or location that is outside of your subscription settings.

This is sometimes confused with missing data. If you're not seeing the results you expect to see then please ensure your subscription covers the location or time period you're searching for.

Your subscription settings can be viewed in [Control Center](https://control.predicthq.com/settings/plans).
{% endhint %}

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/events/
```

### Query parameters

<table><thead><tr><th width="373">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>active.*</code><br>date range</td><td><p>The date range during which events occur. </p><p></p><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes. <code>tz</code> is time zone in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format (default is <code>UTC</code>).<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>. </p><p></p><p>E.g. <code>?active.gte=2015-01-01&#x26;active.lte=2015-03-01</code></p></td></tr><tr><td><code>brand_unsafe.*</code><br>brand-unsafe</td><td><p>Whether or not to <strong>exclude</strong> potentially brand-unsafe events. Potentially brand-unsafe events are included by default.</p><p><br>Currently only supports the <code>exclude</code> suffix.</p><ul><li><code>exclude</code>: whether or not to exclude potentially brand-unsafe events from results (<em>required</em>, valid options are <code>true</code> or <code>false</code>)</li></ul><p>Examples of brand-unsafe events include content that promotes hate, violence or discrimination, coarse language, content that is sexually suggestive or explicit, etc.</p><p><br>Please note that use of a suffix is <strong>required</strong>.</p><p><br>E.g. <code>?brand_unsafe.exclude=true</code></p></td></tr><tr><td><code>cancelled.*</code><br>date range</td><td><p>The date range during which events were marked as cancelled in the system. </p><p></p><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes. <code>tz</code> is time zone in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format (default is <code>UTC</code>).<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>.</p><p><br>E.g. <code>?cancelled.gte=2020-03-01&#x26;cancelled.lte=2020-03-15</code></p><p></p><p>Note when filtering on <code>cancelled</code>, events that are not cancelled will not be returned.</p></td></tr><tr><td><code>category</code><br>string</td><td><p>A comma-separated list of categories.</p><p><br><strong>Possible values:</strong></p><ul><li><code>academic</code></li><li><code>school-holidays</code></li><li><code>public-holidays</code></li><li><code>observances</code></li><li><code>politics</code></li><li><code>conferences</code></li><li><code>expos</code></li><li><code>concerts</code></li><li><code>festivals</code></li><li><code>performing-arts</code></li><li><code>sports</code></li><li><code>community</code></li><li><code>daylight-savings</code></li><li><code>airport-delays</code></li><li><code>severe-weather</code></li><li><code>disasters</code></li><li><code>terror</code></li><li><code>health-warnings</code></li></ul><p>E.g. <code>?category=school-holidays,public-holidays</code></p><p><br>Take a look at the <a href="../../getting-started/predicthq-data/event-categories/">Event Categories</a> page for an overview of the different categories.</p></td></tr><tr><td><code>country</code><br>string</td><td><p>A comma-separated list of country codes.</p><p><br>E.g. <code>?country=AU,NZ</code></p></td></tr><tr><td><code>deleted_reason</code><br>string</td><td><p>A comma-separated list of deleted reasons for the events.</p><p><br><strong>Possible values:</strong></p><ul><li><code>cancelled</code></li><li><code>invalid</code></li><li><code>duplicate</code></li><li><code>postponed</code></li></ul><p>E.g. <code>?deleted_reason=cancelled,duplicate</code></p></td></tr><tr><td><code>end.*</code><br>date range</td><td><p>The date range during which events end. </p><p></p><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes. <code>tz</code> is time zone in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format (default is <code>UTC</code>).<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>.</p><p><br>E.g. <code>?end.gte=2018-12-19&#x26;end.lte=2018-12-19</code></p></td></tr><tr><td><code>end_around.*</code><br>date around</td><td><p>Fuzzy date search around event end. Supports <code>origin</code>, <code>offset</code>, <code>scale</code>, <code>decay</code> suffixes.</p><ul><li><code>origin</code>: The date (<em>required</em>)</li><li><code>offset</code>: The number of days from the origin before the score starts to decay (<em>optional</em>, defaults to <code>0d</code>)</li><li><code>scale</code>: Distance from origin +/- offset at which the score will equal the decay value (<em>optional</em>, defaults to <code>3d</code>)</li><li><code>decay</code>: Score value at the <code>scale</code> distance (<em>optional</em>, defaults to <code>0.5</code>)</li></ul><p>Can influence <code>relevance</code>.</p><p><br>E.g. <code>?end_around.origin=2018-12-19</code></p></td></tr><tr><td><code>entity.id</code><br>string</td><td><p>A comma-separated list of entity identifiers.</p><p><br>E.g. <code>?entity.id=XABWvihQAj8TnjvF6WNzLW</code></p></td></tr><tr><td><code>first_seen</code><br>date range</td><td><p>The date range during which events are first seen in the system. </p><p></p><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes. <code>tz</code> is time zone in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format (default is <code>UTC</code>).</p><p><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br></p><p>Please note that use of a suffix is <strong>required</strong>.</p><p></p><p>E.g. <code>?first_seen.gte=2020-11-30</code></p></td></tr><tr><td><code>id</code><br>string</td><td><p>A comma-separated list of event identifiers.</p><p><br>E.g. <code>?id=z13B3870YOgv</code></p></td></tr><tr><td><code>label</code><br>string</td><td><p>A comma-separated list of labels.<br>Please note that all event labels are lowercase and that the search is case sensitive.</p><p></p><p>E.g. <code>?label=holiday,observance</code></p><p></p><p>Supports <code>op</code> suffix to indicate whether to match labels using a logical <code>AND</code>.</p><p><br>E.g. <code>?label=holiday,observance&#x26;label.op=all</code></p><details><summary><strong>available values</strong></summary><ul><li>academic</li><li>academic-session</li><li>agriculture</li><li>air-quality</li><li>airport</li><li>american-football</li><li>animal</li><li>architecture</li><li>arson</li><li>ashfall</li><li>assassination</li><li>attack</li><li>attraction</li><li>australian-football</li><li>auto-racing</li><li>automotive</li><li>autumn-holiday</li><li>avalanche</li><li>badminton</li><li>bars-closed</li><li>bars-open</li><li>baseball</li><li>basketball</li><li>bicycle</li><li>biological-hazard</li><li>blizzard</li><li>bombing</li><li>boxing</li><li>business</li><li>campus</li><li>career</li><li>chemical</li><li>chemical-accident</li><li>christmas-holiday</li><li>civil</li><li>climate-change</li><li>closed-doors</li><li>clothing</li><li>club</li><li>coastal-event</li><li>cold-wave</li><li>comedy</li><li>comic</li><li>community</li><li>concert</li><li>conference</li><li>construction</li><li>corporate</li><li>course</li><li>craft</li><li>cricket</li><li>cyclone</li><li>daylight-savings</li><li>debates</li><li>delay</li><li>design</li><li>digital</li><li>disaster</li><li>disaster-warning</li><li>drought</li><li>dust</li><li>earthquake</li><li>easter-holiday</li><li>education</li><li>election</li><li>entertainment</li><li>entertainment-closed</li><li>entertainment-open</li><li>environment</li><li>environment-pollution</li><li>epidemic</li><li>epidemic-hazard</li><li>esports</li><li>estimated</li><li>exam</li><li>execution</li><li>explosion</li><li>expo</li><li>extreme-weather</li><li>f1</li><li>family</li><li>fashion</li><li>festival</li><li>fighting</li><li>fire</li><li>flood</li><li>fog</li><li>food</li><li>football</li><li>fundraiser</li><li>furniture</li><li>gaming</li><li>golf</li><li>graduation</li><li>gymnastics</li><li>hail</li><li>hazardous-surf</li><li>hazmat</li><li>health</li><li>health-warning</li><li>heat-wave</li><li>hijacking</li><li>hockey</li><li>holiday</li><li>holiday-christian</li><li>holiday-hebrew</li><li>holiday-hindu</li><li>holiday-local</li><li>holiday-local-common</li><li>holiday-muslim</li><li>holiday-national</li><li>holiday-observed</li><li>holiday-orthodox</li><li>holiday-religious</li><li>horse-racing</li><li>horticulture</li><li>hostage-crisis</li><li>household</li><li>hurricane</li><li>hybrid-session</li><li>ice-hockey</li><li>in-person-session</li><li>industrial</li><li>indycar</li><li>instrument</li><li>ironman</li><li>jewelry</li><li>landslide</li><li>local-market</li><li>lockdown</li><li>lpga</li><li>marathon</li><li>marine</li><li>mass-shooting</li><li>medical</li><li>mineral</li><li>minor-league</li><li>mlb</li><li>mls</li><li>mma</li><li>monster-truck</li><li>motocross</li><li>motogp</li><li>movie</li><li>music</li><li>nascar</li><li>natural</li><li>nba</li><li>nba-gleague</li><li>ncaa</li><li>nfl</li><li>nhl</li><li>nuclear</li><li>nursing</li><li>observance</li><li>observance-local</li><li>observance-season</li><li>observance-united-nations</li><li>observance-worldwide</li><li>office</li><li>olympic</li><li>online-session</li><li>outdoor</li><li>packaging</li><li>paper</li><li>parade</li><li>parliament</li><li>performing-arts</li><li>personal-care-closed</li><li>personal-care-open</li><li>pet</li><li>pga</li><li>plastic</li><li>politics</li><li>president</li><li>print</li><li>product</li><li>rain</li><li>rallies</li><li>real-estate</li><li>recreation-closed</li><li>recreation-open</li><li>referendum</li><li>religion</li><li>research-development</li><li>restaurant-closed</li><li>restaurant-open</li><li>retail-closed</li><li>retail-open</li><li>rodeo</li><li>rugby</li><li>running</li><li>sales</li><li>sand</li><li>school</li><li>science</li><li>seminar</li><li>shooting</li><li>skating</li><li>snow</li><li>soccer</li><li>social</li><li>space</li><li>sport</li><li>spring-holiday</li><li>stabbing</li><li>storm</li><li>storm-surge</li><li>summer-holiday</li><li>suspected-attack</li><li>suspected-bombing</li><li>table-tennis</li><li>technology</li><li>tennis</li><li>terror</li><li>thanksgiving-holiday</li><li>thunderstorm</li><li>tool</li><li>tornado</li><li>tourism</li><li>training</li><li>transportation</li><li>travel</li><li>triathlon</li><li>tropical-storm</li><li>tsunami</li><li>typhoon</li><li>vehicle-accident</li><li>volcano</li><li>volleyball</li><li>weather</li><li>weather-warning</li><li>wedding</li><li>wildfire</li><li>wind</li><li>winter-holiday</li><li>wnba</li><li>worship-closed</li><li>worship-open</li><li>wrestling</li><li>wwe</li><li>youth-sport</li></ul></details><p>You can also use the <a href="get-event-counts.md">count endpoint</a> to fetch a list of available labels.</p></td></tr><tr><td><code>limit</code><br>number</td><td><p>The maximum number of results to return per page. The default limit is <code>10</code>.</p><p><br>E.g. <code>?limit=10</code></p></td></tr><tr><td><code>local_rank.*</code><br>rank range</td><td><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code> and <code>lte</code> suffixes.</p><p><br>Please note that use of a suffix is <strong>required</strong>.</p><p><br>Note when filtering on <code>local_rank</code> events that do not have a <code>local_rank</code> will not be returned.</p><p><br>E.g. <code>?local_rank.gte=80&#x26;local_rank.lte=90</code></p></td></tr><tr><td><code>local_rank_level</code><br>number</td><td><p>A comma-separated list of numbers between 1 and 5, corresponding to the PredictHQ local rank levels.</p><p><br><strong>Possible values:</strong></p><ul><li><code>1</code> - Minor (rank between 0 and 20).</li><li><code>2</code> - Moderate (rank between 21 and 40).</li><li><code>3</code> - Important (rank between 41 and 60).</li><li><code>4</code> - Significant (rank between 61 and 80).</li><li><code>5</code> - Major (rank between 81 and 100).</li></ul><p>Note when filtering on <code>local_rank_level</code> events that do not have a <code>local_rank</code> will not be returned.<br></p><p>E.g. <code>?local_rank_level=4,5</code></p></td></tr><tr><td><code>location_around.*</code><br>location around</td><td><p>Fuzzy location search around event location.</p><p><br>Please note this affects the <code>relevance</code> value and does not restrict search results to the specified latitude/longitude and offset. Read more in the <a href="../../getting-started/guides/events-api-guides/understanding-relevance-field-in-event-results.md">Relevance guide</a> and combine with the <code>within</code> parameter to restrict results to a specified latitude/longitude and radius.</p><p><br>Supports <code>origin</code>, <code>offset</code>, <code>scale</code>, <code>decay</code> suffixes.</p><ul><li><code>origin</code>: The location in the form <code>{latitude},{longitude}</code> (<em>required</em>)</li><li><code>offset</code>: The distance before decay is applied (<em>optional</em>, defaults to <code>0km</code>)(Distance unit can be one of <code>m</code>, <code>km</code>, <code>ft</code>, <code>mi</code>)</li><li><code>scale</code>: Distance from origin + offset at which the score will equal decay value (<em>optional</em>, defaults to <code>2km</code>) (Distance unit can be one of <code>m</code>, <code>km</code>, <code>ft</code>, <code>mi</code>)</li><li><code>decay</code>: Score value at <code>scale</code> value (<em>optional</em>, defaults to <code>0.5</code>)</li></ul><p>E.g. <code>?location_around.origin=40.730610,-73.935242</code></p></td></tr><tr><td><code>location_confidence_score.*</code><br>number range</td><td><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code> and <code>lte</code> suffixes.</p><p><br>Please note that use of a suffix is <strong>required</strong>.</p><p></p><p>A unique attribute to Predicted Events that were generated from analyzing sets of recurring events. The score ranges from 1 to 5, representing the event’s propensity to change location with each recurrence. Higher scores indicate a higher consistency in location, while lower scores indicate the event’s location is more likely to shift once additional details become available.</p><p><br>E.g. <code>?location_confidence_score.gte=3&#x26;location_confidence_score.lte=5</code></p></td></tr><tr><td><code>offset</code><br>number</td><td><p>The number of results to skip. The default is <code>0</code>.</p><p><br>E.g. <code>?offset=20</code></p></td></tr><tr><td><code>parent.*</code></td><td><p>Whether or not to include parent events / exclude child events.<br><br>Note that<br><strong>Child</strong> events are those events that have a link to a parent event.<br><strong>Parent</strong> events are all the other events, whether they have children or not.</p><p><br>See the documentation on <a href="../../getting-started/guides/date-and-time-guides/working-with-multi-day-and-umbrella-events.md#umbrella-events-beta">umbrella events</a> for more information on parent and child events.<br><br>Currently supports the <code>include</code> suffix.<br><br><code>include</code>: Whether or not to include parent events in the response (<em>required</em>, valid options are <code>true</code>, <code>false</code> or <code>only</code>)</p><ul><li><code>true</code>: include parent events (default behaviour)</li><li><code>false</code>: exclude parent events - this will return child events only</li><li><code>only</code>: only fetch parent events (exclude child events)</li></ul><p>Default value: <code>true</code>.<br><br>Please note that use of a suffix is <strong>required</strong>.<br><br>E.g. <code>?parent.include=false</code></p></td></tr><tr><td><code>phq_attendance.*</code><br>number range</td><td><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code> and <code>lte</code> suffixes.</p><p><br>Please note that use of a suffix is <strong>required</strong>.</p><p><br>E.g. <code>?phq_attendance.gte=2000&#x26;phq_attendance.lte=10000</code></p></td></tr><tr><td><code>phq_label.*</code><br>string</td><td><p>PHQ Labels leverage newer generation LLMs and classifier models. Currently available for <code>conferences</code>, <code>expos</code>, <code>festivals</code>, <code>community</code> and <code>performing-arts</code>. Legacy labels are available in a separate field to preserve backwards compatibility.<br><br>A comma-separated list of PHQ Labels.<br>Please note that all PHQ Labels are lowercase and that the search is case sensitive.<br>Supports <code>exclude</code> suffix to get events without certain PHQ Labels and can be used without suffix for getting events with certain phq labels.</p><p><br>E.g. <code>?phq_label.exclude=lifestyle&#x26;phq_label=agriculture-forestry-and-fisheries,food-and-beverage</code></p><p></p><p>As with legacy labels, PHQ Labels support the <code>op</code> suffix to indicate whether to match or exclude PHQ Labels using a logical <code>AND</code>.</p><p></p><p>E.g. <code>?phq_label.exclude=lifestyle&#x26;phq_label=agriculture-forestry-and-fisheries,food-and-beverage&#x26;phq_label.op=all&#x26;phq_label.exclude.op=all</code></p><p></p><p>Take a look at <a href="../../getting-started/predicthq-data/labels.md#phq-label-values">PHQ Label Values</a> to get a list of possible values to use within <code>phq_label.*</code> .</p></td></tr><tr><td><code>place.*</code><br>place</td><td><p>A comma-separated list of place ids (see <a href="../places/search-places.md">Places</a>) and/or IATA (3 character), ICAO (4 character), and UN/LOCODE (5 character) airport codes where the events occur. Supports <code>scope</code> or <code>exact</code> suffixes. </p><p></p><p>A <a href="search-events.md#mapping-file">CSV file</a> of all supported airport codes and their respective place ids is available to download.</p><p><br>When <code>place.scope</code> is used, results will contain events that apply to the parent and children places of the specified place. E.g. National, regional and local school holidays that apply to a region.<br><br>When <code>place.exact</code> is used, results will contain events that apply to the specified place only.E.g. Regional school holidays only.<br><br>Please note that use of a suffix is <strong>required</strong>.</p><p><br>E.g.</p><ul><li>all events that apply to the State of New York: <code>?place.scope=5128638</code></li><li>all events that apply to the place associated with San Francisco Airport: <code>?place.scope=SFO</code></li></ul></td></tr><tr><td><code>placekey</code><br>string</td><td><p>A comma-separated list of Placekeys (See <a href="https://www.placekey.io/">placekey.io</a>). Returns events that have a Placekey value matching this filter.</p><p><br>There are 2 parts to a Placekey: <code>what@where</code><br></p><ul><li><p><code>What:</code>Contains 2 part in the form <code>{address}-{POI}</code>.</p><ul><li>The first part represents an address.</li><li>The second part represents a Point Of Interest (E.g. named venue). This will be missing on locations that only have addresses</li></ul></li><li><code>Where:</code> An H3 hexagon index(resolution 10) of the event.</li></ul><p>This filter supports entering a full Placekey to match events having that specific Placekey or a partial Placekey (such as just the <code>@where</code> part) to perform a partial match on Placekey. You can use the following Placekey format in this filter:</p><ul><li><code>{address}-{poi}@{where}</code> - only returns events with a full matching placekey (an exact match)</li><li><code>{address}@{where}</code> - matches events where the the address and where part match (even if poi is different)</li><li><code>@{where}</code> - matches events for which the @Where part matches, ignores the {address}-{poi} parts. You can perform a partial match on the @Where part to find nearby events. The minimum amount of characters that can be matched on is 5. See <a href="../../getting-started/guides/geolocation-guides/searching-by-location/find-events-by-placekey.md">using Placekey</a> for more details.</li></ul><p>Note that Placekey applies to our attended event categories. Some events do not contain a Placekey.<br><br>E.g.<code>?placekey=225@63j-rqb-j7q,@627-s8j-z2k</code></p></td></tr><tr><td><code>postponed.*</code><br>date range</td><td><p>The date range during which events were marked as postponed in the system. </p><p></p><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes. <code>tz</code> is time zone in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format (default is <code>UTC</code>).<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>.</p><p></p><p>E.g. <code>?postponed.gte=2020-03-01&#x26;postponed.lte=2020-03-15</code></p><p><br>Note when filtering on <code>postponed</code>, events that are not postponed will not be returned.</p></td></tr><tr><td><code>predicted_end.*</code><br>date range</td><td><p>The date range during which events are predicted to end. </p><p></p><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes. <code>tz</code> is time zone in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format (default is <code>UTC</code>).<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>.</p><p></p><p>E.g. <code>?predicted_end.gte=2018-12-19&#x26;predicted_end.lte=2018-12-19</code></p><p></p><p>Note when filtering on <code>predicted_end</code>, events that do not have a <code>predicted_end</code> will not be returned.</p></td></tr><tr><td><code>predicted_event_spend.*</code><br>number range</td><td><p>The Predicted Event Spend across all supported industries for an event in USD.<br><br>Supports <code>gt</code>, <code>gte</code>, <code>lt</code> and <code>lte</code> suffixes.<br></p><p>Please note that use of a suffix is <strong>required</strong>.</p><p></p><p>Note: When using this filter events that do not have a <code>predicted_event_spend</code> will not be returned.</p><p></p><p>E.g. <code>?predicted_event_spend.gte=80000&#x26;predicted_event_spend.lte=200000</code><br></p></td></tr><tr><td><code>predicted_event_spend_industry.*</code><br>number range</td><td><p>The Predicted Event Spend for a given industry in USD.<br><br>Supported industries:</p><ul><li><code>accommodation</code></li><li><code>hospitality</code></li><li><code>transportation</code></li></ul><p>The format of this parameter name is:</p><pre><code>predicted_event_spend_industry.&#x3C;industry>.&#x3C;suffix>
</code></pre><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code> and <code>lte</code> suffixes.</p><p></p><p>Please note that use of a suffix is <strong>required</strong>.</p><p></p><p>Note: When using this filter events that do not have a <code>predicted_event_spend</code> will not be returned.</p><p></p><p>E.g. <code>predicted_event_spend_industry.accommodation.gte=80000&#x26;predicted_event_spend_industry.accommodation.lte=200000</code></p></td></tr><tr><td><code>q</code><br>string</td><td><p>A full-text search query.</p><p><br>Can influence <code>relevance</code>.</p><p><br>E.g. <code>?q=katy+perry</code></p></td></tr><tr><td><code>rank.*</code><br>rank range</td><td><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code> and <code>lte</code> suffixes.</p><p><br>Please note that use of a suffix is <strong>required</strong>.</p><p><br>E.g. <code>?rank.gte=80&#x26;rank.lte=90</code></p></td></tr><tr><td><code>rank_level</code><br>number</td><td><p>A comma-separated list of numbers between 1 and 5, corresponding to the PredictHQ rank levels.</p><p><br><strong>Possible values:</strong></p><ul><li><code>1</code> - Minor (rank between 0 and 20).</li><li><code>2</code> - Moderate (rank between 21 and 40).</li><li><code>3</code> - Important (rank between 41 and 60).</li><li><code>4</code> - Significant (rank between 61 and 80).</li><li><code>5</code> - Major (rank between 81 and 100).</li></ul><p>E.g. <code>?rank_level=4,5</code></p></td></tr><tr><td><code>relevance</code><br>string</td><td><p>A comma-separated list of components to include when calculating the <code>relevance</code> field of an event.The relevance components are multiplied together to produce the overall relevance.</p><p><br><strong>Parameter Components:</strong><br>These components correspond to search parameters that can influence relevance. If the parameter isn't provided as part of a search its component will be ignored.By default, <code>relevance</code> includes the components of each relevance-influencing parameter in a search.</p><ul><li><code>q</code></li><li><code>start_around</code></li><li><code>end_around</code></li><li><code>location_around</code></li></ul><p><strong>Field Components:</strong><br>These components correspond to event fields that can be included in relevance. They are not included in <code>relevance</code> by default.</p><ul><li><code>rank</code></li><li><code>local_rank</code></li></ul><p><br>E.g. <code>?relevance=q,rank,location_around</code></p></td></tr><tr><td><code>saved_location.location_id</code><br>string</td><td><p>A comma-separated list of saved location identifiers. Up to a maximum of 20 identifiers. This filters the events returned to events within the locations specified. See the <a href="../saved-locations/search-saved-locations.md">Saved Locations API</a> for more details on getting location IDs for a location.</p><p><br>E.g. <code>?saved_location.location_id=sFlb8HlsLa1j-S4UDEMEkQ</code></p></td></tr><tr><td><code>sort</code><br>string</td><td><p>A comma-separated list of fields to sort results by. The default is <code>relevance,-start</code>.<br>Prefix the field name with <code>-</code> for reverse order.</p><p><br><strong>Possible values:</strong></p><ul><li><code>id</code></li><li><code>title</code></li><li><code>start</code></li><li><code>end</code></li><li><code>first_seen</code></li><li><code>predicted_end</code></li><li><code>updated</code></li><li><code>rank</code></li><li><code>local_rank</code></li><li><code>phq_attendance</code></li><li><code>category</code></li><li><code>duration</code></li><li><code>country</code></li><li><code>labels</code></li><li><code>relevance</code></li><li><code>predicted_event_spend</code></li><li><code>predicted_event_spend_industry.accommodation</code></li><li><code>predicted_event_spend_industry.hospitality</code></li><li><code>predicted_event_spend_industry.transportation</code></li></ul><p>Note when sorting on <code>predicted_end</code>or <code>local_rank</code>  (regardless of sort order), events that do not have a <code>predicted_end</code>, <code>local_rank</code> will be placed last.<br>When sorting by <code>relevance</code> the most relevant results are sorted first, regardless of sort order.<br></p><p>E.g. <code>?sort=country,-start</code></p></td></tr><tr><td><code>start.*</code><br>date range</td><td><p>The date range during which events start. </p><p></p><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes. <code>tz</code> is time zone in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format (default is <code>UTC</code>).<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>.</p><p><br>E.g. <code>?start.gte=2018-12-19&#x26;start.lte=2018-12-19</code></p></td></tr><tr><td><code>start_around.*</code><br>date around</td><td><p>Fuzzy date search around event start. Supports <code>origin</code>, <code>offset</code>, <code>scale</code>, <code>decay</code> suffixes.</p><ul><li><code>origin</code>: The date (<em>required</em>)</li><li><code>offset</code>: The number of days from the origin before the score starts to decay (<em>optional</em>, defaults to <code>0d</code>)</li><li><code>scale</code>: Distance from origin +/- offset at which the score will equal the decay value (<em>optional</em>, defaults to <code>3d</code>)</li><li><code>decay</code>: Score value at the <code>scale</code> distance (<em>optional</em>, defaults to <code>0.5</code>)</li></ul><p>Can influence <code>relevance</code>.</p><p><br>E.g. <code>?start_around.origin=2018-12-19</code></p></td></tr><tr><td><code>start_date_confidence_score.*</code><br>number range</td><td><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code> and <code>lte</code> suffixes.</p><p><br>Please note that use of a suffix is <strong>required</strong>.</p><p></p><p>A unique attribute to Predicted Events that were generated from analyzing sets of recurring events. The score ranges from 1 to 5, representing the event’s consistency in being held around the same date with each recurrence. Higher scores indicate the event is held at mostly the same date each year, while lower scores indicate a greater variation in start date, meaning that details are more likely to change as new details become available.</p><p><br>E.g. <code>?start_date_confidence_score.gte=3&#x26;start_date_confidence_score.lte=5</code></p></td></tr><tr><td><code>state</code><br>string</td><td>A comma-separated list of states for the events. Supports <code>active</code>, <code>deleted</code> and <code>predicted</code>. By default, returns <code>active</code> events only.<br><br>This parameter is useful in conjunction with <code>updated</code> when you cache events and are interested in retrieving a list of all events that have changed since a specific date and time.<br><br>E.g. <code>?state=active,deleted</code></td></tr><tr><td><code>updated.*</code><br>date range</td><td><p>The date range during which events were last modified. </p><p></p><p>Supports <code>gt</code>, <code>gte</code>, <code>lt</code>, <code>lte</code> and <code>tz</code> suffixes. <code>tz</code> is time zone in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format (default is <code>UTC</code>).<br><br>The accepted format for this parameter is either <code>YYYY-MM-DD</code> or <code>YYYY-MM-DDThh:mm:ss</code><br><br>Please note that use of a suffix is <strong>required</strong>.</p><p><br>E.g. <code>?updated.gte=2018-05-01T09:55:00Z</code></p></td></tr><tr><td><code>within</code><br>area</td><td>A geo center and radius in the form <code>{radius}{unit}@{latitude},{longitude}</code>, where the radius unit can be one of: meters <code>m</code>, kilometers <code>km</code>, feet <code>ft</code>, miles <code>mi</code>. When using the units of <code>km</code> and <code>mi</code> you can enter whole numbers or floats <code>e.g. 5mi, 1.5km or 1.2mi</code>. When using the units <code>ft</code> or <code>m</code> you need to enter whole numbers (you cannot enter a fraction of a meter or foot).<br><br>Note that results may contain events that apply to a parent scope of the specified area.<br><br>Note that it can be difficult working out a suitable radius around your location so to make it easier please use our <a href="../suggested-radius/get-suggested-radius.md">Suggested Radius API</a>.<br><br>E.g. National school holidays that apply to the local radius.<br>E.g. <code>?within=2.5mi@-36.844480,174.768368</code> or <code>?within=2750m@-36.844480,174.768368</code></td></tr></tbody></table>

#### Mapping File

Below is a CSV of all supported airport codes and their respective `place_id`.

{% file src="../../.gitbook/assets/airport-codes.csv" %}

## Response

### Response Fields

<table><thead><tr><th width="375">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>cancelled</code><br>string, null</td><td>The date the event was set to cancelled in the system in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br><br>All dates are in UTC.<br><br>This field will only be present for events with <code>deleted_reason</code> set to <code>cancelled</code>, and will have a <code>null</code> value if <code>cancelled</code> date is not available.<br><br>E.g. <code>2018-12-19T10:00:00Z</code></td></tr><tr><td><code>category</code><br>string</td><td><p>The category of the event<br><strong>Possible values:</strong></p><ul><li><code>academic</code></li><li><code>school-holidays</code></li><li><code>public-holidays</code></li><li><code>observances</code></li><li><code>politics</code></li><li><code>conferences</code></li><li><code>expos</code></li><li><code>concerts</code></li><li><code>festivals</code></li><li><code>performing-arts</code></li><li><code>sports</code></li><li><code>community</code></li><li><code>daylight-savings</code></li><li><code>airport-delays</code></li><li><code>severe-weather</code></li><li><code>disasters</code></li><li><code>terror</code></li><li><code>health-warnings</code></li></ul><p>E.g. <code>concerts</code></p></td></tr><tr><td><code>country</code><br>string</td><td>The country code in <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> format.<br>Note that the <code>country</code> value will usually be present but in some cases where the event location is not within a country (e.g. an earthquake in the middle of the ocean) it can be empty.<br><br>E.g. <code>NZ</code></td></tr><tr><td><code>deleted_reason</code><br>string</td><td><p>The reason why the event was deleted.<br><br>Note that this field is only present for events with state <code>deleted</code>.<br><br><strong>Possible values:</strong></p><ul><li><code>cancelled</code></li><li><code>duplicate</code></li><li><code>invalid</code></li><li><code>postponed</code></li></ul><p>E.g. <code>duplicate</code></p></td></tr><tr><td><code>description</code><br>string</td><td>A description of the event.<br>E.g. <code>See Katy Perry in concert [...]</code></td></tr><tr><td><code>duplicate_of_id</code><br>string</td><td>The <code>id</code> of the active event this event is a duplicate of.<br><br>Note that this field is only present for deleted events with <code>deleted_reason</code> set to <code>duplicate</code>.<br><br>E.g. <code>z13B3870YOgv</code></td></tr><tr><td><code>duration</code><br>number</td><td>The duration of the event in seconds.<br><br>E.g. <code>3600</code></td></tr><tr><td><code>end</code><br>string</td><td>The end date of the event in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br><br>All end dates are in UTC <strong>if the event time zone is provided</strong>, and in local time otherwise. For example, Independence Day falls on the 4th of July regardless of the time zone, and will have a <code>null</code> time zone.<br><br>E.g. <code>2018-12-19T10:00:00Z</code></td></tr><tr><td><code>end_local</code><br>string</td><td><p>The local time end date of the event in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format. <code>end_local</code> is the date time in the event's location.</p><p></p><p>The <code>end</code> field is in UTC and <code>end_local</code> is in the local time in the timezone at the events location.<br><br>E.g. <code>2018-12-19T10:00:00</code></p></td></tr><tr><td><code>entities</code><br>array</td><td><p>An array of entities linked to the event.<br><br><strong>Possible types:</strong></p><ul><li><code>event-group</code></li><li><code>venue</code></li></ul><p>E.g. </p><pre class="language-json"><code class="lang-json">[
  {
    "entity_id": "328DxFUbRKvaiJJGyT2gReF",
    "type": "venue",
    "name": "Spark Arena",
    "formatted_address": "Mahuhu Crescent\nAuckland 1010\nNew Zealand"
  }
]
</code></pre></td></tr><tr><td><code>first_seen</code><br>string, null</td><td>The date the event first entered our dataset in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format. All dates are in UTC. This value may be missing on some events, and should not be considered an event announcement date.<br><br>E.g. <code>2017-12-19T06:00:00Z</code></td></tr><tr><td><code>id</code><br>string</td><td>The unique identifier of the event.<br><br>E.g. <code>z13B3870YOgv</code></td></tr><tr><td><code>impact_patterns</code><br>array</td><td><p>Also known as “Demand impact patterns”. This field shows the impact for leading days (days before the event), lagging days (days after an event), and the days the event occurs. See <a data-mention href="../../getting-started/predicthq-data/impact-patterns.md">impact-patterns.md</a>for more details.<br><br><code>impact_patterns</code> is an array of impact pattern objects. The same event can have different impact patterns for different industry verticals. It contains the following fields:</p><ul><li><code>vertical</code> - The industry vertical the impact pattern applies to. </li><li><code>impact_type</code> - Indicates the type of impact shown in the impact pattern. Currently, the supported types are phq_rank and phq_attendance. If the impact_type is phq_rank then the impact values shown per day reflect phq_rank values. If impact_type is phq_attendance then the impact values per day reflect phq_attendance which is the estimated amount of people attending the event per day.</li></ul><p><code>impacts</code> is an array of objects with one entry for each day that contains the following values:</p><ul><li><code>date_local</code> - the date in the local timezone of the event.</li><li><code>value</code> - the value of the <code>impact_type</code> for that given day. For example, if the <code>impact_type</code> was <code>phq_rank</code> the value would be the PHQ Rank value on the given day. Otherwise, it will reflect <code>phq_attendance</code> </li><li><code>position</code> - can be <code>leading</code>, <code>event_day</code> or <code>lagging</code>. <code>leading</code> are the days before the event occurs, <code>event_day</code> are the days the event occurs and <code>lagging</code> are the days after the event has occurred.</li></ul><p>The example below is based on an <code>impact_type</code> of <code>phq_rank</code> for severe weather events.</p><pre class="language-json"><code class="lang-json">[
  {
    "date_local": "2022-01-08",
    "value": 10,
    "position": "leading"
  },
  {
    "date_local": "2022-01-09",
    "value": 21,
    "position": "event_day"
  },
  ...
]
</code></pre></td></tr><tr><td><code>labels</code><br>array</td><td><p>The labels associated with the event.<br>E.g. <code>["holiday", "holiday-national"]</code></p><details><summary><strong>possible labels</strong></summary><ul><li>academic</li><li>academic-session</li><li>agriculture</li><li>air-quality</li><li>airport</li><li>american-football</li><li>animal</li><li>architecture</li><li>arson</li><li>ashfall</li><li>assassination</li><li>attack</li><li>attraction</li><li>australian-football</li><li>auto-racing</li><li>automotive</li><li>autumn-holiday</li><li>avalanche</li><li>badminton</li><li>bars-closed</li><li>bars-open</li><li>baseball</li><li>basketball</li><li>bicycle</li><li>biological-hazard</li><li>blizzard</li><li>bombing</li><li>boxing</li><li>business</li><li>campus</li><li>career</li><li>chemical</li><li>chemical-accident</li><li>christmas-holiday</li><li>civil</li><li>climate-change</li><li>closed-doors</li><li>clothing</li><li>club</li><li>coastal-event</li><li>cold-wave</li><li>comedy</li><li>comic</li><li>community</li><li>concert</li><li>conference</li><li>construction</li><li>corporate</li><li>course</li><li>craft</li><li>cricket</li><li>cyclone</li><li>daylight-savings</li><li>debates</li><li>delay</li><li>design</li><li>digital</li><li>disaster</li><li>disaster-warning</li><li>drought</li><li>dust</li><li>earthquake</li><li>easter-holiday</li><li>education</li><li>election</li><li>entertainment</li><li>entertainment-closed</li><li>entertainment-open</li><li>environment</li><li>environment-pollution</li><li>epidemic</li><li>epidemic-hazard</li><li>esports</li><li>estimated</li><li>exam</li><li>execution</li><li>explosion</li><li>expo</li><li>extreme-weather</li><li>f1</li><li>family</li><li>fashion</li><li>festival</li><li>fighting</li><li>fire</li><li>flood</li><li>fog</li><li>food</li><li>football</li><li>fundraiser</li><li>furniture</li><li>gaming</li><li>golf</li><li>graduation</li><li>gymnastics</li><li>hail</li><li>hazardous-surf</li><li>hazmat</li><li>health</li><li>health-warning</li><li>heat-wave</li><li>hijacking</li><li>hockey</li><li>holiday</li><li>holiday-christian</li><li>holiday-hebrew</li><li>holiday-hindu</li><li>holiday-local</li><li>holiday-local-common</li><li>holiday-muslim</li><li>holiday-national</li><li>holiday-observed</li><li>holiday-orthodox</li><li>holiday-religious</li><li>horse-racing</li><li>horticulture</li><li>hostage-crisis</li><li>household</li><li>hurricane</li><li>hybrid-session</li><li>ice-hockey</li><li>in-person-session</li><li>industrial</li><li>indycar</li><li>instrument</li><li>ironman</li><li>jewelry</li><li>landslide</li><li>local-market</li><li>lockdown</li><li>lpga</li><li>marathon</li><li>marine</li><li>mass-shooting</li><li>medical</li><li>mineral</li><li>minor-league</li><li>mlb</li><li>mls</li><li>mma</li><li>monster-truck</li><li>motocross</li><li>motogp</li><li>movie</li><li>music</li><li>nascar</li><li>natural</li><li>nba</li><li>nba-gleague</li><li>ncaa</li><li>nfl</li><li>nhl</li><li>nuclear</li><li>nursing</li><li>observance</li><li>observance-local</li><li>observance-season</li><li>observance-united-nations</li><li>observance-worldwide</li><li>office</li><li>olympic</li><li>online-session</li><li>outdoor</li><li>packaging</li><li>paper</li><li>parade</li><li>parliament</li><li>performing-arts</li><li>personal-care-closed</li><li>personal-care-open</li><li>pet</li><li>pga</li><li>plastic</li><li>politics</li><li>president</li><li>print</li><li>product</li><li>rain</li><li>rallies</li><li>real-estate</li><li>recreation-closed</li><li>recreation-open</li><li>referendum</li><li>religion</li><li>research-development</li><li>restaurant-closed</li><li>restaurant-open</li><li>retail-closed</li><li>retail-open</li><li>rodeo</li><li>rugby</li><li>running</li><li>sales</li><li>sand</li><li>school</li><li>science</li><li>seminar</li><li>shooting</li><li>skating</li><li>snow</li><li>soccer</li><li>social</li><li>space</li><li>sport</li><li>spring-holiday</li><li>stabbing</li><li>storm</li><li>storm-surge</li><li>summer-holiday</li><li>suspected-attack</li><li>suspected-bombing</li><li>table-tennis</li><li>technology</li><li>tennis</li><li>terror</li><li>thanksgiving-holiday</li><li>thunderstorm</li><li>tool</li><li>tornado</li><li>tourism</li><li>training</li><li>transportation</li><li>travel</li><li>triathlon</li><li>tropical-storm</li><li>tsunami</li><li>typhoon</li><li>vehicle-accident</li><li>volcano</li><li>volleyball</li><li>weather</li><li>weather-warning</li><li>wedding</li><li>wildfire</li><li>wind</li><li>winter-holiday</li><li>wnba</li><li>worship-closed</li><li>worship-open</li><li>wrestling</li><li>wwe</li><li>youth-sport</li></ul></details><p>You can also use the <a href="get-event-counts.md">count endpoint</a> to fetch a list of available labels.</p></td></tr><tr><td><code>local_rank</code><br>number, null</td><td>Similar to PHQ Rank, this is a log scale numerical value between 0 and 100 with a five-level hierarchical impact schema. It is designed to represent the potential impact of an event on its local geographical area.<br><br>Local Rank is calculated for events in the categories <code>community</code>, <code>concerts</code>, <code>conferences</code>, <code>expos</code>, <code>sports</code>, <code>festivals</code>, <code>performing-arts</code>.<br><br>If <code>local_rank</code> is not intended to be available for an event, this field will be <code>null</code>.<br>E.g. <code>72</code></td></tr><tr><td><code>location</code><br>array</td><td>A 2-tuple representing the geo location of the event. Note that the longitude/latitude coordinates use the <a href="https://geojson.org/">GeoJSON order</a> [lon, lat].<br><br>E.g. <code>[174.776792, -36.847319]</code></td></tr><tr><td><code>location_confidence_score</code><br>number</td><td>The Predicted Event location confidence score.</td></tr><tr><td><code>geo</code><br>object</td><td><p>An object containing the geographic information about an event. This field will be used in future instead of the <strong>location</strong> field (the location field will remain in the current version of the API but could be removed in future versions).<br><br>This field has two subfield: <strong>geometry</strong>, which represents the geometry associated with the event in the <a href="https://geojson.org/">GeoJSON format</a>, and <strong>address</strong>, which include the detailed address information.</p><p></p><p><strong>address</strong> subfield</p><ul><li><code>locality</code> (optional) - indicates the city or town the event occurs in</li><li><code>country_code</code> (required) - 2 letter country code</li><li><code>formatted_address</code> (optional) - a full formatted address which can include street address, town, postcode, region/state and country</li><li><code>postcode</code> (optional)</li><li><code>region</code> (optional) - the region or state at which the event takes place</li></ul><p><strong>geometry</strong> subfield</p><p><strong>Possible</strong> <code>geometry.type</code><strong>:</strong></p><ul><li><code>Point</code></li><li><code>Polygon</code></li><li><code>MultiPolygon</code></li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "geometry": {
    "type": "Point",
    "coordinates": [174.776792, -36.847319]
  },
  "address": {
    "locality": "Auckland",
    "country_code": "NZ",
    "postcode":1010
  }
}
</code></pre></td></tr><tr><td><code>parent_event</code><br>object</td><td><p>Used to indicate if this event is part of a larger event. These types of events are called umbrella events in the system. For example, a large multi-day parent umbrella event may have individual child events for sessions on different days. For example the Formula 1 2019 United States Grand Prix has child events for the qualification, 3 practice events, a concert that occurs at the Grand Prix, and the actual race events (there are 12 child events).<br><br>See <a href="../../getting-started/guides/date-and-time-guides/working-with-multi-day-and-umbrella-events.md#umbrella-events-beta">umbrella events</a> for details on this field and details on what umbrella events are.<br><br>Note that this field in this release only shows if a child event has a parent id. It does not indicate if a parent event has child events.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "parent_event": {
    "parent_event_id": "w7dYyrFwTUQGYE6euv"
  }
}
</code></pre></td></tr><tr><td><code>phq_attendance</code><br>number</td><td>A numerical value that reflects the predicted attendance number for supported attendance-based categories. The following categories are supported: concerts, performing arts, sports, expos, conferences, community and festivals.<br><br>phq_attendance reflects the entire attendance for multi-day events (the number of people attending across the full duration of the event) except for some categories like conferences where it is the daily attendance.<br>See <a href="../../getting-started/guides/date-and-time-guides/working-with-multi-day-and-umbrella-events.md">Handling multi-day and Umbrella events</a> for more details.<br><br>E.g. <code>2511</code></td></tr><tr><td><code>phq_labels</code><br>array</td><td><p> An array of objects which contains the PHQ Labels associated to an event as well as the weight that they contribute to the event. Weights from all labels should sum up to 1.<br><br>PHQ Labels leverage newer generation LLMs and classifier models. Currently available for <code>conferences</code>, <code>expos</code>, <code>festivals</code>, <code>community</code> and <code>performing-arts</code> categories. Legacy labels are available in a separate field to preserve backwards compatibility.</p><p><br>E.g.</p><pre class="language-json"><code class="lang-json">[
  {
    "label": "agriculture-forestry-and-fisheries",
    "weight": 0.376
  },
  {
    "label": "food-and-beverage",
    "weight": 0.263
  },
  {
    "label": "art-and-cultural",
    "weight": 0.186
  },
  {
    "label": "science-and-technology",
    "weight": 0.175
  }
]
</code></pre><p></p><p>Take a look at <a href="../../getting-started/predicthq-data/labels.md#phq-label-values">PHQ Label Values</a> to see a list of possible values that could be in <code>phq_labels.label</code>.</p></td></tr><tr><td><code>place_hierarchies</code><br>array</td><td><p>An array of place hierarchies for the event. Each hierarchy is an array of place ids (see <a href="../places/search-places.md">Places</a>). The final place in a hierarchy is a specific place the event applies to. Each place is a sub-place of the place immediately preceding it in the hierarchy.<br><br>For example, a hierarchy might contain the following places in this order: <code>Earth > Europe > United Kingdom > England > Nottingham</code><br><br>Note that the <code>place_hierarchies</code> value can be an empty array in some cases.</p><p></p><p>E.g.</p><pre class="language-json"><code class="lang-json">[
  [
    "6295630",
    "6255148",
    "2635167",
    "6269131",
    "3333178",
    "2641170"
  ]
]
</code></pre></td></tr><tr><td><code>placekey</code><br>string</td><td><p>The Placekey (See <a href="https://www.placekey.io/">placekey.io</a>) reflects the location of an event in the format <code>what@where</code>. Placekey is part of the geo field for an event.<br><br><strong>Possible formats</strong></p><ul><li><code>{address}-{poi}@{where}</code></li><li><code>{address)@{where}</code></li><li><code>@where</code></li></ul><p>E.g. <code>222-229@8t2-fgc-z2k</code> or <code>@7f7-mcy-ndv</code><br><br>Note that Placekey applies to our <a href="https://www.predicthq.com/intelligence/data-enrichment/event-categories">attended event categories</a>. Some events do not contain a Placekey.</p></td></tr><tr><td><code>postponed</code><br>string, null</td><td>The date the event was set to postponed in the system in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br>All dates are in UTC.<br><br>This field will only be present for events with <code>deleted_reason</code> set to <code>postponed</code>, and will have a <code>null</code> value if <code>postponed</code> date is not available.<br><br>E.g. <code>2018-12-19T10:00:00Z</code></td></tr><tr><td><code>predicted_end</code><br>string</td><td>The predicted end date of the event in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br><br>Predicted end dates are in UTC <strong>if the event time zone is provided</strong>, and in local time otherwise. For example, Independence Day falls on the 4th of July regardless of the time zone, and will have a <code>null</code> time zone.<br><br>This field will only be present if an actual <code>end</code> time is <em>not</em> available for an event and we have a predicted end time.<br><br>E.g. <code>2018-12-19T10:00:00Z</code></td></tr><tr><td><code>predicted_end_local</code><br>string</td><td>The predicted end date of the event in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br><br>The predicted end date are in the event's location.<br><br>This field will only be present if an actual <code>end</code> time is <em>not</em> available for an event and we have a predicted end time.<br><br>E.g. <code>2018-12-19T10:00:00</code></td></tr><tr><td><code>predicted_event_spend</code><br>number</td><td>The total Predicted Event Spend across all supported industries for an event in USD. This figure represents the consumer spend impact on local businesses that the event is predicted to generate.<br><br>E.g. <code>11806680</code></td></tr><tr><td><code>predicted_event_spend_industries</code><br>object</td><td><p>The Predicted Event Spend for each supported industry in USD.</p><p></p><p>Possible industries:</p><ul><li><code>accommodation</code> - The consumer spend predicted to be attributed to hotels and hosts.</li><li><code>hospitality</code> - The consumer spend predicted to be attributed to food and beverage.</li><li><code>transportation</code> - The consumer spend predicted to be attributed to ground-based transportation as a means of getting to and from the event.<br></li></ul><p>E.g.</p><pre class="language-json"><code class="lang-json">{
  "predicted_event_spend_industries": {
    "accommodation": 5016960,
    "hospitality": 4924000,
    "transportation": 1865720
  }
}
</code></pre></td></tr><tr><td><code>rank</code><br>number</td><td>A log scale numerical value between 0 and 100 with a five-level hierarchical impact schema. It is designed to represent the potential impact of an event independent of its geographical location.<br><br>E.g. <code>83</code></td></tr><tr><td><code>relevance</code><br>number, null</td><td><p>Relative relevance of the event to the event search.</p><p><br>See the relevance parameter for information on how relevance is calculated.</p><p><br>E.g. <code>2.9654586</code></p></td></tr><tr><td><code>scope</code><br>string</td><td><p>The geographical scope the events apply to.<br><strong>Possible values:</strong></p><ul><li><code>locality</code></li><li><code>localadmin</code></li><li><code>county</code></li><li><code>region</code></li><li><code>country</code></li></ul><p>E.g. <code>locality</code></p></td></tr><tr><td><code>start</code><br>string</td><td>The start date of the event in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.<br><br>All start dates are in UTC <strong>if the event time zone is provided</strong>, and in local time otherwise. For example, Independence Day falls on the 4th of July regardless of the time zone, and will have a <code>null</code> time zone.<br><br>If an event has a start time of midnight (in the event time zone) this is an indication that the actual time may be unknown. You may wish to omit the time when displaying these events.<br><br>E.g. <code>2018-12-19T06:00:00Z</code></td></tr><tr><td><code>start_local</code><br>string</td><td><p>The local start date and time of the event in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format. <code>start_local</code> is the date time in the event's location.</p><p></p><p>The <code>start</code> field is in UTC and <code>start_local</code> is in the local time in the timezone at the event location.<br><br>E.g. <code>2018-12-19T10:00:00</code></p></td></tr><tr><td><code>start_date_confidence_score</code><br>number</td><td>The Predicted Event start date confidence score.</td></tr><tr><td><code>state</code><br>string</td><td><p>The publication state of the event.<br><strong>Possible values:</strong></p><ul><li><code>active</code>: the event is published and valid.</li><li><code>deleted</code>: the event was removed, either because it was cancelled or is a duplicate.</li><li><code>predicted</code>: events that have an unconfirmed start time i.e for which the exact time the event begins is not yet known.</li></ul></td></tr><tr><td><code>timezone</code><br>string, null</td><td>The time zone of the event in <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">TZ Database</a> format. This is helpful so you know which time zone to convert the dates to (if needed).<br><br>If the time zone is <code>null</code>, the <code>start</code> and <code>end</code> date should be regarded as time zone agnostic and already being in local time. Our <code>start</code> and <code>end</code> filters take this into account when specifying a lower and higher bound on dates.<br><br>E.g. <code>Pacific/Auckland</code></td></tr><tr><td><code>title</code><br>string</td><td>The title of the event.<br><br>E.g. <code>Katy Perry</code></td></tr><tr><td><code>updated</code><br>string</td><td>The last modification date of the event in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format. All dates are in UTC.<br><br>E.g. <code>2018-05-01T05:00:00Z</code></td></tr></tbody></table>

### JSON Schema

{% file src="../../.gitbook/assets/events-response-schema.json" %}
Search Events Response JSON Schema
{% endfile %}

{% file src="../../.gitbook/assets/event-schema (1).json" %}
Single Event JSON Schema
{% endfile %}

<details>

<summary>Example response</summary>

Below is an example of a single result.

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
      "phq_attendance": 120000,
      "entities": [
        {
          "entity_id": "dh6tCwHCRjZUNmzaviVw5g",
          "name": "Carlos Sainz Jr",
          "type": "person"
        },
        {
          "entity_id": "fqGj7EdaKsDPGFUgsYhYWq",
          "name": "Kevin Magnussen",
          "type": "person"
        },
        {
          "entity_id": "e5rtDESKg4fLpHzmTcdAxy",
          "name": "Alexander Albon",
          "type": "person"
        },
        {
          "entity_id": "DtXbSrLe9Mb9BQfjzt8q3Q",
          "name": "Sergio Perez",
          "type": "person"
        },
        {
          "entity_id": "32wsZ6AhQTmehuPV9KwqgCY",
          "name": "Lewis Hamilton",
          "type": "person"
        },
        {
          "entity_id": "hdqmJpv6pbCNT5RMLjiQr8",
          "name": "Lando Norris",
          "type": "person"
        },
        {
          "entity_id": "dXA6AvcgEg7W5SJdjcgAAG",
          "name": "Lance Stroll",
          "type": "person"
        },
        {
          "entity_id": "sn3aet9XXYWPu2RmNMVsAG",
          "name": "Daniil Kvyat",
          "type": "person"
        },
        {
          "entity_id": "hKiTqaaffAzV4wGntE6LH8",
          "name": "Robert Kubica",
          "type": "person"
        },
        {
          "entity_id": "eG36WTqRtMwvjHM7SLHwiG",
          "name": "Antonio Giovinazzi",
          "type": "person"
        },
        {
          "entity_id": "JpFCtMes9vVbXxKduZ9jTd",
          "name": "Nicholas Latifi",
          "type": "person"
        },
        {
          "entity_id": "fS2HcqsbnzuCtXgUqch6Py",
          "name": "Max Verstappen",
          "type": "person"
        },
        {
          "entity_id": "dMezEeCcEa9T7RscX4aBmg",
          "name": "Valtteri Bottas",
          "type": "person"
        },
        {
          "entity_id": "DhfPt6zSSUjUrWWfCpukkY",
          "name": "Sebastian Vettel",
          "type": "person"
        },
        {
          "entity_id": "fdX7zyHMKYjAjJhSKhAvaG",
          "name": "Charles Leclerc",
          "type": "person"
        },
        {
          "entity_id": "XS7dVfwZBETRejm7en3Adg",
          "name": "Pierre Gasly",
          "type": "person"
        },
        {
          "entity_id": "33RfRSKSNRfuAzAYWEV8mR8",
          "name": "George Russell",
          "type": "person"
        },
        {
          "entity_id": "e5rv77Gws6cKNCmJra5VFy",
          "name": "Daniel Ricciardo",
          "type": "person"
        },
        {
          "entity_id": "7NT7S5KqiwqdKZiwsydzz8",
          "name": "Nico Hulkenberg",
          "type": "person"
        },
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
      "updated": "2023-06-02T16:21:48Z",
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
        "placekey": "zzw-222@8t2-fgg-gtv"
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
      "private": false,
      "predicted_event_spend": 11806680,
      "predicted_event_spend_industries": {
        "accommodation": 5016960,
        "hospitality": 4924000,
        "transportation": 1865720
      }
    }
  ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/events/?id=5uRg7CqGu7DTtu4Rfk \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "id": "5uRg7CqGu7DTtu4Rfk"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Guides

Below are some guides relevant to this API:

* [Geolocation Guides](../../getting-started/guides/geolocation-guides/)
* [Date and Time Guides](../../getting-started/guides/date-and-time-guides/)
* Other [Event API Guides](../../getting-started/guides/events-api-guides/)

