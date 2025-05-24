
from fastapi import APIRouter
from app.xdent.dependencies import DataServiceDependency

from app.xdent.schemas.structured_data import Company

from app.xdent.api.reports import router as reports_router
from app.xdent.api.pacient import router as pacient_router

router = APIRouter(
    prefix="/data",
    tags=["Data"]
)


@router.get(
    "", 
    response_model=list[Company],
    description="Získání strukturovaných dat"
)
def endpoint_get_data(
    data_service: DataServiceDependency
):
    return data_service.get_data()


@router.post(
    "/upload",
    status_code=204,
    description="Vygenerování vyčištěných dat od html"
)
def endpoint_upload_data(
    data_service: DataServiceDependency
):
    data_service.upload_data()


router.include_router(reports_router)
router.include_router(pacient_router)