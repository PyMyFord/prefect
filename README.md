<p align=center><img align=center src='prefect.png' width=400 /></p>
<h3 align=center>prefect</h3>
<h6 align=center>MyFordMobile reverse-engineered API in Python</h6>
<h6 align=center>
    <a href="https://sonarcloud.io/dashboard?id=PyMyFord_perfect"><img alt="Sonar Quality Gate" src="https://img.shields.io/sonar/quality_gate/PyMyFord_perfect?server=https%3A%2F%2Fsonarcloud.io&style=for-the-badge"></a> 
    <a href="https://github.com/PyMyFord/prefect"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/PyMyFord/prefect?style=for-the-badge"></a>
    <a href="https://pypi.org/project/ford-prefect/"><img alt="PyPI" src="https://img.shields.io/pypi/v/ford-prefect?style=for-the-badge"></a>
    <a href="https://github.com/PyMyFord/prefect"><img alt="GitHub" src="https://img.shields.io/github/license/PyMyFord/prefect?style=for-the-badge"></a>
    <img src="https://img.shields.io/badge/PRETTY%20DOPE-%F0%9F%A4%99-blue.svg?style=for-the-badge" />
</h6>

## Installation

```
pip3 install -U ford-prefect
```

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

- [ ] Environment-variable based authentication


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

Install docshund with `pip3 install -U docshund`.
