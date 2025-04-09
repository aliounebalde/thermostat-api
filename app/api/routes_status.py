from fastapi import APIRouter
from app.models.request import SetPointRequest, ModeRequest
from app.models import controller
router = APIRouter(tags=["Status"], prefix="/status")


@router.get("/")
async def get_status():
    pass


@router.post("/setpoint")
async def set_target(target: SetPointRequest):
    """
    Set the target temperature of the thermostat.
    """
    controller.set_target_temp(target.target_temperature)


@router.post("/mode")
async def set_mode(mode: ModeRequest):
    """
    Set the mode of the thermostat(Auto, Manual,OFF).
    """
    controller.set_mode(mode.mode)
