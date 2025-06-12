---
description: >-
  The official PredictHQ JavaScript Client provides a consistent JavaScript
  interface to our API.
---

# Javascript SDK

<table data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>NPM</strong></td><td></td><td></td><td><a href="https://www.npmjs.com/package/predicthq">https://www.npmjs.com/package/predicthq</a></td></tr><tr><td><strong>GitHub</strong></td><td></td><td></td><td><a href="https://github.com/predicthq/sdk-js">https://github.com/predicthq/sdk-js</a></td></tr></tbody></table>

## Example

### Installation

```bash
npm install predicthq
```

### Setup the SDK

```javascript
import Client from 'predicthq'

// Initialises PredictHQ client library using your access token
// Note: You can find/create your access token at https://control.predicthq.com/clients
const client = new Client({access_token: 'ACCESS_TOKEN'})
```

### Search Events

Perform a basic search of events using the `title` parameter.

```javascript
client.events.search({title: 'Aviation Festival'})
    .then(
        (results) => {
            for (const event of results) {
                console.info(event);
            }
        }
    ).catch(
        err => console.error(err)
    )
```

## Further Examples

Please browse through our [use case examples](https://github.com/predicthq/sdk-js/tree/master/usecases) on our GitHub repository.

## Found an Issue?

Please [log an issue](https://github.com/predicthq/sdk-js/issues/new) on our GitHub repository.
