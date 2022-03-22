from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.naml_keybord import (naml_keybords,
naml_keybord1,naml_keybord2,naml_keybord3,naml_keybord4,naml_keybord5,naml_keybord6)
from keyboards.inline.callback_data import naml_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Naml')
async def show_naml(message: Message):
    await message.answer(f"<b>Naml surasini oyatlarini tanlang</b>",reply_markup=naml_keybord1)

@dp.callback_query_handler(naml_callback_data.filter())
async def show_naml(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=naml_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Naml</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(27,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(27,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Naml surasini oyatlarini tanlang</b>", reply_markup=naml_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Naml surasini oyatlarini tanlang</b>", reply_markup=naml_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Naml surasini oyatlarini tanlang</b>", reply_markup=naml_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Naml surasini oyatlarini tanlang</b>", reply_markup=naml_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Naml surasini oyatlarini tanlang</b>", reply_markup=naml_keybord5)
        elif int(callback_data['items']) <= 93:
            await call.message.answer(f"<b>Naml surasini oyatlarini tanlang</b>", reply_markup=naml_keybord6)

    except:
        pass