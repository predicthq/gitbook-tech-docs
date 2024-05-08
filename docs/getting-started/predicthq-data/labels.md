# Labels

Event labels are succinct descriptive attributes attached to events that can help with **granular data selection** and **feature engineering** use cases.&#x20;

For example, within the Conferences category, knowing the subject(s) covered within the conference (`science-and-technology`, `educational`, `automotive`, etc.) may help you narrow down on events that are relevant to your business.&#x20;

Each event record has two separate label fields (`phq_labels` and `labels`).

All categories have the new `phq_labels` and will be used by default.&#x20;

Event labels can be searched by using the`phq_labels` field.&#x20;

Some `labels` which repeats the category name such as `label: academic` have been removed.

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

PHQ Labels are **constantly being improved and updated** by our team and LLM models therefore we recommend using [Get Event Counts](../../api/events/get-event-counts.md) to retrieve an **up-to-date and relevant** list of PHQ Labels and the count of events labelled with each, **within your PredictHQ plan**. You could also use [Query Parameters](../../api/events/search-events.md#query-parameters) to retrieve a list and the count of PHQ Labels that match your criteria, e.g. PHQ Labels associated with the sports category or PHQ Labels of events that will be taking place in a specific time and place. Here is an example:

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

You can also see a list of PHQ Labels in the "Labels" field on the [Search Events](https://control.predicthq.com/search/events) page of the Control Center:

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-09 at 10.36.38 AM.png" alt=""><figcaption><p>The "Labels" field in Control Center's Search Events Page contains a list of PHQ Labels </p></figcaption></figure>

### Labels (Legacy)

Legacy labels are still returned in order to preserve backward compatibility with existing user implementations.

This field is named `labels`.&#x20;

Legacy labels are available for all event categories.





### Usage

* [Labels in the Events API](../../api/events/search-events.md#query-parameters)
