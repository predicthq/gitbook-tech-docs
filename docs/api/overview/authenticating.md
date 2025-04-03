# Authenticating

All PredictHQ API endpoints require authentication. You can authenticate your request by sending a token in the `Authorization` header of your request. If you try to use an API endpoint without a token or that token has insufficient permissions, you will receive a `403 Forbidden` response.

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/events/" \
     -H "Authorization: Bearer $ACCESS_TOKEN" 
```
{% endtab %}

{% tab title="python" %}
```python
import requests

access_token = "ACCESS_TOKEN"

response = requests.get(
    url="https://api.predicthq.com/v1/events/",
    headers={
      "Authorization": f"Bearer {access_token}"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}

## Create an API Token

Read a more in-depth guide to [creating a new API Token](https://www.predicthq.com/support/how-to-create-an-api-token) or follow the basic steps below:

1. Log into the WebApp and visit the [API Tokens](https://control.predicthq.com/tokens) page under API tools.
2. The first time you create a token - enter the name of the token and click "Create Token". For the second and subsequent times click the "Create New Token" button and enter the name, then click Create Token.
3. Click "Copy Token" to copy your token to the clipboard. You can now paste the token into another application. Keep a copy of your new API Token, as it will not be shown again.

Now you can use the new API Token in the `Authorization` header of your API requests.
