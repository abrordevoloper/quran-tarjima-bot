from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.sajda_keybord import (sajda_keybords,
sajda_keybord1,sajda_keybord2)
from keyboards.inline.callback_data import sajda_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Sajda')
async def show_sajda(message: Message):
    await message.answer(f"<b>Sajda surasini oyatlarini tanlang</b>",reply_markup=sajda_keybord1)

@dp.callback_query_handler(sajda_callback_data.filter())
async def show_sajda(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=sajda_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Sajda</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(32,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(32,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Sajda surasini oyatlarini tanlang</b>", reply_markup=sajda_keybord1)
        elif int(callback_data['items']) <= 30:
            await call.message.answer(f"<b>Sajda surasini oyatlarini tanlang</b>", reply_markup=sajda_keybord2)

    except:
        pass