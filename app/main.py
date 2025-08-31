"""
FastAPI application factory and main application instance.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import api_router
from app.api import auth, telegram
from app.api.endpoints import bots, clients

# Create FastAPI application instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(bots.router, prefix="/bots", tags=["Bots"])
app.include_router(clients.router, prefix="/clients", tags=["Clients"])
app.include_router(telegram.router, prefix="/telegram", tags=["Telegram Webhook"])

@app.get("/")
async def root():
    """
    Root endpoint that provides basic API information.
    """
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}",
        "version": settings.VERSION,
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring.
    """
    return {"status": "healthy", "service": settings.PROJECT_NAME}
