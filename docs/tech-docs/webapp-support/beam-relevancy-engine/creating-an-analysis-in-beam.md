---
description: Use Beam to find correlation between your demand and events data
---

# Creating an Analysis in Beam

When you log in to the [WebApp](https://control.predicthq.com/) as a user, you will see the Beam option on the left-hand side menu bar.

Clicking on the Beam link or icon will direct you to an empty screen or will show a list of previous analyses.

An _analysis_ using Beam means that you have uploaded demand data for a specific location, within the time-period defined by the uploaded data. Beam takes the demand data together with PredictHQ daily aggregated attendance data to look for the effect on demand caused by events and finds a correlation. The results are shown in different formats:

* AI analysis
* A time series graph
* Table
* PDF report
* View ML features option
* Export a CSV

Each visualization contains information on the correlation analysis determined by Beam.

To initiate the analysis in Beam, click on _Create New Analysis_ in the top right-hand corner, and you should see the screen below, prompting you to input details about your business.

<figure><img src="../../.gitbook/assets/image (42).png" alt=""><figcaption><p>Create Beam Analysis page in the WebApp</p></figcaption></figure>

### Name <a href="#name-object-object" id="name-object-object"></a>

Input the desired name of your analysis. This is free form, but suggest inputting a name that you can recall and differentiate if subsequent similar analyses are made.

For example: _nameofuser\_daterange\_analysisdate\_analysiscount._

* _nameofuser_: Record multiple users or departments testing out Beam for different purposes.
* _daterange_: Represents the range of dates within the data set that should be able to distinguish between two analysis across different periods.
* _analysisdate_ and _analysiscount_: The date of analysis and the number of the analysis to keep track of multiple analyses.

For example _JSmith\_Boston\_2018\_20200403\_1_

### Location <a href="#location" id="location"></a>

When creating an analysis in Beam, it's essential to specify the location of interest. You can specify the location of interest by simply selecting a location from your Saved Locations list or adding a new one. Remember, only a Street Address and Radius location type are suitable for Beam Correlation.

To add a location, click the "Add Location" button in the Location dropdown menu. Check [here](../location-insights/how-do-i-add-a-location.md) for more details.

<figure><img src="../../.gitbook/assets/image (43).png" alt=""><figcaption><p>Selecting a location in the Create Beam Analysis page</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (44).png" alt=""><figcaption><p>Adding a Saved Location to the list of locations in the Beam Analysis page</p></figcaption></figure>

When you create a location this sets a radius using the [Suggested Radius](https://www.predicthq.com/tools/suggested-radius) feature. The Beam analysis looks for events within this radius.
