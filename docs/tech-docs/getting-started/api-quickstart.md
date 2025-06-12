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

Read a more in-depth guide to [creating a new API Token](../webapp-support/webapp-overview/how-to-create-an-api-token.md) or follow the basic steps below:

1. Log into the WebApp and visit the [API Tokens](https://control.predicthq.com/tokens) page under API tools.
2. The first time you create a token - enter the name of the token and click "Create Token". For the second and subsequent times click the "Create New Token" button and enter the name, then click Create Token.
3. Click "Copy Token" to copy your token to the clipboard. You can now paste the token into another application. Keep a copy of your new API Token, as it will not be shown again.
4. Use the new API Access Token in the Authorization header of your API requests as shown in the example below

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

{% embed url="https://youtu.be/_vD5GpQxXRg?si=7QMdU92ATASiELcj" %}
How to set up and access PredictHQ APIs
{% endembed %}

{% hint style="info" %}
Refer to [filtering-and-finding-relevant-events.md](guides/tutorials/filtering-and-finding-relevant-events.md "mention") for guidance on how to identify events relevant to your business.
{% endhint %}

## Streamlit Demo Apps

To demonstrate how quick and easy it is to build extremely powerful apps using our APIs, we put together some Streamlit demos. All the code is available on GitHub and we encourage you to take the code, modify it, and use your own locations of interest to demo our APIs internally to your team or to simply better understand our technology.

{% content-ref url="guides/streamlit-demo-apps.md" %}
[streamlit-demo-apps.md](guides/streamlit-demo-apps.md)
{% endcontent-ref %}

## Explore the API

Below is a guide to point you in the right direction if you're new to the PredictHQ APIs:

{% hint style="info" %}
Did you know - The [WebApp](https://control.predicthq.com/) uses the same APIs you have access to. One of the easiest ways to learn how to use our APIs is to see it in action in the WebApp.
{% endhint %}
