# Troubleshooting

The PredictHQ API uses conventional HTTP status codes to indicate the success or failure of an API request. If you receive an error, this is what it means:

<table><thead><tr><th width="293">HTTP Status Code</th><th>Description</th></tr></thead><tbody><tr><td><strong>Bad Request</strong><br>400</td><td>The request contains invalid parameters, or invalid or incomplete data.</td></tr><tr><td><strong>Unauthorized</strong><br>401</td><td>You failed to provide a valid <code>Authorization</code> header, or your credentials are invalid or expired.</td></tr><tr><td><strong>Payment Required</strong><br>402</td><td>Your subscription has expired.</td></tr><tr><td><strong>Forbidden</strong><br>403</td><td>You tried to perform an action that is not authorized. E.g. you failed to request the required scope.</td></tr><tr><td><strong>Not Found</strong><br>404</td><td>The resource or endpoint does not exist. Please ensure the URL is correct. Note that you may need to add a trailing slash to the URL path.</td></tr><tr><td><strong>Too Many Requests</strong><br>429</td><td>You have reached your subscription (or global) rate limit. Please implement exponential backoffs and retries and take care not to send too many requests in a short period of time.</td></tr><tr><td><strong>Service Unavailable</strong><br>503</td><td>The API has been switched to maintenance mode for a major or complex release.</td></tr></tbody></table>

## Retrying Failed Requests

As with any API exposed over the public Internet, some requests may fail and they should simply be retried automatically. We recommend that you implement a solution that automatically retries any `5xx` errors _3_ times with an exponentially increasing delay.

For example: On receiving a `5xx` response immediately retry, if you receive a subsequent `5xx` response wait _1_ second and retry, if you receive a further `5xx` response wait _5_ seconds and retry, if you still receive a 5xx response fail the request and handle it accordingly.
