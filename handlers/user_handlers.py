from aiogram.types import Message, CallbackQuery
from lexicon.messages import service_description_message


async def our_services(callback: CallbackQuery):
    # await callback.bot.delete_message(callback.from_user.id, callback.message.message_id)
    # await callback.message.answer(text=f"{a2_value}\n\n{main_message}", reply_markup=keyboard)
    await callback.message.edit_text(text=service_description_message ) #, reply_markup=keyboard)