---
description: >-
  This guide shows how to authenticate, make your first API call, and retrieve
  structured real-world context from PredictHQ.
---

# API Quickstart

This guide shows how to make your first API call. For guidance on integrating event data into production forecasting or AI systems, see [Core Concepts](core-concepts/).

#### What you need:

1. A PredictHQ account:
   1. Existing users: [log in with your PredictHQ account](https://control.predicthq.com/)
   2. New users: [Sign up for free to get started](https://signup.predicthq.com/).
2. An API Access Token: We'll guide you through creating one below.

## Create an Access Token

Read a more in-depth guide to [creating a new API Token](https://app.gitbook.com/s/Ri9YaBiPckypV66Jggc2/webapp-overview/how-to-create-an-api-token) or follow the basic steps below:

1. Log into the WebApp and visit the [API Tokens](https://control.predicthq.com/tokens) page under API tools.
2. The first time you create a token - enter the name of the token and click "Create Token". For the second and subsequent times click the "Create New Token" button and enter the name, then click Create Token.
3. Click "Copy Token" to copy your token to the clipboard. You can now paste the token into another application. Keep a copy of your new API Token, as it will not be shown again.
4. Use the new API Access Token in the Authorization header of your API requests as shown in the example below

## Access Events API

The Events API returns structured, deduplicated real-world events that can be integrated directly into forecasting, ML, and AI systems.

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

{% embed url="https://youtu.be/_vD5GpQxXRg?si=7QMdU92ATASiELcj" %}
How to set up and access PredictHQ APIs
{% endembed %}

{% hint style="info" %}
For guidance on identifying which events materially impact your demand, [see the Beam guide](core-concepts/what-is-beam.md).
{% endhint %}

## Streamlit Demo Apps

To demonstrate how PredictHQ APIs can be integrated into interactive applications, we provide several Streamlit examples. All the code is available on GitHub and we encourage you to take the code, modify it, and use your own locations of interest to demo our APIs internally to your team or to simply better understand our technology.

{% content-ref url="guides/streamlit-demo-apps.md" %}
[streamlit-demo-apps.md](guides/streamlit-demo-apps.md)
{% endcontent-ref %}

## Next: Understanding Event Driven Demand

Calling the Events API is the first step. Successfully using event data in production systems requires addressing scope, relevance, feature engineering, and explainability.

Read [Event-Driven Demand](core-concepts/event-driven-demand.md)￼ to understand the structural challenges of working with real-world events and how PredictHQ’s APIs are designed to address them.
