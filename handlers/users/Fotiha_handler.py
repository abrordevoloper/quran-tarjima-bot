from loader import dp
from aiogram.types import Message,CallbackQuery
from keyboards.inline.Fotiha_keybord import fotiha_keybord
from keyboards.inline.callback_data import fotiha_callback_data

import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Fotiha')
async def show_fotiha(message: Message):
    await message.answer(f"<b>Fotiha surasini oyatlarini tanlang</b>",reply_markup=fotiha_keybord)

@dp.callback_query_handler(fotiha_callback_data.filter(items='back1'))
async def back(call: CallbackQuery):
    await call.message.delete()

@dp.callback_query_handler(fotiha_callback_data.filter())
async def show_oyat(call: CallbackQuery,callback_data: dict):
    await call.message.answer(f"📖 <b>Fotiha</b> surasi <b>{callback_data['items']}-oyat</b>\n\n<i>{oyat_tarjima(1,int(callback_data['items']))}</i>\n")
    await call.message.answer_audio(oyat_audio(1,int(callback_data['items'])))
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer(f"<b>Fotiha surasini oyatlarini tanlang</b>",reply_markup=fotiha_keybord)

