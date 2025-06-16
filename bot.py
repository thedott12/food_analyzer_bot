import logging
from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_BOT_TOKEN
from utils import analyze_food

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Пришли мне фото блюда или продукта (можно добавить описание), и я расскажу тебе всё о его составе и КБЖУ."
    )

@dp.message_handler(content_types=['photo'])
async def handle_photo(message: types.Message):
    photo = message.photo[-1]
    file_id = photo.file_id
    description = message.caption or ""

    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_url = f"https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{file_path}"

    await message.answer("Анализирую фото, это займёт несколько секунд...")

    try:
        result = await analyze_food(file_url, description)
        await message.answer(result, parse_mode=types.ParseMode.MARKDOWN)
    except Exception as e:
        logging.exception(e)
        await message.answer("Произошла ошибка при анализе. Попробуйте ещё раз позже.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
