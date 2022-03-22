from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.nahl_keybord import (nahl_keybords,
nahl_keybord1,nahl_keybord2,nahl_keybord3,nahl_keybord4,nahl_keybord5,nahl_keybord6,nahl_keybord7,nahl_keybord8)
from keyboards.inline.callback_data import nahl_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Nahl')
async def show_nahl(message: Message):
    await message.answer(f"<b>Nahl surasini oyatlarini tanlang</b>",reply_markup=nahl_keybord1)

@dp.callback_query_handler(nahl_callback_data.filter())
async def show_nahl(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=nahl_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Nahl</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(16,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(16,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Nahl surasini oyatlarini tanlang</b>", reply_markup=nahl_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Nahl surasini oyatlarini tanlang</b>", reply_markup=nahl_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Nahl surasini oyatlarini tanlang</b>", reply_markup=nahl_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Nahl surasini oyatlarini tanlang</b>", reply_markup=nahl_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Nahl surasini oyatlarini tanlang</b>", reply_markup=nahl_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Nahl surasini oyatlarini tanlang</b>", reply_markup=nahl_keybord6)
        elif int(callback_data['items']) <= 112:
            await call.message.answer(f"<b>Nahl surasini oyatlarini tanlang</b>", reply_markup=nahl_keybord7)
        elif int(callback_data['items']) <= 128:
            await call.message.answer(f"<b>Nahl surasini oyatlarini tanlang</b>", reply_markup=nahl_keybord8)

    except:
        pass