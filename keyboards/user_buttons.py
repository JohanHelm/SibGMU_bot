from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon import links

news_button = InlineKeyboardButton(
    text='Наши новости!',
    url=links.news_channel
)

services_button = InlineKeyboardButton(
    text='Наши услуги.',
    callback_data='show_all_services'
)

faq_button = InlineKeyboardButton(
    text='Часто задаваемые вопросы.',
    callback_data='show_faq'
)

contacts_button = InlineKeyboardButton(
    text='Контактная информация.',
    callback_data='show_contacts'
)

first_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[news_button, services_button],
                     [faq_button],
                     [contacts_button]]
)
