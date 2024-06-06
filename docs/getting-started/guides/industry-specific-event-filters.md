---
description: >-
  Learn how to effectively filter PredictHQ event data with industry-specific
  recommendations.
---

# Industry-Specific Event Filters

With so many events taking place, it is important to filter out the noise and focus only on events that are relevant to your business. Use this guide in conjunction with our APIs, such as Events API and Features API, and consult [Broken link](broken-reference "mention") for detailed information.

\
These recommendations are intended as starting points and may need to be adapted for your specific locations. Test out these filters and contact [our team](https://www.predicthq.com/contact) for additional guidance.

## Location Type

How a catchment area is defined for a store or location varies by industry as events impact industries differently. Setting the area too small may result in important events being missed, while an excessively large area can introduce unnecessary noise.&#x20;

For stores and locations where proximity to events is important, such as those in Retail and Parking, a radius-based location approach is recommended. For industries like Transportation & Delivery, which may be influenced by broader regional events, city-level locations are advisable. We suggest the following location types as a starting point:

| Industry                                      | Location Type |
| --------------------------------------------- | :-----------: |
| Accommodation                                 |  Radius-based |
| Consumer Packaged Goods                       |      City     |
| Food and Beverage (also known as Restaurants) |  Radius-based |
| Grocery and Supermarkets                      |  Radius-based |
| Leisure, Travel and Tourism                   |      City     |
| Marketing                                     |      City     |
| Parking                                       |  Radius-based |
| Retail                                        |  Radius-based |
| Transportation and Delivery                   |      City     |
| Other                                         |      City     |

To retrieve events for different location types, use the following approaches:

<details>

<summary>Radius-based Locations</summary>

**Using latitude, longitude, and radius**

1. Determine the appropriate radius using the [Suggested Radius API](https://docs.predicthq.com/api/suggested-radius/get-suggested-radius).
2. Configuration:
   1. For the Events API, use the `within` field.
   2. For the Features API and Beam API, use the `location` field.

**Using location IDs**

1. Create Saved Locations via [Location Insights](https://www.predicthq.com/support/category/location-insights) in Control Center or at scale using the [Saved Locations API](https://docs.predicthq.com/api/saved-locations).
2. Configuration:
   1. For the Events API, use the `saved_location.location_id` field.
   2. For the Features API, use the `location` field.

</details>

<details>

<summary>City Locations</summary>

**Using place IDs**

1. Find the place ID for a city using the [Places API](https://docs.predicthq.com/api/places/search-places).
2. Configuration:
   1. For the Events API, use the `place.scope` field.
   2. For the Features API, use the `location` field.

</details>

{% hint style="info" %}
For more information on defining locations by API, see [overview](../../api/overview/ "mention").
{% endhint %}

## Relevant Event Categories

With [almost two dozen event categories](../predicthq-data/event-categories/) available, knowing which ones are relevant to your business is essential. We strongly recommend using [Demand Analysis](https://www.predicthq.com/support/beam-overview) to automatically identify important categories for your specific stores or locations. Access Demand Analysis via [Control Center](https://control.predicthq.com/beam) or the [Beam API](../../api/beam/). Alternatively, explore these industry-level categories as a starting point:

| Industry                                      |                                   Relevant Event Categories                                  |
| --------------------------------------------- | :------------------------------------------------------------------------------------------: |
| Accommodation                                 |                   concerts, conferences, expos, festivals, performing-arts                   |
| Consumer Packaged Goods                       |             public holidays, performing-arts, conferences, conferences, community            |
| Food and Beverage (also known as Restaurants) |              public holidays, performing-arts, conferences, concerts, festivals              |
| Grocery and Supermarkets                      |             public holidays, performing-arts, conferences, conferences, community            |
| Leisure, Travel and Tourism                   |             public holidays, performing-arts, conferences, conferences, community            |
| Marketing                                     |             public holidays, performing-arts, conferences, conferences, community            |
| Parking                                       |                 public holidays, community, concerts, expos, performing-arts                 |
| Retail                                        |              public holidays, performing-arts, community, conferences, festivals             |
| Transportation and Delivery                   |             public holidays, performing-arts, conferences, conferences, community            |
| Other                                         | public holidays, performing-arts, concerts, conferences, community, festivals, expos, sports |

## Minimum PHQ Rank

Setting a minimum [PHQ Rank](../predicthq-data/ranks/phq-rank.md) is important for focusing on events that are likely to influence your demand, helping to exclude those that are too small or irrelevant. We recommend the following PHQ Rank thresholds:

| Industry                                      | Minimum PHQ Rank |
| --------------------------------------------- | :--------------: |
| Accommodation                                 |        35        |
| Consumer Packaged Goods                       |        30        |
| Food and Beverage (also known as Restaurants) |        30        |
| Grocery and Supermarkets                      |        30        |
| Leisure, Travel and Tourism                   |        30        |
| Marketing                                     |        30        |
| Parking                                       |        35        |
| Retail                                        |        50        |
| Transportation and Delivery                   |        30        |
| Other                                         |        30        |
