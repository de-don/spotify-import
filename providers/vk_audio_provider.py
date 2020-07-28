import time

import vk_api

from models.track import Track
from models.tracks_list import TracksList
from providers.abstract_provider import AbstractProvider


class VkProvider(AbstractProvider):
    """Provider for tracks from vk.com"""

    def __init__(self, access_token):
        session = vk_api.VkApi(token=access_token, api_version='5.50')
        self.api = session.get_api()

    def get_tracks(self) -> TracksList:
        """Get all tracks of current user."""
        tracks = []
        offset = 0

        while True:
            resp = self.api.audio.get(
                count=100,
                offset=offset,
            )
            items = resp['items']

            if not items:
                break

            offset += len(items)

            for item in items:
                tracks.append(Track(
                    artist=item.get('artist'),
                    title=item.get('title'),
                ))

            time.sleep(0.34)
        return TracksList(tracks)
