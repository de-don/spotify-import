import logging
import time

import vk_api
from tqdm import tqdm

from models.track import Track
from models.tracks_list import TracksList
from providers.abstract_provider import AbstractProvider
from utils.vk import VkInteractiveTokenAuth

logger = logging.getLogger(__name__)


class VkProvider(AbstractProvider):
    """Provider for tracks from vk.com"""

    def __init__(self):
        logger.info('[Start VK.COM authorization]')

        access_token = VkInteractiveTokenAuth(
            client_id=6121396,
            scope=1073737727,
        ).get_access_token()
        session = vk_api.VkApi(token=access_token, api_version='5.50')
        self.api = session.get_api()

    def get_tracks(self) -> TracksList:
        """Get all tracks of current user."""
        tracks = []
        offset = 0

        pb = tqdm(desc='Export tracks')
        while tqdm:
            resp = self.api.audio.get(
                count=100,
                offset=offset,
            )

            items = resp['items']
            total = resp['count']
            pb.total = total

            if not items:
                break

            offset += len(items)

            for item in items:
                tracks.append(Track(
                    artist=item.get('artist'),
                    title=item.get('title'),
                ))
                pb.update()

            time.sleep(0.34)

        pb.close()
        return TracksList(tracks)
