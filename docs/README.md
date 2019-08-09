# Getting Started Using `prefect`

This library exposes two classes that you care about: `FordAPI` and `Vehicle`.

To get started, install this library (`pip install -U .` from the root directory of this codebase) and then:

```python
from prefect import FordAPI
```

Before you can use the Ford API, you need to authenticate with the server. You can do this in a variety of ways, but the recommended strategy is to put a config file in your `~/.config` directory with credentials like so:

`~/.config/myfordmobile.json`
```json
{
    "username": "YOUR_EMAIL",
    "password": "YOUR_PASSWORD"
}
```

> Note that you need to use your EMAIL as your username.

You can now authenticate by creating a new API caller:

```python
f = FordAPI()
f.authenticate()
```

The first thing you'll want to do is get a list of vehicles:

```python
f.get_vehicles()
```

This returns a list of `Vehicle` objects, each of which can be controlled independently of the others:

```python
# get the first (or only) vehicle associated with this account
my_car = f.get_vehicles()[0]

my_car.lock()
```

A complete list of capabilities is included in the [Reference](Reference.md) page of the /docs in this repo.
