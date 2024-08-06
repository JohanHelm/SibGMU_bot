from aiogram.types import Message, CallbackQuery

from keyboards.user_buttons import first_keyboard
from lexicon.messages import start_message




async def process_start_command(message: Message):
    await message.answer(start_message, reply_markup=first_keyboard)


