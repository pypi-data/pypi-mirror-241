"""Simulation API module.

This module combines all API resources to compose the Simulation API,
responsible for the execution, update and summary of the simulation.

Author:
    Paulo Sanchez (@erlete)
"""


import json
import os
from time import perf_counter as pc

import matplotlib.pyplot as plt
import numpy as np
from colorama import Fore, Style
from scoretree import Score, ScoreArea, ScoreTree

from ..core.gradient import ColorGradient
from ..core.vector import Rotator3D, Vector3D, distance3D
from ..environment.track import Track
from .drone import DroneAPI
from .statistics import TrackStatistics
from .track import TrackAPI


class SimulationAPI:
    """Simulation API class.

    This class represents a simulation that implements all kinematic variants
    of the simulation elements, such as the drone and the track. It provides
    with several methods that allow the user to get information about the
    simulation's state and control it.

    Attributes:
        tracks (list[TrackAPI]): track list.
        drone (DroneAPI): drone element.
        next_waypoint (Vector3D | None): next waypoint data.
        remaining_waypoints (int): remaining waypoints in the track.
        is_simulation_finished (bool): whether the simulation is finished.
        DT (float): simulation time step in seconds.
        DV (float): simulation speed step in m/s.
        DR (float): simulation rotation step in rad/s.
    """

    DT = 0.1  # [s]
    DV = 7.5  # [m/s]
    DR = np.pi  # [rad/s]

    SUMMARY_FILE_PREFIX = "summary_"
    SUMMARY_DIR = "statistics"

    def __init__(self, tracks: list[Track]) -> None:
        """Initialize a SimulationAPI instance.

        Args:
            tracks (list[Track]): track list.
        """
        self._completed_statistics: list[TrackStatistics] = []
        self._statistics = [
            TrackStatistics(TrackAPI(track), self.DT)
            for track in tracks
        ]
        self.tracks = [TrackAPI(track) for track in tracks]  # Conversion.

    @property
    def tracks(self) -> list[TrackAPI]:
        """Get track list.

        Returns:
            list[TrackAPI]: track list.
        """
        return self._tracks

    @tracks.setter
    def tracks(self, value: list[TrackAPI]) -> None:
        """Set track list.

        Args:
            value (list[TrackAPI]): track list.
        """
        if not isinstance(value, list):
            raise TypeError(
                "expected type list[Track] for"
                + f" {self.__class__.__name__}.tracks but got"
                + f" {type(value).__name__} instead"
            )

        if not value:
            raise ValueError(
                f"{self.__class__.__name__}.tracks cannot be empty"
            )

        for i, track in enumerate(value):
            if not isinstance(track, TrackAPI):
                raise TypeError(
                    "expected type Track for"
                    + f" {self.__class__.__name__}.tracks but got"
                    + f" {type(track).__name__} from item at index {i} instead"
                )

        self._tracks = value

        # Internal attributes reset:
        self._is_simulation_finished = False
        self._current_track = self._tracks.pop(0)
        self._current_statistics = self._statistics.pop(0)
        self._current_timer = 0.0
        self._target_rotation = Rotator3D()
        self._target_speed = 0.0

    @property
    def drone(self) -> DroneAPI:
        """Returns the drone element.

        Returns:
            DroneAPI: drone element.
        """
        return self._current_track.drone

    @property
    def next_waypoint(self) -> Vector3D | None:
        """Returns the next waypoint data.

        Returns:
            Vector3D | None: next waypoint data.
        """
        return self._current_track.next_waypoint

    @property
    def remaining_waypoints(self) -> int:
        """Returns the remaining waypoints in the track.

        Returns:
            int: remaining waypoints in the track.
        """
        return self._current_track.remaining_waypoints

    @property
    def is_simulation_finished(self) -> bool:
        """Returns whether the simulation is finished.

        Returns:
            bool: True if the simulation is finished, False otherwise.
        """
        return self._is_simulation_finished

    def set_drone_target_state(
        self,
        yaw: int | float,
        pitch: int | float,
        speed: int | float
    ) -> None:
        """Set drone target state.

        Args:
            yaw (int | float): target drone yaw in radians.
            pitch (int | float): target drone pitch in radians.
            speed (int | float): target drone speed in m/s.
        """
        if not isinstance(yaw, (int, float)):
            raise TypeError(
                "expected type (int, float) for"
                + f" {self.__class__.__name__}.set_drone_target_state yaw"
                + f" but got {type(yaw).__name__} instead"
            )

        if not isinstance(pitch, (int, float)):
            raise TypeError(
                "expected type (int, float) for"
                + f" {self.__class__.__name__}.set_drone_target_state pitch"
                + f" but got {type(pitch).__name__} instead"
            )

        if not isinstance(speed, (int, float)):
            raise TypeError(
                "expected type int | float for"
                + f" {self.__class__.__name__}.set_drone_target_state speed"
                + f" but got {type(speed).__name__} instead"
            )

        self._target_rotation = Rotator3D(
            np.rad2deg(yaw),
            np.rad2deg(pitch),
            0
        )
        self._target_speed = speed

    def update(
        self,
        plot: bool = True,
        dark_mode: bool = False,
        fullscreen: bool = True
    ) -> None:
        """Update drone state along the current track and plot environment.

        Args:
            plot (bool): whether to plot statistics after each track. Defaults
                to True.
            dark_mode (bool): whether to use dark mode for the plot. Defaults
                to False. Only used if plot is True.
            fullscreen (bool): whether to plot the figure in fullscreen mode.
                Defaults to True. Only used if plot is True.
        """
        self._current_timer += self.DT

        # Simulation endpoint conditions' definition for later use:
        c1 = self._current_timer >= self._current_track.timeout
        c2 = self._current_track.is_track_finished
        c3 = self._current_track.is_drone_stopped

        # On completed track finish condition:
        if c2 and c3:
            self._current_statistics.is_completed = True
            self._current_statistics.distance_to_end = distance3D(
                self._current_track.drone.position,
                self._current_track.track.end
            )

        # On each of the simulation finish conditions:
        if c1 or (c2 and c3):

            # Plot current track statistics:
            if plot:
                self.plot(dark_mode, fullscreen)

            # Save current statistics:
            self._completed_statistics.append(self._current_statistics)

            # Get next track and reset time counter:
            if self._tracks:
                self._current_track = self._tracks.pop(0)
                self._current_statistics = self._statistics.pop(0)
                self._current_timer = 0.0
            else:
                self._is_simulation_finished = True

            return

        # Rotation update:
        self._current_track.drone.rotation = Rotator3D(
            *[
                np.rad2deg(
                    min(curr_rot + self.DR * self.DT, tg_rot)
                    if curr_rot < tg_rot else
                    max(curr_rot - self.DR * self.DT, tg_rot)
                ) for curr_rot, tg_rot in zip(
                    self._current_track.drone.rotation,
                    self._target_rotation
                )
            ]
        )

        # Speed update:
        speed = self._current_track.drone.speed
        self._current_track.drone.speed = (
            min(speed + self.DV * self.DT, self._target_speed)
            if self._target_speed >= speed else
            max(speed - self.DV * self.DT, self._target_speed)
        )

        # Position update:
        rot = self._current_track.drone.rotation
        self._current_track.drone.position += (
            Vector3D(
                speed * self.DT * np.cos(rot.x) * np.cos(rot.y),
                speed * self.DT * np.sin(rot.x) * np.cos(rot.y),
                speed * self.DT * np.sin(rot.y)
            )
        )

        self._current_statistics.add_data(
            position=self._current_track.drone.position,
            rotation=self._current_track.drone.rotation,
            speed=self._current_track.drone.speed
        )

    def plot(self, dark_mode: bool, fullscreen: bool) -> None:
        """Plot simulation environment.

        Args:
            dark_mode (bool): whether to use dark mode for the plot.
            fullscreen (bool): whether to plot the figure in fullscreen mode.
        """
        # Variable definition for later use:
        times = np.arange(0, self._current_track.timeout, self.DT)
        speeds = self._current_statistics.speeds
        rotations = [
            [rot.x for rot in self._current_statistics.rotations],
            [rot.y for rot in self._current_statistics.rotations],
            [rot.z for rot in self._current_statistics.rotations]
        ]
        positions = [
            [pos.x for pos in self._current_statistics.positions],
            [pos.y for pos in self._current_statistics.positions],
            [pos.z for pos in self._current_statistics.positions]
        ]
        gradient = ColorGradient("#dc143c", "#15b01a", len(positions[0]))

        # Figure and axes setup:
        plt.style.use("dark_background" if dark_mode else "fast")
        fig = plt.figure()
        ax1 = fig.add_subplot(121, projection="3d")
        ax2 = fig.add_subplot(422)
        ax3 = fig.add_subplot(424)
        ax4 = fig.add_subplot(426)
        ax5 = fig.add_subplot(428)

        # 2D axes configuration:
        config_2d = {
            "axes": (ax2, ax3, ax4, ax5),
            "data": (speeds, *rotations),
            "labels": (
                "Speed [m/s]",
                "X rotation [rad]",
                "Y rotation [rad]",
                "Z rotation [rad]"
            ),
            "titles": (
                "Speed vs Time",
                "X rotation vs Time",
                "Y rotation vs Time",
                "Z rotation vs Time"
            )
        }

        for ax, data_, title, label in zip(*config_2d.values()):
            ax.plot(times[:len(data_)], data_)
            ax.set_xlim(0, self._current_track.timeout)
            ax.set_title(title)
            ax.set_xlabel("Time [s]")
            ax.set_ylabel(label)
            ax.grid(True)

        ax2.set_ylim(self._current_track.drone.SPEED_RANGE)

        # 3D ax configuration:
        self._current_track._track.plot(ax1)

        for x, y, z, c in zip(*positions, gradient.steps):
            ax1.plot(x, y, z, "D", color=ColorGradient.rgb_to_hex(c), ms=2)

        ax1.plot(*positions, "k--", alpha=.75, lw=.75)

        ax1.set_title("3D Flight visualization")
        ax1.set_xlabel("X [m]")
        ax1.set_ylabel("Y [m]")
        ax1.set_zlabel("Z [m]")  # type: ignore

        # Figure configuration:
        plt.tight_layout()
        plt.get_current_fig_manager().window.state(  # type: ignore
            "zoomed" if fullscreen else "normal"
        )
        plt.show()

    def _compute_score(
        self,
        statistics: TrackStatistics
    ) -> tuple[bool, list[Score]]:
        """Compute track simulation score from statistics.

        Args:
            statistics (TrackStatistics): track statistics.

        Returns:
            tuple[bool, list[Score]]: list containing track completion flag and
                list of scores on each weighted area.
        """
        # Variable definition for later use:
        waypoints = statistics.track.track.waypoints  # Track waypoints.
        positions = statistics.positions  # Drone positions during simulation.
        max_sp = self.drone.SPEED_RANGE[1]  # Max drone speeed.

        # Track Distance (TD):
        min_td = sum([
            distance3D(waypoints[i], waypoints[i+1])
            for i in range(len(waypoints) - 1)
        ])
        max_td = 2 * min_td
        td = sum([
            distance3D(positions[i], positions[i+1])
            for i in range(len(positions) - 1)
        ])

        # Distance To End (DTE):
        max_tte = max_sp / self.DV  # Max time to end.
        min_dte = 0
        max_dte = max_sp * max_tte - .5 * self.DV * max_tte ** 2
        dte = statistics.distance_to_end

        # Track Time (TT):
        min_tt = max_td / max_sp + min_dte
        max_tt = (max_td / self.DV + max_tte) * 2
        tt = len(statistics.positions) * self.DT

        # Pondered score:
        return (
            statistics.is_completed,
            [
                Score(
                    name="Distance to end (DTE)",
                    weight=0.4,
                    score_range=(min_dte, max_dte),
                    value=dte if statistics.is_completed else max_dte,
                    inverse=True
                ),

                Score(
                    name="Track distance (TD)",
                    weight=0.25,
                    score_range=(min_td, max_td),
                    value=td if statistics.is_completed else max_td,
                    inverse=True
                ),
                Score(
                    name="Track Time (TT)",
                    weight=0.35,
                    score_range=(min_tt, max_tt),
                    value=tt if statistics.is_completed else max_tt,
                    inverse=True
                )
            ]
        )

    def summary(self) -> None:
        """Print a summary of the simulation."""
        # Track weight computation:
        weight_range = range(1, len(self._completed_statistics) + 1)
        track_weights = [
            i / sum(weight_range)
            for i in weight_range
        ]

        # Score tree generation:
        st = ScoreTree([ScoreArea("Simulation", 1, [
            Score(f"Track {i + 1} (DNF)", 1, (0, 1), 0)
            if not score[0] else
            ScoreArea(f"Track {i + 1}", weight, score[1])
            for (i, weight), score in zip(
                enumerate(track_weights), [
                    self._compute_score(stat)
                    for stat in self._completed_statistics
                ]
            )
        ])], colorized=True)

        print(
            Fore.BLUE + Style.BRIGHT
            + " Simulation statistics ".center(80, "=")
            + Style.RESET_ALL + "\n"
            + str(st)
            + Fore.BLUE + Style.BRIGHT + "\n"
            + f" Total score: {st.score * 100:.2f}% ".center(80, "=")
            + Style.RESET_ALL
        )
