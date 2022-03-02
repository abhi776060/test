import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify1 = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials('8b48e217f6df4f0fabe0800f097ae985','288402091b2e45adac1888f58247400f'))

album=[]
results = spotify1.search(q='vijay prakash', limit=50)
# print(results)
for idx, track in enumerate(results['tracks']['items']):
    # print(track)
    album.append((track['name'],track['external_urls']['spotify']))
print(album)