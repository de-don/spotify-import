from typing import Optional, List

import spotipy
from spotipy import SpotifyImplicitGrant

from models.track import Track
from utils.common import clear_string, chunk

scope = ','.join([
    'user-read-email',
    'user-read-private',
    'playlist-read-collaborative',
    'playlist-modify-public',
    'playlist-read-private',
    'playlist-modify-private',
    'user-library-modify',
    'user-library-read',
])

sp = spotipy.Spotify(
    auth_manager=SpotifyImplicitGrant(
        client_id='f7c529d9b38b465891d8ba2a95ce7b18',
        redirect_uri='http://localhost/',
        cache_path='./.spotify-cache',
    )
)


def get_playlist_id(name: str) -> Optional[str]:
    offset = 0
    while True:
        response = sp.current_user_playlists(50, offset)
        total = response.get('total')
        items = response.get('items')

        offset += len(items)

        for item in items:
            if item.get('name') == name:
                return item.get('id')

        if offset >= total:
            return


def get_current_user_id() -> str:
    response = sp.current_user()
    return response.get('id')


def create_playlist(user_id: str, name: str) -> str:
    response = sp.user_playlist_create(
        user=user_id,
        name=name,
        public=False,
    )
    return response.get('id')


def search_track(track: Track) -> Optional[str]:
    queries = [
        # original artist + original title
        track.artist + ' ' + track.title,
        # original artist + cleared title
        track.artist + ' ' + clear_string(track.title),
        # cleared artist + cleared title
        clear_string(track.artist + ' ' + track.title),
        # original title
        track.title,
        # cleared title
        clear_string(track.title),
    ]

    for query in queries:
        response = sp.search(
            q=query,
        )
        tracks = response.get('tracks')
        items = tracks.get('items')
        if items:
            return items[0].get('id')


def add_tracks(user_id: str, playlist_id: str, track_ids: List[str]) -> Optional[str]:
    response = None
    for part_ids in chunk(track_ids, 100):
        # remove this items from the list, to prevent repeats
        sp.user_playlist_remove_all_occurrences_of_tracks(
            user=user_id,
            playlist_id=playlist_id,
            tracks=part_ids,
        )
        response = sp.user_playlist_add_tracks(
            user=user_id,
            playlist_id=playlist_id,
            tracks=part_ids,
        )
    return response and response.get('snapshot_id')
