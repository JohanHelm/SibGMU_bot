from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.back_kb import back_keyboard
from keyboards.first_kb import first_keyboard

from keyboards.services_kb import services_keyboard
from lexicon.messages import (start_message,
                              service_description_message,
                              faq_message,
                              contacts_message,
                              )
from states.states import FSMService


async def our_services(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=service_description_message,
                                     reply_markup=services_keyboard)
    await state.set_state(FSMService.service)


async def faq(callback: CallbackQuery):
    await callback.message.edit_text(text=faq_message,
                                     reply_markup=back_keyboard)


async def contacts(callback: CallbackQuery):
    await callback.message.edit_text(text=contacts_message,
                                     reply_markup=back_keyboard)


async def go_back(callback: CallbackQuery):
    await callback.message.edit_text(text=start_message,
                                     reply_markup=first_keyboard)


async def process_cancel_command_state(callback: CallbackQuery, state: FSMContext):
    print(await state.get_data())
    await state.clear()
    await callback.message.edit_text(text=service_description_message,
                                     reply_markup=services_keyboard)
