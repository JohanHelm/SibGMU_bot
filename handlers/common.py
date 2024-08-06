import os
import dotenv
# from datetime import datetime
from aiogram.types import Message #  , #  #CallbackQuery

# from keyboards.four_buttons import keyboard
# from lexicon.messages import main_message
# from services.google_sheets.g_sheets_interaction import GoogleSheetsManager

# dotenv.load_dotenv("secrets/.env")


async def process_start_command(message: Message):
    # await message.answer(start_message, reply_markup=keyboard)
    await message.answer("start_message")

