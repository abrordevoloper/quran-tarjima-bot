from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.maida_keybord import (maida_keybords,
    maida_keybord1,maida_keybord2,maida_keybord3,maida_keybord4,maida_keybord5,
    maida_keybord6,maida_keybord7,maida_keybord8
    )
from keyboards.inline.callback_data import maida_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Maida')
async def show_maida(message: Message):
    await message.answer(f"<b>Maida surasini oyatlarini tanlang</b>",reply_markup=maida_keybord1)

@dp.callback_query_handler(maida_callback_data.filter())
async def show_maida(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=maida_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Maida</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(5,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(5,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Maida surasini oyatlarini tanlang</b>", reply_markup=maida_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Maida surasini oyatlarini tanlang</b>", reply_markup=maida_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Maida surasini oyatlarini tanlang</b>", reply_markup=maida_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Maida surasini oyatlarini tanlang</b>", reply_markup=maida_keybord4)
        elif int(callback_data['items']) <= 80:
            await call.message.answer(f"<b>Maida surasini oyatlarini tanlang</b>", reply_markup=maida_keybord5)
        elif int(callback_data['items']) <= 96:
            await call.message.answer(f"<b>Maida surasini oyatlarini tanlang</b>", reply_markup=maida_keybord6)
        elif int(callback_data['items']) <= 112:
            await call.message.answer(f"<b>Maida surasini oyatlarini tanlang</b>", reply_markup=maida_keybord7)
        elif int(callback_data['items']) <= 120:
            await call.message.answer(f"<b>Maida surasini oyatlarini tanlang</b>", reply_markup=maida_keybord8)

    except:
        pass