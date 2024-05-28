---
description: >-
  Take PredictHQ API data and load it into a data warehouse, in this example,
  GCP BigQuery
---

# Loading PredictHQ’s Event Data into your Data Warehouse

This guide outlines the process for integrating PredictHQ's Events data into your data lake. It is common for customers to want to get data from our APIs and store it in their data lake. To support this, we have created this guide to help you with the integration process

We use Google Cloud Platform (GCP) as our primary example, but the methods for structuring the data table and making PredictHQ Events API calls can be applied to various data management systems. This guide is designed for users with a basic understanding of GCP or similar data warehousing solutions and the necessary permissions to use them.

Please note that this guide focuses exclusively on integrating PredictHQ’s Events API data and does not cover the Features API.

If you are using Snowflake or ADX for your data lake PredictHQ integrates with those products. See [Receive Data via Snowflake](https://docs.predicthq.com/integrations/third-party-integrations/snowflake) and [Receive Data via AWS Data Exchange](https://docs.predicthq.com/integrations/third-party-integrations/aws-data-exchange) for details.

## Overview

This guide details the data structure of our Events API within a data warehouse environment and outlines two methodologies for creating an Events data table in GCP.

Throughout this guide, we will use the fictional example from our [Filtering Guide](https://docs.predicthq.com/getting-started/guides/tutorials/filtering-and-finding-relevant-events), "Tom’s Pizzeria". This scenario will give us a practical illustration of the methods described and demonstrate how to tailor API queries to specific business needs. For an understanding of how parameters were selected for this example, refer to the [Filtering Guide](https://docs.predicthq.com/getting-started/guides/tutorials/filtering-and-finding-relevant-events).

**Requirements**:

* Access to PredictHQ Data&#x20;
  * JSONL: Requires a PredictHQ account.[ Sign up here](https://predicthq.com/signup) if you don’t already have one.
  * API: An API Access Token is necessary for accessing the data programmatically.
* GCP permissions:
  * Ensure you have "BigQuery Data Owner" and "BigQuery User" permissions over the BigQuery environment.
  * A GCP BigQuery Service Account and its corresponding JSON key are required.[ See the official documentation](https://cloud.google.com/iam/docs/service-account-overview) for details.

## Scenario: Tom’s Pizzeria

In this guide, we'll explore a hypothetical use case for “Tom’s Pizzeria”, a chain of restaurants with locations throughout the US headquartered in Seattle, Washington. Tom is interested in understanding how local events might influence his business operations and customer flow. Tom’s inventory system, website, and tools run off GCP. Tom wants to use event data in his staffing and inventory management systems to help anticipate the demand caused by events. He wants to show upcoming events near stores to his staff. To do this he needs to download events into his data lake.

For comprehensive details on selecting appropriate filters for this scenario, refer to our [Filtering Guide](https://docs.predicthq.com/getting-started/guides/tutorials/filtering-and-finding-relevant-events). This guide will help us understand which events could impact Tom's business and how to configure our data queries accordingly. For our load into GCP, we want to bring through a larger number of events and then filter down to a specific pizzeria location using BigQuery once loaded. See [Querying the Loaded Data](loading-predicthqs-event-data-into-your-data-warehouse.md#querying-the-loaded-data) section for more.

Tom's Data Parameters:

* **Attended Categories**: community, conferences, concerts, expos, festivals, performing-arts, sports.
* **Date Range**: Events active within the range June 1, 2024, to June 30, 2024.
* **Event Rank**: Events with a rank greater than 30 indicate a significant likelihood of impacting local traffic and attendance.
* **Event Status**: Both ‘active’ and ‘predicted’ events to ensure a comprehensive overview.
* **Location**: Bring through all of Seattle first, and Tom can filter for his locations once it’s in BigQuery using our [Suggested Radius API](https://docs.predicthq.com/api/suggested-radius/get-suggested-radius).

For the purposes of this guide, we have limited the example load to a single city for Tom to filter on. Users may bring through as much data as they have access to or require when doing an actual load. We find with data warehouse customers they may pull down all data they have access to into their data warehouse and then query it for relevant locations and data from their applications.



## Data Load Methods

There are several methods available for integrating PredictHQ data with GCP BigQuery or other data warehouse solutions. This guide outlines two primary approaches, both compatible with each other’s data structure. Regardless of the method chosen for the initial data load, ongoing updates will require API code.

**JSONL File Upload Method**: This method provides a straightforward, code-free approach to data upload, by [exporting data](https://www.predicthq.com/support/getting-started-with-data-exporter) from PredictHQ’s [Control Center](https://control.predicthq.com/search/events) web application. We recommend using JSONL uploads for the initial population of your data lake, especially in cases where there is a substantial volume of data, such as multiple years of historical data. Subsequent updates should be managed through API calls to ensure the data remains current.

**API Connection Method**: Connect to the PredictHQ Events API to download the latest data from the API into your data lake. This guide takes you through using the Python API connection method for GCP but similar steps would apply to other programming languages. Events data is dynamic with events changing all the time as events are canceled, postponed, shift location, or have other details change. Also, new events are being announced all the time. We recommend having a process that updates your data on a regular frequency, such as daily.

This guide will walk you through the initial data load, providing you with the tools and understanding necessary to create a robust connection to GCP. You'll learn how to structure your data effectively within your warehouse, setting the stage for potential automation and regular updates that you can implement as needed.



## Table Data Structure

Regardless of the method chosen for initial data creation and loading, the table structure remains consistent. This ensures that both methods are interchangeable, delivering data in a uniform format. The data structure for the table is detailed below:



| Field Name                          | Datatype  | Mode     |
| ----------------------------------- | --------- | -------- |
| id                                  | STRING    | REQUIRED |
| parent\_event                       | JSON      | NULLABLE |
| title                               | STRING    | NULLABLE |
| alternate\_titles                   | JSON      | NULLABLE |
| description                         | STRING    | NULLABLE |
| category                            | STRING    | NULLABLE |
| labels                              | JSON      | NULLABLE |
| phq\_labels                         | JSON      | NULLABLE |
| rank                                | INTEGER   | NULLABLE |
| local\_rank                         | INTEGER   | NULLABLE |
| phq\_attendance                     | INTEGER   | NULLABLE |
| entities                            | JSON      | NULLABLE |
| duration                            | INTEGER   | NULLABLE |
| start                               | TIMESTAMP | NULLABLE |
| end                                 | TIMESTAMP | NULLABLE |
| pdated                              | TIMESTAMP | NULLABLE |
| first\_seen                         | TIMESTAMP | NULLABLE |
| timezone                            | STRING    | NULLABLE |
| location                            | JSON      | NULLABLE |
| geo                                 | JSON      | NULLABLE |
| scope                               | STRING    | NULLABLE |
| country                             | STRING    | NULLABLE |
| place\_hierarchies                  | JSON      | NULLABLE |
| state                               | STRING    | NULLABLE |
| private                             | BOOLEAN   | NULLABLE |
| impact\_patterns                    | JSON      | NULLABLE |
| predicted\_event\_spend             | INTEGER   | NULLABLE |
| predicted\_event\_spend\_industries | JSON      | NULLABLE |

## JSONL file Upload Method

This method is recommended for large data uploads, as it efficiently manages the transfer of large volumes of data better than direct API calls.

### Search Control Center and Export JSONL

To locate and export the relevant event data into a JSONL file, we utilize the PredictHQ [Control Center Search](https://control.predicthq.com/search/events). This tool allows for precise querying of events based on specific criteria, ensuring that you retrieve only the most relevant information for your needs. For detailed instructions on optimizing your search with the Control Center, please refer to [this guide](https://www.predicthq.com/support/control-center-search) on Control Center search capabilities.

Typically you may download all the data you have access to into your data warehouse. In that case, run a search for all events and download them.

In the context of our example [Scenario](loading-predicthqs-event-data-into-your-data-warehouse.md#scenario-toms-pizzeria) for Tom's Pizzeria, they would be downloading events for all of the US and then querying for specific locations. Many customers may bulk load all the data they have access to by exporting it all and then importing it into their data lake. In this example, we’ll download events only for Seattle.\
To do that, we searched for Seattle in the Control Center for the relevant period, status, and attended categories.

<figure><img src="../../../.gitbook/assets/CC Filters.png" alt=""><figcaption><p>Control Center Search for Seattle ready for Export</p></figcaption></figure>

After configuring your filters and executing the search, simply select the Export option. For more details on exporting see the[ CSV Export Guide](https://www.predicthq.com/support/getting-started-with-data-exporter) except select the JSONL file format instead of CSV. This JSONL can then be directly uploaded to your BigQuery setup, as detailed in the [next section](loading-predicthqs-event-data-into-your-data-warehouse.md#create-a-table-via-jsonl-upload).

### Create a Table via JSONL Upload

Setting up a BigQuery table with a JSONL file is a straightforward process, provided you have the necessary permissions on GCP. Before beginning, ensure you are clear about which dataset will host the data. Here are the steps to create the table once you have found and highlighted the dataset in GCP BigQuery:

1. **Click Create Table**: Navigate to the dataset you wish to create the table in, click the hamburger menu and select “Create Table”.

<figure><img src="../../../.gitbook/assets/Create Table.png" alt=""><figcaption><p>Select destination dataset and use the hamburger menu to create table</p></figcaption></figure>

2. **Select the File Location**: Select the JSONL export that you have downloaded somewhere on your computer.
3. **Name the Table**: Give the table about to be created a name that suits

<figure><img src="../../../.gitbook/assets/table upload details.png" alt=""><figcaption><p>table upload example details. Replace with your own dataset and table name</p></figcaption></figure>

4. **Manually Define Schema**: This step involves specifying the schema details manually. You must accurately define each column, ensuring that the datatype and column names precisely match those in the [Table Data Structure](loading-predicthqs-event-data-into-your-data-warehouse.md#table-data-structure). Any discrepancies in spelling or datatype will lead to errors during the upload process. While you have flexibility to modify the schema by adding or removing columns based on your specific data requirements, this guide focuses on the recommended fields we suggest including.

<figure><img src="../../../.gitbook/assets/JSONL BigQuery structure.png" alt=""><figcaption><p>Follow our <a href="loading-predicthqs-event-data-into-your-data-warehouse.md#table-data-structure">Table Data Structure</a> and check for spelling</p></figcaption></figure>

5. **Advanced Options**: Expand the Advanced Options and tick the checkbox “Unknown Values”. This setting allows the system to gracefully handle missing information in specific columns of some records, ensuring that rows with incomplete data are not rejected or throw errors during the upload process.
6. **Create the Table**: Click the "Create Table" button to finalize the creation.

<figure><img src="../../../.gitbook/assets/JSON Unkown Values select.png" alt=""><figcaption><p>tick "Unknown values" and you're ready to create</p></figcaption></figure>

This method allows initializing your BigQuery table with a JSONL dataset suitable for bulk data uploads. However, it does not support ongoing data refreshes. See the [Keep Event Data Updated](loading-predicthqs-event-data-into-your-data-warehouse.md#keep-event-data-updated) section for advice on setting up a regularly updated table after initialization.



## API Connection Method

This method works well for smaller datasets as initial upload and must be used for continuous updates to the table as recommended in our [Keep Event Data Updated](loading-predicthqs-event-data-into-your-data-warehouse.md#keep-event-data-updated) section.

### Table Creation Code

To establish the required data structure in BigQuery, you can utilize the following Python script. This script explicitly defines the columns and data types as laid out in our [Table Data Structure](loading-predicthqs-event-data-into-your-data-warehouse.md#table-data-structure), configuring them precisely as needed for your BigQuery table. Before executing this script, ensure you have the following prerequisites:

* **SERVICE\_ACCOUNT\_JSON**: This is your service account JSON key, which is typically stored in a secure file. If your organization uses a different method to handle service account keys, please modify the code accordingly.
* **dataset\_id**: Specify whether this is a new dataset or an existing one in which you want to place this table.
* **table\_id**: Determine a name for your new PredictHQ data table in BigQuery.

It is advisable to manage this table creation code separately from other data processing scripts to maintain clarity and ease of updates.

{% code lineNumbers="true" fullWidth="true" %}
```python
from google.cloud import bigquery

#Set Service Account Key connection
SERVICE_ACCOUNT_JSON='~/file_location/service_account_key.json' 

# Set BigQuery variables
dataset_id = "[dataset_name]"
table_id = "[table_name]"

# Initialize the BigQuery client
client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)

# Manually create schema
schema = [
    bigquery.SchemaField("id", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("parent_event", "JSON"),
    bigquery.SchemaField("title", "STRING"),
    bigquery.SchemaField("alternate_titles", "JSON"),
    bigquery.SchemaField("description", "STRING"),
    bigquery.SchemaField("category", "STRING"),
    bigquery.SchemaField("labels", "JSON"),
    bigquery.SchemaField("phq_labels", "JSON"),
    bigquery.SchemaField("rank", "INTEGER"),
    bigquery.SchemaField("local_rank", "INTEGER"),
    bigquery.SchemaField("phq_attendance", "INTEGER"),
    bigquery.SchemaField("entities", "JSON"),
    bigquery.SchemaField("duration", "INTEGER"),
    bigquery.SchemaField("start", "TIMESTAMP"),
    bigquery.SchemaField("end", "TIMESTAMP"),
    bigquery.SchemaField("updated", "TIMESTAMP"),
    bigquery.SchemaField("first_seen", "TIMESTAMP"),
    bigquery.SchemaField("timezone", "STRING"),
    bigquery.SchemaField("location", "JSON"),
    bigquery.SchemaField("geo", "JSON"),
    bigquery.SchemaField("scope", "STRING"),
    bigquery.SchemaField("country", "STRING"),
    bigquery.SchemaField("place_hierarchies", "JSON"),
    bigquery.SchemaField("state", "STRING"),
    bigquery.SchemaField("private", "BOOLEAN"),
    bigquery.SchemaField("impact_patterns", "JSON"),
    bigquery.SchemaField("predicted_event_spend", "INTEGER"),
    bigquery.SchemaField("predicted_event_spend_industries", "JSON")
]

#basic create code with no error handling
dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)
table = bigquery.Table(table_ref, schema=schema)
table = client.create_table(table)  # Make an API request to create the table.
print("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))
```
{% endcode %}

This script sets up the initial table structure within BigQuery, providing a foundation for subsequent data loads.

### Extract from Events API

This section outlines the process of querying the PredictHQ Events API using Python, using the example for Tom's Pizzeria. This approach is designed to ensure the data extracted is directly relevant to Tom’s operational needs. The methodology and rationale behind the data extraction parameters used below are explained in the [Scenario](loading-predicthqs-event-data-into-your-data-warehouse.md#scenario-toms-pizzeria) section of this guide.

Before initiating the script, ensure you have configured the following prerequisites:

* **phq\_access\_token**: Insert your PredictHQ access token here. For enhanced security, consider referencing the token indirectly if you prefer not to hard-code it into your script.
* **SERVICE\_ACCOUNT\_JSON**: This is your Google Cloud Platform service account JSON key, which should be securely stored. Adjust the access method in the script if your organization's practices differ.
* **dataset\_id**: Designate whether this is a new or existing dataset in which you plan to house the PredictHQ data.
* **table\_id**: Assign a name to your new PredictHQ data table in BigQuery.
* **params**: Modify these parameters as needed to align with the data you intend to extract from PredictHQ.

This Python script is crafted to fetch the necessary data from the Events API. This method loops through the paginated response from the API and pulls all results and columns. The [next section](loading-predicthqs-event-data-into-your-data-warehouse.md#transform-api-responses) covers transforming this data before we push for upload.\
For more details on any of the parameters we’ve used in the code below, see our [Events API](https://docs.predicthq.com/api/events/search-events) documentation, keeping in mind our [Scenario](loading-predicthqs-event-data-into-your-data-warehouse.md#scenario-toms-pizzeria) to pull attended results in Seattle for Tom.

{% code lineNumbers="true" fullWidth="true" %}
```python
import time
import requests
import json
from google.cloud import bigquery

base_url = "https://api.predicthq.com/v1/events"
access_token = "[phq_phq_access_token]"  
dataset_id = "[dataset_name]"
table_id = "[table_name]" 
SERVICE_ACCOUNT_JSON='~/file_location/service_account_key.json'

headers = {
    "Authorization": f"Bearer {access_token}",  
    "Accept": "application/json"
}

params = {      # adjust these parameters to correspond to the data you want to pull down
    "categories": "community,conferences,concerts,expos,festivals,performing-arts,sports",
    "place.scope": "5809844",     #Seattle geonames ID
    "active.gte": "2024-06-01",
    "active.lte": "2024-06-30",
    "state": "active,predicted",
    "limit": 500       # Maximum number of events per page
}

# Initialize the BigQuery client
client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)

def fetch_all_pages(base_url, headers, params):
    print("calling Events API")
    
    results = []
    next_url = base_url  # Start with the base URL

    while next_url:
        response = requests.get(next_url, headers=headers, params=params)
        params = None  # After the first request, prevent re-sending initial parameters
        if response.status_code == 200:
            data = response.json()
            results.extend(data.get('results', []))
            next_url = data.get('next')  # Update the next_url from the 'next' field in the response
        else:
            print(f"Failed to fetch data: {response.status_code}, Message: {response.text}")
            break

    print("total events fetched", len(results))

    return results

events_data = fetch_all_pages(base_url, headers, params)

```
{% endcode %}

### Transform API Responses

To ensure seamless compatibility with the BigQuery table structure, we run a transformation function applied to the data retrieved from the Events API in the previous step. The function performs essential adjustments, including:

* Handling null or empty responses to maintain data integrity.
* Restricting output to only the columns defined in our table structure ensures consistency and relevance.
* Formatting complex fields to JSON, suitable for BigQuery ingestion.

Append this transformation code to the extraction code from above. After successful data extraction and transformation, the processed data is ready for loading into BigQuery.



{% code lineNumbers="true" fullWidth="true" %}
```python
def prepare_data_for_bigquery(events_data):
    schema_fields = set([
        'id', 'parent_event', 'title', 'alternate_titles', 'description', 'category', 'labels',  
        'phq_labels', 'rank', 'local_rank', 'phq_attendance', 'entities', 'duration', 'start', 
        'end', 'updated', 'first_seen', 'timezone', 'location', 'geo', 'scope', 'country',
        'place_hierarchies', 'state', 'private', 'impact_patterns',
        'predicted_event_spend', 'predicted_event_spend_industries'
    ])

    # Fields that are to be in JSON format
    json_fields = {'phq_labels', 'entities', 'geo', 'location', 'impact_patterns', 
                   'predicted_event_spend_industries', 'labels', 'place_hierarchies', 
                   'parent_event', 'alternate_titles'} 

    cleaned_events = []

    for event in events_data:
        filtered_event = {}

        for key in schema_fields:
            if key in event and event[key] is not None:
                # If key is in json_fields, serialize it as JSON string
                if key in json_fields:
                    # Ensure the data is properly structured as a JSON string
                    filtered_event[key] = json.dumps(event[key])
                else:
                    filtered_event[key] = event[key]
            else:
                # Provide default None for missing fields, or an empty JSON structure as appropriate
                filtered_event[key] = 'null' if key in json_fields else None

        cleaned_events.append(filtered_event)

    return cleaned_events

transformed_events_data = prepare_data_for_bigquery(events_data)

```
{% endcode %}

### Load Data into the Table

Once the data has been successfully extracted from the API and transformed to meet our [schema requirements](loading-predicthqs-event-data-into-your-data-warehouse.md#table-data-structure), the next step involves loading this data into the previously established BigQuery table. This process utilizes Python code integrated with the BigQuery API to load the data.

Below is the code block that you need to append to the end of the extraction and transformation script. It includes a basic retry mechanism to handle occasional upload failures, which is common in network-related operations. However, depending on your requirements for reliability and data integrity, you might consider implementing a more advanced retry logic.

{% code lineNumbers="true" fullWidth="true" %}
```python
def insert_data_with_retry(table_ref, data, max_attempts=3):
    for attempt in range(max_attempts):
        errors = client.insert_rows_json(table_ref, data)
        if not errors:
            print("Data inserted successfully.")
            return
        else:
            print(f"Attempt {attempt + 1} failed with errors: {errors}")
            time.sleep(2)  # Wait for 2 seconds before the next retry

    print("Failed to insert data after several attempts.")

table_ref = client.dataset(dataset_id).table(table_id)

#Run insert data with retry
insert_data_with_retry(table_ref, transformed_events_data)
```
{% endcode %}

With this step completed, the data from PredictHQ Events API is now populated into your BigQuery table and is ready for analytical querying. This setup initially caters to a single load of data; however, to maintain the relevance and timeliness of your data, consider adapting this script to periodically update the dataset based on changes reflected in the "updated" timestamp column of the source data. See the [section below](loading-predicthqs-event-data-into-your-data-warehouse.md#keep-event-data-updated) on updating your data.

Below is the full code where we have combined all these 3 code parts into one executable.

<details>

<summary>Full Code</summary>

{% code lineNumbers="true" fullWidth="true" %}
```python
import time
import requests
import json
from google.cloud import bigquery

bse_url = "https://api.predicthq.com/v1/events"
access_token = "[phq_phq_access_token]"  
dataset_id = "[dataset_name]"
table_id = "[table_name]" 
SERVICE_ACCOUNT_JSON='~/file_location/service_account_key.json'


headers = {
    "Authorization": f"Bearer {access_token}",  
    "Accept": "application/json"
}

params = {      # adjust these parameters to correspond to the data you want to pull down
    "categories": "community,conferences,concerts,expos,festivals,performing-arts,sports",
    "place.scope": "5809844",     #Seattle geonames ID
    "active.gte": "2024-06-01",
    "active.lte": "2024-06-30",
    "state": "active,predicted",
    "limit": 500       # Maximum number of events per page
}

# Initialize the BigQuery client
client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)

def fetch_all_pages(base_url, headers, params):
    print("calling Events API")
    
    results = []
    next_url = base_url  # Start with the base URL

    while next_url:
        response = requests.get(next_url, headers=headers, params=params)
        params = None  # After the first request, prevent re-sending initial parameters
        if response.status_code == 200:
            data = response.json()
            results.extend(data.get('results', []))
            next_url = data.get('next')  # Update the next_url from the 'next' field in the response
        else:
            print(f"Failed to fetch data: {response.status_code}, Message: {response.text}")
            break

    print("total events fetched", len(results))

    return results

events_data = fetch_all_pages(base_url, headers, params)

def prepare_data_for_bigquery(events_data):
    schema_fields = set([
        'id', 'parent_event', 'title', 'alternate_titles', 'description', 'category', 'labels',  
        'phq_labels', 'rank', 'local_rank', 'phq_attendance', 'entities', 'duration', 'start', 
        'end', 'updated', 'first_seen', 'timezone', 'location', 'geo', 'scope', 'country',
        'place_hierarchies', 'state', 'private', 'impact_patterns',
        'predicted_event_spend', 'predicted_event_spend_industries'
    ])

    # Fields that are to be in JSON format
    json_fields = {'phq_labels', 'entities', 'geo', 'location', 'impact_patterns', 
                   'predicted_event_spend_industries', 'labels', 'place_hierarchies', 
                   'parent_event', 'alternate_titles'} 

    cleaned_events = []

    for event in events_data:
        filtered_event = {}

        for key in schema_fields:
            if key in event and event[key] is not None:
                # If key is in json_fields, serialize it as JSON string
                if key in json_fields:
                    # Ensure the data is properly structured as a JSON string
                    filtered_event[key] = json.dumps(event[key])
                else:
                    filtered_event[key] = event[key]
            else:
                # Provide default None for missing fields, or an empty JSON structure as appropriate
                filtered_event[key] = 'null' if key in json_fields else None

        cleaned_events.append(filtered_event)

    return cleaned_events

transformed_events_data = prepare_data_for_bigquery(events_data)

def insert_data_with_retry(table_ref, data, max_attempts=3):
    for attempt in range(max_attempts):
        errors = client.insert_rows_json(table_ref, data)
        if not errors:
            print("Data inserted successfully.")
            return
        else:
            print(f"Attempt {attempt + 1} failed with errors: {errors}")
            time.sleep(2)  # Wait for 2 seconds before the next retry

    print("Failed to insert data after several attempts.")

table_ref = client.dataset(dataset_id).table(table_id)

#Run insert data with retry
insert_data_with_retry(table_ref, transformed_events_data)
```
{% endcode %}

</details>

## Keep Event Data Updated

Event data is dynamic and events can change frequently. This happens when events are canceled, posted, or have details updated. Also, PredictHQ’s pipeline is constantly fetching new events so new future events are always being added and can be downloaded via the API.

To keep your data updated see [Keep Data Updated via API](https://docs.predicthq.com/integrations/integration-guides/keep-data-updated-via-api). Use a similar code to [that above](loading-predicthqs-event-data-into-your-data-warehouse.md#api-connection-method) using the ‘updated’ parameter to filter for recently changed events. This will extract all new events and updates to events. Check for events updated since your last table update using the ‘updated’ timestamp column. You will need to code for updating and replacing the data in BigQuery according to your preferred data update standards, but the structure will be the same as outlined above.

We recommend running a daily update process (such as a cron job) that calls the PredictHQ API and updates the data in your data lake.

## Querying the Loaded Data

Once the data is successfully loaded into BigQuery, you can begin querying it to derive insights relevant to your use case. This section provides an example of a BigQuery SQL query tailored to Tom’s scenario as outlined earlier. While the initial data load might have utilized specific filters via the Control Center or API parameters, it's often useful to perform additional queries directly within BigQuery. This capability is particularly valuable if you have loaded a broader dataset and need to perform dynamic or complex filtering post-load.

Some common fields to query are:

* **category:** filter down to the relevant categories most likely impacting your [industry](https://docs.predicthq.com/getting-started/guides/industry-specific-event-filters)
* **start and end:** filter on start and end dates being in a specified time period. You might be looking at events in the next week or month or longer.
* **rank:** is commonly used to filter out smaller events. Filter where rank is equal to or greater than a specific field to filter out smaller events.
* **geo:** This field contains geojson data ([see here](https://docs.predicthq.com/getting-started/guides/geolocation-guides/overview#geojson) for more details) on the location event. For attended events, this field typically holds the latitude and longitude of the point at which the event is occurring. It can also hold [polygon](https://docs.predicthq.com/getting-started/guides/geolocation-guides/working-with-polygons) information for events that cover a wide area like marathons or severe weather events. For marathons, the polygon shows the route of the marathon. Query on this field to find all events in an area like a radius.

See the [Filtering Guide](https://docs.predicthq.com/getting-started/guides/tutorials/filtering-and-finding-relevant-events) for more examples. The SQL example below shows how to query these fields in the database.

Below is a sample BigQuery SQL query that aligns with the parameters specified for our example. This query filters events based on the categories, date range, event rank, and geographical proximity to Tom’s location.

This type of query is used to find all events around a location with a specified radius for a business location. For example a restaurant, hotel, store, parking garage, or any other business location. Once you have the data loaded into GCP you will want to find how events are impacting your locations. Use the type of query below for each location to get all the events around that location.

{% code lineNumbers="true" fullWidth="true" %}
```sql
SELECT *
FROM `predicthq_dataset_test.phq_api_json_format`
WHERE category IN ('concerts','conferences','festivals','performing-arts')
  AND `start` >= '2024-06-01' --Change this to the date range you want to display events for - e.g. the next 30 days
  AND `end` <= '2024-06-30'
  AND rank >= 30
  AND ST_Distance(
      ST_GeogPoint(
          CAST(JSON_EXTRACT_SCALAR(geo, '$.geometry.coordinates[0]') AS FLOAT64),
          CAST(JSON_EXTRACT_SCALAR(geo, '$.geometry.coordinates[1]') AS FLOAT64)),
          ST_GeogPoint(-122.33, 47.60)  --Tom's store location in our example
      ) <= 2400 -- Approximately 1.48 miles in meters
	--When implementing this use the Suggested Radius API to find the radius for your location
  AND state IN ('active', 'predicted');
```
{% endcode %}

This query will retrieve records that meet all the specified criteria, allowing Tom to identify events that could potentially influence the operations and traffic at this pizzeria in Seattle. Modify the above query to fit the specific fields and data types of your table if they differ from this example, and fill your latitude and longitude for your locations with a radius suggested by our [Suggested Radius API](https://docs.predicthq.com/api/suggested-radius/get-suggested-radius).

Visually this type of query allows you to pull all the events in a radius as shown in the image below:

<figure><img src="../../../.gitbook/assets/Radius Map.png" alt=""><figcaption><p>Radius Map example from our website</p></figcaption></figure>

A common example is customers often look at events occurring in the next 1 to 3 months and may display this information in their application, in a BI tool, or in other types of products and tools. A common approach to doing this can be to have a table with a list of your business locations with latitude and longitude for each. For each, call the [Suggested Radius API](https://docs.predicthq.com/api/suggested-radius/get-suggested-radius) to store the radius and then look up your store locations in the table. For example you may have a table of locations like that below:



<table data-full-width="true"><thead><tr><th>location</th><th>lattitude</th><th>longitude</th><th>radius</th><th>radius_unit</th><th>date_start</th><th>date_end</th></tr></thead><tbody><tr><td>store1-chicago</td><td>41.8131</td><td>-87.6586</td><td>4.11</td><td>mi</td><td>2023-07-01</td><td>2023-12-31</td></tr><tr><td>Hyde Park</td><td>51.50736</td><td>-0.16411</td><td>2.06</td><td>mi</td><td>2024-01-01</td><td>2024-03-31</td></tr><tr><td>store10-new-yor</td><td>40.73061</td><td>-73.93524</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></tbody></table>

See our [Snowflake Data Science Guide](https://docs.predicthq.com/integrations/third-party-integrations/snowflake/snowflake-data-science-guide) for an example of doing this in Snowflake.

Using BigQuery for these queries ensures that you leverage powerful, scalable SQL analytics over large datasets, enabling responsive decision-making based on the latest event data available in your system.\


## Utilizing PredictHQ Data in Your Data Warehouse

Having integrated PredictHQ's rich events data into your data warehouse, the opportunities to leverage this data are extensive. By now, you've successfully set up your data structure within Google Cloud Platform's BigQuery and have a solid understanding of the JSONL file Upload or the API Connection methods. Here’s how you can maximize the value of PredictHQ data within your organization:

#### 1. Cross-referencing with Internal Datasets

Enhance the granularity and relevance of your internal analytics by cross-referencing PredictHQ events data with your own datasets. For instance, you can correlate sales data with event occurrences to analyze the impact of local events on sales performance. This cross-analysis can be crucial for demand forecasting and strategic planning.

Customers sometimes use fields like [Placekey ](https://docs.predicthq.com/getting-started/guides/geolocation-guides/join-events-using-placekey)to join events data and other location data.

#### 2. Demand Analysis and Forecasting

PredictHQ data can significantly enhance your demand forecasting models, especially for businesses that are impacted by local events, such as retail, hospitality, and transportation. By understanding when significant events are happening, you can better predict and prepare for attendance surges or declines.&#x20;

You can use Event data from your data warehouse in your demand forecast to improve forecast accuracy. See our [Snowflake Data Science Guide](https://docs.predicthq.com/integrations/third-party-integrations/snowflake/snowflake-data-science-guide) for an example of how you can implement ML features for demand forecasting in a data warehouse. Although that example shows how to do this in Snowflake, a similar approach applies to other data warehouses. See also [Improving Demand Forecasting Models with Event Features](https://docs.predicthq.com/getting-started/guides/tutorials/improving-demand-forecasting-models-with-event-features).

#### 3. Building Tailored Reports

Use the data within BigQuery to create detailed reports and dashboards that monitor the effects of events on your business operations. These reports can provide actionable insights to business users across your organization, from marketing teams planning campaigns around major events to supply chain management preparing for increased activity.

See [Use Events Data in Power BI](https://docs.predicthq.com/getting-started/guides/tutorials/use-events-data-in-power-bi) for an example of building reports in Power BI. You can connect Power BI or other BI tools to your database to build dashboards and reports.

#### 4. Enhancing Customer Experience

Inform your customers about local events that might impact their experience with your service or product. For example, a transportation company could provide passengers with real-time updates about events that might affect travel times or service availability.

#### 5. Event-Driven Marketing

Plan and execute marketing campaigns that align with upcoming events to capitalize on increased foot traffic or digital engagement. This targeted approach can improve marketing ROI by reaching audiences when they are most receptive.



By tapping into the detailed and predictive insights provided by PredictHQ, your business can not only anticipate the impact of external events but also strategize proactively to harness potential opportunities or mitigate risks. Whether through enhancing predictive analytics, refining customer engagement strategies, or driving operational efficiencies, PredictHQ's events data serves as a powerful tool in your data-driven decision-making arsenal.
