from pydantic import BaseModel
from app.models.bot import BotStatus, PlanType # Enum'larni modeldan import qilamiz

class BotBase(BaseModel):
    telegram_token: str
    knowledge_base_uz: str | None = None
    knowledge_base_ru: str | None = None
    knowledge_base_en: str | None = None
    default_language: str = 'uz'

class BotCreate(BotBase):
    pass

class BotPublic(BotBase):
    id: int
    status: BotStatus
    plan_type: PlanType

    class Config:
        from_attributes = True