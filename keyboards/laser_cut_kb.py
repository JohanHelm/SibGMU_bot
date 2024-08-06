from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


plexiglass_button = InlineKeyboardButton(
    text="Оргстекло.",
    callback_data="material_plexiglass"
)

plywood_button = InlineKeyboardButton(
    text="Фанера.",
    callback_data="material_plywood"
)

mdf_button = InlineKeyboardButton(
    text="MDF.",
    callback_data="material_mdf"
)

cancel_fsm_back_button = InlineKeyboardButton(
    text="Вернуться.",
    callback_data="back"
)

laser_cut_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[plexiglass_button, plywood_button],
                     [mdf_button, cancel_fsm_back_button]]
)
