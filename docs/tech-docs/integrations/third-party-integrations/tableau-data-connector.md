---
description: Use events data in Tableau
---

# Integrate with Tableau

See [using-event-data-in-tableau.md](../../getting-started/guides/tutorials/using-event-data-in-tableau.md "mention").

## Deprecated option - Tableau Connector

<details>

<summary>Tableau Connector</summary>

* [Log in](https://control.predicthq.com/) to your PredictHQ account or [sign up](https://signup.predicthq.com/) for a trial if you haven't got an account yet.
* In the [API Clients](https://control.predicthq.com/clients) part of the WebApp, create a new API Client. Save the Client Secret somewhere as you won't be able to see it again within the WebApp. Then click "Create an access token". Select the scopes "Account", "Events" and "Places".
* Open Tableau and select "Web Data Connector". Then in the pop up box enter the URL:

```
https://tableau-connector.predicthq.com
```

* Click on "Begin" and enter the Access Token you generated.
* Choose the filters and parameters that you wish to explore. Refer to the [Search Events documentation](../../api/events/search-events.md) for a full list of fields and parameters.
* Click "Get data" to import events into Tableau.

</details>
