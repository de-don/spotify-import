import time
from typing import List

from models.track import Track
from providers.abstract_provider import AbstractProvider
import vk



class VkProvider(AbstractProvider):
    """Provider for tracks from vk.com"""
    def __init__(self, access_token):
        self.api = vk.API(
            vk.Session(),
            access_token=access_token,
            v='5.50'
        )

    def get_tracks(self) -> List[Track]:
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
        return tracks
