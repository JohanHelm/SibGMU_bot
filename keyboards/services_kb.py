from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


laser_cut_button = InlineKeyboardButton(
    text="Лазерная резка.",
    callback_data="laser_cut_service"
)

software_dev_button = InlineKeyboardButton(
    text="Разработка П/О.",
    callback_data="software_dev_service"
)

three_d_print_button = InlineKeyboardButton(
    text="3D печать.",
    callback_data="three_d_print_service"
)

bot_dev_button = InlineKeyboardButton(
    text="Разработка чат-ботов.",
    callback_data="bot_dev_service"
)

three_d_modeling_button = InlineKeyboardButton(
    text="3D моделирование.",
    callback_data="three_d_modeling_service"
)

three_d_scan_button = InlineKeyboardButton(
    text="3D сканирование.",
    callback_data="three_d_scan_service"
)

engraving_button = InlineKeyboardButton(
    text="Гравировка.",
    callback_data="engraving_service"
)

back_button = InlineKeyboardButton(
    text="Назад.",
    callback_data="go_back"
)

services_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[laser_cut_button, three_d_print_button],
                     [three_d_modeling_button, three_d_scan_button],
                     [software_dev_button, engraving_button],
                     [bot_dev_button, back_button]
                     ]
)
