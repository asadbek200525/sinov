from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery,ContentTypes
from states.post import Post

from loader import dp,db,bot

idlar = db.select_all_user()

for idd in idlar:
    print((idd[4]))
# Echo bot

    @dp.callback_query_handler(text=f'{int(idd[4])}')
    async def bot_echo(message: CallbackQuery,state:FSMContext):
        id = int(message.data)
        await state.update_data({'id':id})
        await message.message.answer(text='habar yuboring')
        await Post.post.set()


    @dp.message_handler(state=Post.post,content_types=ContentTypes.PHOTO)
    async def bot_echo(message: types.Message,state:FSMContext):
        video = message.photo[1].file_id
        datta = await state.get_data()
        id = datta.get('id')
        await bot.send_photo(chat_id=id,photo=video, caption="asadbek")

    @dp.message_handler(state=Post.post,content_types=ContentTypes.VIDEO)
    async def bot_echo(message: types.Message,state:FSMContext):
        video = message.video.file_id
        datta = await state.get_data()
        id = datta.get('id')
        await bot.send_video(chat_id=id,video=video, caption="asadbek")

    @dp.message_handler(state=Post.post)
    async def bot_echo(message: types.Message,state:FSMContext):
        post = message.text
        datta = await state.get_data()
        id = datta.get('id')
        await bot.send_message(chat_id=id,text=post)
        await state.finish()









