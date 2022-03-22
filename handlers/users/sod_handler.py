from loader import dp
from aiogram.types import Message,CallbackQuery
from keyboards.inline.sod_keybord import (sod_keybords,
sod_keybord1,sod_keybord2,sod_keybord3,sod_keybord4,sod_keybord5,sod_keybord6)

from keyboards.inline.callback_data import sod_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Sod')
async def show_sod(message: Message):
    await message.answer(f"<b>Sod surasini oyatlarini tanlang</b>",reply_markup=sod_keybord1)

@dp.callback_query_handler(sod_callback_data.filter())
async def show_sod(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=sod_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Sod</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(38,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(38,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Sod surasini oyatlarini tanlang</b>", reply_markup=sod_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Sod surasini oyatlarini tanlang</b>", reply_markup=sod_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Sod surasini oyatlarini tanlang</b>", reply_markup=sod_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Sod surasini oyatlarini tanlang</b>", reply_markup=sod_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Sod surasini oyatlarini tanlang</b>", reply_markup=sod_keybord5)
        elif int(callback_data['items']) <= 88:
            await call.message.answer(f"<b>Sod surasini oyatlarini tanlang</b>", reply_markup=sod_keybord6)

    except:
        pass