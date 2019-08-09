# *Class* `Vehicle`


High-level API for interacting with a vehicle.

You could foreseeably only interact with your car through this API once you have authenticated with the FordAPI service.

-----
# *Function* `__init__(self, fordAPI: 'FordAPI' = None) -> None`


Create a new Vehicle for data management.

This doesn't really make sense to use on its own.

## Arguments
> - **fordAPI** (`FordAPI`: `None`): The low-level API to use to back this Vehicle

## Returns
    None


-----
# *Function* `from_dict(data: dict, fordAPI: 'FordAPI') -> 'Vehicle'`


Create a new vehicle from a data dictionary returned by the Ford API.

## Arguments
> - **fordAPI** (`FordAPI`: `None`): The low-level API to use to back this Vehicle

## Returns
> - **Vehicle** (`None`: `None`): The vehicle object with data populated


-----
# *Function* `update(self) -> None`


Update the Vehicle information from the server.

## equivalent

>>> v = Vehicle.from_dict(v.get_status(), v._fordAPI) >>> v.update()

## Arguments
    None

## Returns
    None


-----
# *Function* `__repr__(self) -> str`


Produce a string representation of the vehicle.

For use with debugging, or, for example, str(Vehicle).

-----
# *Function* `start_engine(self)`


Start the Vehicle's engine.

Note that calls to this service are NOT parallelizable! This is because the Ford API sets a session variable depending upon which vehicle is marked as "active." If you run too many of this function in a short time-span, you will choke the server and it will forget which car you are talking about. This is not an issue for most users, and will not affect you if you only have one car registered in your account.

## Arguments
    None

## Returns
> - **dict** (`None`: `None`): Metadata about the job and its status. Probably not useful
        to you unless you're doing something funky with the Ford API.


-----
# *Function* `stop_engine(self)`


Cancel a remote-start of the Vehicle's engine.

Note that calls to this service are NOT parallelizable! This is because the Ford API sets a session variable depending upon which vehicle is marked as "active." If you run too many of this function in a short time-span, you will choke the server and it will forget which car you are talking about. This is not an issue for most users, and will not affect you if you only have one car registered in your account.

This is only relevant if you have already called Vehicle#start_engine.

## Arguments
    None

## Returns
> - **dict** (`None`: `None`): Metadata about the job and its status. Probably not useful
        to you unless you're doing something funky with the Ford API.


-----
# *Function* `unlock(self)`


Unlock this vehicle's doors.

## Arguments
    None

## Returns
> - **dict** (`None`: `None`): Metadata about the job and its status.


-----
# *Function* `lock(self)`


Lock this vehicle's doors.

## Arguments
    None

## Returns
> - **dict** (`None`: `None`): Metadata about the job and its status.


-----
# *Function* `get_status(self)`


Get the status of this vehicle, including odometry and fuel levels.

You can pass the results of this function call to a Vehicle.from_dict call in order to recreate a new copy of this Vehicle with updated info.

## Arguments
    None

## Returns
> - **dict** (`None`: `None`): A metadata dictionary with information about this vehicle.


-----
# *Class* `FordAPI`


Low-level class for interacting with the MyFordMobile API.

Authentication is handled separately so that a FordAPI object can be instantiated without having to deal with authentication at creationtime. (In this way, we can more easily pickle and pass around objects without worrying about security leak.)

-----
# *Function* `__init__(self) -> None`


Create a new FordAPI object.

## Arguments
    None

## Returns
    None


-----
# *Function* `url(self, suffix: str = "/") -> str`


Construct a URL based upon the _base_url of this object.

This method will probably only be called privately.

## Arguments
> - **suffix** (`str`: `None`): The URL endpoint to concat to the _base_url

## Returns
> - **str** (`None`: `None`): A fully-qualified URL


-----
# *Function* `post(self, url: str, data: dict) -> requests.Response`


Send a POST HTTP request to a given URL with a payload.

## Arguments
> - **url** (`str`: `None`): The URL endpoint to access     data (dict): A JSONifiable dictionary to send as the request.body

## Returns
> - **requests.Response** (`None`: `None`): The response from the HTTP request


-----
# *Function* `authenticate(self, username: str = "~/.config/myfordmobile.json", password: str = None) -> None`


Perform a server authentication.

> - **TODO** (`None`: `None`): This should be returning a token TODO: Should also accept zero arguments, in which case a local config
      file (~/.config/myfordmobile.json?) holds the credentials

## Arguments
> - **username** (`str`: `None`): User's email     password (str): The user's password

## Returns
    None


-----
# *Function* `get_vehicles(self) -> List['Vehicle']`


Get a list of all registered vehicles for this account.

## Arguments
    None

## Returns
> - **List[dict]** (`None`: `None`): A list of vehicles, in dict metadata form


-----
# *Function* `select_vehicle(self, vin: str) -> bool`


Select a vehicle to be used in this session.

## Arguments
> - **vin** (`str`: `None`): The VIN of this vehicle

## Returns
> - **bool** (`None`: `None`): Whether the selection was successful


-----
# *Function* `_send_command(self, command_name: str) -> dict`


PRIVATE Send a command to the API.

This is a central function call that handles a variety of vehicle commands, such as engine on/off, lock/unlock, etc. You should try to avoid calling this directly if at all possible!

-----
# *Function* `start_engine(self) -> dict`


Start the engine of the currently selected vehicle.

## Arguments
    dict

## Returns
    TODO


-----
# *Function* `cancel_start_engine(self) -> dict`


Start the engine of the currently selected vehicle.

## Arguments
    dict

## Returns
    TODO


-----
# *Function* `unlock(self) -> dict`


Start the engine of the currently selected vehicle.

## Arguments
    dict

## Returns
    TODO


-----
# *Function* `lock(self) -> dict`


Start the engine of the currently selected vehicle.

## Arguments
    dict

## Returns
    TODO


