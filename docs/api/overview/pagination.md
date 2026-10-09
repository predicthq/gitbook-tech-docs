# Pagination

When requesting a list of records, the response usually contains the following fields:

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

Individual API Endpoint documentation describes specific response formats.

You can control the result records that are returned using the standard `offset` and `limit` query string parameters. If no limit is specified, then a default of `10` applies.

[Your plan](https://control.predicthq.com/settings/plans) specifies the maximum number of results and pagination limits. If you require higher limits [contact us](https://www.predicthq.com/contact) to discuss your needs.

## Maximum number of results

When the number of results exceeds the maximum number of records allowed by your subscription the API sets the `overflow` field to `true`. This indicates there are more results available but you are unable to paginate to them.

You can work around this limitation by performing more specific searches resulting in fewer results.
