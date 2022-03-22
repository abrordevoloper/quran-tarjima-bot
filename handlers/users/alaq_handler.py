from loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.alaq_keybord import (alaq_keybord1,alaq_keybords,alaq_keybord2)
from keyboards.inline.callback_data import alaq_callback_data
import logging
from .surah import oyat_tarjima, oyat_audio


@dp.message_handler(text_contains='Alaq')
async def show_alaq(message: Message):
    await message.answer(f"<b>Alaq surasini oyatlarini tanlang</b>", reply_markup=alaq_keybord1)


@dp.callback_query_handler(alaq_callback_data.filter())
async def show_alaq(call: CallbackQuery, callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=alaq_keybords[callback_data['items']])
    else:
        await call.message.answer(
            f"📖 <b>Alaq</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(96, int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(96, int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Alaq surasini oyatlarini tanlang</b>", reply_markup=alaq_keybord1)
        elif int(callback_data['items']) <= 19:
            await call.message.answer(f"<b>Alaq surasini oyatlarini tanlang</b>", reply_markup=alaq_keybord2)

    except:
        pass