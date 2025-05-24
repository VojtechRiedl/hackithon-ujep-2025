
from fastapi import APIRouter

from app.xdent.dependencies import ReportServiceDependency

from app.xdent.schemas.structured_data import ReportCreate
from app.xdent.schemas.structured_data import Report

router = APIRouter(prefix="/reports")

@router.post(
    "/create",
    response_model=Report
)
def endpoint_create_report( 
    report_service: ReportServiceDependency,
    report_create: ReportCreate
):
    return report_service.create_report(report_create)


@router.post(
    "/{id}",
    status_code=204,
)
def endpoint_update_analysis(
    id: int,
    report_service: ReportServiceDependency
):
    report_service.add_analysis_to_report(id)


