from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.ibrohim_keybord import (ibrohim_keybords,
ibrohim_keybord1,ibrohim_keybord2,ibrohim_keybord3,ibrohim_keybord4)

from keyboards.inline.callback_data import ibrohim_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Ibrohim')
async def show_ibrohim(message: Message):
    await message.answer(f"<b>Ibrohim surasini oyatlarini tanlang</b>",reply_markup=ibrohim_keybord1)

@dp.callback_query_handler(ibrohim_callback_data.filter())
async def show_ibrohim(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=ibrohim_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Ibrohim</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(14,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(14,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Ibrohim surasini oyatlarini tanlang</b>", reply_markup=ibrohim_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Ibrohim surasini oyatlarini tanlang</b>", reply_markup=ibrohim_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Ibrohim surasini oyatlarini tanlang</b>", reply_markup=ibrohim_keybord3)
        elif int(callback_data['items']) <= 52:
            await call.message.answer(f"<b>Ibrohim surasini oyatlarini tanlang</b>", reply_markup=ibrohim_keybord4)

    except:
        pass