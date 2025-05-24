
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from app.xdent.models.xdent import Client

class IPacientRepository(ABC):
    
    def __init__(self, db: Session):
        self.db = db

    @abstractmethod
    def get_patient(self, patient_id: int) -> Client | None:
        pass
    
    