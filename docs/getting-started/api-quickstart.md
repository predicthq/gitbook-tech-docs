---
description: >-
  This article describes how to quickly create an access token, view and
  replicate a Streamlit demo app and explore our APIs.
---

# API Quickstart

#### What you need:

1. A PredictHQ account:
   1. Existing users: [log in with your PredictHQ account](https://control.predicthq.com/)
   2. New users: [Sign up for free to get started](https://signup.predicthq.com/).
2. An API Access Token: We'll guide you through creating one below.

## Create an Access Token

Read a more in-depth guide to [creating a new API Client and Token](https://www.predicthq.com/support/how-to-create-an-api-token) or follow the basic steps below:

1. Log into Control Center and visit the [API Clients](https://control.predicthq.com/clients) page under API tools.
2. Select "New Client"&#x20;
   1. Fill in the required information.
   2. Copy the Client Secret, be sure to save this as it will not be shown again.
3. Select Create New Token:
   1. Use the Client Secret to create a new Token.
   2. Keep a copy of your new API Token, as it will not be shown again.
4. Use the new API Access Token in the Authorization header of your API requests as shown in the example below:

## Access Events API

Now you can use the new API Access Token in the `Authorization` header of your API requests as in the example below:

```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    },
    params={
        "q": "taylor swift"
    }
)

print(response.json())
```

{% embed url="https://www.youtube.com/watch?v=vvujroC7Bhs" %}
How to set up and access PredictHQ APIs
{% endembed %}

{% hint style="info" %}
Refer to [filtering-and-finding-relevant-events.md](tutorials/filtering-and-finding-relevant-events.md "mention") for guidance on how to identify events relevant to your business.
{% endhint %}

## Streamlit Demo Apps

To demonstrate how quick and easy it is to build extremely powerful apps using our APIs, we put together some Streamlit demos. All the code is available on GitHub and we encourage you to take the code, modify it, and use your own locations of interest to demo our APIs internally to your team or to simply better understand our technology.

{% content-ref url="guides/streamlit-demo-apps.md" %}
[streamlit-demo-apps.md](guides/streamlit-demo-apps.md)
{% endcontent-ref %}

## Explore the API

Below is a guide to point you in the right direction if you're new to the PredictHQ APIs:

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Events API</strong></td><td><p>Search for real-world events.</p><p></p><p>Customers also use this API to keep a copy of PredictHQ Event data updated in their environment.</p><p></p><p>Every event has unique-to-PredictHQ values like Predicted Attendance, Ranks, Predicted End Times and more.</p></td><td></td><td><a href="../api/events/">events</a></td></tr><tr><td><strong>Broadcasts API</strong></td><td><p>Full broadcast (Live TV) information covering many sporting events in USA.</p><p></p><p>Customers also use this API to keep a copy of PredictHQ Broadcast data updated in their environment.</p><p></p><p>Every Broadcast has Predicted Viewership and more.</p></td><td></td><td><a href="../api/broadcasts/">broadcasts</a></td></tr><tr><td><strong>Features API</strong></td><td><p>Aggregated daily-level features ready for use by ML models.</p><p></p><p>Customers use this API to very quickly get features that can be used by their forecasting (and other) machine-learning models.</p><p></p><p>This API removes all of the hard, time-consuming work of aggregating the individual events from Events API.</p></td><td></td><td><a href="../api/features/">features</a></td></tr><tr><td><strong>Beam API</strong></td><td><p>Decomposition, correlation and feature-importance engine.</p><p></p><p>Customers use this API to understand how events have impacted their business in the past and to know which types of events are likely to impact them in the future so they can prepare for changes in demand.</p></td><td></td><td><a href="../api/beam/">beam</a></td></tr><tr><td><strong>Demand Surge API</strong></td><td>Identify abnormal increases in predicted attendance around your location.<br><br></td><td></td><td><a href="../api/demand-surge/">demand-surge</a></td></tr><tr><td><strong>Suggested Radius API</strong></td><td><p>Takes the guesswork out of working out a suitable radius around your location when searching for events.</p><p></p><p>Customers use this API to more accurately work out a suitable radius around their stores/businesses. Different types of events affect different types of businesses nearer and further away depending on the type.</p><p></p><p>We strongly recommend using Suggested Radius API for each of your locations to remove the guesswork and improve the accuracy.</p></td><td></td><td><a href="../api/suggested-radius/">suggested-radius</a></td></tr><tr><td><strong>Saved Locations API</strong></td><td>Get insights about your locations.</td><td></td><td><a href="../api/saved-locations/">saved-locations</a></td></tr><tr><td><strong>Loop API</strong></td><td>Manage Loop Links and enable submitting events and feedback.</td><td></td><td><a href="../api/loop/">loop</a></td></tr><tr><td><strong>Places API</strong></td><td>Geonames place data.</td><td></td><td><a href="../api/places/">places</a></td></tr></tbody></table>

{% hint style="info" %}
Did you know - [Control Center](https://control.predicthq.com/) uses the same APIs you have access to. One of the easiest ways to learn how to use our APIs is to see it in action in Control Center.
{% endhint %}
