from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Create your views here.

def play(request):
    if request.method =="POST":
        song=request.POST['song']
        birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
        spotify1 = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials('8b48e217f6df4f0fabe0800f097ae985','288402091b2e45adac1888f58247400f'))

        context={'data':[]}
        results = spotify1.search(q=song, limit=50)
        
        for idx, track in enumerate(results['tracks']['items']):
            dict1={}
            dict1['name']=track['name']
            dict1['url']=track['external_urls']['spotify']
            context['data'].append(dict1)

    
    
        return render(request,'spotify.html',context=context)
    else:
        context={'data':""}
        return render(request,'spotify.html',context=context) 