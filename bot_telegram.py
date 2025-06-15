import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from app.handl import router

async def main():
    bot=Bot(token='7828554954:AAFrjOeHk6GoI_5pRCs3mwvZpvgjN6LaFHg')
    dp=Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
if __name__=='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:####
        print('bot turn-of')