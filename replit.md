# FastAPI Modern Application

## Overview

This is a modern FastAPI application built as a SaaS platform for creating and managing multilingual Telegram chatbots powered by Google's Gemini AI. The platform allows clients to register, create AI-powered bots with custom knowledge bases in multiple languages (Uzbek, Russian, English), and deploy them via Telegram webhooks. The application follows clean architecture principles with clear separation between API, service, and data layers.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Application Structure
The application follows a layered architecture pattern with clear separation of concerns:

- **API Layer**: FastAPI routers handling HTTP requests and responses with automatic OpenAPI documentation
- **Service Layer**: Business logic implementation with async/await support for AI integration
- **Data Layer**: SQLAlchemy models with Alembic migrations for database schema management
- **Schema Layer**: Pydantic models for request/response validation and serialization

### Core Components

**FastAPI Application Factory**
- Centralized application configuration with CORS middleware support
- Modular router inclusion system organizing endpoints by domain (auth, bots, clients, webhooks)
- Environment-based configuration using Pydantic BaseSettings
- Comprehensive health monitoring endpoints for container orchestration

**Authentication & Authorization**
- JWT token-based authentication using python-jose
- Secure password hashing with bcrypt via passlib
- OAuth2 password bearer token scheme for API protection
- Dependency injection for current user authentication in protected endpoints

**Database Architecture**
- Async SQLAlchemy with PostgreSQL support (configurable database URL)
- Alembic migrations for schema version control
- Two main entities: Clients (platform users) and Bots (AI chatbots)
- Proper foreign key relationships and enum types for status management

**Multi-language Bot System**
- Bots support three languages: Uzbek (uz), Russian (ru), and English (en)
- Separate knowledge bases per language with fallback to default language
- Language detection from Telegram user preferences
- Configurable default language per bot

**AI Integration Architecture**
- Google Gemini AI integration for intelligent responses
- Master prompt template system for consistent AI behavior
- Async AI service layer with error handling and fallback responses
- Knowledge base-driven responses ensuring AI stays within defined boundaries

**Webhook Processing System**
- Dynamic webhook endpoints using bot tokens as URL parameters
- Real-time message processing from Telegram
- Language detection and appropriate knowledge base selection
- Async HTTP client for Telegram API responses

### Data Models

**Client Model**
- Company information, email-based authentication
- Language preferences and account creation tracking
- One-to-many relationship with Bot entities

**Bot Model**
- Telegram bot token management with unique constraints
- Multi-language knowledge bases (uz/ru/en)
- Status and plan type management (TRIAL/ACTIVE/INACTIVE)
- Subscription expiration tracking for SaaS billing

### API Design Patterns

**RESTful Endpoint Organization**
- Versioned API with `/api/v1` prefix
- Domain-specific routers (auth, bots, clients, telegram)
- Consistent response schemas using Pydantic models
- Proper HTTP status codes and error handling

**Security Implementation**
- Protected endpoints using JWT token dependency injection
- Password validation and secure hashing
- Token expiration management (7-day default)
- Cross-origin resource sharing (CORS) configuration

## External Dependencies

### Core Framework & Database
- **FastAPI**: Modern Python web framework with automatic API documentation
- **SQLAlchemy**: Async ORM for database operations with PostgreSQL support
- **Alembic**: Database migration management system
- **Psycopg**: PostgreSQL database driver for async operations

### Authentication & Security
- **Passlib[bcrypt]**: Secure password hashing library
- **Python-jose[cryptography]**: JWT token creation and validation
- **Python-multipart**: Form data parsing for OAuth2 authentication

### AI & External APIs
- **Google Generative AI**: Gemini AI model integration for intelligent responses
- **HTTPX**: Async HTTP client for Telegram API communication

### Development & Deployment
- **UV**: Modern Python package manager for fast dependency resolution
- **Uvicorn**: ASGI server for development and production deployment
- **Gunicorn**: Production WSGI server with Uvicorn workers

### Environment Configuration
- **Pydantic-settings**: Type-safe configuration management with environment variable support
- **PostgreSQL Database**: Primary data storage (configurable via DATABASE_URL)
- **Google API Key**: Required for Gemini AI integration
- **JWT Secret Key**: Cryptographic key for token signing and validation