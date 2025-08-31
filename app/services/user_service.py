"""
User service layer for business logic.
"""

from typing import List, Optional
from uuid import UUID
import asyncio

from app.models.client import Client
from app.schemas.client import ClientCreate, ClientPublic

class UserService:
    """
    User service for handling user-related business logic.
    """
    
    def __init__(self):
        """
        Initialize user service with in-memory storage.
        Note: In a real application, this would connect to a database.
        """
        self._users: dict[UUID, Client] = {}
    
    async def create_user(self, user_data: ClientCreate) -> ClientPublic:
        """
        Create a new user.
        
        Args:
            user_data: User creation data
            
        Returns:
            Created user response
            
        Raises:
            ValueError: If email already exists
        """
        # Check if email already exists
        existing_user = await self._get_user_by_email(user_data.email)
        if existing_user:
            raise ValueError(f"User with email {user_data.email} already exists")
        
        # Create new user
        user = Client(
            email=user_data.email,
            company_name=user_data.company_name,
            password_hash=user_data.password,  # In real app, hash this
            language_preference=user_data.language_preference
        )
        
        # Store user
        self._users[user.id] = user
        
        # Return user response
        return self._user_to_response(user)
    
    async def get_users(self, skip: int = 0, limit: int = 10) -> List[ClientPublic]:
        """
        Get list of users with pagination.
        
        Args:
            skip: Number of users to skip
            limit: Maximum number of users to return
            
        Returns:
            List of user responses
        """
        users = list(self._users.values())
        paginated_users = users[skip:skip + limit]
        return [self._user_to_response(user) for user in paginated_users]
    
    async def get_user_by_id(self, user_id: UUID) -> Optional[ClientPublic]:
        """
        Get user by ID.
        
        Args:
            user_id: User ID
            
        Returns:
            User response if found, None otherwise
        """
        user = self._users.get(user_id)
        if user:
            return self._user_to_response(user)
        return None
    
    async def update_user(self, user_id: UUID, user_data: ClientCreate) -> Optional[ClientPublic]:
        """
        Update user by ID.
        
        Args:
            user_id: User ID
            user_data: User update data
            
        Returns:
            Updated user response if found, None otherwise
            
        Raises:
            ValueError: If email already exists for another user
        """
        user = self._users.get(user_id)
        if not user:
            return None
        
        # Check email uniqueness if email is being updated
        if user_data.email and user_data.email != user.email:
            existing_user = await self._get_user_by_email(user_data.email)
            if existing_user and existing_user.id != user_id:
                raise ValueError(f"User with email {user_data.email} already exists")
        
        # Update user
        update_dict = user_data.dict(exclude_unset=True)
        user.update(**update_dict)
        
        return self._user_to_response(user)
    
    async def delete_user(self, user_id: UUID) -> bool:
        """
        Delete user by ID.
        
        Args:
            user_id: User ID
            
        Returns:
            True if user was deleted, False if not found
        """
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False
    
    async def _get_user_by_email(self, email: str) -> Optional[Client]:
        """
        Get user by email address.
        
        Args:
            email: Email address
            
        Returns:
            User if found, None otherwise
        """
        for user in self._users.values():
            if user.email == email:
                return user
        return None
    
    def _user_to_response(self, user: Client) -> ClientPublic:
        """
        Convert User model to UserResponse schema.
        
        Args:
            user: User model
            
        Returns:
            User response schema
        """
        return ClientPublic(
            id=user.id,
            email=user.email,
            company_name=user.company_name,
            language_preference=user.language_preference
        )
