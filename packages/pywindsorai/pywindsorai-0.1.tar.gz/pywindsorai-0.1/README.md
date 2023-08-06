# pywindsorai

`pywindsorai` is a python package makes it easier to interact with windsor.ai's API via Python.

## Features

✅ Easy access to windsor.ai APIs

✅ Lightweight (single dependency - [requests](https://pypi.org/project/requests/))

✅ Supports both python 2.7+ and 3

## Usage

### Installation

```sh
pip install pywindsorai
```

### Registration

You need an API key to access windsor.ai's APIs. Register your account first, and then get the API key. For more details check out our official [API documentation](https://www.windsor.ai/api-documentation/) and [this article](https://www.windsor.ai/api-fields/).

### Minimal Example

```python
from pywindsorai.client import Client
from pywindsorai.enums import LAST_7D
from pywindsorai.enums import FIELD_SOURCE, FIELD_CAMPAIGN, FIELD_CLICKS

api_key = 'xxx'  # Get it from your windsor.ai account. It's recommended to store and get this securely, for example an env variable.

# Setup a client object with the API key
client = Client(api_key)

# Call the /connectors API. Response will be a python dict (parsed from the json response recieved).
orders = client.connectors(date_preset=LAST_7D, fields=[FIELD_SOURCE, FIELD_CAMPAIGN, FIELD_CLICKS])
```
