
from sqlalchemy.orm import Session
from bs4 import BeautifulSoup

from app.xdent.interfaces.report_repository import IReportRepository

from app.xdent.models.xdent import Report

from app.xdent.schemas.structured_data import ReportCreate

class ReportRepository(IReportRepository):
    def __init__(self, db: Session):
        super().__init__(db)

    def add_analysis_to_report(self, report: Report, analysis: dict) ->  Report | None:
        """
        Add analysis data to a report.
        """

        if not report:
            return None
        
        if report.clear_text is None:
            return None

        report.analysis = analysis
        self.db.commit()
        self.db.refresh(report)
        return report
    
    def get_report(self, report_id: int) -> Report | None:
        """
        Retrieve a report by its ID.
        """
        return self.db.query(Report).filter(Report.id == report_id).first()


    def create_report(self, report_create: ReportCreate) -> Report:
        """
        Create a new report record in the database.
        """
        report = Report(
            date=report_create.date,
            text=report_create.text,
            client_id=report_create.client_id,

            clear_text=BeautifulSoup(report_create.text, "html.parser").get_text(strip=True),
        )

        self.db.add(report)
        self.db.commit()
        self.db.refresh(report)
        
        return report