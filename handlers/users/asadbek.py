# from aiogram import types
# from aiogram.dispatcher import FSMContext
#
# from states.holatlar import Forma
# from keyboards.default.tolov import tola
# from keyboards.default.kunlari import bekor
# from keyboards.default.almz import almaz
# from keyboards.default.almazlar import asosiy_tugma
# from keyboards.default.tasdiqlash import asosiy
# from loader import dp, bot
#
#
# @dp.message_handler(text='Almaz💎')
# async def bot_echo(message: types.Message):
#     await message.answer(text='Almaz💎 sotib olish uchun ariza berish \n\nIsm Familyangizni Kiriting:',reply_markup=bekor)
#     await Forma.ism_fam.set()
# @dp.message_handler(state=Forma.ism_fam,text='Bekor qilish')
# async def bot_echo(message: types.Message,state: FSMContext):
#     await message.answer(text='Almaz💎 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
#     await state.finish()
#
# @dp.message_handler(state=Forma.ism_fam)
# async def bot_echo(message: types.Message,state: FSMContext):
#     ism = message.text
#     await state.update_data({'ism': ism})
#     await message.answer(text='Yoshingiz kiriting',reply_markup=bekor)
#     await Forma.yosh.set()
# @dp.message_handler(state=Forma.yosh,text='Bekor qilish')
# async def bot_echo(message: types.Message,state: FSMContext):
#     await message.answer(text='Almaz💎 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
#     await state.finish()
# @dp.message_handler(state=Forma.yosh)
# async def bot_echo(message: types.Message,state : FSMContext):
#     yosh = message.text
#     await state.update_data({'yosh':yosh})
#     await message.answer(text='Qancha almaz kerak\nOzingiz hohishingizga qarab kiritishingiz mumkun',reply_markup=almaz)
#     await Forma.almaz.set()
# @dp.message_handler(state=Forma.almaz,text='Bekor qilish')
# async def bot_echo(message: types.Message,state: FSMContext):
#     await message.answer(text='Almaz💎 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
#     await state.finish()
# @dp.message_handler(state=Forma.almaz)
# async def bot_echo(message: types.Message,state : FSMContext):
#     almaz = message.text
#     await state.update_data({"almaz":almaz})
#
#     await message.answer(text="To'lo'v turini kiriting",reply_markup=tola)
#     await  Forma.tolov.set()
# @dp.message_handler(state=Forma.tolov,text='Bekor qilish')
# async def bot_echo(message: types.Message,state: FSMContext):
#     await message.answer(text='Almaz💎 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
#     await state.finish()
#
#
# @dp.message_handler(state=Forma.tolov)
# async def bot_echo(message: types.Message,state : FSMContext):
#     tolov = message.text
#     await state.update_data({'tolov': tolov})
#     await message.answer(text='Free Fire idingizni kiriting',reply_markup=bekor)
#     await Forma.Freeid.set()
# @dp.message_handler(state=Forma.Freeid,text='Bekor qilish')
# async def bot_echo(message: types.Message,state: FSMContext):
#     await message.answer(text='Almaz💎 sotib olish uchun ariza bekor qilindi', reply_markup=asosiy)
#     await state.finish()
#
# @dp.message_handler(state=Forma.Freeid)
# async def bot_echo(message: types.Message,state : FSMContext):
#     Freeid = message.text
#     await state.update_data({"Freeid":Freeid})
#
#     data = await state.get_data()
#     ism = data.get('ism')
#     yosh = data.get('yosh')
#     almaz = data.get('almaz')
#     tolov = data.get('tolov')
#     Freeid = data.get('Freeid')
#
#     matn = f"Almaz💎: \n\n👤Ismingiz :{ism}\n"\
#            f"📅Yoshingiz : {yosh}\n"\
#            f"💎Almaz : {almaz}\n"\
#            f"💰Tolov :{tolov}\n"\
#            f"🎮Id_Free Fire :{Freeid}\n"\
#
#     await message.answer(text=f'{matn}\nAgar barchasi togri bolsa Tasdiqlashni bosing danaterlarimiz ozi siz bilan boglanishadi',reply_markup=asosiy_tugma)
#     await Forma.tasdiqlash.set()
#
# @dp.message_handler(state=Forma.tasdiqlash, text='Bekor qilish')
# async def bot_echo(message: types.Message, state: FSMContext):
#     await message.answer(text='Bekor qilindi',reply_markup=asosiy)
#     await state.finish()
#
# @dp.message_handler(state=Forma.tasdiqlash, text='Tasdiqlash')
# async def bot_echo(message: types.Message, state: FSMContext):
#     await message.answer(text='Adminga yuborildi yaqin vaqt ichida danaterlarimiz siz bilan boglanishadi')
#
#     username = message.from_user.username
#
#     matn = f'Ushbu @{username} sizga quydagi malumotni yubordi\n'
#
#     data = await state.get_data()
#     ism = data.get('ism')
#     yosh = data.get('yosh')
#     almaz = data.get('almaz')
#     tolov = data.get('tolov')
#     Freeid = data.get('Freeid')
#
#
#     matn +=f'ISMI : {ism}\n'\
#            f'YOSHI : {yosh}\n'\
#            f'ALMAZ : {almaz}\n'\
#            f'TOLOV : {tolov}\n'\
#            f'FREE id : {Freeid}\n'\
#
#     await message.answer(text='🔎', reply_markup=asosiy)
#     await bot.send_message(chat_id=1035757120, text=matn, reply_markup=asosiy)
#     await state.finish()
#
#
