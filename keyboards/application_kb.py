from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


telegram_button = InlineKeyboardButton(
    text="Telegram.",
    callback_data="telegram_communication"
)

phone_button = InlineKeyboardButton(
    text="Телефон.",
    callback_data="phone_communication"
)

email_button = InlineKeyboardButton(
    text="Электронная почта.",
    callback_data="email_communication"
)

cancel_fsm_back_button = InlineKeyboardButton(
    text="Вернуться.",
    callback_data="back"
)

application_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[telegram_button, phone_button],
                     [email_button, cancel_fsm_back_button]]
)
