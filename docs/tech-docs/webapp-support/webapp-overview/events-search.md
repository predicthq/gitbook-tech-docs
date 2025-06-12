# Events Search

### Searching for Events in the WebApp

Find events with our easy-to-use search tool. Increase visibility into the millions of different events happening around the world to understand which ones may have an impact on your business. See results in a variety of ways, including a list, map, or calendar view.

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption><p>Events Search in the WebApp</p></figcaption></figure>

Note that search is set up to display events that you have access to under your subscription. So if you have access to specific cities like New York and Boston, you will only see events from those cities.

The time zone used in the search is the time zone set in your profile within the WebApp.

To use it, choose the categories, locations, ranks, and date range you want to search. Choose more filters. The search supports the following filters:

### Search Filters

Filters can be used to narrow down your search results. Your filters will be remembered per device until you change them. So, for example, once you search for a particular location and set of categories those search filters will be remembered the next time you load the search until you change them. Click the cross next to each filter to clear it.

See below for a list of filters:

* **Categories** - choose one or more categories to view events under those categories. See our [categories page](https://www.predicthq.com/intelligence/data-enrichment/event-categories) for an overview.\

* **Date range** - specify the date range. You can search for future, or past events. Choose from preconfigured date ranges, or set a custom date range on the calendar. Note that the date ranges available are limited by what you have access to in your subscription.
* **Labels** - Within categories, we have different labels. For example, labels within the sports category indicate what type of sporting event you are looking at.
* **Event name** - This option searches the event title and description. It's a way to search for a specific event or to search for events with text in their title or description.
* **PHQ Attendance** - Filter by PHQ attendance to find events above a certain attendance, or within an attendance range. PHQ attendance indicates how many people our advanced models predict will attend an event. For example, you might want to find all events of 10,000 PHQ attendance and above for a city. To do that, set the from value to 10,000.
* **Rank** - Filter by one of our 2 ranks: PHQ Rank or Local Rank. Higher-ranked events will tend to be larger events. PHQ Rank is based on the number of people predicted to attend the event. Filter for large PHQ rank events to find large events in your area. Find out more about our ranks [here](https://www.predicthq.com/tools/rankings).
* **Event status** - By default, the status shows active, canceled, predicted, and postponed. Change the status to view certain event statuses. The available statuses are:
  * Active - Active events where the details are confirmed.
  * Canceled - Events that have been canceled.
  * Postponed - Events that have been postponed from the original announced dates and times.
  * Predicted - Future events that we predict will occur but where all the details are not finalized. They could be events that haven’t been scheduled or even announced yet, but are expected to occur – based on years of historical event, entity, demand, and venue data. Or they could be events we know are going to occur like an upcoming sports semi-final game but where the location or timing isn't yet confirmed. See [predicted-events.md](../../getting-started/predicthq-data/predicted-events.md "mention") for more details.

#### Choose Your Location

When searching for events, a key value to choose is the location or locations you want to search. By default, if you don't set locations for some plans the search will return events for all the locations that you have access to under your subscription. For other plans, you will need to choose a location to search.

Note: Depending on your plan you may see a different location control when searching.

In our combined location search control (released in June 2024) you can search on a street address, a geographic area (like a city, country, state, region, or country), or for a [saved location](../location-insights/). Saved Locations are listed first at the top of the control.

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption><p>Location filter in the Events Search page</p></figcaption></figure>

To search on a street address enter the street address and then choose the relevant result from the results shown - below I searched on "130 W 46th St" for an address in New York. Behind the scenes, we locate the latitude and longitude for the address look up the [suggested radius](https://www.predicthq.com/tools/suggested-radius), and then search for events in the radius.

<figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption><p>Searching by street address in the Location filter</p></figcaption></figure>

This is a smart search control that will look at what you've entered and try to determine if it's a street address, geographic area, or a saved location. If you have any problems with the search to recognize the right type we'd suggest you [create a saved location ](../location-insights/how-do-i-add-a-location.md)and configure that to be the type you need and then search on that saved location.

#### Selecting Multiple Locations

By default, you select 1 location at a time when using search. To select multiple locations toggle the "enable multiple select" at the bottom of the dialog as shown below.

When you select multiple locations there are some limits to be aware of. You can select multiple geographic areas (like multiple cities or states). You can also select multiple saved locations. But you cannot select a geographic area and a saved location as they are different types of locations.

See below for an example of entering multiple geographic area (city, state, country type) locations:

<figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption><p>Selecting multiple locations by geographic area (city, state, country type) in the Location filter</p></figcaption></figure>

Below is another example of searching on multiple saved locations (also known as [location insights](../location-insights/an-overview-of-location-insights.md) locations).

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption><p>Selecting multiple locations by Saved Locations in the Location filter</p></figcaption></figure>

You can search on multiple geographic areas or multiple saved locations but you cannot mix the two types.

**Using Latitude and Longitude in the New Locations Control**

If you want to search on a particular address you can enter that address into the location control. Sometimes though you may want to use latitude and longitude directly in the search. For example, maybe you have a list of coordinates in a spreadsheet for different locations as latitude and longitude and you want to find events in these locations.

To do this enter a latitude and longitude into the location control and it will recognize it, look up the [suggested radius](https://www.predicthq.com/tools/suggested-radius), and allow you to search on it. After entering the latitude and longitude you will see it shown below in the control. Click on it to search for events at this location. See the screenshot below:

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption><p>Searching location by latitude and longitude in the Location filter</p></figcaption></figure>

If you want to override the suggested radius you can also enter a radius in the format `<radius number><unit>@<lat>,<long>`. For example `5km@50.63449,5.58148` to set the radius to 5 kilometers for those coordinates or `6mi@50.63449,5.58148` to set the radius to 6 miles. Units supported are:

* `km - kilometers`
* `m - meters`
* `mi - miles`
* `ft - feet`

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption><p>Searching by latitude and longitude with a specified radius in the Location filter</p></figcaption></figure>

### List View

The WebApp List view shows a list of events. The events shown are based on the filters you've selected. You can change the page size at the bottom of the list to show more events. By default, the list view will show all the events available in your subscription.

<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption><p>Events search result in List view</p></figcaption></figure>

Events are ordered by the sort parameter. Choose your sort values and run your search to see a list of events that you have access to under your plan.

The list view calls our [Events API](../../api/events/) to get back the events data. All the data you see in the list view can be retrieved using the API. See our [tech docs](../../) for more info on using the API.

### Map View

Try our map view to see the events on a map.

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption><p>Events search result in Map view</p></figcaption></figure>

### Calendar View <a href="#calendar-view" id="calendar-view"></a>

The calendar will show you upcoming events in a week, month, or year view.

<figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption><p>Events search result in Calendar view</p></figcaption></figure>

### Live TV Events <a href="#live-tv-events" id="live-tv-events"></a>

See [can-you-access-live-tv-events-via-the-webapp.md](../tools/live-tv-events/can-you-access-live-tv-events-via-the-webapp.md "mention")

### Export Events

See [export-events-data-from-the-webapp.md](../getting-started/export-events-data-from-the-webapp.md "mention")
