import os

import dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.register import register_common, register_user_handlers


async def start_bot():
    dotenv.load_dotenv("secrets/.env")
    storage = MemoryStorage()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher(storage=storage)
    register_common(dp)
    register_user_handlers(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
