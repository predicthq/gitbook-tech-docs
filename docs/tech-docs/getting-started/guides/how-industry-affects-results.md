# How Industry Affects Results

PredictHQ tailors results to your industry. When you specify an industry, we apply industry-specific patterns and thresholds that reflect how real-world events affect businesses like yours.

## Supported Industries

PredictHQ APIs currently support the following industries. Use the Industry Value when specifying an industry in an API request. If your business doesn’t map exactly, use the Examples / Adjacent column to find the closest fit.

| Supported Industry                     | Industry Value   | Examples / Adjacent Industries                                                       |
| -------------------------------------- | ---------------- | ------------------------------------------------------------------------------------ |
| Accommodation                          | `accommodation`  | Hotels, hostels, co-working spaces with short-term stays.                            |
| Consumer Packaged Goods (CPG)          | `cpg`            | Packaged food & beverages, household goods.                                          |
| Leisure, Travel & Tourism              | `tourism`        | Entertainment venues (cinemas, casinos, theme parks), attractions, DMOs, OTAs.       |
| Marketing and Advertising              | `marketing`      | Agencies, ad networks, campaign platforms.                                           |
| Parking                                | `parking`        | Car parks, garages.                                                                  |
| Food and Beverage (Restaurants & Bars) | `restaurants`    | Cafes, pubs, quick service restaurants, hospitality venues.                          |
| Retail                                 | `retail`         | Supermarkets, fashion, electronics, gyms/fitness centers (if sales-oriented).        |
| Transportation and Delivery            | `transportation` | Rail, buses, rideshare, delivery services.                                           |
| Other                                  | `other`          | If your business does not clearly fit into one of the above industries, use `other`. |

## Where Industry Matters

Industry is used across our systems to tune how events are interpreted and modeled for your business. This includes areas like impact patterns, thresholds, and catchment radius recommendations.

* **Suggested Radius API**\
  Radius recommendations vary by industry, since the catchment area for demand differs across sectors.
* **Predicted Impact Patterns**\
  For each event, we calculate its leading and lagging impact per industry. These patterns are then used in the Features API to ensure event impacts reflect your sector.
* **Beam**\
  Beam builds on these industry-tuned patterns and thresholds, and further personalizes results with your own demand data.
* **Forecasts API**\
  Uses industry in the same way as Beam (industry is passed through to Beam behind the scenes).

## Key Takeaways

* Specifying your industry ensures results reflect real-world demand in your sector.
* If your business doesn’t clearly fit into a supported industry, choose `other`.
* Adjacent industries can map to supported ones - use the closest fit.

## Related Guides

* [industry-specific-event-filters.md](industry-specific-event-filters.md "mention") - shows default event categories and local rank thresholds by industry when you can’t yet use Beam (or for custom filtering).
* [industry-tuned-predictions.md](../core-concepts/industry-tuned-predictions.md "mention") - explains how industry-specific modeling works across PredictHQ products.
