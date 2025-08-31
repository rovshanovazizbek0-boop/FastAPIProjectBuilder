from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.models import Bot, Client
from app.schemas import BotCreate, BotPublic
from app.api.dependencies import get_current_client
from sqlalchemy.future import select

router = APIRouter()

@router.post("/", response_model=BotPublic, status_code=201)
async def create_bot(
    bot_in: BotCreate,
    db: AsyncSession = Depends(get_db),
    current_client: Client = Depends(get_current_client)
):
    """
    Create a new bot for the current client.
    """
    new_bot = Bot(**bot_in.model_dump(), client_id=current_client.id)
    db.add(new_bot)
    await db.commit()
    await db.refresh(new_bot)
    return new_bot

@router.get("/me", response_model=list[BotPublic])
async def get_my_bots(
    db: AsyncSession = Depends(get_db),
    current_client: Client = Depends(get_current_client)
):
    """
    Get all bots owned by the current client.
    """
    result = await db.execute(
        select(Bot).where(Bot.client_id == current_client.id)
    )
    bots = result.scalars().all()
    return bots