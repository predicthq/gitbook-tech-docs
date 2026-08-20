# Analyses

A Beam Analysis correlates one location's historical demand with real-world events. The lifecycle: [create an analysis](create-an-analysis.md) against a Saved Location, [upload demand data](upload-demand-data.md), then retrieve [Feature Importance](get-feature-importance.md) - the results that scope Features API and Events API calls via the `analysis_id`.

Run one analysis per location. Refresh monthly by [uploading new demand data](upload-demand-data.md) and [refreshing](refresh-an-analysis.md) - don't delete and recreate, or you lose accumulated correlation history.
