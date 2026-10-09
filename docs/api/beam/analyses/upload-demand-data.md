---
description: Upload your demand data as CSV, line-delimited JSON, or JSON.
---

# Upload demand data

{% openapi-operation spec="beam-api" path="/v1/beam/analyses/{analysis_id}/sink" method="post" %}
[OpenAPI beam-api](https://raw.githubusercontent.com/predicthq/api-specs/refs/heads/main/openapi/beam-api.yaml)
{% endopenapi-operation %}

## Error codes

The API can return an unsuccessful HTTP response code for several reasons. In addition to an error message, there may also be a `code` field when applicable. The following table outlines the meaning of several error codes that may be returned.

| Code                                        | Description                                                                                                                                    |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `content_type_invalid`                      | The `Content-Type` header is unsupported.                                                                                                      |
| `data_validation_failed`                    | The format of the data uploaded is incorrect.                                                                                                  |
| `json_no_data`                              | An empty JSON body was uploaded.                                                                                                               |
| `json_invalid_format`                       | The uploaded JSON is formatted incorrectly. Ensure JSON data is correctly UTF-8 encoded and that there are no invalid escape sequences. |
| `ndjson_no_data`                            | An empty NDJSON body was uploaded.                                                                                                             |
| `ndjson_invalid_format`                     | The NDJSON body is formatted incorrectly. Ensure NDJSON data is correctly UTF-8 encoded and that there are no invalid escape sequences. |
| `csv_invalid_row`                           | The uploaded CSV has an invalid row.                                                                                                           |
| `csv_invalid_header`                        | The uploaded CSV headers are incorrect. Use `date,demand`.                                                                              |
| `csv_no_data`                               | The uploaded CSV is empty or only has headers set.                                                                                             |
| `csv_invalid_format`                        | The uploaded CSV is formatted incorrectly. Ensure CSV data is correctly UTF-8 encoded and that there are no invalid escape sequences.   |
| `start_date_invalid`                        | The earliest date in the uploaded demand data is before `2017-01-01`.                                                                          |
| `end_date_invalid`                          | The latest date in the uploaded demand data is more than one year into the future.                                                               |
| `duplicate_rows`                            | The uploaded demand data contains duplicate dates. Remove all duplicates before uploading.                                              |
| `no_data`                                   | There is no demand data.                                                                                                                       |
| `weekly_demand_date_check_failed`           | The weekly demand dates do not start on the same weekday.                                                                                      |
| `below_minimum_threshold`                   | There are not enough data points in the uploaded demand data.                                                                                  |
| `constant_demand_column`                    | The demand column is constant.                                                                                                                 |
| `exceeding_missing_data_percentage`         | There are too many missing demand values.                                                                                                      |
| `exceeding_consecutive_missing_data_volume` | There are too many consecutive missing demand values.                                                                                          |
| `high_variance_difference_rate`             | The variance of the uploaded demand data is too large to be processed.                                                                         |
| `unexpected_error`                          | An unexpected error occurred.                                                                                                                  |

## Examples

Upload a CSV file with either example:

{% tabs %}
{% tab title="curl" %}
```bash
curl -X POST "https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/sink" \
     -H "Content-Type: text/csv" \
     -H "Authorization: Bearer $API_TOKEN" \
     --data @data.csv
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.post(
    url="https://api.predicthq.com/v1/beam/analyses/$ANALYSIS_ID/sink",
    headers={
        "Authorization": "Bearer $API_TOKEN",
        "Content-Type": "text/csv"
    },
    data=open("data.csv")
)

print(response.status_code)
```
{% endtab %}
{% endtabs %}

## OpenAPI spec

See the [Beam API OpenAPI spec](https://api.predicthq.com/docs/?urls.primaryName=Beam+API).

## Guides

Here are some guides relevant to this API:

* [Beam guides](https://app.gitbook.com/s/tNhzHETmXsrWeVBndqqJ/getting-started/guides/beam-guides)
