# Data Accuracy

We have a rigorous set of models and algorithms to ensure we’re providing a clean and verified data set. Our machine learning models are working day-in and day-out, which is especially crucial for event data, which is changing all of the time.

Every event in our API goes through multiple steps to ensure quality and accuracy. Some example steps are:

**Standardization:** All events follow the same schema for ease of ingestion, comparability and compatibility.

**Aggregation:** We pull in events and entities from hundreds of different sources and compare them for quality and accuracy.

**Enrichment:** We categorize, label and add entities to all events to help reduce noise. We also ensure all events have a date, time and location.

**Spam Filtering:** Bad data is worse than no data at all. We ensure you only have access to events that are actually happening.

30% to 40% of events we receive are spam, add-ons or duplicates. We have a 0% spam rate.

**Geocoding:** Every event has a lat/long, allowing for precise mapping. Events also follow identification patterns from the open-source Geonames database. For instance, all events in California will have multiple IDs, of which 5332921 (the ID for California) will always be included. We also provide venue name and formatted address whenever possible.

**De-duplicating:** We combine duplicate records into one reliable event. E.g. Our system may find a football game with 30,000 expected attendees. It finds eight listings of this game from five different sources. Our unique model kicks in and keeps a single event with the aggregated detail from all of the listings.

**Ranking:** See details above on what goes into our rankings. We track accuracy with a variety of metrics and we’re refining daily. The top metrics we track are: Spam rates, number of duplicated events, location and competitive comparison.
