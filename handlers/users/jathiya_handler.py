from loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.jathiya_keybord import (jathiya_keybords,
jathiya_keybord1,jathiya_keybord2,jathiya_keybord3)
from keyboards.inline.callback_data import jathiya_callback_data
import logging
from .surah import oyat_tarjima, oyat_audio


@dp.message_handler(text_contains='Jathiya')
async def show_jathiya(message: Message):
    await message.answer(f"<b>Jathiya surasini oyatlarini tanlang</b>", reply_markup=jathiya_keybord1)


@dp.callback_query_handler(jathiya_callback_data.filter())
async def show_jathiya(call: CallbackQuery, callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=jathiya_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Jathiya</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(45, int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(45, int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Jathiya surasini oyatlarini tanlang</b>", reply_markup=jathiya_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Jathiya surasini oyatlarini tanlang</b>", reply_markup=jathiya_keybord2)
        elif int(callback_data['items']) <= 37:
            await call.message.answer(f"<b>Jathiya surasini oyatlarini tanlang</b>", reply_markup=jathiya_keybord3)

    except:
        pass