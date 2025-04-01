# Grouping Analyses in Beam

### What is an Analysis? <a href="#what-is-an-analysis" id="what-is-an-analysis"></a>

An Analysis in [Beam](./) is an evaluation of a particular demand data set for a specific location and date range. This can be created in the [WebApp](https://control.predicthq.com/beam) from any location you define or one of your saved locations in [Location Insights](https://control.predicthq.com/location-insights). Alternatively, you can create Analyses at scale via the [Beam API](../../api/beam/).

### Why group Analyses? <a href="#why-group-analyses" id="why-group-analyses"></a>

While single Analyses are ideal, offering insights tailored to each store or location, grouping Analyses can present a more practical approach as it provides a manageable, aggregated view across multiple stores or locations. This can be useful for businesses, such as retail chains, that manage operations at a regional or state level. Group Analyses support these operations, like marketing campaigns, inventory management, and demand forecasting, by delivering aggregated insights consolidated across all stores.

### How to effectively create Groups <a href="#how-to-effectively-create-groups" id="how-to-effectively-create-groups"></a>

Creating groups within Beam requires careful thought and consideration. Follow these guidelines for optimal results:

1. **Group Size**: Include at least two Analyses in a Group.
2. **Location Replication**: Prevent unwanted bias by ensuring each Analysis within a Group corresponds to a unique store or location.
3. **Demand Consistency**: Ensure all Analysis within a Group are based on the same demand and unit of measurement. For example, in-store pizza sales in $US.
4. **Country Consistency**: Ensure all stores or locations are within the same country to maintain a level of homogeneity.
5. **Temporal Consistency**: Aim for either identical, or at least, substantial overlap in date ranges across Analyses.
6. **Industry Consistency**: Ensure all Analyses in a Group are from the same industry, such as accommodation, hospitality, retail, or parking.
7. **Group Membership**: Define Groups based on meaningful criteria that offer strategic value. Common grouping parameters include:
   * Geographical Location: e.g. by state, region, or city.
   * Type of Area: e.g. urban or rural areas.
   * Store Characteristics: e.g. standalone or inside a mall.
   * Performance: e.g. high, medium or low sales.

### How to create Group Analyses in Beam <a href="#how-to-create-group-analyses-in-beam" id="how-to-create-group-analyses-in-beam"></a>

At least two Analyses are required to create a meaningful Group. First create Analyses, then create Groups.

**Analyses**:

* Analysis creation: [Analyses](creating-an-analysis-in-beam.md) can be created in the [WebApp](https://control.predicthq.com/beam) or via the [Beam API](../../api/beam/).
* Analysis name: This user-defined field serves labeling and identification purposes. Incorporating group membership details into the Analysis name helps in identifying relevant Analyses, thereby speeding up the group creation step. For example, ‘groupA\_\_store123\_\_instore\_pizza\_sales\_\_2022’.

**Groups**:

* Group creation: Groups can be created in the [WebApp](https://control.predicthq.com/beam/groups) by selecting specific Analyses or via the [Beam API](../../api/beam/analysis-groups/) by passing a list of Analysis IDs.
* User-defined grouping: Users can define their own Groups based on business needs.&#x20;
* Flexible group membership: An Analysis can be part of more than one Group, providing greater flexibility.

### How to use Category Importance <a href="#how-to-use-category-importance" id="how-to-use-category-importance"></a>

Category importance at the group-level follows a similar interpretation as that of single [Analyses](https://www.predicthq.com/support/viewing-the-category-importance-notebook-in-beam). It represents a weighted aggregation of the Category Importance from each contributing Analysis, where the weights are proportional to the average daily demand of each. This gives more influence to Analyses with a larger share of the overall group demand.&#x20;

As with single Analyses, the important categories highlight key drivers of demand for your stores or locations, though with a more generalized view. Different strategic actions can be taken based on these insights, for example:

1. **Improved demand forecasting accuracy**:
   * Integrate Category Importance results using the [Beam API](../../api/beam/analysis-groups/get-aggregated-feature-importance.md) and [Features API](../../api/beam/get-feature-importance.md) by introducing specific event features to your models. See [this notebook](https://docs.predicthq.com/getting-started/guides/beam-guides/forecast-ready-features-at-scale) for an example of how to get features for all your stores or locations.
2. **Informed marketing strategies**:
   * Run targeted campaigns to capitalize on events occurring near your stores or locations, taking advantage of the buzz around events.
   * Run off-season promotions during quiet periods to stimulate demand and maintain customer engagement.
3. **Partnerships and sponsorships**:
   * Collaborate with event organizers or related businesses for cross-promotional opportunities.
4. **Tailored product offerings**:
   * Develop and offer products or services that align with the interests and needs of customers attending these events.

### Considerations and Watchouts <a href="#considerations-and-watchouts" id="considerations-and-watchouts"></a>

1. **Impact of demand share**: The aggregation of Category Importance assigns weight to analyses based on their average daily demand, naturally giving more weight to those with a higher demand. This approach is designed to reflect the real-world impact of each analysis. If more balanced results are desired, consider grouping analyses with comparable levels of demand to prevent any single analysis dominating the overall results.&#x20;
2. **Integration with Features API**: The [Beam API](../../api/beam/analysis-groups/get-aggregated-feature-importance.md) provides a list of features for each important category, which can be incorporated into your models via the [Features API](../../api/features/get-features.md). Ideally, these features should be tailored to the store or location of interest but using group-level features is a viable alternative if store or location-level modeling is impractical. However, this may lead to some stores or locations having features that are entirely zeros, which is something to consider and take into account.
