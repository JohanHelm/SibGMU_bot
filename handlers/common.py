from aiogram.types import Message

from keyboards.first_kb import first_keyboard
from lexicon.messages import start_message


async def process_start_command(message: Message):
    await message.answer(start_message, reply_markup=first_keyboard)


