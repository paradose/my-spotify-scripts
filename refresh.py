from auth import refresh_token, base_64
import json
import requests

class Refresh:

    def __init__(self):
        self.refresh_token = refresh_token
        self.base_64 = base_64
    
    def refresh(self):
        # curl -H "Authorization: Basic ZjM4Zj...Y0MzE=" -d grant_type=refresh_token -d refresh_token=NgAagA...NUm_SHo https://accounts.spotify.com/api/token
        query =  "https://accounts.spotify.com/api/token"
        response = requests.post(query,
        data ={"grant_type":"refresh_token","refresh_token":self.refresh_token},
        headers={"Authorization": "Basic " + self.base_64})
        response_json = response.json()
        return response_json["access_token"]
    
