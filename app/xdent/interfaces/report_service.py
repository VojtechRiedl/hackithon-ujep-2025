

from abc import ABC, abstractmethod

from app.xdent.interfaces.report_repository import IReportRepository
from app.xdent.interfaces.ai_repository import IAIRepository
from app.xdent.schemas.structured_data import ReportCreate, Report


class IReportService(ABC):
    """
    Interface for report service classes.
    """

    def __init__(self, report_repository: IReportRepository, ai_repository: IAIRepository):
        self.report_repository = report_repository
        self.ai_repository = ai_repository

    @abstractmethod
    def add_analysis_to_report(self, report_id: int) -> None:
        """
        Add analysis data to a report.

        :param report_id: The ID of the report to which the analysis will be added.
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
