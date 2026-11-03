# Analyses

A Beam Analysis correlates one location's historical demand with real-world events. The lifecycle has three steps:

1. For a Saved Location, [create an Analysis](create-an-analysis.md).
2. [Upload demand data](upload-demand-data.md).
3. Retrieve [Feature Importance](get-feature-importance.md), the results that scope Features API and Events API calls via the `analysis_id`.

Run one Analysis per location. Refresh monthly by [uploading new demand data](upload-demand-data.md) and [refreshing](refresh-an-analysis.md) - don't delete and recreate, or you lose accumulated correlation history.
