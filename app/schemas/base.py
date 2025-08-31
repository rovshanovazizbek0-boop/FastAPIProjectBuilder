"""
Base schemas for common functionality.
"""

from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class BaseSchema(BaseModel):
    """
    Base schema with common configuration.
    """
    
    class Config:
        """
        Pydantic configuration for all schemas.
        """
        # Allow population by field name and alias
        allow_population_by_field_name = True
        # Use enum values instead of enum names
        use_enum_values = True
        # Validate assignment
        validate_assignment = True
        # Allow arbitrary types
        arbitrary_types_allowed = True

class TimestampMixin(BaseModel):
    """
    Mixin for schemas that include timestamp fields.
    """
    created_at: datetime
    updated_at: datetime

class IDMixin(BaseModel):
    """
    Mixin for schemas that include ID field.
    """
    id: UUID
