"""
Main file for prefect Python library for interacting with the MyFordMobile API
servers. These servers host a SOAP-style API that sometimes has a few REST-API
flavored artifacts.
"""

from typing import List
import os
import json

import requests

_BEARER_TOKEN = "b7bdf3f01761660c87a6b3b21afb898a"


class Vehicle:
    """
    High-level API for interacting with a vehicle.

    You could foreseeably only interact with your car through this API once you
    have authenticated with the FordAPI service.
    """

    def __init__(self, fordAPI: 'FordAPI' = None) -> None:
        """
        Create a new Vehicle for data management.

        This doesn't really make sense to use on its own.

        Arguments:
            fordAPI (FordAPI): The low-level API to use to back this Vehicle

        Returns:
            None

        """
        self._fordAPI = fordAPI

    @staticmethod
    def from_dict(data: dict, fordAPI: 'FordAPI') -> 'Vehicle':
        """
        Create a new vehicle from a data dictionary returned by the Ford API.

        Arguments:
            fordAPI (FordAPI): The low-level API to use to back this Vehicle

        Returns:
            Vehicle: The vehicle object with data populated

        """
        v = Vehicle(fordAPI=fordAPI)
        v._update_from_dict(data)
        return v

    def _update_from_dict(self, data: dict) -> None:
        self._data = data
        self.location = (float(data["LATITUDE"]), float(data["LONGITUDE"]))
        self.odometer = float(data["ODOMETER"])
        self._ev_dte = data.get("ELECTRICDTE", 0)
        self._fuel_dte = float(data.get("FUELDTE", 0))
        self._dte = float(data.get("OVERALLDTE", 0))
        self._vehicle_type = data["MODELNAME"]
        self._vehicle_year = data["MODELYEAR"]
        self.vin = data["vin"]
        self.nickname = data["vehiclenickname"]
        self._fuel_level = float(data["fuelLevel"])
        self._state_of_charge = data.get("stateOfCharge")
        self._charge_status = data.get("chargeStatus")
        self._plug_status = data.get("plugStatus")

    def update(self) -> None:
        """
        Update the Vehicle information from the server.

        If you haven't made any other changes to the Vehicle object, these two
        lines are equivalent:

        >>> v = Vehicle.from_dict(v.get_status(), v._fordAPI)
        >>> v.update()

        Arguments:
            None

        Returns:
            None

        """
        self._update_from_dict(self.get_status())

    def __repr__(self) -> str:
        """
        Produce a string representation of the vehicle.

        For use with debugging, or, for example, str(Vehicle).
        """
        return f"<'{self.nickname}' {self._vehicle_year} {self._vehicle_type}>"

    def start_engine(self):
        """
        Start the Vehicle's engine.

        Note that calls to this service are NOT parallelizable! This is because
        the Ford API sets a session variable depending upon which vehicle is
        marked as "active." If you run too many of this function in a short
        time-span, you will choke the server and it will forget which car you
        are talking about. This is not an issue for most users, and will not
        affect you if you only have one car registered in your account.

        Arguments:
            None

        Returns:
            dict: Metadata about the job and its status. Probably not useful
                to you unless you're doing something funky with the Ford API.

        """
        self._fordAPI.select_vehicle(self.vin)
        return self._fordAPI.start_engine()

    def stop_engine(self):
        """
        Cancel a remote-start of the Vehicle's engine.

        Note that calls to this service are NOT parallelizable! This is because
        the Ford API sets a session variable depending upon which vehicle is
        marked as "active." If you run too many of this function in a short
        time-span, you will choke the server and it will forget which car you
        are talking about. This is not an issue for most users, and will not
        affect you if you only have one car registered in your account.

        This is only relevant if you have already called Vehicle#start_engine.

        Arguments:
            None

        Returns:
            dict: Metadata about the job and its status. Probably not useful
                to you unless you're doing something funky with the Ford API.

        """
        self._fordAPI.select_vehicle(self.vin)
        return self._fordAPI.cancel_start_engine()

    def unlock(self):
        """
        Unlock this vehicle's doors.

        Arguments:
            None

        Returns:
            dict: Metadata about the job and its status.

        """
        self._fordAPI.select_vehicle(self.vin)
        return self._fordAPI.unlock()

    def lock(self):
        """
        Lock this vehicle's doors.

        Arguments:
            None

        Returns:
            dict: Metadata about the job and its status.

        """
        self._fordAPI.select_vehicle(self.vin)
        return self._fordAPI.lock()

    def get_status(self):
        """
        Get the status of this vehicle, including odometry and fuel levels.

        You can pass the results of this function call to a Vehicle.from_dict
        call in order to recreate a new copy of this Vehicle with updated info.

        Arguments:
            None

        Returns:
            dict: A metadata dictionary with information about this vehicle.

        """
        return [
            v
            for v in self._fordAPI.get_vehicles()
            if v.vin == self.vin
        ][0]._data


