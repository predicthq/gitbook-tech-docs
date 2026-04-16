# Understanding Demand Variability and Event Contribution in Beam

Not all demand fluctuations are equal. Some are predictable - driven by day-of-week patterns, long-term growth trends, or seasonal cycles. Others are anomalous: unexpected spikes or drops that sit outside those regular patterns. These anomalies are where events have the most impact, and where accurate forecasting is hardest.

Beam is designed to help you understand and act on this anomalous demand. It identifies how much of your demand is anomalous, and then quantifies how much of that anomalous demand is driven by real-world context - things like concerts, sports games, conferences, or public holidays near your location.

## How Beam Identifies Anomalous Demand

Beam analyses your historical demand data and decomposes it into two components:

* **Baseline demand**: The stable, predictable portion of demand. This captures long-term trends, regular seasonal patterns, and recurring cycles - the demand you'd expect even without any unusual external influences.
* **Anomalous demand**: Everything left over after the baseline is removed. This is the variable, irregular portion of demand - the spikes and dips that can't be explained by your regular structured patterns alone. External factors like events, weather, or promotions tend to show up here.

The **demand variability ratio** measures the proportion of your total demand that is anomalous. A higher ratio means more of your demand is being driven by anomalous, external factors - which in turn means there's more opportunity for event intelligence to improve your forecasts.

> Beam's decomposition is optimised for identifying event-driven anomalies and may differ from decompositions produced by other tools such as STL or Prophet.

<table><thead><tr><th width="228.62890625">Demand Variability Ratio</th><th>What it means</th></tr></thead><tbody><tr><td>0–5%</td><td>Most demand follows predictable baseline patterns</td></tr><tr><td>5–10%</td><td>Some variability exists, likely influenced by external factors</td></tr><tr><td>>10%</td><td>Anomalies are a significant driver of demand fluctuations</td></tr></tbody></table>

Beam calculates this separately for **positive anomalies** (demand surges) and **negative anomalies** (demand drops), so you can understand both the upside and downside impact.

## How Events Explain That Variability

Once Beam has identified your anomalous demand, the next step is to determine how much of it can be attributed to events.

Beam measures how much of your anomalous demand can be accounted for by events. This gives you an **event contribution percentage**: the share of your anomalous demand that is explained by events happening near your location.

For example:

> _"Positive demand variability contributes 12.9% to total demand, and events explain 78% of that."_

This means that roughly 12.9% of your total demand sits above your predictable baseline, and of that elevated demand, events account for nearly 80%.

{% hint style="success" %}
Based on analysis of over 300,000 Beam analyses across 59,000+ locations in 171 countries over the last 12 months, PredictHQ's event data explains an average of 61% of positive demand variability - though this varies depending on location, industry, and the types of events near your business.
{% endhint %}

Like the demand variability ratio, this is calculated separately for positive and negative anomalies, so you can see how events drive both demand surges and demand drops.

## Why This Matters for Forecasting

Understanding demand variability and event contribution gives you two practical advantages:

1. **Knowing whether events are relevant to your business.** If events explain a large share of your anomalous demand, incorporating event features into your forecasting model is likely to meaningfully improve accuracy. If the contribution is low, other factors (promotions, weather, etc.) may be more important to focus on.
2. **Knowing which events matter.** Beam's feature importance analysis goes a step further - it identifies which specific event categories (concerts, sports, conferences, public holidays, etc.) are the primary drivers of your demand variability. This lets you prioritise the right signals when building or refining your models.

## Next Steps

* Use the [Beam API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/overview) to run an analysis on your demand data.
* See [Feature Importance in Beam](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/analyses/get-feature-importance) to understand which event categories are driving your demand.
