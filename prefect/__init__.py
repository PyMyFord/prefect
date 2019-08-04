"""
Main file for prefect Python library for interacting with the MyFordMobile API
servers. These servers host a SOAP-style API that sometimes bhas a few REST-API
flavored artifacts.
"""

from typing import List
import requests


class FordAPI:
    """
    High-level class for interacting with the MyFordMobile API.

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
                "Accept": "application/json"
            },
            json=data
        )

    def authenticate(self, username: str, password: str) -> None:
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
        params = {
            "PARAMS": {
                "emailaddress": username,
                "password": password,
                "persistent": "1",
                "apiLevel": "1",
            }
        }
        res = self.post(self.url("services/webLoginPS"), params)

        # TODO: We should get back a token in here???
        # Set this._token.
        # TODO: Returning for debug only.
        return res

    def get_vehicles(self) -> List[dict]:
        """
        Get a list of all registered vehicles for this account.

        TODO: Return List[Vehicle] instead of List[dict]

        Arguments:
            None

        Returns:
            List[dict]: A list of vehicles, in dict metadata form

        """
        params = {
            "PARAMS": {
                "SESSIONID": self._token,
                "apiLevel": "1",
            }
        }
        res = self.post(self.url("services/webRemoteEnergyReportPS"), params)
        return res.json()["getAllVehiclesResponse"]

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
                "VIN", str,
                "SESSIONID", self._token,
                "apiLevel", "1",
            }
        }
        res = self.post(self.url("services/webSetActiveVehiclePS"), params)
        return 'error' not in res.json()

    def start_engine(self) -> None:
        """
        Start the engine of the currently selected vehicle.

        Arguments:
            None

        Returns:
            TODO

        """
        params = {
            "PARAMS": {
                "LOOKUPCODE", "START_CMD",
                "SESSIONID", self._token,
                "apiLevel", "1",
            }
        }
        res = self.post(self.url("services/webAddCommandPS"), params)
        result = res.json()
        if "error" in result:
            raise ValueError("Authentication failed.", result["error"])
        if "status" in result and "400" in result["status"]:
            raise ValueError("Failure from server.", result)
        return result
