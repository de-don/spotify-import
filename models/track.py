class Track:
    """Track representation."""
    _separator = '---'

    def __init__(self, artist: str, title: str):
        self.artist = artist
        self.title = title

    def to_string(self) -> str:
        """Convert track to string."""
        return f'{self.artist} {self._separator} {self.title}'

    @classmethod
    def from_string(cls, source: str):
        """Convert track to string."""
        artist, title, *_ = source.split(cls._separator)

        return cls(
            artist=artist.strip(),
            title=title.strip()
        )
