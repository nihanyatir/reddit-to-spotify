import http.client
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

connection = http.client.HTTPSConnection("www.reddit.com")

connection.request("GET", "/r/music.json")

music_response = connection.getresponse()

music_response_data = music_response.read()
music_json = json.loads(music_response_data)

song_list = []
for post in music_json["data"]["children"]:
    url = post["data"]["url"]
    if "youtube.com/watch" in url:
        bracket_index = post["data"]["title"].find("[")

        # If bracket_index is -1, this means the string does NOT contain a [
        if bracket_index == -1:
            continue

        song_list.append(post["data"]["title"][0:bracket_index - 1])


scope = "playlist-modify-private"
token = util.prompt_for_user_token(
        'username', 
        scope='playlist-modify',
        client_id='client-id',
        client_secret='client-secret',
        redirect_uri='http://localhost:8080')

spotify = spotipy.Spotify(auth=token)

playlist_id = "spotify:playlist:"
track_id_list = []
for song in song_list:
    result = spotify.search(q=song)
    if len(result["tracks"]["items"]) == 0:
        continue
    track_id_list.append(result["tracks"]["items"][0]["uri"])

spotify.user_playlist_add_tracks("spotify:user:username", playlist_id, track_id_list)
