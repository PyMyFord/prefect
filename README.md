<p align=center><img align=center src='prefect.png' width=600 /></p>
<h3 align=center>prefect</h3>
<h6 align=center>MyFordMobile reverse-engineered API in Python</h6>


## Functions

### `FordAPI`

| Endpoint | Detected | Prototyped | Complete |
|----------|----------|------------|----------|
| `authenticate` | 🐳 | | |
| `get_vehicles` | | 🐳 | |
| `select_vehicle` | | 🐳 | |
| `start_engine` | | 🐳 | |



## Usage

```python
from prefect import FordAPI

F = FordAPI()
F.authenticate(USERNAME, PASSWORD)
F.get_vehicles() # returns a list of dicts with metadata
```

## Roadmap

- [ ] Figure out JSON token authentication (is this a JWT?)
- [ ] Full map of endpoints (check RE'd .apk?)
- [ ] `Vehicle` class to handle manipulation of individual vehicle object
- [ ] Config-file-based credentials for automatic authentication (if no args are passed to `authenticate` call)


### High-level 'intent'-based API
- [ ] "Turn on my car"
- [ ] "Start/stop charging my car"
