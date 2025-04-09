from pydantic import BaseModel, Field
from ..utils.modeEnum import ThermostatMode
import time
from app import config


class ThermostatController:
    def __init__(self):
        self.current_temperature: float | None
        self.target_temperature: float
        self.mode: ThermostatMode = ThermostatMode.AUTO
        self.state: str
        self.last_state_change = time.time()
        self.min_cycle_duration = config.MIN_CYCLE_DURATION

    def get_status(self):
        """Get the current status of the thermostat."""
        return {
            "current_temperature": self.current_temperature,
            "target_temperature": self.target_temperature,
            "mode": self.mode,
            "state": self.state
        }

    def set_target_temp(self, temperature: float):
        """Set the target temperature."""
        self.target_temperature = temperature

    def set_mode(self, mode: ThermostatMode):
        """Set the mode of the thermostat."""
        self.mode = mode

    def evaluate(self):
        now = time.time()
        if self.current_temperature is None:
            return

        # respect du min_cycle_duration
        if now - self.last_state_change < self.min_cycle_duration:
            return

        if self.current_temperature < self.target_temperature:  # - self.cold_tolerance:
            self.state = "on"
            self.last_state_change = now
        elif self.current_temperature > self.target_temperature:   # + self.hot_tolerance:
            self.state = "off"
            self.last_state_change = now
