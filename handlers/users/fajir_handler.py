from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.fajir_keybord import (fajir_keybords,
                                            fajir_keybord1,fajir_keybord2
                                            )
from keyboards.inline.callback_data import fajir_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Fajir')
async def show_fajir(message: Message):
    await message.answer(f"<b>Fajir surasini oyatlarini tanlang</b>",reply_markup=fajir_keybord1)

@dp.callback_query_handler(fajir_callback_data.filter())
async def show_fajir(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=fajir_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Fajir</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(89,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(89,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Fajir surasini oyatlarini tanlang</b>", reply_markup=fajir_keybord1)
        elif int(callback_data['items']) <= 30:
            await call.message.answer(f"<b>Fajir surasini oyatlarini tanlang</b>", reply_markup=fajir_keybord2)

    except:
        pass