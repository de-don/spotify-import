import time
from typing import List

import vk

from .common import Audio


def get_audio_list(token: str, user_id: int = None) -> List[Audio]:
    """Get list of all audios of user.

    Args:
        token: token from the official app with available audio API.
        user_id: id of the user (if none - current user)

    """
    api = vk.API(
        vk.Session(),
        access_token=token,
        v='5.50'
    )
    audios = []
    offset = 0

    while True:
        resp = api.audio.get(
            user_id=user_id,
            count=100,
            offset=offset,
        )
        items = resp['items']

        if not items:
            break

        offset += len(items)

        for item in items:
            audios.append(Audio(
                artist=item.get('artist'),
                title=item.get('title'),
            ))

        time.sleep(0.34)

    return audios
