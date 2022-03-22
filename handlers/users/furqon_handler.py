from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.furqon_keybord import (furqon_keybords,
furqon_keybord1,furqon_keybord2,furqon_keybord3,furqon_keybord4,furqon_keybord5)
from keyboards.inline.callback_data import furqon_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Furqon')
async def show_furqon(message: Message):
    await message.answer(f"<b>Furqon surasini oyatlarini tanlang</b>",reply_markup=furqon_keybord1)

@dp.callback_query_handler(furqon_callback_data.filter())
async def show_furqon(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=furqon_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Furqon</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(25,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(25,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Furqon surasini oyatlarini tanlang</b>", reply_markup=furqon_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Furqon surasini oyatlarini tanlang</b>", reply_markup=furqon_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Furqon surasini oyatlarini tanlang</b>", reply_markup=furqon_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Furqon surasini oyatlarini tanlang</b>", reply_markup=furqon_keybord4)
        elif int(callback_data['items']) <= 77:
            await call.message.answer(f"<b>Furqon surasini oyatlarini tanlang</b>", reply_markup=furqon_keybord5)

    except:
        pass