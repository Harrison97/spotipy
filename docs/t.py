from spotipy import Spotify

s = Spotify(token)

tracks = s.current_user_top_tracks(limit=10)
for track in tracks.items:
    print(track.name)

finlandia = '3hHWhvw2hjwfngWcFjIzqr'
s.playback_start_tracks([finlandia])
