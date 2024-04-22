---
description: Transforming Event Data into ML-Ready Features in Snowflake
---

# Snowflake Data Science Guide

## This guide and the Features API

This guide is intended to provide guidance on generating machine learning ready features from PredictHQ's intelligent event data in Snowflake similar to the output of the [Features API](https://docs.predicthq.com/getting-started/guides/features-api-guides/increase-accuracy-with-the-features-api), but is not intended to be in parity with the comprehensive results of the Features API. If possible, our primary recommendation is to use the Features API as it provides more comprehensive results. For more information on the Features API, please go to this page and for a more detailed guide on using the Features API for Machine Learning, please see the [Feature Engineering Guide](https://docs.predicthq.com/getting-started/guides/features-api-guides/feature-engineering-guide).

If you don't know which is the best for you, please [reach out](https://www.predicthq.com/contact/sales)!

## Overview

This guide assumes you have access to PredictHQ’s events data in Snowflake via a [Snowflake data share](https://docs.predicthq.com/integrations/third-party-integrations/snowflake). The guide is to show customers how to generate aggregations similar to those provided by the Features API documented in the Features API [list of available features](https://docs.predicthq.com/api/features/get-features#available-features). These features provide daily aggregated data which shows the sum of data for all events happening in a location - for example, the amount of people attending events around a location. The goal is to generate aggregated features that can be used in demand forecasting.

Snowflake's ease of use and integration have made it a popular choice as a cloud data warehouse and is one of the ways PredictHQ's intelligent event data can be accessed for various use cases. In this guide, machine learning ready daily level aggregated event data will be generated on a per-location basis intended to be similar to the data provided by the PredictHQ Features API and ready to be added to a training set as quickly as possible.\


**Requirements:**

1\. A list of locations with their respective latitude & longitude.

2\. Access to PredictHQ's intelligent event data via Snowflake

3\. Understanding of SQL & Snowflake's SQL Interface.\


**The process to follow:**

1. Get the Suggested Radius for Each Location
2. Create the input table filled with locations
3. Set the date range that you want to retrieve data for
4. Choose which method to follow
   1. [Snowpark Method](https://app.gitbook.com/o/WGid6DiA3ccvlkmvc17s/s/tNhzHETmXsrWeVBndqqJ/\~/changes/155/integrations/third-party-integrations/snowflake/snowflake-data-science-guide/snowpark-method-guide)
   2. [SQL Method](https://app.gitbook.com/o/WGid6DiA3ccvlkmvc17s/s/tNhzHETmXsrWeVBndqqJ/\~/changes/155/integrations/third-party-integrations/snowflake/snowflake-data-science-guide/sql-method-guide)
5. Use the output in machine learning demand forecasting models or for other applications

## Get the Suggested Radius for each Location

When querying events at the location level, a common way to retrieve those events is with a latitude, longitude, and radius to get the events within a given area. But, a common gap is knowing what radius to use when searching for events. Insert the Suggested Radius API.&#x20;

The [Suggested Radius API](https://docs.predicthq.com/api/suggested-radius/get-suggested-radius) returns a radius that can be used to find attended events around a given location and takes into account a number of different factors like population density, the surrounding street network, and the industry vertical of the location.&#x20;

As a first step, it is recommended to get the suggested radius for each location before moving forward with the guide. Below is an example of how to query the Suggested Radius API for a list of locations using the [PredictHQ Python SDK](https://docs.predicthq.com/integrations/sdks/python-sdk). Note: this code will need to be run in a separate environment than Snowflake.&#x20;

For more information on the Suggested Radius API, visit [our documentation](https://docs.predicthq.com/api/suggested-radius/get-suggested-radius).

```python
# The code below uses the PredictHQ Python SDK
# https://docs.predicthq.com/integrations/sdks/python-sdk
from predicthq import Client 

# Please copy paste your access token here
# or read our Quickstart documentation if you don't have a token yet
# https://docs.predicthq.com/guides/quickstart/
ACCESS_TOKEN = 'ABC123'

phq_client = Client(access_token=ACCESS_TOKEN)

# Specify a list of locations to retrieve the suggested radius for
list_of_locations = [
    {'name': 'store1-chicago', 'latitude': '41.81310', 'longitude': '-87.65860', 'industry': 'retail'},
    {'name': 'Hyde Park', 'latitude': '51.50736', 'longitude': '-0.16411', 'industry': 'accommodation'},
    {'name': 'store10-new-york', 'latitude': '40.730610', 'longitude': '-73.935242', 'industry': 'retail'},
]

for location in list_of_locations:
	# Get suggested radius for a given location and the industry of interest
	# to be used when retrieving events. supported industries: 'parking', 'restaurants', 'retail', 'accommodation'
	suggested_radius = phq_client.radius.search(
            location__origin=f"{location['latitude']},{location['longitude']}", 
            radius_unit="mi", 
            industry=location["industry"]
    )
	print(f"Suggested Radius for {location['name']} with the industry {location['industry']}: {suggested_radius.radius} {suggested_radius.radius_unit}")

```



## Create Input table used in both methods

To be able to reference the locations further in the guide, a table of locations is required as input (called **SAVED\_LOCATIONS**). Please fill this table with \
The **SAVED\_LOCATIONS** input table requires this format:

<table data-full-width="true"><thead><tr><th width="190">location</th><th>latitude</th><th>longitude</th><th data-type="number">radius</th><th>radius_unit</th><th>date_start</th><th>date_end</th></tr></thead><tbody><tr><td>store1-chicago</td><td>41.81310</td><td>-87.65860</td><td>4.11</td><td>mi</td><td>2023-07-01</td><td>2023-12-31</td></tr><tr><td>Hyde Park</td><td>51.50736</td><td>-0.16411</td><td>2.06</td><td>mi</td><td>2024-01-01</td><td>2024-03-31</td></tr><tr><td>store10-new-york</td><td>40.73061</td><td>-73.93524</td><td>null</td><td>...</td><td>...</td><td>...</td></tr></tbody></table>

* **location**: a unique identifier for the location.
* **latitude**/**longitude**: it is recommended to include 5 decimal places.
* **radius**: the value returned from the using the Suggested Radius API.
* **radius\_unit**: coded for either “km” (kilometers) or “mi” (miles).
* **date\_start**/**date\_end**: the date range for the data to be returned. Can be changed.

Here is the input table used when running this code. Note the datatypes of each column for the inputs.

{% code fullWidth="true" %}
```sql
CREATE OR REPLACE TEMP TABLE saved_locations (
    location STRING
    , lat STRING
    , lon STRING
    , radius FLOAT
    , radius_unit STRING
    , date_start DATE
    , date_end DATE);

INSERT INTO saved_locations (location, lat, lon, radius, radius_unit, date_start, date_end)
VALUES ('Hyde Park', '51.5073638', '-0.1641135', 2.06, 'mi'   
        , DATE_TRUNC('MONTH', DATEADD(MONTH, -3, CURRENT_DATE()))       --Start of 3 months ago
        , DATEADD(DAY, -1, DATE_TRUNC('MONTH', CURRENT_DATE()))         --End of last month
        )
;
```
{% endcode %}

By default, 3 months of historical data is returned. If the model is being trained, we recommend, at minimum, two years of historical data, but this can be changed as needed. If you are forecasting for a future period then the date range should reflect the period you are forecasting for - e.g. the next 2 weeks.

Once the input table is in the format of the above, the below code shapes that table to be in a day-by-day format of the input called **SAVED\_LOCATIONS\_DAILY:**

{% code fullWidth="true" %}
```sql
----split the table out into having one day equals one row between the date range.
CREATE OR REPLACE TEMP TABLE saved_locations_daily AS
select
    date(date_start) + value::int as date,
    s.location,
    s.lat,
    s.lon,
    s.radius,
    lower(s.radius_unit) as radius_unit        --forcing the lower in case of data entry mistakes
   from saved_locations s,
     table(flatten(array_generate_range(0, datediff('day', date_start, date_end) + 1))) t
;
```
{% endcode %}

## Choose which Method to use

### 1. [Snowpark Method Guide](snowpark-method-guide.md)

Call the Features API with Python and save the output ML Features into Snowflake.

### 2. [SQL Method Guide](sql-method-guide.md)

Use SQL in Snowflake to run over the events table and create the ML Features.

## Integrating PredictHQ Features into Your Demand Forecasting Model

The **ML\_FEATURES\_FOR\_LOCATIONS** table offers ready-to-use features for forecasting models. Merge these features with current demand data using the location and date as keys. Train models using historical data from this table and use future data for forecasting.&#x20;

\
For more information on creating machine learning-ready features from PredictHQ’s intelligent event data, check out the [Feature Engineering Guide](https://github.com/predicthq/phq-data-science-docs/blob/master/feature-engineering-guide/feature\_engineering\_guide.ipynb) or this blog on [Enhancing Demand Forecasting with PredictHQ and PowerBI: A Technical Exploration](https://www.predicthq.com/blog/enhancing-demand-forecasting-with-predicthq-and-powerbi-a-technical). While these resources discuss the Features API, remember to use the **ML\_FEATURES\_FOR\_LOCATIONS** table instead.
