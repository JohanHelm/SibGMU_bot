from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.laser_cut_kb import laser_cut_keyboard
from keyboards.application_kb import application_keyboard
from lexicon.messages import (laser_cut_message,
                              application_message
                              )
from states.states import FSMService


async def laser_cut(callback: CallbackQuery, state: FSMContext):
    await state.update_data(service=callback.data)
    await callback.message.edit_text(text=laser_cut_message,
                                     reply_markup=laser_cut_keyboard)
    await state.set_state(FSMService.material)


async def material_plexiglass(callback: CallbackQuery, state: FSMContext):
    await state.update_data(material=callback.data)
    await callback.message.edit_text(text=application_message,
                                     reply_markup=application_keyboard)
    await state.set_state(FSMService.communication)
