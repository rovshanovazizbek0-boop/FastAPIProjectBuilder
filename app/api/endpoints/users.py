"""
User API endpoints.
"""

from typing import List
from fastapi import APIRouter, HTTPException, Depends
from uuid import UUID

from app.schemas.client import ClientCreate, ClientPublic
from app.services.user_service import UserService

router = APIRouter()

def get_user_service() -> UserService:
    """
    Dependency to get user service instance.
    """
    return UserService()

@router.post("/", response_model=ClientPublic)
async def create_user(
    user_data: ClientCreate,
    user_service: UserService = Depends(get_user_service)
):
    """
    Create a new user.
    """
    try:
        user = await user_service.create_user(user_data)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[ClientPublic])
async def get_users(
    skip: int = 0,
    limit: int = 10,
    user_service: UserService = Depends(get_user_service)
):
    """
    Get list of users with pagination.
    """
    users = await user_service.get_users(skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=ClientPublic)
async def get_user(
    user_id: UUID,
    user_service: UserService = Depends(get_user_service)
):
    """
    Get a specific user by ID.
    """
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=ClientPublic)
async def update_user(
    user_id: UUID,
    user_data: ClientCreate,
    user_service: UserService = Depends(get_user_service)
):
    """
    Update a specific user.
    """
    try:
        user = await user_service.update_user(user_id, user_data)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{user_id}")
async def delete_user(
    user_id: UUID,
    user_service: UserService = Depends(get_user_service)
):
    """
    Delete a specific user.
    """
    success = await user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
