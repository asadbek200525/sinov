from aiogram import types
from aiogram.dispatcher import FSMContext

from states.post import Post
from keyboards.default.adasdd import honor
from loader import dp, bot

@dp.message_handler(text='honor 7a')
async def bot_echo(message: types.Message):
    await Post.message.set()
@dp.message_handler(state=Post.message)
async def bot_echo(message: types.Message,state: FSMContext):
    textt = message.text
    await state.update_data({'textt': textt})

    username = message.from_user.full_name

    matn = f'Ushbu {username} sizga quydagi malumotni yubordi\n\n'

    data = await state.get_data()
    textt = data.get('textt')

    matn += f'Malumot : {textt}\n' \

    await bot.send_message(chat_id=1035757120, text=matn, reply_markup=honor)
    await state.finish()





