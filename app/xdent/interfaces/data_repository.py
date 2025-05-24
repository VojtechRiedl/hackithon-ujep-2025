

from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

class IDataRepository(ABC):
    """
    Interface for data repository classes.
    """

    def __init__(self, db: Session):
        self.db = db

    @abstractmethod
    def get_structured_data(self) -> list[dict]:
        """
        Retrieve structured data from the repository.

        :return: A list of dictionaries containing the structured data.
        """
        pass

    
    @abstractmethod
    def upload_data_to_database(self, data: list[dict]):
        pass


    @abstractmethod
    def get_data_from_database(self):
        pass