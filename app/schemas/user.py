"""
User-related Pydantic schemas for request/response validation.
"""

from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

from app.schemas.base import BaseSchema, TimestampMixin, IDMixin

class UserBase(BaseSchema):
    """
    Base user schema with common user fields.
    """
    email: EmailStr = Field(..., description="User email address")
    name: str = Field(..., min_length=1, max_length=100, description="User full name")
    is_active: bool = Field(default=True, description="Whether the user is active")

class UserCreate(UserBase):
    """
    Schema for creating a new user.
    """
    pass

class UserUpdate(BaseSchema):
    """
    Schema for updating an existing user.
    """
    email: Optional[EmailStr] = Field(None, description="User email address")
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="User full name")
    is_active: Optional[bool] = Field(None, description="Whether the user is active")

class UserResponse(UserBase, IDMixin, TimestampMixin):
    """
    Schema for user responses (includes all fields).
    """
    
    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "email": "user@example.com",
                "name": "John Doe",
                "is_active": True,
                "created_at": "2023-08-31T10:00:00Z",
                "updated_at": "2023-08-31T10:00:00Z"
            }
        }
    }

class UserInDB(UserResponse):
    """
    Schema for user as stored in database (may include additional fields).
    """
    pass
