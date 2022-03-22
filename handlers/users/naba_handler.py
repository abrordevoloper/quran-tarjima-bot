from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.naba_keybord import (naba_keybords,
naba_keybord1,naba_keybord2,naba_keybord3)
from keyboards.inline.callback_data import naba_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Naba')
async def show_naba(message: Message):
    await message.answer(f"<b>Naba surasini oyatlarini tanlang</b>",reply_markup=naba_keybord1)

@dp.callback_query_handler(naba_callback_data.filter())
async def show_naba(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=naba_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Naba</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(78,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(78,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Naba surasini oyatlarini tanlang</b>", reply_markup=naba_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Naba surasini oyatlarini tanlang</b>", reply_markup=naba_keybord2)
        elif int(callback_data['items']) <= 40:
            await call.message.answer(f"<b>Naba surasini oyatlarini tanlang</b>", reply_markup=naba_keybord3)

    except:
        pass