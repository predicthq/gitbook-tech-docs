---
description: Transforming Event Data into ML-Ready Features using Snowpark and Python
---

# Snowpark Method Guide

## Calling the Features API from Snowflake to calculate features

There are two options for calculating features in Snowflake:&#x20;

1. Call the Features API using [Snowpark](https://docs.snowflake.com/en/developer-guide/snowpark/python/index)&#x20;
2. Use the [Python Connector ](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector)or other libraries.&#x20;

If either of the above approaches are taken, the Features API can be called for each location and have the results saved into a table instead of using SQL. These options skip the maintenance of SQL and is the recommended approach if possible.

Below is an example of calling the Features API with Python in Snowpark. This uses the PredictHQ Python SDK. It loops over the **SAVED\_LOCATIONS** table, calls the Features API using the SDK, and outputs the results into a table. So, it achieves a similar result to the SQL method but using the API. This code needs to be modified to include relevant features for what is desired to be fetched.

Note this is not designed to be production-ready code that can be used without modifications. It is provided as an example. Please test and optimize as needed.

### Python Code

{% code fullWidth="true" %}
```python
from snowflake.snowpark import Session
from predicthq import Client
import pandas as pd

# Snowflake connection parameters
connection_parameters = {
  "account": "<your_account>",
  "user": "<your_username>",
  "password": "<your_password>",
  "role": "<your_role>",
  "warehouse": "<your_warehouse>",
  "database": "<your_database>",
  "schema": "<your_schema>"
}

# Create a session
session = Session.builder.configs(connection_parameters).create()

# PredictHQ Client setup
phq = Client(access_token="your_predicthq_access_token")

# Fetch location data from the Snowflake table
locations_df = session.table("SAVED_LOCATIONS").to_pandas()

# Prepare a DataFrame to collect all data
all_data = []

# Iterate over each row in the location DataFrame
for index, location in locations_df.iterrows():
    # Prepare the radius in the appropriate unit
    radius_with_unit = f"{location['RADIUS']}{location['RADIUS_UNIT']}"

    # Call the Features API for each location
    for feature in phq.features.obtain_features(
            active__gte=str(location['DATE_START']),
            active__lte=str(location['DATE_END']),
            location__geo={
                "lon": location['LON'],
                "lat": location['LAT'],
                "radius": radius_with_unit
            },
            phq_attendance_sports__stats=["sum"],
            phq_attendance_conferences__stats=["sum"]

 # add more ML features here like phq_attendance_community, phq_attendance_concerts,
 # phq_attendance_expos, phq_attendance_festivals, phq_attendance_performing_arts,
 # and so on.

    ):
                data_point = {
            'location': location['LOCATION'],
            'date': feature.date,
            'phq_attendance_conferences': getattr(feature.phq_attendance_conferences.stats, 'sum', 0),
            'phq_attendance_sports': getattr(feature.phq_attendance_sports.stats, 'sum', 0)
        }
        all_data.append(data_point)

# Convert all collected data to a DataFrame
results_df = pd.DataFrame(all_data)

# Convert the DataFrame to a Snowpark DataFrame
snow_df = session.create_dataframe(results_df)

# Append the results to the existing Snowflake table
snow_df.write.mode("append").save_as_table("ML_FEATURES_FOR_LOCATIONS")

# Print the contents of the table to verify
print(session.table("ML_FEATURES_FOR_LOCATIONS").show())

# Close the session
session.close()

```
{% endcode %}

### Table Output

The output of the script above should look similar to the data below:

<table data-full-width="true"><thead><tr><th width="226">location</th><th width="178">date</th><th width="321" data-type="number">phq_attendance_conferences</th><th data-type="number">phq_attendance_sports</th></tr></thead><tbody><tr><td>store1-chicago</td><td>2024-01-16</td><td>231</td><td>19329</td></tr><tr><td>store1-chicago</td><td>2024-01-17</td><td>666</td><td>12312</td></tr><tr><td>store1-chicago</td><td>2024-01-18</td><td>215</td><td>0</td></tr><tr><td>store1-chicago</td><td>2024-01-19</td><td>87</td><td>23246</td></tr><tr><td>store1-chicago</td><td>2024-01-20</td><td>395</td><td>19448</td></tr></tbody></table>



### Refer back to [Main Guide](https://app.gitbook.com/o/WGid6DiA3ccvlkmvc17s/s/tNhzHETmXsrWeVBndqqJ/\~/changes/155/integrations/third-party-integrations/snowflake/snowflake-data-science-guide)
