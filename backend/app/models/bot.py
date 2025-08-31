import datetime
import enum
from sqlalchemy import String, DateTime, func, Text, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base

class BotStatus(enum.Enum):
    TRIAL = "TRIAL"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class PlanType(enum.Enum):
    TRIAL = "TRIAL"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"

class Bot(Base):
    __tablename__ = "bots"
    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    telegram_token: Mapped[str] = mapped_column(String, unique=True, index=True)
    knowledge_base_uz: Mapped[str] = mapped_column(Text, nullable=True)
    knowledge_base_ru: Mapped[str] = mapped_column(Text, nullable=True)
    knowledge_base_en: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[BotStatus] = mapped_column(Enum(BotStatus), default=BotStatus.TRIAL)
    plan_type: Mapped[PlanType] = mapped_column(Enum(PlanType), default=PlanType.TRIAL)
    subscription_expires_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    default_language: Mapped[str] = mapped_column(String(2), default='uz')