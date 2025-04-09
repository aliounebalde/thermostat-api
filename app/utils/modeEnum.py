# An mode Enum class for a thermostat controller.
# This class defines the different modes that a thermostat can be in.

from enum import Enum


class ThermostatMode(str, Enum):
    """Enum class for thermostat modes."""

    AUTO = "auto"
    MANUAL = "manual"
    OFF = "off"

    def __str__(self):
        return self.value
