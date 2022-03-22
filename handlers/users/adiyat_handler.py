from loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.adiyat_keybord import (adiyat_keybord1)
from keyboards.inline.callback_data import adiyat_callback_data
import logging
from .surah import oyat_tarjima, oyat_audio


@dp.message_handler(text_contains='Adiyat')
async def show_adiyat(message: Message):
    await message.answer(f"<b>Adiyat surasini oyatlarini tanlang</b>", reply_markup=adiyat_keybord1)


@dp.callback_query_handler(adiyat_callback_data.filter())
async def show_adiyat(call: CallbackQuery, callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    else:
        await call.message.answer(
            f"📖 <b>Adiyat</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(100, int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(100, int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
        await call.message.answer(f"<b>Adiyat surasini oyatlarini tanlang</b>", reply_markup=adiyat_keybord1)
