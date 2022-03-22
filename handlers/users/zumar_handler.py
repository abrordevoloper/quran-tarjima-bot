from loader import dp
from aiogram.types import Message,CallbackQuery
from keyboards.inline.zumar_keybord import (zumar_keybords,zumar_keybord1,
zumar_keybord2,zumar_keybord3,zumar_keybord4,zumar_keybord5)

from keyboards.inline.callback_data import zumar_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Zumar')
async def show_zumar(message: Message):
    await message.answer(f"<b>Zumar surasini oyatlarini tanlang</b>",reply_markup=zumar_keybord1)

@dp.callback_query_handler(zumar_callback_data.filter())
async def show_zumar(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=zumar_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Zumar</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(39,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(39,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Zumar surasini oyatlarini tanlang</b>", reply_markup=zumar_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Zumar surasini oyatlarini tanlang</b>", reply_markup=zumar_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Zumar surasini oyatlarini tanlang</b>", reply_markup=zumar_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Zumar surasini oyatlarini tanlang</b>", reply_markup=zumar_keybord4)
        elif int(callback_data['items']) <= 75:
            await call.message.answer(f"<b>Zumar surasini oyatlarini tanlang</b>", reply_markup=zumar_keybord5)

    except:
        pass