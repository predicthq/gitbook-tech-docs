# Troubleshooting

The PredictHQ API uses conventional HTTP status codes to indicate the success or failure of an API request. If you receive an error, this is what it means:

<table><thead><tr><th width="293">HTTP Status Code</th><th>Description</th></tr></thead><tbody><tr><td><strong>Bad Request</strong><br>400</td><td>The request contains invalid parameters, or invalid or incomplete data.</td></tr><tr><td><strong>Unauthorized</strong><br>401</td><td>You failed to provide a valid <code>Authorization</code> header, or your credentials are invalid or expired.</td></tr><tr><td><strong>Payment Required</strong><br>402</td><td>Your subscription has expired.</td></tr><tr><td><strong>Forbidden</strong><br>403</td><td>You tried to perform an action that is not authorized. E.g. you failed to request the required scope.</td></tr><tr><td><strong>Not Found</strong><br>404</td><td>The resource or endpoint does not exist. Please ensure the URL is correct. Note that you may need to add a trailing slash to the URL path.</td></tr><tr><td><strong>Too Many Requests</strong><br>429</td><td>You have reached your subscription (or global) rate limit. Please implement exponential backoffs and retries and take care not to send too many requests in a short period of time.</td></tr><tr><td><strong>Server Error</strong><br>5xx</td><td>An unexpected error occurred on our end. These errors are transient — retry the request using exponential backoff.</td></tr><tr><td><strong>Service Unavailable</strong><br>503</td><td>The API has been switched to maintenance mode for a major or complex release.</td></tr></tbody></table>

### Retrying Failed Requests

As with any API exposed over the public internet, some requests may fail transiently and should be retried automatically. We recommend implementing exponential backoff with jitter for all `5xx` errors and `429 Too Many Requests` responses.

**Retry up to 3 times** before failing the request and handling it accordingly.

**Backoff schedule (with jitter):**

| Attempt   | Base delay | Jitter        |
| --------- | ---------- | ------------- |
| 1st retry | 1 second   | ±500ms random |
| 2nd retry | 2 seconds  | ±500ms random |
| 3rd retry | 4 seconds  | ±500ms random |

Jitter prevents multiple clients from retrying in lockstep, which can amplify load on the API. A simple approach is to add a random value between 0 and 1000ms to each base delay.

Do not retry `4xx` errors other than `429` — these indicate a problem with the request itself (invalid parameters, authentication failure, insufficient permissions) that retrying will not resolve.
