
from app.xdent.interfaces.data_service import IDataService
from app.xdent.interfaces.data_repository import IDataRepository


from app.xdent.schemas.structured_data import Company

class DataService(IDataService):
    def __init__(self, data_repository: IDataRepository):
        super().__init__(data_repository)
    
    def get_structured_data(self) -> list[Company]:
        return self.data_repository.get_structured_data()

    def upload_data(self) -> None:
        """
        Upload the data to the database.
        """

        data = self.data_repository.get_structured_data()

        self.data_repository.upload_data_to_database(data)

    def get_data(self) -> list[Company]:
        return self.data_repository.get_data_from_database()