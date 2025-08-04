"""This module is responsible for the configuration of the FastAPI application."""

import fastapi
from contextlib import asynccontextmanager
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.solution.exceptions.errors_excepctions import CustomAPIResponse
from app.core.logger_custom import log

@asynccontextmanager
async def lifespan(app):
    """Lifespan event handler for startup and shutdown events."""
    # Startup
    log.info("🔥 Endpoints available:")
    routes = [f"➡️  {route.path} [{', '.join(route.methods)}]" for route in app.routes]
    for route in routes:
        log.info(f"{route}")
    yield

app = fastapi.FastAPI(
    title="API-MEDIA",
    description="API FastAPI To Manage Data from Media",
    version="1.0.0",
    lifespan=lifespan,
)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(CustomAPIResponse)
async def custom_exception_handler(request: Request, exc: CustomAPIResponse):
    return JSONResponse(status_code=exc.status_code, content=exc.detail)
