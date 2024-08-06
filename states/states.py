from aiogram.fsm.state import State, StatesGroup


class FSMService(StatesGroup):
    service = State()
    material = State()
    communication = State()



