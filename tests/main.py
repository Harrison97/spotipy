# shows artist info for a URN or URL

import spotipy

token = spotipy.prompt_for_user_token('SpoQ')
sp = spotipy.Spotify(auth=token)
result = sp.search('radiohead')
print(result)


response = sp.categories()
for cat in response['categories']['items']:
    cat_id = cat['id']
    response = sp.category_playlists(category_id=cat_id)
    print(response['playlists'])
