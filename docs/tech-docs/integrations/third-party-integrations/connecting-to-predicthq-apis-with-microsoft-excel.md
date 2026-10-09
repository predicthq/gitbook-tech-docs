---
description: Learn how to connect PredictHQ data to Microsoft Excel using APIs.
---

# Connecting to PredictHQ APIs with Microsoft Excel

## Overview

The data used in this guide is based on a popular location, in our case San Francisco City as a whole. Change the location from San Francisco to the location you want to look at.

Below are the main steps involved in this guide:

1. Building Report Parameters around a Location
   * Example Parameters for this Guide
2. Select an Input method
   * API connection
3. View events data in Excel

**Requirements:**

1. API: [API Access Token](../../getting-started/api-quickstart.md)
2. Microsoft Excel

### Example parameters for this guide:

1. **Date**: user-defined, this tutorial uses a 3-month period from January 1st to March 31st 2024
2. **Categories**: community, conferences, concerts, expos, festivals, performing-arts, sports - these are our [attended categories](https://docs.predicthq.com/getting-started/predicthq-data/event-categories)
3. **Event State**: Active and Predicted
4. **Predicted Attendance** (`phq_attendance`): attended events only - filtered to events with an attendance of at least 1
5. **Location**: San Francisco city (place ID [5391959](https://www.geonames.org/5391959/san-francisco.html))

Location could be substituted for a specific latitude and longitude relating to an individual store, or could be scoped even wider depending on need. We suggest utilizing our [Predicted Impact Area API](https://docs.predicthq.com/api/impact-area/get-impact-area) to hone in on a specific shop location and pull only events within a more accurate area based on those results. For now, we will look at the citywide events in San Francisco as our example.

### How to get events data via PredictHQ's API

This guide provides details on how to load PredictHQ's event data into Microsoft Excel using the Events API. We provide examples for Excel running in Microsoft Windows. In this tutorial we'll show you how to connect to the API and load data into a Spreadsheet. Start by creating a new empty Spreadsheet in Microsoft Excel.

PredictHQ has a number of different APIs that can be used to build reports, in this example, we will stick to the Events API. Starting this process assumes a PredictHQ API access token has been created by following the [API Quickstart guide](https://docs.predicthq.com/getting-started/api-quickstart).

Microsoft Excel connects using the URL for the [Events API](https://docs.predicthq.com/api/events/search-events): `https://api.predicthq.com/v1/events/` but you must add query parameters to this URL for the Excel connection, in line with the parameters outlined in the [Example Parameters for this Guide](connecting-to-predicthq-apis-with-microsoft-excel.md#example-parameters-for-this-guide).

Following these parameters and the [Events API](https://docs.predicthq.com/api/events/search-events) documentation the result is a URL string like the one below:

{% code overflow="wrap" fullWidth="true" %}
```url
https://api.predicthq.com/v1/events/?active.gte=2024-01-01&active.lt=2024-04-01&active.tz=America/Los_Angeles&category=community,conferences,concerts,expos,festivals,performing-arts,sports&state=active,predicted&phq_attendance.gte=1&place.scope=5391959&limit=500
```
{% endcode %}

{% hint style="info" %}
Note: Scope uses the Place ID (geonames ID) for San Francisco (see our [tech docs for info on Place ID](https://docs.predicthq.com/getting-started/guides/geolocation-guides/searching-by-location/find-events-by-place-id)). If you were looking for events happening around a business location you would use the [within parameter](https://docs.predicthq.com/getting-started/guides/geolocation-guides/searching-by-location/find-events-by-latitude-longitude-and-radius) with the latitude and longitude of your business location and the area from the Predicted Impact Area API.
{% endhint %}

Time zone parameter (active.tz) filters results based on that given time zone, even though the API returns date results in UTC.

Limit parameter allows for more results returned per “page” which allows for faster loading, rather than the default 10 per page.

See also our [filtering guide](../../getting-started/guides/events-api-guides/filtering-and-finding-relevant-events.md) for details on how to query the Events API for events impacting your locations.

With this API query string, event data can start to be loaded into Microsoft Excel.

First, create a new Spreadsheet. Then, to open the data connection options:

1. Click the **Data** tab.
2. On the **Data** tab, click **Get Data**.

<figure><img src="../../.gitbook/assets/image (82).png" alt="The Data tab in Microsoft Excel with the Get Data menu open"><figcaption></figcaption></figure>

Choose the **Advanced** tab, not the **Basic** default. Because the PredictHQ API is Bearer token authorized, select the Advanced tab to include the API Access Token request header.

Add the HTTP request header with the following information:

1. **URL parts**: our created Events API URL from the above: `https://api.predicthq.com/v1/events/?active.gte=2024-01-01&active.lt=2024-04-01&active.tz=America/Los_Angeles&category=community,conferences,concerts,expos,festivals,performing-arts,sports&state=active,predicted&phq_attendance.gte=1&place.scope=5391959&limit=500`
2. **HTTP request header parameters**:
   1. In the first field, enter `Authorization`
   2. In the second field, enter `Bearer <api_token>`. where <`api_token>` will be replaced with your PredictHQ API Access Token. Replace <`api_token>` with your actual API Access Token. Leave the ‘Bearer ’ part in. Below is what the fields look like once you enter your API key.\
      \
      ![](<../../.gitbook/assets/image (83).png>)\\

The filled-out information should look like this (except that api\_key should be replaced with your actual api\_key)

<figure><img src="../../.gitbook/assets/API Connection.png" alt="The Excel web connection dialog with the Events API URL and the Authorization header filled in"><figcaption><p>Web Connection URL and Header</p></figcaption></figure>

After clicking **OK**, the Data Transformation page opens where you can choose data shaping options before building the report.

Rename the Query to something relevant, as it defaults to the connection URL string parameters which does not look neat. Rename it to “PredictHQ Connection”. If you use a different name, change the Power Query to match.

<figure><img src="../../.gitbook/assets/API Rename connection Query.png" alt=""><figcaption><p>Rename the Query</p></figcaption></figure>

To format and expand some columns, paste the following code into the Advanced Editor for this Query. To open the Advanced Editor:

1. Under **Queries**, right-click the Query name.
2. Click **Advanced Editor**.

<figure><img src="../../.gitbook/assets/API go to Advanced Editor.png" alt=""><figcaption><p>Right click renamed Query -> Advanced Editor</p></figcaption></figure>

To update the Power Query code:

1. Replace the entire existing Power Query code with the following code.
2. In Lines 4 and 8, replace ‘\[api\_token]’ with the PredictHQ API Access Token you used previously.

{% hint style="info" %}
This example doesn't work unless you replace the \[api\_token] with your token.\
Lines 2 and 11 refer to the Query name, if you've named it something other than "PredictHQ Connection" you will need to replace it here aswell.
{% endhint %}

This code expands out the 'impact\_patterns' column (see [Predicted Impact Patterns ](https://docs.predicthq.com/getting-started/predicthq-data/impact-patterns)in our technical documentation for more information) and filters it to accommodation and actual attendance distribution. It renames some essential columns. It also accounts for our API pagination, making sure all results are returned. The final output of this multi-stage transformation is the following Power Query:

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
    #"Expanded Column1.Result.results1" = Table.ExpandRecordColumn(#"Expanded Column1.Result.results", "Column1.Result.results", {"id", "title", "description", "category", "labels", "rank", "local_rank", "phq_attendance", "entities", "duration", "start", "start_local", "end", "end_local", "updated", "first_seen", "timezone", "location", "geo", "impact_patterns", "scope", "country", "place_hierarchies", "state", "private", "predicted_event_spend", "predicted_event_spend_industries", "phq_labels"}),
    #"Expanded impact_patterns" = Table.ExpandListColumn(#"Expanded Column1.Result.results1", "impact_patterns"),
    #"Expanded impact_patterns1" = Table.ExpandRecordColumn(#"Expanded impact_patterns", "impact_patterns", {"vertical", "impact_type", "impacts"}, {"impact_patterns.vertical", "impact_patterns.impact_type", "impact_patterns.impacts"}),
    #"Expanded impact_patterns.impacts" = Table.ExpandListColumn(#"Expanded impact_patterns1", "impact_patterns.impacts"),
    #"Expanded impact_patterns.impacts1" = Table.ExpandRecordColumn(#"Expanded impact_patterns.impacts", "impact_patterns.impacts", {"date_local", "value", "position"}, {"impact_patterns.impacts.date_local", "impact_patterns.impacts.value", "impact_patterns.impacts.position"}),
    #"Filtered Rows" = Table.SelectRows(#"Expanded impact_patterns.impacts1", each ([impact_patterns.vertical] = "accommodation" and [impact_patterns.impacts.position] = "event_day")),
    #"Changed Number Type" = Table.TransformColumnTypes(#"Filtered Rows",{{"impact_patterns.impacts.value", Int64.Type}}),
    #"Changed Date Type" = Table.TransformColumnTypes(#"Changed Number Type", {
    {"impact_patterns.impacts.date_local", type date},
    {"start", type datetime}, {"end", type datetime},
    {"start_local", type datetime}, {"end_local", type datetime}
    }),
    #"Extracted Date" = Table.TransformColumns(#"Changed Date Type", {
        {"start", DateTime.Date, type date}, {"end", DateTime.Date, type date},
        {"start_local", DateTime.Date, type date}, {"end_local", DateTime.Date, type date}
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

The code in the Advanced Editor should look like the following screenshot:

<figure><img src="../../.gitbook/assets/API Power Query complete (1).png" alt=""><figcaption></figcaption></figure>

Click **Close & Apply** and wait for the data transformation to finish processing through multiple API pages.

<figure><img src="../../.gitbook/assets/API Close &#x26; Apply.png" alt=""><figcaption><p>API Close &#x26; Apply</p></figcaption></figure>

After this step the data is now ready to start building a report with, as it has been successfully loaded and transformed in Microsoft Excel. You should see a Spreadsheet like that shown below:

<figure><img src="../../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

You now have a connection to the API that you can refresh to get updated data.
