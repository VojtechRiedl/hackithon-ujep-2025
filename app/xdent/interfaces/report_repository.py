

from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from app.xdent.models.xdent import Report

from app.xdent.schemas.structured_data import ReportCreate

class IReportRepository(ABC):
    """
    Interface for report repository classes.
    """

    def __init__(self, db: Session):
        self.db = db

    @abstractmethod
    def get_report(self, report_id: int) -> Report | None:
        """
        Retrieve a report by its ID.

        :param report_id: The ID of the report to retrieve.
        :return: The report if found, otherwise None.
        """
        pass
    
    @abstractmethod
    def add_analysis_to_report(self, report: Report, analysis: dict) ->  Report | None:
        """
        Add analysis data to a report.

        :param report: The report to which the analysis will be added.
        """
        pass


    @abstractmethod
    def create_report(self, report_create: ReportCreate) -> Report:
        """
        Create a new report.

        :param report_create: The data used to create the report.
        :return: The created report.
        """
        pass