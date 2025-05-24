
from fastapi import FastAPI

from app.dcuk.api.mqtt import mqtt_client

dcuk_api = FastAPI(
    title="DCUK API",
    description="API for DCUK",
    docs_url="/docs",
)