import requests
import os

class NavicaAPI:
    BASE_URL = "https://navapi.navicamls.net/api/v2/nav98/"
    def __init__(self, access_token):
        self.access_token = access_token

    def get_properties(self, endpoint='listings', params={}):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.get(f"{self.BASE_URL}/{endpoint}", headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
