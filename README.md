<p align=center><img align=center src='prefect.png' width=400 /></p>
<h3 align=center>prefect</h3>
<h6 align=center>MyFordMobile reverse-engineered API in Python</h6>
<h6 align=center><a href="https://sonarcloud.io/dashboard?id=PyMyFord_perfect"><img src="https://sonarcloud.io/api/project_badges/measure?project=PyMyFord_perfect&metric=alert_status" /></a></h6>

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

## Hacking on this repo

- Submit pull requests for individual features
- Make sure things work locally before pushing

- When pushing new changes to the function signatures or new documentation, re-generate the `Reference.md` file under /docs. You can use [`docshund`](https://github.com/FitMango/docshund) to do this, *thusly*:

```shell
docshund prefect/__init__.py > docs/Reference.md
```
