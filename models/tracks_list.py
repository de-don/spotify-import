from typing import List

from models.track import Track


class TracksList:
    """Tracks list representation."""

    def __init__(self, tracks:  List[Track]):
        self.tracks = tracks

    def __iter__(self):
        return iter(self.tracks)

    def __len__(self):
        return len(self.tracks)

    def to_file(self, file_path: str):
        """Save tracks to file."""
        with open(file_path, 'w+', encoding='utf8') as file:
            for track in self.tracks:
                file.write(track.to_string() + '\n')

    @classmethod
    def from_file(cls, file_path: str) -> 'TracksList':
        """Import tracks from file."""
        tracks = []
        with open(file_path, 'r', encoding='utf8') as file:
            for line in file.readlines():
                tracks.append(Track.from_string(line.strip()))
        return cls(tracks=tracks)
