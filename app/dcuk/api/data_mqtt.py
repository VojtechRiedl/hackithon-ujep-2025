
from fastapi import APIRouter

from app.xdent.dependencies import SessionDependency

from app.xdent.models.xdent import Data

from fastapi import HTTPException

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


@router.get("/{id}")
def get_mqtt_data_by_id(
    id: int,
    session: SessionDependency
):
    """
    Get MQTT data.
    """

    data = session.query(Data).filter(Data.id == id).first()

    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    
    return data