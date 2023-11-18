"""Track statistics generation module.

Author:
    Paulo Sanchez (@erlete)
"""


from ..api.track import TrackAPI
from ..core.vector import Rotator3D, Vector3D


class TrackStatistics:

    def __init__(
        self,
        track: TrackAPI,
        timestep: int | float
    ) -> None:
        """Initialize a TrackStatistics instance.

        Args:
            track (TrackAPI): statistics track.
            timestep (int | float): statistics timestep.
        """
        self.track = track
        self.timestep = timestep
        self._waypoints = track.waypoints

        # Automatically generated attributes:
        self._is_completed = False
        self._distance_to_end = 0.0
        self._data = [(track.track.start, Rotator3D(), 0.0)]  # Initial data.

    @property
    def track(self) -> TrackAPI:
        """Get track.

        Returns:
            TrackAPI: track.
        """
        return self._track

    @track.setter
    def track(self, value: TrackAPI) -> None:
        """Set track.

        Args:
            value (TrackAPI): track.
        """
        if not isinstance(value, TrackAPI):
            raise TypeError(
                "expected type TrackAPI for"
                + f" {self.__class__.__name__}.track but got"
                + f" {type(value).__name__} instead"
            )

        self._track = value

    @property
    def timestep(self) -> int | float:
        """Get statistics timestep.

        Returns:
            int | float: statistics timestep.
        """
        return self._timestep

    @timestep.setter
    def timestep(self, value: int | float) -> None:
        """Set statistics timestep.

        Args:
            value (int | float): statistics timestep.
        """
        if not isinstance(value, (int, float)):
            raise TypeError(
                "expected type int | float for"
                + f" {self.__class__.__name__}.timestep but got"
                + f" {type(value).__name__} instead"
            )

        self._timestep = value

    @property
    def waypoints(self) -> list[Vector3D]:
        """Get track waypoints.

        Returns:
            list[Vector3D]: track waypoints.
        """
        return self._waypoints

    @property
    def is_completed(self) -> bool:
        """Get track completion status.

        Returns:
            bool: track completion status.
        """
        return self._is_completed

    @is_completed.setter
    def is_completed(self, value: bool) -> None:
        """Set track completion status.

        Args:
            value (bool): track completion status.
        """
        if not isinstance(value, bool):
            raise TypeError(
                "expected type bool for"
                + f" {self.__class__.__name__}.is_completed but got"
                + f" {type(value).__name__} instead"
            )

        self._is_completed = value

    @property
    def distance_to_end(self) -> float:
        """Get drone distance to track end.

        Returns:
            float: drone distance to track end.
        """
        return self._distance_to_end

    @distance_to_end.setter
    def distance_to_end(self, value: int | float) -> None:
        """Set drone distance to track end.

        Args:
            value (int | float): drone distance to track end.
        """
        if not isinstance(value, (int, float)):
            raise TypeError(
                "expected type int | float for"
                + f" {self.__class__.__name__}.distance_to_end but got"
                + f" {type(value).__name__} instead"
            )

        self._distance_to_end = float(value)

    @property
    def data(self) -> list[tuple[Vector3D, Rotator3D, int | float]]:
        """Get drone position, rotation and speed data at each timestep.

        Returns:
            list[tuple[Vector3D, Rotator3D, int | float]]: position,
                rotation and speed of the drone at each timestep.
        """
        return self._data

    @property
    def positions(self) -> list[Vector3D]:
        """Get drone positions at each timestep.

        Returns:
            list[Vector3D]: drone positions at each timestep.
        """
        return [data[0] for data in self._data]

    @property
    def rotations(self) -> list[Rotator3D]:
        """Get drone rotations at each timestep.

        Returns:
            list[Rotator3D]: drone rotations at each timestep.
        """
        return [data[1] for data in self._data]

    @property
    def speeds(self) -> list[int | float]:
        """Get drone speeds at each timestep.

        Returns:
            list[int | float]: drone speeds at each timestep.
        """
        return [data[2] for data in self._data]

    def add_data(
        self,
        position: Vector3D,
        rotation: Rotator3D,
        speed: int | float
    ) -> None:
        """Add drone position, rotation and speed data.

        Args:
            position (Vector3D): drone position.
            rotation (Rotator3D): drone rotation.
            speed (int | float): drone speed.
        """
        if not isinstance(position, Vector3D):
            raise TypeError(
                "expected type Vector3D for"
                + f" {self.__class__.__name__}.add_data but got"
                + f" {type(position).__name__} instead"
            )

        if not isinstance(rotation, Rotator3D):
            raise TypeError(
                "expected type Rotator3D for"
                + f" {self.__class__.__name__}.add_data but got"
                + f" {type(rotation).__name__} instead"
            )

        if not isinstance(speed, (int, float)):
            raise TypeError(
                "expected type int | float for"
                + f" {self.__class__.__name__}.add_data but got"
                + f" {type(speed).__name__} instead"
            )

        self._data.append((position, rotation, speed))
