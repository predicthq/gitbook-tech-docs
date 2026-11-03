# Ranks

Two scores quantify an event's expected impact, both on a logarithmic 0-100 scale:

* [PHQ Rank](phq-rank.md) - global impact, normalized worldwide. Use it to compare events across locations.
* [Local Rank](local-rank.md) - impact relative to the surrounding population. Use it to find events that matter locally - a 5,000-person event means more in a small town than a big city.

In practice you rarely set rank thresholds by hand: a Beam Analysis calibrates them per location, and passing `beam.analysis_id` to the Events and Features APIs applies them automatically. For manual starting points, see [Recommended Event Categories and Local Rank Thresholds](../../guides/industry-specific-event-filters.md).
