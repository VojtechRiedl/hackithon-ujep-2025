

from fastapi import Depends

from typing import Annotated

from app.xdent.interfaces.data_repository import IDataRepository
from app.xdent.repositories.data_repository import DataRepository

from app.xdent.interfaces.data_service import IDataService
from app.xdent.services.data_service import DataService

from app.xdent.infrastructure.ollama_client import ollama_client, OllamaClient
from app.xdent.infrastructure.database import Database, database

from app.xdent.interfaces.report_repository import IReportRepository
from app.xdent.repositories.report_repository import ReportRepository

from app.xdent.interfaces.report_service import IReportService
from app.xdent.services.report_service import ReportService

from app.xdent.interfaces.ai_repository import IAIRepository
from app.xdent.repositories.ai_repository import AIRepository


from app.xdent.interfaces.pacient_repository import IPacientRepository
from app.xdent.repositories.pacient_repository import PacientRepository

from app.xdent.interfaces.pacient_service import IPacientService
from app.xdent.services.pacient_service import PacientService

from sqlalchemy.orm import Session

from typing import Generator


def get_database() -> Database:
    return database


DatabaseDependency = Annotated[Database, Depends(get_database)]


def get_session(db: DatabaseDependency) -> Generator[Session, None, None]:
    yield from db.get_db()


SessionDependency = Annotated[Session, Depends(get_session)]

def get_ollama_client() -> OllamaClient:
    return ollama_client

OllamaClientDependency = Annotated[
    OllamaClient,
    Depends(get_ollama_client)
]


def get_data_repository(db: SessionDependency) -> IDataRepository:
    return DataRepository(db)


DataRepositoryDependency = Annotated[
    IDataRepository,
    Depends(get_data_repository)
]

def get_data_service(
    data_repository: DataRepositoryDependency
) -> IDataService:
    return DataService(data_repository)


DataServiceDependency = Annotated[
    IDataService,
    Depends(get_data_service)
]


def get_ai_repository(
    ollama_client: OllamaClientDependency
) -> IAIRepository:
    return AIRepository(ollama_client)

AIRepositoryDependency = Annotated[
    IAIRepository,
    Depends(get_ai_repository)
]


def get_report_repository(
    db: SessionDependency,
) -> IReportRepository:
    return ReportRepository(db)


ReportRepositoryDependency = Annotated[
    IReportRepository,
    Depends(get_report_repository)
]


def get_report_service(
    report_repository: ReportRepositoryDependency,
    ai_repository: AIRepositoryDependency
) -> IReportService:
    return ReportService(report_repository, ai_repository)

ReportServiceDependency = Annotated[
    IReportService,
    Depends(get_report_service)
]


def get_pacient_repository(
    db: SessionDependency
) -> IPacientRepository:
    return PacientRepository(db)


PacientRepositoryDependency = Annotated[
    IPacientRepository,
    Depends(get_pacient_repository)
]


def get_pacient_service(
    pacient_repository: PacientRepositoryDependency
) -> IPacientService:
    return PacientService(pacient_repository)


PacientServiceDependency = Annotated[
    IPacientService,
    Depends(get_pacient_service)
]