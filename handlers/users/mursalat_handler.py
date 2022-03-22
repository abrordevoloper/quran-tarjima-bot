from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.mursalat_keybord import (mursalat_keybords,
mursalat_keybord1,mursalat_keybord2,mursalat_keybord3,mursalat_keybord4)
from keyboards.inline.callback_data import mursalat_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Mursalat')
async def show_mursalat(message: Message):
    await message.answer(f"<b>Mursalat surasini oyatlarini tanlang</b>",reply_markup=mursalat_keybord1)

@dp.callback_query_handler(mursalat_callback_data.filter())
async def show_mursalat(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=mursalat_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Mursalat</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(77,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(77,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Mursalat surasini oyatlarini tanlang</b>", reply_markup=mursalat_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Mursalat surasini oyatlarini tanlang</b>", reply_markup=mursalat_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Mursalat surasini oyatlarini tanlang</b>", reply_markup=mursalat_keybord3)
        elif int(callback_data['items']) <= 50:
            await call.message.answer(f"<b>Mursalat surasini oyatlarini tanlang</b>", reply_markup=mursalat_keybord4)

    except:
        pass