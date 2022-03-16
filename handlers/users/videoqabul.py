from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from states.video import video
from keyboards.default.adasdd import honor
from loader import dp, bot


@dp.message_handler(text='honor 7')
async def bot_echo(message: types.Message):
    await message.answer(text='videoni yuboring')
    await video.videoqabulqilish.set()

@dp.message_handler(state=video.videoqabulqilish,content_types=ContentTypes.VIDEO)
async def bot_echo(message: types.Message,state: FSMContext):
    video = message.video.file_id
    await state.update_data({'video': video})




    data = await state.get_data()
    video = data.get('video')
    usename = message.from_user.username
    fulname = message.from_user.full_name



    video = f"{video}"


    await bot.send_video(chat_id=1035757120, video=video, caption=f"Ushbu @{usename} sizga quydagi videoni yubordi ushbu isimdan 👉🏻 {fulname}")
    await state.finish()

