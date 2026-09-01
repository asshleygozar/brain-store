from fastapi import APIRouter
from .routers import ingest_router

api_router = APIRouter()

api_router.include_router(ingest_router, prefix='/ingest', tags=['Ingest'])