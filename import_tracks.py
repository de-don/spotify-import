import config
from utils.common import Audio
from utils.spotify import get_playlist_id, create_playlist, get_current_user_id, search_track, add_tracks

audios = []

with open('tracks.txt', 'r', encoding='utf8') as file:
    for line in file.readlines():
        artist, title = line.strip().split(' // ')
        audios.append(Audio(
            artist=artist,
            title=title,
        ))

user_id = get_current_user_id()

playlist_id = get_playlist_id(config.spotify_playlist_name)
if not playlist_id:
    playlist_id = create_playlist(user_id, config.spotify_playlist_name)

track_ids = []
skipped = []
for audio in audios:
    track_id = search_track(audio)
    if track_id:
        track_ids.append(track_id)
    else:
        print("Not found", audio)
        skipped.append(audio)

add_tracks(user_id, playlist_id, track_ids)
print("added", len(track_ids))
print("skipped", len(skipped))
