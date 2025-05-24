
from pydantic import BaseModel, Field, ConfigDict

from datetime import datetime

from typing import Any


class Report(BaseModel):
    """
    Report model for Xdent.
    """
    id: int = Field(..., description="Unique identifier for the report")
    date: datetime = Field(..., description="Date and time of the report")
    text: str = Field(..., description="Text content of the report")
    clear_text: str | None = Field(..., description="")
    analysis: dict[str, Any] | None = Field(..., description="")

    model_config = ConfigDict(from_attributes=True)


class Client(BaseModel):
    """
    Client model for Xdent.
    """
    id: int = Field(..., description="Unique identifier for the client")
    name: str = Field(..., description="Name of the client")
    surname: str = Field(..., description="Surname of the client")
    reports: list[Report] = Field(..., description="List of reports associated with the client")

    model_config = ConfigDict(from_attributes=True)
    

class Company(BaseModel):
    """
    Company model for Xdent.
    """
    id: int = Field(..., description="Unique identifier for the company")
    name: str = Field(..., description="Company name")
    clients: list[Client] = Field(..., description="List of clients associated with the company")
    
    model_config = ConfigDict(from_attributes=True)


class ReportCreate(BaseModel):
    """
    RecordCreate model for Xdent.
    """
    client_id: int = Field(..., description="ID of the client associated with the report")
    date: datetime = Field(..., description="Date and time of the report")
    text: str = Field(..., description="Text content of the report")

    model_config = ConfigDict(from_attributes=True)