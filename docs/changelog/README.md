---
description: >-
  A record of product updates, data quality improvements, and new features
  across the PredictHQ platform. Updated each release cycle.
---

# Changelog

{% updates format="full" %}
{% update date="2026-05-04" tags="data-quality,enhancement" %}
## Restaurant Predicted Impact Patterns - Holiday & Observance Improvements

Predicted Impact Patterns for the Restaurant industry have been rebuilt for US public holidays, observances, and school holidays using data-driven analysis of real restaurant demand data. This improves forecast accuracy for customers in the restaurant and quick-service retail sectors, particularly around key holiday periods.
{% endupdate %}

{% update date="2026-05-04" tags="enhancement,developer-tools" %}
## MCP Server - OAuth & Connector Improvements

The PredictHQ MCP server now supports OAuth session management and token refresh, and is compatible with Claude connectors (previously only ChatGPT was supported). Event search parameter validation has also been improved. The MCP server allows AI agents and LLMs to query PredictHQ event data directly without building custom API integrations.
{% endupdate %}

{% update date="2026-05-04" tags="python-sdk,enhancement" %}
## Predicted Impact Area in Python SDK

The Python SDK now includes full support for the Predicted Impact Area endpoint, replacing Suggested Radius as the recommended way to define the geographic area around a location.
{% endupdate %}

{% update date="2026-05-04" tags="data-quality,enhancement" %}
## Event Descriptions

Descriptions have been added at scale to attended events that previously had none - approximately 79% of the catalogue. Higher-ranked events were prioritised. This improves the usefulness of event data for customers building AI applications, search, and recommendation features where event context matters beyond title and category. More descriptions to come.
{% endupdate %}

{% update date="2026-03-14" tags="new-feature,events-api,features-api,beam,forecasts-api,saved-locations" %}
## Predicted Impact Area - General Availability

Predicted Impact Area is now generally available across Events API, Features API, Beam. It replaces Suggested Radius as the recommended approach for defining the geographic catchment area around a business location. Unlike a simple radius, Predicted Impact Area uses a data-driven model to define the area where events actually influence demand - accounting for real-world geography. The Suggested Radius endpoint remains available but is no longer the recommended default.
{% endupdate %}

{% update date="2026-01-30" tags="new-feature,saved-locations" %}
## Store Closures & Operating Hours in Saved Locations

Saved Locations now support `closed_days` and `operating_hours` fields via the API and WebApp. Beam and the Forecasts API treat closed days as non-demand days, ensuring that forecasts are not distorted by days when a location is not trading. This is particularly relevant for customers with locations that have non-standard trading patterns - seasonal closures, variable hours, or planned shutdowns.
{% endupdate %}
{% endupdates %}
