
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.dcuk.main import dcuk_api
from app.xdent.main import xdent_api

from contextlib import asynccontextmanager

from app.xdent.infrastructure.database import database
from app.xdent.models.xdent import BASE
from app.dcuk.infrastructure.mqtt_client import mqtt_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    database.create_all()
    await mqtt_client.connect()
    yield
    await mqtt_client.disconnect()


app = FastAPI(
    title="API",
    description="API",
    docs_url="/docs",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/dcuk", dcuk_api)
app.mount("/xdent", xdent_api)