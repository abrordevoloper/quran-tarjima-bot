from loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.fil_keybord import (fil_keybord1)
from keyboards.inline.callback_data import fil_callback_data
import logging
from .surah import oyat_tarjima, oyat_audio


@dp.message_handler(text_contains='Fil')
async def show_fil(message: Message):
    await message.answer(f"<b>Fil surasini oyatlarini tanlang</b>", reply_markup=fil_keybord1)


@dp.callback_query_handler(fil_callback_data.filter())
async def show_fil(call: CallbackQuery, callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    else:
        await call.message.answer(
            f"📖 <b>Fil</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(105, int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(105, int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
        await call.message.answer(f"<b>Fil surasini oyatlarini tanlang</b>", reply_markup=fil_keybord1)