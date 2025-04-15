from pydantic import BaseModel
from app.utils.modeEnum import ThermostatMode
from app.utils.stateEnum import StateEnum


class StatusResponse(BaseModel):
    temperature: float | None = None
    target_temp: float
    mode: ThermostatMode
    state: StateEnum


class DefaultResponse(BaseModel):
    message: str = 'ok'
