# Rate Limits

Your requests to the API will be rate limited, based on the limit specified in your plan. Rate limits are specified in `rps` (requests per second) and your request rate is measured across a one second window.

E.g. a rate limit of 50 rps means you can make 50 requests in a second.

The rate limit applies to your entire Organization as a whole, regardless of IP address or API Token. If you exceed your rate limit, requests may be rejected with the `429 Too Many Requests` response code until the rate limit resets at the start of the next window.

{% hint style="info" %}
From time-to-time we may introduce additional temporary rate limits to ensure the reliability of our service is maintained.
{% endhint %}

### Concurrent Requests

Your rate limit controls how many requests per second your organisation can make, but it does not limit how many of those requests can be in-flight simultaneously. Sending a large number of concurrent requests — even within your rps limit — can cause bursts that exceed your limit, result in `429` errors, and put unnecessary pressure on the API.

We recommend limiting the number of concurrent requests your application makes at any one time. A good rule of thumb is to keep concurrent requests well below your rps limit, and to prefer sequential or lightly-concurrent patterns when fetching data in bulk.

If you are building a system that needs to make many requests (for example, fetching data across a large number of locations or date ranges), consider:

* Using a queue or worker pool with a fixed concurrency limit rather than parallelising all requests at once
* Adding a small delay between requests if you are iterating sequentially
* Implementing retry logic with exponential backoff to handle any `429` responses gracefully

See Retrying Failed Requests for guidance on backoff and retry behaviour.

### Retrying Failed Requests

Please ensure you are using appropriate retries and exponential backoff's to work within the rate limits. Please see the following page with advice on retrying failed requests.

* [#retrying-failed-requests](troubleshooting.md#retrying-failed-requests "mention")
