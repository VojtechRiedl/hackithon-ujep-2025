

from app.xdent.interfaces.report_service import IReportService


from app.xdent.interfaces.report_repository import IReportRepository
from app.xdent.interfaces.ai_repository import IAIRepository
from app.xdent.schemas.structured_data import ReportCreate, Report

from fastapi import HTTPException

class ReportService(IReportService):
    """
    Service class for handling report-related operations.
    """

    def __init__(self, report_repository: IReportRepository, ai_repository: IAIRepository):
        super().__init__(report_repository, ai_repository)

    def add_analysis_to_report(self, report_id: int) -> None:
        """
        Add analysis data to a report.

        :param report_id: The ID of the report to which the analysis will be added.
        """

        report = self.report_repository.get_report(report_id)
        
        if not report:
            raise HTTPException(detail="Report not found", status_code=404)

        analysis = self.ai_repository.get_xdent_response(report.clear_text)

        if not analysis:
            raise HTTPException(detail="Analysis generation failed", status_code=400)

        # Call the repository method to add analysis to the report
        self.report_repository.add_analysis_to_report(report, analysis)

    def create_report(self, report_create: ReportCreate) -> Report:
        """
        Create a new report.

        :param report_create: The data used to create the report.
        :return: The created report.
        """
        
        # Call the repository method to create a new report
        report = self.report_repository.create_report(report_create)

        if not report:
            raise HTTPException(detail="Report creation failed", status_code=400)

        analysis = self.ai_repository.get_xdent_response(report.clear_text)

        if not analysis:
            raise HTTPException(detail="Analysis generation failed", status_code=400)

        self.report_repository.add_analysis_to_report(report, analysis)

        return report