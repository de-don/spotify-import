from typing import List


class Track:
    """Track representation."""
    _separator = '---'

    def __init__(self, artist: str, title: str):
        self.artist = artist
        self.title = title

    def to_string(self) -> str:
        """Convert track to string."""
        return f'{self.artist} {self._separator} {self.title}'

    def __str__(self):
        return f'{self.artist} - {self.title}'

    @classmethod
    def from_string(cls, source: str) -> 'Track':
        """Convert track to string."""
        artist, title, *_ = source.split(cls._separator)

        return cls(
            artist=artist.strip(),
            title=title.strip()
        )

    @classmethod
    def to_file(cls, tracks: List['Track'], file_path: str):
        """Save tracks to file."""
        with open(file_path, 'w+', encoding='utf8') as file:
            for track in tracks:
                file.write(track.to_string() + '\n')

    @classmethod
    def from_file(cls, file_path: str) -> List['Track']:
        """Import tracks from file."""
        tracks = []
        with open(file_path, 'r', encoding='utf8') as file:
            for line in file.readlines():
                tracks.append(Track.from_string(line.strip()))
        return tracks
