from fastapi import APIRouter, Depends
from .routers import ingest_router, admin_router

api_router = APIRouter()

api_router.include_router(ingest_router, prefix='/ingest', tags=['Ingest'])
api_router.include_router(admin_router, prefix='/admin', tags=['Admin'])