import config
from utils.common import Track
from utils.spotify import get_playlist_id, create_playlist, get_current_user_id, search_track, add_tracks

tracks = []

with open('tracks.txt', 'r', encoding='utf8') as file:
    for line in file.readlines():
        tracks.append(Track.from_string(line.strip()))

user_id = get_current_user_id()

playlist_id = get_playlist_id(config.spotify_playlist_name)
if not playlist_id:
    playlist_id = create_playlist(user_id, config.spotify_playlist_name)

track_ids = []
skipped = []
for track in tracks:
    track_id = search_track(track)
    if track_id:
        track_ids.append(track_id)
    else:
        print("Not found", track)
        skipped.append(track)

add_tracks(user_id, playlist_id, track_ids)
print("added", len(track_ids))
print("skipped", len(skipped))
