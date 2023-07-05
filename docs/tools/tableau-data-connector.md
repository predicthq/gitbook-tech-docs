---
description: >-
  The Tableau Data Connector allows customers to import PredictHQ events
  directly into Tableau.
---

# Tableau Data Connector

## Requirements

Couple of things to keep in mind:

* The latest version of Chrome, Firefox, Safari or Edge is required.
* Tableau 10.0 or greater is required.
* Some spreadsheet software has trouble with **utf-8** characters so please select **utf-8** encoding when importing a CSV file.

## Instructions

* [Log in](https://control.predicthq.com/) to your PredictHQ account or [sign up](https://signup.predicthq.com/) for a trial if you haven't got an account yet.
* In the [API Clients](https://control.predicthq.com/clients) part of Control Center, create a new API Client. Save the Client Secret somewhere as you won't be able to see it again within Control Center. Then click "Create an access token". Select the scopes "Account", "Events" and "Places".
* Open Tableau and select "Web Data Connector". Then in the pop up box enter the URL:

```
https://tableau-connector.predicthq.com
```

* Click on "Begin" and enter the Access Token you generated.
* Choose the filters and parameters that you wish to explore. Refer to the [Search Events documentation](../api/events/search-events.md) for a full list of fields and parameters.
* Click "Get data" to import events into Tableau.
