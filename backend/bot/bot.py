import asyncio
import aiohttp
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
API_URL = "http://127.0.0.1:8000/api/lessons/"  # URL API

bot = Bot(token=TOKEN) # type: ignore
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я бот с расписанием 📅. Введи /schedule для просмотра.")

# Команда /schedule
@dp.message(Command("schedule"))
async def schedule_handler(message: Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            if response.status == 200:
                data = await response.json()
                text = "\n".join([f"{lesson['day']['name']}: {lesson['teacher']['name']} - {lesson['group']['name']}" for lesson in data])
                await message.answer(f"📅 Расписание:\n{text}")
            else:
                await message.answer("Ошибка при получении данных 😢")

# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
