from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values
from Playlist import Playlist
from tqdm import tqdm
import spotipy

class Spotify:
    def __init__(self, read_limit):
        self.read_limit = read_limit
        config = dotenv_values()
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=config['CLIENT_ID'],
            client_secret=config['CLIENT_SECRET'],
            redirect_uri=config['REDIRECT_URL'],
            scope="user-library-read"
        ))

    def get_playlist(self, uri):
        all_tracks = []
        LIMIT = 50
        name = self.sp.playlist(uri, fields="name")["name"]
        total = self.sp.playlist_items(uri, limit=1, offset=0)["total"]
        count = 0
        with tqdm(total=total) as t:
            while count < total:
                new_tracks = self.sp.playlist_items(uri, limit=LIMIT, offset=count)                    
                for track in new_tracks["items"]:
                    track = track["track"]
                    all_tracks.append(track)
                t.update(len(new_tracks["items"]))
                count += LIMIT
                if total == -1 or count >= total:
                    break
        return Playlist(name, all_tracks)
    
    # returns: list[ { <name>:<id> } ]
    def get_user_playlists(self):
        playlists = {}
        total = self.sp.current_user_playlists(limit=1)["total"]
        count = 0
        with tqdm(total=total) as t:
            while count < total:
                read_playlists = self.sp.current_user_playlists(limit=self.read_limit, offset=count)
                for playlist in read_playlists["items"]:
                    playlists[playlist["name"]] = playlist["id"]
                t.update(len(read_playlists["items"]))
                count += self.read_limit
                if total == -1 or count >= total:
                    break
        return playlists

    def get_user_favs(self):
        all_tracks = []
        LIMIT = 50
        total = self.sp.current_user_saved_tracks(1, 0)["total"]
        count = 0
        with tqdm(total=total) as t:
            while count < total:
                new_tracks = self.sp.current_user_saved_tracks(LIMIT, 0)
                for track in new_tracks["items"]:
                    track = track["track"]
                    all_tracks.append(track)
                t.update(len(new_tracks["items"]))
                count += LIMIT
                if total == -1 or count >= total:
                    break
        return Playlist("favs", all_tracks)