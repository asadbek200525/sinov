from aiogram.dispatcher.filters.state import State,StatesGroup


class Post(StatesGroup):
    post = State()
    message = State()