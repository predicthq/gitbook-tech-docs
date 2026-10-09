---
description: >-
  Predicted Attendance represents the number of people predicted to attend an
  event.
---

# Predicted Attendance

This value represents the number of people predicted to attend an event. The [Events API response](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events) returns the exact Predicted Attendance number as the `phq_attendance` value for attendance-based events.&#x20;

PHQ Rank also has a value between 0 and 100 that represents how many people will attend an event. For example, an event with a PHQ Rank 50 has around 1,000 attendance.&#x20;

PHQ Rank, Local Rank, and Predicted Attendance use the following table to translate the numeric value to rank level and tier.

<table><thead><tr><th width="215">PHQ Rank Level</th><th width="213">PHQ Rank Range</th><th>Expected Attendance</th></tr></thead><tbody><tr><td>1 - Minor</td><td>0 - 10<br>11 - 20</td><td>~10<br>~30</td></tr><tr><td>2 - Moderate</td><td>21 - 30<br>31 - 40</td><td>~100<br>~300</td></tr><tr><td>3 - Important</td><td>41 - 50<br>51 - 60</td><td>~1,000<br>~3,000</td></tr><tr><td>4 - Significant</td><td>61 - 70<br>71 - 80</td><td>~10,000<br>~30,000</td></tr><tr><td>5 - Major</td><td>81 - 90<br>91 - 100</td><td>~100,000<br>~300,000+</td></tr></tbody></table>

These mappings are sometimes referred to as ranking bands.

## How PredictHQ calculates Predicted Attendance

PredictHQ calculates Predicted Attendance via machine learning models (ML models) and expert systems in our pipeline. We train our ML models on historical data, and they predict the number of people that are predicted to attend a future event before they happen. Our models use a large number of inputs (called machine learning features) to make an accurate prediction.

PredictHQ monitors the accuracy of their models and periodically retrains them to ensure we retain high-accuracy predictions.

### Examples of models used for Predicted Attendance

We have ML models to predict attendance for all our attended categories. Some types of events within some categories may use expert systems instead of machine learning models. For example, although most of our main sports within the sports category use ML models, Formula 1 race events do not use an ML model.

ML models use machine learning features as inputs to predict attendance. These features are different pieces of data that allow the model to make an accurate prediction based on different factors. For example, the sports teams playing, the type of sport, and the venue a sports game is played all affect the Predicted Attendance. If two very popular sports teams play at a large stadium then they are more likely to have more people attending the game.

The following sections give examples of ML models and the factors they use to predict attendance.

#### Sports model - features used

The sports model uses these ML features to predict how many people will attend a sporting event:

* Teams
* Venue
* Sport
* Duration
* Weekday/Weekend
* Gender
* Recurring Event
* International/Domestic
* Tournament
* And more

#### Concerts model - features used

The concerts model uses these ML features to predict how many people will attend a concert event:

* Music genre
* Record label
* Population density
* Venue capacity
* Performer data
* Ticket sales
* And more

#### Performing arts model - features used

The performing arts model uses these ML features to predict how many people will attend a performing-arts event:

* Type of event
* Venue capacity
* Ticket sales
* Duration
* Start time
* Number of performers
* Population density
* And more

**Conferences model - features used**&#x20;

The conferences model uses these ML features to predict how many people will attend a conference event:

* Event density
* Venue capacity
* Location&#x20;
* Duration
* Start time
* Population density
* And more

### Expert systems and other types of models

We also have other specialist models for some types of events. For example, we have a specific model that predicts attendance for Youth Sports that uses features like age groups, student numbers, the number of teams in a tournament, and more to make specific attendance predictions for Youth Sports events.

Where we don’t have models we use the following data to predict attendance:

* Venue capacity
* Maximum Attendance
* Recurring event group attendance
* Provider future attendance
* Provider-specific ranking methods

We also update sports events with actual attendance after they happen (mainly major US sports and major soccer leagues)

