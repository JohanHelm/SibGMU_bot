from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.first_kb import first_keyboard
from keyboards.back_kb import back_keyboard
from keyboards.services_kb import services_keyboard
from keyboards.laser_cut_kb import laser_cut_keyboard
from lexicon.messages import (start_message,
                              service_description_message,
                              faq_message,
                              contacts_message,
                              laser_cut_message)


async def our_services(callback: CallbackQuery):
    await callback.message.edit_text(text=service_description_message,
                                     reply_markup=services_keyboard)


async def laser_cut(callback: CallbackQuery):
    await callback.message.edit_text(text=laser_cut_message,
                                     reply_markup=laser_cut_keyboard)


async def faq(callback: CallbackQuery):
    await callback.message.edit_text(text=faq_message,
                                     reply_markup=back_keyboard)


async def contacts(callback: CallbackQuery):
    await callback.message.edit_text(text=contacts_message,
                                     reply_markup=back_keyboard)


async def go_back(callback: CallbackQuery):
    await callback.message.edit_text(text=start_message,
                                     reply_markup=first_keyboard)


# Этот хэндлер будет срабатывать на команду "/cancel" в любых состояниях,
# кроме состояния по умолчанию, и отключать машину состояний
# @dp.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text='Вы вышли из машины состояний\n\n'
             'Чтобы снова перейти к заполнению анкеты - '
             'отправьте команду /fillform'
    )
    await state.clear()
