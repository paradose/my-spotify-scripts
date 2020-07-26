import json
import requests
from auth import spotify_user_id, discover_weekly_id
from datetime import date
from refresh import Refresh

class SaveDiscovers:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = ""
        self.discover_weekly_id = discover_weekly_id
        self.tracks = ""
        self.discover_playlist = "3GfAutnyoQS8TQVgvVnZN9"
    
    def find_songs(self):

        print("retrieving songs...")

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            discover_weekly_id)
        
        response = requests.get(query,
                            headers={"Content-Type": "application/json",
                            "Authorization": "Bearer {}".format(self.spotify_token)})
        
        response_json = response.json()

        print(response)

        for i in response_json["items"]:
            self.tracks += (i["track"]["uri"] + ",")
        self.tracks = self.tracks[:-1]

        self.add_to_playlist()

    def create_playlist(self):
        
        # today = date.today()
        # todayFormatted = today.strftime("%d/%m/%Y")

        query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)
        request_body = json.dumps({
            "name": "my discover weeklys",
            "description": "yayeet",
            "public": True
        })

        response = requests.post(query,data=request_body,headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
            })
        
        response_json = response.json()

        return response_json["id"]
    
    def add_to_playlist(self):
       print("adding to playlist ...")
       query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(self.discover_playlist, self.tracks)
       response = requests.post(query,headers={"Content-Type": "application/json","Authorization": "Bearer {}".format(self.spotify_token)})
       print(response.json)
    
    def call_refresh(self):
        print("refreshing token")
        refresh_caller = Refresh()
        self.spotify_token = refresh_caller.refresh()
        self.find_songs()

a = SaveDiscovers()
a.call_refresh()
