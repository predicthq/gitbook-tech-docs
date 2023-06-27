# Authenticating

All PredictHQ API endpoints require authentication. You can authenticate your request by sending a token in the `Authorization` header of your request. If you try to use an API endpoint without a token or that token has insufficient permissions, you will receive a `403 Forbidden` response.

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET https://api.predicthq.com/v1/events/ \
     -H "Authorization: Bearer $ACCESS_TOKEN" 
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Create an access token

Read a more in-depth guide to [creating a new API Client and Token](https://www.predicthq.com/support/how-to-create-an-api-token) or follow the basic steps below:

1. Log into Control Center and visit the [API Clients](https://control.predicthq.com/clients) page.
2. Select "New Client" and fill in the required information.
3. Make sure to keep a copy of your new Client Secret as this cannot be shown to you again.
4. Use the new Client Secret to create a new Token.
5. Make sure to keep a copy of your new API Token as this cannot be shown to you again.

Now you can use the new API Token in the `Authorization` header of your API requests.
