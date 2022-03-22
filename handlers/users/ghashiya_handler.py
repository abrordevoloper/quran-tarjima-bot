from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.ghashiya_keybord import (ghashiya_keybords,
ghashiya_keybord1,ghashiya_keybord2
                                               )
from keyboards.inline.callback_data import ghashiya_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Ghashiya')
async def show_ghashiya(message: Message):
    await message.answer(f"<b>Ghashiya surasini oyatlarini tanlang</b>",reply_markup=ghashiya_keybord1)

@dp.callback_query_handler(ghashiya_callback_data.filter())
async def show_ghashiya(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=ghashiya_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Ghashiya</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(88,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(88,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Ghashiya surasini oyatlarini tanlang</b>", reply_markup=ghashiya_keybord1)
        elif int(callback_data['items']) <= 26:
            await call.message.answer(f"<b>Ghashiya surasini oyatlarini tanlang</b>", reply_markup=ghashiya_keybord2)

    except:
        pass