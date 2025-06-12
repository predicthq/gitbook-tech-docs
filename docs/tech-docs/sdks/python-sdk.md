---
description: >-
  The official PredictHQ Python Client provides a consistent, pythonic interface
  to our API.
---

# Python SDK

<table data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>PyPi</strong></td><td>Get the PredictHQ Python SDK on PyPi.</td><td></td><td><a href="https://pypi.org/project/predicthq/">https://pypi.org/project/predicthq/</a></td></tr><tr><td><strong>GitHub</strong></td><td>View the code on GitHub.</td><td></td><td><a href="https://github.com/predicthq/sdk-py">https://github.com/predicthq/sdk-py</a></td></tr></tbody></table>

## Example

### Installation

```bash
pip install predicthq
```

### Setup the SDK

```python
from predicthq import Client

# Initialises PredictHQ client library using your access token.
# Note: You can find/create your access token at https://control.predicthq.com/clients
phq = Client(access_token="$ACCESS_TOKEN")
```

### Search Events

Perform a basic search of events using the `q`, `rank_level` and `country` parameters.

```python
for event in phq.events.search(q="Foo Fighters", rank_level=[4, 5], country='US'):
    print(event.rank, event.category, event.title, event.start.strftime('%Y-%m-%d'))
```

By default, the event search will only return the first ten results. If you want to paginate or access more results at once, please look at either using limit/offset parameters or at using the `iter_all()` helper.

## Further Examples

Please browse through our [use case examples](https://github.com/predicthq/sdk-py/tree/master/usecases) on our GitHub repository.

## Found an Issue?

Please [log an issue](https://github.com/predicthq/sdk-py/issues/new) on our GitHub repository.
