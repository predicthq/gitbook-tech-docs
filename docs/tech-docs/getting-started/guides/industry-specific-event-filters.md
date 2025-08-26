---
description: Industry-level defaults for event relevancy when Beam can’t be applied.
---

# Industry-Specific Event Relevancy Defaults

## Beam Comes First

The most accurate way to identify which events impact your business is with Beam, PredictHQ’s relevancy engine. Beam analyzes your demand data to surface which event categories matter most at each of your locations, so you don’t need to guess.

**If you have demand data, always run Beam first.**

## When You Can’t Use Beam

If demand data isn’t available, we’ve done research to provide industry-level defaults. These include:

* Recommended Feature Groups (categories) per industry
* Minimum Local Rank thresholds to filter out events too small to matter

These are starting points only. Switch to Beam as soon as you can provide demand data.

## Recommended Feature Groups / Categories

<table><thead><tr><th width="236.2265625">Industry</th><th>Recommended Feature Groups / Categories</th></tr></thead><tbody><tr><td>Accommodation</td><td>academic, community, concerts, conferences, expos, festivals, observances, performing-arts, public-holidays, school-holidays, severe-weather, sports</td></tr><tr><td>Parking</td><td>concerts, expos, festivals, observances, performing-arts, public-holidays, school-holidays, sports</td></tr><tr><td>Restaurants</td><td>community, concerts, conferences, expos, festivals, performing-arts, public-holidays, school-holidays, sports</td></tr><tr><td>Retail, CPG</td><td>academic, community, concerts, conferences, expos, festivals, observances, performing-arts, public-holidays, school-holidays, severe-weather, sports</td></tr><tr><td>Transportation</td><td>academic, community, concerts, conferences, expos, festivals, observances, performing-arts, public-holidays, school-holidays, severe-weather, sports</td></tr><tr><td>Tourism, Marketing, and Others</td><td>concerts, expos, festivals, performing-arts, public-holidays, school-holidays, sports</td></tr></tbody></table>

## Minimum Local Rank Thresholds

Local Rank is a location-sensitive scale (0–100, logarithmic) that predicts how much impact an event will have in its immediate vicinity - factoring in population density and local characteristics such as how built-up or accessible an area is ￼. For example, a 1,000-person conference may register a Local Rank of 43 in densely populated Hong Kong and 65 in less crowded Dublin—despite the same PHQ Rank ￼.

**Beam already applies Local Rank filtering automatically** when identifying impactful event types for your demand modeling. However, if you’re setting up filters or queries manually, these thresholds offer a smart default to focus your analysis where it matters until you can rely solely on Beam.

<table><thead><tr><th width="242.7578125">Industry</th><th>Minimum Local Rank</th></tr></thead><tbody><tr><td>Accommodation</td><td>50</td></tr><tr><td>Parking</td><td>60</td></tr><tr><td>Restaurants</td><td>65</td></tr><tr><td>Retail</td><td>35</td></tr><tr><td>Others</td><td>35</td></tr></tbody></table>
