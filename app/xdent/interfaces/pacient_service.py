

from abc import ABC, abstractmethod

from app.xdent.interfaces.pacient_repository import IPacientRepository

from app.xdent.schemas.structured_data import Client

class IPacientService(ABC):
    
    def __init__(self, pacient_repository: IPacientRepository):
        self.pacient_repository = pacient_repository

    @abstractmethod
    def get_patient(self, patient_id: int) -> Client | None:
        pass