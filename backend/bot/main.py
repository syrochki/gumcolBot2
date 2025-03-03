import asyncio
import os
import aiohttp
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, WebAppInfo
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
API_URL = "http://127.0.0.1:8000/api/"  # URL API

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(
                text="📅 Открыть расписание",
                web_app=WebAppInfo(url="---"))
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Привет! Нажми кнопку, чтобы открыть расписание.", reply_markup=keyboard)

# Команда /schedule
@dp.message(Command("schedule"))
async def schedule_handler(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}/lessons/") as response:
            if response.status == 200:
                data = await response.json()
                text = "\n".join([f"{lesson['day']}: {lesson['subject']} - {lesson['teacher']}. Кабинет: {lesson['classroom']}" for lesson in data])
                await message.answer(f"📅 Расписание:\n{text}")
            else:
                await message.answer("Ошибка при получении данных 😢")

# Команда /days
@dp.message(Command("days"))
async def day_handler(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}/days/") as response:
            if response.status == 200:
                data = await response.json()
                text = "\n".join([f"{day['day']}" for day in data])
                await message.answer(f"Дни недели: \n{text}")
            else:
                await message.answer("Ошибка при получении данных 😢")

# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
