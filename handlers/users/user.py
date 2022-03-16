from aiogram import types
from loader import dp,bot
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

# Echo bot
@dp.message_handler(text = "honor 3")
async def bot_echo(message: types.Message):
    a = message.from_user.full_name
    idd = message.from_user.id
    print((idd))
    await bot.send_message(chat_id=1035757120, text=f'ushbu foydalanuvchi {a}',reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Xabar yuborish',callback_data=f'{idd}')
            ]
        ]
    ))





