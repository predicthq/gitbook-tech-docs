# Rate Limits

Your requests to the API will be rate limited, based on the limit specified in your plan. Rate limits are specified in `rpm` (requests per minute) and your request rate is measured across a one minute window.

E.g. a rate limit of 1k rpm means you can make 1,000 requests in a minute.

The rate limit applies to your entire Organization as a whole, regardless of IP, Access Token or API Client. If you exceed your rate limit, requests may be rejected with the `429 Too Many Requests` response code until the rate limit resets at the start of the next minute window.

{% hint style="info" %}
From time-to-time we may introduce additional, temporary rate limits to ensure the reliability of our service is maintained.
{% endhint %}

Please ensure you are using appropriate retries and exponential backoff's to work within the rate limits.
