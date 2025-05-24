

from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, JSON
from sqlalchemy.orm import relationship



from app.xdent.infrastructure.database import database


BASE = database.Base

class Company(BASE):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    clients = relationship("Client", back_populates="company")


class Client(BASE):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)

    company = relationship("Company", back_populates="clients")

    reports = relationship("Report", back_populates="client")


class Report(BASE):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False)
    text = Column(Text, nullable=False)
    clear_text = Column(Text, nullable=True)
    analysis = Column(JSON, nullable=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)

    client = relationship("Client", back_populates="reports")
