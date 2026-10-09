---
description: >-
  Loop Links let you submit missing events and provide
  feedback on existing events.
---

# Integrate with Loop Links

[PredictHQ's Loop tool](https://www.predicthq.com/tools/loop) allows customers to submit feedback on existing events and to submit missing events. PredictHQ has global events data from hundreds of providers, but sometimes our data may not include events such as hyperlocal events. Loop allows customers to report events that appear to be missing. It also allows customers to provide feedback on events if they have updates to details like attendance, times, or location.

Using [Loop ](https://loop.predicthq.com/)requires a PredictHQ login to the WebApp, however, some customers want their users to be able to submit event feedback without needing a PredictHQ login. These customers want a way to integrate the ability to report missing events or event feedback into their product.

**Loop Links** provide a way for customers to integrate with Loop without their users needing a WebApp login, and enable the following:

* You can integrate Loop into your products, such as a web app, mobile app, or other tool
* You can generate a unique URL to allow your users to submit event feedback and missing event information
* PredictHQ processes events in the normal way and adds valid events or feedback to its system
* The Events API returns events that PredictHQ approves via Loop

This means you can allow your users to submit feedback on events but your support team doesn't need to spend time managing this feedback. It goes straight to PredictHQ.

To use Loop Links you need to use the API that creates Loop Links. See [**Loop Links Technical Details**](integrate-with-loop-links.md#loop-links-technical-details) below. See also, our [Loop Links API documentation](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/loop) for details on creating Loop Links.

## Overview

Loop Links provide a URL that allows a user to provide event feedback. You create Loop Links URLs via the Loop Links API. You must configure your own URLs before you can integrate Loop Links into your application.

The link does not require authentication. It has customer details embedded. For example:

* **Label**: My First Capture Link
* **Link**: `https://phq.link/loop/jG5KnDpad5SAUMkUtR` (note: this is not a valid link, just an example)

You can link to the URL from within your application, and feedback goes straight into the Loop system.

The advantage is you don't need to build a UI. The UI is responsive and works on desktop, tablet, and mobile.

## Loop Links integration

You integrate two functions in your application:

* One for submitting missing events
* Another for feedback on events - event feedback should be linked to a part of your application that displays an event

These buttons link to the screens shown in the following section.

Below is a fictitious example app with examples of adding buttons for the two types of Loop Feedback

<figure><img src="../../.gitbook/assets/example-app-with-loop-links.png" alt="A fictitious example app with buttons for submitting a missing event and providing event feedback through Loop Links"><figcaption></figcaption></figure>

The following diagram shows how your app integrates with the Loop Links event pages:

<figure><img src="../../.gitbook/assets/loop-links-integrated-example.png" alt="Diagram showing how the buttons in an app link to the Loop Links pages for submitting a missing event and providing event feedback"><figcaption></figcaption></figure>

The heading at the top of the Loop pages defaults to your organization name in the WebApp. You can update it to change it via the API.

**Missing event link**

Opens a PredictHQ web page where users can enter details of a missing event in the browser.

We recommend you open this in a new window.

**Event feedback link**

Opens a PredictHQ web page where users can provide feedback on an existing event. Requires the public event ID of the event.

Integrate this link where you are displaying a PredictHQ event in your app. We recommend you open this in a new window.

### Submitting missing events

When a user submits a missing event:

* Users enter event details
* PredictHQ teams review and approves or reject events
* Approved events show as visible to the customer as active events
* Users receive an email when an event is approved or rejected

<figure><img src="../../.gitbook/assets/loop-submit-missing-event.png" alt=""><figcaption></figcaption></figure>

### Providing Feedback on Events

When a user gives feedback on an event:

* User reviews the event details on the page and can provide feedback
* This requires an event ID to be passed to the Loop Links' URL
* PredictHQ approves or rejects the feedback
* Users receive an email if there are any questions about their feedback

<figure><img src="../../.gitbook/assets/loop-event-feedback.png" alt=""><figcaption></figcaption></figure>

## Loop Links automated emails

The Loop Links platform sends automated emails in the following cases:

* When a submitted event is approved
* When a submitted event is rejected
* When there is a reply or comment on event feedback

The email templates contain the organization at the top of the template. This is the same organization name that is shown at the top of the the Loop Link pages for submitting missing events and event feedback. You can update it by calling `PUT /v1/loop/settings`. See [**Loop Links Technical Details**](integrate-with-loop-links.md#loop-links-technical-details) for more information.

**Note that users cannot reply to these emails. In order to reply to them you need to use the event feedback page for the event in question and send a response in the feedback.**

The following tabs show some example emails:

{% tabs %}
{% tab title="Approved Submission Email" %}
See an example below of the email template for approved events:

<figure><img src="../../.gitbook/assets/approved-event-loop-links-email.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Reply to Submission/Feedback Email" %}
See an example below of the email template for rejected events and replies to event feedback:

<figure><img src="../../.gitbook/assets/reply-event-loop-links-email.png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## Tracking Loop Feedback

Users with admin access can track Loop feedback at [loop.predicthq.com](https://loop.predicthq.com/) :

* Needs a PredictHQ login
* Shows if Loop submissions are approved or rejected
* Shows details of the discussion about the Loop events with responses from PredictHQ
* Allows administrators to track the status of events submitted by their end users

This is typically used by support teams if issues are raised about event feedback and they want to review the feedback.

## Loop Links Technical Details

### Integration overview

1. Create Loop Links using the API:
   1. Store links in your system, or
   2. Use the link immediately.
2. To set the name displayed at the top of the Loop pages, update the **`org_name`** field via the settings API if required
3. In your application, implement the links.
When an end-user clicks a link, the Public Loop UI opens in their browser. No login is needed. The end-user completes the form to submit an event (or feedback, depending on the type of link) and receives an email when the event they submitted is approved or rejected.

### Types of links

#### Submit missing event

To **submit a missing event**, open the Loop Link from your application:

E.g., open the link with /event/ in the URL:

`https://loop.phq.link/event/kt9fJZXpWFGSA5ky1Cunb2` (note: this is not a valid link just an example)

#### Submit event feedback

To **provide feedback on an existing event** - open the /event-feedback/ Loop Link and supply the `event_id` parameter on the URL:

`https://loop.phq.link/event-feedback/kt9fJZXpWFGSA5ky1Cunb2?event_id=BzjFubD5eqvrRA7NSw` (note: this is not a valid link just an example)

Note that the event ID to use is the `id` field from the [Events API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events). Typically feedback is provided when you are displaying an event from the PredictHQ API in your application. Add a feedback link or icon next to the event so users can provide feedback.

#### To pre-fill the user's email address

The Loop forms require a user email address. You can pre-populate the email address by passing it in the query string. The name of the parameter is `email`.

`https://loop.phq.link/event/kt9fJZXpWFGSA5ky1Cunb2?email=example@example.com` (note: this is not a valid link just an example)

### Loop Link expiration and reuse

Loop Links work as follows:

* Loop Links can be reused unless an expiry date time is set
* If an expiry date time is set they can no longer be used after they expire
* If no expiry date time is set they can be reused indefinitely
