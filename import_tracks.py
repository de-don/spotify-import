from tqdm import tqdm

import config
from models.tracks_list import TracksList
import utils.spotify as spotify

tracks_list = TracksList.from_file(file_path='tracks.txt')

# Get current spotify user id
user_id = spotify.get_current_user_id()

# Get playlist id (or create)
playlist_id = spotify.get_playlist_id(config.spotify_playlist_name)
if not playlist_id:
    playlist_id = spotify.create_playlist(user_id, config.spotify_playlist_name)

# Find the tracks
track_ids = []
skipped = []
for track in tqdm(tracks_list, 'Search for tracks', total=len(tracks_list)):
    track_id = spotify.search_track(track)
    if track_id:
        track_ids.append(track_id)
    else:
        tqdm.write(f"Not found {track}")
        skipped.append(track)

# Add tracks to playlist
spotify.add_tracks(user_id, playlist_id, track_ids)

print("added", len(track_ids))
print("skipped", len(skipped))
