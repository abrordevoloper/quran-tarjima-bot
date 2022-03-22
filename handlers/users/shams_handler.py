from loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.shams_keybord import (shams_keybord1
                                            )
from keyboards.inline.callback_data import shams_callback_data
import logging
from .surah import oyat_tarjima, oyat_audio


@dp.message_handler(text_contains='Shams')
async def show_shams(message: Message):
    await message.answer(f"<b>Shams surasini oyatlarini tanlang</b>", reply_markup=shams_keybord1)


@dp.callback_query_handler(shams_callback_data.filter())
async def show_shams(call: CallbackQuery, callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    else:
        await call.message.answer(
            f"📖 <b>Shams</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(91, int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(91, int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
        await call.message.answer(f"<b>Shams surasini oyatlarini tanlang</b>", reply_markup=shams_keybord1)
