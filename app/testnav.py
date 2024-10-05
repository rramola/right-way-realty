    
import requests
import os

def getprops():
    url = "https://navapi.navicamls.net/api/v2/nav98/listings?and[0][ListingId][eq]=159150"
    access_token = "0d56bf44bf5c56b3e3c645c5804e4337"
    headers = {
            "Authorization": f"Bearer {access_token}"
        }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


x = getprops()
print(x)