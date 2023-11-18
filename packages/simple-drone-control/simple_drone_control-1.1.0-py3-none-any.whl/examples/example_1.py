"""Main simulation module.

This module contains all simulation code. It imports the Simulation API, which
allows the user to control a Drone along a set of designed tracks. The API
automatically handles track switching, so the information it provides is always
related to the current track.

Author:
    Paulo Sanchez (@erlete)
"""

import os

from sdc.api.simulation import SimulationAPI
from sdc.core.vector import Rotator3D, Vector3D, distance3D
from sdc.environment.reader import TrackSequenceReader

# Simulation API definition:
sim = SimulationAPI(
    TrackSequenceReader(
        os.path.join(os.path.dirname(__file__), "tracks.json")
    ).track_sequence
)

# Simulation mainloop:
while not sim.is_simulation_finished:

    """Drone element.

    This element represents the dynamic part of the simulation. It provides
    with several methods that allow the user to get information about the
    drone's state and control it.

    Attributes:
        position (Vector3D): current drone position.
        rotation (Rotator3D): current drone rotation.
        speed (float): current drone speed.
    """
    drone = sim.drone

    """Next waypoint data.

    The next_waypoint provides information about the location (x, y, z) of the
    next waypoint of the track. It can either be a Vector3D or None if the end
    of the track has been reached. On the other hand, the `remaining` element
    provides information on how many waypoints are left in the track. If it
    reaches 0, the track is finished.
    """
    next_waypoint, remaining = sim.next_waypoint, sim.remaining_waypoints

    #########################################################
    # TODO: implement path planning and control logic here. #
    #########################################################

    # Update drone state:
    sim.set_drone_target_state(
        yaw=0,  # TODO: implement value change.
        pitch=0,  # TODO: implement value change.
        speed=0  # TODO: implement value change.
    )

    # Update simulation state:
    sim.update(plot=True, dark_mode=False, fullscreen=False)

# Print simulation statistics summary:
sim.summary()
