# Understanding Forecast Accuracy Metrics

The Forecasts API provides three common metrics to help you evaluate how well the model is performing. Each metric highlights a different aspect of error—use them together to get a complete picture.

## MAPE – Mean Absolute Percentage Error

MAPE measures the average size of the error as a percentage of actual values. It’s easy to interpret and useful when comparing forecast performance across different products, locations, or scales. However, it can become distorted when actual values are close to zero.

* Best used when actual values are consistently non-zero.
* Good for comparing forecasts across series with different scales.
* Can produce very large values when actual demand is low, even if the forecast is reasonable.

## MAE – Mean Absolute Error

MAE shows the average difference between predicted and actual values, in the same units as your input (e.g. units sold, bookings). It treats all errors equally, making it a simple and intuitive measure of overall accuracy.

* Easy to interpret and compare against your typical daily volumes.
* Treats all errors the same—no extra weight on large deviations.
* Best used when actual values are on a consistent scale across time or series.

## RMSE – Root Mean Squared Error

RMSE also measures error in the same units as your input, but gives more weight to large misses by squaring them before averaging. It’s useful when large errors are particularly disruptive.

* Penalizes larger errors more than MAE does.
* Helpful for identifying volatility or occasional large misses.
* Useful when high-impact outliers matter more than average performance.

