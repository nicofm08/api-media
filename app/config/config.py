"""This module is responsible for the configuration of the FastAPI application."""

import fastapi
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.solution.exceptions.errors_excepctions import CustomAPIResponse

app = fastapi.FastAPI(
    title="API-MEDIA",
    description="API FastAPI To Manage Data from Media",
    version="1.0.0",
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
