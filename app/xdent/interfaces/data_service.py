from abc import ABC, abstractmethod

from app.xdent.interfaces.data_repository import IDataRepository
from app.xdent.schemas.structured_data import Company


class IDataService(ABC):
    """
    Interface for data service classes.
    """
    def __init__(self, data_repository: IDataRepository):
        self.data_repository = data_repository

    @abstractmethod
    def get_structured_data(self) -> list[Company]:
        """
        Retrieve structured data.

        :return: A list of Company objects containing the structured data.
        """
        pass

    @abstractmethod
    def upload_data(self) -> None:
        pass


    @abstractmethod
    def get_data(self) -> None:
        pass