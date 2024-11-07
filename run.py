import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет')

@dp.message(Command('help'))  # Бот ждет ввода команды help и запускает функцию ниже.
async def get_help(message: Message):  # На вход получает команду от хендлера "help" и выводит ответ ниже
    await message.answer('Это команда /help')  # Просто ответ в чате на наш запрос - отвечает 'Это команда /help'

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
