# Labels

Event labels are succinct descriptive attributes attached to events that can help with **granular data selection** and **feature engineering** use cases.&#x20;

For example, within the Conferences category, knowing the subject(s) covered within the conference (`science-and-technology`, `educational`, `automotive`, etc.) may help you narrow down on events that are relevant to your business.&#x20;

Each event record has two separate label fields.

### PHQ Labels

PHQ Labels are generated through newer Large Language Models (LLMs) and overall achieve a higher standard of **specificity** and **relevance** in highlighting an event's key themes when compared to legacy methods.

This field is named `phq_labels`.

PHQ Labels are available for the following categories:

* Conferences
* Expos
* Festivals
* Performing Arts
* Community

### Labels (Legacy)

Legacy labels are still returned in order to preserve backwards compatibility with existing user implementations.

This field is named `labels`

Legacy labels are available for all event categories.

### Usage

* [Labels in the Events API](../../api/events/search-events.md#query-parameters)
