# Algorithms

The forecasting algorithms available to Forecasts API models. Most integrations use the default for their industry, but the list lets you see what's available and pin a specific algorithm when you have a reason to.

The Forecasts API has these algorithms:

* `phq-xgboost` supports every industry. It is the default for every industry except `restaurants` and `retail`.
* `phq-cffm` is in beta. It is optimized for the named industries `restaurants` and `retail`, and it accepts only those industries. It is the default for those industries.
