from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re

#set up client Credentials
sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='d84ab9456bc14c25bd84a0eb6b82eece',
    client_secret='438aa9d6f71147d493ace242c08edf5e'
))

#full track url
track_url="https://open.spotify.com/track/003vvx7Niy0yvhvHt4a68B"

#Extract track ID directly from the URL using regex
track_id=re.search(r'track/([a-zA-Z0-9]+)',track_url).group(1)

#fetch track details
track=sp.track(track_id)
print(track)

#Extract metadata
track_data={
'track_name':track['name'],
'artist_name':track['album']['artists'][0]['name'],
'album_name':track['album']['name'],
'release_date':track['album']['release_date'],
'popularity':track['popularity'],
'duration_ms':track['duration_ms']/60000
             }
#Display the metadata
print(f'\nTrack Name:{track_data["track_name"]}')
print(f'Artist Name:{track_data["artist_name"]}')
print(f'Album Name:{track_data["album_name"]}')
print(f'Release Date:{track_data["release_date"]}')
print(f'Popularity:{track_data["popularity"]}')
print(f'Duration(min):{track_data["duration_ms"]:.2f}')

#converting metadata to dataframe
df=pd.DataFrame([track_data])
print("\nTrack data as DataFrame")
print(df)

#Save metadata to csv
df.to_csv('spotify_track_data.csv',index=False)

features=['popularity','duration_ms']
values=[track_data['popularity'],track_data['duration_ms']]

plt.figure(figsize=(8,5))
plt.bar(features,values,color=['pink','purple'], edgecolor='black')
plt.ylabel('Values')
plt.title(f"Track metadat for '{track_data['track_name']}'")
plt.show()