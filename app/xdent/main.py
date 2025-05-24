from fastapi import FastAPI

from app.xdent.api.routers import router as data_router

xdent_api = FastAPI(
    title="Xdent API",
    description="API for Xdent",
    docs_url="/docs",
)


xdent_api.include_router(data_router)