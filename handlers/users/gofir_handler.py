from loader import dp
from aiogram.types import Message,CallbackQuery
from keyboards.inline.gofir_keybord import (gofir_keybords,gofir_keybord1,
gofir_keybord2,gofir_keybord3,gofir_keybord4,gofir_keybord5,gofir_keybord6)

from keyboards.inline.callback_data import gofir_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Gofir')
async def show_gofir(message: Message):
    await message.answer(f"<b>Gofir surasini oyatlarini tanlang</b>",reply_markup=gofir_keybord1)

@dp.callback_query_handler(gofir_callback_data.filter())
async def show_gofir(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=gofir_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Gofir</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(40,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(40,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Gofir surasini oyatlarini tanlang</b>", reply_markup=gofir_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Gofir surasini oyatlarini tanlang</b>", reply_markup=gofir_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Gofir surasini oyatlarini tanlang</b>", reply_markup=gofir_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Gofir surasini oyatlarini tanlang</b>", reply_markup=gofir_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Gofir surasini oyatlarini tanlang</b>", reply_markup=gofir_keybord5)
        elif int(callback_data['items']) <= 85:
            await call.message.answer(f"<b>Gofir surasini oyatlarini tanlang</b>", reply_markup=gofir_keybord6)

    except:
        pass