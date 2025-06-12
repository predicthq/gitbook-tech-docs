# Pagination

When requesting a list of records, the response will usually contain the following fields:

<table><thead><tr><th width="190">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>count</strong></td><td>The total number of results.</td></tr><tr><td><strong>previous</strong></td><td>A URL to the previous page, or <code>null</code> if this is the first page.</td></tr><tr><td><strong>next</strong></td><td>A URL to the next page, or <code>null</code> if this is the last page.</td></tr><tr><td><strong>overflow</strong></td><td>Boolean flag that indicates if the search has more results than your subscription allows you to view.</td></tr></tbody></table>

Below is an example response:

```json
{
  "count": 189,
  "overflow": false,
  "previous": null,
  "next": "https://api.predicthq.com/v1/endpoint/?offset=10&limit=10",
  "results": [
    {
        // record 1
    },
    {
        // record 2
    }

    // more records

  ]
}
```

Individual API Endpoint documentation will describe specific response formats.

You can control the result records that are returned using the standard `offset` and `limit` query string parameters. If no limit is specified, then a default of `10` applies.

The maximum number of results and pagination limits are specified in [your plan](https://control.predicthq.com/settings/plans). If you require higher limits please [contact us](https://www.predicthq.com/contact) to discuss your needs.

## Maximum Number of Results

When the number of results exceeds the maximum number of records allowed by your subscription the `overflow` field will be set to `true`. This indicates there are more results available but you are unable to paginate to them.

You can work around this limitation by performing more specific searches resulting in fewer results.
