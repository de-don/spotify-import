import abc
from typing import List

from models.track import Track


class AbstractProvider(abc.ABC):
    """Base class to create audio providers."""

    @abc.abstractmethod
    def get_tracks(self) -> List[Track]:
        """Get list of tracks."""
