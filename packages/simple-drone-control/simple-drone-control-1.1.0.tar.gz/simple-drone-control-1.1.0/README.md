# Simple Drone Control (SDC)

[![Python Test Execution](https://github.com/erlete/simple-drone-control/actions/workflows/python-tests.yml/badge.svg)](https://github.com/erlete/simple-drone-control/actions/workflows/python-tests.yml) [![PyPI release](https://github.com/erlete/simple-drone-control/actions/workflows/python-publish.yml/badge.svg)](https://github.com/erlete/simple-drone-control/actions/workflows/python-publish.yml) [![Coverage Status](https://coveralls.io/repos/github/erlete/simple-drone-control/badge.svg?branch=stable)](https://coveralls.io/github/erlete/simple-drone-control?branch=stable) ![Python version](https://img.shields.io/badge/Python%20Version-3.10-blue)

**Simple drone control simulation that serves as API for more complex programs.**

> [!IMPORTANT]
> This package has been developed with the sole purpose of **serving as educational tool**. It does not provide with real dynamic simulation models for drones nor tracks. However, it can be used to develop some initial ideas for autonomous drone flight algorithms, without having to deal with heavy constraints such as air drag, gravity, etc. Furthermore, since it has not been developed for external usage, multiple errors or inconsistencies might arise

## Installation

This package [has been released through PyPI](https://pypi.org/project/simple-drone-control/), so it can be installed using Python's `pip` module:

```shell
python -m pip install --upgrade simple-drone-control
```

> [!NOTE]
> The command above asumes that your Python interpreter is aliased to `python` and references a version equal to or greater than 3.10

Alternatively, it is also possible to clone this repository and use the package using `pip` and/or `build`.

## Usage

The code snippet below shows all imports required to start developing a simulation. Take a look at this [code skeleton example](src/examples/example_1.py) for a more detailed example.

```python
import sdc  # Imports the whole package.

from sdc.core.vector import Vector3D, Rotator3D, distance3D  # Imports core functionality classes and functions.
from sdc.api.simulation import SimulationAPI  # Imports API simulation class.
from sdc.environment.reader import TrackSequenceReader  # Imports a reader class for track databases.
```

> [!WARNING]
> The package is installed as `simple-drone-control`, but imported as `sdc`. Attempting to import it using the installation name will result in an error

## Contributions

This package has not been developed with expansion expectations, yet external feedback is always welcome, so feel free to drop your suggestions or error reports on the [issues section](https://github.com/erlete/simple-drone-control/issues).
