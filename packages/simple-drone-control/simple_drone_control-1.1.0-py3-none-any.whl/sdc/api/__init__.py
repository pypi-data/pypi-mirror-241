"""API module.

This module is perhaps the most important and complex one, as it provides with
the Simulation API, which allows the user to control a drone along a set of
designed tracks. The API automatically handles track switching, so the
information it provides is always related to the current track. It also
provides with statistical measurement tools for keeping track on the simulation
progress.

Modules:
    drone: drone API extension.
    simulation: core simulation API.
    statistics: statistical measurement tools.
    track: track API extension.

Author:
    Paulo Sanchez (@erlete)
"""
