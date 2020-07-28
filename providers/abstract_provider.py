import abc

from models.tracks_list import TracksList


class AbstractProvider(abc.ABC):
    """Base class to create audio providers."""

    @abc.abstractmethod
    def get_tracks(self) -> TracksList:
        """Get list of tracks."""
