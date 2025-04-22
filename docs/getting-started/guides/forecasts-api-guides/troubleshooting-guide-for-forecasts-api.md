# Troubleshooting Guide for Forecasts API

## Forecast Accuracy Issues

If you’re experiencing lower-than-expected forecast accuracy, there are a few common issues worth checking. Forecasting models rely on consistent, pattern-rich historical data to make reliable predictions. The more signal and structure in your input data, the better the output.

### Not Enough History

Forecast models rely on repeated patterns in your data—seasonality, trends, and demand shifts over time. Without enough historical coverage, the model may struggle to detect these patterns or overfit to short-term fluctuations. We recommend providing at least 18 months of demand history.

What to try:

* Include at least 18 months of historical demand to capture seasonality and other patterns.
* Aggregate similar items, regions, or stores if individual series are sparse or noisy.
* Focus on stable patterns: if your business underwent recent changes, exclude outdated data that no longer reflects reality.
* Ensure consistent time intervals: avoid gaps or overlapping dates in your time series.

### Weak or Unstable Signal

Even if your demand data passes basic data quality checks, forecast quality still depends on the strength and consistency of the demand signal. Flat lines, irregular spikes, or inconsistent patterns can make it harder for the model to detect meaningful trends.

What to try:

* Aggregate similar products to boost volume and pattern strength.
* Exclude outliers that don’t represent normal demand behavior (e.g. one-off promotional spikes).
* Avoid artificial smoothing or flooring (e.g. replacing all zero values with 1), which can distort the signal.
* Focus on series that show some recurring variation—the model performs best when it can detect trends and seasonality.

### Early COVID-19 Disruption

The early months of the COVID-19 pandemic (typically March–June 2020 or longer for many businesses) created extreme, non-recurring shifts in demand across nearly all industries. These sudden drops or surges were driven by lockdowns, panic buying, or closures—none of which represent repeatable patterns the model can learn from.

Including this period in your training data may reduce accuracy, especially if your business has since stabilized or operates differently now.

What to try:

* Exclude the early COVID-19 period (e.g. March–June 2020 or longer) if it doesn’t reflect current conditions.
* Review data around major lockdowns or policy changes, even after 2020, and assess whether it’s relevant to keep.
* If your business fundamentally changed (e.g. moved online, altered operating hours), consider using only post-change data for training.

### Forecasting Too Fine-Grained

Forecasting works best when the signal in your data is stronger than the noise. Extremely granular forecasts—like low-volume SKUs or store-level daily data—can result in high error rates because there’s not enough volume or structure to model accurately.

What to try:

* Aggregate similar products or channels to build a stronger, more consistent demand signal.
* Filter out extremely low-volume series where demand is often zero or close to zero.
* Avoid over-segmenting—forecasting too narrowly (e.g. SKU) may not be practical without enough volume.

### Misaligned Seasonality

Some demand patterns repeat consistently each year—others don’t. If your data doesn’t include multiple seasonal cycles, or if the timing of spikes shifts from year to year, the model may struggle to generalize.

What to try:

* Provide multiple full seasonal cycles (e.g. two Christmas periods, two summer holidays).
* Avoid including only recent post-launch data unless the product is truly new.
* Use longer history to help the model identify what demand shifts are predictable vs. one-offs.

### Shifting Business Patterns

If your business has changed significantly—new pricing models, operational changes, store closures—the model may underperform if older demand no longer reflects current behavior.

What to try:

* Trim outdated data that no longer reflects how your business operates.
* Model each distinct version of the business separately, if feasible (e.g., pre/post relaunch).
* Note recent changes when reviewing forecasts; short-term fluctuations may smooth out over time.

### Misunderstanding Accuracy Metrics

Metrics like MAPE, MAE, and RMSE can tell different stories depending on your demand volume, volatility, and business goals. Don’t rely on a single metric in isolation.

What to try:

* Use MAE for a straightforward measure of average error in units.
* Use MAPE when your demand values aren’t near zero—it shows relative error in percentage terms.
* Use RMSE if large deviations are especially costly in your business.
* Compare forecasts visually as well—some patterns look worse in numbers than they are in practice.
