# Understanding Forecast Accuracy Metrics

The Forecasts API provides three common metrics to help you evaluate how well the model is performing. Each metric highlights a different aspect of error—use them together to get a complete picture.

## MAPE – Mean Absolute Percentage Error

MAPE quantifies the average magnitude of forecast error as a percentage of actual values. It’s easy to interpret and especially useful for comparing forecast performance across products, locations, or scales. However, it can become distorted when actual values are close to zero.

{% hint style="info" %}
In plain English – MAPE shows how far off your forecasts are, on average, as a percentage. It’s great for comparing performance across different types of demand—but it may overstate errors when actual demand values are very low.
{% endhint %}

* Best used when actual values are consistently non-zero.
* Good for comparing forecasts across series with different scales.
* Can produce very large values when actual demand is low, even if the forecast is reasonable.

In our expanding window evaluation framework, the MAPE is calculated not just from a single forecast, but across multiple rolling forecast iterations—this simulates how the model would perform in a real-world setting where forecasts are generated repeatedly over time, and ensures the reported accuracy reflects consistent performance, not just a one-off result.

## WAPE – Weighted Absolute Percentage Error

WAPE quantifies the total forecast error as a percentage of the total actual demand. Unlike MAPE, which gives equal weight to each data point, WAPE weights each error by the size of the actual value. This makes it less sensitive to very small actual values, so it's a more reliable measure of accuracy in some situations.

{% hint style="info" %}
In plain English – WAPE shows the share of your total demand that was mis-forecast, with bigger-demand periods counting more. It gives a more balanced view than MAPE when actual values vary a lot or include small numbers that could distort results. WAPE is a good way to measure forecasting accuracy for businesses with regular low-demand or off-peak periods.
{% endhint %}

* Defined even when some actual values are zero (unlike MAPE, which is undefined in those cases).
* Weights errors by demand size, reducing distortion from very small actual values.
* Best used with stationary series; results may be misleading when demand has strong trends, seasonality, or shifting volatility.

## MAE – Mean Absolute Error

MAE measures the average absolute difference between predicted and actual values, expressed in the same units as your demand (e.g. units sold, bookings). It treats all errors equally, making it a simple and intuitive way to understand overall forecast accuracy.

{% hint style="info" %}
In plain English – MAE tells you how far off your forecast is on average, using the same units you care about—like “bookings” or “items sold”. Every mistake counts the same, so it gives a clear sense of typical error.
{% endhint %}

* Easy to interpret and compare against your typical daily volumes.
* Treats all errors the same—no extra weight on large deviations.
* Best used when actual values are on a consistent scale across time or series.

## RMSE – Root Mean Squared Error

RMSE measures the square root of the average squared differences between predicted and actual values, placing greater weight on larger errors.

{% hint style="info" %}
In plain English – RMSE tells you how far off your forecasts are on average, but it especially highlights big mistakes—so if you care about avoiding large misses, RMSE is useful.
{% endhint %}

* Penalizes larger errors more than MAE does.
* Helpful for identifying volatility or occasional large misses.
* Useful when high-impact outliers matter more than average performance.

