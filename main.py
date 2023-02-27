from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

def main():

    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

    SCOPE = "user-library-read"

    print(client_id, client_secret, redirect_uri)

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

    results = sp.current_user_saved_tracks()

    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

if __name__ == '__main__':
    main()