
from app.xdent.interfaces.data_repository import IDataRepository

import json

from pathlib import Path
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session

from app.xdent.models.xdent import Client, Report, Company

from sqlalchemy import select

from datetime import datetime


class DataRepository(IDataRepository):
    """
    Implementation of the IDataRepository interface.
    """

    def __init__(self, db: Session):
        super().__init__(db)

    def get_structured_data(self) -> list[dict]:
        """
        Retrieve structured data from the repository.
        """
        
        return self._get_data_from_file("app/xdent/sources/structured_output.json")

    def get_data_from_database(self) -> list[Company]:
        return self.db.execute(select(Company)).scalars().all()

    def upload_data_to_database(self, companies_data: list[dict]):

        for company_data in companies_data:
            # Vytvoření a přidání společnosti
            company = Company(name=company_data["idCompany"])
            self.db.add(company)
            self.db.flush()  # získáme company.id pro ForeignKey

            for client_data in company_data.get("clients", []):
                client = Client(
                    name=client_data["firstname"],
                    surname=client_data["lastname"],
                    company_id=company.id,
                )
                self.db.add(client)
                self.db.flush()

                for report_data in client_data.get("reports", []):
                    report = Report(
                        date=datetime.strptime(report_data["datetime"], "%Y-%m-%d %H:%M"),
                        text=report_data["text"],
                        clear_text=BeautifulSoup(report_data.get("text", ""), "html.parser").get_text(strip=True),
                        client_id=client.id,
                    )
                    self.db.add(report)

            self.db.commit()

    def _get_data_from_file(self, file_path: str) -> list[dict]:
        """
        Helper method to read data from a JSON file.
        """
        with Path(file_path).open("r", encoding="utf-8") as file:
            return json.load(file)
