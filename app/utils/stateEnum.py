from enum import Enum


class StateEnum(str, Enum):
    """Enum class for different states."""

    ON = "on"
    OFF = "off"

    def __str__(self):
        return self.value
