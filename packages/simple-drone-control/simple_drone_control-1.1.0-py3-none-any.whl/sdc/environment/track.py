"""Track utilities module.

Author:
    Paulo Sanchez (@erlete)
"""


from ..core.gradient import ColorGradient
from ..core.vector import Vector3D
from ..geometry.ring import Ring


class Track:
    """Track representation class.

    This class is used to represent a track composed of a start point, an end
    point and a sequence of rings.

    Attributes:
        start (Vector3D): track start.
        end (Vector3D): track end.
        rings (list[Ring]): track rings.
        waypoints (list[Vector3D]): track waypoints.
    """

    def __init__(
        self,
        start: Vector3D,
        end: Vector3D,
        rings: list[Ring]
    ) -> None:
        """Initialize a Track instance.

        Args:
            start (Vector3D): track start.
            end (Vector3D): track end.
            rings (list[Ring]): track rings.
        """
        self.start = start
        self.end = end
        self.rings = rings

    @property
    def start(self) -> Vector3D:
        """Get track start.

        Returns:
            Vector3D: track start.
        """
        return self._start

    @start.setter
    def start(self, value: Vector3D) -> None:
        """Set track start.

        Args:
            value (Vector3D): track start.
        """
        if not isinstance(value, Vector3D):
            raise TypeError(
                "expected type Vector3D for"
                + f" {self.__class__.__name__}.start but got"
                + f" {type(value).__name__} instead"
            )

        self._start = value

    @property
    def end(self) -> Vector3D:
        """Get track end.

        Returns:
            Vector3D: track end.
        """
        return self._end

    @end.setter
    def end(self, value: Vector3D) -> None:
        """Set track end.

        Args:
            value (Vector3D): track end.
        """
        if not isinstance(value, Vector3D):
            raise TypeError(
                "expected type Vector3D for"
                + f" {self.__class__.__name__}.end but got"
                + f" {type(value).__name__} instead"
            )

        self._end = value

    @property
    def rings(self) -> list[Ring]:
        """Get track rings.

        Returns:
            list[Ring]: track rings.
        """
        return self._rings

    @rings.setter
    def rings(self, value: list[Ring]) -> None:
        """Set track rings.

        Args:
            value (list[Ring]): track rings.
        """
        if not isinstance(value, list):
            raise TypeError(
                "expected type list[Ring] for"
                + f" {self.__class__.__name__}.rings but got"
                + f" {type(value).__name__} instead"
            )

        for element in value:
            if not isinstance(element, Ring):
                raise TypeError(
                    f"expected Ring, got {type(element).__name__}"
                    + f"on element {element} instead"
                )

        self._rings = value

    @property
    def waypoints(self) -> list[Vector3D]:
        """Get track waypoints.

        Returns:
            list[Vector3D]: track waypoints.
        """
        return [self.start, *[ring.position for ring in self._rings], self.end]

    @staticmethod
    def ax_auto_fit(ax, offset: int = 1, *waypoints: Vector3D) -> None:
        """Set axis limits automatically.

        Args:
            ax (Axes3D): ax to set limits for.
            offset (int, optional): additional distance margin. Defaults to 1.
        """
        x = [checkpoint.x for checkpoint in waypoints]
        y = [checkpoint.y for checkpoint in waypoints]
        z = [checkpoint.z for checkpoint in waypoints]

        centers = (
            (max(x) + min(x)) / 2,
            (max(y) + min(y)) / 2,
            (max(z) + min(z)) / 2
        )

        max_distance = max(
            abs(max(x) - min(x)) / 2,
            abs(max(y) - min(y)) / 2,
            abs(max(z) - min(z)) / 2
        )

        ax.set_xlim3d(
            centers[0] - max_distance - offset,
            centers[0] + max_distance + offset
        )
        ax.set_ylim3d(
            centers[1] - max_distance - offset,
            centers[1] + max_distance + offset
        )
        ax.set_zlim3d(
            centers[2] - max_distance - offset,
            centers[2] + max_distance + offset
        )

    def plot(self, ax, **kwargs) -> None:
        """Plot track.

        Args:
            ax (Axes3D): 3D axis.
            **kwargs: plot arguments.
        """
        self.start.plot(ax, "+", color="darkred", **kwargs)
        self.end.plot(ax, "P", color="darkgreen", **kwargs)

        # Color gradient for rings:
        gradient = ColorGradient("#ff0000", "#0000ff", len(self.rings))
        steps = [ColorGradient.rgb_to_hex(step) for step in gradient.steps]

        # Ring plotting:
        for color, ring in zip(steps, self.rings):
            ring.plot(
                ax,
                color=color,
                edgecolors=color,
                **kwargs
            )

        # Title, labels and legend:
        ax.set_title("Drone track view")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.legend(
            [
                "Start",
                "End"
            ] + [
                f"Ring {i}"
                for i in range(1, len(self.rings) + 1)
            ]
        )

        # Axis planes background color:
        ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

        # Grid and axis views:
        # ax.grid(False)  # TODO: Activate this after debugging
        # ax.set_axis_off()  # TODO: Activate this after debugging
        ax.set_facecolor((1.0, 1.0, 1.0, 0.0))

        # Projection, aspect and axis scale:
        ax.set_proj_type("ortho")
        ax.set_box_aspect((1, 1, 1))
        ax.set_autoscale_on(False)
        self.ax_auto_fit(
            ax,
            1,
            self.start,
            self.end,
            *[ring.position for ring in self.rings]
        )

        # View distance and angle:
        ax.view_init(azim=-135, elev=45)
        ax.dist = 10

    def __repr__(self) -> str:
        """Get short track representation.

        Returns:
            str: short track representation.
        """
        return f"<Track with {len(self._rings)} rings>"

    def __str__(self) -> str:
        """Get long track representation.

        Returns:
            str: long track representation.
        """
        return (
            f"Track from {self._start} to {self._end} with"
            + f" rings: {self._rings}"
        )

    def __len__(self) -> int:
        """Get track length.

        Returns:
            int: track length.
        """
        return len(self._rings) + 2  # Start and end points compensation.

    def __hash__(self) -> int:
        """Get track hash.

        Returns:
            int: track hash.
        """
        return hash(tuple([self._start, *self._rings, self._end]))
