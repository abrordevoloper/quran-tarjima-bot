from loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.mumtahina_keybord import (mumtahina_keybord1
                                            )
from keyboards.inline.callback_data import hadid_callback_data
import logging
from .surah import oyat_tarjima, oyat_audio


@dp.message_handler(text_contains='Mumtahina')
async def show_mumtahina(message: Message):
    await message.answer(f"<b>Mumtahina surasini oyatlarini tanlang</b>", reply_markup=mumtahina_keybord1)


@dp.callback_query_handler(hadid_callback_data.filter())
async def show_mumtahina(call: CallbackQuery, callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    else:

        await call.message.answer(
            f"📖 <b>Mumtahina</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(60, int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(60, int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
        await call.message.answer(f"<b>Mumtahina surasini oyatlarini tanlang</b>",reply_markup=mumtahina_keybord1)
        