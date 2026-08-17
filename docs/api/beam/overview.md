# Overview

Beam is PredictHQ's relevancy engine.

It determines which types of real-world events are materially relevant to your business by analyzing your historical demand data - per location. Event impact varies by geography, industry, and demand profile, so Beam quantifies which event signals consistently explain changes in your demand - and your models train on signal instead of noise.

The primary output is a set of [Feature Importance](analyses/get-feature-importance.md) results and an `analysis_id`. Pass the `analysis_id` to the [Features API](../features/get-features.md) and [Events API](../events/search-events.md) to apply demand-calibrated filtering automatically - the relevant event categories, rank thresholds, and location scope, with no manual configuration. Without Beam, feature selection is a manual guess.

Run one analysis per location and refresh it monthly by appending new demand data. For many locations sharing a single model, use [Analysis Groups](analysis-groups/get-an-analysis-group.md) to aggregate Feature Importance into one consistent feature set.

## Guides

* [What is Beam?](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/core-concepts/what-is-beam)
* [Beam guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/beam-guides)
