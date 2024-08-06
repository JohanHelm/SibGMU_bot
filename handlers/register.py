from aiogram import Dispatcher
from aiogram import F
from aiogram.filters import Command

from handlers.common import process_start_command
from handlers.user_handlers import our_services, faq, go_back, contacts


def register_common(dp: Dispatcher):
    dp.message.register(process_start_command, Command(commands="start"))


def register_user_handlers(dp: Dispatcher):
    dp.callback_query.register(our_services, F.data == "show_all_services")
    dp.callback_query.register(faq, F.data == "show_faq")
    dp.callback_query.register(contacts, F.data == "show_contacts")
    dp.callback_query.register(go_back, F.data == "go_back")

