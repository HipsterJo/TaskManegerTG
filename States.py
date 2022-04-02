from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    timing = State()
    note = State()


