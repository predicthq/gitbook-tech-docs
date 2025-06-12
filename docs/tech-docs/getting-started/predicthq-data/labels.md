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

PHQ Labels are generated through newer Large Language Models (LLMs) and overall achieve a higher standard of **specificity** and **relevance** in highlighting an event's key themes when compared to legacy methods.

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

PHQ Labels are **constantly being improved and updated** by our team and LLM models therefore we recommend using [Get Event Counts](../../api/events/get-event-counts.md) to retrieve an **up-to-date and relevant** list of PHQ Labels and the count of events labeled with each, **within your PredictHQ plan**.&#x20;

Here is an example, for [Taylor Swift and Sabrina Carpenter](https://events.predicthq.com/events/ssZCJhGGKUswicJswa) at the Melbourne Cricket Ground in 2024 it has the following PHQ labels (pop, country, and rock) in the API response:

```
"phq_labels": [ { "label": "pop", "weight": 0.51 }, { "label": "country", "weight": 0.25 }, { "label": "rock", "weight": 0.25 }
```

You could also use [Query Parameters](../../api/events/search-events.md#query-parameters) to retrieve a list and the count of PHQ Labels that match your criteria, e.g. PHQ Labels associated with the sports category or PHQ Labels of events that will be taking place in a specific time and place. Here is an example:

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

print(phq_labels)
# > {'basketball': 408197,'parade': 14327, ... }


```

You can also see a list of PHQ Labels in the "Labels" field on the [Search Events](https://control.predicthq.com/search/events) page of the WebApp:

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-09 at 10.36.38 AM.png" alt=""><figcaption><p>The "Labels" field in the WebApp Search Events Page contains a list of PHQ Labels </p></figcaption></figure>

### Labels (Legacy)

Legacy labels are still returned in order to preserve backward compatibility with existing user implementations.

This field is named `labels`.&#x20;

Legacy labels are available for all event categories.





### Usage

* [Labels in the Events API](../../api/events/search-events.md#query-parameters)
