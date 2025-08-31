import httpx
from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.models import Bot
from sqlalchemy.future import select
from app.services.ai_service import get_gemini_response

router = APIRouter()
TELEGRAM_API_URL = "https://api.telegram.org/bot{token}/sendMessage"

@router.post("/webhook/{token}")
async def process_telegram_update(token: str, request: Request, db: AsyncSession = Depends(get_db)):
    update = await request.json()

    # Botni bazadan topish
    result = await db.execute(select(Bot).where(Bot.telegram_token == token))
    bot = result.scalar_one_or_none()
    if not bot:
        return {"status": "error", "message": "Bot not found"}

    # Xabarni va chat ID'ni olish
    try:
        chat_id = update["message"]["chat"]["id"]
        user_message = update["message"]["text"]
        user_lang_code = update["message"]["from"].get("language_code", bot.default_language)
    except KeyError:
        return {"status": "ok", "message": "Not a text message"}

    # Tilni aniqlash va kerakli bilimlar bazasini tanlash
    lang = "uz" # default
    if "ru" in user_lang_code: lang = "ru"
    if "en" in user_lang_code: lang = "en"

    knowledge_base = getattr(bot, f"knowledge_base_{lang}", None)
    if not knowledge_base: # Agar o'sha tilda baza bo'lmasa, default tilga o'tish
        lang = bot.default_language
        knowledge_base = getattr(bot, f"knowledge_base_{lang}")

    if not knowledge_base: # Agar umuman baza bo'lmasa
         return {"status": "error", "message": "Knowledge base is empty"}

    # Gemini'dan javob olish
    ai_response = await get_gemini_response(knowledge_base, user_message, lang)

    # Telegram'ga javob yuborish
    async with httpx.AsyncClient() as client:
        tg_url = TELEGRAM_API_URL.format(token=bot.telegram_token)
        await client.post(tg_url, json={"chat_id": chat_id, "text": ai_response})

    return {"status": "ok"}