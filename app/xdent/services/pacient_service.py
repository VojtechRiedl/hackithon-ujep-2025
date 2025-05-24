
from app.xdent.interfaces.pacient_service import IPacientService

from app.xdent.interfaces.pacient_repository import IPacientRepository

from app.xdent.schemas.structured_data import Client

from fastapi import HTTPException

class PacientService(IPacientService):
    def __init__(self, pacient_repository: IPacientRepository):
        super().__init__(pacient_repository)
    
    def get_patient(self, patient_id: int) -> Client:
        """
        Retrieve a patient by their ID.
        
        :param patient_id: The ID of the patient to retrieve.
        :return: A dictionary containing the patient's data or None if not found.
        """
        pacient = self.pacient_repository.get_patient(patient_id)
        
        if not pacient:
            raise HTTPException(detail="Patient not found", status_code=404)

        return pacient