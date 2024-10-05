import requests
import os

def fetch_navica_data_from_api(self):
    api_url = "https://navapi.navicamls.net/api/v2/nav98/listings?"
    token = os.getenv("0d56bf44bf5c56b3e3c645c5804e4337")
    if not token:
        self.stdout.write(self.style.ERROR('API token is not set in environment variables'))
        return
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        listings = response.json()
    else:
        response.raise_for_status()