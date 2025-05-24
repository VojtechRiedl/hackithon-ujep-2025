

from fastapi import APIRouter


from app.xdent.dependencies import PacientServiceDependency


from app.xdent.schemas.structured_data import Client

router = APIRouter(prefix="/pacient")


@router.get("/{patient_id}", response_model=Client)
def get_patient(
    patient_id: int, 
    pacient_service: PacientServiceDependency
):
    return pacient_service.get_patient(patient_id)
   