class FordAPI:
    """
    Low-level class for interacting with the MyFordMobile API.

    Authentication is handled separately so that a FordAPI object can be
    instantiated without having to deal with authentication at creationtime.
    (In this way, we can more easily pickle and pass around objects without
    worrying about security leak.)
    """

    def __init__(self) -> None:
        """
        Create a new FordAPI object.

        Arguments:
            None

        Returns:
            None

        """
        self._base_url = "https://www.myfordmobile.com"
        self._token = None

    def url(self, suffix: str = "/") -> str:
        """
        Construct a URL based upon the _base_url of this object.

        This method will probably only be called privately.

        Arguments:
            suffix (str): The URL endpoint to concat to the _base_url

        Returns:
            str: A fully-qualified URL

        """
        return f"{self._base_url}/{suffix}"

    def post(self, url: str, data: dict) -> requests.Response:
        """
        Send a POST HTTP request to a given URL with a payload.

        Arguments:
            url (str): The URL endpoint to access
            data (dict): A JSONifiable dictionary to send as the request.body

        Returns:
            requests.Response: The response from the HTTP request

        """
        return requests.post(
            url,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/javascript, */*",
                "Authorization": f"Bearer {_BEARER_TOKEN}",
            },
            json=data
        )

    def authenticate(self, username: str = "~/.config/myfordmobile.json", password: str = None) -> None:
        """
        Perform a server authentication.

        TODO: This should be returning a token
        TODO: Should also accept zero arguments, in which case a local config
              file (~/.config/myfordmobile.json?) holds the credentials

        Arguments:
            username (str): User's email
            password (str): The user's password

        Returns:
            None

        """
        if password is None:
            try:
                with open(os.path.expanduser(username), 'r') as fh:
                    config = json.load(fh)
                    username = config['username']
                    password = config['password']
            except:
                raise ValueError(
                    "Failed to authenticate. You must provide a username and "
                    "a password, or you can provide a path to a config file "
                    "(~/.config/myfordmobile.json)."
                )
        params = {
            "PARAMS": {
                "emailaddress": username,
                "password": password,
                "persistent": "0",
                "apiLevel": "2",
            }
        }
        res = self.post(self.url("services/webLoginPS"), params)
        self._token = res.json()["response"]["authToken"]

    def get_vehicles(self) -> List['Vehicle']:
        """
        Get a list of all registered vehicles for this account.

        Arguments:
            None

        Returns:
            List[dict]: A list of vehicles, in dict metadata form

        """
        params = {
            "PARAMS": {
                "SESSIONID": self._token,
                "apiLevel": "2",
            }
        }
        res = self.post(self.url("services/webRemoteEnergyReportPS"), params)
        if "response" not in res.json():
            raise ValueError("Failed to fetch results:", res.text)
        response = res.json()["response"]
        if isinstance(response, dict):
            response = [response, ]
        return [Vehicle.from_dict(r, self) for r in response]

    def select_vehicle(self, vin: str) -> bool:
        """
        Select a vehicle to be used in this session.

        Arguments:
            vin (str): The VIN of this vehicle

        Returns:
            bool: Whether the selection was successful

        """
        params = {
            "PARAMS": {
                "VIN": vin,
                "SESSIONID": self._token,
                "apiLevel": "2",
            }
        }
        res = self.post(self.url("services/webSetActiveVehiclePS"), params)
        return 'error' not in res.json()

    def _send_command(self, command_name: str) -> dict:
        """
        PRIVATE Send a command to the API.

        This is a central function call that handles a variety of vehicle
        commands, such as engine on/off, lock/unlock, etc. You should try
        to avoid calling this directly if at all possible!
        """
        params = {
            "PARAMS": {
                "LOOKUPCODE": command_name,
                "SESSIONID": self._token,
                "apiLevel": "2",
            }
        }
        res = self.post(self.url("services/webAddCommandPS"), params)
        result = res.json()
        if "error" in result:
            raise ValueError("Authentication failed.", result["error"])
        if "status" in result and "400" in result["status"]:
            raise ValueError("Failure from server.", result)
        return result

    def start_engine(self) -> dict:
        """
        Start the engine of the currently selected vehicle.

        Arguments:
            dict

        Returns:
            TODO

        """
        return self._send_command("START_CMD")

    def cancel_start_engine(self) -> dict:
        """
        Start the engine of the currently selected vehicle.

        Arguments:
            dict

        Returns:
            TODO

        """
        return self._send_command("CANCEL_START_CMD")

    def unlock(self) -> dict:
        """
        Start the engine of the currently selected vehicle.

        Arguments:
            dict

        Returns:
            TODO

        """
        return self._send_command("UNLOCK_CMD")

    def lock(self) -> dict:
        """
        Start the engine of the currently selected vehicle.

        Arguments:
            dict

        Returns:
            TODO

        """
        return self._send_command("LOCK_CMD")
