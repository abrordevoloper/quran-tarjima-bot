from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.qalam_keybord import (qalam_keybords,
qalam_keybord1,qalam_keybord2,qalam_keybord3,qalam_keybord4)
from keyboards.inline.callback_data import qalam_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Qalam')
async def show_qalam(message: Message):
    await message.answer(f"<b>Qalam surasini oyatlarini tanlang</b>",reply_markup=qalam_keybord1)

@dp.callback_query_handler(qalam_callback_data.filter())
async def show_qalam(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=qalam_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Qalam</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(68,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(68,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Qalam surasini oyatlarini tanlang</b>", reply_markup=qalam_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Qalam surasini oyatlarini tanlang</b>", reply_markup=qalam_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Qalam surasini oyatlarini tanlang</b>", reply_markup=qalam_keybord3)
        elif int(callback_data['items']) <= 52:
            await call.message.answer(f"<b>Qalam surasini oyatlarini tanlang</b>", reply_markup=qalam_keybord4)

    except:
        pass