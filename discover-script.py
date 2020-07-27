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
        self.liked_tracks = ""
        self.discover_playlist = "3GfAutnyoQS8TQVgvVnZN9"
        self.liked_discovered_playlist = "0tAIJjIF7scIAVAMGFY0tC"
    
    def find_songs(self):

        print("retrieving songs...")

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            discover_weekly_id)
        
        response = requests.get(query,
                            headers={"Content-Type": "application/json",
                            "Authorization": "Bearer {}".format(self.spotify_token)})
        
        response_json = response.json()


        for i in response_json["items"]:

            track_uri = i["track"]["uri"]
            track_id = i["track"]["id"]
     
            if self.get_liked_tracks(track_id):
                self.liked_tracks += (track_uri + ",")
            self.tracks += (track_uri + ",")
        self.tracks = self.tracks[:-1]

        self.add_to_playlist()

    def get_liked_tracks(self, trackid):

        query = "https://api.spotify.com/v1/me/tracks/contains?ids={}".format(trackid)
        response = requests.get(query,
                            headers={"Content-Type": "application/json",
                            "Authorization": "Bearer {}".format(self.spotify_token)})
        
        response_json = response.json()
        # returns true if liked
        return response_json[0]


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

       query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(self.liked_discovered_playlist, self.liked_tracks)
       response = requests.post(query,headers={"Content-Type": "application/json","Authorization": "Bearer {}".format(self.spotify_token)})
       print(response.json)
    
    def call_refresh(self):
        print("refreshing token")
        refresh_caller = Refresh()
        self.spotify_token = refresh_caller.refresh()
        self.find_songs()

a = SaveDiscovers()
a.call_refresh()
