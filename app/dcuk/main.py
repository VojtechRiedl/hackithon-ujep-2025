
from fastapi import FastAPI

from app.dcuk.api.mqtt import mqtt_client
from app.dcuk.api.data_mqtt import router as data_mqtt_router

dcuk_api = FastAPI(
    title="DCUK API",
    description="API for DCUK",
    docs_url="/docs",
)

dcuk_api.include_router(data_mqtt_router)