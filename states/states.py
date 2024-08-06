from aiogram.fsm.state import default_state, State, StatesGroup


class FSMChooseService(StatesGroup):
    fill_name = State()
    fill_age = State()
    fill_gender = State()
    upload_photo = State()
    fill_education = State()
    fill_wish_news = State()

