from pydantic import BaseModel
from ..utils.modeEnum import ThermostatMode


class SetPointRequest(BaseModel):
    """
    Request model for setting the target temperature of the thermostat.
    """
    target_temperature: float


class ModeRequest(BaseModel):
    """
    Request model for setting the mode of the thermostat.
    """
    mode: ThermostatMode
