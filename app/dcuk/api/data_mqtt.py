
from fastapi import APIRouter

from app.xdent.dependencies import SessionDependency

from app.xdent.models.xdent import Data

router = APIRouter(
    prefix="/mqtt",
    tags=["data_mqtt"],
)


@router.get("")
def get_mqtt_data(session: SessionDependency):
    """
    Get MQTT data.
    """
    
    return session.query(Data).all()