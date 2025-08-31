from app.core.config import settings

try:
    import google.generativeai as genai
    if settings.GOOGLE_API_KEY:
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        model = None
except Exception:
    model = None

MASTER_PROMPT_TEMPLATE = """Sen mijozlarga yordam beruvchi chatbotsan. Sening vazifang — faqat va faqat quyida berilgan BAZA MA'LUMOTLARI asosida savollarga javob berish. Javobni aniq va qisqa, so'ralgan tilda shakllantir.

Qoidalar:

Javobing faqat berilgan BAZA MA'LUMOTLARI ichida bo'lishi kerak.

Agar savolga javob BAZA MA'LUMOTLARI'da mavjud bo'lmasa, "{language_name}" tilida "Kechirasiz, bu savol bo'yicha menda ma'lumot yo'q" deb javob ber.

O'zingdan hech narsa to'qima va taxmin qilma.

Javobni "{language_name}" tilida berishing SHART.

BAZA MA'LUMOTLARI ({language_name} tilida):
{bot_knowledge_base}
MIJOZNING SAVOLI:
"{user_message}"

Javobing ({language_name} tilida):"""

async def get_gemini_response(knowledge_base: str, user_message: str, lang: str) -> str:
    if model is None:
        error_messages = {
            "uz": "AI xizmati mavjud emas.",
            "ru": "AI сервис недоступен.",
            "en": "AI service is not available."
        }
        return error_messages.get(lang, error_messages["en"])
    
    try:
        prompt = MASTER_PROMPT_TEMPLATE.format(
            language_name=lang,
            bot_knowledge_base=knowledge_base,
            user_message=user_message
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        error_messages = {
            "uz": "AI bilan bog'lanishda xatolik yuz berdi.",
            "ru": "Произошла ошибка при подключении к AI.",
            "en": "An error occurred while connecting to the AI."
        }
        return error_messages.get(lang, error_messages["en"])