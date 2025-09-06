import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

logging.basicConfig(level=logging.INFO)

bot = Bot(token='TOKEN')

dp = Dispatcher()


kb_currency = [
    [types.KeyboardButton(text='🇺🇸 USD'), types.KeyboardButton(text='🇰🇿 KZT')],
    [types.KeyboardButton(text='🪙 BTC'), types.KeyboardButton(text='🔷 ETH')]    
]

@dp.message(Command('start'))
async def start(message: types.Message):
    keyboard_currency = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb_currency)
    await message.answer('Hi', reply_markup=keyboard_currency)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
