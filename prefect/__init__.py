from typing import List
import requests


class FordAPI:
    def __init__(self):
        self._base_url = "https://www.myfordmobile.com"
        self._token = None

    def url(self, suffix: str = "/") -> str:
        return f"{self._base_url}/{suffix}"

    def post(self, url: str, data: dict) -> requests.Response:
        return requests.post(
            url,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            json=data
        )

    def authenticate(self, username: str, password: str) -> None:
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
        return res

    def get_vehicles(self) -> List[dict]:
        params = {
            "PARAMS": {
                "SESSIONID": self._token,
                "apiLevel": "1",
            }
        }
        res = self.post(self.url("services/webRemoteEnergyReportPS"), params)
        return res.json()["getAllVehiclesResponse"]
