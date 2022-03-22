from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.toha_keybord import (toha_keybords,
toha_keybord1,toha_keybord2,toha_keybord3,toha_keybord4,toha_keybord5,
toha_keybord6,toha_keybord7,toha_keybord8,toha_keybord9)
from keyboards.inline.callback_data import toha_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Toha')
async def show_toha(message: Message):
    await message.answer(f"<b>Toha surasini oyatlarini tanlang</b>",reply_markup=toha_keybord1)

@dp.callback_query_handler(toha_callback_data.filter())
async def show_toha(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=toha_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Toha</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(20,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(20,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Toha surasini oyatlarini tanlang</b>", reply_markup=toha_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Toha surasini oyatlarini tanlang</b>", reply_markup=toha_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Toha surasini oyatlarini tanlang</b>", reply_markup=toha_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Toha surasini oyatlarini tanlang</b>", reply_markup=toha_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Toha surasini oyatlarini tanlang</b>", reply_markup=toha_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Toha surasini oyatlarini tanlang</b>", reply_markup=toha_keybord6)
        elif int(callback_data['items']) <= 112:
            await call.message.answer(f"<b>Toha surasini oyatlarini tanlang</b>", reply_markup=toha_keybord7)
        elif int(callback_data['items']) <= 128:
            await call.message.answer(f"<b>Toha surasini oyatlarini tanlang</b>", reply_markup=toha_keybord8)
        elif int(callback_data['items']) <= 135:
            await call.message.answer(f"<b>Toha surasini oyatlarini tanlang</b>", reply_markup=toha_keybord9)

    except:
        pass