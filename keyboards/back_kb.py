from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

back_button = InlineKeyboardButton(
    text="Назад.",
    callback_data="go_back"
)

back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[back_button]]
)