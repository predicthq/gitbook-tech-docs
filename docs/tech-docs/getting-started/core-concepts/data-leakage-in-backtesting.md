# Data Leakage in Backtesting: Why It Doesn't Affect Forecast Accuracy

Real-world events change. A concert gets postponed, a festival is cancelled, a venue changes, an attendance estimate gets refined as an event gets closer. Because PredictHQ continuously enriches event records with the latest available information, some customers evaluating PredictHQ ask a reasonable question: **if the event data underlying a feature can change over time, does that mean historical training data contains information that wouldn't have been available at the time, and would that make backtesting results overstate what we'll see in production?**

This is often described as a "data leakage" concern. This page explains what's actually happening, why it's not the leakage it first appears to be for the vast majority of forecasting use cases, and the evidence behind that conclusion.

## The concern, in more detail

Sophisticated forecasting teams building their own models on top of PredictHQ features typically want one guarantee above all: that a feature value pulled today for a historical date reflects only what would have been knowable *at the forecast point*, with no information from after that point mixed in.

The worry usually comes from two observations:

* **Event records are updated over time.** PredictHQ refines predicted attendance, tracks cancellations and postponements, and corrects details as an event approaches or passes.
* **Pulling the same historical feature twice, months apart, can return a different value**, because the underlying event data has been updated in the meantime.

If those updates were bleeding *future* information into a *past* forecast point, that would be true data leakage, and it would make backtest accuracy an unreliable stand-in for production accuracy. It's a fair thing to check.

## Point-in-time features vs. true leakage

There's an important distinction between two kinds of change:

* **Changes that happen before your forecast horizon starts.** If you're forecasting 5 weeks out, and an event's predicted attendance is refined 4 months before the event, both your backtest and your production run would have seen a similarly mature version of that data at the point you actually generate the forecast. This isn't leakage — it's just PredictHQ's data getting more accurate over time, the same way it would in production.
* **Changes that would only be known *after* your forecast point.** This is the scenario that would matter: if a feature used to build a training example for a 5-week-out forecast only became available 2 weeks before the event, that's information your production model would never have had at decision time.

Because most events enter PredictHQ's system well ahead of when they happen — commonly 3-6 months out, and often longer — the updates that follow (postponements, cancellations, attendance refinements, venue changes) are, in practice, absorbed well before most customers' forecast horizons begin. The dynamic nature of real-world events is expected and continuous; the question that actually matters is whether that continuous refinement changes the forecast accuracy customers experience, at the horizon they actually operate on.

That's an empirical question, and we set out to answer it directly rather than argue it in the abstract.

## What we measured

We ran an internal study — Backtesting Resiliency — that tracked feature values for the same locations and dates across many weekly snapshots over time, and used those snapshots to compare forecast accuracy computed from "if we'd forecast at this horizon" feature values against the accuracy computed from today's fully up-to-date values. The analysis covered several hundred locations across the US, UK, and Canada, using daily Absolute Percentage Error (APE) as the accuracy measure.

The result: forecast accuracy is stable across horizons.

| Horizon before event | Typical (median) accuracy shift | Tail (80th percentile) accuracy shift |
| --- | --- | --- |
| 6 weeks or less | 0 percentage points | 0 percentage points |
| 7-8 weeks | 0 percentage points | ~0.1-0.3 percentage points |
| 9-10 weeks | 0 percentage points | ~0.5-0.6 percentage points |

In other words: at six weeks out or closer, the accuracy you'd measure in a backtest is effectively identical to what today's fully-refined data would show — for the majority of locations, there's no measurable difference at all. A small tail difference only starts to appear beyond seven weeks out, and even then it's modest.

Since the large majority of demand forecasting use cases we see run on horizons of six weeks or less, this means **backtesting results are a reliable guide to production performance for the overwhelming majority of PredictHQ customers.**

## Why individual event updates don't move the needle

It can still feel counterintuitive that individual events change constantly, yet aggregate forecast accuracy barely moves. The reason comes down to aggregation.

Forecasting models don't consume individual event records directly — they consume features that aggregate many events together for a given location, day, and category (for example, total predicted attendance across all concerts, sports, and festivals happening near a store on a given day). A single event being postponed, cancelled, or having its attendance estimate revised is a small perturbation to one input among many contributing to that aggregate. It rarely shifts the aggregate feature enough to change the resulting forecast in any meaningful way.

Individual event-level details are genuinely dynamic — that's simply what real-world context looks like. What our results show is that this dynamism, once rolled up into the aggregated features models actually use, doesn't translate into meaningful forecast accuracy drift within the horizons that matter for real forecasting decisions.

## What this means in practice

* **For forecast horizons up to ~6 weeks** (the majority of demand forecasting use cases): treat backtesting results as a direct, reliable proxy for the accuracy you'll see in production. No special handling of point-in-time snapshots is required.
* **For longer horizons (7+ weeks out):** the effect is still small, but if you're building a model with a longer lead time and want to validate this for your specific use case, talk to your PredictHQ contact — we can help design a backtest that reflects your exact horizon.
* **You don't need to maintain your own historical snapshot of PredictHQ data** purely to guard against this concern. The dynamic updates you'd be trying to protect against are the same updates that make the data more accurate, and they happen well ahead of the point where they'd affect a typical forecast.

## Frequently asked questions

**Does PredictHQ backtesting reflect what I'll see in production?**
Yes, for forecast horizons up to around six weeks — which covers most demand forecasting use cases — our internal analysis found no measurable difference between backtested and production-time accuracy.

**If PredictHQ updates event data after an event happens (e.g. actual attendance), doesn't that leak into my historical training data?**
Post-event updates refine PredictHQ's records for future accuracy, but they don't change the features that were available at your forecast point for that event. The relevant question is whether a feature value changed *within* your forecast horizon, not whether it was later updated after the event occurred — and our results show that within typical horizons, the two produce effectively the same forecast accuracy.

**Should I snapshot PredictHQ data myself to be safe?**
It isn't necessary for the vast majority of use cases. If you have a use case with a long forecast horizon or unusually strict point-in-time requirements, reach out to your PredictHQ contact to discuss options.
