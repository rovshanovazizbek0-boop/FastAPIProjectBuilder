from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Basic application settings
    PROJECT_NAME: str = "FastAPI Modern Application"
    PROJECT_DESCRIPTION: str = "A well-structured FastAPI application with modern Python package management"
    VERSION: str = "1.0.0"
    
    # Environment
    ENVIRONMENT: str = "development"
    
    # API settings
    API_V1_STR: str = "/api/v1"
    
    # CORS settings
    ALLOWED_HOSTS: List[str] = ["*"]

    # Database configuration
    DATABASE_URL: str = "sqlite+aiosqlite:///./database.db"

settings = Settings()
