---
description: >-
  A record of product updates, data quality improvements, and new features
  across the PredictHQ platform. Updated each release cycle.
---

# Changelog

{% updates format="full" %}
{% update date="2026-10-06" tags="webapp,developer-tools,new-feature" %}
## Bolt - Projects

You can create Projects in Bolt to group your notebooks together. To set up a project so every notebook in it follows the same instructions:

1. For a use case, create a project.
2. Add your notebooks to the project.
3. Set the instructions once.

Share a project with anyone in your organization as a viewer or a collaborator, so your team can work together and see each other's notebooks instead of duplicating work or waiting to be unblocked.

Projects are available in Bolt. Open [Projects in Bolt](https://control.predicthq.com/bolt/projects).
{% endupdate %}

{% update date="2026-10-06" tags="enhancement,developer-tools" %}
## MCP server - listed in ChatGPT's plugin directory

The PredictHQ MCP server is listed in ChatGPT's Plugin Directory, so you can [connect to it straight from the PredictHQ listing](https://chatgpt.com/plugins/plugin_asdk_app_6a9607623e008191ad63b9e4879aa58f) without the custom connector setup.

See the [PredictHQ MCP documentation](https://docs.predicthq.com/ai/mcp) for more details on connecting.
{% endupdate %}

{% update date="2026-09-09" tags="developer-tools,enhancement" %}
## MCP server - general availability & listed in Claude's connectors directory

PredictHQ's MCP server has moved out of beta. MCP access is available as a trial period. Contact your account manager for details.

It's also listed in the [Claude Connectors Directory](https://claude.ai/directory/connectors/predicthq), so connecting the PredictHQ MCP in Claude happens straight through the connectors page, no custom connector setup required.

See the [PredictHQ MCP documentation](https://docs.predicthq.com/ai/mcp) for more details on connecting.
{% endupdate %}

{% update date="2026-08-25" tags="webapp,developer-tools,loop,enhancement" %}
## Bolt - Loop feedback and individual card sharing

Bolt can send missing events and event correction feedback to the PredictHQ team through Loop without you leaving the conversation. Tell Bolt about missing events or flag one that needs correcting and Bolt generates the details needed, confirms them with you, and submits the feedback on your behalf, returning a link so you can follow the progress.

Bolt sharing supports sharing individual cards, so you can share specific results instead of the whole notebook. Share multiple cards from the same notebook and they build up into one view. Recipients can see the visual previews and data, and copy the integration code straight from the cards.
{% endupdate %}

{% update date="2026-08-05" tags="data-quality,enhancement,events-api" %}
## Cricket Predicted Attendance - accuracy improvements in the UK & Australia

Predicted Attendance for cricket events in the UK and Australia is more accurate. We've added observed match attendance as a signal for this category, reducing aggregate prediction error by around 65% across a validation sample of UK and Australian cricket events. Predictions now capture more of the variation in crowd size between fixtures at the same ground, from marquee internationals through to domestic matches.

If you have locations near cricket grounds, this improves match-day demand forecasts and makes each fixture's expected impact easier to explain.
{% endupdate %}

{% update date="2026-08-05" tags="developer-tools,webapp,enhancement" %}
## Bolt - Notebook sharing and UI enhancements

Bolt notebooks can be shared with other users in your organization. Give your team view access to your notebooks with or without the chat history. Your team can pick up a use case you have already worked through, seeing the visual previews and data exactly as you built them, copying the integration code straight from the cards.

We have also improved Bolt's interface to include an activity pane showing exactly which PredictHQ APIs have powered the results in your notebook, live statuses so you know the moment a Beam Analysis or Forecast training run finishes, and streaming code generation so you can follow progress. The notebooks page also has improved search and sorting.
{% endupdate %}

{% update date="2026-06-19" tags="data-quality,enhancement,events-api" %}
## Juneteenth - Standardized holiday naming

PredictHQ publishes Juneteenth under a single, consistent title across US states and territories. Individual states chose their own Juneteenth holiday names before the federal government standardized the federal name in 2021, which meant the same day appeared under several different titles depending on the state and year. All variants are now standardized to **Juneteenth**, with substitute observances published as **Juneteenth (substitute)**.

The change covers US states and the US territories of Puerto Rico, the United States Virgin Islands, the Northern Mariana Islands, and American Samoa.
{% endupdate %}

{% update date="2026-06-19" tags="data-quality,enhancement,places" %}
## Region polygons across the Places index

Region-level places in the Places index that did not already have a polygon or multipolygon geometry now have one, sourced from PredictHQ's high-resolution polygon dataset. This was applied across the 3,885 region-level places in the index.
{% endupdate %}

{% update date="2026-06-16" tags="enhancement,developer-tools" %}
## MCP server - Tech docs search

The PredictHQ MCP server includes tools for searching and retrieving PredictHQ's technical documentation. AI assistants and coding agents can look up API parameters, integration guides, tutorials, and conceptual content directly through the MCP - without leaving the AI client or switching to a browser.
{% endupdate %}

{% update date="2026-06-04" tags="new-feature,developer-tools" %}
## MCP server - Full API coverage

The PredictHQ MCP server exposes tools across the full public API surface, including Events, Broadcasts, Features, Saved Locations, Beam, Forecasts, Predicted Impact Area, and Places & Geocoding.

Previously limited to event search, the MCP server now supports the complete PredictHQ integration workflow through natural language: create Saved Locations, run Beam Analyses, retrieve ML-ready features, build and train forecast models, and query Predicted Impact Area - all without writing API calls directly. Works with any MCP-compatible client including Claude, ChatGPT, Cursor, and Claude Code.
{% endupdate %}

{% update date="2026-06-03" tags="data-quality,enhancement,events-api" %}
## NHL postseason labeling

NHL fixtures played in the postseason carry the postseason label. If you filter or weight NHL games by season stage, you get an accurate stage label on these games.
{% endupdate %}

{% update date="2026-06-01" tags="new-feature,developer-tools,webapp" %}
## Bolt - beta launch

Bolt is available to all users in the PredictHQ WebApp.

Bolt is an AI-native developer environment that guides you through the right PredictHQ workflows for your use case and produces production-ready integration code. Describe what you're building and Bolt handles the rest—Saved Locations, Beam Analysis, calibrated features, forecasts—following PredictHQ best practices throughout.
{% endupdate %}

{% update date="2026-05-27" tags="data-quality,enhancement,events-api" %}
## Concert venue and attendance accuracy

Two refinements to concert data quality. We now identify and filter out events from organizers who announce their venue only shortly before the show - where a large default venue stands in until then - so we don't publish intimate gigs with the attendance profile of a large venue. Separately, we also filter out concert records that arrive attached to a sports team entity.
{% endupdate %}

{% update date="2026-05-25" tags="events-api,features-api,deprecation" %}
## Aviation Rank Retired

Aviation Rank has been retired, and the `aviation_rank` field is no longer populated.
{% endupdate %}

{% update date="2026-05-08" tags="data-quality,enhancement" %}
## Denmark school holidays - municipality-level granularity

We expanded school holidays for Denmark from national-level to municipality-level coverage, reflecting how school holidays are determined locally in Denmark. This applies to all future school holidays and historical data back to 2016, adding 8,900+ events to the dataset. If you use Danish school holiday data, you see increased granularity in event results; historical data has been backfilled to 2016.
{% endupdate %}

{% update date="2026-05-04" tags="data-quality,enhancement" %}
## Restaurant Predicted Impact Patterns - Holiday & Observance Improvements

We updated Predicted Impact Patterns for the Restaurant industry for US public holidays, observances, and school holidays, using data-driven analysis of real restaurant demand data. This improves forecast accuracy if you work in the restaurant and quick-service restaurant sectors, particularly around key holiday periods.
{% endupdate %}

{% update date="2026-05-04" tags="enhancement,developer-tools" %}
## MCP server - OAuth & connector improvements

The PredictHQ MCP server now supports OAuth session management and token refresh, and is compatible with Claude connectors (previously only ChatGPT was supported). Event search parameter validation has also been improved. The MCP server allows AI agents and LLMs to query PredictHQ event data directly without building custom API integrations.
{% endupdate %}

{% update date="2026-05-04" tags="python-sdk,enhancement" %}
## Predicted Impact Area in Python SDK

The Python SDK includes full support for the Predicted Impact Area endpoint, replacing Suggested Radius as the recommended way to define the geographic area around a location.
{% endupdate %}

{% update date="2026-05-04" tags="enhancement,loop" %}
## Loop Links - Feedback on Predicted, Cancelled, and Postponed Events

Loop Links now accept feedback on predicted, cancelled, and postponed events, in addition to active events.
{% endupdate %}

{% update date="2026-05-04" tags="data-quality,enhancement" %}
## Event Descriptions

We added descriptions at scale to attended events that previously had none - approximately 79% of the catalog. We prioritized higher-ranked events. This improves the usefulness of event data for customers building AI applications, search, and recommendation features where event context matters beyond title and category. More descriptions to come.
{% endupdate %}

{% update date="2026-04-29" tags="enhancement,webapp" %}
## Stronger password policy

We updated the password requirements across the PredictHQ WebApp, signup, and account flows. New passwords use a 12-character minimum, with no complexity requirements beyond the minimum length.
{% endupdate %}

{% update date="2026-04-15" tags="data-quality,enhancement" %}
## US Academic Events - 2026–2027 Calendar Year

We added academic events for the 2026–2027 calendar year to PredictHQ's dataset, covering 10,804 events across 958 US institutions.
{% endupdate %}

{% update date="2026-04-02" tags="data-quality,enhancement" %}
## UK Local Authority Boundaries - Updated Polygons

We updated the UK council polygons to reflect the Cumbria and Northamptonshire local government reorganizations, with dedicated boundaries now in place for Cumberland, Westmorland & Furness, North Northamptonshire, and West Northamptonshire. UK school holiday polygons have also been refined so each holiday maps cleanly to a single county rather than overlapping neighboring authorities.

If you match UK school holidays and public holidays to a place ID, you get a single, unambiguous match per event, with boundaries that reflect the current local authority map.
{% endupdate %}

{% update date="2026-03-26" tags="enhancement,webapp,features-api" %}
## Include Predicted Events Toggle in Event Trends

Event Trends now includes an **Include Predicted Events** toggle, bringing it in line with the Features API, which has included Predicted Events by default since early 2025. With the toggle off, `predicted_events.exclude` is applied when querying the Features API. Synthetic events are excluded from the Events API results shown on the page, matching how they are treated in the Features API.
{% endupdate %}

{% update date="2026-03-14" tags="new-feature,events-api,features-api,beam,forecasts-api,saved-locations" %}
## Predicted Impact Area - General Availability

Predicted Impact Area is generally available across Events API, Features API, Beam. It replaces Suggested Radius as the recommended approach for defining the geographic catchment area around a business location. Unlike a simple radius, Predicted Impact Area uses a data-driven model to define the area where events actually influence demand - accounting for real-world geography. Predicted Impact Area replaces the Suggested Radius endpoint, which is deprecated.
{% endupdate %}

{% update date="2026-03-13" tags="data-quality,enhancement,events-api" %}
## Local Public Holidays Scoped to Region

Public holidays that are observed locally rather than nationally are now published at region scope rather than country scope. Italian patron saint holidays are a good example - the Feast of Saint Januarius in Naples, the Feast of St Mark in Venice, and the Feast of St John in Florence, Genoa, and Turin are each celebrated in their own city and region rather than nationwide.

You now see these holidays scoped to the places they apply to.
{% endupdate %}

{% update date="2026-03-09" tags="enhancement,beam,webapp" %}
## Beam Charts - Independent Axis Scaling

The demand and Predicted Attendance axes on Beam Analysis charts now scale independently of one another. Where one series operates at a much larger magnitude than the other, both curves stay readable at full detail - useful when presenting an analysis and talking through how event attendance tracks against actual demand.
{% endupdate %}

{% update date="2026-02-19" tags="data-quality,enhancement" %}
## Northern Ireland Half-Term Holidays - Full-Week Coverage

We publish Northern Ireland half-term school holidays as the full week that schools take off. Where a half-term starts midweek, the dates are extended back to the previous Saturday; where it finishes midweek, they are extended forward to the following Sunday. If you have locations in Northern Ireland, you get school holiday events that cover the complete break.
{% endupdate %}

{% update date="2026-01-30" tags="new-feature,saved-locations" %}
## Store Closures & Operating Hours in Saved Locations

Saved Locations now support `closed_days` and `operating_hours` fields via the API and WebApp. Beam and the Forecasts API treat closed days as non-demand days, ensuring that forecasts are not distorted by days when a location is not trading. This is particularly relevant if you have locations with non-standard trading patterns - seasonal closures, variable hours, or planned shutdowns.
{% endupdate %}

{% update date="2026-01-15" tags="enhancement,beam,forecasts-api" %}
## Local Rank Defaults for Restaurant and Parking

The default Local Rank threshold for the Restaurant and Parking industries is now 50 in both the Beam API and the Forecasts API, lowered from 65 for Restaurant and 60 for Parking.
{% endupdate %}

{% update date="2026-01-08" tags="data-quality,enhancement,events-api" %}
## MLB Spring Training Labelling

MLB Spring Training fixtures now carry both the `mlb` league label and the `pre-season` label, following the addition of the Spring Training competition to the MLB league mapping. We republished the affected events.
{% endupdate %}
{% endupdates %}
