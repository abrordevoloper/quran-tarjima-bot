from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.muorij_keybord import (muorij_keybords,
muorij_keybord1,muorij_keybord2,muorij_keybord3)
from keyboards.inline.callback_data import muorij_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Muorij')
async def show_muorij(message: Message):
    await message.answer(f"<b>Muorij surasini oyatlarini tanlang</b>",reply_markup=muorij_keybord1)

@dp.callback_query_handler(muorij_callback_data.filter())
async def show_muorij(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=muorij_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Muorij</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(70,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(70,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Muorij surasini oyatlarini tanlang</b>", reply_markup=muorij_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Muorij surasini oyatlarini tanlang</b>", reply_markup=muorij_keybord2)
        elif int(callback_data['items']) <= 44:
            await call.message.answer(f"<b>Muorij surasini oyatlarini tanlang</b>", reply_markup=muorij_keybord3)

    except:
        pass