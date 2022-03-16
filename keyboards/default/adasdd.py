from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

honor = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='honor 3'),
            KeyboardButton(text='honor 7')
        ],
        [
            KeyboardButton(text='honor 7a'),
            KeyboardButton(text='honor 7x')
        ],
        [
            KeyboardButton(text='honor 8s'),
            KeyboardButton(text='honor 8a')
        ],
        [
            KeyboardButton(text='honor 8x'),
            KeyboardButton(text='honor 9a')
        ],
        [
            KeyboardButton(text='honor 9c'),
            KeyboardButton(text='honor 9 Lite')
        ],
        [
            KeyboardButton(text='hono 10 Lite'),
            KeyboardButton(text='honor 20')
        ],
        [
            KeyboardButton(text='honor 20 Pro')
        ],
        [
            KeyboardButton(text='🔙bacck')
        ]
    ],
    resize_keyboard=True
)