import json
import requests
from auth import spotify_user_id, discover_weekly_id, discover_playlist_id, liked_discovers_playlist_id
from datetime import date
from refresh import Refresh

class DiscoverWeeklySaver:
    def __init__(self, user_id, discover_playlist_id, saved_discover_id):
        self.user_id = user_id
        self.spotify_token = ""
        self.discover_weekly_id = saved_discover_id
        self.discover_playlist = discover_playlist_id
        self.liked_playlist_id = liked_discovers_playlist_id
        self.authorizer= ""
    
    def find_discovered_songs(self):
        print("retrieving songs...")

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            discover_weekly_id)

        response = requests.get(query,headers=self.authorizer)        
        response_json = response.json()

        tracks = ''

        for i in response_json["items"]:

            track_uri = i["track"]["uri"]
            tracks += (track_uri + ",")

        self.add_to_playlist(self.discover_playlist, tracks)

    def find_liked_discovered(self):
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            discover_weekly_id)

        response = requests.get(query,headers=self.authorizer)        
        response_json = response.json()

        liked_tracks = ''
    
        for i in response_json["items"]:
            track_uri = i["track"]["uri"]
            track_id = i["track"]["id"]
            if self.get_liked_tracks(track_id):
                liked_tracks += (track_uri + ",")

        self.add_to_playlist(self.liked_playlist_id, liked_tracks)

    def get_liked_tracks(self, trackid):

        query = "https://api.spotify.com/v1/me/tracks/contains?ids={}".format(trackid)
        response = requests.get(query,headers=self.authorizer)
        
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

        response = requests.post(query,data=request_body,headers=self.authorizer)
        
        response_json = response.json()

        return response_json["id"]
    
    def add_to_playlist(self, playlist_id, tracks):
       print("adding to playlist ...")
       query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(playlist_id, tracks)
       response = requests.post(query,headers=self.authorizer)
       print(response.json)

    
    def call_refresh(self):
        print("refreshing token")
        refresh_caller = Refresh()
        self.spotify_token = refresh_caller.refresh()
        self.authorizer = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
            }

if __name__ == '__main__':
    a = DiscoverWeeklySaver(spotify_user_id, discover_playlist_id, discover_weekly_id)
    a.call_refresh()
    a.find_discovered_songs()