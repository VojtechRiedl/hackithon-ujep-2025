

from app.xdent.models.xdent import Client

from app.xdent.interfaces.pacient_repository import IPacientRepository
from sqlalchemy.orm import Session

class PacientRepository(IPacientRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_patient(self, patient_id: int) -> Client | None:
        return self.db.query(Client).filter(Client.id == patient_id).first()
