import logging
import aiohttp
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from config import TELEGRAM_BOT_TOKEN
from utils import analyze_food

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Пришли мне фото блюда или продукта (можно добавить описание), и я расскажу тебе всё о его составе и КБЖУ."
    )

@dp.message(F.photo)
async def handle_photo(message: types.Message):
    # Получить наибольшее по размеру фото
    photo = message.photo[-1]
    file_id = photo.file_id

    # Получить описание, если есть
    description = message.caption or ""

    # Скачиваем фото во временный файл и получаем direct-URL
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_url = f"https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{file_path}"

    await message.answer("Анализирую фото, это займёт несколько секунд...")

    try:
        result = await analyze_food(file_url, description)
        await message.answer(result, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        logging.exception(e)
        await message.answer("Произошла ошибка при анализе. Попробуйте ещё раз позже.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
