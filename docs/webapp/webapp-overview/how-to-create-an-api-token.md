---
description: Instructions on how to create an API token
---

# How to Create an API Token

Choose "[API Tokens](https://control.predicthq.com/tokens)", under API Tools in the left-hand navigation in the WebApp. The first time you create a token you will see the screen below.

<figure><img src="../.gitbook/assets/image (21).png" alt=""><figcaption><p>API Tokens page when you don't have any token created</p></figcaption></figure>

Enter the name for your token and click "**Create Token**".

{% hint style="info" %}
Optional: Select which scopes the token will have access to. If unsure leave all scopes enabled. To use the events API, your token will need to have the "Events" scope. The other scopes determine what other APIs the token has access to.
{% endhint %}

In the next screen choose "**Copy Token**". This copies the token to the clipboard. You can now paste it into another application.

<figure><img src="../.gitbook/assets/image (22).png" alt=""><figcaption><p>Success message after creating a new token</p></figcaption></figure>

{% hint style="warning" %}
**Remember: You MUST save the token somewhere such as in a password manager, as you won't be able to see it again.**
{% endhint %}

Now that you have an API token, you can call the API. See[ PredictHQ Technical documentation ](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/)for more details.

In the guides where you see `Authorization: Bearer $ACCESS_TOKEN` replace `$ACCESS_TOKEN` with your token. For example, see our [API Quickstart Guide](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/api-quickstart).

You can also use the API Explorer feature in our WebApp to explore the capabilities of the API.

### Viewing a List of Tokens

Once you've created a token you will see the screen below that lists shows a list of tokens. From this screen, you can delete tokens, view token scopes, and edit the token name.

<figure><img src="../.gitbook/assets/image (23).png" alt=""><figcaption><p>API Tokens page with a list of created tokens</p></figcaption></figure>

* To delete click on the delete icon
* To edit a tokens name click on the edit icon
* To create another token click on "Create New Token"

### Where Did My API Clients go?

We previously supported the concept of API Clients. These were removed in July 2024. We found that API Clients weren't being used, weren't necessary for using PredictHQ's APIs, and added complexity to the process of creating a token.

For users who previously created API clients, these will be listed in the tokens screen. In the name of each token if the token was created before the change to remove the API Clients option then the API Client name displays in the token name field. The API Client displays in a regular font before the "|" character. Then the API Token name displays in the 2nd part of the API Token name field after the "|" character. Like this:

API Client name | **API Token name**

The API Clients are still present in the database. Please [contact us](https://www.predicthq.com/contact) if you have any issues with this change to remove API Clients.
