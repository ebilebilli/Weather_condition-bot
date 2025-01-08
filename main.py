import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from settings import TOKEN
from request_system import request_system

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def command_list():
    commands = [
        BotCommand(command='/info', description='Take info about the bot'),
        BotCommand(command='/weather', description='Get weather information')
    ]
    await bot.set_my_commands(commands)

@dp.message(Command('info'))
async def cmd_start(message: Message):
    await message.answer('Welcome! Use /weather "city name" to get the weather information')

@dp.message(Command('weather'))
async def cmd_weather(message: Message):
    city = message.text.split(maxsplit=1)[1].title()
    loop = asyncio.get_event_loop()
    weather_info = await loop.run_in_executor(None, request_system, city)
    
    await message.answer(f'Weather in {city}:\n{weather_info}')

async def main_bot():
    await command_list()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main_bot())
