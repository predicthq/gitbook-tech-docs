---
description: Get Feature Importance data for an Analysis Group.
---

# Get Aggregated Feature Importance

This endpoint provides Feature Importance results aggregated across the Analyses in an existing Analysis Group, and returns a list of feature groups with associated Features API features and group p-values.

## Request

### HTTP Request

```http
GET https://api.predicthq.com/v1/beam/analysis-groups/$group_id/feature-importance
```

### Path Parameters

<table><thead><tr><th width="211">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>group_id</code></td><td>An existing Beam Analysis Group ID.</td></tr></tbody></table>

## Response

### Response Fields

<table><thead><tr><th width="250">Field</th><th>Description</th></tr></thead><tbody><tr><td><code>feature_importance</code><br>array</td><td>List of Feature Importance groups. The structure of the response matches that of an individual Analysis.<br><br>Please refer to the <a href="../get-feature-importance.md#feature-importance-response-fields">Feature Importance Response Fields</a> section for the structure of each record.</td></tr></tbody></table>

<details>

<summary>Example response</summary>

Below is an example response:

```json
{
    "feature_importance": [
        {
            "feature_group": "school-holidays",
            "features": [
                "phq_rank_school_holidays"
            ],
            "p_value": 0.0236,
            "important": true
        },
        {
            "feature_group": "observances",
            "features": [
                "phq_rank_observances"
            ],
            "p_value": 0.0313,
            "important": true
        },
        {
            "feature_group": "conferences",
            "features": [
                "phq_attendance_conferences"
            ],
            "p_value": 0.0532,
            "important": true
        },
        {
            "feature_group": "community",
            "features": [
                "phq_attendance_community"
            ],
            "p_value": 0.0717,
            "important": true
        },
        {
            "feature_group": "performing-arts",
            "features": [
                "phq_attendance_performing_arts"
            ],
            "p_value": 0.2541,
            "important": false
        },
        {
            "feature_group": "concerts",
            "features": [
                "phq_attendance_concerts"
            ],
            "p_value": 0.3528,
            "important": false
        },
        {
            "feature_group": "academic",
            "features": [
                "phq_rank_academic_exam",
                "phq_rank_academic_holiday"
            ],
            "p_value": 0.6479,
            "important": false
        },
        {
            "feature_group": "expos",
            "features": [
                "phq_attendance_expos"
            ],
            "p_value": 0.7802,
            "important": false
        },
        {
            "feature_group": "festivals",
            "features": [
                "phq_attendance_festivals"
            ],
            "p_value": 0.9684,
            "important": false
        },
        {
            "feature_group": "public-holidays",
            "features": [
                "phq_rank_public_holidays"
            ],
            "p_value": 0.9975,
            "important": false
        },
        {
            "feature_group": "sports",
            "features": [
                "phq_attendance_sports"
            ],
            "p_value": 0.9999,
            "important": false
        }
    ]
}
```

</details>

## Examples

{% tabs %}
{% tab title="curl" %}
```bash
curl -X GET "https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID/feature-importance" \
     -H "Accept: application/json" \
     -H "Authorization: Bearer $ACCESS_TOKEN"
```
{% endtab %}

{% tab title="python" %}
```python
import requests

response = requests.get(
    url="https://api.predicthq.com/v1/beam/analysis-groups/$GROUP_ID/feature-importance",
    headers={
      "Authorization": "Bearer $ACCESS_TOKEN",
      "Accept": "application/json"
    }
)

print(response.json())
```
{% endtab %}
{% endtabs %}
