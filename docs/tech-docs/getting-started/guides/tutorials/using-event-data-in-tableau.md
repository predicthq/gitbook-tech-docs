---
description: Learn how to connect PredictHQ data to Tableau and build an example dashboard.
---

# Using Event Data in Tableau

PredictHQ provides a rich repository of event data that can impact key business operations including demand forecasting and strategic planning. This tutorial demonstrates how to seamlessly integrate PredictHQ with Tableau to create dynamic visualizations, offering insights into how events may influence business trends. Follow along as we explore a quick and easy way to load a static event export as well as advice on connecting directly from data warehouses where PredictHQ data is stored.

## Use Cases

Demand Forecasting, Dynamic Pricing, Workforce Optimization, Demand Analytics, Inventory Management, Event Visibility

## Relevant Industries

Accommodation, Consumer Packaged Goods, Grocery and Supermarkets, Leisure, Travel and Tourism, Marketing and Advertising, Parking, Restaurants, Retail, Transportation and Delivery and Others

## Getting Started

This tutorial requires access to both Tableau and PredictHQ.&#x20;

1. Tableau: The instructions provided are based on [Tableau Public](https://public.tableau.com/app/discover), but other Tableau products, such as Tableau Desktop, should operate similarly.
2. PredictHQ: To download a static export of PredictHQ data, a [PredictHQ account](https://signup.predicthq.com/) is required.

## Connection with JSON File

Tableau supports [various methods](https://help.tableau.com/current/pro/desktop/en-us/exampleconnections_overview.htm) for connecting to data sources, including local files and data warehouses. This tutorial focuses on connecting to PredictHQ data via a [JSON file](https://help.tableau.com/current/pro/desktop/en-us/examples_json.htm).&#x20;

Connecting via a JSON file in Tableau involves downloading a static snapshot of event data through [bulk exporting from PredictHQ's WebApp](../export-data-via-control-center.md). It is particularly useful for scenarios where real-time data updates are not essential. Ideal for quick testing or one-off analyses, this approach provides an efficient way to get started with event data in Tableau. This is a good way to try PredictHQ's data for the first time and explore how it can be useful in your business.

A JSON file export contains a structured list of events, much like a CSV export, but with better handling of nested data. While Tableau also [supports CSV file connections](https://help.tableau.com/current/pro/desktop/en-us/examples_text.htm), accessing nested data, such as [Impact Patterns](../../predicthq-data/impact-patterns.md), is more challenging. In contrast, Tableau's native support for JSON files simplifies the integration and manipulation of nested information, making it the preferred method for connecting PredictHQ data.

### Export File

**Search Events**

1. Access our WebApp: Log in and navigate to [Search Events](https://control.predicthq.com/search/events).&#x20;
2. Configure Filters: Set relevant filters, such as those for category, date, and location. Once set, click 'Search'.

> **Example Search**
>
> To view all [attendance-based events](../../predicthq-data/event-categories/attendance-based-events.md) in San Francisco scheduled or predicted to take place in May 2024, use the following URL with pre-configured filters:
>
> [https://control.predicthq.com/search/events?category=conferences,expos,concerts,festivals,performing-arts,community,sports\&place.scope=5391959\&active.gte=2024-05-01\&active.lte=2024-05-31\&state=active,predicted\&sort=phq\_attendance,-start](https://control.predicthq.com/search/events?category=conferences,expos,concerts,festivals,performing-arts,community,sports\&place.scope=5391959\&active.gte=2024-05-01\&active.lte=2024-05-31\&state=active,predicted\&sort=phq_attendance,-start\&t=1716862100079)

{% hint style="info" %}
For guidance on finding the most relevant events for your business, see [filtering-and-finding-relevant-events.md](filtering-and-finding-relevant-events.md "mention"). For searches around specific locations or stores, exporting a JSON file from our WebApp [Saved Locations](https://control.predicthq.com/location-insights) is recommended.
{% endhint %}

**Export as JSON**

3. Export Events: Once the events of interest are displayed on our WebApp's Search, click 'Export' on the right-hand side followed by 'Export Events Data'. In the dialog box that appears, select the 'JSONL' tab and then click 'Export'.&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcvQzusKN7PGRgRBq2QZ7AMtb-3r3k3B4Y4HRW3TDPYA1AZNt1fqiMprRB-prb9CiL3rTOe-7oH0z7aNEN_1rjPXY1GesmiVng0kjAUP3bC_S1Vg8OSBCsSv7qfvROnQnkHeJ_5RDWXCbm-TOSSK7DPieQ?key=Vi0_07VB32pOkrxgXfeY_A" alt="" width="375"><figcaption><p>Export Events dialog box</p></figcaption></figure>

4. Download Link: Once the export is ready, the dialog box will update with a download link. The link will also be sent via email.
5. Save Export: Download the file and save it to a directory for later use.

{% hint style="info" %}
For more information on using our WebApp Search and exporting files, see [export-data-via-control-center.md](../export-data-via-control-center.md "mention").
{% endhint %}

### Connect in Tableau

**Connect to File**

1. Start Tableau: Open Tableau and under 'Connect' select 'JSON file'.
2. Locate File: Navigate to the directory where the export was previously saved. It may be necessary to change the file extension filter from 'JSON Files (\*.json)' to 'All Files (\*.\*)' in order to see and select the JSON lines file. Click 'Open' to load the file.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeYM6sCSxWnNn4WT6rinrcHl_oqGIeunmUmlT2IgZwwugm0XhASIhcRj1ucG_aoomHbEi3SH0TTjbLeM689xM_C8qRcE4He-BLQiq_VKdKfHXWMswwJnE3vJUaCs5kFV1FBXRPgGPpj1r5daiqa5oB03qxx?key=Vi0_07VB32pOkrxgXfeY_A" alt="" width="375"><figcaption><p>File extension options</p></figcaption></figure>

{% hint style="info" %}
For more information on connecting a local JSON file to Tableau and setting up the data source, see this [Tableau article](https://help.tableau.com/current/pro/desktop/en-us/examples_json.htm).
{% endhint %}

**Flatten Nested JSON**

3.  Select Schema Levels: When the file is loaded, the 'Select Schema Levels' dialog box should automatically appear. The schema levels can also be modified by following these [instructions](https://help.tableau.com/current/pro/desktop/en-us/examples_json.htm#change-schema-levels). To ensure the data is structured correctly for this tutorial, select the following schema levels or follow these [instructions](https://help.tableau.com/current/pro/desktop/en-us/examples_json.htm#change-schema-levels) to change the schema levels:&#x20;

    1. Root Level: Typically named after the JSON file e.g. `Events-Export-…`
    2. Impact Patterns: Includes data related to impact patterns.
    3. Impacts: Details specific impact values for each day.

    <figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdLRxDH6Zq-2jnUoQwltqqWhrpBN2UeamCuAJkjk02RHxx-V_It0GgKe-cl-PKax5O5zPnD6i1QSlyggRFzrsZhBjArKOCHbWJ43Qabi_UUbyy2JJ4YoP2JlMlJVRbEa57SQBiWXlW2dTubdGh2jY1BtE5P?key=Vi0_07VB32pOkrxgXfeY_A" alt="" width="375"><figcaption><p>Schema levels to select</p></figcaption></figure>

{% hint style="info" %}
For more information on schema levels, see this [Tableau article](https://help.tableau.com/current/pro/desktop/en-us/examples_json.htm#select-schema-level).
{% endhint %}

**Update Data Types**

4. Check Data Types: Tableau automatically interprets a field's data type but this is not always correct. Review and adjust the data type where necessary by following [these instructions](https://help.tableau.com/current/pro/desktop/en-us/datafields_typesandroles_datatypes.htm#change-the-data-type-for-a-field-in-the-data-source-page), ensuring the following fields are set correctly for this tutorial:

| Field         | Correct Data Type              |
| ------------- | ------------------------------ |
| `End Local`   | Date & Time                    |
| `Date Local`  | Date                           |
| `Start Local` | Date & Time                    |
| `State`       | String (Geographic Role: None) |

{% hint style="info" %}
For more information on data types, see this [Tableau article](https://help.tableau.com/current/pro/desktop/en-us/datafields_typesandroles_datatypes.htm).
{% endhint %}

## Dashboard with Event Data

This section will guide you through creating a simple dashboard in Tableau, featuring a time series chart of daily event impact derived from [Impact Patterns](../../predicthq-data/impact-patterns.md) and a table listing relevant events. PredictHQ data is connected via a JSON file.&#x20;

### Worksheets

**Chart**

1. New Worksheet: [Open a new worksheet](https://help.tableau.com/current/pro/desktop/en-us/environ_workbooksandsheets.htm#create-new-worksheets-dashboards-or-stories) and name it 'Time Series'.
2. Set Filters: Use filters to refine the data for events of interest only. [Drag the following fields](https://help.tableau.com/current/pro/desktop/en-us/filtering.htm#drag-dimensions-measures-and-date-fields-to-the-filters-shelf) to the Filters shelf:

<table data-full-width="false"><thead><tr><th width="174">Folder</th><th width="153">Field</th><th>Dialog Box</th></tr></thead><tbody><tr><td>Event-Export-...</td><td><code>State</code></td><td><p>Filter [State]</p><ol><li>Under 'General' and 'Select from list', check <code>active</code> and <code>predicted</code>.</li><li>Click 'OK'.</li></ol><p>Notes</p><ul><li>This filter is necessary unless these states have already been filtered via our WebApp Search.</li></ul></td></tr><tr><td>Event-Export-...</td><td><code>Category</code></td><td><p>Filter [Category]</p><ol><li>Under 'General' and 'Select from list', check <code>community</code>, <code>concerts</code>, <code>conferences</code>, <code>expos</code>, <code>festivals</code>, <code>performing-arts</code>, <code>sports</code>.</li><li>Click 'OK'.</li></ol><p>Notes</p><ul><li>This filter is necessary unless these categories have already been filtered via our WebApp Search.</li></ul></td></tr><tr><td>Impact Patterns</td><td><code>Vertical</code></td><td><p>Filter [Vertical]</p><ol><li>Under 'General' and 'Select from list', check an industry e.g. <code>accommodation</code>.</li><li>Click 'OK'.</li></ol><p>Note</p><ul><li><code>Vertical</code> is the industry vertical associated with the impact pattern. </li><li>This tutorial focuses on event day impact, which is the same for all industries.  </li><li>Choose any available industry if yours is not available.</li></ul></td></tr><tr><td>Impacts</td><td><code>Date Local</code></td><td><p>Filter Field [Date Local]</p><ol><li>Select 'Range of Dates' then click 'Next'.</li></ol><p>Filter [Date Local]</p><ol><li>Set the minimum and maximum dates to '01/05/2024' and '31/05/2024', respectively.</li><li>Click 'OK'.</li></ol><p>Notes</p><ul><li><code>Date Local</code> is the date in the local time zone. </li></ul></td></tr><tr><td>Impacts</td><td><code>Position</code></td><td><p>Filter [Position]</p><ol><li>Under 'General' and 'Select from list', check event_day.</li><li>Click 'OK'.</li></ol><p>Notes</p><ul><li><code>Position</code> categorizes <code>Date</code> Local in relation to when the event takes place, such as before, during, or after the event. </li><li>While this tutorial focuses on the impact during event days, exploring impacts on other days is also encouraged.</li></ul></td></tr></tbody></table>

{% hint style="info" %}
For more information on PredictHQ event fields, see [Broken link](broken-reference "mention").
{% endhint %}

2. Apply Filters Globally: Apply the above filters to 'all worksheets using this data source' by right-clicking each field in the Filters shelf and following these [instructions](https://help.tableau.com/current/pro/desktop/en-us/filtering_global.htm#apply-filters-to-all-worksheets-that-use-the-current-primary-data-source). This prevents the need to repeat configurations across multiple worksheets, ensuring consistency in data.
3. Create Chart:&#x20;
   1. Drag `Value` from 'Source Measures' to the Row shelf.&#x20;
   2. Drag `Date Local` from 'Impacts' to the Column shelf. Then right-click on the `Date Local` pill and select the 'Exact Date' format.&#x20;
   3. Update the y-axis title to 'Daily Event Day Impact' by following these [instructions](https://help.tableau.com/current/pro/desktop/en-us/formatting_editaxes.htm#change-the-appearance-of-an-axis).
4. Chart Preview:

<figure><img src="../../../.gitbook/assets/image (97).png" alt="" width="563"><figcaption><p>Time Series worksheet</p></figcaption></figure>

**Table**

1. New Worksheet: [Open a new worksheet](https://help.tableau.com/current/pro/desktop/en-us/environ_workbooksandsheets.htm#create-new-worksheets-dashboards-or-stories) and call it 'Event Info'.
2. Create Table:&#x20;
   1. Add all relevant fields to the Row shelf and ensure they are all formatted as 'Discrete' to produce the correct table. This formatting change should turn all the pills blue. For this tutorial, the following fields are considered:

<table data-full-width="false"><thead><tr><th width="177">Folder</th><th width="182">Field</th><th>Notes</th></tr></thead><tbody><tr><td>Impacts</td><td><code>Date Local</code></td><td><ul><li>Right-click on the pill and select the 'Exact Date' and 'Discrete' formats.</li></ul></td></tr><tr><td>Event-Export-...</td><td><code>Id</code></td><td><ul><li>This is the ID of the event. </li></ul></td></tr><tr><td>Event-Export-...</td><td><code>Category</code></td><td><ul><li>This is the <a href="../../predicthq-data/event-categories/">event category</a>.</li></ul></td></tr><tr><td>Event-Export-...</td><td><code>Start Local</code></td><td><ul><li>This is the start date of the event in the local time zone.</li><li>Right-click on each of the pills and select the 'Exact Date' and 'Discrete' formats.</li></ul></td></tr><tr><td>Event-Export-...</td><td><code>End Local</code></td><td><p></p><ul><li>This is the end date of the event iin the local time zone.</li><li>Right-click on each of the pills and select the 'Exact Date' and 'Discrete' formats.</li></ul></td></tr><tr><td>Event-Export-...</td><td><code>Timezone</code></td><td><ul><li>The local time zone.</li></ul></td></tr><tr><td>Source Measures</td><td><code>Phq Attendance</code></td><td><ul><li>This is the <a href="../../predicthq-data/predicted-attendance.md">predicted attendance</a> for an event.</li><li>Right-click on the pill and select the 'Discrete' format.</li></ul></td></tr><tr><td>Source Measures</td><td><code>Value</code></td><td><p></p><ul><li>This is the <a href="../../predicthq-data/impact-patterns.md">daily impact for an event</a>. For this tutorial, only impact on event days is considered.</li><li>Sort by descending `Value` by following these <a href="https://help.tableau.com/current/reader/desktop/en-us/reader_sort.htm">instructions</a>.</li></ul></td></tr></tbody></table>

{% hint style="info" %}
For more information on PredictHQ event fields, see [Broken link](broken-reference "mention").
{% endhint %}

3. Table Preview:

<figure><img src="../../../.gitbook/assets/image (98).png" alt=""><figcaption><p>Event Info worksheet</p></figcaption></figure>

### Dashboard

1. New Dashboard: [Open a new dashboard](https://help.tableau.com/current/pro/desktop/en-us/environ_workbooksandsheets.htm#create-new-worksheets-dashboards-or-stories).
   1. Set the size of the dashboard to 'Automatic' by following these [instructions](https://help.tableau.com/current/pro/desktop/en-us/dashboards_organize_floatingandtiled.htm#set-overall-dashboard-size) to ensure the dashboard adjusts to fit the screen it's being viewed on.
2. Add Worksheets: From the Sheets list, drag the Time Series sheet anywhere in the dashboard and then 'Event Info' to the right. Resize the [layout containers](https://help.tableau.com/current/pro/desktop/en-us/dashboards_organize_floatingandtiled.htm#layout-container-types) as needed.
3. Set Filters: Use the Time Series worksheet as an interactive filter by following these [instructions](https://help.tableau.com/current/pro/desktop/en-us/dashboards_create.htm#add-interactivity). This allows you to click on specific dates in the chart to dynamically filter the events displayed in the table.&#x20;
4. Dashboard Preview:

<figure><img src="../../../.gitbook/assets/image (99).png" alt=""><figcaption><p>Dashboard</p></figcaption></figure>

{% hint style="info" %}
For more information on creating dashboards, see this [Tableau article](https://help.tableau.com/current/pro/desktop/en-us/dashboards_create.htm).
{% endhint %}

### Next steps

There are several ways to expand the functionality and relevance of this dashboard to your specific business needs:

1. Incorporate Business Metrics: Integrate key metrics such as sales figures or units sold to gain a comprehensive view of how events influence business performance. Linking event impacts with sales data can help uncover high-level trends and support data-driven decision-making.
2. Explore Impact Patterns: While this tutorial focuses on the immediate impacts of events, exploring additional impact patterns could yield deeper insights. For example, examining patterns leading up to and after events might reveal extended influences on consumer behavior or operational demands.&#x20;
3. Customize Visualizations: Enhance the dashboard with more complex visualizations like heat maps or geographic visualizations. These can offer spatial insights into where events have the most impact, assisting in regional marketing strategies and resource allocation.
4. Up-to-date Event Data: Ensure the dashboard reflects the most current data by considering connections like Snowflake or Amazon Data Exchange. These methods (see [examples](using-event-data-in-tableau.md#other-connection-methods) below) offer real-time updates which are essential for accommodating the dynamic nature of event data.

## Other Connection Methods

While this tutorial primarily focuses on connecting via a JSON file, other connection methods are available for those needing real-time updates or integration with other data services

<details>

<summary>Snowflake</summary>

This connection method involves accessing PredictHQ data through Snowflake’s Secure Data Share and connecting it to Tableau.

**Snowflake Data Share**

1. Setup: Coordinate with your Snowflake administrator to set up a Data Share with PredictHQ.&#x20;
2. Database: Create a database from the Data Share and ensure that the necessary permissions are granted to users.

For more information on receiving PredictHQ data via Snowflake, see this [guide](../../../integrations/third-party-integrations/snowflake/).

**Connect to Snowflake in Tableau**

3. Connection Details: Before connecting, gather all necessary information including:
   1. [Login credentials](https://help.tableau.com/current/pro/desktop/en-us/examples_snowflake.htm#before-you-begin) for Snowflake authentication
   2. [Server, Warehouse, Database and Schema information](https://help.tableau.com/current/pro/desktop/en-us/examples_snowflake.htm#set-up-the-data-source) to set up the data source. &#x20;
4. Start Tableau: Open Tableau and connect to Snowflake by following these [instructions](https://help.tableau.com/current/pro/desktop/en-us/examples_snowflake.htm#make-the-connection-and-set-up-the-data-source).

For more information on connecting to Snowflake in Tableau and setting up the data source, see this [Tableau article](https://help.tableau.com/current/pro/desktop/en-us/examples_snowflake.htm).

**Filter for Relevant Events in Tableau**

5. Configure SQL Query: Use Tableau’s custom SQL query to manage how data is brought in for subsequent analyses. For PredictHQ data, this typically involves flattening nested JSON, converting data types, and applying filters, such as category, date, and location, to filter for relevant events. See this [Power BI tutorial](using-event-data-in-power-bi.md) for an example of how this query might be structured.

For more information on connecting to a custom SQL query, see this [Tableau article](https://help.tableau.com/current/pro/desktop/en-us/customsql.htm).

</details>

<details>

<summary>Amazon S3</summary>

This connection method involves accessing PredictHQ data through AWS Data Exchange and connecting it to Tableau.

**AWS Data Exchange**

1. Setup: Subscribe to PredictHQ data on AWS Data Exchange
2. Amazon S3: Copy the data to your specified S3 bucket. Ensure that your AWS IAM user or role has read permissions for this bucket.&#x20;

For more information on receiving PredictHQ data via AWS Data Exchange, see this [guide](../../../integrations/third-party-integrations/aws-data-exchange/).

**Connect to Amazon S3 in Tableau**

3. Connection Details: Before connecting, gather all [necessary information](https://help.tableau.com/current/pro/desktop/en-us/examples_amazons3.htm#before-you-begin) including:
   1. AWS IAM access key for the S3 bucket.
   2. The name and AWS region of the S3 bucket.
4. Start Tableau: Open Tableau and connect to the S3 bucket by following these [instructions](https://help.tableau.com/current/pro/desktop/en-us/examples_amazons3.htm#make-the-connection-and-set-up-the-data-source).

For more information on connecting to Amazon S3 in Tableau and setting up the data source, see this [Tableau article](https://help.tableau.com/current/pro/desktop/en-us/examples_amazons3.htm).

**Filter for Relevant Events in Tableau**

5. Configure SQL Query: Use Tableau’s custom SQL query to manage how data is brought in for subsequent analyses. For PredictHQ data, this typically involves flattening nested JSON, converting data types, and applying filters, such as category, date, and location, to filter for relevant events. See this [Power BI tutorial](using-event-data-in-power-bi.md) for an example of how this query might be structured.

For more information on connecting to a custom SQL query, see this [Tableau article](https://help.tableau.com/current/pro/desktop/en-us/customsql.htm).

</details>

<details>

<summary>More Common Connectors</summary>

Some other connectors commonly used with PredictHQ data include the following:

* [Google BigQuery](https://help.tableau.com/current/pro/desktop/en-us/examples_googlebigquery.htm)
* [Azure SQL Database](https://help.tableau.com/current/pro/desktop/en-us/examples_azure_sql_database.htm)
* [Amazon Redshift](https://help.tableau.com/current/pro/desktop/en-us/examples_amazonredshift.htm)

For more information on loading PredictHQ data into data warehouses, see this [guide](loading-event-data-into-a-data-warehouse.md) which provides an example using Google BigQuery.

See this [article](https://help.tableau.com/current/pro/desktop/en-us/exampleconnections_overview.htm) for all connectors supported by Tableau. Once PredictHQ data is connected to a data warehouse, techniques similar to those described in this guide can be applied for querying data from these sources.

</details>

## Conclusion

This tutorial has demonstrated how to connect PredictHQ data to Tableau and build a functional dashboard. This is just one way to harness the power of event data. Continue to refine and expand your dashboard to align with your business needs, maximizing the insights available and thereby enhancing strategic decision-making processes.

## **Resources for Download**

{% file src="../../../.gitbook/assets/Events-Export-San-Francisco-from-20240501-to-20240531 (1).jsonl" %}
JSON file
{% endfile %}

{% file src="../../../.gitbook/assets/PredictHQ Example Dashboard (1).twbx" %}
Tableau workbook
{% endfile %}
