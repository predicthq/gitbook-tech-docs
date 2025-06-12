# Viewing the Table of Results in Beam

Below the graph is a table of results in Beam. The table shows details on the most impactful days found by Beam including the highest rank events on those days. It also includes the statistics on the decomposed historical demand and the future predicted attendance for the predicted future impact.

The table has two tabs:

### **Predicted Future Tab**

Beam's advanced models correlate your historical demand data with extensive, verified event data to identify days when events will significantly influence the demand for a business. This tab shows future events that are predicted to impact your demand.

<figure><img src="../../.gitbook/assets/image (63).png" alt=""><figcaption><p>Predicted Future tab of impactful days in a Beam Analysis</p></figcaption></figure>

It also shows Predicted Attendance per day. This is based on the number of people who are predicted to attend events on those days in the radius set for the Beam analysis.

This tab shows up to 10 impactful days if you have access to the future time-period in your subscription. If you do not have access you will see an option to upgrade your subscription to get access to more data to see the future predicted events.

The top events occurring each day in the area analyzed by Beam are shown in order of the highest rank to the lowest rank. If more events are present on the day than are shown in the table then click on the + X Events link to see more. This will open the search page to show you more events.

If you want to get a full list of events from the API use the "**Get all Event details**" option from the "..." sub-menu next to "Get Forecasting Features".

### **Historical Tab**

Beam's advanced models analyze your historical demand data using verified event data. This helps identify past event impacts on demand, providing valuable insights for future planning.

<figure><img src="../../.gitbook/assets/image (65).png" alt=""><figcaption><p>Historical tab of impactful days in a Beam Analysis</p></figcaption></figure>

This tab shows the top impactful days in the past when events have impacted your demand. Not that this table doesn't show all the days where events have impacted demand just some of the top examples. You can use the APIs to download more details.

The top events occurring each day in the area analyzed by Beam are shown in order from the highest rank to the lowest rank. If more events are present on the day than are shown in the table then click on the + X Events link to see more. This will open the search page to show you more events.

#### Values Shown in the Table

The table has the following information:

* **Date -** The date
* **Actual Demand** - The actual demand that was uploaded.
* **Baseline Demand** - The baseline extracted by the Beam models from your underlying demand data. This will show the underlying pattern in your demand data with the remainder removed. It reflects typical demand without outliers.
* **Predicted Attendance** - Reflects the total amount of people attending events within the location covered by the beam analysis. This is determined by the events within the radius used by the Beam analy
* **Remainder** - Expected demand produced by the Beam Decomposition model. This removes the impact of seasonality and overall growth trends, to isolate any irregular factors that might impact your demand. This indicates spikes or dips in demand that may be caused by events.
* **Top events driving demand** - Shows an example event occurring on that day. This table will show the highest-ranked events first. The icons indicate the event category. Click on the event to view the full details of the event.



\
