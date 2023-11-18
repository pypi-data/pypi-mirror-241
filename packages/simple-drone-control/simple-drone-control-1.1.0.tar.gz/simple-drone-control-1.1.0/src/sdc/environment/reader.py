"""Track file reader module.

Author:
    Paulo Sanchez (@erlete)
"""


import json

from ..core.vector import Rotator3D, Vector3D
from ..environment.track import Track
from ..geometry.ring import Ring


class TrackSequenceReader:
    """Track sequence reader class.

    This class is used to read a track sequence file and return a list of
    tracks.

    Attributes:
        path (str): track sequence file path.
        track_sequence (list[Track]): track sequence.
    """

    def __init__(self, path: str) -> None:
        """Initialize a TrackSequenceReader instance.

        Args:
            path (str): track sequence file path.
        """
        self.path = path
        self._track_sequence = self.read()

    @property
    def path(self) -> str:
        """Get track sequence file path.

        Returns:
            str: track sequence file path.
        """
        return self._path

    @path.setter
    def path(self, value: str) -> None:
        """Set track sequence file path.

        Args:
            value (str): track sequence file path.
        """
        if not isinstance(value, str):
            raise TypeError(
                "expected type str for"
                + f" {self.__class__.__name__}.path but got"
                + f" {type(value).__name__} instead"
            )

        self._path = value

    @property
    def track_sequence(self) -> list[Track]:
        """Get track sequence.

        Returns:
            list[Track]: track sequence.
        """
        return self._track_sequence

    def read(self) -> list[Track]:
        """Read track sequence file.

        Returns:
            list[Track]: track sequence.
        """
        with open(self.path, mode="r", encoding="utf-8") as fp:
            data = json.load(fp)

        return [
            Track(
                Vector3D(*value["start"]),
                Vector3D(*value["end"]),
                [
                    Ring(
                        Vector3D(*ring["position"]),
                        Rotator3D(*ring["rotation"]),
                    )
                    for ring in value["rings"]
                ]
            ) for value in data.values()
        ]
