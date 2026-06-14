from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(prefix="/api", tags=["System"])


@router.get("/status")
def status():
    return {
        "status": "online"
    }


@router.get("/version")
def version():
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION
    }


@router.get("/system")
def system():
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "database": "connected"
    }