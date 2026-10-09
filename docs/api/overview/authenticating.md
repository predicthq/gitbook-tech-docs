# Authenticating

All PredictHQ API endpoints require authentication. You can authenticate your request by sending a token in the `Authorization` header of your request. If you try to use an API endpoint without a token or that token has insufficient permissions, you receive a `403 Forbidden` response.

The PredictHQ API is a RESTful API, and you can access it at the `https://api.predicthq.com` URL. The API exchanges all data in JSON by default. These examples send a token in the `Authorization` header:

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/events/" \
     -H "Authorization: Bearer $API_TOKEN" 
```
{% endtab %}

{% tab title="python" %}
```python
import requests

api_token = "$API_TOKEN"

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": f"Bearer {api_token}"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Create an API token

To create a token:

1. In the WebApp, open the [**API Tokens**](https://control.predicthq.com/tokens) page.
2. Enter a name for the token and click **Create Token**.
3. To copy your token to the clipboard, click **Copy Token**. The WebApp doesn't show the token again, so a password or secrets manager is the safest place to keep a copy.

Now you can use the new API Token in the `Authorization` header of your API requests.
