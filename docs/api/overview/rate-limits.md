# Rate Limits

Your requests to the API will be rate limited, based on the limit specified in your plan. Rate limits are specified in `rps` (requests per second) and your request rate is measured across a one second window.

E.g. a rate limit of 50 rps means you can make 50 requests in a second.

The rate limit applies to your entire Organization as a whole, regardless of IP, Access Token or API Client. If you exceed your rate limit, requests may be rejected with the `429 Too Many Requests` response code until the rate limit resets at the start of the next minute window.

{% hint style="info" %}
From time-to-time we may introduce additional rate limits to ensure the reliability of our service is maintained.
{% endhint %}

Please ensure you are using appropriate retries and exponential backoff's to work within the rate limits. Please see the following page with advice on retrying failed requests.

* [#retrying-failed-requests](troubleshooting.md#retrying-failed-requests "mention")
