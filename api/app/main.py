from fastapi import FastAPI

from app.core.config import settings
from app.routers.health import router as health_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI-Powered Cyber Investigation Platform"
)

app.include_router(health_router)

@app.get("/")
def root():
    return {
        "project": settings.PROJECT_NAME,
        "status": "Backend Running"
    }