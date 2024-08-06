from aiogram.types import CallbackQuery

from keyboards.first_kb import first_keyboard
from keyboards.back_kb import back_keyboard
from keyboards.services_kb import services_keyboard
from lexicon.messages import (start_message,
                              service_description_message,
                              faq_message,
                              contacts_message)


async def our_services(callback: CallbackQuery):
    # await callback.bot.delete_message(callback.from_user.id, callback.message.message_id)
    # await callback.message.answer(text=f"{a2_value}\n\n{main_message}", reply_markup=keyboard)
    await callback.message.edit_text(text=service_description_message, reply_markup=services_keyboard)


async def faq(callback: CallbackQuery):
    await callback.message.edit_text(text=faq_message, reply_markup=back_keyboard)


async def contacts(callback: CallbackQuery):
    await callback.message.edit_text(text=contacts_message, reply_markup=back_keyboard)


async def go_back(callback: CallbackQuery):
    await callback.message.edit_text(start_message, reply_markup=first_keyboard)
