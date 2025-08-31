"""
User data models.
"""

from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from dataclasses import dataclass, field

@dataclass
class User:
    """
    User data model representing a user entity.
    """
    id: UUID = field(default_factory=uuid4)
    email: str = ""
    name: str = ""
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    
    def __post_init__(self):
        """
        Post-initialization processing.
        """
        if not self.email:
            raise ValueError("Email is required")
        if not self.name:
            raise ValueError("Name is required")
    
    def update(self, **kwargs) -> None:
        """
        Update user attributes and set updated_at timestamp.
        """
        for key, value in kwargs.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()
    
    def to_dict(self) -> dict:
        """
        Convert user to dictionary representation.
        """
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
