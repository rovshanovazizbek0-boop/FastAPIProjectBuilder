from fastapi import APIRouter, Depends
from app.schemas import ClientPublic
from app.api.dependencies import get_current_client
from app.models import Client

router = APIRouter()

@router.get("/me", response_model=ClientPublic)
def read_users_me(current_user: Client = Depends(get_current_client)):
    return current_user