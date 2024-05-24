---
description: >-
  Learn how to connect PredictHQ data to Power BI using multiple methods, and
  build an example report.
---

# Use Events Data in Power BI

In today's data-driven landscape, leveraging powerful analytical tools is essential for making informed decisions and uncovering hidden insights. This step-by-step guide focuses on Power BI as an industry standard robust, user-friendly platform. Power BI is used here as an example of a reporting suite that enables users to integrate data from various sources, create interactive reports, and share insights across an organization, to leverage PredictHQ data for powerful insights.

## Use Cases

[Demand Forecasting](https://docs.predicthq.com/getting-started/tutorials-by-use-case/automated-demand-forecasting-with-ml-models), [Dynamic Pricing](https://docs.predicthq.com/getting-started/tutorials-by-use-case/dynamic-pricing), [Workforce Optimization](https://docs.predicthq.com/getting-started/tutorials-by-use-case/workforce-optimization), [Demand Analytics](https://docs.predicthq.com/getting-started/tutorials-by-use-case/visualization-and-insights), [Inventory Management](https://docs.predicthq.com/getting-started/tutorials-by-use-case/inventory-management), [Event Visibility](https://docs.predicthq.com/getting-started/tutorials-by-use-case/visualization-and-insights)

## Relevant Industries

[Accommodation](https://docs.predicthq.com/getting-started/tutorials-by-use-case/visualization-and-insights#accommodation-demand-analytics-calendar-and-map-tutorials), Consumer Packaged Goods, [Grocery and Supermarkets](https://docs.predicthq.com/getting-started/tutorials-by-use-case/visualization-and-insights#retail-demand-analytics-calendar-and-map-tutorials), Leisure, Travel and Tourism, Marketing and Advertising, [Parking](https://docs.predicthq.com/getting-started/tutorials-by-use-case/visualization-and-insights#transportation-and-parking-demand-analytics-calendar-and-map-tutorials), Restaurants, [Retail](https://docs.predicthq.com/getting-started/tutorials-by-use-case/visualization-and-insights#retail-demand-analytics-calendar-and-map-tutorials), [Transportation and Delivery](https://docs.predicthq.com/getting-started/tutorials-by-use-case/visualization-and-insights#transportation-and-parking-demand-analytics-calendar-and-map-tutorials) and Others

## Overview

This tutorial covers how to connect PredictHQ data to Power BI via two sources, CSV upload and direct API connection using one of our APIs - the Events API.

The data used in this guide is based on a popular location, in our case San Francisco City as a whole. Please change the location from San Francisco to the location you want to look at.

Below are the main steps involved in this guide:

1. Building Report Parameters around a Location
   * Example Parameters for this Guide
2. Select an Input method
   * CSV upload
   * Snowflake Connection
   * API connection
3. Guide to Building the Report
   * Example report download

**Requirements:**

1. Access to PredictHQ data via 3 methods with 3 different requirements:
   * CSV: PredictHQ account - [Sign up here](https://predicthq.com/signup) if you don’t already have an account.
   * Snowflake: PredictHQ [Snowflake Data Share](https://docs.predicthq.com/integrations/third-party-integrations/snowflake)
   * API: [API Access Token](https://www.predicthq.com/support/how-to-create-an-api-token)
2. [Microsoft Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi) reporting software

## Building Report Parameters around a Location

For the purposes of this tutorial, parameters will be fixed for a standard example. Parameters are defined below, focusing on San Francisco city for attended events in a 3 month period.



{% hint style="info" %}
All of our parameters are able to be modified based on user needs, see our [filtering guide](filtering-and-finding-relevant-events.md) for details on what these parameters mean and how they can be modified to suit different use cases.
{% endhint %}

### Example Parameters for this Guide:

1. **Date**: user-defined, this tutorial uses a 3-month period from January 1st to March 31st 2024
2. **Categories**: community, conferences, concerts, expos, festivals, performing-arts, sports - these are our [attended categories](https://docs.predicthq.com/getting-started/predicthq-data/event-categories)&#x20;
3. **Event State**: Active and Predicted
4. **PHQ Attendance**: attended events only - filtered to events with an attendance of at least 1
5. **Location**: San Francisco city (place ID [5391959](https://www.geonames.org/5391959/san-francisco.html))

Location could be substituted for a specific latitude and longitude relating to an individual store, or could be scoped even wider depending on need. We suggest utilizing our [Suggested Radius API](https://docs.predicthq.com/api/suggested-radius/get-suggested-radius) to hone in on a specific shop location and pull only events within a more accurate radius based on those results. For now, we will look at the citywide events in San Francisco as our example.

The report provided in this example shows a graph of the total number of people attending events around the location per day, as well as a list of the events happening at the location sorted by the highest attendance events first.&#x20;

We find many customers want to know what is happening around a business location such as around a hotel, restaurant, store, or other location. The graph of total attendance per day shows you peaks and dips in physically attended events. This allows you to see upcoming busy days or potential demand surges as well as quieter days. The list of events allows you to see events happening on a given day in more detail.

Our customers use this in a variety of ways, for example, an accommodation customer may use a report like this to set their hotel room pricing per day and may increase the price on days with a lot of events happening. A restaurant customer looking at staffing might roster more people when they see a lot of events happening near their location and perhaps reduce staff levels when fewer events are happening. And so on. See our [use case guide](https://docs.predicthq.com/getting-started/tutorials-by-use-case) for more examples.

The end result of the exercise will be a report like this:

<figure><img src="../../../.gitbook/assets/Final Result.png" alt=""><figcaption><p>Final Report Result</p></figcaption></figure>

## Select an Input Method

There are several ways to connect PHQ data to Power BI or other reporting software. Below are three of the main methods users can utilize to connect and start creating reports.

[**CSV Upload**](connect-and-build-events-data-in-power-bi.md#csv-upload-method): The quick and easy way to connect data straight from our PredictHQ Control Center into reporting software. If a static view of data is all you need, this method gets it done fast. This method _does not_ refresh or update the data when it changes. Events are dynamic and get canceled, postponed, move location, and so on. Using a CSV is a good way to do initial modeling but we’d suggest calling the API or connecting to a data warehouse moving forward.

[**Snowflake Connection**](connect-and-build-events-data-in-power-bi.md#snowflake-connection-method): Choosing Snowflake as the data source for Power BI is highly recommended due to its robust data warehousing capabilities and seamless integration. Snowflake provides dynamic scalability and real-time data access, enhancing the accuracy and efficiency of reports. Snowflake offers straightforward connectivity and powerful query performance.

[**API Connection**](connect-and-build-events-data-in-power-bi.md#api-connection-method): Another preferred method for connecting our dynamic events data to Business Intelligence software is to use our robust APIs. This way the report is connected to an ever-updating data source and is always up to date.

### CSV Upload Method

We will use PredictHQ [Control Center Search](https://www.predicthq.com/support/control-center-search) to get our CSV. Filter the events based on the parameters laid out in the [Example Parameters for this Guide](connect-and-build-events-data-in-power-bi.md#example-parameters-for-this-guide). For more information on using Control Center Search use [this guide](https://www.predicthq.com/support/control-center-search). Fill in the parameters and hit search.

<figure><img src="../../../.gitbook/assets/Control Center Filter.png" alt=""><figcaption><p>Control Center Example Filters</p></figcaption></figure>

Once the search has completed hit the Export button on the right to get a CSV. For more details on exporting see the [CSV Export Guide](https://www.predicthq.com/support/getting-started-with-data-exporter). Once the export has been downloaded, it’s ready for use in Power BI. The filename by default should be “Real-World-Events-202xxxxx.csv” where the x are dates of the export - feel free to rename this to anything else.

In Power BI, create a new report and press Get Data -> Text/CSV

<figure><img src="../../../.gitbook/assets/New CSV Connection.png" alt=""><figcaption><p>Get Data -> Text/CSV new connection</p></figcaption></figure>

Upload the CSV export and hit the transform data option.

<figure><img src="../../../.gitbook/assets/CSV Transform Data.png" alt=""><figcaption><p>CSV 'Transform Data'</p></figcaption></figure>

Right-click the Query under Queries and go to the Advanced Editor option. The Query will be named the same as the uploaded CSV name.

<figure><img src="../../../.gitbook/assets/CSV go to Advanced Editor.png" alt=""><figcaption><p>right click Query -> Advanced Editor</p></figcaption></figure>

This opens up a Power Query window which allows code to transform the data for us. Below is a Power Query code that will transform the columns automatically for use in the report.

This code expands out the 'impact\_patterns' column (see [Impact Patterns ](https://docs.predicthq.com/getting-started/predicthq-data/impact-patterns)in our technical documentation for more information) and filters it to accommodation and actual attendance distribution. It renames some essential columns. It also transforms some column formats for easier use in reporting. It is an involved process with multiple steps - the Power Query below is the final output of this multi-stage transformation.

Paste the Power Query below after the first existing 4 lines, after the "Changed Type" step, replacing everything from the existing “in” down.

{% code lineNumbers="true" fullWidth="true" %}
```powerquery
    ,#"Renamed Columns" = Table.RenameColumns(#"Changed Type",{{"impact_patterns", "impact_patterns_raw"}}),
    #"Added Custom" = Table.AddColumn(#"Renamed Columns", "impact_patterns", each Json.Document([impact_patterns_raw])),
    #"Expanded impact_patterns" = Table.ExpandListColumn(#"Added Custom", "impact_patterns"),
    #"Expanded impact_patterns1" = Table.ExpandRecordColumn(#"Expanded impact_patterns", "impact_patterns", {"vertical", "impact_type", "impacts"}, {"impact_patterns.vertical", "impact_patterns.impact_type", "impact_patterns.impacts"}),
    #"Expanded impact_patterns.impacts" = Table.ExpandListColumn(#"Expanded impact_patterns1", "impact_patterns.impacts"),
    #"Expanded impact_patterns.impacts1" = Table.ExpandRecordColumn(#"Expanded impact_patterns.impacts", "impact_patterns.impacts", {"date_local", "value", "position"}, {"impact_patterns.impacts.date_local", "impact_patterns.impacts.value", "impact_patterns.impacts.position"}),
    #"Filtered Rows" = Table.SelectRows(#"Expanded impact_patterns.impacts1", each ([impact_patterns.vertical] = "accommodation" and [impact_patterns.impacts.position] = "event_day")),
    #"Changed Number Type" = Table.TransformColumnTypes(#"Filtered Rows",{{"impact_patterns.impacts.value", Int64.Type}}),
    #"Changed Date Type" = Table.TransformColumnTypes(#"Changed Number Type", {
    {"impact_patterns.impacts.date_local", type date},
    {"start", type datetime},
    {"end", type datetime}
    }),
    #"Extracted Date" = Table.TransformColumns(#"Changed Date Type", {
        {"start", DateTime.Date, type date},
        {"end", DateTime.Date, type date}
    }),
    #"Changed Type1" = Table.TransformColumnTypes(#"Extracted Date",{{"phq_attendance", Int64.Type}}),
    #"Renamed Columns1" = Table.RenameColumns(#"Changed Type1", {
    {"impact_patterns.impacts.date_local", "date_local"},
    {"impact_patterns.impacts.value", "attendance_per_day"}
})
in
    #"Renamed Columns1"
```
{% endcode %}

As you can see we start with a comma to add on to the existing line, its positioning can be changed to the end of the existing line if you prefer, but its function is the same. The final pasted code should look something like this:

<figure><img src="../../../.gitbook/assets/CSV Power Query complete.png" alt=""><figcaption><p>CSV Power Query</p></figcaption></figure>

Hit Done.\
Hit Close & Apply and wait for the data transformation to finish processing.

<figure><img src="../../../.gitbook/assets/CSV Close &#x26; Apply.png" alt=""><figcaption><p>CSV Close &#x26; Apply</p></figcaption></figure>

After completing these steps, we have successfully loaded a CSV extract of PHQ Events data into Power BI ready for use in visuals and reporting. [See the Building the Report](connect-and-build-events-data-in-power-bi.md#guide-to-building-the-report) step below for the next steps.

### Snowflake Connection Method

To connect using Snowflake you will need the following knowledge about your organization's Snowflake environment. Ask your Snowflake Administrators for these settings or refer to Snowflake's official documentation links for the variables below:

1. Server Name: Usually in format <[account\_name](https://docs.snowflake.com/en/user-guide/admin-account-identifier#label-account-name)>.snowflakecomputing.com
2. Warehouse: A [warehouse](https://docs.snowflake.com/en/user-guide/warehouses-overview) is what you use to run queries. See which are available to you using the [SHOW WAREHOUSES](https://docs.snowflake.com/en/sql-reference/sql/show-warehouses) function.
3. Table Location: the Database, Schema, and Table Name for your [PredictHQ Data Share Events](https://docs.predicthq.com/integrations/third-party-integrations/snowflake) table.

To start, navigate to the Snowflake data connection via:

Get Data -> More -> Database -> Snowflake\


<figure><img src="../../../.gitbook/assets/New Snowflake Connection.png" alt=""><figcaption><p>Get Data -> More</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Select Snowflake Database.png" alt=""><figcaption><p>Database -> Snowflake</p></figcaption></figure>

The Server and Warehouse info we gathered above will need to be entered at this step.\
It should look something like the below, replacing square bracket placeholder variables for your Server and Warehouse info.

<figure><img src="../../../.gitbook/assets/Server and Warehouse (1).png" alt=""><figcaption><p>enter Server and Warehouse info</p></figcaption></figure>

Expand Advanced options and scroll down.

Fill the Database where the PredictHQ Events table lies in your Snowflake structure (case sensitive).\
Paste this SQL in the SQL box after substituting the Schema and Table Name. This code assumes no columns have been renamed:

{% code lineNumbers="true" fullWidth="true" %}
```sql
select e.event_id as id, e.parent_event_id, e.update_dt, e.title, e.category, ARRAY_TO_STRING(e.labels,',') as labels, e.phq_labels
    , e.phq_rank, e.phq_attendance, e.local_rank, e.status 
    , CONVERT_TIMEZONE('UTC', Timezone, Event_Start) AS "START", CONVERT_TIMEZONE('UTC', Timezone, Event_End) AS "END", e.predicted_end, e.timezone
    , val.value:value::INT as attendance_per_day, val.value:date_local::DATE as date_local  
    , e.country_code, e.entities, e.geo, e.placekey, e.impact_patterns
    , e.predicted_event_spend_accommodation, e.predicted_event_spend_hospitality, e.predicted_event_spend_transportation
    , e.place_hierarchies, 
From [Schema].[TableName] e    --replace with PredictHQ Events Data Share table location
, LATERAL FLATTEN(INPUT => impact_patterns) imp
, LATERAL FLATTEN(INPUT => imp.value:impacts) val
where val.value:date_local::DATE between '2024-01-01' and '2024-03-31'
    and status in ('active','predicted')
    and phq_attendance >= 1
    and category in ('community','concerts','conferences','expos','festivals','performing-arts','sports')
    and imp.value:vertical::STRING = 'accommodation' and val.value:position::STRING = 'event_day'
    and ARRAY_TO_STRING(PLACE_HIERARCHIES, ',') ilike '%5391959%'
```
{% endcode %}

This code is performing the data transformation and filtering in code. It filters to the parameters laid out in the [Example Parameters for this Guide](connect-and-build-events-data-in-power-bi.md#example-parameters-for-this-guide) section, and transforms some columns we will be using for ease of use in the report.\
The most important transformed column is the 'impact\_patterns' column which we use to find the attendance spread per day across a multi-day event. See [Impact Patterns ](https://docs.predicthq.com/getting-started/predicthq-data/impact-patterns)in our technical documentation for more information.&#x20;

This is what it should look like when filled in - with all square bracket placeholder text replaced.

<figure><img src="../../../.gitbook/assets/SQL Statement.png" alt=""><figcaption></figcaption></figure>

Click "OK". Click "Load Data" on the next screen.

Connection settings: DirectQuery is recommended for constant database connection. Import for one-off import of data from the database.

After completing these steps, we have successfully connected Events data from Snowflake into Power BI ready for use in visuals and reporting and automatic data refreshes. [See the Building the Report](connect-and-build-events-data-in-power-bi.md#guide-to-building-the-report) step below for the next steps.

### API Connection Method

PredictHQ has a few APIs that can be used to build reports, for this example, we will stick to the Events API. Starting this process assumes a PredictHQ API access token has been created by following the [API Quickstart guide](https://docs.predicthq.com/getting-started/api-quickstart).

Power BI will connect using the URL from the [Events API](https://docs.predicthq.com/api/events/search-events): [https://api.predicthq.com/v1/events/](https://api.predicthq.com/v1/events/) but, query parameters must be added to this URL  for the Power BI connection, in line with the parameters outlined in the [Example Parameters for this Guide](connect-and-build-events-data-in-power-bi.md#example-parameters-for-this-guide).&#x20;

Following these parameters and the [Events API](https://docs.predicthq.com/api/events/search-events) documentation we will end up with a URL string like the one below:

{% code overflow="wrap" fullWidth="true" %}
```url
https://api.predicthq.com/v1/events/?active.gte=2024-01-01&active.lt=2024-04-01&active.tz=America/Los_Angeles&category=community,conferences,concerts,expos,festivals,performing-arts,sports&state=active,predicted&phq_attendance.gte=1&place.scope=5391959&limit=500
```
{% endcode %}

Note: Scope uses the Place ID (geonames ID) for San Francisco (see our [tech docs for info on Place ID](https://docs.predicthq.com/getting-started/guides/geolocation-guides/searching-by-location/find-events-by-place-id)). If you were looking for events happening around a business location you would use the [within parameter](https://docs.predicthq.com/getting-started/guides/geolocation-guides/searching-by-location/find-events-by-latitude-longitude-and-radius) with the latitude and longitude of your business location and the radius from the suggested radius API. \
Time zone parameter (active.tz) filters results based on that given time zone, even though date results are returned in UTC.\
Limit parameter allows for more results returned per “page” which allows for faster loading, rather than the default 10 per page.

See also our [filtering guide](filtering-and-finding-relevant-events.md) for details on how to query the Events API for events impacting your locations.

With this API query string, event data can start to be loaded into Power BI.&#x20;

First, start a new report. Then select Get Data -> Web

<figure><img src="../../../.gitbook/assets/New Web Connection.png" alt=""><figcaption><p>Get Data -> Web connection</p></figcaption></figure>

Choose the Advanced tab, not the Basic default. Because the PredictHQ API is Bearer token authorized, the Advanced tab must be selected to include the API Access Token request header.

Add the HTTP request header with the following information:

1. URL parts: our created Events API URL from the above
2. Header: Authorization = Bearer api\_token where ‘\[api\_token]’ will be replaced with your PHQ API Access Token. Just replace ‘\[api\_token]’ with your actual API Access Token. Leave the ‘Bearer ’ part in

The filled-out information should look like this:

<figure><img src="../../../.gitbook/assets/API Connection.png" alt=""><figcaption><p>Web Connection URL and Header</p></figcaption></figure>

After clicking “OK”,  the Data Transformation page will open where data shaping options can be made before building the report.

It is recommended to rename the Query to something relevant, as it defaults to the connection URL string parameters which does not look neat.

In this guide, the Query is renamed to “PredictHQ Connection”.

<figure><img src="../../../.gitbook/assets/API Rename connection Query.png" alt=""><figcaption><p>Rename the Query</p></figcaption></figure>

In order to transform the columns, open Power Query and paste the code below to format and expand some columns for easy use. To do this, go to the Advanced Editor for this Query, right click on the Query name under Queries and click Advanced Editor:

<figure><img src="../../../.gitbook/assets/API go to Advanced Editor.png" alt=""><figcaption><p>Right click renamed Query -> Advanced Editor</p></figcaption></figure>

Replace the entire existing Power Query code with the one below, changing the 2 lines (Lines 4 and 8) that refer to ‘\[api\_token]’ with the PHQ API Access Token used previously.

This code expands out the 'impact\_patterns' column (see [Impact Patterns ](https://docs.predicthq.com/getting-started/predicthq-data/impact-patterns)in our technical documentation for more information) and filters it to accommodation and actual attendance distribution. It renames some essential columns. It also accounts for our API pagination, making sure all results are returned. It is an involved process with multiple steps - the Power Query below is the final output of this multi-stage transformation.&#x20;

{% code lineNumbers="true" fullWidth="true" %}
```powerquery
let
    #"PredictHQ Connection" = List.Generate( () =>
    [URL = "https://api.predicthq.com/v1/events/?active.gte=2024-01-01&active.lt=2024-04-01&active.tz=America/Los_Angeles&category=community,conferences,concerts,expos,festivals,performing-arts,sports&state=active,predicted&phq_attendance.gte=1&place.scope=5391959&limit=500",
     Result = Json.Document(Web.Contents(URL, [Headers=[Authorization="Bearer [api_token]"]]))],
    each [URL] <> null,
    each [
        URL = [Result][next],
        Result = Json.Document(Web.Contents(URL, [Headers=[Authorization="Bearer [api_token]"]]))
    ]
),
    #"Converted to Table" = Table.FromList(#"PredictHQ Connection", Splitter.SplitByNothing(), null, null, ExtraValues.Error),
    #"Expanded Column1" = Table.ExpandRecordColumn(#"Converted to Table", "Column1", {"Result"}, {"Column1.Result"}),
    #"Expanded Column1.Result" = Table.ExpandRecordColumn(#"Expanded Column1", "Column1.Result", {"results"}, {"Column1.Result.results"}),
    #"Expanded Column1.Result.results" = Table.ExpandListColumn(#"Expanded Column1.Result", "Column1.Result.results"),
    #"Expanded Column1.Result.results1" = Table.ExpandRecordColumn(#"Expanded Column1.Result.results", "Column1.Result.results", {"id", "title", "description", "category", "labels", "rank", "local_rank", "phq_attendance", "entities", "duration", "start", "end", "updated", "first_seen", "timezone", "location", "geo", "impact_patterns", "scope", "country", "place_hierarchies", "state", "private", "predicted_event_spend", "predicted_event_spend_industries", "phq_labels"}),
    #"Expanded impact_patterns" = Table.ExpandListColumn(#"Expanded Column1.Result.results1", "impact_patterns"),
    #"Expanded impact_patterns1" = Table.ExpandRecordColumn(#"Expanded impact_patterns", "impact_patterns", {"vertical", "impact_type", "impacts"}, {"impact_patterns.vertical", "impact_patterns.impact_type", "impact_patterns.impacts"}),
    #"Expanded impact_patterns.impacts" = Table.ExpandListColumn(#"Expanded impact_patterns1", "impact_patterns.impacts"),
    #"Expanded impact_patterns.impacts1" = Table.ExpandRecordColumn(#"Expanded impact_patterns.impacts", "impact_patterns.impacts", {"date_local", "value", "position"}, {"impact_patterns.impacts.date_local", "impact_patterns.impacts.value", "impact_patterns.impacts.position"}),
    #"Filtered Rows" = Table.SelectRows(#"Expanded impact_patterns.impacts1", each ([impact_patterns.vertical] = "accommodation" and [impact_patterns.impacts.position] = "event_day")),
    #"Changed Number Type" = Table.TransformColumnTypes(#"Filtered Rows",{{"impact_patterns.impacts.value", Int64.Type}}),
    #"Changed Date Type" = Table.TransformColumnTypes(#"Changed Number Type", {
    {"impact_patterns.impacts.date_local", type date},
    {"start", type datetime},
    {"end", type datetime}
    }),
    #"Extracted Date" = Table.TransformColumns(#"Changed Date Type", {
        {"start", DateTime.Date, type date},
        {"end", DateTime.Date, type date}
    }),
    #"Changed Type" = Table.TransformColumnTypes(#"Extracted Date",{{"phq_attendance", Int64.Type}}),
    #"Renamed Columns" = Table.RenameColumns(#"Changed Type", {
    {"impact_patterns.impacts.date_local", "date_local"},
    {"impact_patterns.impacts.value", "attendance_per_day"}
    })
in
    #"Renamed Columns"
```
{% endcode %}

Click Close & Apply and wait for the data transformation to finish processing through multiple API pages.

<figure><img src="../../../.gitbook/assets/API Close &#x26; Apply.png" alt=""><figcaption><p>API Close &#x26; Apply</p></figcaption></figure>

After this step the data is now ready to start building a report with, as it has been successfully loaded and transformed in Power BI. A template of this API Connection report pre-built is available at the end in the [Example API Connection Report Template](connect-and-build-events-data-in-power-bi.md#example-api-connection-report-template) section.

## Guide to Building the Report

Using either of the two methods above will get PredictHQ Events data loaded and transformed in the same format ready to be used in a report. Not all the columns were transformed, just the ones used in this guide.

This guide creates a connected chart and table that covers the defined time period and shows the attendance per day in the chosen location - in the example San Francisco city as a whole. The chart breaks up attendance per day for the visualization, but the table shows event details and attendance in full, not split by day. Date results are shown in UTC.

To begin, insert a blank chart and table visualization using the Insert -> New Visual tab options, with the chart on top taking up half the screen, and the table on the bottom filling the other half.

Group as one (shift-click both boxes, right-click on one of them, and click the Group -> Group option).

<figure><img src="../../../.gitbook/assets/Group Visuals.png" alt=""><figcaption><p>Blank chart and table grouped</p></figcaption></figure>

Before the next step of filling in the chart and table, add Filters for the page:\
drag the 'date\_local' field from the Data tab on the right to the “Filters on this page” section under Filters.&#x20;

Change the drop-down to Advanced filtering and add the following:

“_Is on or after_” start of the selected date range AND “_is before_” the day after the date range ends - click “apply filter” in the bottom right of the filter menu. \
In the example, those dates are anything on or after the 1st of January 2024 and anything before 1st of April 2024.

<figure><img src="../../../.gitbook/assets/Filter by date range.png" alt=""><figcaption><p>date_local Filter on page</p></figcaption></figure>

Now fill the chart axis.\
The X-axis gets filled with the date\_local field\
The Y-axis gets filled with the attendance\_per\_day field&#x20;

For the table, drag these fields over and resize the columns as needed to fit everything:

Table: id, title, category, phq\_attendance, start, end

For all fields that involve a date (date\_local, start, end), remove the default Date Hierarchy format to get the actual date showing. Use the dropdown in the Visualizations column and select the field name instead of “Date Hierarchy”. If Date Hierarchy is preferred, feel free to leave this as is.

<figure><img src="../../../.gitbook/assets/Remove Date Hierarchy.png" alt=""><figcaption><p>Remove Date Hierarchy</p></figcaption></figure>

For phq\_attendance in the table use the drop down to remove the summary, this summary isn’t actually grouping anything so is an unnecessary default that should be removed. Note that we only want to stop the summarization in the table, leave the chart as is.

<figure><img src="../../../.gitbook/assets/don&#x27;t summarize.png" alt=""><figcaption><p>Remove Summarization from the Table</p></figcaption></figure>

Rename the chart title by clicking on the chart and going to the Visualizations tab -> General -> Title. Let’s rename it to “Event Attendance per day in San Francisco”.

<figure><img src="../../../.gitbook/assets/Rename title.png" alt=""><figcaption><p>Chart Title Rename</p></figcaption></figure>

Click on the "phq\_attendance" column in the table twice to sort by highest to lowest attendance.

The final result should look like the following:

<figure><img src="../../../.gitbook/assets/Final Result.png" alt=""><figcaption><p>Final Report Result</p></figcaption></figure>

The picture above shows how this analysis can be used; by clicking on a spike (or any period on the chart) the report shows the events active during that period. The table data does not show the attendance per day like the chart, but the overall attendance of the event's full duration.

A useful addition to this basic view could be a drill down on the table by adding a new table visual to the group that has the 'id', 'date\_local', and 'attendance\_per\_day' columns, showing how the attendance of an event has been spread out over multiple days (if it is a multi-day event). For more understanding of multi-day events, see our [Working with Multi-day Events](https://docs.predicthq.com/getting-started/guides/date-and-time-guides/working-with-multi-day-and-umbrella-events) documentation.

Customers can add their own data to this chart to compare peaks and troughs of attendance vs sales in a basic comparison report. For deeper analysis into these kinds of reports, we suggest using our [Beam](https://docs.predicthq.com/api/beam) functionality to provide a deeper insight as to which types of events impact demand, as the Events API will only give a high-level view of the story without any additional analysis from PredictHQ to provide more in-depth information.

### Example API Connection Report Template

Below is a downloadable Power BI template that will automatically create the example report used throughout this guide, using the API Connection method.

Upon opening the template, you will be prompted to enter an API Access Token. Inputting this token will enable the report to automatically populate and build according to the parameters set forth in this guide.

<figure><img src="../../../.gitbook/assets/Fill variable on template.png" alt=""><figcaption><p>Fill PredictHQ API Access Token in the report when prompted</p></figcaption></figure>

**Example Report:**

{% file src="../../../.gitbook/assets/PredictHQ API Connection Example Report.pbit" %}
