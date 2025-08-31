"""
Health check API endpoints.
"""

from fastapi import APIRouter
from datetime import datetime

from app.core.config import settings

router = APIRouter()

@router.get("/")
async def health_check():
    """
    Detailed health check endpoint.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT
    }

@router.get("/ready")
async def readiness_check():
    """
    Readiness check endpoint for container orchestration.
    """
    return {
        "status": "ready",
        "timestamp": datetime.utcnow().isoformat(),
        "service": settings.PROJECT_NAME
    }

@router.get("/live")
async def liveness_check():
    """
    Liveness check endpoint for container orchestration.
    """
    return {
        "status": "alive",
        "timestamp": datetime.utcnow().isoformat(),
        "service": settings.PROJECT_NAME
    }
