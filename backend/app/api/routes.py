"""
Main API router that combines all API endpoints.
"""

from fastapi import APIRouter

from app.api import health
from app.api.endpoints import users

# Create main API router
api_router = APIRouter()

# Include health check routes
api_router.include_router(
    health.router,
    prefix="/health",
    tags=["health"]
)

# Include user routes
api_router.include_router(
    users.router,
    prefix="/users",
    tags=["users"]
)
