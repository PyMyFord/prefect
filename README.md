<p align=center><img align=center src='prefect.png' width=600 /></p>
<h3 align=center>prefect</h3>
<h6 align=center>MyFordMobile reverse-engineered API in Python</h6>



## Usage

```python
from prefect import FordAPI

F = FordAPI()
F.authenticate(USERNAME, PASSWORD)
F.get_vehicles() # returns a list of dicts with metadata
my_car = F.get_vehicles()[0]

my_car.start_engine()

print(my_car.status()) # metadata dictionary
```

## Authentication

There are ~three~ (currently 2) ways to authenticate:

### Plaintext username and password

You can pass credentials directly into the `authenticate` call:
```python
F.authenticate(USERNAME, PASSWORD)
```

### Config file
You can store credentials in a JSON config file, and pass the filename into the `authenticate` call:

`~/.config/myfordmobile.json`
```json
{
    "username": "",
    "password": ""
}
```

```python
F.authenticate("~/.config/myfordmobile.json")
```

Or, if you're using that filename (the default), you can omit it entirely:
```python
F.authenticate()
```

## Environment Variables

> Not implemented.


## Roadmap

- [x] Figure out JSON token authentication (is this a JWT?)
- [ ] Full map of endpoints (check RE'd .apk?)
- [x] `Vehicle` class to handle manipulation of individual vehicle object
- [x] Config-file-based credentials for automatic authentication (if no args are passed to `authenticate` call)


### High-level 'intent'-based API
- [ ] "Turn on my car"
- [ ] "Start/stop charging my car"
