from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from .config import settings
import os

# Convert PostgreSQL URL to async format if needed, or fallback to SQLite
database_url = settings.DATABASE_URL
if database_url.startswith('postgresql://'):
    try:
        # Try to use PostgreSQL if available
        import psycopg
        database_url = database_url.replace('postgresql://', 'postgresql+psycopg://', 1)
    except ImportError:
        # Fallback to SQLite if PostgreSQL is not available
        database_url = "sqlite+aiosqlite:///./database.db"
        print("PostgreSQL not available, falling back to SQLite")

engine = create_async_engine(database_url)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session