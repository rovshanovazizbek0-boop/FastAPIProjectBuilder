"""
Application configuration settings.
"""

import os
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application settings with environment variable support.
    """
    
    # Basic application settings
    PROJECT_NAME: str = "FastAPI Modern Application"
    PROJECT_DESCRIPTION: str = "A well-structured FastAPI application with modern Python package management"
    VERSION: str = "1.0.0"
    
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    # API settings
    API_V1_STR: str = "/api/v1"
    
    # CORS settings
    ALLOWED_HOSTS: List[str] = ["*"]
    
    # Security settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here-change-in-production")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # Database settings (for future use)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    
    # External API settings
    EXTERNAL_API_KEY: str = os.getenv("EXTERNAL_API_KEY", "default-api-key")
    
    # Logging settings
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    class Config:
        """
        Pydantic configuration for settings.
        """
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create global settings instance
settings = Settings()
