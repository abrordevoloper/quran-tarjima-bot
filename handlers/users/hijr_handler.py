from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.hijr_keybord import (hijr_keybords,
hijr_keybord1,hijr_keybord2,hijr_keybord3,hijr_keybord4,hijr_keybord5,hijr_keybord6,hijr_keybord7)
from keyboards.inline.callback_data import hijr_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Hijr')
async def show_hijr(message: Message):
    await message.answer(f"<b>Hijr surasini oyatlarini tanlang</b>",reply_markup=hijr_keybord1)

@dp.callback_query_handler(hijr_callback_data.filter())
async def show_hijr(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=hijr_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Hijr</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(15,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(15,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Hijr surasini oyatlarini tanlang</b>", reply_markup=hijr_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Hijr surasini oyatlarini tanlang</b>", reply_markup=hijr_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Hijr surasini oyatlarini tanlang</b>", reply_markup=hijr_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Hijr surasini oyatlarini tanlang</b>", reply_markup=hijr_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Hijr surasini oyatlarini tanlang</b>", reply_markup=hijr_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Hijr surasini oyatlarini tanlang</b>", reply_markup=hijr_keybord6)
        elif int(callback_data['items']) <= 99:
            await call.message.answer(f"<b>Hijr surasini oyatlarini tanlang</b>", reply_markup=hijr_keybord7)

    except:
        pass